from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class GreenLightLoyaltyConfig(models.Model):
    _name = "greenlight.loyalty.config"
    _description = "Loyalty Program Configuration"

    name = fields.Char(required=True, default="Default Loyalty Program")
    is_active = fields.Boolean("Program Active", default=True)

    points_per_dollar = fields.Float(
        "Points per Dollar",
        digits=(10, 2),
        default=1.0,
        help="How many loyalty points the customer earns per dollar spent.",
    )
    redemption_ratio = fields.Float(
        "Redemption Ratio (Points per $1)",
        digits=(10, 2),
        default=100.0,
        help="How many points are needed to redeem $1 discount.",
    )
    min_points_to_redeem = fields.Integer(
        "Minimum Points to Redeem",
        default=100,
        help="Customer must have at least this many points before they can redeem.",
    )
    max_discount_pct = fields.Float(
        "Max Discount %",
        digits=(5, 2),
        default=50.0,
        help="Maximum percentage of the transaction that can be covered by loyalty discount.",
    )

    @api.constrains("points_per_dollar")
    def _check_points_per_dollar(self):
        for rec in self:
            if rec.points_per_dollar < 0:
                raise ValidationError("Points per dollar cannot be negative.")

    @api.constrains("redemption_ratio")
    def _check_redemption_ratio(self):
        for rec in self:
            if rec.redemption_ratio <= 0:
                raise ValidationError("Redemption ratio must be greater than zero.")

    @api.constrains("min_points_to_redeem")
    def _check_min_points(self):
        for rec in self:
            if rec.min_points_to_redeem < 0:
                raise ValidationError("Minimum points to redeem cannot be negative.")

    @api.constrains("max_discount_pct")
    def _check_max_discount_pct(self):
        for rec in self:
            if rec.max_discount_pct < 0 or rec.max_discount_pct > 100:
                raise ValidationError("Max discount percentage must be between 0 and 100.")

    # ------------------------------------------------------------------
    # Singleton accessor
    # ------------------------------------------------------------------

    @api.model
    def get_config(self):
        """Return the active loyalty config, or create a default one."""
        config = self.search([("is_active", "=", True)], limit=1)
        if not config:
            config = self.create({"name": "Default Loyalty Program"})
        return config

    # ------------------------------------------------------------------
    # Earn points
    # ------------------------------------------------------------------

    def earn_points(self, customer, transaction):
        """Calculate points from a confirmed transaction and credit them.

        Args:
            customer: greenlight.customer recordset (single)
            transaction: greenlight.transaction recordset (single)
        Returns:
            The created greenlight.loyalty.history record.
        """
        self.ensure_one()
        if not self.is_active:
            return self.env["greenlight.loyalty.history"]

        # Points earned = floor(transaction total * points_per_dollar)
        points = int(transaction.total * self.points_per_dollar)
        if points <= 0:
            return self.env["greenlight.loyalty.history"]

        new_balance = customer.loyalty_points + points
        customer.loyalty_points = new_balance

        history = self.env["greenlight.loyalty.history"].create({
            "customer_id": customer.id,
            "transaction_id": transaction.id,
            "points_change": points,
            "balance_after": new_balance,
            "event_type": "earn",
            "notes": f"Earned {points} pts on {transaction.name}",
        })
        return history

    # ------------------------------------------------------------------
    # Redeem points
    # ------------------------------------------------------------------

    def redeem_points(self, customer, points, transaction=None):
        """Deduct loyalty points from a customer as a discount.

        Args:
            customer: greenlight.customer recordset (single)
            points: positive integer — number of points to redeem
            transaction: optional greenlight.transaction recordset
        Returns:
            The created greenlight.loyalty.history record.
        Raises:
            UserError if validation fails.
        """
        self.ensure_one()
        if not self.is_active:
            raise UserError("The loyalty program is currently disabled.")

        if points <= 0:
            raise UserError("Points to redeem must be a positive number.")

        if customer.loyalty_points < self.min_points_to_redeem:
            raise UserError(
                f"Customer needs at least {self.min_points_to_redeem} points to redeem. "
                f"Current balance: {customer.loyalty_points}."
            )

        if points > customer.loyalty_points:
            raise UserError(
                f"Cannot redeem {points} points. Customer only has {customer.loyalty_points}."
            )

        # Enforce max discount percentage when a transaction is provided
        if transaction and self.redemption_ratio > 0:
            discount_dollars = points / self.redemption_ratio
            max_discount = transaction.total * (self.max_discount_pct / 100.0)
            if discount_dollars > max_discount:
                max_points = int(max_discount * self.redemption_ratio)
                raise UserError(
                    f"Discount would exceed {self.max_discount_pct}% of the transaction. "
                    f"Maximum redeemable: {max_points} points (${max_discount:.2f})."
                )

        new_balance = customer.loyalty_points - points
        customer.loyalty_points = new_balance

        txn_name = transaction.name if transaction else "N/A"
        history = self.env["greenlight.loyalty.history"].create({
            "customer_id": customer.id,
            "transaction_id": transaction.id if transaction else False,
            "points_change": -points,
            "balance_after": new_balance,
            "event_type": "redeem",
            "notes": f"Redeemed {points} pts on {txn_name}",
        })
        return history

    # ------------------------------------------------------------------
    # Customer history
    # ------------------------------------------------------------------

    @api.model
    def get_customer_history(self, customer_id):
        """Return all loyalty history records for a customer, newest first."""
        return self.env["greenlight.loyalty.history"].search(
            [("customer_id", "=", customer_id)],
            order="create_date desc",
        )


class GreenLightLoyaltyHistory(models.Model):
    _name = "greenlight.loyalty.history"
    _description = "Loyalty Points History"
    _order = "create_date desc"

    customer_id = fields.Many2one(
        "greenlight.customer",
        required=True,
        ondelete="cascade",
        index=True,
    )
    transaction_id = fields.Many2one(
        "greenlight.transaction",
        ondelete="restrict",
        string="Transaction",
    )
    employee_id = fields.Many2one(
        "greenlight.employee",
        string="Employee",
        ondelete="restrict",
        help="Employee who processed the adjustment (for manual adjustments).",
    )

    points_change = fields.Integer(
        "Points Change",
        required=True,
        help="Positive = earned, negative = redeemed/expired.",
    )
    balance_after = fields.Integer(
        "Balance After",
        required=True,
    )

    event_type = fields.Selection(
        [
            ("earn", "Earned"),
            ("redeem", "Redeemed"),
            ("adjust", "Manual Adjustment"),
            ("expire", "Expired"),
            ("bonus", "Bonus"),
        ],
        required=True,
    )

    notes = fields.Text()

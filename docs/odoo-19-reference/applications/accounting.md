# Accounting — Journals, Taxes, Payments & Reconciliation

> **Odoo 19.0 Reference**
> Source: www.odoo.com/documentation/19.0 — HTML converted via markdownify

## Purpose

Odoo Accounting: chart of accounts, journals, invoices, payments, bank reconciliation, taxes, fiscal positions, and multi-currency. Use when configuring or extending the accounting module.

---

# Accounting and Invoicing

Odoo Invoicing is a standalone app designed to create invoices, send them to customers, and manage
payments. It also handles flows involving vendor bills. On the other hand, the Accounting app is a
comprehensive accounting solution that allows the same actions and includes additional features such
as standard financial reports, bank reconciliation, budgets, asset management, and more.

> **Note:**
>
> [Odoo Tutorials: Accounting](https://www.odoo.com/slides/accounting-19)

[#### Get started

Basic concepts of accounting and initial setup of your accounting](accounting/get_started.html)[#### Taxes

Taxes, fiscal positions, and integrations](accounting/taxes.html)[#### Customer invoices

Customer invoices, payment terms, and electronic invoicing](accounting/customer_invoices.html)[#### Vendor bills

Vendor bills, assets, and invoice digitization (OCR)](accounting/vendor_bills.html)[#### Payments

Invoices and bills payments (online, checks, batches) and follow-up on invoices](accounting/payments.html)[#### Bank and cash accounts

Bank synchronization, reconciliation, and cash registers](accounting/bank.html)[#### Reporting

Reporting, declarations, and analytic accounting](accounting/reporting.html)

## Double-entry bookkeeping

Odoo automatically creates all the underlying journal entries for all accounting transactions (e.g.,
customer invoices, vendor bills, point-of-sales orders, expenses, inventory valuations, etc.).

Odoo uses the double-entry bookkeeping system, whereby every entry needs a corresponding and
opposite counterpart in a different account, with one account debited and the other credited.
It ensures that all transactions are recorded accurately and consistently and that the accounts
always balance.

> **Note:**
>
> [Accounting Cheat Sheet](accounting/get_started/cheat_sheet.html)

## Accrual and cash basis

Both accrual and cash basis accounting are supported in Odoo. This allows reporting income and
expense either when the transaction occurs (accrual basis) or when the payment is made or received
(cash basis).

> **Note:**
>
> [Cash basis](accounting/taxes/cash_basis.html)

## Multi-company

[Multiple companies](../general/companies/multi_company.html) can be managed within the same
database. Each company has its own [chart of accounts](accounting/get_started/chart_of_accounts.html), but [accounts can be shared](accounting/get_started/consolidation.html#consolidation-account-mapping), which is useful when viewing consolidation reports. Users can view
records and reports from multiple companies simultaneously but can only work on a single company’s
accounting at a time.

> **Note:**
>
> - [Multi-company](../general/companies/multi_company.html)
> - [Inter-company transactions](../general/companies/multi_company.html#general-multi-company-inter-company-transactions)

## Multi-currency environment

A [multi-currency](accounting/get_started/multi_currency.html) environment with an automated
exchange rate to ease international transactions is available in Odoo. Every transaction is recorded
in the company’s default currency; for transactions occurring in another currency, Odoo stores both
the value in the company’s currency and the transactions’ currency value. Odoo generates currency
gains and losses after reconciling the journal items.

> **Note:**
>
> [Manage a bank in a foreign currency](accounting/bank/foreign_currency.html)

## Branches

Parent [companies](../general/companies.html) and their [branches](../general/companies.html#general-companies-branches) can be managed within a single database, operating under shared
accounting and reporting rules, including the following:

- The parent company’s [chart of accounts](accounting/get_started/chart_of_accounts.html),
  [main currency](accounting/get_started/multi_currency.html), and [taxes](accounting/taxes.html)
  apply to all branches.
- Branches can manage their own dedicated journals and related records.
- The parent company manages a common [fiscal period](accounting/reporting/year_end.html#accounting-year-end-fiscal-years), so
  its [lock and closing dates](accounting/reporting/year_end.html#accounting-year-end-lock-everything-date) apply across all
  branches. However, branches may set earlier lock dates if needed.
- The parent company can access all [reports](accounting/reporting.html), [invoices](accounting/customer_invoices.html), [bills](accounting/vendor_bills.html), etc., from its branches,
  while each branch can only view its own data.

> **Note:**
>
> The [Fiscal localization](fiscal_localizations.html) package is set on the parent company.

> **Warning:**
>
> Adding a branch to a company enables [multi-company functions](../general/companies/multi_company.html).
>
> For more information, refer to [Odoo’s pricing page](https://www.odoo.com/pricing-plan) or
> contact your Odoo account manager.

### Reporting

The parent company consolidates accounting operations from all branches, providing a centralized
view of [financial reports](accounting/reporting.html), such as profit and loss or balance sheets.

### VAT

Each company and branch must be configured with its own legal information, including a VAT number
when applicable. Depending on the structure, branches may share the parent company’s VAT number or
have their own, resulting in a common or separate [VAT return](accounting/reporting/tax_returns.html).

This flexible setup allows users to generate individual reports and tax returns for each entity if
needed.

## International standards

Odoo Accounting supports over 100 countries and provides standardized features and mechanisms
applicable across all regions. Country-specific modules are included to comply with local accounting
regulations. [Fiscal localizations](fiscal_localizations.html) handle regional requirements, such
as charts of accounts, taxes, or any other legal obligations.

## Accounts receivable and payable

By default, one account is designated for accounts receivable entries and another for accounts
payable entries. As transactions are linked to **contacts**, it is possible to run a report per
customer, vendor, or supplier.

The **Partner Ledger** report displays the balance of customers and suppliers. To access it, go to
Accounting ‣ Reporting ‣ Partner Ledger.

## Reporting

The following financial [reports](accounting/reporting.html) are available and updated in
real-time:

| Financial reports | |
| --- | --- |
| Statement | Balance sheet |
| Profit and loss |
| Cash flow statement |
| Executive summary |
| Tax return |
| EC sales list |
| Audit | General ledger |
| Trial balance |
| Journal audit |
| Intrastat report |
| Check register |
| Partner | Partner ledger |
| Aged receivable |
| Aged payable |
| Management | Invoice analysis |
| Analytic report |
| Audit trail |
| Budget report |
| Unrealized currency gains/losses |
| Deferred revenue |
| Deferred expense |
| Depreciation schedule |
| Disallowed expenses |
| Loans analysis |
| Product margins |
| 1099 report |

> **Note:**
>
> [Create and customize reports](accounting/reporting/customize.html) with Odoo’s report engine.

### Tax return

In the [Tax return](accounting/reporting/tax_returns.html#accounting-tax-returns-report), Odoo computes all accounting transactions
for the specific tax period and uses these totals to calculate the tax obligation.

> **Note:**
>
> Depending on the country’s localization, an XML version of the tax report can be generated to be
> uploaded to the VAT platform of the relevant taxation authority.

## Bank synchronization

The bank synchronization system directly connects with banking institutions to automatically
import all transactions into the database. It gives an overview of the cash flow without logging
into an online banking system or waiting for paper bank statements.

> **Note:**
>
> [Bank synchronization](accounting/bank/bank_synchronization.html)

## Inventory valuation

Both periodic (manual) and perpetual (automated) inventory valuations are supported in Odoo. The
available methods are Standard Price, Average Cost (AVCO), and First In First Out (FIFO).

> **Note:**
>
> [Valuation cheat sheet](../inventory_and_mrp/inventory/inventory_valuation/cheat_sheet.html)

## Retained earnings

Retained earnings are the portion of income retained by a business. Odoo calculates current year
earnings in real-time, so no year-end journal or rollover is required. The profit
and loss balance is automatically reported on the balance sheet report.

> **Note:**
>
> [Accounting Cheat Sheet](accounting/get_started/cheat_sheet.html)

## Fiduciaries

The Accounting Firms mode can be activated by going to Accounting ‣
Configuration ‣ Settings. When enabled:

- The document’s sequence becomes editable on all documents;
- The Total (tax incl.) field appears to speed up and control the encoding by automating
  line creation with the right account and tax;
- Invoice Date and Bill Date are pre-filled when encoding a transaction.
- A Quick encoding option is available for customer invoices and vendor bills.

## Share invoices with external accountants

Odoo offers multiple ways to share invoices and bills with an external accountant, including
the abilities to [grant access rights] to your database,
to [automatically send copies of a journal’s invoices or bills] to a
specified email address, and to [download ZIP files] containing all invoices
and all bills.

### Accountant access rights

To grant access to the company’s accountant, [add the accountant as a new user](../general/users.html#users-add-individual) and configure the appropriate [access rights](../general/users/access_rights.html) in the Accounting section to enable access to the
company’s financial data:

- Accounting: Select Administrator.
- Bank: Allow bank account validation.

> **Note:**
>
> Adding an accountant as a new user in [Odoo Online](../../administration/odoo_online.html) is
> free if the accountant has an Odoo account registered with the same email address as the one
> listed for the company user. However, [Odoo.sh](../../administration/odoo_sh.html) and
> [Odoo On-premise](../../administration/on_premise.html) may involve extra charges for each
> additional user. For more pricing information, see
> [Odoo’s pricing](https://www.odoo.com/pricing-plan).

For a multi-company environment, set the appropriate [access](../general/users.html#users-multi-companies).

### Send copies of a journal’s invoices or bills

Sales and purchase type journals can be used to send all of their invoices and bills to external
email addresses. These records are sent in XML format.

To configure a journal to automatically send its records to a specified email address, follow these
steps:

1. Navigate to Accounting ‣ Configuration ‣ Journals.
2. Open the desired journal.
3. In the Advanced Settings tab, enter an email address in the Send Copy To
   field.

> **Note:**
>
> Multiple email addresses can be entered. Separate them with `;` without a space (i.e.:
> `sample1@example.com;sample2@example.com`).

### ZIP file export

Groups of invoices and bills can be exported in ZIP files. To export invoices or bills in ZIP files,
follow these steps:

1. Navigate to Accounting ‣ Customers ‣ Invoices or Accounting
   ‣ Vendors ‣ Bills.
2. Select the invoices or bills to be included in the ZIP file.
3. Click  Print menu, and click Export ZIP.

Once the ZIP file is exported, it can be sent to an external accountant to provide them with all the
information of your invoices and bills.

---

# Get started

When you first open your Odoo Accounting app, the Accounting Dashboard welcomes you with
a step-by-step onboarding banner, a wizard that helps you get started. This onboarding banner is
displayed until you choose to close it.

The settings visible in the onboarding banner can still be modified later by going to
Accounting ‣ Configuration ‣ Settings.

> **Note:**
>
> Odoo Accounting automatically installs the appropriate **Fiscal Localization Package** for your
> company, according to the country selected at the creation of the database. This way, the right
> accounts, reports, and taxes are ready-to-go. [Click here](../fiscal_localizations.html#fiscal-localizations-packages)
> for more information about Fiscal Localization Packages.

## Accounting onboarding banner

The step-by-step Accounting onboarding banner is composed of four steps:

![Step-by-step onboarding banner in Odoo Accounting](../../../_images/accounting-onboarding-banner.png)

1. [Accounting Periods]
2. [Bank Account]
3. [Taxes]
4. [Chart of Accounts]

### Accounting Periods

Define the **Fiscal Years**’ opening and closing dates, which are used to generate reports
automatically, and set your **Tax Return Periodicity**, along with a reminder to never miss a tax
return deadline.

By default, the opening date is set on the 1st of January and the closing date on the 31st of
December, as this is the most common use.

> **Note:**
>
> You can also change these settings by going to Accounting ‣ Configuration ‣
> Settings ‣ Fiscal Periods and updating the values.

### Bank Account

Connect your bank account to your database and have your bank statements synced automatically. To do
so, find your bank in the list, click Connect, and follow the instructions on-screen.

> **Note:**
>
> [Click here](bank/bank_synchronization.html) for more information about this feature.

If your Bank Institution can’t be synchronized automatically, or if you prefer not to sync it with
your database, you can also configure your bank account manually by typing its name, clicking
Create your Bank Account, and filling out the form.

- Name: the bank account’s name, as displayed in Odoo.
- Account Number: your bank account number (IBAN in Europe).
- Bank: click Create and edit to configure the bank’s details. Add the
  bank institution’s Name and its Identifier Code (BIC or SWIFT).
- Code: this code is your Journal’s Short Code, as displayed in Odoo.
  By default, Odoo creates a new Journal with this short code.
- Journal: This field is displayed if you have an existing bank journal that is not
  linked yet to a bank account. If so, then select the Journal you want to use to record
  the financial transactions linked to this bank account or create a new one by clicking
  Create and Edit.

> **Note:**
>
> - You can add as many bank accounts as needed with this tool by going to
>   Accounting ‣ Configuration ‣ Add a Bank Account.
> - [Click here](bank.html) for more information about Bank Accounts.

### Taxes

This menu allows you to create new taxes, (de)activate, or modify existing taxes. Depending on the
[localization package](../fiscal_localizations.html) installed on your database, taxes required for
your country are already configured.

> **Note:**
>
> [Click here](taxes.html) for more information about taxes.

### Chart of Accounts

With this menu, you can add accounts to your **Chart of Accounts** and indicate their initial
opening balances.

Basic settings are displayed on this page to help you review your Chart of Accounts. To access all
the settings of an account, click on the Setup button at the end of the line.

![Setup of the Chart of Accounts and their opening balances in Odoo Accounting](../../../_images/setup_chart_of_accounts.png)
> **Note:**
>
> [Click here](get_started/chart_of_accounts.html) for more information on how to configure your
> Chart of Accounts.

## Invoicing onboarding banner

There is another step-by-step onboarding banner that helps you take advantage of your Odoo Invoicing
and Accounting apps. The Invoicing onboarding banner is the one that welcomes you if you use the
Invoicing app rather than the Accounting app.

If you have Odoo Accounting installed on your database, you can reach it by going to
Accounting ‣ Customers ‣ Invoices.

The Invoicing onboarding banner consists of four main steps:

![Step-by-step onboarding banner in Odoo Invoicing](../../../_images/invoicing-onboarding-banner.png)

1. [Company Data]
2. [Documents Layout]
3. [Create Invoice]
4. [Online Payments]

### Company Data

Add your company’s details, such as the name, address, logo, website, phone number, email address,
and Tax ID or VAT number. These details are then displayed on your documents, such as invoices.

> **Note:**
>
> You can also change the company’s details by going to Settings ‣ General
> Settings, scrolling down to the Companies section, and Update Info.

### Documents Layout

Customize the [default invoice layout](../../studio/pdf_reports.html#studio-pdf-reports-default-layout).

> **Note:**
>
> You can also change the invoice layout by going to Settings ‣ General
> Settings, scrolling down to the Companies section, and clicking Configure
> Document Layout.

### Create Invoice

Create your first invoice.

> **Note:**
>
> Add your **bank account number** and a link to your **General Terms & Condition** in the footer.
> This way, your contacts can find the full content of your GT&C online without having to print
> them on the invoices you issue.

### Online Payments

Get started with Stripe and enable secure integrated credit and debit card payments within Odoo.

> **Note:**
>
> To use other payment providers, go to
> Invoicing –> Configuration –> Payment Providers and
> [enable the desired providers](../payment_providers.html).

> **Note:**
>
> - [Bank and cash accounts](bank.html)
> - [Chart of accounts](get_started/chart_of_accounts.html)
> - [Consolidation](get_started/consolidation.html)
> - [Bank synchronization](bank/bank_synchronization.html)
> - [Fiscal localizations](../fiscal_localizations.html)
> - [Odoo Tutorials: Accounting and Invoicing - Getting started [video]](https://www.odoo.com/slides/slide/getting-started-7063)

---

# Accounting cheat sheet

The **Balance Sheet** is a snapshot of the company’s finances at a specific date (as opposed to
the Profit and Loss, which is an analysis over a period).

- **Assets** represent the company’s wealth and the goods it owns. Fixed assets include buildings
  and offices, while current assets include bank accounts and cash. The money owed by a client is
  an asset. An employee is not an asset.
- **Liabilities** are obligations from past events that the company will have to pay in the
  future (utility bills, debts, unpaid suppliers). Liabilities could also be defined as a source
  of financing which is provided to the company, also called *leverage*.
- **Equity** is the amount of the funds contributed by the owners of the company (founders or
  shareholders) plus previously retained earnings (or losses). Each year, net profits (or losses)
  may be reported as retained earnings or distributed to the shareholders (as a dividend).

What is owned (an asset) has been financed through debts to reimburse (liabilities) or equity
(profits, capital).

A difference is made between **assets** and **expenses**:
:   - An **asset** is a resource with economic value that an individual, corporation, or country owns
      or controls with the expectation that it will provide a future benefit. Assets are reported on
      a company’s balance sheet. They are bought or created to increase a firm’s value or benefit its
      operations.
    - An **expense** is the costs of operations a company bears to generate revenues.

The **profit and loss** (P&L) report shows the company’s performance over a specific period of
time, usually a quarter or a fiscal year.

> - The **revenue** refers to the money earned by the company by selling goods and/or services.
> - The **cost of goods sold** (COGS, or also known as “Cost of Sale”) refers to the sale of
>   goods’ costs (e.g., the cost of the materials and labor used to create the goods).
>
>   - The **Gross profit** equals the revenues from sales minus the cost of goods sold.
>   - **Operating expenses** (OPEX) include administration, sales and R&D salaries, rent and
>     utilities, miscellaneous costs, insurances, and anything beyond the costs of products sold
>     or the cost of sale.

> Assets = Liabilities + Equity

## Chart of accounts

The **chart of accounts** lists all the company’s accounts: both Balance sheet accounts and P&L
accounts. Every transaction is recorded by debiting and crediting multiple accounts in a journal
entry. In a way, a chart of accounts is like a company’s DNA!

Every account listed in the chart of accounts belongs to a specific category. In Odoo, each account
has a unique code and belongs to one of these categories:

- **Equity and subordinated debts**
  :   - **Equity** is the amount of money invested by a company’s shareholders to finance the
        company’s activities.
      - **Subordinated debts** are the amount of money lent by a third party to a company to finance
        its activities. In the event of the dissolution of a company, these third parties are
        reimbursed before the shareholders.
- **Fixed assets** are tangible (i.e., physical) items or properties that a company purchases and
  uses to produce its goods and services. Fixed assets are long-term assets. This means the assets
  have a useful life of more than one year. They also include properties, plants, and equipments
  (also known as “PP&E”) and are recorded on the balance sheet with that classification.
- **Current assets and liabilities**
  :   - The **current assets** account is a balance sheet line item listed under the Assets section,
        which accounts for all company-owned assets that can be converted to cash within one year.
        Current assets include cash, cash equivalents, accounts receivable, stock inventory,
        marketable securities, prepaid liabilities, and other liquid assets.
      - **Current liabilities** are a company’s short-term financial obligations due within one year.
        An example of a current liability is money owed to suppliers in the form of accounts payable.
- **Bank and cash accounts**
  :   - A **bank account** is a financial account maintained by a bank or other financial institution
        in which the financial transactions between the bank and a customer are recorded.
      - A **cash account**, or cash book, may refer to a ledger in which all cash transactions are
        recorded. The cash account includes both the cash receipts and the cash payment journals.
- **Expenses and income**
  :   - An **expense** is the costs of operations a company bears to generate revenues. It is simply
        defined as the cost one is required to spend on obtaining something. Common expenses include
        supplier payments, employee wages, factory leases, and equipment depreciation.
      - The term “**income**” generally refers to the amount of money, property, and other transfers
        of value received over a set period of time in exchange for services or products.

### Example

\*: Customer Refund and Customer Payment boxes cannot be simultaneously selected as they are contradictory.

> Balance = Debit - Credit

## Journal entries

Every financial document of the company (e.g., an invoice, a bank statement, a pay slip, a capital
increase contract) is recorded as a journal entry, impacting several accounts.

For a journal entry to be balanced, the sum of all its debits must be equal to the sum of all its
credits.

examples of accounting entries for various transactions. (see entries.js)

## Reconciliation

[Reconciliation](../bank/reconciliation.html) is the process of linking
journal items of a specific account and matching credits and debits.

Its primary purpose is to link payments to their related invoices to mark them as paid. This is done
by doing a reconciliation on the accounts receivable account and/or the accounts payable account.

Reconciliation is performed automatically by the system when:

- the payment is registered directly on the invoice
- the links between the payments and the invoices are detected at the bank matching process

#### Customer Statement Example

| Accounts Receivable | Debit | Credit |
| --- | --- | --- |
| Invoice 1 | 100 |  |
| Partial payment 1/2 |  | 70 |
| Invoice 2 | 65 |  |
| Partial payment 2/2 |  | 30 |
| Payment 2 |  | 65 |
| Invoice 3 | 50 |  |
|  |  |  |
| Total to pay | 50 |  |

## Bank Reconciliation

Bank reconciliation is the matching of bank statement lines (provided by your bank) with
transactions recorded internally (payments to suppliers or from customers). For each line in a bank
statement, it can be:

- **matched with a previously recorded payment**: a payment is registered when a check is received
  from a customer, then matched when checking the bank statement.
- **recorded as a new payment**: the payment’s journal entry is created and reconciled with the
  related invoice when processing the bank statement.
- **recorded as another transaction**: bank transfer, direct charge, etc.

Odoo should automatically reconcile most transactions; only a few should need manual review. When
the bank reconciliation process is finished, the balance on the bank account in Odoo should match
the bank statement’s balance.

## Checks Handling

There are two approaches to managing checks and internal wire transfers:

- Two journal entries and a reconciliation
- One journal entry and a bank reconciliation

The first journal entry is created by registering the payment on the
invoice. The second one is created when registering the bank statement.

| Account | Debit | Credit | Reconciliation |
| --- | --- | --- | --- |
| Account Receivable |  | 100 | Invoice ABC |
| Undeposited funds | 100 |  | Check 0123 |

| Account | Debit | Credit | Reconciliation |
| --- | --- | --- | --- |
| Undeposited funds |  | 100 | Check 0123 |
| Bank | 100 |  |  |

A journal entry is created by registering the payment on the invoice. When
reconciling the bank statement, the statement line is linked to the
existing journal entry.

| Account | Debit | Credit | Reconciliation | Bank Statement |
| --- | --- | --- | --- | --- |
| Account Receivable |  | 100 | Invoice ABC |  |
| Bank | 100 |  |  | Statement XYZ |

---

# Chart of accounts

The **chart of accounts (COA)** is the list of all the accounts used to record financial
transactions in the general ledger of an organization. The chart of accounts can be found under
Accounting ‣ Configuration ‣ Chart of Accounts.

When browsing your chart of accounts, you can sort the accounts by Code,
Account Name, or Type, but other options are available in the drop-down menu

![Drop-down toggle button](../../../../_images/drop-down.png)
![Group the accounts by type in Odoo Accounting](../../../../_images/chart-of-accounts-sort.png)

## Configuration of an account

The country you select during the creation of your database (or additional company in your database)
determines which [fiscal localization package](../../fiscal_localizations.html) is installed by
default. This package includes a standard chart of accounts already configured according to the
country’s regulations. You can use it directly or set it according to your company’s needs.

To create a new account, go to Accounting ‣ Configuration ‣ Chart of Accounts,
click Create, and fill in (at the minimum) the required fields
(Code, Account Name, Type).

> **Warning:**
>
> It is not possible to modify the **fiscal localization** of a company once a journal entry has
> been posted.

### Code and name

Each account is identified by its Code and Name, which also indicate the
account’s purpose.

### Type

Correctly configuring the **account type** is critical as it serves multiple purposes:

- Information on the account’s purpose and behavior
- Generate country-specific legal and financial reports
- Set the rules to close a fiscal year
- Generate opening entries

To configure an account type, open the Type field’s drop-down selector and select the
corresponding type from the following list:

| Report | Category | Account Types | Description |
| --- | --- | --- | --- |
| Balance Sheet | Assets | Receivable | Money owed to the company by customers for goods or services delivered |
| Bank and Cash | Funds held in company bank accounts or on hand as cash |
| Current Assets | Short-term assets expected to be converted into cash within a year |
| Non-current Assets | Long-term assets not expected to be converted to cash within a year |
| Prepayments | Payments made in advance for goods or services to be received in the future |
| Fixed Assets | Tangible long-term assets like buildings, machinery, and vehicles used in operation and subject to depreciation |
| Liabilities | Payable | Money the company owes to suppliers or vendors |
| Credit Card | Balances and transactions associated with company credit card usage |
| Current Liabilities | Obligations due within one year, such as short-term loans or accrued expenses |
| Non-current Liabilities | Long-term debts and financial obligations due beyond one year |
| Equity | Equity | The owner’s residual interest in the company after liabilities are deducted from assets |
| Current Year Earnings | The company’s net profit or loss accumulated in the current fiscal year |
| Profit & Loss | Income | Income | Revenue generated from the company’s primary business activities |
| Other Income | Revenue from secondary or non-operational sources, like interest or asset sales |
| Expense | Expense | Costs incurred during operations to generate revenue |
| Depreciation | The allocation of the cost of tangible assets over their useful life |
| Cost of Revenue | Direct costs attributable to the production or delivery of goods and services |
| Other | Other | Off-Balance Sheet | Transactions not displayed on the balance sheet or profit and loss report |

#### Assets

Some **account types** can **automate** the creation of [asset](../vendor_bills/assets.html#assets-automation) entries.
To **automate** entries, click View on an account line and go to the
Automation tab.

You have three choices for the Automation tab:

1. No: this is the default value. Nothing happens.
2. Create in draft: whenever a transaction is posted on the account, a draft entry is
   created but not validated. You must first fill out the corresponding form.
3. Create and validate: you must also select a Deferred Expense Model.
   Whenever a transaction is posted on the account, an entry is created and immediately validated.

### Default taxes

In the View menu of an account, select a **default tax** to be applied when this
account is chosen for a product sale or purchase.

### Tags

Some accounting reports require **tags** to be set on the relevant accounts. To add a tag, under
View, click the Tags field and select an existing tag or Create
a new one.

### Account groups

**Account groups** are useful to list multiple accounts as *sub-accounts* of a bigger account and
thus consolidate reports such as the **Trial Balance**. By default, groups are handled automatically
based on the code of the group. For example, a new account `131200` is going to be part of the group
`131000`. You can attribute a specific group to an account in the Group field under
View.

#### Create account groups manually

> **Note:**
>
> Regular users should not need to create account groups manually. The following section is only
> intended for rare and advanced use cases.

To create a new account group, activate [developer mode](../../../general/developer_mode.html#developer-mode) and head to
Accounting ‣ Configuration ‣ Account Groups. Here, create a new group and enter
the name, code prefix, and company to which that group account should be available. Note
that you must enter the same code prefix in both From and to fields.

![Account groups creation.](../../../../_images/account-groups.png)

To display your **Trial Balance** report with your account groups, go to
Accounting ‣ Reporting ‣ Trial Balance, then open the Options menu
and select Hierarchy and Subtotals.

![Account Groups in the Trial Balance in Odoo Accounting](../../../../_images/chart-of-accounts-groups.png)

### Allow reconciliation

To keep the reconciliation process simple, when reconciling a bank, cash, or credit card transaction
with an existing journal item, only journal items that debit or credit accounts with the
Allow reconciliation option enabled are displayed as possible matches.

To enable this option on an account, tick the Allow Reconciliation checkbox in the
account’s settings, and Save; or enable the button from the chart of accounts view.

### Shared Accounts

The **Shared Accounts** feature allows the creation of a single account for a specific purpose and
sharing it between multiple companies. It is especially useful for multi-company environments where
a similar account might be used across different companies.

### Deprecated

It is not possible to delete an account once a transaction has been recorded on it. You can make
them unusable by using the **Deprecated** feature: check the Deprecated box in the
account’s settings, and Save.

> **Note:**
>
> - [Accounting cheat sheet](cheat_sheet.html)
> - [Non-current assets and fixed assets](../vendor_bills/assets.html)
> - [Deferred expenses](../vendor_bills/deferred_expenses.html)
> - [Deferred revenues](../customer_invoices/deferred_revenues.html)
> - [Fiscal localizations](../../fiscal_localizations.html)
> - [Odoo Tutorials: Chart of accounts](https://www.odoo.com/slides/slide/chart-of-accounts-6834)
> - [Odoo Tutorials: Update your chart of accounts](https://www.odoo.com/slides/slide/update-your-chart-of-accounts-6391)

---

# Consolidation

Consolidation allows combining financial data from **multiple separate companies**, each with its
own books, into a unified view, providing a “fair image” of the entire group’s financial health.

It helps create a clear, comprehensive view of the group’s financial performance by combining data
from multiple companies.

> **Note:**
>
> Consolidating companies involves **legally separate entities**, whereas [branches](../../../general/companies.html#general-branches) are **subdivisions** of a single legal entity which often share the
> head office’s resources (journals, taxes, accounts, fiscal positions) and are not consolidated in
> the same way.

## Consolidation tools

**Several tools** combined together will contribute to the construction of the financial
consolidation:

1. **Account Mapping:** Similar accounts from different companies can be mapped together. This
   allows Odoo to combine them correctly in consolidated reports. To map accounts, go to
   Accounting ‣ Configuration ‣ Chart of Accounts. Click View
   on the account line. In the Mapping tab, enter a code in the corresponding company
   Code column to map the account.

   ![Mapping different codes to different companies.](../../../../_images/multi_company_mapping.png)
   > **Note:**
   >
   > [Import mapping] or merge existing
   > accounts using the [merging tool] can simplify the process.

   When multiple accounts from one company are mapped to a single account in another, it is then
   possible to group the multiple accounts into a single line in the other company’s reporting by
   [grouping by](../reporting/customize.html#customize-reports-lines-group-by) the *account code* (`account_code`) rather
   than the *account ID* (`account_id`).

   > **Note:**
   >
   > Some reports, such as the [profit and loss](../reporting.html#accounting-reporting-profit-and-loss), split
   > the lines into different sections by account type. When these reports are grouped by account
   > code, the section splits are maintained, but within each section, line grouping by account
   > code is respected.

   > **Tip:**
   >
   > Belgian Company is a parent company with a subsidiary, American Company. American Company has
   > five income accounts:
   >
   > - 400000 Product Sales - Domestic
   > - 400100 Product Sales - International
   > - 410000 Service Revenue - Consulting
   > - 420000 Subscription Revenue
   > - 430000 Freight & Handling Revenue
   >
   > All five of the US income accounts correspond to one single income account (700000 Income) in
   > the Belgian Company.
   >
   > For the Belgian Company’s profit and loss report to show one line for all of the American
   > Company’s combined income accounts related to the Belgian Company’s single income account, all
   > five income accounts from the American Company must be mapped to The Belgian Company’s 700000
   > Income account, and the report’s lines must be [grouped by](../reporting/customize.html#customize-reports-lines-group-by) the account code.
2. **Multi-Ledgers:** Ledgers are fundamental to the process of consolidation. They are either:

   - *Regular Ledgers:* Each company in the consolidation scope has its own standard accounting
     ledger where all the regular day-to-day transactions are recorded. It excludes the company’s
     consolidation adjustment journals.
   - *Multi-Ledger for Consolidation:* The company doing the actual consolidation also has a
     special multi-ledger. This one includes all the other companies’ consolidation adjustments
     journals (the ones excluded from their own ledgers). This allows for viewing the total impact
     of all the adjustments.

   To create a new ledger, go to Accounting ‣ Configuration ‣ Multi-Ledgers
   and hit the New button. Enter a name, pick the company the ledger is linked to and
   most importantly, determine which journals are to be excluded from the ledger.
3. **Multi-Company Selector:** The consolidated view can be accessed using the multi-company
   :   selector. Selecting the consolidating company as the current company and making the other
       companies visible in the selector, all the journal items are displayed from the consolidating
       company’s perspective.

   ![Selecting the main company and activating others.](../../../../_images/multi_company_selector.png)
4. **Horizontal Groups:** Odoo’s reporting tools allow for combining multi-ledgers and using
   :   horizontal groups to view the consolidated Balance Sheet or P&L. They also show how much each
       company contributes to the overall consolidated figures.

       Follow these steps to create an Horizontal Group:

       - Activate the [developer mode](../../../general/developer_mode.html#developer-mode).
       - Go to Accounting ‣ Configuration ‣ Horizontal Groups and click
         New.
       - Add a Group Name and select the Reports where the horizontal group
         can be used.
       - In the Field column, click Add a line.
       - In the Create rules window, add a Field and create a new
         Domain rule if needed. Then, click Save & Close.

   ![Using horizontal groups to see each company's contribution.](../../../../_images/horizontal_groups.png)
   > **Warning:**
   >
   > When opened, financial reports usually default to a statutory view, using the company’s
   > regular ledger (including its consolidation adjustment). To see the full consolidation picture,
   > **make sure to select the multi-ledger** that includes all the consolidation adjustments.
5. **Cumulative Translation Adjustments:** When consolidating companies with different currencies,
   Odoo handles the translation.

   - *Equity accounts:* Use the historical exchange rate.
   - *Profit & Loss (P&L) accounts:* Use the average exchange rate.
   - *Balance sheet accounts (excluding equity):* Use the closing exchange rate.
   > **Warning:**
   >
   > The rates used are those of the company currently selected.

## Account merging

Accounts can be merged to reduce the number of accounts and standardize them across companies. This
is optional; consolidation works without it.

To use the merge tool, select all the companies with an account that needs to be merged in the
company selector in the top right corner of the screen.

![Selecting all companies that have accounts to be merged.](../../../../_images/shared_accounts_merge_tool_select_companies.png)

Then, go to Accounting ‣ Configuration ‣ Chart of Accounts and select the
accounts to merge. Click the  Actions menu and select Merge
accounts.

In the Merge accounts window, enable the Group by name? option if needed and
click Merge.

The selected accounts are then merged into a single shared account, accessible by all the chosen
companies, just as if the account had been directly created to be shared.

## Account unmerging

Accounts can also be unmerged if needed.

> **Warning:**
>
> Note that unmerging accounts **will not unmerge the chatters** of the accounts. Once merged, the
> changes’ histories are permanently merged.

To unmerge accounts, select a company with a shared account in the company selector at the top
right corner of the screen. Then, go to Accounting ‣ Configuration ‣ Chart of
Accounts and select the account to unmerge. Click the  Actions menu and
select Unmerge accounts.

An Odoo Warning confirmation pop-up window will appear, listing how the accounts will
be split.

![Confirmation wizard for the Unmerge Tool of the shared accounts feature.](../../../../_images/shared_accounts_unmerge_tool_confirmation_wizard.png)

Click Unmerge. A new account linked to each company will be created for the previously
shared account.

## Import a mapping

To **import an account mapping**, select all the related companies in the company selector at the
top right corner of the screen and go to Accounting ‣ Configuration ‣ Chart of
Accounts.

First, to choose the fields to export, select the accounts, click the
Actions button and select Export. Then, in the Export data
window, add the Code mapping/Code, Code Mapping/Company and
External ID fields using the  icon and click Export. No other
field is required.

Second, rework it in a spreadsheet adding the desired code for each company on desired accounts.

Third, to reimport the file (xlsx or csv format) in Odoo, click Import and, in the
Import Chart of Accounts section, click Import CoA. In the
Accounting Import Guide, drop or click Upload Data File to import the file.
Then, click Import.

Finally, the codes now take into account the mapping company per company.

---

# Journals

Journal entries are recorded in different **journals** to maintain an organized record of a
company’s financial transactions. Odoo uses six different types of journals to organize accounting
records:

- [Bank]
- [Cash]
- [Credit Card]
- [Sales]
- [Purchase]
- [Miscellaneous]

> **Note:**
>
> It is possible to have multiple journals of the same type, such as two separate bank journals,
> each for a unique bank account, or two separate sales journals to track B2B versus B2C income.

Each card on the Accounting Dashboard represents a journal. To edit the configuration of
a journal, click the  (vertical ellipsis) on the journal card, then
click Configuration. Alternatively, go to Accounting ‣ Configuration
‣ Journals to select and edit an existing journal or to create a new one.

While different journal types have slightly different fields to configure, some fields are
consistent across all the journal types:

- Short Code: Each journal must have a unique code (from 1 to 5 characters long). The
  short code is used as the prefix for all journal entries belonging to this journal.
- Currency: If desired, set the currency of this journal. For bank and cash journals,
  this is the currency of the journal’s [transactions](../bank/transactions.html). This field is
  only visible when [multiple currencies](multi_currency.html) are enabled.

The Advanced Settings tab contains more technical options:

- Allowed accounts: Limit which accounts are available when recording journal entries in
  this journal. Leave this field blank to allow all accounts.
- Email Alias: Set an email address to create journal entries by digitizing PDFs sent
  to this address. This is most commonly used to create [customer invoices and vendor bills](../vendor_bills/invoice_digitization.html#accounting-bill-digitization-email-alias).
- Secure Posted Entries with Hash: Restrict the [alterability](../reporting/data_inalterability.html) of this journal’s entries to comply with tax authorities in
  certain countries.

> **Warning:**
>
> The Secure Posted Entries with Hash option cannot be removed from a journal once the
> journal has a posted journal entry.

> **Note:**
>
> - Bank and cash journals do not have the Secure Posted Entries with Hash or
>   Email Alias fields.
> - If an [alias domain](../../../general/email_communication/email_servers_inbound.html#email-inbound-custom-domain) has not yet been configured, a link to
>    Configure Alias Domain is displayed instead of the
>   Email Alias field.

## Bank, cash, and credit card journals

Bank, cash, and credit card journals share the following features:

- Suspense Account: [Transactions](../bank/transactions.html) on this journal are posted on this
  account until they are reconciled, at which point this account is replaced with the account the
  transaction was reconciled against. At any moment, the suspense account’s balance in the general
  ledger shows the balance of transactions that have not yet been reconciled.

  > **Note:**
  >
  > When a bank transaction is reconciled, the journal entry is modified to replace the bank
  > suspense account with the account of the journal item it is reconciled with. This account is
  > usually either:
  >
  > - the [outstanding receipts or payments account] if reconciling with a registered payment; or
  > - the account receivable or payable if reconciling with an invoice or bill directly.
- Dedicated Payment Sequence: Tick this field to use separate sequences for payments
  and transactions posted on this journal.

  > **Note:**
  >
  > If the Dedicated Payment Sequence field is ticked, payments that use an
  > [outstanding account] will have references that
  > add P before the journal’s short code. Otherwise, the references will begin with
  > PAY.

The Incoming Payments and Outgoing Payments tabs contain the [payment
methods](../payments.html#accounting-payments-payment-methods) of this journal. Different payment methods are
available depending on the journal type. If desired, set [outstanding accounts] on the payment methods.

> **Note:**
>
> - [Bank and cash accounts](../bank.html)
> - [Multi-currency system](multi_currency.html)
> - [Transactions](../bank/transactions.html)
> - [Bank configuration](https://www.youtube.com/watch?v=tVhhXw-VnGE)

### Outstanding accounts

By default, payments in Odoo do not create journal entries, but they can be configured to create
journal entries by using **outstanding accounts** on [bank] and
[cash] journals.

- An **outstanding receipts account** is where incoming payments are posted until they are linked
  with incoming bank transactions.
- An **outstanding payments account** is where outgoing payments are posted until they are linked
  with outgoing bank transactions.

These accounts are usually of [type](chart_of_accounts.html#chart-of-account-type) Current Assets and
Current Liabilities.

Payments that are registered in Odoo are posted to the outstanding receipts and outstanding payments
accounts until they are reconciled. At any moment, the outstanding receipts account’s balance in the
general ledger shows the balance of registered incoming payments that have not yet been reconciled,
and the outstanding payments account’s balance in the general ledger shows the balance of registered
outgoing payments that have not yet been reconciled.

#### Configuration

To configure outstanding accounts, go to Accounting ‣ Configuration ‣ Journals
and select or create a bank or cash journal. In the Incoming Payments and
Outgoing Payments tabs, set Outstanding Receipts accounts and
Outstanding Payments accounts for each payment method that you want to create journal
entries.

> **Note:**
>
> - If the main bank account of the journal is added as an outstanding receipts account or
>   outstanding payments account, when a payment is registered, the invoice or bill’s status is
>   directly set to Paid.
> - If the outstanding receipts or outstanding payments account for a payment method is left blank,
>   registering a payment with that payment method will not create any journal entry.

### Bank

Bank journals are used to record journal entries related to [bank transactions](../bank/transactions.html) and incoming and outgoing [payments](../payments.html). The following
fields are specific to bank journals:

- Bank Account: This Bank and Cash type account is the default account for
  this bank journal.
- Account Number: The bank account’s number is used when registering payments and is
  required for generating outgoing payment files, such as [SEPA](../payments/pay_sepa.html) or
  [NACHA](../../fiscal_localizations/united_states.html#l10n-us-nacha). To edit the bank account details, click on the
   (Internal link) button next to the Account Number
  and update the account information accordingly.
- Bank: The bank name is used when registering payments and is required for generating
  outgoing payment files. To edit the bank account details, click on the
  (Internal link) button next to the Bank name and update the account
  information accordingly.
- Bank Feeds: Define the method of creating bank [transactions](../bank/transactions.html), whether Manual or via [Online Synchronization](../bank/bank_synchronization.html).
- Split Transactions: Split collective payments for CODA files.

Multiple payment methods are available for bank journals, as are configurations for generating
outgoing payment files, such as [SEPA](../payments/pay_sepa.html) or [NACHA](../../fiscal_localizations/united_states.html#l10n-us-nacha).

### Cash

Cash journals are used to record journal entries related to cash [transactions](../bank/transactions.html). The following fields are specific to cash journals:

- Cash Account: This Bank and Cash type account is the default account for
  this cash journal.
- Profit Account: This Income or Other Income type account is
  used to register a profit when the ending balance of a cash register is greater than expected.
- Loss Account: This Expenses type account is used to register a loss when
  the ending balance of a cash register is less than expected.

Only manual payment methods are available for cash journals.

### Credit card

Credit card journals are used to record journal entries related to credit cards. The following
fields are specific to credit card journals:

- Journal Account: This Credit Card type account is the default account for
  this credit card journal.
- Bank Feeds: Define the method of creating credit card transactions, whether manual or
  via [Online Synchronization](../bank/bank_synchronization.html).

Only manual payment methods are available for credit card journals.

## Sales, purchase, and miscellaneous journals

### Sales

Sales journals, also known as income journals, are used to record journal entries related to
[customer invoices](../customer_invoices.html). The following fields are specific to customer
invoice journals:

- Default Income Account: Invoices in this journal use this Income or
  Other Income type account unless overwritten by another income account set on the
  product category, product, or invoice line itself.
- Dedicated Credit Note Sequence: Check this box to use a separate sequence for the
  reference of credit notes that increments separately from the main invoice sequence and adds an
  `R` to the reference before the journal’s short code.
- Dedicated Debit Note Sequence: Check this box to use a separate sequence for the
  reference of credit notes that increments separately from the main invoice sequence and adds a `D`
  before the journal’s short code.

Sales journals have additional fields in the Advanced Settings tab that allow you to set
the default communication format that will appear on customer invoices so that the customer can
refer to that particular invoice when making a payment:

- Communication Type: Choose if the format of the payment reference communicated to the
  customer should be based on the invoice number or the customer’s number.
- Communication Standard: Choose the format of the payment reference itself that is
  communicated to the customer.

### Purchase

Purchase journals are used to record journal entries related to [vendor bills](../vendor_bills.html). The following fields are specific to purchase journals:

- Default Expense Account: Vendor bills in this journal use this Expense
  type account unless overwritten by another expense account set on the product category, product,
  or expense.
- Private Part Account: Select the account to be used to register the private part of
  mixed expenses.
- Dedicated Credit Note Sequence: Check this box to use a separate sequence for the
  reference of credit notes that increments separately from the main vendor bill sequence and adds
  an `R` to the reference before the journal’s short code.
- Dedicated Debit Note Sequence: Check this box to use a separate sequence for the
  reference of credit notes that increments separately from the main invoice sequence and adds a `D`
  before the journal’s short code.

### Miscellaneous

Miscellaneous journals are used to record journal entries that are not related to any of the other
journal types such as tax closing journal entries.

> **Note:**
>
> - [Tax return eLearning](https://www.odoo.com/slides/slide/tax-return-10564)
> - [Tax return (VAT report)](../reporting/tax_returns.html)
> - [Taxes](../taxes.html)

---

# Multi-currency system

Odoo allows you to issue invoices, receive bills, and record transactions in currencies other than
the main currency configured for your company. You can also set up bank accounts in other currencies
and run reports on your foreign currency activities.

> **Note:**
>
> - [Manage a bank account in a foreign currency](../bank/foreign_currency.html)

## Configuration

### Main currency

The **main currency** is defined by default according to the company’s country. You can change it by
going to Accounting ‣ Configuration ‣ Settings ‣ Currencies and changing the
currency in the Main Currency setting.

### Enable foreign currencies

Go to Accounting ‣ Configuration ‣ Currencies, and enable the currencies you
wish to use by toggling the Active button.

![Enable the currencies you wish to use.](../../../../_images/enable-foreign-currencies.png)

### Currency rates

#### Manual update

To manually create and set a currency rate, go to Accounting ‣ Configuration ‣
Currencies, click on the currency you wish to change the rate of, and under the Rates
tab, click Add a line to create a new rate.

![Create or modify the currency rate.](../../../../_images/manual-rate-update.png)

#### Automatic update

When you activate a second currency for the first time, Automatic Currency Rates appears
under Accounting ‣ Configuration ‣ Settings in the Currencies
section. Click the  (Update now) icon to update the rates.

Rates can be updated at regular intervals automatically. To do so, change the
Interval from Manually to Daily, Weekly, or
Monthly. You can also select the web service from which you want to retrieve the latest
currency rates by clicking the Service field.

### Exchange difference entries

Odoo automatically records exchange differences entries on dedicated accounts, in a dedicated
journal.

To define which journal and accounts to use to post exchange difference entries, go to
Accounting ‣ Configuration ‣ Settings, scroll to the
Default Accounts section, and edit the Journal, the Gain and
Loss accounts.

> **Tip:**
>
> If you receive a payment for a customer invoice one month after it was issued, the exchange rate
> has likely changed since. Therefore, this fluctuation implies some profit or loss due to the
> exchange difference, which Odoo automatically records in the default **Exchange Difference**
> journal.

### Chart of accounts

Each account can have a set currency. By doing so, all moves relevant to the account are forced to
have that account’s currency.

To do so, go to Accounting ‣ Configuration ‣ Charts of Accounts and select a
currency in the field Currency. If left empty, all active currencies are handled
instead of just one.

### Journals

If a currency is set on a **journal**, that journal only handles transactions in that currency.

To do so, go to Accounting ‣ Configuration ‣ Journals, open the journal you
want to edit, and select a currency in the field Currency.

![Select the currency for the journal to handle.](../../../../_images/journal-currency.png)

## Multi-currency accounting

### Invoices, bills, and other documents

For all documents, you can select the currency and journal to use for the transaction on the
document itself.

![Select the currency and journal to use.](../../../../_images/currency-field.png)

### Payment registration

To register a payment in a currency other than your company’s main currency, click on the
Register Payment payment button of your document and, in the pop-up window, select a
**currency** in the Amount field.

![Select the currency and journal to use before registering the payment.](../../../../_images/register-payment.png)

### Bank transactions

When creating or importing bank transactions, the amount is in the company’s main currency. To input
a **foreign currency**, select a currency in the Foreign Currency. Once selected, enter
the Amount in your main currency for it to automatically get converted in the foreign
currency in the Amount in Currency field.

![The extra fields related to foreign currencies.](../../../../_images/foreign-fields.png)

When reconciling, Odoo displays both the foreign currency amount and the equivalent amount in your
company’s main currency.

### Exchange rate journal entries

To see **exchange difference journal entries**, go to
Accounting ‣ Review ‣ Journal Items. In the search bar, click the
 (down caret) icon and, in the Group By column, select
Miscellaneous.

![Exchange rate journal entry.](../../../../_images/exchange-journal-currency.png)

---

# Average price on returned goods

*Average cost valuation* (AVCO) is an inventory valuation method that evaluates cost based on the
total cost of goods bought or produced during a period, divided by the total number of items
on-hand. Inventory valuation is used to:

- reflect the value of a company’s assets;
- keep track of the amount of unsold goods;
- account for monetary value in goods that have yet to generate profit;
- report on flow of goods throughout the quarter.

Because AVCO uses the weighted average to evaluate the cost, it is a good fit for companies that
sell only a few different products in large quantities. In Odoo, this costing analysis is
*automatically updated* each time products are received.

Thus, when shipments are returned to their supplier, Odoo automatically generates accounting entries
to reflect the change in inventory valuation. However, Odoo does **not** automatically update the
AVCO calculation, because [this can potentially create inconsistencies with inventory
valuation].

> **Note:**
>
> This document addresses a specific use case for theoretical purposes. For instructions on how to
> set up and use AVCO, refer to the [inventory valuation cheat sheet](../../../inventory_and_mrp/inventory/inventory_valuation/cheat_sheet.html).

## Configuration

To use average cost inventory valuation on a product, navigate to Inventory ‣
Configuration ‣ Product Categories and select the category that will be using AVCO. On the
product category page, set Costing Method to `Average Cost (AVCO)` and
Inventory Valuation to `Automated`.

> **Note:**
>
> [Inventory valuation cheat sheet](../../../inventory_and_mrp/inventory/inventory_valuation/cheat_sheet.html)

## Using average cost valuation

The average cost method adjusts the inventory valuation when products are received in the warehouse.
This section explains how it works, but if the explanation is unnecessary, skip to the [return
to supplier use case] section.

### Formula

When new products arrive, the new average cost for each product is recomputed using the formula:

\[Avg~Cost = \frac{(Old~Qty \times Old~Avg~Cost) + (Incoming~Qty \times Purchase~Price)}{Final~Qty}\]

- **Old Qty**: product count in stock before receiving the new shipment;
- **Old Avg Cost**: calculated average cost for a single product from the previous inventory
  valuation;
- **Incoming Qty**: count of products arriving in the new shipment;
- **Purchase Price**: estimated price of products at the reception of products (since vendor bills
  may arrive later). The amount includes not only the price for the products, but also added costs,
  such as shipping, taxes, and [landed costs](../../../inventory_and_mrp/inventory/inventory_valuation/landed_costs.html). At
  reception of the vendor bill, this price is adjusted;
- **Final Qty**: quantity of on-hand stock after the stock move.

> **Warning:**
>
> When products leave the warehouse, the average cost **does not** change. Read about why the
> average cost valuation is **not** adjusted [here].

### Compute average cost

To understand how the average cost of a product changes with each shipment, consider the following
table of warehouse operations and stock moves. Each is a different example of how the average cost
valuation is affected.

| Operation | Incoming Value | Inventory Value | Qty On Hand | Avg Cost |
| --- | --- | --- | --- | --- |
|  |  | $0 | 0 | $0 |
| Receive 8 tables at $10/unit | 8 \* $10 | $80 | 8 | $10 |
| Receive 4 tables at $16/unit | 4 \* $16 | $144 | 12 | $12 |
| Deliver 10 tables | -10 \* $12 | $24 | 2 | $12 |

> **Note:**
>
> Ensure comprehension of the above computations by reviewing the “Receive 8 tables at $10/unit”
> example.
>
> Initially, the product stock is 0, so all values are $0.
>
> In the first warehouse operation, `8` tables are received at `$10` each. The average cost is
> calculated using the [formula]:
>
> \[Avg~Cost = \frac{0 + 8 \times $10}{8} = \frac{$80}{8} = $10\]
>
> - Since the *incoming quantity* of tables is `8` and the *purchase price* for each is `$10`,
> - The inventory value in the numerator is evaluated to `$80`;
> - `$80` is divided by the total amount of tables to store, `8`;
> - `$10` is the average cost of a single table from the first shipment.
>
> To verify this in Odoo, in the *Purchase* app, order `8` quantities of a new product, `Table`,
> with no previous stock moves, for `$10` each.
>
> In the table’s Product Category field in the General Information tab of
> the product form, click the ➡️ (arrow) icon, to open an External Link to
> edit the product category. Set the Costing Method to `Average Cost (AVCO)` and
> Inventory Valuation to `Automated`.
>
> Then, return to the purchase order. Click Confirm Order, and click Receive
> Products to confirm receipt.
>
> Next, check the inventory valuation record generated by the product reception by navigating to
> Inventory ‣ Reporting ‣ Inventory Valuation. Select the drop-down for
> `Table`, and view the Total Value column for the *valuation layer* (inventory
> valuation at a specific point in time = on-hand quantity \* unit price). The 8 tables in-stock
> are worth $80.
>
> ![Show inventory valuation of 8 tables in Odoo.](../../../../_images/inventory-val-8-tables.png)

> **Note:**
>
> When the product category’s Costing Method is set to AVCO, then the
> average cost of a product is also displayed on the Cost field, under the
> General Information tab, on the product page itself.

#### Product delivery (use case)

For outgoing shipments, [outbound products have no effect on the average cost valuation]. Although the average cost valuation is not recalculated, the
inventory value still decreases because the product is removed from stock and delivered to the
customer location.

> **Note:**
>
> To demonstrate that the average cost valuation is not recalculated, examine the “Deliver 10
> tables” example.
>
> \[Avg~Cost = \frac{12 \times $12 + (-10) \times $12}{12-10} = \frac{24}{2} = $12\]
>
> 1. Because 10 tables are being sent out to customers, the *incoming quantity* is `-10`. The
>    previous average cost (`$12`) is used in lieu of a vendor’s *purchase price*;
> 2. The *incoming inventory value* is `-10 * $12 = -$120`;
> 3. The old *inventory value* (`$144`) is added to the *incoming inventory value* (`-$120`), so
>    `$144 + -$120 = $24`;
> 4. Only `2` tables remain after shipping out `10` tables from `12`. So the current *inventory
>    value* (`$24`) is divided by the on-hand quantity (`2`);
> 5. `$24 / 2 = $12`, which is the same average cost as the previous operation.
>
> To verify this in Odoo, sell `10` tables in the *Sales* app, validate the delivery, and then
> review the inventory valuation record by going to in Inventory ‣ Reporting ‣
> Inventory Valuation. In the topmost valuation layer, delivering `10` tables reduces the
> product’s value by `-$120`.
>
> **Note**: What is not represented in this stock valuation record is the revenue made from this
> sale, so this decrease is not a loss to the company.
>
> ![Show how deliveries decrease inventory valuation.](../../../../_images/inventory-val-send-10-tables.png)

## Return items to supplier (use case)

Because the price paid to suppliers can differ from the price the product is valued at with the
AVCO method, Odoo handles returned items in a specific way.

1. Products are returned to suppliers at the original purchase price, but;
2. The internal cost valuation remains unchanged.

The above [example table] is updated as follows:

| Operation | Qty\*Avg Cost | Inventory Value | Qty On Hand | Avg Cost |
| --- | --- | --- | --- | --- |
|  |  | $24 | 2 | $12 |
| Return 1 table bought at $10 | -1 \* $12 | $12 | 1 | $12 |

In other words, returns to vendors are perceived by Odoo as another form of a product exiting the
warehouse. To Odoo, because the table is valued at $12 per unit, the inventory value is reduced by
`$12` when the product is returned; the initial purchase price of `$10` is unrelated to the table’s
average cost.

> **Tip:**
>
> To return a single table that was purchased for `$10`, navigate to the receipt in the *Inventory*
> app for the [8 tables purchased in Exercise 1] by going to the
> Inventory Overview, clicking on Receipts, and selecting the desired
> receipt.
>
> Then, click Return on the validated delivery order, and modify the quantity to `1` in
> the reverse transfer window. This creates an outgoing shipment for the table. Select
> Validate to confirm the outgoing shipment.
>
> Return to Inventory ‣ Reporting ‣ Inventory Valuation to see how the
> outgoing shipment decreases the inventory value by $12.
>
> ![Inventory valuation for return.](../../../../_images/inventory-valuation-return.png)

### Eliminate stock valuation errors in outgoing products

Inconsistencies can occur in a company’s inventory when the average cost valuation is recalculated
on outgoing shipments.

To demonstrate this error, the table below displays a scenario in which 1 table is shipped to a
customer and another is returned to a supplier at the purchased price.

| Operation | Qty\*Price | Inventory Value | Qty On Hand | Avg Cost |
| --- | --- | --- | --- | --- |
|  |  | $24 | 2 | $12 |
| Ship 1 product to customer | -1 \* $12 | $12 | 1 | $12 |
| Return 1 product initially bought at $10 | -1 \* $10 | **$2** | **0** | $12 |

In the final operation above, the final inventory valuation for the table is `$2` even though there
are `0` tables left in stock.

> **Note:**
>
> Use the average cost to value the return. This does not mean the company gets $12 back for a $10
> purchase; the item returned for $10 is valued internally at $12. The inventory value change
> represents a product worth $12 no longer being accounted for in company assets.

## Anglo-Saxon accounting

In addition to using AVCO, companies that use **Anglo-Saxon accounting** also keep a holding
account that tracks the amount to be paid to vendors. Once a vendor delivers an order, **inventory
value** increases based on the vendor price of the products that have entered the stock. The holding
account (called **stock input**) is credited and only reconciled once the vendor bill is received.

The table below reflects journal entries and accounts. The *stock input* account stores the money
intended to pay vendors when the vendor bill has not yet been received. To balance accounts when
returning products that have a price difference between the price the product is **valued at** and
the price it was bought for, a *price difference* account is created.

| Operation | Stock Input | Price Diff | Inventory Value | Qty On Hand | Avg Cost |
| --- | --- | --- | --- | --- | --- |
|  |  |  | $0 | 0 | $0 |
| Receive 8 tables at $10 | ($80) |  | $80 | 8 | $10 |
| Receive vendor bill $80 | $0 |  | $80 | 8 | $10 |
| Receive 4 tables at $16 | ($64) |  | $144 | 12 | $12 |
| Receive vendor bill $64 | $0 |  | $144 | 12 | $12 |
| Deliver 10 tables to customer | $0 |  | $24 | 2 | $12 |
| Return 1 table initially bought at $10 | **$10** | **$2** | **$12** | 1 | $12 |
| Receive vendor refund $10 | $0 | $2 | $12 | 1 | $12 |

### Product reception

#### Summary

At product reception, Odoo ensures companies can pay for goods that were purchased by preemptively
moving an amount matching the price of received goods into the [liability account](cheat_sheet.html), **Stock Input**. Then, once the bill
has been received, the amount in the holding account is transferred to *Accounts Payable*. Transfers
into this account means the bill has been paid. **Stock Input** is reconciled once the vendor bill
is received.

Inventory valuation is a method of calculating how much each in-stock product is worth internally.
Since there is a difference between the price the product is **valuated at** and the price the
product was actually **purchased for**, the **Inventory Valuation** account is unrelated to the
crediting and debiting operations of the **Stock Input** account.

To conceptualize all this, follow the breakdown below.

#### Accounts balanced at received products

In this example, a company starts with zero units of a product, `table`, in stock. Then, 8 tables
are received from the vendor:

1. The **Stock Input** account stores `$80` of credit owed to the vendor. The amount in this account
   is unrelated to the inventory value.
2. `$80` worth of tables came **in** (**debit** the *Inventory Value* account `$80`), and
3. `$80` must be paid **out** for received goods (**credit** the *Stock Input* account `$80`).

##### In Odoo

Odoo generates an accounting journal entry when shipments that use AVCO costing method are
received. Configure a Price Difference Account by selecting the ➡️ (arrow)
icon next to the Product Category field on the product page.

Under Account Properties, create a new Price Difference Account by typing in
the name of the account and clicking Create and Edit. Then set the account
Type as `Expenses`, and click Save.

![Create price difference account.](../../../../_images/create-price-difference.png)

Then, receive the shipment in the *Purchase* app or *Inventory* app, and navigate to the
Accounting app ‣ Accounting ‣ Journal Entries. In the list, find the
Reference that matches the warehouse reception operation for the relevant product.

![Show accounting entry of 8 tables from the list.](../../../../_images/search-for-entry-of-tables.png)

Click on the line for 8 tables. This accounting journal entry shows that when the 8 tables were
received, the `Stock Valuation` account increased by `$80`. Conversely, the **Stock Input** account
(set as `Stock Interim (Received)` account by default) is credited `$80`.

![Debit stock valuation and credit stock input 80 dollars.](../../../../_images/accounting-entry-8-tables.png)

#### Accounts balanced at received vendor bill

In this example, a company starts with zero units of a product, table, in stock. Then, 8 tables are
received from the vendor. When the bill is received from vendor for 8 tables:

1. Use `$80` in the **Stock Input** account to pay the bill. This cancels out and the account now
   holds `$0`.
2. Debit **Stock Input** `$80` (to reconcile this account).
3. Credit **Accounts payable** `$80`. This account stores the amount the company owes others, so
   accountants use the amount to write checks to vendors.

##### In Odoo

Once the vendor requests payment, navigate to the Purchase app ‣ Orders ‣
Purchase and select the PO for 8 tables. Inside the PO, select Create Bill.

Switch to the Journal Items tab to view how `$80` is transferred from the holding
account, `Stock Interim (Received)` to `Accounts Payable`. Confirm the bill to record
the payment to the vendor.

![Show bill linked to the purchase order for 8 tables.](../../../../_images/receive-8-table-bill.png)

### On product delivery

In the [above example table], when 10 products are delivered
to a customer, the **Stock Input** account is untouched because there are no new products coming in.
To put it simply:

1. **Inventory valuation** is credited `$120`. Subtracting from inventory valuation represents
   `$120` worth of products exiting the company.
2. Debit **Accounts Receivable** to record revenue from the sale.

![Show journal items linked to sale order.](../../../../_images/sell-10-tables.png)
> **Note:**
>
> Understand Anglo-Saxon expensing
>
> In the accounting journal entry invoicing a customer for 10 tables, the accounts **Product
> Sales**, **Tax Received**, and **Accounts Receivable** all pertain to the sale of the product.
> **Accounts Receivable** is the account where the customer payment will be received.
>
> Anglo-Saxon accounting recognizes the cost of goods sold (COGS) once the sale is made. So, up
> until the product is sold, scrapped, or returned, costs of keeping the product in stock are not
> accounted for. The **Expense** account is debited `$120` to log the costs of storing 10 tables
> during this period of time.

### On product return

In the [above example table], when returning 1 product to a
vendor purchased at `$10`, a company expects `$10` in the **Accounts Payable** account from the
vendor. However, **Stock Input** account must be debited `$12` because the average cost is `$12` at
the time of the return. The missing `$2` is accounted for in the Price Difference
Account, which is set up in the product’s Product Category.

> **Note:**
>
> Behavior of *price difference accounts* varies from localization. In this case, the account is
> intended to store differences between vendor price and *automated* inventory valuation methods.

Summary:

1. Debit **Stock Input** account `$10` to move the table from stock to stock input. This move is to
   indicate that the table is to be processed for an outgoing shipment.
2. Debit **Stock Input** an additional `$2` to account for the **Price Difference**.
3. Credit **Stock Valuation** `$12` because the item is leaving the stock.

![2 dollar difference expensed in Price Difference account.](../../../../_images/expensing-price-difference-account.png)

Once the vendor’s refund is received,

1. Credit **Stock Input** account `$10` to reconcile the price of the table.
2. Debit **Accounts Payable** `$10` to have the accountants collect and register the payment in
   their journal.

![Return to get 10 dollars back.](../../../../_images/return-credit-note.png)

---

# Tax units

> **Warning:**
>
> This is only applicable to multi-company environments.

A **tax unit** is a group of VAT-taxable enterprises that are legally independent of each other but
are closely linked financially, organizationally, and economically and therefore considered the same
VAT-taxable enterprise. **Tax units** are not mandatory, but if created, constituent companies of
the unit must belong to the same **country**, use the same **currency**, and one company must be
designated as the **representative** company of the **tax unit**. **Tax units** receive a specific
**tax ID** intended only for **tax returns**. **Constituent** companies keep their **tax ID** used
for **commercial purposes**.

> **Tip:**
>
> Enterprise **A** owes €300.000,00 of VAT taxes and enterprise **B** can recover €280.000,00 of
> VAT taxes. They form up as a **tax unit** so that the two amounts balance out and must conjointly
> only pay €20.000,00 of VAT taxes.

## Configuration

To create a **tax unit**, go to Accounting ‣ Configuration ‣ Tax Units, and
click New. Enter a **name** for the unit, select a Country, the
Companies to incorporate in the unit, the Main Company, and the
Tax ID of the **constituent** company of that tax unit.

### Fiscal position

As transactions between constituents of the same **tax unit** are not subject to VAT, it is possible
to create a [tax mapping (fiscal position)](../taxes/fiscal_positions.html) to avoid the
application of VAT on inter-constituent transactions.

Be sure a constituent company has been selected before, then go to Accounting ‣
Configuration ‣ Fiscal Positions, and Create a new **fiscal position**. Click the
Tax Mapping tab, select the Tax on Product usually applied for
**non-constituent** transactions, and in Tax to Apply, select the 0% tax to apply for
**constituent** transactions.

Do the same for the Account Mapping tab if required, and repeat this process for
**each** constituent company on your database.

> **Tip:**
>
> Depending on your [localization package](../../fiscal_localizations.html), taxes
> may vary from the screenshot displayed.
>
> ![Tax mapping of fiscal position for tax unit](../../../../_images/fiscal-positions.png)

Then, assign the fiscal position by opening the **Contacts** app. Search for a **constituent**
company, and open the contact’s **card**. Click the Sales & Purchase tab, and in the
Fiscal Position field, input the **fiscal position** created for the **tax unit**.
Repeat the process for each **constituent** company card form, on each company database.

> **Note:**
>
> [Fiscal positions (tax and account mapping)](../taxes/fiscal_positions.html).

## Tax report

The **representative** company can access the aggregated tax report of the **tax unit** by going to
Accounting ‣ Reporting ‣ Tax Report, and selecting the **tax unit** in
Tax Unit. This report contains the aggregated transactions of all **constituents** and
the .XML export contains the name and VAT number of the **main** company.

![tax unit tax report](../../../../_images/report.png)

---

# Taxes

Tax regulations generally require companies to compute tax amounts on sales, keep a record of
accumulated tax debit and credit, and periodically file this information in tax returns.

## Overview

In general, managing taxes in Odoo involves the following steps:

1. Taxes are added on individual lines of documents created via the Sales, Purchase, Accounting, and
   Point of Sale apps.
2. Odoo automatically computes tax amounts on the documents.
3. On accounting documents, Odoo generates journal items to keep track of tax debit and tax credit.
4. The total base, tax debit, and tax credit for a period can be viewed in the tax return report
   and used to file a tax return.

### Taxes on sales and purchases

Most sales and purchase documents have a Taxes field where taxes can be applied to
individual lines. This includes [invoices](customer_invoices.html) and [vendor bills](vendor_bills.html) in the Accounting app, [sales quotations](../../sales/sales/sales_quotations.html)
in the Sales app, and [purchase orders](../../inventory_and_mrp/purchase/manage_deals/rfq.html) in
the Purchase app.

![Adding a 21% tax on an invoice line.](../../../_images/invoice-tax.png)
> **Note:**
>
> When adding a product to a sale or purchase line, the taxes [assigned to the product] are automatically applied to the line.
>
> In the [Point of Sale](../../sales/point_of_sale.html) app, the taxes [assigned to the
> products] are applied directly to the order and cannot be changed except by a
> [fiscal position](taxes/fiscal_positions.html).

### Automatic computation of tax amounts

Applying a tax to a sale or purchase line allows Odoo to automatically compute the tax amount based
on the sale or purchase line’s subtotal and the tax’s configuration. The details of the computation
are explained in the [Tax computation documentation](taxes/tax_computation.html).

![Odoo automatically computes a tax amount for the 21% tax.](../../../_images/invoice-tax-amount.png)

### Automatic generation of tax journal items

Upon applying a tax on an [invoice](customer_invoices.html) or [vendor bill](vendor_bills.html), a
tax payable journal item is automatically generated with the tax amount. This keeps track of the tax
debit or credit associated with the transaction.

Furthermore, the tax amount is added to the amount due on the receivable or payable journal item.

Finally, [Tax Grids](reporting/tax_returns.html#accounting-tax-returns-tax-grids) are added both to the automatically
created tax payable journal item and to the invoice line on which the tax is applied. These tags are
used to retrieve the journal items corresponding to the tax’s base and tax amount in the [Tax
Return](reporting/tax_returns.html) report.

![Odoo automatically generates a tax payable journal item for the 21% tax.](../../../_images/invoice-tax-items.png)
> **Note:**
>
> If [Cash Basis](taxes/cash_basis.html) is enabled, upon reconciling the invoice or vendor bill
> with the payment, an additional journal entry is created to represent the creation of the tax
> debit or credit at that point in time.

### Filing tax returns

The [Tax Return](reporting/tax_returns.html) report aggregates the base and tax amounts from
invoices and vendor bills over a given period and presents it in a format tailored to the
[fiscal localization](../fiscal_localizations.html).

The amounts presented in the tax return report can be used to complete tax declarations that need to
be periodically submitted to the government. In most cases, there is a one-to-one correspondence
between the lines of the tax return and the official tax declaration, allowing amounts to simply be
copied from one to the other.

![The base section of the tax return report for Belgium.](../../../_images/tax-return-base.png)
![The tax section of the tax return report for Belgium.](../../../_images/tax-return-tax.png)

## Basic tax configuration

Follow these basic steps to set up taxes:

1. Enable any relevant [company-wide options].
2. Activate any needed [pre-configured taxes].
3. Assign taxes on your [products].

### Company-wide options

To access these configuration options, go to Accounting ‣ Configuration
‣ Settings and scroll down to Taxes.

#### Default taxes

The default Sales Tax and Purchase Tax are automatically set on products
when creating new products.

If [Accounting Firms](../accounting.html#accounting-fiduciaries) mode is enabled, the default sales tax is
automatically set on new invoice lines, and the default purchase tax is automatically set on new
vendor bill lines.

Prices can be changed to Tax Included to treat all taxes as [tax
included](taxes/tax_computation.html#taxes-included-in-price) by default. This would be appropriate if all of a company’s
pricing is done tax-included. If only some of a company’s pricing is tax-included, individual taxes
can be set as Tax Included.

#### EU intra-community distance selling

Activate this option if you are based in the EU and sell to consumers in other EU countries to apply
local VAT rates.

> **Note:**
>
> [EU intra-community distance selling](taxes/eu_distance_selling.html)

#### Cash basis

Activate this option if taxes must be accounted for on a cash rather than accruals basis. Some
countries mandate cash basis accounting; in that case, this option will be activated by default by
the [fiscal localization package](../fiscal_localizations.html).

> **Note:**
>
> [Cash basis](taxes/cash_basis.html)

### Activate pre-configured taxes

The list of taxes can be accessed by going to Accounting ‣ Configuration ‣
Taxes.

Generally, inactive taxes are created for most sales tax rates by the [fiscal localization](../fiscal_localizations.html) package, but only the main tax rate is active by default. To activate an
inactive tax, click the toggle in the Active column.

### Assign taxes on products

To configure the taxes used for each product, go to Accounting ‣ Customers ‣
Products, select the product to configure, and fill the Sales Taxes and
Purchase Taxes fields. These taxes are automatically applied when adding the product to
an invoice, vendor bill, sales order, purchase order, or point of sale order.

> **Note:**
>
> Use the [Default Taxes] company-wide setting to automatically fill these
> fields on new products.

## Advanced tax configuration

The following aspects of a tax can be customized:

- How the tax [appears in the backend]
- How the tax [appears to customers]
- The details of the [tax computation](taxes/tax_computation.html)
- How tax payable journal items are [created]
- How to configure the tax to [replace] other taxes according to
  [fiscal positions](taxes/fiscal_positions.html).

To open a tax’s configuration, go to Accounting ‣ Configuration ‣ Taxes, then
click the tax name.

### Configure backend appearance and availability

The following options determine how a tax is displayed to users in the Odoo back-end.

#### Tax name

The Tax Name appears for backend users in the Taxes field in [sales
orders](../../sales/sales.html), [invoices](customer_invoices.html), product forms, etc.

#### Tax type

The Tax Type determines where the tax is available to be selected.

- **Sales**: Customer invoices, product customer taxes, etc.
- **Purchase**: Vendor bills, product vendor taxes, etc.
- **None**

> **Note:**
>
> Use None for taxes that you want to include in a [Group of Taxes](taxes/tax_computation.html#taxes-computation) but that you do not want to list along with other sales or purchase taxes.

#### Tax scope

The Tax Scope restricts the use of taxes to a type of product, either **goods** or
**services**.

#### Description

The Description can be edited for the purpose of internal documentation.

### Configure how the tax appears to customers

#### Label on invoices

The Label on Invoices appears on invoice lines in invoice PDFs and on the customer
portal.

![The Label on Invoice shows on the invoice line when viewed in the customer portal.](../../../_images/invoice-portal-tax.png)

#### Tax group

The Tax Group is shown in the totals section of the invoice, in invoice PDFs and on the
customer portal. Multiple taxes that belong to the same tax group are aggregated together into a
single tax amount.

![The Tax Group shows in the totals section when viewed in the customer portal.](../../../_images/invoice-portal-total.png)

### Configure how tax journal items are created

The Distribution for Invoices and Distribution for Refunds sections control
the generation of tax payable journal items in invoices and credit notes, respectively. They also
determine which [tax grids](reporting/tax_returns.html#accounting-tax-returns-tax-grids) are set on invoice lines when
this tax is applied.

Each of these sections should contain one Base line, one or more % of tax
lines amounting to 100% (e.g. one 100% line, or two 50% lines), and optionally, one or more
% of tax lines amounting to -100.00%.

The Base line can have one or more Tax Grids set, which are added to the
invoice line on which the tax is applied.

The % of tax lines control the creation of tax payable journal items. The tax amount is
distributed according to the percentages on these lines, and each line is then used as a template to
create a tax payable journal item with the same Account and Tax Grids. If
the Account is not specified, it defaults to the account of the original invoice line on
which the tax is applied.

Typical cases include:

- one 100% of tax line: this is the most common case where the tax amount should appear
  on a single tax payable journal item.
- one 100% of tax and one -100% of tax line: this is appropriate if the tax
  simultaneously generates both a tax debit and a tax credit which cancel each other out (e.g. EU
  intra-community reverse-charge VAT).
- one 50% of tax line that specifies a tax payable account and another
  50% of tax line that does not specify an account: this is appropriate for partially
  deductible purchase VAT, where part of the tax must be considered an expense rather than a tax
  credit asset that can offset tax liability.

![The Distribution for Invoices of a 21% VAT tax.](../../../_images/distribution-invoices.png)
![The Distribution for Refunds of a 21% VAT tax.](../../../_images/distribution-refunds.png)

### Tax mapping

Taxes can be combined with [fiscal positions](taxes/fiscal_positions.html) to map taxes to each
other so that the correct tax is applied based on the customer’s or vendor’s location and business
type.

When configuring a tax, leave the Fiscal Position field blank to make the tax
immediately available across all fiscal positions, or select specific fiscal positions where this
tax should be used to replace other taxes with it. If one or more fiscal positions are selected, use
the Replaces field to select all of the taxes that this tax should replace for the
selected fiscal position(s).

To replace one tax with multiple other taxes, configure each of the replacement taxes to replace the
default product tax.

> **Tip:**
>
> As a sales tax, the 0% Exports tax applies to quotations, sales orders, and invoices
> that use the Foreign Trade fiscal position. On those records, any time that the
> 15% tax would be used, the 0% Exports tax is used instead.
>
> ![The **0% Exports** tax record](../../../_images/tax-mapping-example.png)

> **Note:**
>
> Since the first fiscal position in the sequence is considered the company’s default, the taxes
> set on products are expected to be used with that fiscal position, so the Replaces
> field is not displayed on it.

> **Note:**
>
> To more easily view which taxes are replaced, use the
> adjust settings in the taxes list view and display the Replaces field.
>
> ![The **Replaces** field shown in the list view](../../../_images/tax-mapping-list.png)

> **Note:**
>
> Tax mapping only works with [active] taxes.

## Extra taxes

“Extra taxes” is a broad term referring to additional taxes beyond the standard or basic taxes
imposed by governments. These extra taxes can be **luxury** taxes, **environmental** taxes,
**import** or **export duties** taxes, etc.

> **Note:**
>
> The method to compute these taxes varies across different countries. We recommend consulting your
> country’s regulations to understand how to calculate them for your business.

To compute an extra tax in Odoo, [create a tax], enter a tax name, select
a [Tax Computation], set an Amount, and in the
Advanced Options tab, enable Affect Base of Subsequent Taxes. Then, drag and
drop the taxes in the [order they should be computed](taxes/tax_computation.html#taxes-base-subsequent).

> **Tip:**
>
> - In Belgium, the formula to compute an environmental tax is: `(product price + environmental
>   tax) x sales tax`. Therefore, our environmental tax has to come *before* the sales tax in the
>   computation sequence.
> - In our case, we created a 5% environmental tax (Ecotax) and put it *before* the Belgian base
>   tax of 21%.
>
> ![Environmental tax sequence in Belgium.](../../../_images/ecotax.png)

> **Note:**
>
> - [Tax computation](taxes/tax_computation.html)
> - [Fiscal positions (tax and account mapping)](taxes/fiscal_positions.html)
> - [B2B (tax excluded) and B2C (tax included) pricing](taxes/B2B_B2C.html)
> - [Tax return (VAT report)](reporting/tax_returns.html)

---

# Cash basis taxes

Cash basis taxes are due when the payment is made, as opposed to standard taxes that are due when
the invoice is confirmed. Reporting your income and expenses to the government based on the cash
basis method is mandatory in some countries and under some conditions.

> **Tip:**
>
> You sell a product in the 1st quarter of your fiscal year, and the payment is received in the 2nd
> quarter. Based on the cash basis method, the tax you must pay is for the 2nd quarter.

## Configuration

Go to Accounting ‣ Configuration ‣ Settings and under the Taxes
section, enable Cash Basis.

Then, define the Tax Cash Basis Journal. Click on the external link button next to the
journal to update its default properties such as the Journal Name, Type or
Short Code.

![Select your Tax Cash Basis Journal and click on the external link](../../../../_images/tax_cash_basis_journal.png)
> **Note:**
>
> By default, the journal entries of the Cash Basis Taxes journal are named using the
> CABA short code.

Once this is done, go to Accounting ‣ Configuration ‣ Accounting: Taxes to
configure your taxes. You can either Create a new tax or update an existing one by
clicking on it.

The Account column reflects the proper transitional accounts to post taxes until the
payment is registered.

![Fill in the account column with a transitional accounts where taxes go until the payment is registered](../../../../_images/account_column.png)

In the Advanced Options tab, decide of the Tax Exigilibity. Select
Based on Payment, so the tax is due when the payment of the invoice is received. You can
then also define the Cash Basis Transition Account where the tax amount is recorded as
long as the original invoice has not been reconciled.

![Fill in the Cash Basis Transition Account where taxes amounts go until payment reconciliation.](../../../../_images/advanced_options.png)

## Impact of cash basis taxes on accounting

To illustrate the impact of cash basis taxes on accounting transactions, let’s take an example with
the sales of a product that costs 1,000$, with a cash basis tax of 15%.

!

The following entries are created in your accounting, and the tax report is currently empty.

| **Customer journal (INV)** | |
| --- | --- |
| **Debit** | **Credit** |
| Receivable $1,150 |  |
|  | Income $1,000 |
|  | Temporary tax account $150 |

When the payment is then received, it is registered as below :

| **Bank journal (BANK)** | |
| --- | --- |
| **Debit** | **Credit** |
| Bank $1,150 |  |
|  | Receivable $1,150 |

> **Note:**
>
> Once the payment is registered, you can use the Cash Basis Entries smart button on
> the invoice to access them directly.

Finally, upon reconciliation of the invoice with the payment, the below entry is automatically
created:

| **Tax Cash Basis Journal (Caba)** | |
| --- | --- |
| **Debit** | **Credit** |
| Income account $1,000 |  |
| Temporary tax account $150 |  |
|  | Income account $1,000 |
|  | Tax Received $150 |

The journal items Income account vs. Income account are neutral, but they
are needed to ensure correct tax reports in Odoo with accurate base tax amounts.

Using a default Base Tax Received Account is recommended so your balance is at zero and
your income account is not polluted by unnecessary accounting movements. To do so, go to
Configuration ‣ Settings ‣ Taxes, and select a
Base Tax Received Account under Cash Basis.

---

# Tax computation

## Tax computation

The Tax Computation field determines the relation between the tax amount and the base
the tax is based on. The following options are available:

- [Group of Taxes]: a combination of several other taxes
- [Fixed]: a fixed amount
- [Percentage of Price]: a percentage of the
  tax-excluded sales price
- [Percentage of Price Tax Included]: a
  percentage of the tax-included total
- [Custom Formula]: a custom, user-defined formula

### Group of taxes

The tax is a combination of multiple sub-taxes. You can add as many taxes as you want, in the order
you want them to be applied.

> **Warning:**
>
> Make sure the tax sequence is correct, as the display order determines the application order and
> may affect tax computation, particularly if a tax [affects the base of subsequent taxes].

### Fixed

The tax has a fixed amount in the default currency. The amount remains the same per unit,
regardless of the sales price.

The computation is \(\text{tax amount} = \text{fixed tax amount} \times \text{quantity}\).

> **Tip:**
>
> A product has a sales price of $1000, and we apply a $10 Fixed tax. We then have:
>
> | Product sales price | Price without tax | Tax | Total |
> | --- | --- | --- | --- |
> | 1,000 | 1,000 | 10 | 1,010.00 |

### Percentage of price

The tax rate is a percentage of the **tax-excluded** subtotal.

The exact tax computation depends on the [Included in Price] field,
which determines whether the tax amount is included in the sales price.

Tax-excludedTax-included

If Included in Price is Tax Excluded, the computation is
\(\text{tax amount} = \text{sales price} \times \text{tax rate}\).

> **Tip:**
>
> A product has a sales price of $1000, and we apply a 10% Percentage of Price
> tax that is Tax Excluded. We then have:
>
> | Product sales price | Price without tax | Tax | Total |
> | --- | --- | --- | --- |
> | 1,000 | 1,000 | 100 | 1,100.00 |

If Included in Price is Tax Included, the computation is
\(\text{tax amount} = \text{sales price} \times \frac{\text{tax rate}}{1 +
\text{tax rate}}\).

> **Tip:**
>
> A product has a sales price of $1000, and we apply a 10% Percentage of Price
> tax that is Tax Included. We then have:
>
> | Product sales price | Price without tax | Tax | Total |
> | --- | --- | --- | --- |
> | 1,000 | 909.09 | 90.91 | 1,000.00 |

### Percentage of price tax included

> **Warning:**
>
> This tax computation is rarely used and only useful in countries (e.g., Brazil, Bolivia) that
> quote tax rates as a percentage of the tax-included total.
> For the more common need to compute tax amounts from a tax-included price, use the
> [Percentage of Price] tax computation with
> [Included in Price] set to Tax Included.

The tax rate is a percentage of the **tax-included** total.

The exact tax computation depends on the [Included in Price] field,
which determines whether the tax amount is included in the sales price.

Tax-excludedTax-included

If Included in Price is set to Tax Excluded, the computation is
\(\text{tax amount} = \text{sales price} \times \frac{\text{tax rate}}{1 -
\text{tax rate}}\).

> **Tip:**
>
> A product has a sales price of $1000, and we apply a 10% Percentage of Price
> Tax Included tax that is Tax Excluded. We then have:
>
> | Product sales price | Price without tax | Tax | Total |
> | --- | --- | --- | --- |
> | 1,000 | 1,000 | 111.11 | 1,111.11 |
>
> Note that the real tax rate in terms of the tax-excluded price is
> \(\frac{111.11}{1000} = 11.111\%\).

If Included in Price is set to Tax Included, the computation is
\(\text{tax amount} = \text{sales price} \times \text{tax rate}\).

> **Tip:**
>
> A product has a sales price of $1000, and we apply a 10%
> Percentage of Price Tax Included tax that is Tax Included.
> We then have:
>
> | Product sales price | Price without tax | Tax | Total |
> | --- | --- | --- | --- |
> | 1,000 | 900 | 100 | 1,000.00 |
>
> Note that the real tax rate in terms of the tax-excluded price is
> \(\frac{100}{900} = 11.111\%\).

### Custom formula

> **Warning:**
>
> If a tax can be expressed as a multiple of the quantity of the product to which it applies, it
> can be defined as a [Fixed] tax. Doing so is strongly recommended
> over defining a Custom Formula tax.

> **Note:**
>
> To use Custom Formula taxes, [install](../../../general/apps_modules.html#general-install) the Define
> Taxes as Python Code (`account_python_tax`) module.

For a Custom Formula tax, the tax amount is computed according to a Python expression
defined in the Formula field. The Python expression may contain the following tokens:

- any of the following variables:

  - `price_unit`: the unit price of the product
  - `base`: the taxable basis on which the tax is applied - may differ from the `price_unit` if
    other taxes are applied first
  - `quantity`: the quantity of the product
  - `product`: the product record - product fields can also be accessed
- integers and floating-point numbers
- the following permitted tokens: `(`, `)`, `+`, `-`, `*`, `/`, `,`, `<`, `>`, `<=`, `>=`, `and`,
  `or`, `None`, `min`, and `max`

> **Tip:**
>
> A product has a sales price of $1000, and we apply a Custom Formula tax with a
> Formula of `min(base, 500) * 0.10 + max(base - 500, 0) * 0.20`
>
> We then have:
>
> | Product sales price | Price without tax | Tax | Total |
> | --- | --- | --- | --- |
> | 1,000 | 1,000 | 150 | 1,150.00 |

## Included in price

> **Note:**
>
> To set a company-wide default for this setting, go to Accounting ‣
> Configuration ‣ Settings, find the Taxes section, and set the Prices
> setting to Tax Excluded or Tax Included. This setting cannot be changed
> once invoices have been created.

Default indicates that the tax follows the company-wide default.

Tax Excluded indicates that the tax amount is not included in the sales price. The tax
computation will therefore compute a tax amount on top of the sales price.

Tax Included indicates that the tax amount is included in the sales price. The tax
computation will therefore split the sales price into a tax-excluded base and the tax amount. This
makes it suitable for B2C sales in most countries, where prices are quoted tax-inclusive.

> **Tip:**
>
> A product has a sales price of $1000, and we apply a 10% Percentage of Price tax
> with Included in Price set to Tax Included. We then have:
>
> | Product sales price | Price without tax | Tax | Total |
> | --- | --- | --- | --- |
> | 1,000 | 909.09 | 90.91 | 1,000.00 |

> **Note:**
>
> For a guide on configuring tax-excluded and tax-included prices for B2B and B2C customers,
> see [B2B (tax excluded) and B2C (tax included) pricing](B2B_B2C.html).

## Affect base of subsequent taxes

This setting controls how multiple taxes on a product line affect each other.

If this setting is enabled, this tax’s tax amount is included in the base of any subsequent tax
applied on the same product line that has its [Base affected by preceding taxes] setting enabled. As such,
the subsequent tax’s base is the sum of the tax-excluded base and this tax’s tax amount.

Tax-excludedTax-included

If Affect base of subsequent taxes is enabled and Included in Price is
set to Tax Excluded, subsequent taxes with the Base affected by
preceding taxes setting enabled will be based on a modified sales price equal to the original
sales price plus the tax amount.

> **Tip:**
>
> A product has a sales price of $1000, and we apply a 10% Percentage of Price
> tax where the Included in Price setting is set to Tax Excluded and
> the Affect base of subsequent taxes setting is enabled. Any subsequent tax with
> its Base affected by preceding taxes will be based on a modified sales price of
> $1100.

If Affect base of subsequent taxes is enabled and Included in Price is
set to Tax Included, subsequent taxes with the Base affected by
preceding taxes setting enabled will be based on the original sales price.

> **Tip:**
>
> A product has a sales price of $1000, and we apply a 10% Percentage of Price
> tax where the Included in Price setting is set to Tax Included and
> the Affect base of subsequent taxes setting is enabled. Any subsequent tax with
> its Base affected by preceding taxes will be based on the original sales price
> of $1000.

If this setting is disabled, the tax amount will not be included in the base of any subsequent tax
applied on the same product line.

Tax-excludedTax-included

If Affect base of subsequent taxes is disabled and Included in Price
is set to Tax Excluded, subsequent taxes with the Base affected by
preceding taxes setting enabled will be based on the original sales price.

> **Tip:**
>
> A product has a sales price of $1000, and we apply a 10% Percentage of Price
> tax where the Included in Price setting is set to Tax Excluded and
> the Affect base of subsequent taxes setting is enabled. Any subsequent tax with
> its Base affected by preceding taxes will be based on the original sales price
> of $1000.

If Affect base of subsequent taxes is disabled and Included in Price
is set to Tax Included, subsequent taxes with the Base affected by
preceding taxes setting enabled will be based on a modified sales price equal to the original
sales price minus the tax amount.

> **Tip:**
>
> A product has a sales price of $1000, and we apply a 10% Percentage of Price
> tax where the Included in Price setting is set to Tax Included and
> the Affect base of subsequent taxes setting is enabled. Any subsequent tax with
> its Base affected by preceding taxes will be based on a modified sales price of
> $909.09.

This setting is considered any time multiple taxes are applied to the same product line, whether
via a [group of taxes] or multiple taxes added directly to a product line.

> **Note:**
>
> The order in which taxes are applied depends only on the order in which they appear in the
> Taxes list, not on the order in which they are added to a product line.
>
> To modify the order, go to Accounting ‣ Configuration ‣ Taxes, and drag and
> drop taxes using the handles to the left of the tax names.
>
> ![The order of appearance of taxes in the Taxes list determines which tax is applied first](../../../../_images/list-sequence.png)
>
> Regardless of the order in the Taxes list, Tax Excluded taxes do not
> affect the base of subsequent Tax Included taxes (see the note in
> [Base affected by preceding taxes]).

> **Tip:**
>
> In the following example:
>
> - the Ecotax is a Fixed tax of €0.90 per unit, with the Affect base of
>   subsequent taxes setting enabled.
> - The 21% VAT tax is a 21% Percentage of Price tax with the Base affected
>   by preceding taxes setting enabled.
> - In the Taxes list, the 21% VAT tax comes after the Ecotax, as shown in the
>   configuration above.
>
> When applying both taxes to a product line, the Ecotax amount is added to the basis of the 21%
> VAT tax.
>
> ![The Ecotax is added to the basis of the 21% VAT tax](../../../../_images/subsequent-line.png)

## Base affected by preceding taxes

This setting, which is only visible in [developer mode](../../../general/developer_mode.html),
determines whether any previous tax that [affects the base of subsequent taxes] will modify the sales price that this tax is based on.

> **Note:**
>
> Taxes with [Included in Price] set to Tax Included do
> not have this setting. Such taxes are never affected by previous Tax Excluded taxes,
> except if they have the Fixed [tax computation] type.

---

# Withholding taxes

A **withholding tax**, also known as retention tax, mandates the payer of a customer invoice to
deduct a tax from the payment and remit it to the government. Typically, a tax is included in the
subtotal to calculate the total amount paid, while withholding taxes are directly subtracted from
the payment.

## Configuration

In Odoo, a withholding tax is defined by creating a negative tax. To create one, go
to Accounting ‣ Configuration ‣ Taxes and, in the Amount field,
enter a negative amount.

![negative tax amount in field](../../../../_images/negative-amount.png)

Then, go to the Advanced Options tab and create a retention Tax Group.

![tax group for retention tax.](../../../../_images/tax-group.png)
> **Note:**
>
> If the retention is a percentage of a regular tax, create a Tax with a
> Tax Computation as a Group of Taxes. Then, set both the regular tax and
> the retention one in the Definition tab.

## Retention taxes on invoices

Once the retention tax has been created, it can be used on customer forms, sales orders, and
customer invoices.
Several taxes can be applied on a single customer invoice line.

![invoice lines with taxes](../../../../_images/invoice-tax1.png)
> **Note:**
>
> [Taxes](../taxes.html)

---

# VAT numbers verification (VIES)

[VAT Information Exchange System](https://ec.europa.eu/taxation_customs/vies/#/vat-validation), or
**VIES**, is a tool provided by the European Commission that allows you to check the validity of VAT
numbers for companies registered in the European Union.

Odoo’s VAT Validation feature uses the VIES to verify your contacts’ VAT numbers directly from
Odoo’s interface.

> **Note:**
>
> Regardless of whether or not the Verify VAT Numbers feature is enabled, Odoo checks the format of
> a contact’s VAT against the [expected format of VAT numbers](https://en.wikipedia.org/wiki/VAT_identification_number) from that country.

## VIES VAT number verification

To activate this feature, go to Accounting ‣ Configuration ‣ Settings. In the
Taxes section, enable the Verify VAT Numbers feature, and click on
Save.

Once the Verify VAT Numbers feature is enabled, if the contact’s Tax ID
field is populated *and* its country is different from your company’s country, Odoo displays an
Intra-Community Valid checkbox. Odoo tests the VAT number through the VIES and
automatically checks or unchecks the Intra-Community Valid checkbox depending on the
validity of the VAT number.

![Intra-community valid checkbox on the contact record](../../../../_images/intra-community-valid.png)
> **Warning:**
>
> It is possible to manually override the Intra-Community Valid field on a contact in
> case the automatic VIES check is incorrect (for example, if the company was recently created and
> its VAT is not yet in the VIES). This change is logged in the chatter for transparency.

> **Note:**
>
> Odoo can [automatically apply fiscal positions](fiscal_positions.html#fiscal-positions-automatic). If the Verify VAT
> Numbers feature is enabled, any fiscal positions with VAT required enabled will require
> Intra-Community valid VAT numbers to apply automatically.

---

# Fiscal positions (tax and account mapping)

Default taxes and accounts are set on products and customers to create new transactions on the fly.
However, depending on the customers’ and vendors’ location and business type, using different
taxes and accounts for a transaction might be necessary.

**Fiscal positions** allow the creation of rules to adapt the taxes and the income and expense
accounts used for a transaction automatically.

They can be applied [automatically], [manually], or [assigned to a partner].

> **Note:**
>
> Several default fiscal positions are available as part of your [fiscal localization
> package](../../fiscal_localizations.html#fiscal-localizations-packages).

## Configuration

To edit or create a fiscal position, go to Accounting ‣ Configuration ‣ Fiscal
Positions, and open the record to modify or click New.

> **Note:**
>
> If any notes are legally required when using this fiscal position, add them in the
> Legal Notes… field below the [tax mapping]
> section to display them on quotations, sales orders, invoices, and bills.

### Tax mapping

Fiscal positions are required to map taxes. [Tax mapping](../taxes.html#taxes-tax-mapping) is configured on
taxes themselves.

### Account mapping

Account mapping is based on the income and expense accounts defined on the product or product
category. To map to another account, select the account to be replaced in the left column
(Account on Product) and select the account to use instead in the right column
(Account to Use Instead).

![Example of a fiscal position's account mapping](../../../../_images/fiscal-positions-account-mapping.png)

## Application

### Automatic application

To automatically apply a fiscal position following a set of conditions, go to
Accounting ‣ Configuration ‣ Fiscal Positions, open the fiscal position to
modify, and tick Detect Automatically.

From there, several conditions can be activated:

- VAT Required: the customer’s VAT number must be present on their contact form.
- Country Group and Country: the fiscal position is only applied to the
  selected country or country group.

![Example of a fiscal position automatic application settings](../../../../_images/fiscal-positions-automatic.png)
> **Note:**
>
> - If the [Verify VAT Numbers](vat_verification.html) feature is enabled, any fiscal positions
>   with VAT required enabled will require Intra-Community valid VAT numbers to apply
>   automatically.
> - Taxes on **eCommerce orders** are automatically updated once the customer has logged in or
>   filled out their billing details.

> **Warning:**
>
> The fiscal positions’ **sequence** defines which fiscal position is applied if all conditions
> set on multiple fiscal positions are met simultaneously.
>
> For example, suppose the first fiscal position in a sequence targets *country A* while the second
> fiscal position targets a *country group* that comprises *country A*. In that case, only the
> first fiscal position will be applied to customers from *country A*.

### Manual application

To manually select a fiscal position, open a sales order, purchase order, invoice, or bill, go to
the Other Info tab and select the desired Fiscal Position before adding
product lines.

![Selection of a fiscal position on a sales order, invoice, or bill](../../../../_images/fiscal-positions-manual.png)

### Assign to a partner

To define which fiscal position must be used by default for a specific partner, go to
Accounting ‣ Customers ‣ Customers, select the partner, open the
Sales & Purchase tab, and select the Fiscal Position.

![Selection of a fiscal position on a customer](../../../../_images/fiscal-positions-customer.png)
> **Note:**
>
> To view all partners at once instead of only customers, remove the Customer Invoices
> filter or use the **Contacts** application.

> **Note:**
>
> - [Taxes](../taxes.html)
> - [B2B (tax excluded) and B2C (tax included) pricing](B2B_B2C.html)

---

# AvaTax integration

Avalara’s *AvaTax* is a cloud-based tax software. Integrating *AvaTax* with Odoo provides real-time
and region-specific tax calculations when users sell, purchase, and invoice items in Odoo. *AvaTax*
tax calculation is supported with every United Nations charted country, including inter-border
transactions.

> **Warning:**
>
> *AvaTax* is only available for integration with databases/companies that have locations in the
> United States, Canada, and Brazil. This means the fiscal position/country of a database can only
> be set to the United States, Canada, or Brazil. For more information, reference this
> documentation: [Fiscal country].

*AvaTax* accounts for location-based tax rates for each state, county, and city. It improves
remittance accuracy by paying close attention to laws, rules, jurisdiction boundaries, and special
circumstances (like, tax holidays, and product exemptions). Companies who integrate with *AvaTax*
can maintain control of tax-calculations in-house with this simple API integration.

> **Warning:**
>
> Some limitations exist in Odoo while using AvaTax for tax calculation:
>
> - AvaTax uses the company address by default. To use the warehouse address, enable [Allow
>   Ship Later](../../../sales/point_of_sale/shop.html#pos-shop-ship) in the **POS** app settings.
> - Excise tax is **not** supported. This includes tobacco/vape taxes, fuel taxes, and other
>   specific industries.

> **Note:**
>
> Avalara’s support documents: [About AvaTax](https://community.avalara.com/support/s/document-item?language=en_US)

## Set up on AvaTax

To use *AvaTax*, an account with Avalara is required for the setup. If one has not been set up yet,
connect with Avalara to purchase a license: [Avalara: Let’s Talk](https://www.avalara.com/us/en/get-started.html?campaignID=701Uz00000kcMwLIAU&utm_campaign=AMER_PROS_Unpaid-Synd_General-Contact_07_2025_ODOO-Page---Contact-Us&marketing_channel=web_referral&vendor=partner&paid_unpaid=unpaid&target_audience=prospect).

> **Note:**
>
> Upon account setup, take note of the *AvaTax* Account ID. This will be needed in the
> [Odoo setup]. In Odoo, this number is the API
> ID.

Then, [create a basic company profile](https://www.odoo.com/r/2k0).

### Create basic company profile

Collect essential business details for the next step: locations where tax is collected,
products/services sold (and their sales locations), and customer tax exemptions, if applicable.
Follow the Avalara documentation for creating a basic company profile:

1. [Add company information](https://www.odoo.com/r/XZDW).
2. [Tell us where the company collects and pays tax](https://www.odoo.com/r/E6g).
3. [Verify jurisdictions and activate the company](https://www.odoo.com/r/NIy).
4. [Add other company locations for location-based filing](https://www.odoo.com/r/GF4).
5. [Add a marketplace to the company profile](https://www.odoo.com/r/QA5).

### Connect to AvaTax

After creating the basic company profile in Avalara, connect to *AvaTax*. This step links Odoo and
*AvaTax* bidirectionally.

Navigate to either Avalara’s [sandbox](https://sandbox.admin.avalara.com/) or [production](https://admin.avalara.com/) environment. This will depend on which type of Avalara account the
company would like to integrate.

> **Note:**
>
> [Sandbox vs production environments in Avalara](https://knowledge.avalara.com/bundle/fzc1692293626742/page/sandbox-vs-production.html).

Log in to create the License Key. Go to Settings ‣ License and API
Keys. Click Generate License Key.

> **Warning:**
>
> A warning appears stating: `If your business app is connected to Avalara solutions, the
> connection will be broken until you update the app with the new license key. This action cannot
> be undone.`
>
> Generating a new license key breaks the connection with existing business apps using the *AvaTax*
> integration. Make sure to update these apps with the new license key.

If this will be the first API integration being made
with *AvaTax* and Odoo, then click Generate license key.

If this is an additional license key, ensure the previous connection can be broken. There is
**only** one license key associated with each of the Avalara sandbox and production accounts.

> **Warning:**
>
> Copy this key to a safe place. It is strongly encouraged to back up the license key for
> future reference. This key **cannot** be retrieved after leaving this screen.

## Odoo configuration

Before using *AvaTax*, there are some additional configurations in Odoo to ensure tax calculations
are made accurately.

Verify that the Odoo database contains necessary data. The country initially set up in the database
determines the fiscal position, and aids *AvaTax* in calculating accurate tax rates.

### Fiscal country

To set the Fiscal Country, navigate to Accounting app ‣ Configuration
‣ Settings.

> **Note:**
>
> [Fiscal localizations](../../fiscal_localizations.html)

Under the Taxes section, set the Fiscal Country feature to United
States, Canada, or Brazil. Then, click Save.

### Company settings

All companies operating under the Odoo database should have a full and complete address listed in
the settings. Navigate to the Settings app, and under the Companies
section, ensure there is only one company operating the Odoo database. Click Update Info
to open a separate page to update company details.

If there are multiple companies operating in the database, click Manage Companies to
load a list of companies to select from. Update company information by clicking into the specific
company.

Database administrators should ensure that the Street…, Street2…,
City, State, ZIP, and Country are all updated for
the companies.

This ensures accurate tax calculations and smooth end-of-year accounting operations.

> **Note:**
>
> - [Companies](../../../general/companies.html)
> - [Get started](../get_started.html)

### Module installation

Next, ensure that the Odoo *AvaTax* module is installed. To do so, navigate to the
Apps application. In the Search… bar, type in `avatax`, and press
`Enter`. The following results populate:

| Name | Technical name | Description |
| --- | --- | --- |
| Avatax | `account_avatax` | Default *AvaTax* module. This module adds the base *AvaTax* features for tax calculation. |
| Avatax for geo localization | `account_avatax_geolocalize` | This module includes the features required for integration of *AvaTax* into geo-localization in Odoo. |
| Avatax for SO | `account_avatax_sale` | Includes the information needed for tax calculation on sales orders in Odoo. |
| Avatax for Inventory | `account_avatax_stock` | Includes tax calculation in Odoo Inventory. |
| Amazon/Avatax Bridge | `sale_amazon_avatax` | Includes tax calculation features between the *Amazon Connector* and Odoo. |
| Avatax Brazil | `l10n_br_avatax` | Includes information for tax calculation in the Brazil localization. |
| Avatax Brazil for Services | `l10n_br_avatax_services` | This module includes the required features for tax calculation for services in the Brazil localization. |
| Avatax Brazil Sale for Services | `l10n_br_edi_sale_services` | This module includes the required features for tax calculation for the sale of services in the Brazil localization. This includes electronic data interchange (EDI). |
| Test SOs for the Brazilian AvaTax | `l10n_br_test_avatax_sale` | This module includes the required features for test sales orders in the Brazil localization. |

Click the Install button on the module labeled, Avatax: `account_avatax`.
Doing so installs the following modules:

- Avatax: `account_avatax`
- Avatax for SO: `account_avatax_sale`
- Avatax for Inventory: `account_avatax_stock`

Should *AvaTax* be needed for geo-localization, or with the *Amazon Connector*, then install those
modules individually by clicking on Install on Avatax for geo localization
and Amazon/Avatax Bridge, respectively.

> **Note:**
>
> For localization specific *AvaTax* instructions, view the following [fiscal localization](../../fiscal_localizations.html) documentation:
>
> - [Brazil](../../fiscal_localizations/brazil.html)
> - [United States](../../fiscal_localizations/united_states.html)

### Odoo AvaTax settings

To integrate the *AvaTax* API with Odoo, go to
Accounting app ‣ Configuration ‣ Settings section. The AvaTax
fields in the Taxes section is where the *AvaTax* configurations are made, and the
credentials are entered in.

First, tick the checkbox to the left of the AvaTax settings, to activate *AvaTax* on the
database. This is a quick, convenient way to activate and deactivate *AvaTax* tax calculation on the
Odoo database.

![Configure AvaTax settings](../../../../_images/avatax-configuration-settings.png)

#### Prerequisites

First, select the Environment in which the company wishes to use *AvaTax* in. It can
either be Sandbox or Production.

> **Note:**
>
> For help determining which *AvaTax* environment to use (either Production or
> Sandbox), visit: [Sandbox vs Production environments](https://knowledge.avalara.com/bundle/fzc1692293626742/page/sandbox-vs-production.html).

#### Credentials

Now, the credentials can be entered in. The *AvaTax* Account ID should be entered in the
API ID field, and the License Key should be entered in the API
Key field.

> **Warning:**
>
> The Account ID can be found by logging into the *AvaTax* portal ([sandbox](https://sandbox.admin.avalara.com/) or [production](https://admin.avalara.com/)). In the
> upper-right corner, click on the initials of the user and Account. The
> Account ID is listed first.
>
> To access the License Key see this documentation:
> [Connect to AvaTax].

For the Company Code field, enter the Avalara company code for the company being
configured. Avalara interprets this as `DEFAULT`, if it is not set. The Company Code can
be accessed in the Avalara management portal.

First, log into the *AvaTax* portal ([sandbox](https://sandbox.admin.avalara.com/) or [production](https://admin.avalara.com/)). Then, navigate to Settings ‣ Manage Companies.
The Company Code value is located in the row of the Company in the
Company Code column.

![AvaTax company code highlighted on the company details page.](../../../../_images/company-code.png)

#### Transaction options

There are two transactional settings in the Odoo *AvaTax* settings that can be configured:
Use UPC and Commit Transactions.

If the checkbox next to Use UPC is ticked, the transactions will use Universal Product
Codes (UPC), instead of custom defined codes in Avalara. Consult a certified public accountant (CPA)
for specific guidance.

Should the Commit Transactions checkbox be ticked, then, the transactions in the Odoo
database will be committed for reporting in *AvaTax*.

#### Address validation

The *Address Validation* feature ensures that the most up-to-date address by postal standards is set
on a contact in Odoo. This is important to provide accurate tax calculations for customers.

> **Warning:**
>
> The Address Validation feature only works with partners/customers in North America.

Additionally, tick the checkbox next to the Address validation field.

> **Warning:**
>
> For accurate tax calculations, it is best practice to enter a complete address for the contacts
> saved in the database. However, *AvaTax* can still function by implementing a best effort attempt
> using only the Country, State, and Zip code. These are the
> three minimum required fields.

Save the settings to implement the configuration.

> **Note:**
>
> Manually Validate the address by navigating to the Contacts app, and
> selecting a contact. Now that the *AvaTax* module has been configured on the database, a
> Validate button appears directly below the Address.
>
> Click Validate, and a pop-up window appears with a Validated Address and
> Original Address listed. If the Validated Address is the correct mailing
> address for tax purposes, click Save Validated.
>
> ![Validate address pop-up window in Odoo with "Save Validated" button and "Validated Address" highlighted.](../../../../_images/validate-address.png)

> **Warning:**
>
> All previously-entered addresses for contacts in the Odoo database will need to be validated
> using the manually validate process outlined above. Addresses are not automatically validated if
> they were entered previously. This only occurs upon tax calculation.

#### Test connection

After entering all the above information into the *AvaTax* setup on Odoo, click Test
connection. This ensures the API ID and API KEY are correct, and a
connection is made between Odoo and the *AvaTax* application programming interface (API).

#### Sync parameters

Upon finishing the configuration and settings of the *AvaTax* section, click the Sync
Parameters button. This action synchronizes the exemption codes from *AvaTax*.

### Fiscal position

Next, navigate to Accounting app ‣ Configuration ‣ Accounting: Fiscal
Positions. A Fiscal Position is listed named, Automatic Tax Mapping
(AvaTax). Click it to open *AvaTax’s* fiscal position configuration page.

Here, ensure that the Use AvaTax API checkbox is ticked.

Optionally, tick the checkbox next to the field labeled: Detect Automatically. Should
this option be ticked, then, Odoo will automatically apply this Fiscal Position for
transactions in Odoo.

Enabling Detect Automatically also makes specific parameters, such as VAT
required, Foreign Tax ID, Country Group, Country,
Federal States, or Zip Range appear. Filling these parameters filters the
Fiscal Position usage. Leaving them blank ensures all calculations are made using this
Fiscal Position.

> **Warning:**
>
> Should the Detect Automatically checkbox not be ticked, each customer will need to
> have the Fiscal Position set on their Sales and Purchase tab of the
> contact record. To do so, navigate to Sales app ‣ Order ‣ Customers, or
> Contacts app ‣ Contacts. Then, select a customer or contact to set the fiscal
> position on.
>
> Navigate to the Sales and Purchase tab, and down to the section labeled,
> Fiscal Position. Set the Fiscal Position field to the fiscal position
> for the customer.

> **Note:**
>
> [Fiscal positions (tax and account mapping)](fiscal_positions.html)

#### AvaTax accounts

Upon selecting the checkbox option for Use AvaTax API a new AvaTax tab
appears. Click into this tab to reveal two different settings.

The first setting is the AvaTax Invoice Account, while the second is, AvaTax
Refund Account. Ensure both accounts are set for smooth end-of-year record keeping. Consult a
certified public accountant (CPA) for specific guidance on setting both accounts.

Click Save to implement the changes.

### Tax mapping

The *AvaTax* integration is available on sale orders and invoices with the included *AvaTax* fiscal
position.

> **Note:**
>
> Additionally, there is a Tax Mapping tab and Account Mapping tab in the
> Automatic Tax Mapping (AvaTax) fiscal position, where mapping for products can also
> be configured. To access Fiscal Positions navigate to Accounting app
> ‣ Configuration ‣ Accounting: Fiscal Positions.

#### Product category mapping

Before using the integration, specify an Avatax Category on the product categories.
Navigate to Inventory app ‣ Configuration ‣ Product Categories. Select the
product category to add the AvaTax Category to. In the AvaTax Category
field, select a category from the drop-down menu, or Search More… to open the complete
list of options.

![Specify AvaTax Category on products.](../../../../_images/avatax-category.png)

#### Product mapping

*AvaTax* Categories may be set on individual products, as well. To set the Avatax
Category navigate to Inventory app ‣ Products ‣ Products. Select the product
to add the Avatax Category to. Under the General Information tab, on the
far-right, is a selector field labeled: Avatax Category. Finally, click the drop-down
menu, and select a category, or Search More… to find one that is not listed.

> **Note:**
>
> If both the product, and its category, have an AvaTax Category set, the product’s
> AvaTax Category takes precedence.

![Override product categories as needed.](../../../../_images/override-avatax-product-category.png)
> **Warning:**
>
> Mapping an AvaTax Category on either the *Product* or *Product Category* should be
> completed for every *Product* or *Product Category*, depending on the route that is chosen.

> **Note:**
>
> - [Fiscal positions (tax and account mapping)](fiscal_positions.html)
> - [AvaTax use](avatax/avatax_use.html)
> - [Avalara (Avatax) portal](avatax/avalara_portal.html)
> - [US Tax Compliance: Avatax elearning video](https://www.odoo.com/slides/slide/us-tax-compliance-avatax-2858?fullscreen=1)

---

# EU intra-community distance selling

EU intra-community distance selling involves the cross-border trade of goods and services from
vendors registered for VAT purposes to individuals (B2C) located in a European Union member state.
The transaction is conducted remotely, typically through online platforms, mail orders, telephone,
or other means of communication.

EU intra-community distance selling is subject to specific VAT rules and regulations. The vendor
must charge VAT per the VAT rate applicable in the buyer’s country.

> **Note:**
>
> This remains applicable even if the vendor is located outside of the European Union.

## Configuration

The **EU Intra-community Distance Selling** feature helps you comply with this regulation by
creating and configuring new **fiscal positions** and **taxes** based on your company’s country. To
enable it, go to Accounting ‣ Configuration ‣ Settings ‣ Taxes, tick
EU Intra-community Distance Selling, and Save.

![EU intra-community Distance Selling feature in Odoo Accounting settings](../../../../_images/enable-feature.png)
> **Note:**
>
> Whenever you add or modify taxes, you can automatically update your fiscal positions. To do so,
> go to Accounting/Invoicing ‣ Settings ‣ Taxes ‣ EU Intra-community Distance
> Selling and click on the Refresh tax mapping.

> **Note:**
>
> We highly recommend checking that the proposed mapping is suitable for the products and services
> you sell before using it.

> **Note:**
>
> - [Taxes](../taxes.html)
> - [Fiscal localizations](../../fiscal_localizations.html)
> - [Fiscal positions (tax and account mapping)](fiscal_positions.html)

## One-Stop Shop (OSS)

The OSS system introduced by the European Union simplifies VAT collection
for **cross-border** sales of goods and services. It primarily applies to business-to-consumer
**(B2C)** cases. With the OSS, businesses can register for VAT in their home country and use a
single online portal to handle VAT obligations for their sales within the EU. There are **two
primary schemes**: the **Union OSS** scheme for cross-border services and the **Import OSS** scheme
for goods valued at or below €150.

### Reports

To generate **OSS sales** or **OSS imports** reports and submit them onto the OSS portal, go to
Accounting ‣ Reporting ‣ Tax Report, click Report: Generic Tax
report, and select either OSS Sales or OSS Imports. Once selected, click on
PDF, XLSX, or XML in the top-left corner. This generates the
currently-opened report in the selected format. Once generated, log into the platform of your
competent federal authority to submit it onto the OSS portal.

![OSS reports view](../../../../_images/oss-report.png)
> **Note:**
>
> - [European Commission: OSS | Taxation and Customs Union](https://ec.europa.eu/taxation_customs/business/vat/oss_en)

---

# B2B (tax excluded) and B2C (tax included) pricing

When working with consumers, prices are usually expressed with taxes included in the price (e.g., in
most eCommerce). But, when you work in a B2B environment, companies usually negotiate prices with
taxes excluded.

Odoo manages both use cases easily, as long as you register your prices on the product with taxes
excluded or included, but not both together. If you manage all your prices with tax included (or
excluded) only, you can still easily do sales order with a price having taxes excluded (or included)
: that’s easy.

This documentation is only for the specific use case where you need to have two references for the
price (tax included or excluded), for the same product. The reason of the complexity is that there
is not a symmetrical relationship with prices included and prices excluded, as shown in this use
case, in Belgium with a tax of 21%:

- Your eCommerce has a product at **10€ (taxes included)**
- This would do **8.26€ (taxes excluded)** and a **tax of 1.74€**

But for the same use case, if you register the price without taxes on the product form (8.26€), you
get a price with tax included at 9.99€, because:

- **8.26€ \* 1.21 = 9.99€**

So, depending on how you register your prices on the product form, you will have different results
for the price including taxes and the price excluding taxes:

- Taxes Excluded: **8.26€ & 10.00€**
- Taxes Included: **8.26€ & 9.99€**

> **Note:**
>
> If you buy 100 pieces at 10€ taxes included, it gets even more tricky. You will get: **1000€
> (taxes included) = 826.45€ (price) + 173.55€ (taxes)** Which is very different from a price per
> piece at 8.26€ tax excluded.

This documentation explains how to handle the very specific use case where you need to handle the
two prices (tax excluded and included) on the product form within the same company.

> **Note:**
>
> In terms of finance, you have no more revenues selling your product at 10€ instead of 9.99€ (for a
> 21% tax), because your revenue will be exactly the same at 9.99€, only the tax is 0.01€ higher.
> So, if you run an eCommerce in Belgium, make your customer a favor and set your price at 9.99€
> instead of 10€. Please note that this does not apply to 20€ or 30€, or other tax rates, or a
> quantity >1. You will also make you a favor since you can manage everything tax excluded, which is
> less error prone and easier for your salespeople.

## Configuration

### Introduction

The best way to avoid this complexity is to choose only one way of managing your prices and stick to
it: price without taxes or price with taxes included. Define which one is the default stored on the
product form (on the default tax related to the product), and let Odoo compute the other one
automatically, based on the pricelist and fiscal position. Negotiate your contracts with customers
accordingly. This perfectly works out-of-the-box and you have no specific configuration to do.

If you can not do that and if you really negotiate some prices with tax excluded and, for other
customers, others prices with tax included, you must:

1. always store the default price **tax excluded** on the product form, and apply a tax (price
   excluded on the product form)
2. create a pricelist with prices in **tax included**, for specific customers
3. create a fiscal position that switches the tax excluded to a tax included
4. assign both the pricelist and the fiscal position to customers who want to benefit to this
   pricelist and fiscal position

For the purpose of this documentation, we will use the above use case:

- your product default sale price is 8.26€ tax excluded
- but we want to sell it at 10€, tax included, in our shops or eCommerce website

### Setting your products

Your company must be configured with tax excluded by default. This is usually the default
configuration, but you can check your **Default Sale Tax** from the menu
Configuration ‣ Settings of the Accounting application.

![../../../../_images/price_B2C_B2B01.png](../../../../_images/price_B2C_B2B01.png)

Once done, you can create a **B2C** pricelist. You can activate the pricelist feature per customer
from the menu: Configuration ‣ Settings of the Sale application. Choose the
option **different prices per customer segment**.

Once done, create a B2C pricelist from the menu Configuration ‣ Pricelists. It’s
also good to rename the default pricelist into B2B to avoid confusion.

Then, create a product at 8.26€, with a tax of 21% (defined as tax not included in price) and set a
price on this product for B2C customers at 10€, from the Sales ‣ Products menu of
the Sales application:

![../../../../_images/price_B2C_B2B02.png](../../../../_images/price_B2C_B2B02.png)

### Setting the B2C fiscal position

From the accounting application, create a B2C fiscal position from this menu:
Configuration ‣ Fiscal Positions. This fiscal position should map the VAT 21%
(tax excluded of price) with a VAT 21% (tax included in price)

![../../../../_images/price_B2C_B2B03.png](../../../../_images/price_B2C_B2B03.png)

## Test by creating a quotation

Create a quotation from the Sale application, using the Sales ‣ Quotations menu.
You should have the following result: 8.26€ + 1.73€ = 9.99€.

![../../../../_images/price_B2C_B2B04.png](../../../../_images/price_B2C_B2B04.png)

Then, create a quotation but **change the pricelist to B2C and the fiscal position to B2C** on the
quotation, before adding your product. You should have the expected result, which is a total price
of 10€ for the customer: 8.26€ + 1.74€ = 10.00€.

![../../../../_images/price_B2C_B2B05.png](../../../../_images/price_B2C_B2B05.png)

This is the expected behavior for a customer of your shop.

## Avoid changing every sale order

If you negotiate a contract with a customer, whether you negotiate tax included or tax excluded, you
can set the pricelist and the fiscal position on the customer form so that it will be applied
automatically at every sale of this customer.

The pricelist is in the **Sales & Purchases** tab of the customer form, and the fiscal position is
in the accounting tab.

Note that this is error prone: if you set a fiscal position with tax included in prices but use a
pricelist that is not included, you might have wrong prices calculated for you. That’s why we
usually recommend companies to only work with one price reference.

---

# Customer invoices

A customer invoice is a document issued by a company for products and/or services sold to a
customer. It records receivables as they are sent to customers. Customer invoices can include
amounts due for the goods and/or services provided, applicable sales taxes, shipping and handling
fees, and other charges. Odoo supports multiple invoicing and payment workflows.

> **Note:**
>
> [Invoicing processes](customer_invoices/overview.html)

From draft invoice to profit and loss report, the process involves several steps once the goods (or
services) have been ordered/shipped (or rendered) to a customer, depending on the invoicing policy:

- [Invoice creation]
- [Invoice confirmation]
- [Invoice sending]
- [Payment and reconciliation]
- [Payment follow-up]
- [Reporting]

## Invoice creation

Draft invoices can be created directly from documents like sales orders or purchase orders or
manually from the Customer Invoices journal in the Accounting Dashboard.

An invoice must include the required information to enable the customer to pay promptly for their
goods and services. Make sure the following fields are appropriately completed:

- Customer: When a customer is selected, Odoo automatically pulls information from the
  customer record like the invoice address,
  [preferred payment terms](customer_invoices/payment_terms.html),
  [fiscal positions](taxes/fiscal_positions.html), receivable account, and more onto the invoice.
  To change these values for this specific invoice, edit them directly on the invoice. To change
  them for future invoices, change the values on the contact record.
- Invoice Date: If not set manually, this field is automatically set as the current date
  upon confirmation.
- Due Date or [payment terms](customer_invoices/payment_terms.html): To specify when
  the customer has to pay the invoice.
- Journal: Automatically set and can be changed if needed.
- [Currency](get_started/multi_currency.html). If the invoice’s currency differs from the
  company’s currency, the currency exchange rate is automatically displayed.

In the Invoice Lines tab:

- Product: Click Add a line, then search for and select the product.
- Quantity
- Price
- [Taxes](taxes.html) (if applicable)

To access the product catalog and view all items in an organized display, click [Catalog](../../inventory_and_mrp/inventory/warehouses_storage/inventory_management/product_catalog.html).
When the products and quantities are selected, click Back to Invoice to return to the
invoice; the selected catalog items will appear in the invoice lines.

> **Note:**
>
> To display the total amount of the invoice in words, go to Accounting ‣
> Configuration ‣ Settings and activate the Total amount of invoice in letters
> option.

The Journal Items tab displays the accounting entries created. Additional invoice
information such as the Customer Reference, Payment Reference, [Fiscal
Positions](taxes/fiscal_positions.html), [Incoterms](customer_invoices/incoterms.html), and more can be
added or modified in the Other Info tab.

> **Note:**
>
> Odoo initially creates invoices in Draft status. Draft invoices have no accounting
> impact until they are [confirmed].

> **Note:**
>
> [Pro-forma invoices](../../sales/sales/invoicing/proforma.html)

## Invoice confirmation

Click Confirm when the invoice is completed. The invoice’s status changes to
Posted, and a journal entry is generated based on the invoice configuration. On
confirmation, Odoo assigns each invoice a unique number from a defined [sequence](customer_invoices/sequence.html).

> **Note:**
>
> - Once confirmed, an invoice can no longer be updated. Click Reset to draft if
>   changes are needed.
> - If required, invoices and other journal entries can be locked once posted using the
>   [Secure posted entries with hash](reporting/data_inalterability.html#data-inalterability-restricted) feature.

## Invoice sending

To set a preferred Invoice sending method for a customer, go to
Accounting ‣ Customers ‣ Customers and select the customer. In the
Accounting tab of the contact form, select the preferred Invoice sending
method in the Customer Invoices section.

> **Note:**
>
> Sending letters in Odoo requires [In-App Purchase (IAP)](../../essentials/in_app_purchase.html)
> credit or tokens.

To send the invoice to the customer, navigate back to the invoice record and follow these steps:

1. Click Send.
2. If the [default invoice layout](../../studio/pdf_reports.html#studio-pdf-reports-default-layout) has not been customized
   yet, a Configure your document layout pop-up window appears. Configure the layout and
   click Continue.

   > **Note:**
   > - The document layout can be changed at any time in the general settings.
   > - To add a QR code for banking app payments to the invoice, enable the QR Code
   >   option in the Configure Your Document Layout window. To modify this option, go
   >   to Accounting ‣ Configuration ‣ Settings, scroll down to the
   >   Customer Payments section, and enable/disable the QR Codes option.
3. In the Send window:

   - If a preferred Invoice sending method was set in the contact form, it is selected
     by default. Select another one if needed.
   - If no preferred Invoice sending method was set in the contact form, select the
     method to use for sending the invoice to the customer.
4. Click Send if the by Email option is selected, or click
   Download.

### Sending multiple invoices

To send multiple invoices, go to Accounting ‣ Customers ‣ Invoices,
select them in the Invoices list view and click Send. The
Send window displays the number of selected invoice to send by email.

After clicking Send, a banner is added to the selected invoices to indicate they are
part of an ongoing send batch. This helps prevent the process from being triggered manually again,
as it may take some time to complete for exceptionally large batches.

To check all invoices that have not yet been sent, go to Accounting ‣ Customers
‣ Invoices. In the Invoices list view, click into the search bar and filter on
Not Sent.

## Payment and reconciliation

In Odoo, an invoice is considered Paid when the associated accounting entry has been
reconciled with a corresponding bank transaction.

> **Note:**
>
> - [Payments](payments.html)
> - [Bank reconciliation](bank/reconciliation.html)

## Payment follow-up

Odoo’s [follow-up actions](payments/follow_up.html) help companies follow up on customer invoices.
Different actions can be set up to remind customers to pay their outstanding invoices, depending on
how much the customer is overdue. These actions are bundled into follow-up levels that trigger when
an invoice is overdue by a certain number of days. If there are multiple overdue invoices for the
same customer, the actions are performed on the most overdue invoice.

## Reporting

### Partner reports

#### Partner Ledger

The Partner Ledger report shows the balance of customers and suppliers. To access it,
go to Accounting ‣ Reporting ‣ Partner Ledger.

#### Aged Receivable

To review outstanding customer invoices and their related due dates, use the [Aged Receivable](reporting.html#accounting-reporting-aged-receivable) report. To access it, go to Accounting ‣
Reporting ‣ Aged Receivable.

#### Aged Payable

To review outstanding vendor bills and their related due dates, use the [Aged Payable](reporting.html#accounting-reporting-aged-payable) report. To access it, go to Accounting ‣
Reporting ‣ Aged Payable.

### Profit and Loss

The [Profit and Loss](reporting.html#accounting-reporting-profit-and-loss) statement shows details of income
and expenses.

### Balance sheet

The [Balance Sheet](reporting.html#accounting-reporting-balance-sheet) summarizes the company’s assets,
liabilities, and equity at a specific time.

---

# Invoicing processes

Depending on your business and the application you use, there are
different ways to automate the customer invoice creation in Odoo.
Usually, draft invoices are created by the system (with information
coming from other documents like sales order or contracts) and
accountant just have to validate draft invoices and send the invoices in
batch (by regular mail or email).

Depending on your business, you may opt for one of the following way to
create draft invoices:

## Sales

### Sales Order ‣ Invoice

In most companies, salespeople create quotations that become sales order
once they are validated. Then, draft invoices are created based on the
sales order. You have different options like:

- Invoice manually: use a button on the sale order to trigger the draft
  invoice
- Invoice before delivery: invoice the full order before triggering the
  delivery order
- Invoice based on delivery order: see next section

Invoice before delivery is usually used by the eCommerce application
when the customer pays at the order and we deliver afterwards.
(pre-paid)

For most other use cases, it’s recommended to invoice manually. It
allows the salesperson to trigger the invoice on demand with options:
invoice the whole order, invoice a percentage (advance), invoice some
lines, invoice a fixed advance.

This process is good for both services and physical products.

> **Note:**
>
> - [Pro-forma invoices](../../../sales/sales/invoicing/proforma.html)

> **Note:**
>
> Invoices can also be generated from sales orders created in the [Repairs
> app](../../../inventory_and_mrp/repairs.html) for invoicing after-sales
> services.

### Sales Order ‣ Delivery Order ‣ Invoice

Retailers and eCommerce usually invoice based on delivery orders,
instead of sales order. This approach is suitable for businesses where
the quantities you deliver may differs from the ordered quantities:
foods (invoice based on actual Kg).

This way, if you deliver a partial order, you only invoice for what you
really delivered. If you do back orders (deliver partially and the rest
later), the customer will receive two invoices, one for each delivery
order.

> **Note:**
>
> - [Invoicing policies](../../../sales/sales/invoicing/invoicing_policy.html)

### eCommerce Order ‣ Invoice

An eCommerce order will also trigger the creation of the order when it
is fully paid. If you allow paying orders by check or wire transfer,
Odoo only creates an order and the invoice will be triggered once the
payment is received.

## Contracts

### Regular Contracts ‣ Invoices

If you use contracts, you can trigger invoice based on time and material
spent, expenses or fixed lines of services/products. Every month, the
salesperson will trigger invoice based on activities on the contract.

Activities can be:

- fixed products/services, coming from a sale order linked to this contract
- materials purchased (that you will re-invoice)
- time and material based on timesheets or purchases (subcontracting)
- expenses like travel and accommodation that you re-invoice to the customer

You can invoice at the end of the contract or trigger intermediate
invoices. This approach is used by services companies that invoice
mostly based on time and material. For services companies that invoice
on fix price, they use a regular sales order.

> **Note:**
>
> - [Invoicing based on time and materials](../../../sales/sales/invoicing/time_materials.html)
> - [Invoicing processes](#)
> - [Invoice project milestones](../../../sales/sales/invoicing/milestone.html)

### Recurring Contracts ‣ Invoices

For subscriptions, an invoice is triggered periodically, automatically.
The frequency of the invoicing and the services/products invoiced are
defined on the contract.

> **Note:**
>
> - [Subscriptions](../../../sales/subscriptions.html)

## Others

### Creating an invoice manually

Users can also create invoices manually without using contracts or a
sales order. It’s a recommended approach if you do not need to manage
the sales process (quotations), or the delivery of the products or
services.

Even if you generate the invoice from a sales order, you may need to
create invoices manually in exceptional use cases:

- if you need to create a refund
- If you need to give a discount
- if you need to change an invoice created from a sales order
- if you need to invoice something not related to your core business

### Resequencing of the invoices

It remains possible to resequence the invoices but with some restrictions:

1. The feature does not work when entries are previous to a lock date.
2. The feature does not work if the sequence is inconsistent with the month of the entry.
3. It does not work if the sequence leads to a duplicate.
4. The order of the invoice remains unchanged.
5. It is useful for people who use a numbering from another software and who want to continue the
   current year without starting over from the beginning.

### Invoice digitization with optical character recognition (OCR)

**Invoice digitization** is the process of automatically encoding traditional paper invoices into
invoices forms in your accounting.

Odoo uses OCR and artificial intelligence technologies to recognize the content of the documents.
Vendor bills and customer invoices forms are automatically created and populated based on scanned
invoices.

> **Note:**
>
> - [Document digitization](../vendor_bills/invoice_digitization.html)

---

# Delivery and invoice addresses

Companies often have multiple locations, and it is common that a customer invoice should be sent to
one address and the delivery should be sent to another. Odoo’s **Customer Addresses** feature is
designed to handle this scenario by making it easy to specify which address to use for each case.

> **Note:**
>
> [Invoicing processes](overview.html)

## Configuration

To specify a sales order’s invoice and delivery addresses, first go to Accounting
‣ Configuration ‣ Settings. In the Customer Invoices section, enable
Customer Addresses and click Save.

On quotations and sales orders, there are now fields for Invoice Address and
Delivery Address. If the customer has an invoice or delivery address listed on their
[contact record](../../../sales/sales/sales_quotations/different_addresses.html#sales-send-quotations-contact-form-config), the corresponding field uses that
address, by default, but any contact’s address can be used instead.

> **Note:**
>
> For more information, refer to the documentation on [Contact Form Configuration](../../../sales/sales/sales_quotations/different_addresses.html#sales-send-quotations-contact-form-config).

## Invoice and deliver to different addresses

Delivery orders and their delivery slip reports use the address set as the Delivery
Address on the sales order. By default, invoice reports show both the shipping address and the
invoice address to assure the customer that the delivery is going to the correct location.

Emails also go to different addresses. The quotation and sales order are sent to the main contact’s
email, as usual, but the invoice is sent to the email of the address set as the
Invoice Address on the sales order.

> **Note:**
>
> - Reports, such as the delivery slip and invoice report, can be [customized using Studio](../../../studio/pdf_reports.html).
> - If [Send by Post](snailmail.html) is checked when you click Send, the
>   invoice will be mailed to the invoice address.

---

# Payment terms and installment plans

**Payment terms** specify all the conditions of a sale’s payment to help ensure customers pay their
invoices correctly and on time.

Payment terms are generally defined on documents such as sales orders, customer invoices, and
vendor bills. Payment terms cover:

- The due date(s)
- Early payment discounts
- Any other conditions on the payment

An **installment plan** allows the customers to pay an invoice in parts, with the amounts and
payment dates defined beforehand by the seller.

> **Tip:**
>
> Immediate Payment
> :   The full payment is due on the day of the invoice’s issuance.
>
> 15 Days (or Net 15)
> :   The full payment is due 15 days after the invoice date.
>
> 21 MFI
> :   The full payment is due by the 21st of the month following the invoice date.
>
> 30% Advance End of Following Month
> :   30% is due on the day of the invoice’s issuance. The remaining balance is due at the end of the
>     following month.
>
> 2% 10, Net 30 EOM
> :   A 2% [cash discount](cash_discounts.html) if the payment is received within ten days.
>     Otherwise, the full payment is due at the end of the month following the invoice date.

> **Note:**
>
> - Payment terms are not to be confused with [down payment invoices](../../../sales/sales/invoicing/down_payment.html). If, for a specific order, you issue
>   multiple invoices to your customer, that is neither a payment term nor an installment plan but
>   an invoicing policy.
> - This page is about the *payment terms* feature, not [terms & conditions](terms_conditions.html), which can be used to declare contractual obligations regarding content
>   use, return policies, and other policies surrounding the sale of goods and services.

> **Note:**
>
> - [Odoo Tutorials: payment terms](https://www.odoo.com/slides/slide/payment-terms-1679)
> - [Cash discounts and tax reduction](cash_discounts.html)

## Configuration

To create new payment terms, follow these steps:

1. Go to Accounting ‣ Configuration ‣ Payment Terms and click on
   New.
2. Enter a name in the Payment Terms field. This field is the name displayed both
   internally and on sales orders.
3. Tick the Early Discount checkbox and fill out the discount percentage, discount days,
   and [tax reduction](cash_discounts.html#cash-discounts-tax-reductions) fields to add a [cash discount](cash_discounts.html), if desired.
4. In the Due Terms section, add a set of rules (terms) to define what needs to be paid
   and by which due date(s). Defining terms automatically calculates the payments’ due date(s). This
   is particularly helpful for managing **installment plans** (payment terms with multiple
   terms).

   To add a term, click on Add a line, define the discount’s value and type in the
   Due fields, then fill out the After fields to determine the due date.

   > **Note:**
   >
   > The Days end of the month on the option allows you to add a [buffer period] so that an invoice registered at the end of the month isn’t
   > due at the beginning of the month that immediately follows.
5. Enter the text to be displayed on the document (sales order, invoice, etc.) in the gray textbox
   in the Preview column.
6. Tick the Show installment dates checkbox to display a breakdown of each payment and
   its due date on the invoice report, if desired.

> **Note:**
>
> To instead specify a number of days *before the end of the month*, use a negative value in the
> After field.

To test that your payment terms are configured correctly, enter an invoice date on the
Example line to generate the payments that would be due and their due dates
using these payment terms.

> **Warning:**
>
> Terms are computed in the order of their due dates.

> **Tip:**
>
> In the following example, 30% is due on the day of issuance, and the remaining 70% is due at the
> end of the following month.
>
> ![Example of Payment Terms. The first line is the 30% due immediately. The second line is the remaining 70% due at the end of the following month.](../../../../_images/configuration.png)

### End of the month buffer

The Days end of the month on the option allows users to add a buffer period so that an
invoice registered at the end of the month isn’t due at the beginning of the month that immediately
follows.

When using this option, Odoo calculates the due date by taking the invoice date, adding the integer
in the After field, going to the end of the resulting month, and then adding the integer
from the Days on the next month field.

> **Tip:**
>
> For example, take two invoices, one dated 5 March and the other dated 28 March. Both use the same
> payment terms with a single Due Terms line for 100% of the due amount, due `5`
> Days end of the month on the `1`.
>
> For the invoice dated 5 March, the due date is computed as **1 April** with the following
> calculations:
>
> - 5 March + 5 days = 10 March
> - 10 March + end of the month = 31 March
> - 31 March + on the 1 = 1 April
>
> For the invoice dated 28 March, the due date is computed as **1 May** with the following
> calculations:
>
> - 28 March + 5 days = 2 April
> - 2 April + end of the month = 30 April
> - 30 April + on the 1 = 1 May

## Using payment terms

Payment terms can be defined using the Payment Terms field on:

- **Contacts:** To automatically set default payment terms on a contact’s new sales orders,
  invoices, and bills. This can be modified in the contact form, under the Sales &
  Purchase tab.
- **Quotations/Sales Orders:** To set specific payment terms automatically on all invoices generated
  from a quotation or sales order.

Payment terms can be defined using the Due Date field, with the Terms
drop-down list on:

- **Customer invoices:** To set specific payment terms on an invoice.
- **Vendor bills:** To set specific payment terms on a bill.

> **Note:**
>
> Setting payment terms on a vendor bill is mostly useful for managing vendor terms with multiple
> installments or cash discounts. Otherwise, manually setting the **due date** is enough. If
> payment terms are already defined, empty the field to select a date.

## Journal entries

Invoices with specific payment terms generate different *journal entries*, with one *journal item*
for every computed *due date*.

This makes for easier [follow-ups](../payments/follow_up.html) and
[reconciliation](../bank/reconciliation.html) since Odoo takes each
due date into account, rather than just the balance due date. It also helps to get an accurate
[aged receivable report](../customer_invoices.html#accounting-invoices-aging-report).

> **Tip:**
> ![The amount debited to the account receivable is split into two journal items with distinct due dates](../../../../_images/journal-entry.png)
>
> In this example, an invoice of $1000 has been issued with the following payment terms: *30% is
> due on the day of issuance, and the remaining 70% is due at the end of the following month.*
>
> | Account | Due date | Debit | Credit |
> | --- | --- | --- | --- |
> | Account Receivable | February 21 | 300 |  |
> | Account Receivable | March 31 | 700 |  |
> | Product Sales |  |  | 1000 |
>
> The $1000 debited to the account receivable is split into two distinct journal items. Both of
> them have their own due date.

---

# Default terms and conditions (T&C)

Specifying terms and conditions is essential to establish important contractual points, such as
return and refunds, warranty, and after-sale services.

You can add default terms and conditions at the bottom of all customer invoices, sales orders, and
quotations, either as text or a link to a web page.

> **Note:**
>
> [Odoo Tutorial: Terms & Conditions](https://www.odoo.com/slides/slide/terms-conditions-1680)

## Configuration

Go to Accounting ‣ Configuration ‣ Settings. Under the Customer
Invoices, enable Default Terms & Conditions. By default, the Add a Note
option is selected, and the terms and conditions are displayed at the bottom of the document. Enter
the terms and conditions in the text box below.

![Example of terms and conditions as a note](../../../../_images/terms-note.png)
> **Note:**
>
> You can also add a PDF version of your terms and conditions as an attachment when sending the
> document via email. Edit the email templates if you want to include them by default.

Alternatively, to display the terms and conditions on a web page, select the Add a link
to a Web Page option and click Save. Click Update Terms, edit the
content, and click Save. The link to that page is then added as a note in your document.

> **Note:**
>
> You can edit the layout and content of the page using the [Website](../../../websites/website.html) app. If the Website app is activated, the Edit in
> Website Builder option then replaces Update Terms.

![Example of terms and conditions as a web page](../../../../_images/terms-webpage.png)

---

# Cash discounts and tax reduction

**Cash discounts** are reductions in the amount a customer must pay for goods or services offered as
an incentive for paying their invoice promptly. These discounts are typically a percentage of the
total invoice amount and are applied if the customer pays within a specified time. Cash discounts
can help a company maintain a steady cash flow.

> **Tip:**
>
> You issue a €100 invoice on the 1st of January. The full payment is due within 30 days, and you
> also offer a 2% discount if your customer pays you within seven days.
>
> The customer can pay €98 up to the 8th of January. After that date, they would have to pay €100
> by the 31st of January.

A [tax reduction] can also be applied depending on the country
or region.

> **Note:**
>
> - [Payment terms and installment plans](payment_terms.html)
> - [Payments](../payments.html)

## Configuration

To grant cash discounts to customers, you must first verify the [gain and loss accounts]. Then, configure [payment terms] and add a cash discount by checking the Early Discount
checkbox and filling in the discount percentage, discount days, and [tax
reduction] fields.

### Cash discount gain/loss accounts

With a cash discount, the amount you earn depends on whether the customer benefits from the cash
discount or not. This inevitably leads to gains and losses, which are recorded on default accounts.

To modify these accounts, go to Accounting ‣ Configuration ‣ Settings, and, in
the Default Accounts section, select the accounts you want to use for the
Cash Discount Gain account and Cash Discount Loss account.

### Payment terms

Cash discounts are defined on [payment terms](payment_terms.html). Configure them to your liking by
going to Accounting ‣ Configuration ‣ Payment Terms, and make sure to fill out
the discount percentage, discount days, and [tax reduction]
fields.

![Configuration of payment terms named "2/7 Net 30". The field "Description on Invoices" reads: "Payment terms: 30 Days, 2% Early Payment Discount under 7 days".](../../../../_images/payment-terms.png)

### Tax reductions

Depending on the country or region, the base amount used to compute the tax can vary, which can lead
to a **tax reduction**. Since tax reductions are set on individual payment terms, each term can use
a specific tax reduction.

To configure how the tax reduction is applied, go to a payment term with the Early
Discount checkbox enabled, and select one of the three following options:

- Always (upon invoice)
  :   The tax is always reduced. The base amount used to compute the tax is the discounted amount,
      whether the customer benefits from the discount or not.
- On early payment
  :   The tax is reduced only if the customer pays early. The base amount used to compute the tax is the
      same as the sale: if the customer benefits from the reduction, then the tax is reduced. This means
      that, depending on the customer, the tax amount can vary after the invoice is issued.
- Never
  :   The tax is never reduced. The base amount used to compute the tax is the full amount, whether the
      customer benefits from the discount or not.

> **Tip:**
>
> You issue a €100 invoice (tax-excluded) on the 1st of January, with a 21% tax rate. The full
> payment is due within 30 days, and you also offer a 2% discount if your customer pays you within
> seven days.
>
> Always (upon invoice)On early paymentNever
>
> | Due date | Total amount due | Computation |
> | --- | --- | --- |
> | 8th of January | €118.58 | €98 + (21% of €98) |
> | 31st of January | €120.58 | €100 + (21% of €98) |
>
> | Due date | Total amount due | Computation |
> | --- | --- | --- |
> | 8th of January | €118.58 | €98 + (21% of €98) |
> | 31st of January | €121.00 | €100 + (21% of €100) |
>
> | Due date | Total amount due | Computation |
> | --- | --- | --- |
> | 8th of January | €119.00 | €98 + (21% of €100) |
> | 31st of January | €121.00 | €100 + (21% of €100) |

> **Note:**
>
> - [Tax grids](../reporting/tax_returns.html#accounting-tax-returns-tax-grids), which are used for the tax report, are
>   correctly computed according to the [type of tax reduction] you configured.
> - The **type of cash discount tax reduction** may be correctly pre-configured, depending on your
>   [fiscal localization package](../../fiscal_localizations.html#fiscal-localizations-packages).

## Apply a cash discount to a customer invoice

On a customer invoice, apply a cash discount by selecting the [payment terms you created]. Odoo automatically computes the correct amounts, tax amounts, due
dates, and accounting records.

Under the Journal Items tab, you can display the discount details by clicking on the
“toggle” button and adding the Discount Date and Discount Amount columns.

![An invoice of €100.00 with "2/7 Net 30" selected as payment terms. The "Journal Items" tab is open, and the "Discount Date" and "Discount Amount" columns are displayed.](../../../../_images/invoice-journal-entry.png)

The discount amount and due date are also displayed on the generated invoice report sent to the
customer if the Show installment dates option is checked on the payment terms.

![An invoice of €100.00 with the following text added to the terms and conditions: "30 Days, 2% Early Payment Discount under 7 days. 118.58 € due if paid before 01/08/2023."](../../../../_images/invoice-print.png)

### Payment reconciliation

When you record a [payment](../payments.html) or [reconcile your bank transactions](../bank/reconciliation.html), Odoo takes the customer payment’s date into account to determine if the
customer can benefit from the cash discount or not.

> **Note:**
>
> If your customer pays the discount amount *after* the discount date, you can always decide to
> mark the invoice as fully paid with a write-off or as partially paid.

---

# Credit notes and refunds

A credit/debit note, or credit/debit memo, is a document sent to a customer to inform them that they
have been *credited/debited* a certain amount.

Several use cases can lead to a credit note, such as:

> - a mistake in the invoice or vendor bill
> - a return of the goods, or a rejection of the services
> - the goods delivered are damaged

Debit notes are less common but are most frequently used to track debts owed by customers or to
vendors because of modifications to confirmed customer invoices or vendor bills.

> **Note:**
>
> Issuing a credit/debit note is the only legal method for canceling, refunding, or modifying a
> validated invoice. Make sure to **register the payment** afterward if money is being refunded to
> the customer and/or validate the
> [return](../../../sales/sales/products_prices/returns.html) if a storable product is being
> returned.

## Issue a customer credit note

In most cases, credit notes are created directly from the corresponding invoices. To do so,
go to Accounting ‣ Customers ‣ Invoices, open the relevant invoice, and click
Credit Note.

In the Credit Note window, fill in the Reason and update the
Journal and Reversal date if needed. There are two options:

- Click Reverse to open a draft credit note prefilled with the exact details from the
  original invoice. Update the Product and Quantity and click
  Confirm. This option allows for a partial refund or modifications to the credit note.
- Click Reverse and Create invoice to create a credit note that is automatically
  validated and reconciled with the related invoice, and to open a new draft invoice prefilled with
  the exact details from the original invoice.

To create a credit note from scratch, go to Accounting ‣ Customers ‣ Credit
Notes, and click New. Filling out a credit note follows the same process as completing
an [invoice](../customer_invoices.html#accounting-invoice-creation).

> **Note:**
>
> A credit note sequence starts with `R` and is followed by the related document number (e.g.,
> RINV/2025/0004 is associated with the invoice INV/2025/0004).

## Issue a customer debit note

In most cases, debit notes are created directly from the corresponding invoices. To do so,
go to Accounting ‣ Customers ‣ Invoices, open the relevant invoice, and click
Debit Note. Then, follow these steps:

1. In the Create Debit Note window, fill in the Reason and update the
   Use Specific Journal and Debit Note Date fields.
2. Enable the Copy Lines option to copy the invoice lines and click Create
   Debit Note.
3. In the debit note, update the Product and Quantity and click
   Confirm.

> **Note:**
>
> To create a debit note from the invoice list view, select the desired invoice(s), click
>  Actions, and select Create Debit Note.

## Record a vendor refund

Vendor refunds or vendor credit notes are recorded the same way as [credit notes]:

To record a vendor refund or a vendor credit note directly from the corresponding vendor bill, go to
Accounting ‣ Vendors ‣ Bills, open the relevant vendor bill, and click
Credit Note.

To record it from scratch, go to Accounting ‣ Vendors ‣ Refunds, and click on
New.

## Record a vendor debit note

Debit notes from vendors are recorded the same way [debit notes are issued to customers].

To record a debit note, go to Accounting ‣ Vendors ‣ Bills open the relevant
vendor bill, and click Debit Note.

> **Note:**
>
> To create a debit note from the vendor bill list view, select the desired vendor bill(s), click
>  Actions and select Create Debit Note.

## Journal entries

Creating a credit/debit note from an invoice/bill generates a **reverse entry** that cancels out the
journal items from the original invoice/bill.

> **Tip:**
>
> The journal entry of an invoice:
>
> ![Invoice journal entry](../../../../_images/journal-entries-invoice.png)
>
> The credit note’s journal entry generated to reverse the original invoice above:
>
> ![Credit note journal entry reverses the invoice journal entry](../../../../_images/journal-entries-credit-note.png)

---

# Cash rounding

**Cash rounding** is required when the lowest physical denomination
of currency, or the smallest coin, is higher than the minimum unit
of account.

For example, some countries require their companies to round up or
down the total amount of an invoice to the nearest five cents, when
the payment is made in cash.

## Configuration

Go to Accounting ‣ Configuration ‣ Settings
and enable *Cash Rounding*, then click on *Save*.

![../../../../_images/cash_rounding01.png](../../../../_images/cash_rounding01.png)

Go to Accounting ‣ Configuration ‣ Cash Roundings,
and click on *Create*.

Define here your *Rounding Precision*, *Rounding Strategy*, and
*Rounding Method*.

Odoo supports two **rounding strategies**:

1. **Add a rounding line**: a *rounding* line is added on the invoice.
   You have to define which account records the cash roundings.
2. **Modify tax amount**: the rounding is applied in the taxes section.

## Apply roundings

When editing a draft invoice, open the *Other Info* tab, go to the
*Accounting Information* section, and select the appropriate *Cash
Rounding Method*.

---

# Deferred revenues

**Deferred revenues**, or **unearned revenues**, are invoices addressed to customers
for goods yet to be delivered or services yet to be rendered.

The company cannot report them on the current **profit and loss statement**, or *income statement*,
since the goods and services will be effectively delivered/rendered in the future.

These future revenues must be deferred on the company’s balance sheet among the current liabilities
until they can be **recognized**, at once or over a defined period, on the profit and loss
statement.

For example, let’s say a business sells a software license of $1200 for 1 year. They immediately
invoice it to the customer but can’t consider it earned yet, as the future months of licensing have
not yet been delivered. Therefore, they post this new revenue in a deferred revenue account and
recognize it on a monthly basis. Each month, for the next 12 months, $100 will be recognized as
revenue.

Odoo Accounting handles deferred revenues by spreading them in multiple entries that are posted
periodically.

> **Note:**
>
> The server checks once a day if an entry must be posted. It might then take up to 24 hours before
> you see a change from Draft to Posted.

## Configuration

Make sure the default settings are correctly configured for your business. To do so, go to
Accounting ‣ Configuration ‣ Settings. The following options are available:

Journal
:   The deferral entries are posted in this journal.

Deferred Revenue
:   Revenues are deferred on this Current Liability account until they are recognized.

Generate Entries
:   By default, Odoo [automatically generates]
    the deferral entries when you post a customer invoice. However, you can also choose to
    [generate them manually] by selecting the
    Manually & Grouped option instead.

Based on
:   There are three ways to calculate the deferred revenue recognition:

    > - Days: The total amount is divided equally by the total number of days in the
    >   period, inclusive of the start and end dates.
    > - Months: Each full month represents an equal proportion of the total amount,
    >   regardless of the actual number of days in that month (standardized basis).
    > - Full Months: Any month started is treated as a complete month. However, the final
    >   month is only considered full if the period extends to the very last day of that month.

    Suppose an invoice of $1200 must be deferred over 12 months.

    - The Days option accounts for different amounts depending on the number of days in
      each month (e.g., ~$102 for January and ~$92 for February).
    - The Months option accounts for $100 each month prorated to the number of days in
      that month (e.g., $50 for the first month if the Start Date is set to the 15th of
      the month).
    - The Full Months option considers each month started to be full (e.g., $100 for the
      first month even if the Start Date is set to the 15th of the month); this means that
      with the Full Months option, a full $100 is recognized in the first partial month,
      eliminating the need for a 13th month to recognize any remainder as would be the case when using
      the Months option.

## Generate deferral entries on validation

> **Note:**
>
> Make sure the Deferred Date field is visible in the Invoice Lines
> tab. In most cases, the start of the deferred period should be in the same month as the
> Invoice Date. Deferred revenue entries are posted from the invoice date and are
> displayed in the report accordingly.

For each line of the invoice that should be deferred, specify the start and end dates of the
deferral period.

If the Generate Entries field in the **Settings** is set to On invoice/bill
validation, Odoo automatically generates the deferral entries when the invoice is validated. Click
the Deferred Entries smart button to see them.

One entry, dated on the same day as the invoice’s accounting date, moves the invoice amounts from
the income account to the deferred account. The other entries are deferral entries which, month
after month, move the invoice amounts from the deferred account to the income account to recognize
the revenue.

> **Tip:**
>
> You can defer a January invoice of $1200 over 12 months by specifying a start date of 01/01/2023
> and an end date of 12/31/2023. At the end of August, $800 is recognized as an income,
> whereas $400 remains on the deferred account.

## Reporting

The deferred revenue report computes an overview of the necessary deferral entries for each account.
To access it, go to Accounting ‣ Reporting ‣ Deferred Revenue.

To view the journal items of each account, click on the account name and then Journal
Items.

![Deferred revenue report](../../../../_images/deferred_revenue_report.png)
> **Note:**
>
> Only invoices whose accounting date is before the end of the period of the report are taken
> into account.

## Generate grouped deferral entries manually

If you have a lot of deferred revenues and wish to reduce the number of journal entries created, you
can generate deferral entries manually. To do so, set the Generate Entries field in the
**Settings** to Manually & Grouped. Odoo then aggregates the deferred amounts in a
single entry.

At the end of each month, go to Accounting ‣ Reporting ‣ Deferred Revenue and
click the Generate Entries button. This generates two deferral entries:

- One dated at the end of the month which aggregates, for each account, all the deferred amounts
  of that month. This means that a part of the deferred revenue is recognized at the end of that
  period.
- The reversal of this created entry, dated on the following day (i.e., the first day of the
  next month) to cancel the previous entry.

> **Tip:**
>
> There are three invoices deferred based on Months:
>
> - Invoice A: $1200 to be deferred from 01/01/2023 to 12/31/2023
> - Invoice B: $600 to be deferred from 01/01/2023 to 12/31/2023
> - Invoice C: $600 to be deferred in a future period (it will appear on the Not
>   Started column)
>
> In January
> :   At the end of January, after clicking the Generate Entries button, there are the
>     following entries:
>
>     - Entry 1 dated on the 31st January:
>
>       - Line 1: Income account -1200 -600 -600 = **-2400** (cancelling the total of all invoices)
>       - Line 2: Income account 100 + 50 = **150** (recognizing 1/12 of invoice A and invoice B)
>       - Line 3: Deferred account 2400 - 150 = **2250** (amount that has yet to be deferred later
>         on)
>     - Entry 2 dated on the 1st February, the reversal of the previous entry:
>
>       - Line 1: Income account **2400**
>       - Line 3: Income account **-150**
>       - Line 2: Deferred account **-2250**
>
> In February
> :   At the end of February, after clicking the Generate Entries button, there are the
>     following entries:
>
>     - Entry 1 dated on the 28th February:
>
>       - Line 1: Income account -1200 -600 -600 = **-2400** (cancelling the total of all invoices)
>       - Line 2: Income account 200 + 100 = **300** (recognizing 2/12 of invoice A and invoice B)
>       - Line 3: Deferred account 2400 - 300 = **2100** (amount that has yet to be deferred later
>         on)
>     - Entry 2 dated on the 1st March, the reversal of the previous entry.
>
> From March to November
> :   The same computation is done for each month until November.
>
> In December
> :   There is no need to generate entries in December.
>
> In total
> :   If we aggregate everything, we would have:
>
>     - Invoice A and invoice B
>     - Two entries (one for the deferral and one for the reversal) for each month from January to
>       November
>     - Invoice C will be deferred later
>
>     Therefore, at the end of December, invoices A and B are fully recognized as income
>     only once in spite of all the created entries thanks to the reversal mechanism.

---

# Electronic invoicing (EDI)

EDI, or electronic data interchange, is the inter-company communication of business documents, such
as purchase orders and invoices, in a standard format. Sending documents according to an EDI
standard ensures that the system receiving the message can interpret the information correctly.
Various EDI file formats are available depending on your company’s country.

The EDI feature allows companies to automate administrative processes. It may also be required by
some governments for fiscal control or to support administrative procedures. Electronic sending of
documents such as customer invoices, credit notes, or vendor bills is one application of EDI.

Odoo supports e-invoicing in many countries. Refer to the [country’s page] for more details.

> **Note:**
>
> [Fiscal localizations documentation](../../fiscal_localizations.html)

## Configuration

By default, the format available in the [send window]
depends on the customer’s country.

To define a specific e-invoicing format for a customer, go to Accounting ‣
Customers ‣ Customers, access the customer form, go to the Accounting tab, and select
the appropriate Format in the Customer invoices section.

## E-invoice generation

From a confirmed invoice, click Send. In the Print & Send window, enable the
relevant e-invoicing format option (e.g., by Peppol), then click Send to
generate and attach the corresponding e-invoicing XML file.

## Peppol

The [Peppol](https://peppol.org/about/) network ensures the exchange of documents and information
between companies and governmental authorities. It is primarily used for electronic invoicing, and
its access points (connectors to the Peppol network) allow companies to send electronic documents
such as customer invoices and credit notes and receive documents like vendor bills and refunds.

In this case, Odoo acts as both an **access point** and an SMP
and enables electronic invoicing transactions without the need to send invoices or bills by email or
post.

> **Note:**
>
> - Peppol registration is **free** and available in Odoo Community.
> - Supported formats for sending documents include **BIS Billing 3.0, XRechnung CIUS, and
>   NLCIUS**.
> - The following **countries** are eligible for **Peppol registration in Odoo**:
>
>   Andorra, Albania, Austria, Bosnia and Herzegovina, Belgium, Bulgaria, Switzerland, Cyprus,
>   Czech Republic, Germany, Denmark, Estonia, Spain, Finland, France, United Kingdom, Greece,
>   Croatia, Hungary, Ireland, Iceland, Italy, Liechtenstein, Lithuania, Luxembourg, Latvia,
>   Monaco, Montenegro, North Macedonia, Malta, Netherlands, Norway, Poland, Portugal, Romania,
>   Serbia, Sweden, Slovenia, Slovakia, San Marino, Turkey, Holy See (Vatican City State).

### Registration

To register on Peppol, go to Accounting ‣ Configuration ‣ Settings and scroll
to the PEPPOL Electronic Invoicing section. Then, follow these steps:

1. Click Activate Electronic Invoicing and fill in the following fields:

   - Using the  (down arrow) icon, make sure the relevant
     country-specific Peppol endpoint identifier is selected in the dropdown list, then enter your
     Peppol endpoint (usually a Company Registry or VAT number).
   - Email
   - Phone, including the country code (e.g., `+32` in Belgium)
2. Click Activate Peppol. The registration is then pending activation and should be
   automatically activated within a day.

   > **Note:**
   >
   > [Peppol endpoint - OpenPeppol eDEC Code Lists](https://docs.peppol.eu/edelivery/codelists/)
   > (open the “Participant Identifier Schemes” as HTML page)
3. Define where documents should be received:

   - Receive in Journal: If necessary, select another purchase journal in the
     Incoming Invoices Journal field.
   - [Receive in Documents](../../../productivity/documents.html): Select a folder in the
     Document Workspace field if multiple purchase journals are used.
4. Click Save.

All invoices and vendor bills can then be sent/received directly using Peppol.

> **Note:**
>
> - To update the Primary contact email, click
>   Advanced Configuration, modify it, and click Save.
> - If you are using an access point from a previous provider, make sure to deregister from it
>   first, then register with your new access point, unless it’s Hermes (BOSA). If using Hermes
>   (BOSA), no action is needed; the migration is handled automatically.

> **Note:**
>
> - To manually trigger the scheduled action used to check the Peppol registration status, enable
>   [developer mode](../../../general/developer_mode.html#developer-mode), open the Settings app, go to Settings
>   ‣ Technical ‣ Scheduled actions, and search for Peppol: update participant
>   status. Open the scheduled action, then click Run Manually.
> - To try Peppol without sending real data, enable demo mode by selecting Odoo Demo
>   ID as the Peppol endpoint identifier. To switch back to production mode, [deregister from
>   the demo mode] and [register] in production.

### Contact verification

Before sending an invoice to a contact using Peppol, make sure the contact is registered as a Peppol
participant. To do so, follow these steps:

1. Go to Accounting ‣ Customers ‣ Customers and access the customer’s form.
2. In the Accounting tab, check the following information in the Customer
   invoices section:

   - eInvoice format: Select the relevant format.
   - Using the  (down arrow) icon, make sure the relevant
     country-specific Peppol endpoint identifier is selected in the dropdown list, then enter the
     customer’s endpoint identifier, usually a Company Registry or VAT number.
3. To verify the contact, enable [developer mode](../../../general/developer_mode.html#developer-mode) and click
   Verify. Its Peppol endpoint verification is marked as Valid
   if the contact is found on the Peppol network.

![verify contact registration](../../../../_images/customer-form.png)
> **Warning:**
>
> While Odoo prefills the endpoint number based on the information available for a contact,
> verifying these details with the contact is recommended.

### Send invoices

All posted invoices that are ready to be sent via Peppol can be viewed in the Invoices
list view in the following ways:

- Use the  (adjust settings) button to add the
  Peppol status column.
- Apply the Peppol Ready filter in the search bar.

To send the invoice to the customer via Peppol, click Send on the confirmed invoice
form. In the Send window, enable the by Peppol option and click
Send.

> **Note:**
>
> - [Multiple invoices](../customer_invoices.html#accounting-invoice-sending-multiple-invoices) can also be sent in
>   batches via Peppol.
> - Set the preferred [Invoice sending](../customer_invoices.html#accounting-invoice-sending) method for a customer to
>   by Peppol in the Customer Invoices section of the customer form’s
>   Accounting tab.

The status is updated to Done once the invoices have been successfully delivered to the
contact’s access point.

### Receive vendor bills

New documents received via Peppol are checked multiple times a day. Depending on the
[registration settings], received documents
are automatically:

- either imported into the purchase journal set in the PEPPOL Electronic Invoicing
  section, and corresponding vendor bills are created as drafts;
- or received via the [Documents app].

> **Note:**
>
> To manually trigger the scheduled action used to retrieve incoming Peppol documents, enable
> [developer mode](../../../general/developer_mode.html#developer-mode), open the Settings app, go to Settings ‣
> Technical ‣ Scheduled actions, and search for Peppol: retrieve new documents. Open
> the scheduled action, then click Run Manually.

#### Vendor bills reception in Documents

> **Note:**
>
> Make sure the Documents - Import from Peppol (`documents_account_peppol`) module is
> [installed](../../../general/apps_modules.html#general-install).

To receive vendor bills via the [Documents app](../../../productivity/documents.html), follow these
steps:

1. In the Documents app, create a specific [folder](../../../productivity/documents.html#documents-folders) or enable [file
   centralization](../../../productivity/documents.html#documents-file-centralization) for Accounting documents.
2. Open the Accounting app, go to Accounting ‣ Configuration ‣ Settings, and
   scroll to the PEPPOL Electronic Invoicing section.
3. In the Document Workspace field, choose the relevant folder.
4. Use the Document Tags field to add tags to incoming Peppol documents for easy
   identification.
5. Click Save.

Then, open the Document app, navigate to the appropriate folder, select the relevant vendor bills,
and click Create Vendor Bill. The corresponding vendor bill is then created.

### Peppol deregistration from Odoo

Only one Peppol receiver registration can be active for each Peppol endpoint identifier at a time.
To stop using Odoo as the Peppol access point, e.g., to switch to another provider or reconfigure
the registration for a new database, you must first deregister from Peppol. To do so, go to
Accounting ‣ Configuration ‣ Settings, scroll down to the PEPPOL
Electronic Invoicing section, and click  Advanced Configuration.
Then click Remove from Peppol and confirm.

Once removed, the Peppol registration is deleted from the database, and documents can no longer be
sent or received via Peppol in Odoo.

## Country-specific e-invoicing details

Refer to the following pages for detailed, country-specific information:

- [Argentina](electronic_invoicing/argentina.html)
- [Austria](electronic_invoicing/austria.html)
- [Belgium](electronic_invoicing/belgium.html)
- [Brazil](electronic_invoicing/brazil.html)
- [Chile](electronic_invoicing/chile.html)
- [Colombia](electronic_invoicing/colombia.html)
- [Croatia](electronic_invoicing/croatia.html)
- [Ecuador](electronic_invoicing/ecuador.html)
- [Estonia](electronic_invoicing/estonia.html)
- [Finland](electronic_invoicing/finland.html)
- [Guatemala](electronic_invoicing/guatemala.html)
- [Hungary](electronic_invoicing/hungary.html)
- [Ireland](electronic_invoicing/ireland.html)
- [Italy](electronic_invoicing/italy.html)
- [Latvia](electronic_invoicing/latvia.html)
- [Lithuania](electronic_invoicing/lithuania.html)
- [Luxembourg](electronic_invoicing/luxembourg.html)
- [Mexico](electronic_invoicing/mexico.html)
- [Netherlands](electronic_invoicing/netherlands.html)
- [Norway](electronic_invoicing/norway.html)
- [Peru](electronic_invoicing/peru.html)
- [Romania](electronic_invoicing/romania.html)
- [Spain](electronic_invoicing/spain.html)
- [Spain - Basque Country](electronic_invoicing/basque_country.html)
- [Uruguay](electronic_invoicing/uruguay.html)

---

# Invoice sequence

When confirming an invoice, Odoo generates a unique invoice reference number. By default, it uses
the sequence format `INV/year/incrementing-number` (e.g., `INV/2025/00001`), which restarts from
`00001` each year.

However, it is possible to [change the sequence format] and
its periodicity, and to [mass-resequence invoices].

> **Note:**
>
> Changes made to reference numbers are logged in the chatter.

## Changing the default sequence

To customize the default sequence, open the last confirmed invoice, click Reset to
Draft, and edit the invoice’s reference number.

![Editing the reference number of an invoice.](../../../../_images/reference-number.png)

Odoo then explains how the detected format will be applied to all future invoices. For example, if
the current invoice’s month is added, the sequence’s periodicity will change to every month instead
of every year.

![Editing the reference number of an invoice.](../../../../_images/sequence-dialog.png)
> **Note:**
>
> The sequence format can be edited directly when creating the first invoice of a given sequence
> period.

## Mass-resequencing invoices

It can be helpful to resequence multiple invoice numbers. For example, when importing invoices from
another invoicing or accounting system and the reference originates from the previous software,
continuity for the current year must be maintained without restarting from the beginning.

> **Note:**
>
> This feature is only available to users with administrator or advisor access.

Follow these steps to resequence invoice numbers:

1. Activate the [developer mode](../../../general/developer_mode.html#developer-mode).
2. From the Accounting Dashboard, open the Customer Invoices journal.
3. Select the invoices that need a new sequence.
4. Click the  Actions menu and select Resequence.
5. In the Ordering field, choose to

   - Keep current order: The order of the numbers remains the same.
   - Reorder by accounting date: The number is reordered by accounting date.
6. Set the First New Sequence.
7. Preview Modifications and click Confirm.

![Resequence options window](../../../../_images/invoice-sequencing.png)
> **Note:**
>
> - To indicate where the sequence change began, the first invoice in the new sequence is
>   highlighted in red in the Customer Invoices list. This visual marker is permanent
>   and purely informational.
> - If there are any irregularities in the new sequence, such as gaps, cancelled, or deleted
>   entries within the open period, a Gaps in the sequence message appears in the
>   Customer Invoices journal on the Accounting dashboard. To view more details about
>   the related invoice(s), click Gaps in the sequence. This visual marker is temporary
>   and will disappear once the entry’s accounting date is on or after the lock date.

> **Note:**
>
> Resequencing is not possible:
>
> - When entries are before a lock date.
> - When the sequence leads to a duplicate.
> - When the range is invalid. For example, if the Invoice Date doesn’t align with the
>   date in the new sequence, such as using a 2024 sequence (INV/2024/XXXXX) for an invoice dated
>   in 2025.
>
> In these cases, a Validation Error message appears.

---

# Snailmail

Sending direct mail can be an effective strategy for grabbing people’s attention, especially when
their email inboxes are overflowing. With Odoo, you have the ability to send invoices and follow-up
reports through postal mail worldwide, all from within your database.

## Configuration

Go to Accounting ‣ Configuration ‣ Settings and scroll down to the
Customer Invoices section to activate Snailmail.

> **Note:**
>
> Set a preferred [invoice sending](../customer_invoices.html#accounting-invoice-sending) method in the
> Accounting tab of a contact to use it by default.

## Sending invoices by post

In the invoice form view, ensure the Customer address is correct and has the country
set. Click Send, select by Post, then Send the letter.

> **Warning:**
>
> Documents sent via snailmail must respect the following rules:
>
> - The paper format must be **A4**.
> - Margins must be at least **5 mm** on all sides. To configure margins, activate the
>   [developer mode](../../../general/developer_mode.html#developer-mode) and go to Settings ‣ Technical ‣
>   Paper Format.
> - A square of **15mm by 15mm** on the bottom left corner must remain clear.
> - Odoo fills these areas with white before sending the letter; any overflowing content will be
>   cut.
> - The **postage area** must remain clear (download the [`snailmail PDF template`](../../../../_downloads/5b14d01e129cc51a32303602599b291f/snailmail-template.pdf) for details).
> - Pingen (Odoo’s snailmail service provider) scans the **address area** to obtain the address.
>   Any text outside the address area is not considered part of the address.

## Pricing

Snailmail is an [In-app purchases (IAP)](../../../essentials/in_app_purchase.html) service that requires prepaid stamps
(credits) to work. Sending one document consumes one stamp.

To buy stamps, go to Accounting ‣ Configuration ‣ Settings, scroll down to the
Snailmail section, and click Buy credits.

> **Note:**
>
> - [Invoice sending](../customer_invoices.html#accounting-invoice-sending)
> - [Odoo’s IAP Privacy Policy](https://iap.odoo.com/privacy#header_4)
> - [Pingen’s layout requirements](https://help.pingen.com/en/templates-and-postal-requirements/letter-standards)

---

# EPC QR codes

European Payments Council quick response codes, or **EPC QR codes**, are two-dimensional barcodes
that customers can scan with their **mobile banking applications** to initiate a **SEPA credit
transfer (SCT)** and pay their invoices instantly.

In addition to bringing ease of use and speed, it greatly reduces typing errors that would
potentially make for payment issues.

> **Note:**
>
> This feature is only available for companies in several European countries such as Austria,
> Belgium, Finland, Germany, and the Netherlands.

> **Note:**
>
> - [Bank and cash accounts](../bank.html)

## Configuration

Go to Accounting ‣ Configuration ‣ Settings and activate the QR
Codes feature in the Customer Payments section.

### Configure your bank account’s journal

Make sure that your Bank Account is correctly configured in Odoo with your IBAN and BIC.

To do so, go to Accounting ‣ Configuration ‣ Journals, open your bank journal,
then fill out the Account Number and Bank under the Bank Account
Number column.

![Bank account number column in the bank journal](../../../../_images/bank-journal.png)

## Issue invoices with EPC QR codes

EPC QR codes are added automatically to your invoices. Customers whose bank supports making payments
via EPC QR codes will be able to scan the code and pay the invoice.

Go to Accounting ‣ Customers ‣ Invoices, and create a new invoice.

Before posting it, open the Other Info tab. Odoo automatically fills out the
Recipient Bank field with your IBAN.

> **Note:**
>
> In the Other Info tab, the account indicated in the Recipient Bank field
> is used to receive your customer’s payment. Odoo automatically populates this field with your
> IBAN by default and uses it to generate the EPC QR code.

When the invoice is printed or previewed, the QR code is included at the bottom.

![QR code on a customer invoice](../../../../_images/invoice-qr-code.png)
> **Note:**
>
> If you want to issue an invoice without an EPC QR code, remove the IBAN indicated in the
> Recipient Bank field, under the Other Info tab of the invoice.

---

# Incoterms

Incoterms are standardized trade terms used in
international transactions to define the rights and responsibilities of buyers and sellers. They
establish the obligations related to the delivery of goods, the transfer of risks, and the
distribution of costs between the parties involved. Incoterms specify important details, such as the
point at which the risk and costs transfer from the seller to the buyer, the responsibility for
transportation, insurance, customs clearance, and other relevant aspects of the transaction.

> **Note:**
>
> By default, all 11 Incoterms are available in Odoo:
>
> - **EXW**: Ex works
> - **FCA**: Free carrier
> - **FAS**: Free alongside ship
> - **FOB**: Free on board
> - **CFR**: Cost and freight
> - **CIF**: Cost, insurance and freight
> - **CPT**: Carriage paid to
> - **CIP**: Carriage and insurance paid to
> - **DPU**: Delivered at place unloaded
> - **DAP**: Delivered at place
> - **DDP**: Delivered duty paid

> **Note:**
>
> - [Intrastat](../reporting/intrastat.html)
> - [Customer invoices](../customer_invoices.html)
> - [Vendor bills](../vendor_bills.html)

## Define an Incoterm

To define an Incoterm manually, create an invoice or bill, click the Other Info tab, and
select the Incoterm.

### Incoterm location

A location relevant to the chosen Incoterm can be added to the invoice or bill under
Other Info in the Incoterm Location field.

> **Tip:**
>
> If the chosen Incoterm code is `CIF` (Cost, Insurance, Freight), the associated location might be
> the destination port where the goods will be delivered.

## Default Incoterm configuration

You can set a default Incoterm rule to **automatically** populate the Incoterm field on all newly
created invoices and bills. Under Accounting/Invoicing ‣ Configuration ‣
Settings, scroll down to the Customer Invoices section, and select an Incoterm in the
Default Incoterm field.

---

# Vendor bills

Vendor bills can be registered either **manually** or **automatically** in Odoo. The
[Aged Payable report] provides an overview of all
outstanding bills to help ensure timely payment of the correct amounts.

> **Note:**
>
> - Tutorial [Registering a vendor bill](https://www.odoo.com/slides/slide/register-a-vendor-bill-6582)
> - [Manage vendor bills](../../inventory_and_mrp/purchase/manage_deals/manage.html)
> - [Credit notes and refunds](customer_invoices/credit_notes.html)

## Bill creation

### Manually

To create a vendor bill manually, go to Accounting ‣ Vendors ‣ Bills and
click New.

> **Note:**
>
> Alternatively, it is possible to create a vendor bill from the Accounting dashboard:
>
> - either click New on the Purchases journal;
> - or click the  (vertical ellipsis) icon of the
>   Purchases journal, then Bill under the New section.

### Automatically

Vendor bills can be automatically created by sending an email to an [email alias](vendor_bills/invoice_digitization.html#accounting-bill-digitization-email-alias) associated with the purchase journal, or by
[uploading a PDF](vendor_bills/invoice_digitization.html#accounting-bill-digitization-manual-upload).

> **Note:**
>
> - Once the bill is uploaded, the PDF document appears on the right side of the screen, making it
>   easy to fill in the bill information.
> - Bills can be [digitized](vendor_bills/invoice_digitization.html) for automatic
>   completion and [matched with purchase orders](vendor_bills/invoice_digitization.html#accounting-bill-digitization-vendor-bills-matching-po) to replace OCR-detected data with the
>   existing purchase order’s details.
> - Services such as digitizing scanned or PDF vendor bills in Odoo require [In-App
>   Purchase (IAP)](../../essentials/in_app_purchase.html) credits.

To automatically post bills from selected vendors, go to Accounting ‣ Vendors ‣
Vendors and select the relevant vendor. In the Accounting tab, under the
General section, update the Auto-post bills field with one of the following
options:

- Always
- Ask after 3 validations without edits
- Never

> **Note:**
>
> [Vendor bills matching with purchase orders](vendor_bills/invoice_digitization.html#accounting-bill-digitization-vendor-bills-matching-po)

## Bill completion

Whether the bill is created manually or automatically, make sure the following fields are
appropriately completed:

- Vendor: Odoo automatically fills in some information based on the information on the
  vendor’s contact record as well as previous purchase orders and bills.
- Bill Reference: Add the sales order reference provided by the vendor. This field is
  used to [match](payments.html#accounting-payments-payments-matching) the products when they are received.
- Auto-Complete: Select a past bill/purchase order to complete the document
  automatically. The Vendor field should be completed before completing this field.
- Bill Date: Select the document’s issuance date.
- Accounting Date: Update the document’s accounting registration date if needed.
- Payment Reference: The Memo field automatically includes the payment
  reference once the payment is registered.
- Recipient Bank: Indicates the account number to which the payment will be made. This
  field is required when paying via batch payment files (such as [NACHA](../fiscal_localizations/united_states.html#l10n-us-ach-electronic-transfers) and [SEPA](payments/pay_sepa.html)).
- Due Date or Payment Terms must be specified for the bill payment.
- Journal: Select which journal should record the bill and in which [currency](get_started/multi_currency.html).

In the Invoice Lines tab:

- To access the product catalog, click [Catalog](../../inventory_and_mrp/inventory/warehouses_storage/inventory_management/product_catalog.html).
- Select the products and quantities, then click Back to Bill to return to the vendor
  bill; the selected catalog items will appear in the vendor bill lines.
- Update the Quantity, Price, and [Taxes](taxes.html) fields if needed.

> **Note:**
>
> If the bill line does not correspond to an existing product in the database, click Add
> a line and enter a description for the bill line without linking it to a product.

> **Note:**
>
> Multiple bills for the same purchase order may be issued if the vendor is on back-order and sends
> invoices as products are shipped or if the vendor sends partial bills or requests a deposit. In
> this case, multiple bills may have the same Bill Reference.

## Bill confirmation

Click Confirm when the document is completed. The status changes to Posted,
and a journal entry is generated based on the vendor bill information. On confirmation, Odoo assigns
each vendor bill a unique number from a defined [sequence](vendor_bills/sequence.html).

> **Note:**
>
> Once confirmed, a vendor bill can no longer be updated. Click Reset to draft if
> changes are required.

## Payment and reconciliation

To register a payment, click on Pay. In the Pay window, select the
Journal, the Payment Method, the Amount, and the
Currency.

When the Amount paid is less than the total remaining amount on the vendor bill, the
payment is [partial](payments.html#accounting-payments-partial-payment), and the Payment
Difference field displays the outstanding balance.

The Memo field is filled automatically if the Payment Reference has been set
correctly on the vendor bill. If the field is empty, select the vendor invoice number as a
reference.

Then click Create payment. An In Payment/Partial banner appears
on the bill until it is [reconciled](bank/reconciliation.html) and its status updates to
Paid.

> **Note:**
>
> - [Payments](payments.html)
> - [Bank reconciliation](bank/reconciliation.html)

## Aged payable report

For an overview of the open vendor bills and their due dates, go to Accounting ‣
Reporting ‣ Aged payable.

Click the  (right arrow) icon next to a vendor to view the details
of all their outstanding bills, including the due dates and amounts.

> **Note:**
>
> Click PDF or XLSX to generate a PDF or XLSX file, respectively.

---

# Document digitization

Document digitization refers to the process of converting paper or digital documents into records
in a database. Using OCR and artificial intelligence
technologies, Odoo reads the content and automatically creates and fills in the record’s details.
This process is mainly used for vendor bills (or refunds).

> **Note:**
>
> Although less common, this digitization process can also be applied to customer invoices and
> credit notes. The [settings] need to be
> adjusted accordingly.

> **Note:**
>
> - [Test Odoo’s invoice digitization](https://www.odoo.com/app/invoice-automation)
> - [Odoo Tutorials: Vendor Bill Digitization](https://www.odoo.com/slides/slide/vendor-bill-digitization-7065)
> - [In-app purchases (IAP)](../../../essentials/in_app_purchase.html)

## Configuration

Go to Accounting ‣ Configuration ‣ Settings and navigate to the
Digitization section. Enable the Document Digitization option and choose
whether Vendor Bills should be processed automatically or on demand.

> **Note:**
>
> If the Single Invoice Line Per Tax option is enabled, only one line is created per
> tax in the new vendor bill, regardless of the number of lines on it.

## Vendor bills upload

Vendor bills are [uploaded manually] or sent to a
[designated email alias] to be digitized. They can
also be [automatically posted] for selected
vendors.

> **Note:**
>
> Once the bill is uploaded, the document preview appears on the right side of the screen.

> **Note:**
>
> [Vendor bills](../vendor_bills.html)

### Manual upload

In the Accounting dashboard, drag and drop vendor bills into the desired purchase journal or click
Upload on the purchase journal.

### Upload via email alias

Vendor bills can be uploaded via an email alias associated with the relevant journal in two ways:

- scanned from a connected scanner configured to send email to an email alias;
- sent directly to an email alias.

Each PDF attached to the email is automatically converted into a new draft vendor bill.

> **Note:**
>
> - Only PDF and XML formats are processed via an email alias associated with a journal.
> - JPEG files must be processed via [email alias in the Documents app](../../../productivity/documents.html#documents-email-aliases).

To add an email alias to a journal, follow these steps:

1. Make sure an [alias domain](../../../websites/website/configuration/domain_names.html) has been
   configured.
2. The default email alias `vendor-bills@` followed by the alias domain is automatically created
   and available in the Advanced Settings tab of the Vendor Bills journal.
3. To change a default email alias, go to Accounting ‣ Configuration ‣
   Journals, select the corresponding journal, and edit the Email Alias in the
   Advanced Settings tab.
4. Configure the connected scanner to send scanned documents to the email alias, if needed.

> **Note:**
>
> Alternatively, an [email alias in the Documents app](../../../productivity/documents.html#documents-email-aliases) can be used
> to automatically send vendor bills to the Finance [folder](../../../productivity/documents.html#documents-folders) (e.g., `inbox-financial@example.odoo.com`).

### Automatic vendor bill posting

> **Note:**
>
> To use the Auto-post bills option, the Digitize automatically setting in
> the [Document Digitization] section must be
> enabled for vendor bills.

To automatically post digitized vendor bills for specific vendors, go to Accounting
‣ Vendors ‣ Vendors and click the desired vendor. In the Accounting tab of the
contact form, select an Auto-post bills option in the Automation section:

- Always
- Ask after 3 validations without edits: When the third uploaded bill is confirmed
  without any edits, an Autopost Bills window appears. The following options can be
  chosen: Activate auto-validation, Ask me later, or Never for
  this vendor.
- Never

> **Note:**
>
> Since automation is triggered after three validated bills without edits, the contact name must
> already exist in the database, and each uploaded vendor bill must include a bill date.

## Digitization and data recognition with AI

Depending on the [settings], documents are either
automatically digitized or require manual processing if digitization is set to on-demand only.

To manually digitize an [uploaded document], click Digitize document.

Once the document has been digitized, a blue banner appears; click
Refresh. Review and correct any information uploaded during digitization: click on the
related field(s) to edit them, or click Reload AI data to refresh the data.

Then, click Confirm to post the document.

> **Note:**
>
> Once a document has been digitized, the Vendor field remains empty if the vendor
> doesn’t exist in the database. To add it, click the  (down arrow)
> in the Vendor field; the vendor name appears highlighted in the document preview on
> the right. Click it to open a new vendor form with the name pre-filled.

> **Note:**
>
> The following vendor bill fields are recognized by OCR:
>
> - Vendor, Bill Reference, Bill Date, Payment
>   Reference (only in the Belgian +++xxx/xxxx/xxxxx+++ format), Recipient Bank,
>   Due Date, and the currency (in a [multi-currency](../get_started/multi_currency.html) environment and if the currency is activated).
> - From the Invoices Lines tab: Product description/label,
>   Quantity, unit Price, Taxes (if the [tax is activated](../taxes.html#taxes-list-activation); this field is not recognized by OCR for the [Indian
>   localization](../../fiscal_localizations/india.html)), Untaxed Amount, and
>   Total.

## Purchase order matching

When a digitized vendor bill is recognized by OCR, Odoo
searches the database for a matching purchase order. If found, the vendor bill can be manually
matched with the existing open purchase order lines.

Once a vendor bill has been [uploaded] and
[digitized], click the Purchase
matching smart button to access the Purchase matching list view, displaying all
purchase order lines linked to the vendor assigned to the vendor bill. Then, select the relevant
purchase order lines and the draft vendor bill (shown in grey), and click Match.

> **Note:**
>
> In the Purchase Matching list view, update the Quantity and
> Price in the purchase order lines, if necessary.

If there is no existing purchase order related to the vendor of the uploaded vendor bill, a new
purchase order can be directly created from the vendor bill lines. To do so, follow these steps:

1. Once the vendor bill is uploaded, make sure the Vendor field is filled in with the
   correct vendor.
2. Click the Purchase matching smart button, select the draft vendor bill in the list
   (shown in grey), and click Add to PO.
3. In the Add to Purchase Order window, start typing in the Purchase Order
   field and select Create and edit.
4. In the Create Purchase Order window, select the vendor assigned to the vendor bill,
   then complete all [required fields](../../../inventory_and_mrp/purchase/manage_deals/rfq.html#purchase-manage-deals-create-new-rfq) and click
   Confirm.
5. In the Purchase Matching list view, select the relevant purchase order lines and the
   draft vendor bill (shown in grey), and click Match.

> **Note:**
>
> If any information required for the purchase order fields is missing, click Save and
> Close in the Create Purchase Order window. Then, open the Purchase app to fill in
> the fields and [confirm the purchase order](../../../inventory_and_mrp/purchase/manage_deals/rfq.html#purchase-manage-deals-confirm-order).

> **Note:**
>
> - Electronic vendor bills with embedded XML ensure more accurate and efficient processing.
> - Alternatively, the [Auto-complete](../vendor_bills.html#accounting-vendor-bills-bill-completion) feature
>   can transfer information from the purchase order to the vendor bill, without requiring OCR.

## Pricing

The document digitization feature is an In-App Purchase (IAP) service requiring prepaid credits.
Digitizing one document uses one credit.

To buy credits, [go to the Settings app](../../../essentials/in_app_purchase.html#iap-buying-credits) or Accounting ‣
Configuration ‣ Settings, navigate to the Digitization section, and click
Buy credits.

> **Note:**
>
> - Odoo Enterprise users with a valid subscription get free credits to test IAP features before
>   purchasing more credits for the database. This includes demo/training databases, educational
>   databases, and one-app-free databases.
> - XML files don’t require OCR credits because they contain structured data that can be processed
>   directly, without OCR.

> **Note:**
>
> - [Odoo In-App Purchase Privacy Policy](https://iap.odoo.com/privacy#header_6)
> - [In-app purchases (IAP)](../../../essentials/in_app_purchase.html)

---

# Non-current assets and fixed assets

**Non-current Assets**, also known as **long-term assets**, are investments that are expected to be
realized after one year. They are capitalized rather than being expensed and appear on the company’s
balance sheet. Depending on their nature, they may undergo **depreciation**.

**Fixed Assets** are a type of Non-current Assets and include the properties bought for their
productive aspects, such as buildings, vehicles, equipment, land, and software.

For example, let’s say we buy a car for $ 27,000. We plan to amortize it over five years, and we
will sell it for $ 7,000 afterward. Using the linear, or straight-line, depreciation method,
$ 4,000 are expensed each year as **depreciation expenses**. After five years, the **Accumulated
Depreciation** amount reported on the balance sheet equals $ 20,000, leaving us with $ 7,000 of
**Not Depreciable Value**, or Salvage value.

Odoo Accounting handles depreciation by creating all depreciation entries automatically in *draft
mode*. They are then posted periodically.

Odoo supports the following **Depreciation Methods**:

- Straight Line
- Declining
- Declining Then Straight Line

> **Note:**
>
> The server checks once a day if an entry must be posted. It might then take up to 24 hours before
> you see a change from *draft* to *posted*.

## Prerequisites

Such transactions must be posted on an **Assets Account** rather than on the default
expense account.

### Configure an Assets Account

To configure your account in the **Chart of Accounts**, go to Accounting ‣
Configuration ‣ Chart of Accounts, click on *Create*, and fill out the form.

![Configuration of an Assets Account in Odoo Accounting](../../../../_images/assets01.png)
> **Note:**
>
> This account’s type must be either *Fixed Assets* or *Non-current Assets*.

### Post an expense to the right account

#### Select the account on a draft bill

On a draft bill, select the right account for all the assets you are buying.

![Selection of an Assets Account on a draft bill in Odoo Accounting](../../../../_images/assets02.png)

#### Choose a different Expense Account for specific products

Start editing the product, go to the *Accounting* tab, select the right **Expense Account**, and
save.

![Change of the Assets Account for a product in Odoo](../../../../_images/assets03.png)
> **Note:**
>
> It is possible to [automate the creation of assets entries] for these
> products.

#### Change the account of a posted journal item

To do so, open your Purchases Journal by going to Accounting ‣ Accounting ‣
Purchases, select the journal item you want to modify, click on the account, and select the right
one.

![Modification of a posted journal item's account in Odoo Accounting](../../../../_images/assets04.png)

## Assets entries

### Create a new entry

An **Asset entry** automatically generates all journal entries in *draft mode*. They are then posted
one by one at the right time.

To create a new entry, go to Accounting ‣ Accounting ‣ Assets, click on
*Create*, and fill out the form.

Click on **select related purchases** to link an existing journal item to this new entry. Some
fields are then automatically filled out, and the journal item is now listed under the **Related
Purchase** tab.

![Assets entry in Odoo Accounting](../../../../_images/assets05.png)

Once done, you can click on *Compute Depreciation* (next to the *Confirm* button) to generate all
the values of the **Depreciation Board**. This board shows you all the entries that Odoo will post
to depreciate your asset, and at which date.

![Depreciation Board in Odoo Accounting](../../../../_images/assets06.png)

#### What does “Prorata Temporis” mean?

The **Prorata Temporis** feature is useful to depreciate your assets the most accurately possible.

With this feature, the first entry on the Depreciation Board is computed based on the time left
between the *Prorata Date* and the *First Depreciation Date* rather than the default amount of time
between depreciations.

For example, the Depreciation Board above has its first depreciation with an amount of $ 241.10
rather than $ 4,000.00. Consequently, the last entry is also lower and has an amount of $ 3758.90.

#### What are the different Depreciation Methods

The **Straight Line Depreciation Method** divides the initial Depreciable Value by the number of
depreciations planned. All depreciation entries have the same amount.

The **Declining Depreciation Method** multiplies the Depreciable Value by the **Declining Factor**
for each entry. Each depreciation entry has a lower amount than the previous entry. The last
depreciation entry doesn’t use the declining factor but instead has an amount corresponding to the
balance of the depreciable value so that it reaches $0 by the end of the specified duration.

The **Declining Then Straight Line Depreciation Method** uses the Declining Method, but with a
minimum Depreciation equal to the Straight Line Method. This method ensures a fast depreciation
at the beginning, followed by a constant one afterward.

### Assets from the Purchases Journal

You can create an asset entry from a specific journal item in your **Purchases Journal**.

To do so, open your Purchases Journal by going to Accounting ‣ Accounting ‣
Purchases, and select the journal item you want to record as an asset. Make sure that it is posted
in the right account (see: [Change the account of a posted journal item]).

Then, click on *Action*, select **Create Asset**, and fill out the form the same way you would do to
[create a new entry].

![Create Asset Entry from a journal item in Odoo Accounting](../../../../_images/assets07.png)

## Modification of an Asset

You can modify the values of an asset to increase or decrease its value.

To do so, open the asset you want to modify, and click on *Modify Depreciation*. Then, fill out the
form with the new depreciation values and click on *Modify*.

A **decrease in value** posts a new Journal Entry for the **Value Decrease** and modifies all the
future *unposted* Journal Entries listed in the Depreciation Board.

An **increase in value** requires you to fill out additional fields related to the account movements
and creates a new Asset entry with the **Value Increase**. The Gross Increase Asset Entry can be
accessed with a Smart Button.

![Gross Increase smart button in Odoo Accounting](../../../../_images/assets08.png)

## Disposal of Fixed Assets

To **sell** an asset or **dispose** of it implies that it must be removed from the Balance Sheet.

To do so, open the asset you want to dispose of, click on *Sell or Dispose*, and fill out the form.

![Disposal of Assets in Odoo Accounting](../../../../_images/assets09.png)

Odoo Accounting then generates all the journal entries necessary to dispose of the asset, including
the gain or loss on sale, which is based on the difference between the asset’s book value at the
time of the sale and the amount it is sold for.

> **Note:**
>
> To record the sale of an asset, you must first post the related Customer Invoice so you can link
> the sale of the asset with it.

## Assets Models

You can create **Assets Models** to create your Asset entries faster. It is particularly useful if
you recurrently buy the same kind of assets.

To create a model, go to Accounting ‣ Configuration ‣ Assets Models, click on
*Create*, and fill out the form the same way you would do to create a new entry.

> **Note:**
>
> You can also convert a *confirmed Asset entry* into a model by opening it from
> Accounting ‣ Accounting ‣ Assets and then, by clicking on the button *Save
> Model*.

### Apply an Asset Model to a new entry

When you create a new Asset entry, fill out the **Fixed Asset Account** with the right asset
account.

New buttons with all the models linked to that account appear at the top of the form. Clicking on a
model button fills out the form according to that model.

![Assets model button in Odoo Accounting](../../../../_images/assets10.png)

## Automate the Assets

When you create or edit an account of which the type is either *Non-current Assets* or *Fixed
Assets*, you can configure it to create assets for the expenses that are credited on it
automatically.

You have three choices for the **Automate Assets** field:

1. **No:** this is the default value. Nothing happens.
2. **Create in draft:** whenever a transaction is posted on the account, a draft *Assets entry* is
   created, but not validated. You must first fill out the form in Accounting ‣
   Accounting ‣ Assets.
3. **Create and validate:** you must also select an Asset Model (see: [Assets Models]). Whenever a
   transaction is posted on the account, an *Assets entry* is created and immediately validated.

![Automate Assets on an account in Odoo Accounting](../../../../_images/assets11.png)
> **Note:**
>
> You can, for example, select this account as the default **Expense Account** of a product to
> fully automate its purchase. (see: [Choose a different Expense Account for specific products]).

> **Note:**
>
> - [Chart of accounts](../get_started/chart_of_accounts.html)

---

# Deferred expenses

**Deferred expenses** and **prepayments** (also known as **prepaid expenses**) are both costs that
have already occurred for products or services yet to be received.

Such costs are **assets** for the company that pays them since it already paid for products and
services but has either not yet received them or not yet used them. The company cannot report them
on the current **profit and loss statement**, or *income statement*, since the payments will be
effectively expensed in the future.

These future expenses must be deferred on the company’s balance sheet until the moment in time they
can be **recognized**, at once or over a defined period, on the profit and loss statement.

For example, let’s say we pay $1200 at once for one year of insurance. We already pay the cost now
but haven’t used the service yet. Therefore, we post this new expense in a *prepayment account* and
decide to recognize it on a monthly basis. Each month, for the next 12 months, $100 will be
recognized as an expense.

Odoo Accounting handles deferred expenses by spreading them across multiple entries that are
posted periodically.

> **Note:**
>
> The server checks once a day if an entry must be posted. It might then take up to 24 hours before
> you see a change from Draft to Posted.

## Configuration

Make sure the default settings are correctly configured for your business. To do so, go to
Accounting ‣ Configuration ‣ Settings. The following options are available:

Journal
:   The deferral entries are posted in this journal.

Deferred Expense
:   Expenses are deferred on this Current Asset account until they are recognized.

Generate Entries
:   By default, Odoo [automatically generates]
    the deferral entries when you post a vendor bill. However, you can also choose to
    [generate them manually] by selecting the
    Manually & Grouped option instead.

Based on
:   There are three ways to calculate the deferred expenses recognition:

    > - Days: The total amount is divided equally by the total number of days in the
    >   period, inclusive of the start and end dates.
    > - Months: Each full month represents an equal proportion of the total amount,
    >   regardless of the actual number of days in that month (standardized basis).
    > - Full Months: Any month started is treated as a complete month. However, the final
    >   month is only considered full if the period extends to the very last day of that month.

    Suppose a bill of $1200 must be deferred over 12 months.

    - The Days option accounts for different amounts depending on the number of days in
      each month (e.g., ~$102 for January and ~$92 for February).
    - The Months option accounts for $100 each month prorated to the number of days in
      that month (e.g., $50 for the first month if the Start Date is set to the 15th of
      the month).
    - The Full Months option considers each month started to be full (e.g., $100 for the
      first month even if the Start Date is set to the 15th of the month); this means that
      with the Full Months option, a full $100 is recognized in the first partial month,
      eliminating the need for a 13th month to recognize any remainder as would be the case when using
      the Months option.

## Generate deferral entries on validation

> **Note:**
>
> Make sure the Deferred Date field is visible in the Invoice Lines
> tab. In most cases, the start of the deferred period should be in the same month as the
> Accounting Date. Deferred expense entries are posted from the accounting
> date and are displayed in the report accordingly.

For each line of the bill that should be deferred, specify the start and end dates of the deferral
period.

If the Generate Entries field is set to On invoice/bill validation, Odoo
automatically generates the deferral entries when the bill is validated. Click on the
Deferred Entries smart button to see them.

One entry, dated on the same day as the bill’s accounting date, moves the bill amounts from the
expense account to the deferred account. The other entries are deferral entries which will, month
after month, move the bill amounts from the deferred account to the expense account to recognize
the expense.

> **Tip:**
>
> You can defer a January bill of $1200 over 12 months by specifying a start date of 01/01/2023
> and an end date of 12/31/2023. At the end of August, $800 is recognized as an expense,
> whereas $400 remains on the deferred account.

## Reporting

The deferred expense report computes an overview of the necessary deferral entries for each account.
To access it, go to Accounting ‣ Reporting ‣ Deferred Expense.

To view the journal items of each account, click on the account name and then Journal
Items.

![Deferred expense report](../../../../_images/deferred_expense_report.png)
> **Note:**
>
> Only bills whose accounting date is before the end of the period of the report
> are taken into account.

## Generate grouped deferral entries manually

If you have a lot of deferred revenues and wish to reduce the number of journal entries created, you
can generate deferral entries manually. To do so, set the Generate Entries field in the
**Settings** to Manually & Grouped. Odoo then aggregates the deferred amounts in a
single entry.

At the end of each month, go to the Deferred Expenses report and click the
Generate Entries button. This generates two deferral entries:

- One dated at the end of the month which aggregates, for each account, all the deferred amounts
  of that month. This means that at the end of that period, a part of the deferred expense is
  recognized.
- The reversal of this created entry, dated on the following day (i.e., the first day of the
  next month) to cancel the previous entry.

> **Tip:**
>
> There are three bills deferred based on Months:
>
> - Bill A: $1200 to be deferred from 01/01/2023 to 12/31/2023
> - Bill B: $600 to be deferred from 01/01/2023 to 12/31/2023
> - Bill C: $600 to be deferred in a future period (it will appear on the Not Started
>   column)
>
> In January
> :   At the end of January, after clicking the Generate Entries button, there are the
>     following entries:
>
>     - Entry 1 dated on the 31st January:
>
>       - Line 1: Expense account -1200 -600 -600 = **-2400** (cancelling the total of all bills)
>       - Line 2: Expense account 100 + 50 = **150** (recognizing 1/12 of bill A and bill B)
>       - Line 3: Deferred account 2400 - 150 = **2250** (amount that has yet to be deferred later
>         on)
>     - Entry 2 dated on the 1st February, the reversal of the previous entry:
>
>       - Line 1: Expense account **2400**
>       - Line 3: Expense account **-150**
>       - Line 2: Deferred account **-2250**
>
> In February
> :   At the end of February, after clicking the Generate Entries button, there are the
>     following entries:
>
>     - Entry 1 dated on the 28th February:
>
>       - Line 1: Expense account -1200 -600 -600 = **-2400** (cancelling the total of all bills)
>       - Line 2: Expense account 200 + 100 = **300** (recognizing 2/12 of bill A and bill B)
>       - Line 3: Deferred account 2400 - 300 = **2100** (amount that has yet to be deferred later
>         on)
>     - Entry 2 dated on the 1st March, the reversal of the previous entry.
>
> From March to November
> :   The same computation is done for each month until November.
>
> In December
> :   There is no need to generate entries in December.
>
> In total
> :   If we aggregate everything, we would have:
>
>     - Bill A and Bill B
>     - Two entries (one for the deferral and one for the reversal) for each month from January to
>       November
>     - Bill C will be deferred later
>
>     Therefore, at the end of December, bills A and B are fully recognized as expense only once in
>     spite of all the created entries thanks to the reversal mechanism.

---

# Vendor bill sequence

When confirming a vendor bill, Odoo generates a unique vendor bill reference number. By default, it
uses the sequence format `BILL/year/month/incrementing-number` (e.g., `BILL/2025/01/00001`), which
restarts from `00001` each year.

However, it is possible to [change the sequence format]
and its periodicity, and to [mass-resequence vendor bills].

> **Note:**
>
> Changes made to reference numbers are logged in the chatter.

## Changing the default sequence

To customize the default sequence, open the last confirmed vendor bill, click Reset to
Draft, and edit the vendor bill’s reference number.

![Editing the reference number of a vendor bill.](../../../../_images/sequence-reference-number.png)

Odoo then explains how the detected format will be applied to all future vendor bills. For example,
if the current vendor bill’s month is withdrawn, the sequence’s periodicity will change to every
year instead of every month.

![Editing the reference number of a vendor bill.](../../../../_images/sequence-dialog1.png)
> **Note:**
>
> The sequence format can be edited directly when creating the first vendor bill of a given
> sequence period.

## Mass-resequencing vendor bills

It can be helpful to resequence multiple vendor bill numbers. For example, when importing vendor
bills from another accounting system and the reference originates from the previous software,
continuity for the current year must be maintained without restarting from the beginning.

> **Note:**
>
> This feature is only available to users with administrator or advisor access.

Follow these steps to resequence vendor bill numbers:

1. Activate the [developer mode](../../../general/developer_mode.html#developer-mode).
2. In the vendor bills list view, select the vendor bills that need a new sequence.
3. Click the  Actions menu and select Resequence.
4. In the Ordering field, choose to

   - Keep current order: The order of the numbers remains the same.
   - Reorder by accounting date: The number is reordered by accounting date.
5. Set the First New Sequence.
6. Preview Modifications and click Confirm.

![Resequence options window](../../../../_images/sequence-bill-sequencing.png)
> **Note:**
>
> - To indicate where the sequence change began, the first vendor bill in the new sequence is
>   highlighted in red in the Vendor Bills list. This visual marker is permanent
>   and purely informational.
> - If there are any irregularities in the new sequence, such as gaps, cancelled, or deleted
>   entries within the open period, a Gaps in the sequence message appears in the
>   Vendor Bills journal on the Accounting dashboard. To view more details about the
>   related vendor bill(s), click Gaps in the sequence. This visual marker is temporary
>   and will disappear once the entry’s accounting date is on or after the lock date.

> **Note:**
>
> Resequencing is not possible:
>
> - When entries are before a lock date.
> - When the sequence leads to a duplicate.
> - When the range is invalid. For example, if the Bill Date doesn’t align with the
>   date in the new sequence, such as using a 2024 sequence (BILL/2024/MM/XXXX) for an vendor bill
>   dated in 2025.
>
> In these cases, a Validation Error message appears.

---

# Payments

In Odoo, payments can either be automatically linked to an invoice or bill or be stand-alone records
for use at a later date:

- If a payment is **linked to an invoice or bill**, it reduces/settles the amount due on the
  invoice. Multiple payments on the same invoice are possible.
- If a payment is **not linked to an invoice or bill**, the customer has an outstanding credit with
  the company, or the company has an outstanding debit with a vendor. Those outstanding amounts
  reduce/settle unpaid invoices/bills.

> **Note:**
>
> - [Internal transfers](bank/internal_transfers.html)
> - [Bank reconciliation](bank/reconciliation.html)
> - [Odoo Tutorials: Bank Configuration](https://www.odoo.com/slides/slide/bank-configuration-6832)

## Payment methods

Several payment methods are available in Odoo to allow different configurations for different types
of payments. Examples of payment methods include manual payments (such as cash), [checks](payments/pay_checks.html), and batch payment files (such as [NACHA](../fiscal_localizations/united_states.html#l10n-us-ach-electronic-transfers) and [SEPA](payments/pay_sepa.html)). Payment methods can be
configured in the Incoming Payments and Outgoing Payments tabs of a bank or
cash journal.

> **Note:**
>
> [Payment methods](../../sales/point_of_sale/payment_methods.html) for Point of Sale

### Preferred payment method

A contact’s preferred payment method can be set so that when a payment is created for that contact,
the payment method is automatically selected by default. Invoices and bills can be filtered by
Payment Method to simplify [group] payments.

To set a preferred Payment Method for a customer or a vendor, go to
Accounting ‣ Customers ‣ Customers or Accounting ‣ Vendors
‣ Vendors and select the customer or vendor. In the Sales & Purchase tab of the
contact form, select the preferred Payment Method in the Sales section for
invoice payments or for vendor bill payments in the Purchase section.

> **Note:**
>
> Access a full list of all contacts from the Customers or Vendors list
> view by removing the Customers or Vendors filter. Alternatively, access
> the full contact list through the Contacts app.

### Checks

[Vendor bills can be paid by check](payments/pay_checks.html) using a dedicated outgoing payment
method, which allows check numbers to be tracked and checks to be printed directly from Odoo.

For incoming customer check payments, you can use the default Manual Payment payment
method, or you can create a payment method specifically for checks to help identify such payments
quickly. To create a *Check* payment method, follow these steps:

1. Go to Accounting ‣ Configuration ‣ Journals and select the Bank
   journal.
2. In the Incoming Payments tab, click Add a line.
3. As Payment Method, select Manual, then enter `Check` as the
   Name.

When registering a customer payment [on an invoice] or
[not related to an invoice], use the new Check
payment method.

> **Note:**
>
> Registering a customer payment by check in Odoo does not move funds. Checks must be deposited in
> order to make the payment. Once deposited to your bank, the check should appear as a [bank
> transaction](bank/transactions.html), at which point it can be [reconciled](bank/reconciliation.html) with the registered payment.

> **Note:**
>
> - For best practice, enter the check number as the Memo when registering a customer
>   payment by check.
> - [Batch payments](payments/batch.html) can simplify reconciling deposits containing multiple
>   checks.

## Registering payment from an invoice or bill

To register a payment for an invoice or a bill, follow these steps:

1. Click Pay on a customer invoice or vendor bill. In the Pay window, select
   the Journal and the Payment Date.
2. If previously set, the contact’s preferred Payment Method is automatically selected
   by default but can be updated if necessary.
3. If using [payment terms](customer_invoices/payment_terms.html), the Amount is
   automatically set based on the installment amounts defined by the payment term. To pay the full
   amount instead, click full amount.
4. If necessary, edit the Memo.
5. Click Create Payment.

After the payment is registered, the customer invoice or vendor bill is marked as
In payment.

Without outstanding accountsUsing outstanding accounts

If no [outstanding accounts](get_started/journals.html#accounting-journals-outstanding-accounts) are configured,
no journal entry is created. To display more information about the payment, click the
Payments smart button.

When the invoice or vendor bill is [reconciled](bank/reconciliation.html) with a bank
transaction, its status is updated to Paid.

> **Note:**
>
> - If a bank transaction is reconciled in a different currency, a journal entry is
>   automatically created to post the currency exchange gains/loss amount.
> - When a bank transaction is reconciled with an invoice with cash-basis, a journal entry is
>   automatically created to post the cash-basis tax amount.

By default, payments in Odoo do not create journal entries, but they can easily be configured
to create journal entries using [outstanding accounts](get_started/journals.html#accounting-journals-outstanding-accounts).

Registering a payment on a customer invoice or vendor bill generates a new journal entry and
reduces the Amount Due based on the payment amount. The counterpart is
reflected in an [outstanding](get_started/journals.html#accounting-journals-outstanding-accounts) **receipts** or
**payments** account. At this point, the customer invoice or vendor bill is marked as
In payment. Then, when the payment is [reconciled](bank/reconciliation.html) with
a bank transaction, the invoice or vendor bill status changes to Paid.

The  information icon next to the payment line displays more
information about the payment. To access additional information, such as the related journal,
click View.

![See detailed information of a payment.](../../../_images/information-icon.png)
> **Note:**
>
> - Unreconciling a payment unlinks it from the invoice or bill but does not delete the
>   payment.
> - If a payment is (un)reconciled in a different currency, a journal entry is automatically
>   created to post the currency exchange gains/losses (reversal) amount.
> - If a payment is (un)reconciled on an invoice with cash-basis taxes, a journal entry is
>   automatically created to post the cash-basis tax (reversal) amount.

> **Note:**
>
> If the main bank account is set as the outstanding account on the bank journal’s payment
> method, registering the full payment on an invoice or bill moves the invoice/bill directly
> to the Paid status without requiring bank reconciliation.

## Registering payments not tied to an invoice or bill

When a new payment is registered via Customers / Vendors ‣ Payments, it is not
directly linked to an invoice or bill.

Without outstanding accountsUsing outstanding accounts

Payments that are not linked to an invoice or bill should not be registered without using
[outstanding accounts](get_started/journals.html#accounting-journals-outstanding-accounts), as there is no way to
associate the payment with the invoice or bill since no journal entry is created for the
payment. The amount paid or received is not reflected in the accounting and the
Amount Due is not updated based on the payment amount.

Instead, the payment’s journal entry matches the outstanding account with the
account receivable or the account payable until the payment is manually matched with its
related invoice or bill. Then, [reconciling](bank/reconciliation.html) the payment with the
bank transaction completes the payment workflow.

### Payments matching

> **Note:**
>
> During the [bank reconciliation](bank/reconciliation.html) process, a remaining balance is
> identified if the total debits and credits do not match when records are compared with bank
> transactions. This balance must either be reconciled later or written off immediately.

#### For a single invoice or bill

Without outstanding accountsUsing outstanding accounts

By default, payments in Odoo do not create journal entries. As a result, there is no payment
to match.

A blue banner appears when validating a new invoice/bill and an **outstanding payment** exists
for this specific customer or vendor. To match it with the invoice or bill, click
Add under Outstanding Credits or Outstanding Debits.

![Shows the Add option to reconcile an invoice or a bill with a payment.](../../../_images/add-option.png)

The invoice or bill is then marked as In payment until the payment is
[reconciled](bank/reconciliation.html) with its corresponding [bank transaction(s)](bank/transactions.html).

#### For multiple invoices or bills

Without outstanding accountsUsing outstanding accounts

By default, payments in Odoo do not create journal entries. As a result, there is no payment
to match, but this feature can still be used to match miscellaneous journal items.

The Payments matching or Auto-reconcile tool allows reconciling
journal items with each other (i.e., payments with customer invoices or vendor bills) either
individually or in batches. Access the Accounting Dashboard, click the
 (ellipsis) button from the Customer
Invoices or Vendor Bills journals, and select Payments Matching.
Alternatively, go to Accounting ‣ Accounting ‣ Reconcile.

To manually Reconcile journal items, select the individual items from the list
view and click Reconcile.

##### Auto-Reconcile Feature

Without outstanding accountsUsing outstanding accounts

To use the Auto-Reconcile feature, follow these steps:

1. In the Journal Items to reconcile list view, click Auto-Reconcile
   next to the receivable or payable account (or a specific contact’s group of journal items
   in that account).
2. In the Reconcile automatically window, click Reconcile.

To use the Auto-Reconcile feature, follow these steps:

1. In the Journal Items to reconcile list view, click Auto-Reconcile
   next to the receivable or payable account (or a specific contact’s group of journal items
   in that account).
2. In the Reconcile Automatically window, set the
   Reconcile field depending on how you want to match journal items:

   - Perfect Match: Each debit journal item will be matched with
     the corresponding credit journal item of the same value.
   - Clear Accounts: All reconciled journal items will have the same
     matching number, as they are selected from the same account.
3. Click Reconcile.

Invoices and bills are automatically matched to their corresponding payments and marked as
In payment until they are [reconciled](bank/reconciliation.html) with their
corresponding [bank transactions](bank/transactions.html).

## Registering payments on multiple invoices/credit notes or bills/refunds (group payments)

To register payments on multiple invoices/credit notes or bills/refunds, follow these steps:

1. Go to Accounting ‣ Customers ‣ Invoices/Credit Notes or
   Accounting ‣ Vendors ‣ Bills/Refunds.
2. In the list view, click into the search bar, group by Payment Method, select the
   relevant invoices/credit notes or bills/refunds and click Pay.
3. In the Pay window, select the Journal and the Payment Date.
4. If previously set, the contact’s preferred Payment Method is automatically selected
   by default but can be updated if necessary.
5. If using [payment terms](customer_invoices/payment_terms.html), the Amount is
   automatically set based on the installment amounts defined by the payment term. To pay the full
   amount instead, click full amount.
6. To combine all payments from the same contact into a single payment, enable the Group
   Payments option, or leave it unchecked to create separate payments.
7. Click Create payment.

Without outstanding accountsUsing outstanding accounts

The invoices or bills are then marked as In payment until they are
[reconciled](bank/reconciliation.html) with the bank transactions.

The invoices or bills are then marked as In payment until the bank transactions
are [reconciled](bank/reconciliation.html) with the payments.

## Registering a single payment for multiple customers or vendors (batch payments)

Batch payments allow grouping payments from multiple customers to ease [reconciliation](bank/reconciliation.html). They are also useful when depositing [checks] or cash payments to the bank or for generating bank payment files such
as [SEPA](payments/pay_sepa.html) or [NACHA](../fiscal_localizations/united_states.html#l10n-us-nacha).

> **Note:**
>
> [Batch payments](payments/batch.html)

### Payments matching

The Payments matching tool opens all unreconciled journal items and allows them to be
processed individually, matching all payments and journal items. Go to the
Accounting Dashboard, go to Accounting ‣ Accounting ‣ Reconcile or
click the  (ellipsis) button from the Customer
Invoices or Vendor Bills journals, and select Payments Matching.

![Payments matching menu in the drop-down menu.](../../../_images/payments-journal.png)
> **Note:**
>
> During the [reconciliation](bank/reconciliation.html), if the sum of the debits and credits does
> not match, there is a remaining balance. This either needs to be reconciled at a later date or
> written off directly.

## Registering a partial payment

To register a partial payment, click on Pay from the related invoice or bill.

Without outstanding accountsUsing outstanding accounts

In the case of a partial payment (when the Amount paid is less than the total
remaining amount on the invoice or the bill), fill in the Amount in the
Pay window.

In the case of a partial payment (when the Amount paid is less than the total
remaining amount on the invoice or the bill), the Payment Difference field
displays the outstanding balance. There are two options:

- Keep open: Keep the invoice or the bill open and mark it with a
  Partial banner;
- Mark as fully paid: Select an account in the Post Difference In
  field and change the Label if needed. A journal entry will be created to balance
  the accounts payable or receivable with the selected account.

![register a partial payment](../../../_images/partial-payment.png)

## Reconciling payments with bank transactions

Without outstanding accountsUsing outstanding accounts

Once a payment has been registered, the status of the invoice or bill is In
payment. The next step is [reconciling](bank/reconciliation.html) the related [bank
transaction](bank/transactions.html) line with the invoice or bill to finalize the payment
workflow and mark the invoice or bill as Paid.

Once a payment has been registered, the status of the invoice or bill is In
payment. The next step is [reconciling](bank/reconciliation.html) the payment with the
related [bank transaction](bank/transactions.html) line to finalize the payment workflow and
mark the invoice or bill as Paid.

---

# Online payments

To make it more convenient for your customers to pay the invoices you issue, you can activate the
**Invoice Online Payment** feature, which adds a *Pay Now* button on their **Customer Portal**. This
allows your customers to see their invoices online and pay directly with their favorite payment
method, making the payment process much easier.

![Payment provider choice after having clicked on "Pay Now"](../../../../_images/online-payment-providers.png)

## Configuration

Make sure your [payment providers are correctly configured](../../payment_providers.html).

> **Note:**
>
> By default, [Wire Transfer](../../payment_providers/bank_payments.html#payment-providers-bank-payments-wire-transfer) is the
> only payment provider activated, but you still have to fill out the payment details.

To activate the Invoice Online Payment, go to Accounting ‣ Configuration ‣
Settings ‣ Customer Payments, enable **Invoice Online Payment**, and click on *Save*.

## Customer Portal

After issuing the invoice, click on Send and send the invoice by email to the customer.
They will receive an email with a link that redirects them to the invoice on their **Customer
Portal**.

![Email with a link to view the invoice online on the Customer Portal.](../../../../_images/view-invoice.png)

They can choose which Payment Provider to use by clicking on *Pay Now*.

!["Pay now" button on an invoice in the Customer Portal.](../../../../_images/pay-now.png)
> **Note:**
>
> - [Online payments](../../payment_providers.html)

---

# Batch payments

Batch payments allow grouping payments from multiple customers or vendors into a single batch and
generating a detailed deposit slip or payment file with a batch reference. This reference can be
used during [reconciliation](../bank/reconciliation.html) to match bank transactions with the
corresponding payments. This feature is particularly useful for submitting [SEPA Direct Debit
payments](batch_sdd.html), depositing cash payments or [checks](../payments.html#accounting-payments-checks), or
generating outgoing payment files, such as [SEPA](pay_sepa.html) or [NACHA](../../fiscal_localizations/united_states.html#l10n-us-nacha).

## Configuration

To enable batch payments, go to Accounting ‣ Configuration ‣ Settings, scroll
down to the Customer Payments section, and enable Batch Payments.

## Batch creation

To create a batch payment, follow these steps:

1. Make sure all payments to be included in the batch have been [registered](../payments.html#accounting-payments-from-invoice-bill).
2. Go to Accounting ‣ Customers ‣ Payments.
3. Select the payments to include in the batch.

   > **Note:**
   >
   > All payments in the batch must use the same payment method. If needed, payments can be grouped
   > using the Payment Method Line.
4. Click Create batch or click  Actions and select
   Create batch payment.
5. In the batch payment form, review the selected payments. If any individual payments were missed,
   click Add a line and select the missing payments to be included in the batch.
6. Once all relevant payments are included, click Validate to finalize the batch.

> **Note:**
>
> Once validated, no additional payments can be added to a batch.

> **Note:**
>
> - Click Print to download a list of the included payments.
> - To view existing batch payments, go to Accounting ‣ Customers ‣ Batch
>   Payments.

### Bank reconciliation

Once the bank transactions [have been created](../bank/transactions.html) in your database, you can
[reconcile](../bank/reconciliation.html#accounting-reconciliation-reconcile) them with the batch payment.

> **Note:**
>
> - [Payments](../payments.html)
> - [SEPA Direct Debit (SDD) customer payments](batch_sdd.html)

---

# SEPA Direct Debit (SDD) customer payments

SEPA (Single Euro Payments Area) is a payment-integration initiative of the European Union that
facilitates standardized and simplified electronic payments in euros across participating countries.
With **SEPA Direct Debit** (SDD), customers sign a mandate that authorizes you to collect future
payments from their bank accounts. This is particularly useful for recurring payments based on a
[subscription](../../../sales/subscriptions.html).

You can record customer SDD mandates in Odoo and generate XML files listing payments to be
collected with the mandates. [Uploading these files to your bank]
instructs them to collect these payments from your customers.

> **Note:**
>
> - SDD is supported by all SEPA countries, which includes the 27 member states of the European
>   Union as well as additional countries.
> - [List of all SEPA countries](https://www.europeanpaymentscouncil.eu/document-library/other/epc-list-sepa-scheme-countries).

## Configuration

### Creditor identifier

To enable SDD for customer payments, go to Accounting ‣ Configuration ‣
Settings, scroll to the Customer Payments section, enable SEPA Direct Debit
(SDD), and click Save. Then, scroll to the Customer Payments section again,
set the company’s Creditor Identifier, and click Save.

> **Note:**
>
> The creditor identifier is provided by your bank or the authority responsible for delivering
> them in your country. For testing purposes, you can use the test creditor identifier
> `DE98ZZZ09999999999`.

### PAIN file version

By default, the [SEPA-compliant XML files] generated by Odoo
use the SDD **PAIN.008.001.02** format. If your bank requires the updated 2023
version, go to Accounting ‣ Configuration ‣ Journals and select the
Bank journal. Then, in the Incoming Payments tab, set the SEPA
Pain version field to Updated 2023 (Pain 008.001.08).

> **Note:**
>
> [SEPA Direct Debit Core Customer-to-PSP Implementation Guidelines](https://www.europeanpaymentscouncil.eu/document-library/implementation-guidelines/sepa-direct-debit-core-customer-psp-implementation-0).

## SEPA Direct Debit Mandates

An SDD mandate is a legal document authorizing a company to debit funds from a customer’s bank
account. It includes key information, such as the customer’s name and IBAN, the mandate’s start
and end date, and the mandate’s unique identifier. The mandate form must be filled in and signed by
the customer.

### Creating mandates

To create an SDD mandate:

1. Go to Accounting ‣ Customers ‣ Direct Debit Mandates.
2. Click New and fill out the fields.
3. Click Send & Print, optionally edit the email, then click Send & Print
   to email the mandate form to the customer for signature.
4. Click Validate to activate the mandate.

> **Warning:**
>
> A valid IBAN must be defined in the Account Number field of the [bank journal](../bank.html) used to receive SDD payments for the mandate.

> **Note:**
>
> - To print the mandate form after the mandate has been validated, click the
>   (gear) icon, then select Mandate form.
> - The SDD Scheme depends on the type of customer: Select CORE for B2C
>   customers and B2B for B2B customers.
> - SDD mandates are created automatically for [online payments made with SDD](../../payment_providers/bank_payments.html#payment-providers-bank-payments-sdd).

Once an SDD mandate is active, subsequent SDD payments can be generated via Odoo and
[uploaded to your online banking interface]. Customers with an
active SDD mandate can also use this payment method for [online purchases](../../payment_providers/bank_payments.html#payment-providers-bank-payments-sdd).

### Closing or revoking a mandate

SDD mandates are closed automatically after their End Date. If this field is
left empty, the mandate remains active until it is closed or revoked. To close or revoke a mandate,
go to Accounting ‣ Customers ‣ Direct Debit Mandates, select the relevant
mandate, and click Close or Revoke.

**Closing** a mandate updates the mandate’s end date to the current day. Invoices issued after the
present day will not be processed with an SDD payment. **Revoking** a mandate disables the
mandate immediately. No SDD payment can be registered anymore, regardless of the invoice’s
date. However, payments that have already been registered are still included in the next [SDD
XML file].

> **Warning:**
>
> - Mandates are automatically closed 36 months after the date of the last collection.
> - Closed or revoked mandates cannot be reactivated.

## Processing SDD payments

All registered SDD payments can be processed at once by uploading an XML file containing a batch
of all posted SDD payments to your online banking interface. To do so, follow these steps:

1. [Create a batch payment](batch.html#accounting-batch-creation) and include the SDD payments to
   collect.

   > **Note:**
   >
   > You can filter payments by SDD scheme using the SDD CORE and SDD B2B
   > filters.
2. Validate the batch payment. The XML file is generated automatically and available
   for download in the chatter.
3. Download the XML file and upload it to your online banking interface to process the payments.
4. Once the SDD batch payment has been received, [reconcile the transaction](../bank/reconciliation.html) with the batch payment to mark the related invoices as
   Paid.

> **Note:**
>
> - To view the payments and invoices linked to a specific SDD mandate, click the
>   Collections and Invoices Paid smart button on the [Direct Debit
>   Mandate] form.
> - Click Re-generate Export file in the batch payment form to regenerate the XML file.

> **Note:**
>
> - [Batch payments](batch.html)
> - [SEPA Direct Debit for online payments](../../payment_providers/bank_payments.html#payment-providers-bank-payments-sdd)
> - [SEPA guidelines](https://www.europeanpaymentscouncil.eu/document-library/implementation-guidelines/sepa-credit-transfer-inter-psp-implementation-guidelines)

## SDD rejections

SDD rejections can occur for several reasons, the most common being insufficient funds in the
customer’s account. With SDD, the recipient’s account is credited before the funds are actually
debited from the customer’s account. As a result, if an SDD payment is later rejected, the bank
automatically withdraws the amount of that payment from the recipient’s account, and a new
transaction for a negative amount is created to reflect the SDD rejection.

SDD rejections are handled differently depending on whether [outstanding accounts](../get_started/journals.html#accounting-journals-outstanding-accounts) are configured or not for the SDD payment method.

> **Note:**
>
> The following procedures assume that the incoming SDD payment’s bank transaction has already
> been [reconciled](../bank/reconciliation.html#accounting-reconciliation-reconcile) with the payments or invoices.

Without outstanding accountsUsing outstanding accounts

If no [outstanding accounts](../get_started/journals.html#accounting-journals-outstanding-accounts) are configured
for the SDD payment method, no journal entry is created. In this case, you must cancel and
unreconcile the payment.

1. Access the invoice linked to the rejected SDD payment.
2. Click the Payments smart button to access the payment associated with the
   invoice.
3. Click Reset to draft, then Cancel.
4. Go back to the invoice and click the  (information) icon
   in the footer of the Invoice Lines tab, then click Unreconcile.
5. [Access the bank journal’s reconciliation view](../bank/reconciliation.html#accounting-reconciliation-access) and
   [reconcile](../bank/reconciliation.html#accounting-reconciliation-reconcile) the transaction created for the
   SDD rejection with the debit (negative journal item) to the account receivable on the
   incoming bank transaction.

If an [outstanding account](../get_started/journals.html#accounting-journals-outstanding-accounts) is set on the
SDD payment method, SDD payments create journal entries. If an SDD payment is rejected,
you must reverse the journal entry associated with the rejected payment and reconcile the
reversal of the journal entry with the transaction for the SDD rejection. To do so, follow
these steps:

1. Access the invoice linked to the rejected SDD payment.
2. Click the  (information) icon in the footer of the
   Invoice Lines tab, then click View to access the payment associated
   with the invoice.
3. Click the Journal entry smart button to access the related journal entry.
4. Click Reverse entry, optionally edit the fields in the popup, then click
   Reverse. A reversal entry is created with a Reference mentioning
   the initial journal entry. As a result, the invoice is marked as Not paid.
5. [Access the bank journal’s reconciliation view](../bank/reconciliation.html#accounting-reconciliation-access) and
   [reconcile](../bank/reconciliation.html#accounting-reconciliation-reconcile) the transaction created for the
   SDD rejection with the reversal of the entry related to the payment.

---

# Follow-up on invoices

Follow-up messages can be sent to customers when payments are overdue. Odoo helps identify late
payments and allows scheduling and sending the appropriate reminders using **follow-up actions**
according to the number of overdue days. Follow-ups can be sent through different methods, including
email, WhatsApp message, SMS, or post.

> **Note:**
>
> - [Odoo Tutorials: Payment Follow-up](https://www.youtube.com/watch?v=50qy2ygS7eM)
> - [Payment terms and installment plans](../customer_invoices/payment_terms.html)

## Configuration

To configure Follow-up actions, go to Accounting ‣ Configuration
‣ Follow-up Levels. In the Follow-up Levels list view, several follow-up levels and
actions are configured by default.

To modify a follow-up level, click on the record. From the form view, edit the
Description or adjust the number of days before a reminder is sent. In the
Notification tab, select Actions such as Send Email,
[Send WhatsApp message](../../../productivity/whatsapp.html), [Send SMS Message](../../../marketing/sms_marketing/pricing_and_faq.html#pricing-pricing-and-faq), and [Send a Letter](../customer_invoices/snailmail.html#customer-invoices-snailmail).

> **Note:**
>
> Sending letters and WhatsApp or SMS messages in Odoo requires [In-App Purchase (IAP)](../../../essentials/in_app_purchase.html) credit or tokens.

To use a pre-filled template when sending an email or letter, select a Content Template.
To modify it, click the  (internal link arrow) icon next to the
Content Template field. If enabled, WhatsApp and SMS messages use a
specific WhatsApp Template or Sms Template field that can be modified by
clicking the  (internal link arrow) icon.

Other options can be enabled in the Options section within the specific follow-up level:

- Automate the reminder with the Automatic option.
- Attach Invoices that are overdue in the reminder.
- Add followers on the related customer to receive notifications about any email reply
  made on the reminder’s email.

In the Activity tab, enable the option to automatically schedule [activities](../../../essentials/activities.html) when the follow-up level is triggered. Select the
Responsible user and the Activity Type, and enter a Summary.

To add a new Follow-up Level, click New and fill in the fields.

> **Note:**
>
> Set a negative number of days to send a reminder before the invoice due date.

## Invoice follow-ups

> **Note:**
>
> Reconcile all bank transactions before starting the follow-up process to avoid sending reminders
> for invoices that have already been paid.

To view all overdue invoices, go to Accounting ‣ Customers ‣ Invoices. In the
Invoices list view, click into the search bar and filter on Overdue.

### Follow-ups for one customer

For a detailed overview of a customer’s invoice follow-up status, go to Accounting
‣ Customers ‣ Customers. Open the customer’s form and click the Accounting tab. In
the Invoice follow-ups section, click on the different levels to view the
Follow-up Status of each level. If actions are needed, click Overdue
Invoices to have a detailed list of the overdue invoices.

Additional options can be set:

- Reminders: These are either Automatic or Manual.
- Next reminder: The date by which the next follow-up actions should be taken is
  automatically set when follow-ups are processed, but can be manually adjusted if needed.
- Responsible: The user who handles the follow-up actions.

To manually send a payment reminder to a customer, click Send and select the actions in
the Send and Print window:

- Print
- Email
- WhatsApp
- Sms
- By post

Enable the Attach Invoices option, and change the Content Template,
WhatsApp Template, or Phone if needed. Then, click Send or
Send & Print to send the [follow-up report].

> **Note:**
>
> [In-app purchases (IAP)](../../../essentials/in_app_purchase.html)

> **Note:**
>
> - The contact information on the invoice or the contact form is used to send the reminder.
> - The chatter keeps a full record of all follow-up actions.

### Follow-ups for all customers due for action

After setting up the additional [follow-up] options, review which customers have
overdue invoices or require follow-up. To do so, go to Accounting ‣ Customers ‣
Customers. In the Customers kanban view, click the search bar and filter by
Overdue Invoices or Requires Follow-up.

To take follow-up actions for all relevant customers, switch to the list view and select the
customers requiring follow-up. Then, click  (Actions) and select
Process Follow-ups to send them the [follow-up report].

## Reports

### Customer statement

To get a comprehensive overview of a customer’s account status, click the Customer
Statement smart button on the customer’s form. This statement corresponds to the [Partner
Ledger](../customer_invoices.html#accounting-invoices-partner-ledger) report’s portion specific to that customer.

To send it to the customer, click Send, change the Email Template if needed,
and click Print & Send.

To view the customer statements for multiple customers at once, select the customers from the
Customers list view, click  (Actions), and select
Open Customer Statements.

Click PDF or XLSX to generate a PDF or XLSX file, respectively.

### Follow-up report

To get a complete overview of a customer’s due invoices, separating those that are due from those
that are overdue, click the [Customer Statement]
smart button on the customer’s form. Then, click  Report: Customer
Statement and select Follow-Up Report.

To view the follow-up report for all customers at once, go to Accounting ‣
Reporting ‣ Partner Ledger. Then, click  Report: and select
Follow-Up Report.

Click PDF or XLSX to generate a PDF or XLSX file, respectively.

---

# Pay with SEPA

SEPA, the Single Euro Payments Area, is a payment-integration initiative of the European Union to
simplify bank transfers denominated in euros. SEPA allows you to send payment orders to your
bank to automate bank wire transfers.

SEPA is supported by the banks of the 27 EU member states, as well as:

EFTA countries:

- Iceland;
- Liechtenstein;
- Norway;
- Switzerland.

Non-EEA SEPA countries:

- Andorra;
- Monaco;
- San Marino;
- United Kingdom;
- Vatican City State.

Non-EEA territories:

- Saint-Pierre-et-Miquelon;
- Guernsey;
- Jersey;
- Isle of Man.

When paying a bill in Odoo, you can select SEPA mandates as a payment option. At the end of the day,
you can generate the SEPA file containing all bank wire transfers and upload it to your online
banking interface to process the payments.

By default, the file follows the SEPA Credit Transfer **‘pain.001.001.03’** specifications. This is
a well-defined standard among banks. However, for Swiss and German companies, other formats are used
**‘pain.001.001.03.ch.02’** for Switzerland and **‘pain.001.003.03’** for Germany.

Once the payments are processed by your bank, you can directly import the account statement in
Odoo. The bank reconciliation process will seamlessly match the SEPA orders you sent to your bank
with actual bank statements.

## Configuration

### Activate SEPA Credit Transfer (SCT)

To pay suppliers with SEPA, you must activate the **SEPA Credit Transfer** setting. To do so, go to
Accounting ‣ Configuration ‣ Settings ‣ Vendor Payments: SEPA Credit Transfer
(SCT). By activating the setting and filling out your company data, you will be able to use the
SCT option when paying your vendor.

> **Note:**
>
> According to the localization package installed, the **SEPA Direct Debit** and **SEPA Credit
> Transfer** modules may be installed by default. If not, they need to be [installed](../../../general/apps_modules.html#general-install).

### Activate SEPA payment methods on banks

From the accounting dashboard, click on the drop-down menu (⋮) on your bank journal and
select Configuration. Click the Outgoing Payments tab, and, if not already
present, add SEPA Credit Transfer under Payment Method.

Make sure to specify the IBAN account number (domestic account numbers do not work with SEPA) and
the BIC (bank identifier code) in the Journal Entries tab.

### Registering payments

You can register any vendor payments made with SEPA. To do so, go to Accounting ‣
Vendors ‣ Payments. When creating your payment, select SEPA Credit Transfer as the
Payment Method.

The first time you pay a vendor with SEPA, you have to fill in the Recipient Bank
Account field with the bank name, IBAN, and BIC (Bank Identifier Code). Odoo automatically verifies
if the IBAN format is respected.

For future payments to this vendor, Odoo will automatically suggest you the bank account, but it
remains possible to select a new one.

Once your payment is registered, do not forget to confirm it. You can also pay vendor bills from the
bill directly using the Register Payment button at the top of a vendor bill.
The form is the same, but the payment is directly linked to the bill and will be automatically
reconciled with it.

---

# Pay by checks

Once you decide to pay a supplier bill, you can select to pay by check. You can then print all the
payments registered by check. Finally, the bank reconciliation process will match the checks you
sent to suppliers with actual bank statements.

## Configuration

### Activate checks payment methods

To activate the checks payment method, go to Accounting ‣ Configuration ‣
Settings, and scroll down to the Vendor Payments section. There, you can activate the
payment method as well as set up the Check Layout.

> **Note:**
>
> - Once the Checks setting is activated, the **Checks** payment method is
>   automatically set up in the Outgoing Payments tabs of **bank** journals.
> - Some countries require specific modules to print checks; such modules may be installed by
>   default. For instance, the U.S. Checks Layout module is required to print U.S.
>   checks.

## Compatible check stationery for printing checks

### United States

For the United States, Odoo supports by default the check formats of:

- **Quickbooks & Quicken**: check on top, stubs in the middle and bottom;
- **Peachtree**: check in the middle, stubs on top and bottom;
- **ADP**: check in the bottom, and stubs on the top.

## Pay a supplier bill with a check

Paying a supplier with a check is done in three steps:

1. registering a payment
2. printing checks in batch for all registered payments
3. reconciling bank statements

### Register a payment by check

To register a payment, open any supplier bill from the menu Purchases ‣ Vendor
Bills.
Once the supplier bill is validated, you can register a payment. Set the Payment Method
to Checks and validate the payment.

### Print checks

On your Accounting Dashboard in the Bank Journal, you can see the
number of checks registered. By clicking on Checks to print you have got the possibility
to print the reconciled checks.

To print all checks in batch, select all payments from the list view and click on Print.

---

# Forecast future bills to pay

In Odoo, you can manage payments by setting automatic **Payments Terms** and **follow-ups**.

## Configuration: payment terms

In order to track vendor conditions, we use **Payment Terms** in Odoo. They allow keeping track of
due dates on invoices. Examples of **Payment Terms** are:

- 50% within 30 days
- 50% within 45 days

To create them, go to Accounting ‣ Configuration ‣ Invoicing: Payment Terms and
click on Create to add new terms or click existing ones to modify them.

> **Note:**
>
> [Odoo Tutorials: Payment Terms](https://www.odoo.com/slides/slide/payment-terms-terms-and-conditions-6852)

Once **Payment Terms** are defined, you can assign them to your vendor by default. To do so, go to
Vendors ‣ Vendors, select a vendor, click the Sales & Purchase tab,
and select a specific **Payment Term**. This way, every time you purchase from this vendor, Odoo
automatically proposes the chosen Payment Term.

> **Note:**
>
> If you do not set a specific Payment Term on a vendor, you can still set one on the vendor bill.

## Forecast bills to pay with the aged payable report

To track amounts to be paid to the vendors, use the **Aged Payable** report. To access it, go to
Accounting ‣ Reporting ‣ Partner Reports: Aged Payable. This report gives you a
summary per vendor of the amounts to pay, compared to their due date (the due date being computed on
each bill using the terms). This report tells you how much you will have to pay within the following
months.

## Select bills to pay

You can get a list of all your vendor bills by going to Vendors ‣ Bills. To view
only the bills that you need to pay, click Filters ‣ Bills to Pay. To view only
overdue payments, select the Overdue filter instead.

You can also group bills by their due date by clicking Group By ‣ Due Date and
selecting a time period.

---

# Trusted accounts (send money)

To protect users from sending money to scammers, vendor bank account numbers must be marked as
trusted before you can use them to make an outgoing payment.

To do so, open the vendor bank account and click on the Send Money toggle switch button.

![Example of a vendor bank account with the "Send Money" toggle button switched to "trusted."](../../../../_images/send-money-toggle.png)
> **Note:**
>
> All accounts are initially marked as untrusted.

## Phishing attacks

A **phishing attack** is an online scam designed to trick individuals or companies into giving away
sensitive information or money by sending out fraudulent communication. Fraudsters pretend to be
legitimate companies and may use partial information to give credibility to their requests.

There are several types of phishing attacks, including **invoice fraud**. In this case, the
fraudster pretends to be a genuine supplier following up on unpaid bills or sending a new invoice,
but with different payment information than usual and with fake contact details.

To protect yourself from these types of phishing attacks, remain vigilant when you receive
unexpected invoices or payment requests.

> **Warning:**
>
> In case of doubt, **we recommend contacting the vendor by phone**. Make sure to call an official
> phone number by searching yourself, as the URLs, email addresses, and phone numbers written in
> the communication you received may be fake.

### Elements to check

There are several elements you can check by yourself when you receive an outgoing payment request to
a new account:

Communication style
:   Fraudulent emails and invoices often use a different communication style, such as **different
    wording**, and may include **spelling and grammatical mistakes**. Examine and **compare** them
    with previous ones that you know to be authentic (e.g., payment instructions, language, company
    logo, etc.).\*

Urgency
:   Invoice frauds often use **urgent or threatening language** and change the **payment deadline**.
    Check if you really received a late payment reminder previously.

Type of account
:   A company is unlikely to replace a bank account with a **money transfer service**.

Email and links domain names
:   Double-check the **email address domain** (`example@domain.com`). However, be wary that fraudsters
    can make their email addresses look genuine or even hack email addresses from your vendor’s
    employees or even someone within your own organization.

    Hover over the links in your email and check that the URLs they redirect to are genuine. Your
    internet browser usually displays the link’s target at the bottom left of the window.

---

# Bank and cash accounts

You can manage as many bank or cash accounts as needed on your database. Configuring them correctly
allows you to have all your banking data up-to-date and ready for [reconciliation](bank/reconciliation.html) with your journal entries.

In Odoo Accounting, each bank account has a dedicated journal set to post all entries in a dedicated
account. Both the journal and the account are automatically created and configured whenever you add
a bank account.

> **Note:**
>
> [Cash journals](get_started/journals.html#accounting-journals-cash) and accounts must be configured manually.

Bank journals are displayed by default on the Accounting Dashboard in the form of cards
which include action buttons.

![Bank journals are displayed on the Accounting Dashboard and contain action buttons](../../../_images/card.png)

## Manage bank and cash accounts

### Connect a bank for automatic synchronization

To connect your bank account to your database, go to the Accounting Dashboard and on the
kanban card of an unconnected bank, click Search over 26000 banks. Select your bank from
the list, click on Connect, and follow the instructions.

> **Note:**
>
> [Bank synchronization](bank/bank_synchronization.html)

### Create a bank account

If your banking institution is not available in Odoo, or if you don’t want to connect your bank
account to your database, you can configure your bank account manually.

To manually add a bank account, go to the Accounting Dashboard and on the kanban card of
an unconnected bank, click Search over 26000 banks. Then, click on Record
transactions manually (at the bottom right), fill out the bank information, and click
Create.

> **Note:**
>
> - Odoo automatically detects the bank account type (e.g., IBAN) and enables some features
>   accordingly.
> - A default [bank journal](get_started/journals.html#accounting-journals-bank) is available and can be used to
>   configure your bank account by going to Accounting ‣ Configuration ‣
>   Accounting: Journals ‣ Bank. Open it and edit the different fields to match your bank
>   account information.

---

# Bank synchronization

Odoo synchronizes directly with your bank institution to automatically import all bank transactions
into the database. It supports over 26,000 financial institutions worldwide and relies on multiple
[third-party providers] to connect with
banks.

> **Note:**
>
> To use this service, a valid Odoo Enterprise subscription is required.

> **Note:**
>
> To check if your bank is compatible with Odoo, go to [Odoo Accounting Features](https://www.odoo.com/app/accounting-features#part_5), and click See list of
> supported institutions in the Bank & Cash section.

> **Note:**
>
> [Transactions](transactions.html)

## Configuration

### First synchronization

To synchronize the database with a bank, go to the Accounting Dashboard, click New, and
select the Bank card. In the Add a Bank Account window, select the relevant
bank and click Connect.

> **Note:**
>
> - Alternatively, click the  (vertical ellipsis) icon of the
>   Bank journal, and Connect bank, or click Search over 26000
>   banks in the Accounting dashboard.
> - Depending on your bank and country, you can select the Type of account and/or
>   choose another [third-party provider]
>   to connect with the bank if needed before clicking Connect.
> - If your bank is not listed in the Search for an institution window, scroll down the
>   list and click  Add new bank to create a bank account manually. Fill
>   in the Account Number, Bank, and SWIFT Code, and click
>   Connect. A bank journal is then created and named using the account number. Note
>   that in this case, the bank is not synchronized.
> - If issues occur during the first synchronization, check that no firewall or proxy is blocking
>   the address <https://production.odoofin.com/>. Make sure your web browser allows pop-ups and that
>   any ad-blocker is disabled.

> **Warning:**
>
> When setting up bank synchronization, accounting transactions are automatically recorded from the
> date of the last transaction +1 day (e.g., if the last transaction date is 31/12/2025, the
> recording starts on 01/01/2026). If the journal contains no transactions, all available past
> transactions are retrieved. To limit the retrieval period, go to Accounting ‣
> Accounting ‣ Lock Dates, and set a date in the Lock Everything field.

> **Note:**
>
> - Some banks are in a Beta status, meaning they’re not yet fully supported by
>   third-party providers. This may lead to bugs or other issues. Although they can be used, Odoo
>   does not provide technical support in this case.
> - The [third-party provider] may
>   request more information to connect with a bank. This information is not stored on Odoo’s
>   servers.
> - To view all past synchronizations, activate the [developer mode](../../../general/developer_mode.html#developer-mode) and go to
>   Accounting ‣ Configuration ‣ Online Synchronization.

### Manual synchronization

After the [first synchronization], bank
journals are synchronized by default every twelve hours. To manually trigger synchronization, go to
the Accounting dashboard and click Fetch Transactions on the relevant bank journal.

> **Note:**
>
> Alternatively, activate the [developer mode](../../../general/developer_mode.html#developer-mode), go to
> Accounting ‣ Configuration ‣ Online Synchronization, select the relevant
> bank, and click Fetch transactions.

> **Note:**
>
> - Some banks do not support automatic transaction fetching. For these institutions, an error
>   message appears during the automatic account synchronization, prompting the user to disable the
>   automatic synchronization. This message is also logged in the chatter of the online
>   synchronization. In such cases, disable the Automatic synchronization option in the
>   corresponding bank’s Online Synchronization and make sure to perform manual
>   synchronizations by clicking Fetch Transactions on the relevant bank journal.
> - For some bank institutions, transactions can only be fetched up to three months in the past. If
>   older transactions are needed, they can be [imported](transactions.html#accounting-transactions-import).

### Update synchronization credentials

To update bank credentials, activate the [developer mode](../../../general/developer_mode.html#developer-mode), and go to
Accounting ‣ Configuration ‣ Online Synchronization. Open the connection that
needs to be updated, click Update Credentials, and follow the steps.

> **Note:**
>
> - The steps may vary depending on the third-party provider, as each provider follows its own
>   process.
> - When updating bank credentials, make sure all accounts are selected for synchronization,
>   including those from other banking institutions if applicable.

### Third-party providers

Odoo relies on third-party providers to securely connect to your bank accounts and automatically
import transactions and financial data into the database. The following providers are used:

- [Plaid](https://plaid.com/discover-apps/) (supported in the [United States of America and Canada](https://plaid.com/docs/institutions/))
- [Yodlee](https://www.yodlee.com/) (supported in Europe)
- [Salt Edge](https://www.saltedge.com/) (supported [worldwide](https://www.saltedge.com/products/account_information/coverage))
- [Ponto](bank_synchronization/ponto.html) (supported in Europe)
- [Enable Banking](https://enablebanking.com/) (supported in [Scandinavian countries](https://enablebanking.com/open-banking-apis))

> **Note:**
>
> When [connecting a bank to Odoo]:
>
> - Depending on your bank and country, change the default third-party provider when selecting the
>   bank, if necessary.
> - Make sure to check the consent checkbox to allow information to be shared with Odoo.
> - Select all accounts that need access and synchronization, including those from other banking
>   institutions.

> **Note:**
>
> - [Bank synchronization troubleshooting]
> - [Salt Edge bank synchronization troubleshooting]
> - [Ponto bank synchronization troubleshooting](bank_synchronization/ponto.html#accounting-bank-synchronization-ponto-troubleshooting)

## Duplicate transactions

When importing transactions, some may appear [duplicated](transactions.html#accounting-transactions-duplicate)
due to the same online transaction identifier or the same currency, amount, account number, and
date.

## Missing transactions

Missing or pending transactions are entries that the bank has not yet validated.

To find missing and pending transactions, access the [bank reconciliation view](reconciliation.html#accounting-reconciliation-access), click the  (gear) icon, and select
Find Missing Transactions.

To import a posted missing transaction, select it and click Import Transactions.

> **Note:**
>
> - Make sure the connection with the bank is active to find missing transactions.
> - Pending transactions cannot be imported.

## Troubleshooting

> **Note:**
>
> [Bank synchronization troubleshooting - Ponto](bank_synchronization/ponto.html#accounting-bank-synchronization-ponto-troubleshooting)

### Synchronization errors or disconnections

To report a connection error to [Odoo support](https://www.odoo.com/help), activate the
[developer mode](../../../general/developer_mode.html#developer-mode), go to Accounting ‣ Configuration ‣
Online Synchronization, select the failed connection, and copy the error description and the
reference.

If the connection with the proxy is lost and reconnection using the Reconnect option
isn’t successful, contact [support](https://www.odoo.com/help) directly. Provide the client ID or
the error reference from the chatter.

### Why is the synchronization not working in real-time?

Synchronization is not designed to work in real time, as third-party providers synchronize accounts
at different intervals. To manually trigger synchronization and retrieve bank transactions, go to
the Accounting Dashboard, and click Fetch Transactions.

Alternatively, to synchronize and fetch transactions, activate the [developer mode](../../../general/developer_mode.html#developer-mode) and go to Accounting ‣ Configuration ‣ Online
Synchronization.

Some providers restrict refreshes to once per day. If transactions have already been fetched,
clicking Fetch Transactions again may not retrieve the latest data.

Transactions may appear on a bank account, but cannot be fetched if they have a Pending
status; only transactions with a Posted status are retrieved.

### Why do my transactions only synchronize when I refresh manually?

Some banks implement additional security measures and require extra steps, such as an SMS or email
authentication code, or another type of MFA. As a result,
the third-party provider cannot retrieve transactions until the security code is provided.

### Why are no transactions visible?

There are a few possible reasons for this issue:

- No bank accounts were synchronized during the [first synchronization].
- There may be no new transactions available to fetch.

If the bank account is correctly linked to a journal, but posted transactions still aren’t visible
in the database, contact [support](https://www.odoo.com/help).

### Why are no accounts shown after synchronization?

During the synchronization process, a bank institution was selected, but no bank accounts from this
institution were authorized during the [first synchronization].

### Saltedge troubleshooting

#### Why is there an error when deleting a synchronization in Odoo?

Odoo can’t permanently delete the connection established with the banking institution. However,
it revokes consent, which prevents Odoo from accessing the account. The error message indicates that
the consent has been revoked, but the record could not be deleted as it remains in Salt Edge.

To delete the connection, connect to the [Salt Edge account](https://www.saltedge.com/dashboard)
and manually remove the synchronization. Once this is done, the record can be deleted in Odoo.

#### I have an error saying that this account has already been synchronized

The bank account has already been synchronized with Salt Edge. Access the Salt Edge [dashboard](https://www.saltedge.com/dashboard) to check if a connection with the same credentials exists.
There are two options:

- If a connection with the same credentials exists in Salt Edge but has not been synchronized with
  Odoo, delete the existing connection and create a new one from the Odoo database.
- If a connection with the same credentials exists in Salt Edge and has already been synchronized
  with Odoo, [update the synchronization credentials] to reactivate the connection.

---

# Transactions

Importing transactions from your bank statements allows keeping track of bank account transactions
and reconciling them with the ones recorded in your accounting.

[Bank synchronization](bank_synchronization.html) automates the process. However, if you do not
want to use it or if your bank is not yet supported, other options exist:

- [Import bank transactions] delivered by your bank;
- [Register bank transactions] manually.

> **Note:**
>
> [Grouping transactions by statement] is optional.

## Transaction view

The list of transactions for the bank journal is displayed in the Bank Matching view. To
access it, go to the Accounting Dashboard, then either:

- click the journal name (e.g., Bank) or its Transactions button to display
  all transactions, including those previously reconciled, or
- click the x to reconcile button to display only unreconciled transactions. To include
  previously reconciled transactions, remove the Not Matched filter from the search bar.

Unreconciled transactions display the following information while collapsed:

- The date of the transaction
- A button linked to the chatter. The icon of this button can vary:

  - The  (comments) icon displays only on hover and indicates that
    there are no attachments or activities for the transaction.
  - The  (attachments) icon indicates that there is an attachment on
    the journal entry.
  - The  (activities) icon indicates that there is an activity
    scheduled on the journal entry.
- The label of the transaction
- The partner of the transaction (if one is set)
- Up to two [action buttons](reconciliation.html#accounting-reconciliation-action-buttons), depending on the
  details of the transaction
- The balance of the transaction

> **Note:**
>
> - When the chatter of a transaction is open, a blue tag highlights the related transaction.
> - The chatter can be opened and closed by clicking the
>   (comments) icon and the  (close) icon in the top right
>   of the view.
> - Once a transaction is [reconciled](reconciliation.html), its action buttons are replaced with
>   the labels of the item(s) it was reconciled with or the account if it was reconciled with the
>   Set Account action button.

## Duplicate transactions

Duplicate transactions occur when either by human error or [bank sync](bank_synchronization.html)
error, the same transaction is created multiple times. The duplicate transaction view identifies
potential duplicate transactions so they can be selected and deleted. To access the duplicate
transaction view, first access the Bank Matching view by going to the
Accounting Dashboard and clicking the bank journal’s name, then open the
Actions menu and click Find Duplicate Transactions.

Potential duplicate transactions are identified based on their amount, date, and account number, or
(if the transaction is created via [bank sync](bank_synchronization.html)) the transaction ID.

Select a Starting Date to view the corresponding potential duplicate transactions, then
select the transactions to delete and click  Delete Selected.

> **Note:**
>
> Any transactions created by [bank sync](bank_synchronization.html) that the bank sync provider
> determines to be potential duplicates are displayed in the Provider Duplicates tab.
> This tab is only visible if there are any potential duplicates according to the provider.

## Import transactions

Odoo supports multiple file formats to import transactions:

- SEPA recommended Cash Management format (CAMT.053)
- Comma-separated values (CSV)
- Excel (XLSX)
- Open Financial Exchange (OFX)
- Quicken Interchange Format (QIF)
- Belgium: Coded Statement of Account (CODA)

To import a file, go to the Accounting Dashboard, click the
(ellipsis) icon on the Bank journal, and select Import file.
Next, select the file and upload it.

> **Note:**
>
> Alternatively, access the transaction list by:
> :   - clicking on the Bank journal’s name, then clicking Upload
>     - dragging and dropping a file on the bank journal on the Accounting Dashboard
>     - dragging and dropping a file on the Bank Matching view

Certain file types such as CSV and XLSX, then require setting the necessary formatting options and
mapping the file columns with their related Odoo fields, after which you can run a Test
and Import your bank transactions. Other file types are mapped automatically.

> **Note:**
>
> [Export and import data](../../../essentials/export_import_data.html)

## Register bank transactions manually

You can also record your bank transactions manually. To do so, go to the Accounting
Dashboard, click the Bank journal’s name, and then on New. The
Partner field is optional to ease the reconciliation process, but the Label
and Date fields are mandatory.

## Statements

A **bank statement** is a document provided by a bank or financial institution that lists the
transactions that have occurred in a particular bank account over a specified period of time.

In Odoo Accounting, it is optional to group transactions by their related statement, but depending
on your business flow, you may want to record them for record-keeping and organizational purposes.

To access a list of existing statements, go to the Accounting Dashboard, click the
 (dropdown menu) icon next to the bank or cash journal you want to
check, then click Statements.

> **Warning:**
>
> To ensure the ending balances of your bank statements in Odoo align with the ending balances of
> the statements that are provided by your bank, create an opening transaction to record the bank
> account balance as of the date you begin synchronizing or importing transactions. This is
> necessary to ensure the accuracy of your accounting.

> **Note:**
>
> To access a statement’s transactions, click Transactions directly from the
> Bank Statements list view or open a statement and click the Statement
> lines smart button.

### Statement creation

The Bank Matching view displays transactions from most recent to oldest and groups them
by statement, with any recent transactions that do not belong to a statement at the top. To add
transactions to a statement, hover on the most recent transaction that should be included in the
statement, and click the Statement button that appears on the upper separator line.
Doing so creates a statement from that transaction down to the oldest transaction that is not yet
part of a statement.

![A "Statement" button is visible when hovering on a transaction.](../../../../_images/statements-kanban.png)

In the Create Statement window, fill out the statement’s Reference, verify
its Starting Balance and Ending Balance, add an attachment such as a PDF
of the statement if desired, and click Save.

> **Note:**
>
> Transactions can also be added to statements from the list view. Select all the transactions
> corresponding to the bank statement, and, in the Statement column, select an existing
> statement or create a new one by typing its reference, clicking on Create and
> edit…, filling out the statement’s details, and saving.

### Statement viewing, editing, and printing

To view an existing statement, click the statement amount in the Bank Matching view
or click the statement name and then the  (Internal link) icon in
the Bank Matching list view. From here, you can edit the Reference,
Starting Balance, Ending Balance, and Attachments.

> **Note:**
>
> - Manually updating the Starting Balance automatically updates the Ending
>   Balance based on the new value of the Starting Balance and the value of the
>   statement’s transactions.
> - If the Starting Balance doesn’t equal the previous statement’s Ending
>   Balance, or if the Ending Balance doesn’t equal the running balance
>   (Starting Balance plus the statement’s transactions), a warning appears explaining
>   the issue. To maintain flexibility, it is still possible to save without first resolving the
>   issue.

To generate and print a PDF of the bank statement, click the  (gear) icon
and click  Statement.

> **Note:**
>
> When a bank statement is generated to be printed, it is automatically added to the
> Attachments if no file was attached when creating the statement.

---

# Bank reconciliation

**Bank reconciliation** is the process of validating [bank transactions](transactions.html). Many
of these transactions are matched with counterpart items related to business records such as
[customer invoices](../customer_invoices.html), [vendor bills](../vendor_bills.html), and
[payments](../payments.html), while others that may not have a matching counterpart item (such as
bank fees) can be written off [manually] or with
[reconciliation models]. Not only is bank reconciliation
compulsory for most businesses, but it also offers several benefits, such as reduced risk of errors
in financial reports, detection of fraudulent activities, and improved cash flow management.

Thanks to the [default matching rules] and customizable
bank [reconciliation models](reconciliation_models.html), Odoo selects the matching items
automatically when possible.

> **Note:**
>
> - [Odoo Tutorials: Bank reconciliation](https://www.odoo.com/slides/slide/bank-reconciliation-6562)
> - [Bank synchronization](bank_synchronization.html)
> - [Transactions](transactions.html)

## Bank reconciliation view

To access a journal’s Bank Matching view, go to the Accounting Dashboard and
either:

- click the journal name (e.g., Bank) or its Transactions button to display
  all transactions, including those previously reconciled, or
- click the x to reconcile button to display only unreconciled transactions. To include
  previously reconciled transactions, remove the Not Matched filter from the search bar.

![Reaching the bank reconciliation tool from the accounting dashboard](../../../../_images/bank-card.png)

The Bank Matching view is composed of lines for each transaction of the journal with the
newest displayed first. Each transaction has a date, a label, a partner (if set), [action
buttons], and the transaction amount. Each line can be
expanded to show additional information and buttons.

![The user interface of the bank matching view of a bank journal.](../../../../_images/user-interface.png)
> **Note:**
>
> Once a [transaction](transactions.html) is reconciled, the suggested action button(s) is
> replaced with the counterpart entry/entries it was matched with or the account(s) it was written
> off to.

### Transactions

Every [transaction](transactions.html) is linked to a journal entry that debits/credits the
journal’s main account and its suspense account until it is fully reconciled. At that point, the
suspense account is replaced with the account of the counterpart item or, in the case of
[manual matching], the selected account.

> **Note:**
>
> - [Duplicate transactions](bank_synchronization.html#accounting-bank-synchronization-duplicate-transactions)
> - [Missing transactions](bank_synchronization.html#accounting-bank-synchronization-missing-transactions)

#### Possible action buttons

Up to two suggested action buttons are available as primary buttons, but all available action
buttons are displayed when the transaction is expanded. The following action buttons are available
depending on the details of the transaction:

- Set Partner: Open a search view to add a partner to the transaction.
- Set Account: Open a search view to manually select an account to write off the full
  amount of the transaction with this account. If necessary, [edit the line] to change the amount.
- Receivable: Write off the transaction to the receivable account of the partner.
- Sales: Open a list view of sales orders belonging to the transaction’s
  Partner (or proceed directly to the form view if only one relevant sales order
  exists). Select the relevant sales order(s) and click Create Invoices, then return to
  the Bank Matching view and match the invoice(s) using the Reconcile action
  button.
- Payable: Write off the transaction to the payable account of the partner.
- Reconcile: Open a search view of existing items from records such as customer
  invoices, vendor bills, and payments. Select one or multiple items to add counterpart items with
  the corresponding accounts of those items.
- Batches: Open a short list of [batch payments](../payments/batch.html). To view all
  batch payments, click Search More …. Select a batch payment to add a counterpart
  item for each payment of the batch with the corresponding account of each payment.
- [Reconciliation models](reconciliation_models.html): Each manual reconciliation model that could apply to the transaction
  is displayed. Click the reconciliation model’s action button to generate the counterpart items
  defined on the reconciliation model.

> **Note:**
>
> To remove the partner from a transaction, click the  (close) icon
> next to the partner’s name.

Click the  (chevron down) button next to the possible action
buttons of an expanded line to display any of the above action buttons that are hidden due to space
limitations, as well as the following:

- Upload bills: Upload one or more bills to be [digitized](../vendor_bills/invoice_digitization.html). After digitization, the bills are available for matching
  via the Reconcile action button.
- Manage Models: Open the list view of [Reconciliation models](reconciliation_models.html).
- Open Journal Entry: Open the journal entry of this transaction.
- Delete Transaction: Delete this transaction.

> **Note:**
>
> Uploading bills from the Bank Matching view does not automatically reconcile them
> with the active transaction.

> **Note:**
>
> [In-app purchases (IAP)](../../../essentials/in_app_purchase.html)

## Reconcile transactions

When possible, Odoo automatically reconciles transactions based on their fields.

If no partner is set on the transaction, the transaction’s Label is compared with the
Number, Customer Reference, Bill Reference, and
Payment Reference of existing invoices, bills, and payments.

If a partner is set on the transaction, the transaction is instead matched with invoices, bills, and
payments of the partner based on the Amount. The following rules are used in a
sequential order to identify and apply a match:

- Exact match
- Discounted match: for payment terms with discounts for early payments
- Tolerance match: within 3% to account for merchant fees, rounding differences, and user errors
- Currency match: when the transaction is in a different currency than the invoice, bill, or
  payment (with a 3% tolerance for exchange rate differences)
- Amount in label: if the invoice Amount is found in the transaction’s
  Label

In addition to using these fixed matching rules, transactions can be matched automatically with the
use of [reconciliation models](reconciliation_models.html). Otherwise, reconcile transactions
manually by following these steps:

1. Expand the desired line among unmatched bank transactions to display all available action
   buttons.
2. Define the counterpart. There are several options for defining a counterpart, including
   [matching existing items], [manually setting
   the account], matching with [batch payments](../payments/batch.html), and using [reconciliation model buttons].
3. If the resulting entry is not fully balanced, add another existing counterpart item or write it
   off by [setting the account] of the remaining
   amount.

### Existing items

To reconcile transactions with existing items related to records such as customer invoices, vendor
bills, and payments, click the Reconcile action button, select the matching journal
item(s) in the list, and click Select.

> **Note:**
>
> If the Partner is set, this list is automatically filtered to only include items
> related to that partner.

> **Note:**
>
> Use the search bar within the Search: Journal Items to Match window to search for
> specific journal items.

If a transaction amount is lower than the invoice or bill it is reconciled with, the transaction is
fully reconciled, but the difference remains open on the counterpart item. The remaining amount can
be left open to be reconciled later or the invoice or bill can be marked as fully paid. To mark the
invoice or bill as fully paid, [edit] the line, click
fully paid, and Save. To reverse this, [edit] the line again, click partial payment, and
Save.

If a transaction amount is greater than the invoice or bill it is reconciled with, the transaction
is only partially reconciled. The remaining balance can be reconciled as any other transaction
amount.

> **Note:**
>
> Existing items of draft entries can be matched. Eventual automatic moves (like currency exchange
> or cash basis moves) are created in draft simultaneously with the reconciliation. Posting the
> original entry also posts the automatic move.

### Set account

If no existing item matches the selected transaction, you can still write off the transaction
manually: Click Set Account, then choose the appropriate account. To write off only part
of the transaction, [edit the line] to reflect the correct
value and reconcile the remaining amount as desired.

> **Note:**
>
> If the partner is set, write the amount off to their receivable or payable account directly by
> clicking the Receivable or Payable [action button].

### Reconciliation models

Use [reconciliation models](reconciliation_models.html) to create custom rules that can be applied
automatically or manually via custom buttons for operations that are frequently repeated. These
custom buttons allow you to quickly reconcile bank transactions manually and can also be combined
with other reconciliation models and with counterpart items when reconciling transactions.

> **Tip:**
>
> An outgoing bank transaction for $103 is partially matched with a vendor bill for $100, leaving
> $3 of the transaction still unreconciled. Use the Bank Fees reconciliation model to
> create a new counterpart item for $3 and reconcile it with the remaining $3 of the bank
> transaction.

## Edit lines and unreconcile transactions

To edit a counterpart item, expand the line, click the  (pencil) icon,
and edit the necessary fields in Edit Line window.

> **Note:**
>
> When the counterpart item is an existing journal item, some fields are read-only.

If a transaction is partially matched with a counterpart item, use the link to mark the invoice as
fully paid or to switch back to a partial payment.

To unreconcile a transaction, delete all counterpart items associated with the transaction by
clicking on the  (trash) icon.

## Netting

Netting (also known as AP/AR offsetting) is the process of balancing incoming debts from and
outgoing debts to the same partner. Reconciling the incoming and outgoing debts creates a new
journal entry that balances the debts. Two main scenarios exist:

- [A bank transaction balances] (either fully or
  partially) the incoming and outgoing debts.
- [No bank transaction balances] the incoming
  and outgoing debts. This situation can occur either when the debts balance each other completely
  or when the debts remain unbalanced.

### Netting with bank transactions

When a bank transaction balances (either fully or partially) the incoming and outgoing debts,
reconcile the bank transaction from the Bank Matching view like any other [existing
items]:

1. Click Reconcile on the transaction.
2. Select all the relevant counterpart items on both the payable and receivable side.
3. Click Select.
4. If a balance remains, depending on the details, the following situations are possible:

   - An invoice, bill, or other item is not fully reconciled, and the remaining balance can be
     [reconciled] with other bank transactions.
   - The bank transaction itself is not fully reconciled, and the remaining balance can be
     [reconciled] as in any other situation.

### Netting without bank transactions

When no bank transaction balances the incoming and outgoing debts, there is nothing to reconcile
from the Bank Matching view. However, the debt amount is visible in both the account
receivable and the account payable. To balance these debts so that they no longer appear on the
partner ledger, follow these steps:

1. Go to Accounting ‣ Accounting ‣ Reconcile.
2. Select the journal items that debit or credit the account receivable and account payable and
   represent the debts to be netted.
3. Click Reconcile.
4. If the debts don’t balance each other perfectly, a Write-Off Entry popup window
   appears, allowing you to decide how to resolve the remaining balance:

   - Select Allow partials to only partially reconcile the account receivable and
     account payable and leave the remaining balance open.
   - Use a [reconciliation model button](reconciliation_models.html) to write off the balance.
   - Manually choose an Account, and optionally adjust the Tax,
     Journal, Label, Date, and To Check fields.

The items are then matched, and their balance is removed from the partner ledger, representing that
no payment is due for these debts.

> **Note:**
>
> The workflow is the same whether there are only two equal debts in the receivable and payable
> accounts or multiple debts in each account.

---

# Reconciliation models

Reconciliation models are custom rules that complement the [default set of matching rules](reconciliation.html#accounting-reconciliation-reconcile) and enable more advanced automation of the [bank
reconciliation](reconciliation.html) process. These models are especially useful when dealing with
recurring flows like writing off bank fees or [cash discounts](../customer_invoices/cash_discounts.html).

> **Note:**
>
> [Odoo Tutorials: Reconciliation models](https://www.odoo.com/slides/slide/reconciliation-models-6858)

## Configuration

To access reconciliation models, go to the Accounting Dashboard, click the
 (dropdown menu) menu on the bank journal, and select
Models under the Reconciliation section.

To create a new reconciliation model, click New.

Reconciliation models can be either Manual or Automated. Manual
reconciliation models appear as [possible action buttons](reconciliation.html#accounting-reconciliation-action-buttons) when [reconciling](reconciliation.html). Automatic
reconciliation models apply automatically to transactions that meet the reconciliation model’s
[matching conditions].

Each reconciliation model is configured with [matching conditions] to identify the relevant bank transactions and [Counterpart
Items] to be generated during reconciliation.

> **Note:**
>
> To create an activity on the transaction, select which type of activity to create in the
> Next Activity field.

> **Warning:**
>
> If a record matches with several reconciliation models, the first one in the *sequence* of models
> is applied. Rearrange the order by dragging and dropping the handle next to the name.
>
> ![Rearrange the sequence of models in the list view.](../../../../_images/list-view.png)

### Matching conditions

A reconciliation model’s matching conditions determine to which transactions it applies.

The following fields can be used to restrict the reconciliation model’s availability to transactions
that meet the conditions:

- Journals
- Partners
- Amount: Select Is lower than or equal to, Is greater than or
  equal to, or Is between and enter the amount(s).
- Label: Select Contains, Not Contains, or Match
  Regex and enter the transaction label’s matching condition.

> **Note:**
>
> [Regular expressions](https://regexone.com/), often abbreviated as **regex**, can be used in
> Odoo in various ways to search, validate, and manipulate data. Regex can be powerful but also
> complex, so it’s essential to use it judiciously.
>
> To use regular expressions in a reconciliation model, set the Label to
> Match Regex and add an expression. Odoo automatically retrieves the transactions
> that match the regex expression and the conditions specified in the reconciliation model.

> **Note:**
>
> A transaction must meet all conditions for the reconciliation model to be available for it. If no
> condition is defined (i.e., if all fields are left blank), the reconciliation model will be
> available for all transactions.

### Counterpart items

Each line in the Counterpart items tab creates a journal item with the specified
details:

- Partner: Select the partner, if any, to set on the journal item.
- Account: Select the account, if any, to set on the journal item.
- Amount Type: Select how the amount of the journal item should be calculated:

  - Fixed: Use a fixed amount.
  - Percentage of balance: Use a percentage of the remaining balance of the
    transaction, regardless of the transaction total.
  - Percentage of statement line: Use a percentage of the transaction total, regardless
    of the remaining balance of the transaction.
  - From label: Use a percentage from the transaction’s label using regex.
- Amount: Enter the amount to be used on the journal item. This field will be either a
  fixed amount, percentage amount, or regex depending on the Account Type.
- Taxes: Select a tax, if any, to set on the journal item. This field is hidden behind
  the  (settings adjust) icon by default.
- Analytic: Select an analytic distribution, if any, to set on the journal item.
- Label: Enter a label, if any, to set on the journal item.

> **Note:**
>
> - While neither the Partner nor Account fields are mandatory, at least
>   one of the two must be set for the reconciliation model to work correctly.
> - The reconciliation model can be used for [partner mapping]
>   if the Counterpart Items include a Partner but no Account.

## Default reconciliation models

In Odoo, different models are available by default depending on the company’s [fiscal
localization](../../fiscal_localizations.html). These can be updated if needed. The following
reconciliation models exist across most fiscal localizations.

### Internal Transfers

The Internal Transfers reconciliation model is used for making [internal transfers](internal_transfers.html) from one bank or cash account to another by moving the entire transaction’s
balance to a liquidity or internal transfer account. To fully transfer the amount from one account
to another, this reconciliation model must be used on both the incoming journal’s transaction and
the outgoing journal’s transaction.

> **Note:**
>
> [Internal transfers](internal_transfers.html)

### Bank Fees

The Bank Fees reconciliation model generates a counterpart item that moves the remaining
balance of a transaction to a bank fees account (that varies by [fiscal localization](../../fiscal_localizations.html)) and includes “Bank Fees” in the Label of the new item
that it creates. This reconciliation model is only applicable to transactions whose label contains
“Bank Fees” due to its [matching conditions].

> **Tip:**
>
> An outgoing bank transaction for $103 is partially matched with a vendor bill for $100, leaving
> $3 of the transaction still unreconciled. Use the Bank Fees reconciliation model to
> create a new counterpart item for $3 and reconcile it with the remaining $3 of the bank
> transaction.

### Cash Discount

The Cash Discount reconciliation model generates a counterpart item that moves the
remaining balance of a transaction to a cash discount account (that varies by [fiscal
localization](../../fiscal_localizations.html)) and includes “Cash Discount” in the Label of
the new item that it creates.

> **Note:**
>
> [Cash discounts and tax reduction](../customer_invoices/cash_discounts.html)

## Partner mapping

Partner mapping allows you to establish rules for automatically matching transactions to the correct
partner account, saving time and reducing the risk of errors that can occur during manual
reconciliation. For example, you can create a partner mapping rule for incoming payments with
specific reference numbers or keywords in the transaction description. When an incoming payment
meets these criteria, Odoo automatically maps it to the corresponding customer’s account.

To create a partner mapping rule, configure any [matching conditions], such as a specific transaction label, and then configure the
Partner and any other relevant fields in the [Counterpart Items] tab. Setting an Account is not mandatory for
partner mapping.

---

# Internal transfers

Internal money transfers can be handled in Odoo. At least two bank or cash accounts are needed to
make internal transfers.

> **Note:**
>
> [How to add an additional bank account](../bank.html#accounting-bank-create)

## Configuration

An internal transfer account is automatically created on your database based on your company’s
[localization](../../fiscal_localizations.html) and depending on your country’s legislation. To
modify the default Internal Transfer account, go to Accounting ‣
Configuration ‣ Settings and scroll down to the Default Accounts section.

## Register an internal transfer from one bank to another

When money is transferred from one bank or cash account to another, that amount appears as two
transactions on the corresponding journals, whether the transactions are created manually, via
import, or via [bank synchronization](bank_synchronization.html). When reconciling the transaction,
select the Internal Transfers [reconciliation model](reconciliation_models.html)
button. This reconciliation model button writes the transaction off to the Internal
Transfer account.

> **Warning:**
>
> Remember to reconcile the transaction for both the outgoing transaction on the journal that sends
> the payment and the incoming transaction on the journal that receives the payment.

> **Tip:**
>
> Take, for example, a transfer of $1000 from Bank A to Bank B:
>
> - Bank journal (Bank A)
>
>   | **Account** | **Debit** | **Credit** |
>   | --- | --- | --- |
>   | Bank A account |  | $1,000 |
>   | **Internal transfer account** | **$1,000** |  |
> - Bank journal (Bank B)
>
>   | **Account** | **Debit** | **Credit** |
>   | --- | --- | --- |
>   | Bank B account | $1,000 |  |
>   | **Internal transfer account** |  | **$1,000** |

> **Note:**
>
> - [Bank reconciliation](reconciliation.html)
> - [Reconciliation models](reconciliation_models.html)

---

# Manage a bank account in a foreign currency

In Odoo, every transaction is recorded in the default currency of the company, and reports are all
based on that default currency. When you have a bank account in a foreign currency, for every
transaction, Odoo stores two values:

- The debit/credit in the currency of the *company*;
- The debit/credit in the currency of the *bank account*.

Currency rates are updated automatically using the web services of a banking institution. By
default, Odoo uses the European Central Bank’s web services but other options are available.

## Configuration

### Activate multi-currencies

To work with multiple currencies, go to Accounting ‣ Configuration ‣ Settings
‣ Currencies and tick Multi-Currencies. Under Post Exchange difference
entries in:, provide a Journal, a Gain Account, a Loss Account,
and then click on Save.

### Configure currencies

Once Odoo is configured to support multiple currencies, they are all created by default, but not
necessarily active. To activate the new currencies, click on Activate Other Currencies
under the Multi-Currencies setting or go to Accounting ‣ Configuration
‣ Accounting: Currencies.

When the currencies are activated, you can choose to **automate** the currency rate update, or leave
it on **manual**. To configure the rate update, go back to Accounting ‣
Configuration ‣ Settings ‣ Currencies, check Automatic Currency Rates, set
Interval to your desired frequency, and then click on Save. You also have
the option to choose the Service you wish to obtain currency rates from.

Click on the Update now button (🗘) besides the Next Run field to update
the currency rates manually.

### Create a new bank account

In the accounting application, go to Accounting ‣ Configuration ‣ Journals and
create a new one. Enter a Journal Name and set the Type to `Bank`. In the
Journal Entries tab, enter a **short code**, a **currency**, and then finally click on
the Bank Account field to create a new account. In the pop-up window of the account
creation, enter a name, a code (ex.: 550007), set its type to `Bank and Cash`, set a currency type,
and save. When you are back on the **journal**, click on the Account Number field, and
in the pop-up window, fill out the Account Number, Bank of your account, and
save.

![Example of a created bank journal.](../../../../_images/foreign-journal.png)

Upon creation of the journal, Odoo automatically links the bank account to the journal. It can be
found under Accounting ‣ Configuration ‣ Accounting: Chart of Accounts.

## Vendor bill in a foreign currency

To pay a bill in a foreign currency, simply select the currency next to the Journal
field and register the payment. Odoo automatically creates and posts the foreign **exchange gain or
loss** as a new journal entry.

![How to set a bill currency.](../../../../_images/foreign-bill-currency.png)
> **Note:**
>
> Note that you can pay a foreign bill with another currency. In that case, Odoo automatically
> converts between the two currencies.

## Unrealized Currency Gains/Losses Report

This report gives an overview of all unrealized amounts in a foreign currency on your balance sheet,
and allows you to adjust an entry or manually set an exchange rate. To access this report, go to
Reporting ‣ Management: Unrealized Currency Gains/Losses. From here, you have
access to all open entries in your **balance sheet**.

![View of the Unrealized Gains/Losses journal.](../../../../_images/foreign-gains-losses.png)

If you wish to use a different currency rate than the one set in Accounting ‣
Configuration ‣ Settings ‣ Currencies, click the Exchange Rates button and change
the rate of the foreign currencies in the report.

![Menu to manually change exchange rates.](../../../../_images/foreign-exchange-rates.png)

When manually changing **exchange rates**, a yellow banner appears allowing you to reset back to
Odoo’s rate. To do so, simply click on Reset to Odoo’s Rate.

![Banner to reset back to Odoo's rates.](../../../../_images/foreign-reset-rates.png)

In order to update your **balance sheet** with the amount of the adjustment column,
click on the Adjustment Entry button. In the pop-up window, select a
Journal, Expense Account and Income Account to calculate and
process the **unrealized gains and losses**.

You can set the date of the report in the Date field. Odoo automatically reverses the
booking entry to the date set in Reversal Date.

Once posted, the adjustment column should indicate `0.00`, meaning all **unrealized
gains/losses** have been adjusted.

![Unrealized Currency Gains/Losses report once adjusted.](../../../../_images/foreign-adjustment.png)

---

# Loans management

Odoo’s loan management gives a comprehensive list of all loans undertaken by your company in order
to maintain a holistic and forecasted view of upcoming due dates (e.g., cash forecast). Set up
amortization schedules—or import them—and let Odoo automatically handle monthly interest and
principal adjustments so that your financial reports are always accurate with minimal effort.

## Create a new loan

Create a new loan by going to Accounting ‣ Accounting ‣ Loans. When creating a
new loan, there are three options for how to create amortization schedules:

- importing it from a supported file;
- calculating it from multiple input values (e.g., the Amount Borrowed, the
  Duration, etc.) using the Compute button;
- manually filling in the lines of the schedule.

In each case, three different fields are required for each line of the amortization schedule: the
Date, the Principal, and the Interest.

The Amount Borrowed, Interest, and Duration fields will be red
if the sum of the lines does not match the total of the amortization schedule lines.

## Loan entries mechanism

When the amount borrowed is credited to a bank account, it should be transferred to a long-term
account (defined in the Loan Settings tab). Then, upon the validation of the loan, Odoo
creates the necessary journal entries so that there is always a holistic and forecasted view of
upcoming due dates. The entire process is completely automated with a long-term and short-term
principal reclassification mechanism.

For each line of the amortization schedule, Odoo creates the following entries:

A payment entry on the same date that
:   - debits the principal amount to the long-term account;
    - debits the interest amount to the expense account;
    - credits the payment amount to the short-term account: this is the amount that will be
      withdrawn by the bank.

A reclassification entry on the same date that
:   - debits the sum of the principal amounts of the next 12 months to the long-term account;
    - credits the sum of the principal amounts of the next 12 months to the short-term account.

A reversed entry of the reclassification entry on *the next day* that simply reverses the previous
one.

With this mechanism, month after month, the short-term account is always up to date with the
current short-term due amounts.

## Closing a loan

By default, a loan will be closed whenever its last payment entry is posted. However, it can also
be manually closed (e.g., because it is being paid off early) by clicking on the Close
button. A wizard will appear asking from which date the loan should be closed. All draft entries
after this date will be deleted too.

A loan can also be cancelled. In that case, all entries will be deleted even if they were already
posted.

## Loans Analysis Report

By going to Accounting ‣ Review ‣ Loans Analysis, you can access a
report with a pivot view of your ongoing loans. By default, the report shows the principal,
interest, and total payment for each year for the duration of the loan.

---

# Reporting

Odoo includes **generic** and **dynamic** reports available for all countries, regardless of the
[localization package](../fiscal_localizations.html) installed:

- [Balance Sheet]
- [Profit and Loss]
- [Executive Summary]
- [General Ledger]
- [Aged Receivable]
- [Aged Payable]
- [Cash Flow Statement]
- [Tax Report]

To expand the lines of a report and view its details, click the
(right arrow) on the left. Then click the  (down arrow)
to the right of the account, journal entry, payment, invoice, etc. to Annotate and view
the details.

![Annotate reports.](../../../_images/reporting-annotate.png)

To export reports in PDF or XLSX format, click PDF at the top or click the
 (down arrow) icon next to the PDF button and
select XLSX.

To compare values across periods, click the Comparison menu and select the periods you
want to compare.

![Comparison menu to compare time periods.](../../../_images/reporting-comparison.png)

## Balance Sheet

The Balance Sheet shows a snapshot of your organization’s assets, liabilities, and
equity at a particular date.

## Profit and Loss

The Profit and Loss report (or **Income Statement**) shows your company’s net income by
deducting expenses from revenue for the reporting period.

## Executive Summary

The Executive Summary provides an overview of all the important figures for overseeing
your company’s performance.

It includes the following items:

- Performance:
  :   - Gross profit margin:
        :   The contribution of all sales your business makes **minus** any direct costs needed to
            make those sales (labor, materials, etc.).
      - Net profit margin:
        :   The contribution of all sales made by your business **minus** any direct costs needed to
            make those sales *and* fixed overheads your company has (electricity, rent, taxes
            to be paid as a result of those sales, etc.).
      - Return on investment (per annum):
        :   The ratio of the net profit to the amount of assets the company used to make those profits.
- Position:
  :   - Average debtors days:
        :   The average number of days it takes your customers to (fully) pay you across all your
            customer invoices.
      - Average creditors days:
        :   The average number of days it takes you to (fully) pay your suppliers across all your bills.
      - Short-term cash forecast:
        :   How much cash is expected in or out of your business in the next month, i.e., the balance of
            your **Sales account** for the month **minus** the balance of your **Purchases account** for
            the month.
      - Current assets to liabilities:
        :   Also referred to as the **current ratio**, this is the ratio of current assets (assets
            that could be turned into cash within a year) to the current liabilities (liabilities
            that will be due in the next year). It is typically used to measure a company’s ability to
            service its debt.

## General Ledger

The General Ledger report shows all transactions from all accounts for a selected date
range. The initial summary report shows the totals for each account. To expand an account and view
its details, click the  (right arrow) on the left.
This report is useful for reviewing each transaction that occurred during a specific period.

## Aged Receivable

The Aged Receivable report shows the sales invoices awaiting payment during a selected
month and several months prior.

## Aged Payable

The Aged Payable report displays information on individual bills, credit notes, and
overpayments you owe and how long these have gone unpaid.

## Cash Flow Statement

The Cash Flow Statement shows how changes in balance sheet accounts and income affect
cash and cash equivalents and breaks the analysis down to operating, investing, and financing
activities.

## Tax Report

The Tax Report shows the NET and TAX amounts for all the
taxes grouped by type (Sales/Purchases).

---

# Tax return (VAT report)

Companies with a registered VAT number are required to submit a tax return
monthly or quarterly, depending on their turnover and the applicable regulatory requirements. A tax
return - or VAT report - provides the tax authorities with information about the taxable
transactions made by the company. The **output tax** is charged on the sale of goods and services,
while the **input tax** refers to the tax included in the price of purchased goods or services.
Based on these values, the company can calculate the tax amount they must pay or be refunded.

> **Note:**
>
> - [European Commission documentation on VAT](https://ec.europa.eu/taxation_customs/business/vat/what-is-vat_en).
> - [Taxes](../taxes.html)
> - [Get started](../get_started.html)
> - [Fiscal localizations](../../fiscal_localizations.html)

## Configuration

### Tax return periodicity

The configuration of the tax return periodicity allows Odoo to compute tax returns correctly and
automatically send reminders to make sure that deadlines are met.

To do so, go to Accounting ‣ Configuration ‣ Settings, navigate to the
Tax Return Periodicity section, and update the following fields, if needed:

- Periodicity: Define the tax return periodicity.
- Deadline: Define when Odoo should send reminders to submit the tax return.
- Journal: Update the journal where the tax return is recorded, if needed.

> **Note:**
>
> This information is usually configured during the [app’s initial setup](../get_started.html).

### Tax grids

Odoo generates tax reports based on the Tax Grids settings configured for each tax. All
recorded transactions must apply the correct tax rates to ensure accurate reporting.

Tax Grids are displayed in the Journal Items tab of any invoice or bill.

![example of tax grids used on an invoice](../../../../_images/tax-return-grids.png)

To configure tax grids for taxes, go to Accounting ‣ Configuration ‣ Taxes,
open the relevant tax, and edit the tax settings and the tax grids used to record invoices or
refunds.

> **Note:**
>
> Taxes and reports are usually pre-configured according to the country selected for the
> [company](../../../general/companies.html).

### Tax returns journal

On the Accounting dashboard, complete the following actions displayed in the Tax Returns
journal before creating tax returns:

- Set Company Data: [Configure the company details](../../../general/companies.html#general-companies-company).
- Set Periods: In the Accounting Periods window, fill in the
  Opening date, Fiscal Year End, and update the Periodicity if
  needed.
- Review Chart of Accounts

## Close a tax period

### Tax return lock date

Setting a tax lock date prevents changes that could impact VAT-related journal entries. Locking the
period before processing the Closing Journal Entry helps ensure the accuracy of the
final report and reduces the risk of tax errors.

To view or edit the current Lock Tax Return date, go to Accounting ‣
Accounting ‣ Lock Dates.

> **Note:**
>
> Any new transaction whose accounting date is before the Lock Tax Return date has its
> tax values moved to the next open tax period, preventing any changes to a report after its period
> is closed.

### Tax return

On the Accounting Dashboard, the Tax Returns journal displays automatic reminders to
avoid missing important tasks and deadlines.

After completing all [configurations] and posting all
tax-related transactions for the reporting period, click Tax Returns on the
Tax Returns journal from the Accounting dashboard. Alternatively, go to
Accounting ‣ Accounting ‣ Tax Returns.

The Tax Return view displays a chronological list of all pending [tax returns (VAT
report)] and [advance payments] (based on the [fiscal localization](../../fiscal_localizations.html)). Each item on the list includes:

- A period (month or quarter).
- A deadline date.
- The related company and [branch(es)](../../../general/companies.html#general-branches), if applicable.
- Action steps, such as [Review], [Submit], and [Pay], which turn green when completed.
- Action buttons: These are displayed as primary (purple) and secondary (grey) buttons to indicate
  their priority.
- A  (vertical ellipsis) menu for additional options.

![Tax return tool overview](../../../../_images/tax-return-view.png)
> **Note:**
>
> - Before the tax return is reviewed, the number of Pending or Passed tax
>   validation checks is displayed in red or green, respectively.
> - If the Deadline date has passed, it appears in red.

> **Note:**
>
> To export all tax returns from the selected period, click the  (gear)
> icon, then click  Export All to download the tax returns XLSX.

#### VAT report

Each pending tax return (VAT report) follows these steps: [review], [submit], and [pay].

To access a tax return, click the local VAT report button (e.g., VAT Return (BE) or
Tax Report (US), depending on the [fiscal localization](../../fiscal_localizations.html)) or the Generic Tax report button on the tax return line
in the Tax Return view.

> **Note:**
>
> - Click PDF or XLSX to generate a PDF or XLSX file, respectively.
> - Click the  (gear) icon and Copy to Documents to save the
>   report to the [Documents](../../../productivity/documents.html) app. Select the format to
>   Export to, the Documents Name, the Folder to store it in,
>   and add any Tags. Then click Export.

To create a new return, click New, select the relevant Return Type, and
fill in the required Dates. Then, click Generate Return. The following
returns can be generated:

- Annual Closing: Corporate Tax
- VAT (return)/Tax
- VAT Listing (Belgium-specific)
- EC Sales List (EU-specific)
- Advance Payment (Belgium-specific)
- Intrastat (EU-specific)

##### Review

To start the review of a tax return, click on the relevant tax return line:

- If all automatic tax validation checks have passed, click Validate to complete the
  Review step. The [Lock Tax Return] date is
  automatically updated, and the closing journal entry is posted in the Tax Returns
  journal. The tax return can then be [submitted].
- If any automatic tax validation checks are pending, the Tax Checks view displays the
  following, depending on the [fiscal localization](../../fiscal_localizations.html):

  - Bank Matching: This check is used to identify any missing bills; it is optional for
    VAT reports.
  - Bill attachments: Bills must have attached documents as proof in case of an audit.
  - Company data: Missing information (e.g., VAT number or country) can lead to errors
    in tax reports or exemptions.
  - Draft entries: Any draft invoices and bills within the corresponding period must be
    reviewed and posted, or assigned a different accounting date.
  - No negative amount in VAT report: Some countries only allow positive values in tax
    returns, as a negative amount could indicate misconfigurations.
  - Taxes and countries matching: Taxes applied on invoices and bills must match the
    customer’s country.

  Each check card is either highlighted in green (Reviewed or Supervised), red (Anomaly) or
  grey (To review). If a check fails, there are two options:

  - Click on the failed check’s card to fix the issue.
  - Click Anomaly and select Reviewed or Supervised to pass the
    check without fixing the issue.

  Once all checks have passed, click Validate. Then, depending on the [fiscal
  localization](../../fiscal_localizations.html), click Lock in the Lock window.

  On validating the tax return, the [Lock Tax Return] date
  is automatically updated, and the closing journal entry is posted in the Tax Returns
  journal.

> **Note:**
>
> - To add customized checks, activate [developer mode](../../../general/developer_mode.html#developer-mode), and go to
>   Accounting ‣ Configuration ‣ Check. Then, click New and
>   complete the necessary fields.
> - All check status changes are logged in the chatter.

> **Note:**
>
> If the Lock Tax Return date is not locked before reviewing the tax return, the
> fiscal period is automatically locked on the same date as the accounting date of the closing
> journal entry. While this feature helps prevent certain fiscal errors, it is recommended to set
> the [Lock Tax Return date] manually beforehand.

> **Warning:**
>
> After the tax report for a period has been posted, that period is locked to prevent new
> VAT-related journal entries from being created. Corrections to customer invoices or vendor bills
> must be recorded in the following period.

##### Submit

Once a tax return has completed the [Review] step,
proceed as follows:

1. In the Tax Return view, click the local VAT report button (e.g., VAT
   Return (BE) or Tax Report (US), depending on the [fiscal localization](../../fiscal_localizations.html)) or the Generic Tax report button on the relevant tax
   return line to preview the tax return report.
2. Once the tax return report has been verified, go back to the Tax Return view and
   click Submit.
3. If a Submission Instructions pop-up window appears, follow the local
   Instructions, and click Mark as Submitted or [Mark
   Paid].

The submitted tax return contains all the values tax authorities need, and the amount to be paid or
refunded.

> **Note:**
>
> - To display all posted closing journal entries, click the Tax Returns journal in
>   the Accounting dashboard.
> - To display the tax return entry posted, click the  (vertical
>   ellipsis) icon and select View Entry. The following options are available if
>   needed:
>
>   - Reverse Entry
>   - Reset to Draft: The Lock Tax Return date must be manually removed
>     using a [lock date exception](year_end.html#accounting-year-end-lock-date-exception) to reset a tax
>     return entry to draft.

##### Pay

Once a tax return is submitted, a Payment window appears if a tax payment is required.
It displays all necessary payment details to complete the transaction, including a QR code
for the banking app, if available for the country’s [fiscal localization](../../fiscal_localizations.html) package. There are three options:

- Click Mark Paid after completing the payment: the corresponding tax return line
  disappears from the Tax Return view.
- Click Send to email all payment information. Once sent, the tax return completes the
  Pay step, and its corresponding line disappears from the Tax Return view.
- Click Discard: the corresponding tax return line remains visible in the
  Tax Return view, indicating the amount due. Click the
  (paperclip) icon to access the PDF and XLSX files of the submitted tax return.

  ![view when tax return is submitted](../../../../_images/tax-return-submitted.png)

#### Advance tax payments

> **Note:**
>
> Advance tax payments are specific to local [fiscal localizations](../../fiscal_localizations.html) and the requirements of certain countries’ tax systems.

In the Tax Return view, click Pay on the relevant advance tax payment line
that needs to be processed.

In the Advance Payment window, follow the local recommendations, fill in the required
local fields, and use the provided payment details to finalize the transaction. Two options are
available:

- Click Mark Paid once the payment is processed: The corresponding advance tax payment
  line disappears from the Tax Return view.
- Click Send to email all payment information. Once sent, the advance tax payment
  completes the Pay step, and its corresponding line disappears from the Tax
  Return view.
- Click Discard: The corresponding advance tax payment line remains visible in the
  Tax Return view.

> **Note:**
>
> To mark a tax payment that has already been completed, click the
> (vertical ellipsis) icon and select Mark as Completed.

---

# Tax carryover

When performing tax reports, the **tax carryover** feature allows carrying amounts from one period
to another without creating new entries.

It has been created to meet the legal requirements of specific locations, where amounts must be
transferred from period to period (for example, because the total of the line is negative).

The feature is activated by default in countries where it is required, such as Belgium, France, and
Italy. There is no specific configuration required.

Let’s take an example of a Belgian company that created a credit note of 100 for one of their
customers. The due tax is 21%.

![Illustration with a credit note](../../../../_images/belgian-example.png)

In this case, as per local regulation, grid 81 of the tax report may contain a negative amount. But
it must be declared to the government as zero, and the negative amount should be carried over to the
next period.

If we go to Accounting app ‣ Reporting ‣ Tax Report, a pop-up on line 81
explains that the amount will be carried over in the next period.

![pop-up message stating the amount will be carried over to the next period](../../../../_images/pop-up.png)

At the time of the tax closing period, the tax report shows that the amount was carried over from
the previous period. It also indicates the amount that will be carried over to this line in the next
period based on the existing transactions and the carryover from the previous period.

![Illustration of the tax return](../../../../_images/tax-return.png)

---

# Analytic accounting

Analytic accounting helps track costs and revenues and analyze a project’s or service’s
profitability. When creating journal entries, costs can be [distributed] across one or more analytic accounts.

To activate this feature, go to Accounting ‣ Configuration ‣ Settings and
enable Analytic Accounting in the Analytics section.

> **Note:**
>
> [Analytic budget](budget.html)

## Analytic accounts

Analytic accounts give an overview of costs and revenue.

To access analytic accounts, go to Accounting ‣ Configuration ‣ Analytic
Accounts. To create a new analytic account, click New and fill in the following
information:

- Analytic Account: Assign the name of the analytic account.
- Customer: Select the customer linked to the project, if applicable.
- Reference: Include a reference to make the account easier to find if needed.
- Plan: Link the Analytic Account to an [analytic plan].
- Company: In a [multi-company](../../../general/companies/multi_company.html)
  environment, select the company using the analytic account. To make the analytic account
  accessible to all companies, leave the field empty.
- Currency: Update the currency of the analytic account if needed.

Then, the [budget](budget.html) information can be filled in.

## Analytic plans

Analytic plans group [analytic accounts],
allowing the company to analyze its accounting, such as tracking costs and revenues by project or
department.

To access analytic plans, go to Accounting ‣ Configuration ‣ Analytic Plans.
Click New to create a new plan, add a name, and fill in the following information:

- Parent: Link the plan to another analytic plan if a hierarchy between plans must be
  built.
- Default Applicability: Define how the plan is applied when creating a new journal
  entry:

  - Optional: Adding the analytic plan is not mandatory.
  - Mandatory: The entry cannot be confirmed if no analytic account is selected.
  - Unavailable: The plan is not available.
- Color: Set a color for the tag related to this specific plan.

To fine-tune a plan’s applicability, create a new line in the Applicability tab and set
the following fields:

- Domain: Choose the accounting documents to which the plan applies.
- Financial Accounts Prefixes: Enter the prefix(es) of the account(s) to which the plan
  applies.
- Product Category: Choose the product category to which the plan applies.
- Applicability: Define how the plan is applied when creating a new journal entry. The
  applicability set here always overrides the default applicability.
- Company: In a [multi-company](../../../general/companies/multi_company.html)
  environment, select the company using the plan. To make the analytic plan accessible to all
  companies, leave the field empty.

Two smart buttons are available:

- Subplans: To have a more complex analytic structure. Click the smart button, then
  click New to add a subplan. This creates a parent-child relationship between the two
  plans, and the Parent field of the subplan is automatically populated with the
  original plan.
- Analytic Accounts: To access the [analytic accounts] linked to the plan.

> **Note:**
>
> Each analytic plan must have at least one analytic account.

## Analytic distribution

The distribution of costs in one or more analytic accounts can be set in each [invoice/bill] or [en masse].

> **Note:**
>
> The analytic distribution is prefilled based on the applicability and the [analytic
> distribution models].

### Analytic distribution on invoices or bills

To add analytic distribution, click the Analytic Distribution column when creating an
[invoice](../customer_invoices.html#accounting-invoice-creation) or [bill](../vendor_bills.html#accounting-vendor-bills-creation).

> **Note:**
>
> The Analytic Distribution field is mandatory only if the [analytic plan] has been set as Mandatory in either
> the Default Applicability field on an analytic plan or the Applicability
> field on an analytic plan line.

In the Analytic window, select the desired Analytic Accounts in the
different Analytic Plans displayed in columns. Then, split the costs between the
accounts by modifying the percentage.

![create a distribution template](../../../../_images/analytic-distribution.png)

### Analytic distribution en masse

To mass-edit analytic accounts in several entries simultaneously, go to Accounting
‣ Accounting ‣ Journal items, and select the ones that need to be updated. Click the
Analytic Distribution column and add the required distribution in the
Analytic column, then click the  (cross) and
Update. The analytic distribution is then added to the selected journal items.

### Analytic distribution models

Analytic distribution models automatically apply a specific distribution based on defined criteria.

To create a new analytic distribution model, go to Accounting ‣ Configuration ‣
Analytic Distribution Models, click New, and set the conditions the model has to meet
to apply automatically:

> **Note:**
>
> - All specified conditions of an analytic distribution model must be met for the model to be
>   applied. To apply an analytic distribution model based on individual conditions, create
>   separate analytic distribution models for each condition.
> - Analytic distribution models can be combined and sequenced, allowing distribution across
>   multiple models if linked to different
>   [analytic plans]. To adjust the order,
>   drag and drop the models using the  (draggable) icon.

- Accounts Prefixes: Apply the distribution model only to journal items involving
  accounts that begin with specific prefixes.
- Partner: Apply the distribution model only to journal items involving a specific
  partner.
- Product: Apply the distribution model only to journal items involving a specific
  product.
- Company: In a [multi-company](../../../general/companies/multi_company.html)
  environment, apply the distribution model only to journal items involving a specific company. To
  apply it across all companies, leave the field empty.
- Analytic Distribution: [Analytic distribution] that will be applied when the above
  conditions are met.

> **Tip:**
>
> Any time a journal item is posted to the Utilities (601000) account, it should be
> automatically distributed in the Departments analytic plan as follows:
>
> - 60% to the Manufacturing analytic account
> - 30% to the Marketing analytic account
> - 10% to the Admin analytic account
>
> To automate this distribution, the Accounts Prefix can be set to `601`, as
> Utilities (601000) is the only account in the chart of accounts that begins with
> `601`.
>
> If additional accounts such as Electricity (601100) or Gas (601200) are
> available in the chart of accounts, the distribution will also apply to both since they share the
> same prefix.

To define more criteria, use the  (adjust settings) icon to
reveal more columns or click View on an individual analytic distribution model.

- Partner Category: Apply this distribution model only to journal items involving a
  partner in a specific category.
- Product Category: Apply this distribution model to journal items involving a product
  in a specific category.

> **Note:**
>
> Alternatively, it is possible to create an analytic distribution model from the
> Analytic window by clicking New Model:
>
> - either when creating an invoice/bill and filling in the [analytic distribution];
> - or when [mass-editing analytic accounts] in several entries simultaneously.

---

# Budgets

[Analytic budgets] track specific activities and projects
using analytic accounts, helping businesses make informed decisions about specific departments,
projects, or other groups of transactions. In contrast, [financial budgets] are tied to the general ledger accounts that appear on the profit
and loss and focus on the company’s overall economic position.

## Analytic budgets

Analytic budgets allow for allocating and tracking income and expenses in detail, breaking down
costs and revenues by specific projects, departments, or groups of transactions. Analytic budgets
can be applied across various departments or projects to measure profitability and performance. Odoo
manages analytic budgets using [analytic accounting](analytic_accounting.html).

To activate the option for creating analytic budgets, go to Accounting ‣
Configuration ‣ Settings, and enable Budget Management in the Analytics
section.

> **Warning:**
>
> Odoo structures budgets using [plans](analytic_accounting.html#accounting-analytic-accounting-analytic-plans) and
> [accounts](analytic_accounting.html#accounting-analytic-accounting-analytic-accounts), which must be configured
> *before* creating a budget.

### Set an analytic budget

To create a new budget, go to Accounting ‣ Accounting ‣ Analytic Budgets and
click New. Make sure the following fields are appropriately completed: Budget
Name, Period, and Budget Type.

Click Add a line in the Budget Lines tab to structure the budget with the
[analytic plans](analytic_accounting.html#accounting-analytic-accounting-analytic-plans) and [accounts](analytic_accounting.html#accounting-analytic-accounting-analytic-accounts) previously created. While the [analytic
plans](analytic_accounting.html#accounting-analytic-accounting-analytic-plans) correspond to the column names, select the
[analytic accounts](analytic_accounting.html#accounting-analytic-accounting-analytic-accounts) to define the budget
lines and set the amounts for each in the Budgeted column. Once all the budget lines are
settled, click Open. If changes need to be made once the budget’s status is
Open, there are two options:

- Reset to Draft: To overwrite the data, then reopen the budget.
- Revise: A new budget will be created. Once it is Open, a Rev
  reference is added to the Budget Name. The original budget is then
  Revised.

### Check an analytic budget

Once the budget is Open, two additional columns are available: Committed and
Achieved. These columns’ amounts are automatically calculated based on the related
[analytic distribution](analytic_accounting.html#accounting-analytic-accounting-analytic-distribution) of journal
items. When the [analytic distribution](analytic_accounting.html#accounting-analytic-accounting-analytic-distribution)
of a journal item within the budget’s period is updated, the budget’s columns for the analytic
account(s) selected in the distribution are automatically updated. The Achieved amount
reflects the current result according to the items of confirmed journal entries for the associated
[analytic account](analytic_accounting.html#accounting-analytic-accounting-analytic-accounts). In contrast, the
Committed amount displays the full value of the Achieved amount, plus any
confirmed purchase orders that have not yet been billed.

> **Note:**
>
> - When a line in a request for quotation or purchase order includes an analytic distribution, a
>   Budget smart button appears, providing a link to the [budget report] for more details.
> - For Open budgets, if a request for quotation or a purchase order is created using
>   the associated analytic distribution and exceeds the allocated budget amount, the corresponding
>   purchase order line is highlighted in red.

To reveal the Theoretical amount or percentage, use the
(adjust settings) icon in the Budget Lines’ header. The
Theoretical amount represents the amount of money that could theoretically have been
spent or should have been received based on the current date relative to the start/end dates. Click
Details to open a filtered view of the [budget report] related to that specific budget line.

![open budget with committed, achieved, and theoretical amounts](../../../../_images/budget.png)
> **Note:**
>
> Deleting a budget is only allowed in the Draft and Cancelled stages.

To view the budget lines of one or multiple budgets directly from the Budgets list view,
select the budget(s) and click Budget Lines.

### Generate periodic budgets

To create periodic budgets (monthly, quarterly, and yearly) for the selected Analytic
Plans, click Generate. A new budget is created for each Period between the
start and end dates:

- If a single analytic plan is selected, each budget includes a line for each account in that
  analytic plan.
- If multiple analytic plans are selected, each budget includes a line for each account/analytic
  plan combination.

To generate periodic budgets, follow these steps:

1. In the Budgets list view, click Generate.
2. In the Generate Budget window, set the dates and select the Period and
   the Analytic Plans.

   ![all the options to generate periodical budgets](../../../../_images/generate-budgets.png)
3. Click Split to create the periodic budgets.
4. Click Budgets in the top-left corner to return to the Budgets list view.
5. One by one, click on the different periodic budgets with the Draft status to open
   them and set the amounts in the Budgeted column for each analytic account linked to
   the chosen analytic plans.
6. Click Open for each periodic budget.

### Reporting

To perform various reporting actions, go to Accounting ‣ Reporting ‣
Budget Report, then:

- Track, analyze, and compare budget data.
- Filter and group data using the  (plus-square) or
   (minus-square) icon.
- Drill down into the report to see more details on the actual amounts and transactions.
- Export the data for further analysis or reporting needs.

## Financial budgets

Financial budgets are structured around specific income and expense accounts and transactions for
official financial reporting and compliance purposes.

> **Note:**
>
> Financial budgets are available on the [Profit and Loss](../reporting.html#accounting-reporting-profit-and-loss) report.

### Set a financial budget

To create a new financial budget, follow these steps:

1. Go to Accounting ‣ Reporting ‣ Profit and Loss to open the
   [Profit and Loss](../reporting.html#accounting-reporting-profit-and-loss) report.
2. Click the  (calendar) button to use the date selector and choose a
   period.
3. Click the  Budget button and name the budget. A new column
   labeled with the budget name will appear next to the Balance column.
4. Assign amounts to each account requiring analysis.
5. A new % column will appear to the right of the new budget column, indicating the
   current status.

Different financial budgets can be created using these steps for comparison purposes.

> **Note:**
>
> The date selector enables the division of periods and navigation between periods, automatically
> updating the amounts accordingly.

---

# Intrastat

Intrastat is the data collection and statistics production system for goods traded among EU member
states. It collects data on:

- Commercial transactions of goods for use, consumption, investment, or resale with ownership
  transfer;
- Goods movements without transfer of ownership (e.g., stock relocations or moves of goods
  before or after outsourced production or processing, and after maintenance or repair);
- Returns of goods.

> **Note:**
>
> Although the Intrastat system continues to be used, the term Intrastat is not used in the [latest
> legislation](http://data.europa.eu/eli/reg/2019/2152/2022-01-01), referring instead to
> *intra-Union trade in goods statistics*.

> **Note:**
>
> [Eurostat Statistics Explained - Glossary: Intrastat](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:Intrastat)

## General configuration

Enable the Intrastat report by going to Accounting ‣ Configuration ‣ Settings.
Under the Customer Invoices section, tick Intrastat and then
Save.

### Default transaction codes: invoice and refund

You can set a default [transaction code] for all newly created
invoice and refund transactions. Under Accounting ‣ Configuration ‣ Settings,
select a Default invoice transaction code and/or a Default refund transaction
code and then Save. The code will be set automatically on all respective invoice lines.

### Region code

The region code is **only used by Belgian companies**. Under Accounting ‣
Configuration ‣ Settings, select the Company Intrastat Region where the company is
located and then Save.

> **Note:**
>
> If your warehouses are located in more than one region, you can define the region code at the
> level of each warehouse instead. To do so, go to Inventory ‣ Configuration ‣
> Warehouses, select a warehouse, set its Intrastat region, and then Save.
>
> ![Adding the Intrastat region to a warehouse](../../../../_images/warehouse-region.png)

## Product configuration

All products must be properly configured to be included in the Intrastat report.

### Commodity code

Commodity codes are internationally recognized reference numbers used to classify goods depending on
their **nature**. Intrastat uses the [Combined Nomenclature](https://taxation-customs.ec.europa.eu/customs-4/calculation-customs-duties/customs-tariff/combined-nomenclature_en).

To add a commodity code, go to Accounting ‣ Customers ‣ Products and select a
product. Under the Accounting tab, set the product’s Commodity Code.

> **Note:**
>
> [National Bank of Belgium - Intrastat commodity codes](https://www.nbb.be/en/statistics/foreign-trade/nomenclature-and-codes)

### Quantity: weight and supplementary unit

Depending on the nature of the goods, it is necessary to specify either the product’s weight in
kilos (without packaging) or the product’s supplementary unit, such as square meter (`m2`), number
of items (`p/st`), liter (`l`), or gram (`g`).

To add a product’s weight or supplementary unit, go to Accounting ‣ Customers ‣
Products and select a product. Under the Accounting tab, depending on the commodity
code set, either fill in the product Weight or its Supplementary Units.

### Country of origin

To add the product’s country of origin, go to Accounting ‣ Customers ‣ Products
and select a product. Under the Accounting tab, set the Country of Origin.

## Invoices and bills configuration

Once products are properly configured, several settings must be configured on the invoices and bills
you create.

### Transaction code

Transaction codes are used to identify a transaction’s nature. [Default transaction codes] can be set for invoice and refund transactions.

To set a transaction code on an invoice line, create an invoice or a bill, click the columns
selection button, tick Intrastat, and use the newly-added Intrastat column
to select a transaction code.

![Adding the Intrastat column to an invoice or bill](../../../../_images/intrastat-column.png)
> **Note:**
>
> [National Bank of Belgium - Intrastat: Nature of transactions from January 2022](https://www.nbb.be/doc/dd/onegate/data/new_natures_of_transaction_2022_en.pdf)

### Partner country

The partner country represents the vendor’s country for bills and the customer’s country for
invoices. It is automatically filled in using the country set in the contact’s Country
field.

To edit the partner country manually, create an invoice or a bill, click the Other Info
tab, and select the Intrastat Country.

### Transport code

The transport code identifies the presumed **mode of transport** used to send the goods (arrival or
dispatch).

To add the transport code, create an invoice or a bill, go to the Other info tab,
and select the Intrastat Transport Mode.

### Value of the goods

The value of a good is the untaxed Subtotal (Price multiplied by
Quantity) of an invoice line.

## Partner configuration

Two fields from the partner’s contact form are used with Intrastat: VAT and
Country. The country can be [manually set] on the
invoice or bill.

## Generate the Intrastat report

Generate the report by going to Accounting ‣ Reporting ‣ Audit Reports:
Intrastat Report. It is automatically computed based on the [default configuration] and the information found on the [products], [invoices and bills], and [partners].

Export the report as a PDF, XLSX, or XML file to post it to your legal administration.

Each report line refers to a single invoice line and contains the following information:

- Invoice or bill reference number;
- System, which is a code automatically generated depending on whether the document is an invoice
  (dispatch) or a bill (arrival);
- [Country], which is the vendor’s country for arrivals and the
  customer’s country for dispatches;
- [Transaction Code];
- (If your company is located in Belgium) [Region Code];
- [Commodity Code];
- [Origin Country];
- [Partner VAT];
- [Transport Code];
- [Incoterm Code](../customer_invoices/incoterms.html);
- [Weight];
- [Supplementary Units]; and
- [Value], which is always expressed in euros even if the original invoice or
  bill used another currency.

---

# Data inalterability check report

Tax authorities in some countries require companies to **prove their posted accounting entries are
unaltered**, meaning that once an entry has been secured, it can no longer be changed.

To do so, Odoo creates a unique fingerprint for each secured entry thanks to the **SHA-256 algorithm**.
This fingerprint is called a hash. The hash is generated by taking an entry’s essential data
(the values of the `name`, `date`, `journal_id`, `company_id`, `debit`, `credit`, `account_id`, and
`partner_id` fields), concatenating it, and inputting it to the SHA-256 hash function, which then
outputs a fixed size (256-bit) string of characters. The hash function is deterministic (the
same input always creates the same output): any minor modification to the original data would
completely change the resulting hash. Consequently, the SHA-256 algorithm is often used, among
others, for data integrity verification purposes.

In addition, the previous entry’s hash is always added to the next entry to form a **hash chain**.
This is used to ensure a new entry is not added afterward between two secured entries, as doing so
would break the hash chain.

> **Note:**
>
> Hashes generated by the SHA-256 algorithm are theoretically not unique, as there is a finite
> number of possible values. However, this number is exceptionally high: 2²⁵⁶, which is a lot
> bigger than the number of atoms in the known universe. This is why hashes are considered unique
> in practice.

## Inalterability features

Inalterability features can be enabled by activating the [secure posted entries with hash] option on any journal or using the [secure entries wizard].

- Two indicators are added to the journal entry’s form view.
  They show whether the entry is secured or not.

  - A  or  (lock icon) next to the Posted state.
  - A Secured checkbox in the Other info tab.
- A Not Secured filter is available on journal entries and journal items’ list views.
  It can be used to find posted journal entries that are not secured yet.
- The option to open the [secure entries wizard] is displayed in the
  Accounting menu.

## Secure posted entries with hash

To activate the hashing function on a specific journal, go to Accounting ‣
Configuration ‣ Journals. Open a sales, purchase, or miscellaneous journal, go to the
Advanced Settings tab, and enable Secure Posted Entries with Hash.
Journals for which the feature is activated are called “restricted”.

To compute the hash of an entry, Odoo retrieves the predecessor entries of the chain (i.e., the
entries with the same sequence prefix) and hashes them in a continuous way from the last hashed
entry to the new entry to hash.

> **Warning:**
>
> Once you post an entry in a restricted journal, you cannot disable the feature anymore, nor edit
> any secured entry.

## Secure entries wizard

You can also use the Secure Entries Wizard to secure all journal entries,
in **all** journals, up to a specific date.

> **Note:**
>
> The wizard operates independently of the journal settings and journal types.

To open it, activate the [developer mode](../../../general/developer_mode.html#developer-mode), go to Accounting
‣ Accounting, and click on Secure Entries. If the [inalterability features] are activated, it is also visible outside the debug
mode.

To secure entries, select a date up to which all entries should be secured and press
Secure Entries.

> **Warning:**
>
> After securing the entries, you can no longer edit them.

> **Note:**
>
> It can happen that entries that are past the selected date are secured.
> This is possible since the hash chain corresponds to the sequence prefix,
> ordered by sequence number.

## Report download

To download the data inalterability check report, go to Accounting ‣ Configuration
‣ Settings ‣ Reporting and click on Download the Data Inalterability Check Report.

The report’s first section is an overview of all journal sequence prefixes containing hashed entries.
In the Restricted column, you can see whether or not a journal has the [secure
posted entries with hash] option (V) activated or not (X). The
Check column tells you whether all entries are correctly hashed.

![Configuration report for two journals](../../../../_images/journal-overview.png)

The second section gives a more detailed result of the data consistency check for each hashed
journal sequence prefix. You can view the first hashed entry and its corresponding hash,
as well as the last hashed entry and its corresponding hash.

![Data consistency check report for a journal](../../../../_images/data-consistency-check.png)

---

# Silverfin integration

[Silverfin](https://www.silverfin.com) is a third-party service provider that offers a cloud
platform for accountants.

Odoo and Silverfin provide an integration to automate the synchronization of data.

## Configuration

To configure this integration, you need to input the following data into your Silverfin account:

- user’s email address
- [Odoo API key]
- URL of the Odoo database
- name of your Odoo database

### Odoo API key

You can create Odoo external API keys either [for a single database]
(hosting: Odoo Online, On-premise, and Odoo.sh) or [for all databases managed by a single user] (hosting: Odoo Online).

> **Warning:**
>
> - These API keys are personal and provide full access to your user account. Store it securely.
> - You can copy the API key only at its creation. It is not possible to retrieve it later.
> - If you need it again, create a new API key (and delete the old one).

> **Note:**
>
> [External JSON-2 API](../../../../developer/reference/external_api.html)

#### Per database

To add an API key to a **single** database, connect to the database, enable the [developer
mode](../../../general/developer_mode.html#developer-mode), click on the user menu, and then My Profile /
Preferences. Under the Account Security tab, click on New API
Key, confirm your password, give a descriptive name to your new key, and copy the API key.

![creation of an Odoo external API key for a database](../../../../_images/api-key-db.png)
> **Note:**
>
> [API Keys](../../../../developer/reference/external_rpc_api.html#api-external-api-keys)

#### For all databases (fiduciaries)

To add an API key to **all** databases managed by a single user at the same time **(the easiest
method for fiduciaries)**, navigate to [Odoo’s website](https://www.odoo.com) and sign in with
your administrator account. Next, open [your account security settings in developer mode](https://www.odoo.com/my/security?debug=1), click on New API Key, confirm your
password, give a descriptive name to your new key, and copy the new API key.

> **Note:**
>
> Open the [database manager](https://www.odoo.com/my/databases) to view all databases that will
> be linked to the single API key.

![creation of an Odoo external API key for an Odoo user](../../../../_images/api-key-user.png)

---

# Custom reports

Odoo comes with a powerful and easy-to-use reporting framework. The engine allows you to create new
reports, such as tax reports, balance sheets, and income statements with specific groupings and
layouts.

> **Warning:**
>
> Activate the [developer mode](../../../general/developer_mode.html#developer-mode) to access the accounting report
> configuration.

To create a new report, go to Accounting ‣ Configuration ‣ Accounting Reports.
From here, create either a [root report] or a [variant].

> **Note:**
>
> - Consider saving modified reports as report variants to keep their root reports intact.
> - To access an existing report’s management interface from the report itself, click on the
>    (gears) icon.

## Root reports

Root reports can be regarded as generic, neutral accounting reports. They serve as models on which
local accounting versions are built. If a report has no root report, it is considered to be a root
report itself.

> **Tip:**
>
> A tax report for Belgium and the US would both use the same generic version as a base and adapt
> it for their domestic regulations.

Creating a menu item is required to access a new root report. To do so, open the report’s
configuration, click Action, Create Menu Item, and refresh the page. The
report is now available under Accounting ‣ Reporting.

> **Note:**
>
> Cases that require creating a new root report are rare, such as when a country’s tax authorities
> require a new and specific type of report.

## Variants

Variants are country-specific versions of root reports and, therefore, always refer to a root
report. To create a variant, select a generic (root) report in the Root Report field
when creating a new report.

When a root report is opened from the Accounting app’s Reporting menu, all of its
variants are displayed in the report variant selector in the top right corner of the view.

> **Tip:**
>
> VAT Report (BE) is a variant of the root Generic Tax report.
>
> ![Report variant selection.](../../../../_images/engine-variant.png)

## Lines

After creating a report (either root or variant), the next step is to fill it with lines. To create
a new line, click on Add a line. To modify an existing line, click on the line itself
and edit the popup. All lines require a Name and can have an optional Code
which allows using the line’s value in formulas.

![Engine lines options.](../../../../_images/engine-lines-options.png)

## Expressions

Each line can contain one or multiple **expressions**. Expressions can be seen as **sub-variables**
needed by a report line. To create an expression, click on Add a line *within* a line’s
popup.

When creating an expression, you must enter a Label used to refer to that expression.
The label must be unique among the expressions of each report line. Both the Computation
Engine and the Formula fields must also be completed. The **computation engine**
defines how the **formula(s)** and **subformula(s)** are interpreted. It is possible to mix
expressions using different computation engines under the same line if needed.

> **Note:**
>
> Depending on the engine, subformulas may also be required.

### Odoo Domain computation engine

When using the Odoo Domain computation engine, a formula is interpreted as an [Odoo
domain](../../../../developer/reference/backend/orm.html#reference-orm-domains) targeting `account.move.line` objects.

The subformula allows you to define how the move lines matching the domain are used to compute the
value of the expression:

`sum`
:   The result is the sum of all the balances of the matched move lines.

`sum_if_pos`
:   The result is the sum of all the balances of the matched move lines if this amount is positive.
    Otherwise, it is `0`.

`sum_if_neg`
:   The result is the sum of all the balances of the matched move lines if this amount is negative.
    Otherwise, it is `0`.

`count_rows`
:   The result is the number of sub-lines of this expression. If the parent line has a [group-by] value, this will correspond to the number of distinct
    grouping keys in the matched move lines. Otherwise, it will be the number of matched move lines.

> **Note:**
>
> To **reverse** the sign of the result, put a `-` sign at the beginning of the subformula.

![Expression line within a line report](../../../../_images/engine-expressions.png)

### Tax Tags computation engine

When using the Tax Tags computation engine, the contents of the Formula
field are matched to tax tags. If such tags do not exist when creating the expression, they will be
created.

When evaluating the expression, the expression computation can roughly be expressed as: **(amount of
the move lines with** `+` **tag)** `-` **(amount of the move lines with** `-` **tag)**.

> **Tip:**
>
> If the Formula is set to `tag_name`, the engine matches tax tags `+tag_name` and
> `-tag_name`, creating them if necessary. To exemplify further: two tags are matched by the
> formula. If the formula is `A`, it will require (and create, if needed) tags `+A` and `-A`.

### Aggregate Other Formulas computation engine

The Aggregate Other Formulas computation engine performs arithmetic operations on the
amounts obtained from other expressions. Formulas here are composed of references to expressions
separated by one of the four basic arithmetic operators (addition `+`, subtraction `-`, division
`/`, and multiplication `*`). To refer to an expression, type in its parent line’s **code** followed
by a period `.` and the expression’s **label** (ex. **code.label**).

**Subformulas** can be one of the following:

`if_above(CUR(amount))`
:   The value of the arithmetic expression will be returned only if it is greater than the provided
    bound. Otherwise, the result will be `0`.

`if_below(CUR(amount))`
:   The value of the arithmetic expression will be returned only if it is lower than the provided
    bound. Otherwise, the result will be `0`.

`if_between(CUR1(amount1), CUR2(amount2))`
:   The value of the arithmetic expression will be returned only if it is strictly between the
    provided bounds. Otherwise, it will be brought back to the closest bound.

`if_other_expr_above(LINE_CODE.EXPRESSION_LABEL, CUR(amount))`
:   The value of the arithmetic expression will be returned only if the value of the expression
    denoted by the provided line code and expression label is greater than the provided bound.
    Otherwise, the result will be `0`.

`if_other_expr_below(LINE_CODE.EXPRESSION_LABEL, CUR(amount))`
:   The value of the arithmetic expression will be returned only if the value of the expression
    denoted by the provided line code and expression label is lower than the provided bound.
    Otherwise, the result will be `0`.

`CUR` is the currency code in capital letters, and `amount` is the amount of the bound expressed in
that currency.

`cross_report(xml_id | report_id)`
:   Used to match an expression from another report targeted by the xml\_id or the report ID itself.

### Prefix of Account Codes computation engine

The Prefix of Account Codes computation engine is used to match amounts made on accounts
using the prefixes of these accounts’ codes as variables in an arithmetic expression.

> **Tip:**
>
> `21`
>
> Arithmetic expressions can also be a single prefix, such as here.

> **Tip:**
>
> `21 + 10 - 5`
>
> This formula adds the balances of the move lines made on accounts whose codes start with `21`
> and `10`, and subtracts the balance of the ones on accounts with the prefix `5`.

It is also possible to ignore a selection of sub-prefixes.

> **Tip:**
>
> `21 + 10\(101, 102) - 5\(57)`
>
> This formula works the same way as the previous example but ignores the prefixes `101`, `102`,
> and `57`.

You can apply ‘sub-filtering’ on **credits and debits** using the `C` and `D` suffixes. In this
case, an account will only be considered if its prefix matches, *and* if the total balance of the
move lines made on this account is **credit/debit**.

> **Tip:**
>
> Account `210001` has a balance of -42 and account `210002` has a balance of 25. The formula
> `21D` only matches the account `210002`, and hence returns 25. `210001` is not matched, as its
> balance is *credit*.

Prefix exclusions can be mixed with the `C` and `D` suffixes.

> **Tip:**
>
> `21D + 10\(101, 102)C - 5\(57)`
>
> This formula adds the balances of the move lines made on accounts whose code starts with `21`
> *if* it is debit (`D`) and `10` *if* it is credit (`C`), but ignores prefixes `101`, `102`, and
> subtracts the balance of the ones on accounts with the prefix `5`, ignoring the prefix `57`.

To match the letter `C` or `D` in a prefix and not use it as a suffix, use an empty exclusion `()`.

> **Tip:**
>
> `21D\()`
>
> This formula matches accounts whose code starts with `21D`, regardless of their balance sign.

In addition to using code prefixes to include accounts, you can also match them with **account
tags**. This is especially useful, for example, if your country lacks a standardized chart of
accounts, where the same prefix might be used for different purposes across companies.

> **Tip:**
>
> `tag(25)`
>
> This formula matches accounts whose associated tags contain the one with ID *25*.

If the tag you reference is defined in a data file, an XMLID can be used instead of the ID.

> **Tip:**
>
> `tag(my_module.my_tag)`
>
> This formula matches accounts whose associated tags include the tag denoted by
> *my\_module.my\_tag*.

You can also use arithmetic expressions with tags, possibly combining them with prefix selections.

> **Tip:**
>
> `tag(my_module.my_tag) + tag(42) + 10`
>
> The balances of accounts tagged as *my\_module.my\_tag* will be summed with those of accounts
> linked to the tag with ID *42* and accounts with the code prefix `10`

`C` and `D` suffixes can be used in the same way with tags.

> **Tip:**
>
> `tag(my_module.my_tag)C`
>
> This formula matches accounts with the tag *my\_module.my\_tag* and a credit balance.

Prefix exclusion also works with tags.

> **Tip:**
>
> `tag(my_module.my_tag)\(10)`
>
> This formula matches accounts with the tag *my\_module.my\_tag* and a code not starting with
> `10`.

### External Value computation engine

The External Value computation engine is used to refer to **manual** and **carryover
values**. Those values are not stored using `account.move.line`, but with
`account.report.external.value`. Each of these objects directly points to the expression it impacts,
so very little needs to be done about their selection here.

**Formulas** can be one of the following:

`sum`
:   If the result must be the sum of all the external values in the period.

`most_recent`
:   If the result must be the value of the latest external value in the period.

In addition, **subformulas** can be used in two ways:

`rounding=X`
:   Replacing `X` with a number instructs to round the amount to X decimals.

`editable`
:   Indicates this expression can be edited manually, triggering the display of an icon in the
    report, allowing the user to perform this action.

> **Note:**
>
> Manual values are created at the `date_to` currently selected in the report.

Both subformulas can be mixed by separating them with a `;`.

> **Tip:**
>
> `editable;rounding=2`
>
> This subformula shows the correct way to mix both behaviors.

### Custom Python Function computation engine

The Custom Python Function computation engine is a means for developers to introduce
custom computation of expressions on a case-by-case basis. The Formula is the name of a
**python function** to call, and the Subformula is a **key** to fetch in the
**dictionary** returned by this function. Use this computation engine only if making a custom
module.

## Columns

Reports can have an **indefinite number** of columns to display. Each column gets its values from
the **expressions** declared on the **lines**. The field expression\_label of the column
gives the label of the expressions whose value is displayed. If a line has no **expression** in that
field, then nothing is displayed for it in this column. If multiple columns are required, you must
use different **expression** labels.

![Columns of report.](../../../../_images/engine-columns.png)

When using the **period comparison** feature found under the Options tab of an
accounting report, all columns are repeated in and for each period.

## Line grouping

Non-standard grouping is possible by adding or using existing fields on the *Journal Item* model,
provided that the fields are related and non-stored.

> **Note:**
>
> Grouping lines requires the report to have explicit report lines that can be edited. The deferred
> reports, for example, do not support grouping lines as they use dynamic lines that are generated.

### Create a new field on journal item

To create a non-stored, related field in the *Journal Item* model, first go to
Accounting ‣ Journal Items, and click the  (bug) icon,
then click Fields. Click New to create a new field, and complete the
following fields:

- Field Name: a technical name for the field
- Field Label: the label to be displayed for the field
- Field Type: the type of field that this related field should point to
- Stored: Leave this field unchecked as only non-stored fields can be used to group
  lines.
- Related Model: If the field type is one2many, many2many, or
  many2one, select the model of the original field to group by.
- Related Field Definition: the technical path to the field you want to group by

  > **Tip:**
  >
  > To group by the sales team of the commercial partner, set the related field definition to
  > `move_id.team_id`.

### Group lines

To group lines, go to the [Lines] tab of the desired report, click
on the line you want to group, and edit the Group by field. Enter the technical name
(Field Name) of the field to use as the grouping key.

> **Note:**
>
> To find a list of all the model’s fields and their technical names, go to
> Accounting ‣ Journal Items, and click the  (bug)
> icon, then click Fields. The technical name of each field is listed in the
> Field Name column.

> **Note:**
>
> [Consolidation via grouping by account code](../get_started/consolidation.html#consolidation-account-mapping)

---

# Year-end closing

Year-end closing is essential for maintaining financial accuracy, complying with regulations, making
informed decisions, and ensuring transparency in reporting.

> **Note:**
>
> [Tax return](tax_returns.html)

## Fiscal years

By default, the fiscal year is set to last 12 months and ends on December 31st. However, its
duration and end date can vary due to cultural, administrative, and economic considerations.

To modify these values, go to Accounting ‣ Configuration ‣ Settings. Under the
Fiscal Periods section, change the Last Day field if necessary.

If the period lasts *more* than or *less* than 12 months, enable Fiscal Years and
Save. Go back to the Fiscal Periods section and click
Fiscal Years. Then, click New, give it a Name and both a
Start Date and End Date.

> **Note:**
>
> Once the set fiscal period is over, Odoo automatically reverts to the default periodicity,
> considering the value specified in the Last Day field.

## Year-end checklist

### Before closure

Before closing a fiscal year, ensure that everything is accurate and up-to-date:

- Make sure all bank accounts are fully [reconciled](../bank/reconciliation.html) up to year-end
  and confirm that the ending book balances match the bank statement balances.
- Confirm that all [customer invoices](../customer_invoices.html) and [vendor bills](../vendor_bills.html) have been created and all draft entries have been either confirmed or
  cancelled, as needed.
- Ensure the accuracy of all [expenses](../../expenses.html) and validate them.
- Check that all [received payments](../payments.html) have been encoded and confirmed.
- Close all [suspense accounts](../get_started/journals.html#accounting-journals-bank-cash-cc).
- Ensure [loans](../bank/loans.html) are properly registered for automatic amortization
  calculations.
- Review overdue payables and receivables aged over 60 days, and assess whether a provision for
  uncertain liabilities or an allowance for doubtful accounts is required.
- Book all [depreciation](../vendor_bills/assets.html) and [deferred revenue](../customer_invoices/deferred_revenues.html) entries.

### Closing a fiscal year

Then, to close the fiscal year:

- Run a [tax report](../reporting.html#accounting-reporting-tax-report), and verify that all tax information is
  correct.
- Reconcile all accounts on the [balance sheet](../reporting.html#accounting-reporting-balance-sheet):

  - Update the bank balances in Odoo to reflect the actual balances as per the bank statements.
  - Reconcile all transactions in the cash and bank accounts by running the [aged receivables](../reporting.html#accounting-reporting-aged-receivable) and [aged payables](../reporting.html#accounting-reporting-aged-payable) reports.
  - Audit all accounts, fully understanding all transactions and their nature, including [loans](../bank/loans.html) and [fixed assets](../vendor_bills/assets.html).
  - Optionally, [match payments](../payments.html#accounting-payments-payments-matching) to validate any open
    vendor bills and customer invoices with their payments. While this step is optional, it could
    assist the year-end closing process if all outstanding payments and invoices are reconciled,
    potentially finding errors or mistakes in the system.

Next, the accountant likely verifies balance sheet items and book entries for:

> - year-end manual adjustments,
> - work in progress,
> - depreciation journal entries,
> - loans,
> - tax adjustments,
> - etc.

During the year-end audit, the accountant may print paper copies of all balance sheet items (e.g.,
loans, bank accounts, prepayments, sales tax statements) to compare them against the balances
recorded in Odoo.

> **Note:**
>
> As part of this process, setting a [Lock Everything] date to the last day (inclusive) of the preceding
> fiscal year is good practice. This ensures that journal entries with an accounting date on or
> before the lock date cannot be created or modified during the audit. Users with *administrator*
> access rights can still create and edit entries if an [exception is configured].

#### Lock everything date

Setting a lock date prevents modifications to any posted journal entries with an accounting date on
or before the lock date. It also prevents posting new entries with an accounting date on or before
the lock date. In such cases, the system automatically sets the accounting date to the day after the
lock date.

To set a Lock Everything date, go to Accounting ‣ Accounting ‣ Lock
Dates. In the Lock Journal Entries window, set the Lock Everything date and
Save.

After setting the Lock Everything date, an [exception] can be made if a modification is necessary.

##### Lock date exception

Users with [Administrator](../../accounting.html#accounting-accountant-access-rights) access rights to the
Accounting app can create exceptions. To do so:

1. After setting and saving a lock date, go to Accounting ‣ Accounting ‣ Lock
   Dates. In the Lock Journal Entries window, remove the Lock Everything
   date.
2. In the Exception banner, choose if this exception should be set for me
   (the current user) or for everyone, and how long it should last.
3. A Reason for this exception can be added.
4. All of this information is logged in the chatter of the [company record](../../../general/companies.html).

> **Note:**
>
> To remove a lock date after it has been saved, configure the exception to apply for
> everyone and set the duration to forever. This does not apply to the
> Hard Lock date, which is irreversible to ensure inalterability and to meet accounting
> requirements in certain countries.

#### Current year’s earnings

Odoo uses a unique account type called **current year’s earnings** to display the difference
between the **income** and **expense** accounts.

> **Note:**
>
> The chart of accounts can only contain one account of this type. By default, it is a 999999
> account named Undistributed Profits/Losses.

To allocate the current year’s earnings, create a new miscellaneous entry with a date set to the end
of the fiscal year to book them to any equity account.

Then, verify whether the current year’s earnings on the **balance sheet** correctly show a zero
balance. If so, a Hard Lock date can be set to the last day of the fiscal year in
Accounting ‣ Accounting ‣ Lock Dates.

> **Note:**
>
> The Hard Lock date field is irreversible and is intended to ensure data
> inalterability required to comply with accounting regulations in certain countries. If such
> compliance is not applicable, setting this field may not be necessary. However, if required, the
> date should only be set once it is confirmed to be correct, as it **cannot be changed or
> overridden**, regardless of access rights.

## Annual closing

To complete the fiscal year-end process and finalize the annual closing, go to the Accounting
dashboard and click Tax Returns on the Tax Returns journal from the
Accounting dashboard. Alternatively, go to Accounting ‣ Accounting ‣ Tax
Returns.

This view displays a chronological list of all pending returns including [tax returns](tax_returns.html#accounting-tax-returns-vat-report), [advance payments](tax_returns.html#accounting-tax-returns-advance-payments) (based on the [fiscal localization](../../fiscal_localizations.html)), and annual closings. A pending Annual Closing follows
two steps: [review] and [submit]. The Annual Closing item includes:

- A period (year).
- A deadline date.
- The related company and [branch(es)](../../../general/companies.html#general-branches), if applicable.
- Action steps, such as [Review] and [Submit], which turn green when completed.
- Action buttons for key tasks.
- A  (vertical ellipsis) menu for additional options.

> **Note:**
>
> - Before the annual closing is reviewed, the number of Pending or Passed
>   closing validation checks is displayed in red or green, respectively.
> - If the Deadline date has passed, it appears in red.

### Review

To start reviewing an annual closing, click the annual closing line. The annual closing checks view
displays the following, depending on the [fiscal localization](../../fiscal_localizations.html):

> - Aged payables per partner: Review payables without a partner.
> - Aged receivables per partner: Review receivables without a partner.
> - Bank Reconciliation: Reconcile all bank account transactions up to year-end.
> - Deferred Entries: Ensure start and end dates are correctly set on bills and
>   invoices.
> - Earnings Allocation: After adjustments, transfer the undistributed profits/losses to
>   an equity account.
> - Fixed Assets: Ensure assets are properly registered for automatic depreciation
>   calculation.
> - Loans: Ensure loans are properly registered for automatic amortization calculations.
> - Manual Adjustments: Complete any necessary manual adjustments and internal checks.
> - No draft entries: Review and post draft invoices, bills, and entries in the period,
>   or change their accounting date.
> - Overdue payables: Review overdue payables aged over 60 days and assess the need for
>   an allowance for uncertain liabilities.
> - Overdue receivables: Review overdue receivables aged over 60 days and assess the
>   need for an allowance for doubtful accounts or expected credit loss provision, as per IFRS 9
>   guidelines.
> - Total Receivables: Verify that the total aged receivables equals the customer
>   account balance.
> - Total payables: Verify that the total aged payables equals the vendor account
>   balance.

Some of the checks are performed automatically, while others serve as reminders to review essential
tasks. Each check card is either labeled as:

- Reviewed (highlighted in green): The check has passed.
- To review (highlighted in grey): Action is required before the check can be manually
  marked as Reviewed or Supervised.
- Anomaly (highlighted in red): The automatic check detects an issue. There are two
  options:

  - Click the failed check’s card to fix the issue.
  - Click Anomaly and select Reviewed or Supervised to pass the
    check without fixing the issue.

Once all closing validation checks have passed, either labeled as Reviewed or
Supervised, click Validate to complete the Review step. The
annual closing can then be [submitted].

> **Note:**
>
> - To add customized checks, activate [developer mode](../../../general/developer_mode.html#developer-mode), and go to
>   Accounting ‣ Configuration ‣ Check. Then, click New and
>   complete the necessary fields.
> - All check status changes are logged in the chatter.

### Submit

Once a tax return has completed the [Review](tax_returns.html#accounting-tax-returns-vat-return-review) step,
click Submit.

If a Submission Instructions pop-up window appears, depending on the [fiscal
localization](../../fiscal_localizations.html), follow the local Instructions, and click
Mark as Submitted.

> **Note:**
>
> To review checks before submitting the annual closing, click the
> (vertical ellipsis) icon on the annual closing line and select Reset.
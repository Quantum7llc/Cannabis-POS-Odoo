# CRM — Pipeline, Leads & Activities

> **Odoo 19.0 Reference**
> Source: www.odoo.com/documentation/19.0 — HTML converted via markdownify

## Purpose

CRM pipeline: leads, opportunities, activities, and reporting. Covers lead scoring, pipeline stages, sales teams, and forecasting. Use when customising the sales pipeline or lead management.

---

# CRM

**Odoo CRM** helps you organize your sales activities: track leads, close opportunities and get
accurate forecasts. Keep opportunities organized with the pipeline and manage your day-to-day
activities with meetings and next activities.

> **Note:**
>
> - [Odoo Tutorials: CRM](https://www.odoo.com/slides/crm-16)

---

# Organize the pipeline

---

# Lost opportunities

Not every opportunity results in a successful sale. To keep the pipeline up-to-date, *lost*
opportunities need to be identified. Specifying why an opportunity was lost helps identify recurring
issues, reveal coaching opportunities, and can assist with improving overall sales strategy.

> **Note:**
>
> [Merging lost opportunities](merge_similar.html) with active ones will pull them back into the
> pipeline.

## Mark an opportunity as lost

To mark an opportunity as lost, first open the CRM app, and then select an
opportunity from the pipeline by clicking on its corresponding Kanban card. Doing so reveals that
opportunity’s detail form.

Then, click Lost, located at the top of the opportunity’s detail form.

![Buttons from the top of an opportunity record with the lost button emphasized.](../../../../_images/lost-opps-lost-button.png)

This opens the Mark Lost pop-up window. From the Lost Reason drop-down menu,
choose an existing lost reason. If no applicable reason is available, then create a new one by
entering it into the Lost Reason field, and then clicking Create.

Additional notes and comments can be added below the lost reason in the designated
Closing Note field.

> **Note:**
>
> Neither the Lost Reason field, nor the Closing Note field, on the
> Mark Lost pop-up window are required. However, it is recommended to include this
> information for the sake of traceability, accountability, and reporting purposes.

When all the desired information has been entered in the Mark Lost pop-up window, click
Mark as Lost.

![Lost reasons popup with sample reasons.](../../../../_images/lost-opps-lost-reason.png)

After clicking Mark as Lost, a red Lost banner is added to the upper-right
corner of the opportunity.

![A lost opportunity with the lost banner added.](../../../../_images/lost-banner.png)
> **Note:**
>
> To mark an *inactive* (archived) opportunity as lost, set the Probability field to
> `0` percent.

## Create/edit lost reasons

To create a new lost reason, or edit an existing one, navigate to CRM app ‣
Configuration ‣ Lost Reasons.

To edit an existing lost reason, click the reason to be edited to highlight it. From here, change
the selected lost reason by editing the Description field.

To create a new lost reason, click New in the upper-left corner of the Lost
Reasons page. Then, type the new lost reason in the Description field.

## View lost opportunities

To retrieve lost opportunities, go CRM app ‣ Sales ‣ My Pipeline, then click on
the search bar at the top of the page, and then remove all of the default filters.

![Search bar with lost filter emphasized.](../../../../_images/lost-opps-lost-filter.png)

Open the Filters drop-down menu by clicking the
(dropdown) icon to the right of the search bar to open the drop-down menu containing
Filters, Group By, and Favorites options, designated into
respective columns.

Select the Lost option from the Filters section. Upon selecting
Lost, only the opportunities marked as `Lost` appear on the Pipeline page.

### Sort opportunities by lost reason

To filter opportunities by a specific lost reason, click the
(dropdown) icon to the right of the search bar again to open the drop-down menu. In
addition to the Lost filter, under the Filters column, click Add
Custom Filter, which opens an Add Custom Filter pop-up window.

On the Add Custom Filter pop-up window, click in the first field and type `Lost Reason`
in the search bar, or scroll to search through the list to locate it. Then, click into the next
field, and select = from the drop-down menu. Click into the third field, and then select
a lost reason from the drop-down menu. Finally, click Add.

![Search bar with custom filter added for lost reason.](../../../../_images/lost-opps-lost-custom-filter.png)
> **Note:**
>
> To view results for more than one lost reason, select the operator is in in the
> second field of the custom filter in the Add Custom Filter pop-up window. Choosing
> this operator makes it possible to choose multiple lost reasons in the third field.
>
> ![Add Custom Filter pop-up with multiple lost reasons selected.](../../../../_images/multiple-lost-reasons.png)

## Restore lost opportunities

To restore a lost opportunity, open the CRM app to reveal the Pipeline
dashboard. Or, navigate to CRM app ‣ Sales ‣ My Pipeline. From here, click the
 (dropdown) icon to the right of the search bar to open the
drop-down menu that contains Filters, Group By, and Favorites
columns.

Under the Filters column, select Lost. Doing so reveals all the lost
opportunities on the Pipeline page.

> **Note:**
>
> To see all opportunities in the database, remove the default My Pipeline filter from
> the search bar.

From the lost opportunity’s detail form, click Restore in the upper-left corner. Doing
so removes the red Lost banner from the opportunity form, signifying the opportunity has
been restored.

![Lost opportunity with emphasis on the Restore button.](../../../../_images/lost-opps-restore.png)

### Restore multiple opportunities at once

To restore multiple opportunities at once, open the dashboard mega menu by clicking the
 (dropdown) icon (to the right of the search bar) and select the
default Lost option located under the left-side Filters column.

Next, select the list view option, represented by the  (list) icon in the
upper-right corner. Doing so places all the opportunities from the Pipeline page in a
list view. With the list view chosen, select the checkbox to the left of each opportunity to be
restored.

Once the desired opportunities have been selected, click the  Actions
drop-down menu at the top of the Pipeline page. From the
(Actions) drop-down menu, select Unarchive.

Doing so removes those selected opportunities from the Pipeline page because they no
longer fit the Lost filter criteria. Delete the Lost filter from the search
bar to reveal these newly-restored opportunities.

![Action button from list view with the Unarchive option emphasized.](../../../../_images/lost-opps-unarchive.png)

## Manage lost leads

If *Leads* are enabled on a database, then they can be marked as *lost* in the same manner as
opportunities. Leads use the same [lost reasons] as opportunities.

> **Note:**
>
> To enable leads, navigate to CRM app ‣ Configuration ‣ Settings and check
> the Leads checkbox. This adds a new Leads menu to the header menu bar at
> the top of the page.

### Mark a lead as lost

To mark a lead as lost, navigate to CRM app ‣ Leads, and select a lead from the
list. Doing so reveals that lead’s detail form. Then, click Lost, located at the top of
the lead’s detail form.

This opens the Mark Lost pop-up window. From the Lost Reason drop-down menu,
choose an existing lost reason. If no applicable reason is available, then create a new one by
entering it into the Lost Reason field, and selecting Create.

Additional notes and comments can be added below the lost reason designated in the
Closing Note field.

When all the desired information has been entered in the Mark Lost pop-up window, click
Mark as Lost.

### Restore lost leads

To restore a lost lead, navigate to CRM app ‣ Leads, and then click the
 (dropdown) icon to the right of the search bar to open the
drop-down menu that contains the Filters, Group By, and
Favorites columns.

Under the Filters column, select Lost. Doing so reveals all the lost leads
on the Leads page.

Then, click on the desired lost lead to restore, which opens that lead’s detail form.

From the lost lead’s detail form, click Restore in the upper-left corner. Doing so
removes the red Lost banner from the lead form, signifying the lead has been restored.

### Restore multiple leads at once

To restore multiple leads at once, navigate to CRM app ‣ Leads, open the
Filters drop-down menu, and select the Lost option. Select the checkbox to
the left of each lead to be restored.

Once the desired leads have been selected, click the  (Actions) drop-down
menu at the top of the Leads page. From the  (Actions)
drop-down menu, select Unarchive.

Doing so removes those selected leads from the Leads page because they no longer fit the
Lost filter criteria. Delete the Lost filter from the search bar to reveal
these newly-restored leads.

> **Note:**
>
> [Pipeline Analysis](../performance/win_loss.html)

---

# Merge similar leads and opportunities

Odoo automatically detects similar *leads* and *opportunities* within the *CRM* app. Identifying
these duplicated records allows them to be merged without losing any information in the process.
Not only does this help keep the *pipeline* organized, but it also prevents customers from being
contacted by more than one salesperson.

> **Note:**
>
> When merging opportunities, no information is lost. Data from the other opportunity is logged in
> the chatter, and the information fields, for reference.

## Identify similar leads and opportunities

Similar leads and opportunities are identified by comparing the *email address* and *phone number*
of the associated contact. If a similar lead/opportunity is found, a *Similar Leads* smart button
appears at the top of the lead (or opportunity) record.

![An opportunity record with emphasis on the Similar Leads smart button.](../../../../_images/similar-smart-button.png)

### Comparing similar leads and opportunities

To compare the details of similar leads/opportunities, navigate to CRM app ‣
Pipeline or CRM app ‣ Leads. Open a lead or opportunity, and click the
Similar Leads smart button. Doing so opens a Kanban view that only displays similar
leads/opportunities. Click on a card to view the details for the lead/opportunity, and confirm if
they should be merged.

## Merging similar leads and opportunities

> **Warning:**
>
> When merging, Odoo gives priority to whichever lead/opportunity was created in the system first,
> merging the information into the first created lead/opportunity. However, if a lead and an
> opportunity are being merged, the resulting record is referred to as an opportunity, regardless
> of which record was created first.

After confirming that the leads/opportunities should be merged, return to the Kanban view using the
breadcrumb link, or by clicking the Similar Leads smart button. Click the
 (list) icon to change to list view.

Check the box on the left of the page for the leads/opportunities to be merged. Then, click the
 Actions icon at the top of the page, to reveal a drop-down menu. From
that drop-down menu, select the Merge option to merge the selected opportunities or
leads.

When Merge is selected from the  Actions drop-down menu, a
Merge pop-up modal appears. In that pop-up modal, under the Assign
opportunities to heading, select a Salesperson and Sales Team from the
appropriate drop-down menus.

Below those fields, the leads/opportunities to merge are listed, along with their related
information. To merge those selected leads/opportunities, click Merge.

![List of similar leads and opportunities selected for merge in the CRM app.](../../../../_images/select-merge.png)
> **Important:**
>
> Merging is an irreversible action. Do **not** merge leads/opportunities unless absolutely certain
> they should be combined.

## When leads/opportunities should not be merged

There may be instances where a similar lead or opportunity is identified, but should *not* be
merged. These circumstances vary, based on the processes of the sales team and organization. Some
potential scenarios are listed below.

### Lost leads

If a lead/opportunity has been marked as [lost](lost_opportunities.html), it can still be merged
with an active lead or opportunity. The resulting lead/opportunity is marked active, and added to
the pipeline.

### Different contact within an organization

Leads/opportunities from the same organization, but with different points of contact, may not have
the same needs. In this case, it is beneficial to *not* merge these records, though assigning the
same salesperson, or sales team, can prevent duplicated work and miscommunication.

### Existing duplicates with more than one salesperson

If more than one lead/opportunity exists in the database, there may be multiple salespeople assigned
to them, who are actively working on them independently. While these leads/opportunities may need
to be managed separately, it is recommended that any affected salespeople be tagged in an internal
note for visibility.

### Contact information is similar but not exact

Similar leads and opportunities are identified by comparing the email addresses and phone numbers of
the associated contacts. However, if the email address is *similar*, but not *exact*, they may need
to remain independent.

> **Tip:**
>
> Three different leads were added to the pipeline and assigned to different salespeople. They
> were identified as *Similar Leads* due to the email addresses of the contacts.
>
> Two of the leads appear to come from the same individual, `Robin`, and have identical email
> addresses. These leads should be merged.
>
> The third lead has the same email domain, but the address is different, as is the contact name.
> While this lead is most likely from the same organization, it is from a different contact, and
> should **not** be merged.
>
> ![List of similar leads with emphasis on the contact information in the CRM app.](../../../../_images/contact-info-example.png)

---

# Manage sales teams

The *Sales Teams* feature within Odoo’s *CRM* app allows for the creation and management of multiple
sales teams, each with their own assignment rules, invoicing targets, and roster of salespeople.

## Create a sales team

To create a new sales team, go to CRM app ‣ Configuration ‣ Sales Teams, then
click New.

On the blank sales team form, enter a name in the Sales Team field.

Next, select a Team Leader from the drop-down list.

Set an Email Alias to automatically generate a lead/opportunity for this sales team
whenever a message is sent to that unique email address. Choose whether to accept emails from
Everyone, Authenticated Partners, Followers Only, or
Authenticated Employees.

Select a Company from the drop-down menu to assign this team to.

> **Note:**
>
> The Company field is only visible in multi-company databases, and is not required.

![The settings page for a new sales team.](../../../../_images/sales-team-creation.png)
> **Note:**
>
> If the *Sales* app is installed on the database, an Invoicing Target field appears on
> the sales team form. This is the revenue target for the current month. The amount entered in this
> field is used to populate the invoicing progress bar on the [sales team dashboard].

### Add sales team members

To add team members, click Add under the Members tab when editing the sales
team’s configuration page. This opens a Create Sales Team Members pop-up window.

> **Note:**
>
> If the Rule-Based Assignment feature has **not** been enabled on the *CRM* app’s
> *Settings* page, clicking Add under the Members tab opens an
> Add: Salespersons pop-up window. Tick the checkbox to the far-left of the
> salesperson to be added to the team, then click Select.
>
> ![The Add: Salespersons pop-up window on a new sales team.](../../../../_images/add-salespersons.png)

Select a user from the Salesperson drop-down list to add them to the team. To prevent
this salesperson from being automatically assigned leads, tick the Skip auto assignment
checkbox. If this feature is activated, the salesperson can still be assigned leads manually.

![The Create Sales Team Members pop-up window.](../../../../_images/create-sales-team-members.png)

The Leads (30 days) field tracks how many leads the salesperson has been assigned in the
past thirty days for this team, and the maximum number of leads they should be assigned. To edit the
maximum number of leads this salesperson can be assigned, enter that amount in the Leads
(30 days) field.

> **Note:**
>
> [Assignment rules](../track_leads/lead_scoring.html) can be configured for individual
> salespeople using the Domain section.

Click Save & Close when finished, or Save & New to add additional members.

## Enable multi teams

To allow salespeople to be assigned to more than one sales team, the *Multi Teams* setting needs to
be enabled. First, navigate to CRM app ‣ Configuration ‣ Settings. Under the
CRM section, tick the checkbox labeled Multi Teams. Then, click
Save at the top-left of the page.

![The settings page of the CRM app with the Multi Teams setting enabled.](../../../../_images/enable-multi-teams.png)

## Sales team dashboard

To view the sales team dashboard, go to CRM app ‣ Sales ‣ Teams. Any team the
user is a member of appears in the dashboard.

![The sales team dashboard in the CRM app.](../../../../_images/sales-teams-dashboard.png)

Each Kanban card gives an overview of the sales team’s open opportunities, quotations, sales orders,
and expected revenue, as well as a bar graph of new opportunities per week, and an invoicing
progress bar.

Click the Pipeline button to go directly to that team’s *CRM* pipeline.

Click on the  (vertical ellipsis) icon in the top-right corner of
the Kanban card to open a drop-down menu. Then, to view or edit the team’s settings, click
Configuration.

> **Note:**
>
> - [CRM activities and activity plans](../optimize/utilize_activities.html)
> - [Assign leads with predictive lead scoring](../track_leads/lead_scoring.html)

---

# Acquire leads

---

# Convert leads into opportunities

When moving opportunities through the *CRM* pipeline, *Leads* act as a qualifying step before a
formal opportunity is created. Enabling *Leads* provides additional time to review an opportunity’s
potential and gauge its viability before it’s assigned to a salesperson.

## Configuration

To activate the *Leads* setting, navigate to CRM app ‣ Configuration ‣ Settings
and check the box labeled, Leads. Then, click Save.

![Leads setting on CRM configuration page.](../../../../_images/convert-leads-leads-setting.png)

Activating this feature adds the Leads menu option to the header bar located along the
top of the screen.

![Leads menu on CRM application.](../../../../_images/convert-leads-leads-menu.png)

Once the *Leads* setting has been activated, it applies to all sales teams by default. To turn off
leads for a specific team, navigate to CRM app ‣ Configuration ‣ Sales Teams.
Then, select a team from the list to open that team’s configuration page. Clear the
Leads checkbox, located beneath the Sales Team field, then click
:icon: `fa-cloud-upload` Save.

![Leads menu on CRM application.](../../../../_images/convert-leads-leads-button.png)

## Convert a lead into an opportunity

To convert a lead into an *opportunity*, navigate to CRM app ‣ Leads, and click
on a lead from the list to open it.

> **Warning:**
>
> Attempting to convert a lead with a 100% probability into an opportunity will result in an error
> message.
>
> ![The error message that appears when attempting to convert a 100% probability lead into an opportunity.](../../../../_images/100-percent-lead-error1.png)

Click the Convert to Opportunity button, located at the top-left of the page.

![Create opportunity button on a lead record.](../../../../_images/convert-leads-convert-opp-button.png)

This opens a *Convert to opportunity* pop-up. Here, select the Convert to opportunity
option in the Conversion Action field.

Then, select a Salesperson and a Sales Team to which the opportunity should
be assigned. Neither field is required, but if a selection is made in the Salesperson
field, the Sales Team is automatically populated based on the assignee’s assigned team.

If the lead has already been assigned to a salesperson or a team, these fields automatically
populate with that information.

Under the Customer heading, choose from the following options:

- Create a new customer: Choose this option to use the information in the lead to create
  a new customer record.
- Link to an existing customer: Choose this option, then select a customer from the
  drop-down menu to link this opportunity to.

Lastly, when all configurations are complete, click Create Opportunity.

![Create opportunity pop-up.](../../../../_images/convert-leads-conversion-action.png)

To view the newly created opportunity, navigate to CRM app ‣ My Pipeline.

### Merging similar leads and opportunities

If a Similar Leads smart button appears at the top of the page for the lead, a similar
lead or opportunity already exists in the database. Before converting the current lead, click the
smart button to check if the leads should be merged.

> ![Close up of a lead with emphasis on the Similar Leads smart button.](../../../../_images/similar-leads-smart-button.png)

To merge this lead with an existing similar lead or opportunity, click the Convert to
Opportunity button and select Merge with existing opportunities in the
Conversion Action field. This generates a list of the similar leads/opportunities to be
merged.

When merging, Odoo gives priority to whichever lead/opportunity was created in the system first,
merging the information into the first created lead/opportunity. The resulting record is an
opportunity.

---

# Create opportunities from web contact forms

Adding a contact form to a website makes it easy to convert visitors into leads and opportunities.
After a visitor submits their information, an opportunity can be created automatically, and assigned
to a designated sales team and salesperson.

## Customize contact forms

By default, the *Contact Us* page on an Odoo website displays a preconfigured contact form. This
form can be customized, as needed, to suit the needs of a specific sales team.

Navigate to Website app ‣ Contact Us, then click Edit in the
top-right of the screen to open the web editor. Click on the form building block in the body of the
webpage to open the form configuration settings on the right sidebar. The following options are
available to customize the contact form from the From section of the right sidebar:

![The form configuration settings on an Odoo website.](../../../../_images/form-customization.png)

- Action: the default action for a contact form is Send an Email. Select
  Create an Opportunity from the drop-down list to capture the information in the *CRM*
  app.
- Sales Team: choose a sales team from the drop-down menu that the opportunities from
  this form should be assigned to. This field **only** appears if the Action field is
  set to Create an Opportunity.
- Salesperson: if the opportunities should be assigned to a specific salesperson, select
  them from the drop-down menu. If no selection is made in this field, the opportunities are
  assigned based on the team’s existing rules.
- Marked Fields: use this field to alter how the form handles marked fields. The default
  option is to treat marked fields as Required, which is the recommended setting.
- Mark Text: choose how Marked Fields should be identified. The default
  character is an asterisk (`*`).
- Labels Width: use this field to alter the pixel width of the labels, if desired.
- On Success: select how the webpage reacts after a customer successfully submits a
  form. Nothing keeps the customer on the same screen, with the addition of a
  confirmation message that the form was submitted successfully. Redirect sends the
  customer to a new webpage, based on the address provided in the URL field below.
  Show Message replaces the form with a preconfigured message that informs the customer
  someone should respond to them as soon as possible.
- URL: if Redirect is selected in the On Success field, enter
  the URL for the webpage, where customers should be directed after successfully submitting a form.
- Visibility: use the drop-down menu to add any visibility conditions for this field, if
  desired.

> **Warning:**
>
> If *leads* are activated in *CRM* settings, selecting Create an Opportunity generates
> a lead instead. To activate leads, navigate to CRM app ‣ Configuration ‣
> Settings, and tick the Leads checkbox. Then, click Save.

### Customize contact form fields

In addition to the settings for the form, the settings for each field can be customized, as well.
With the web editor menu still open, click into a field to open the Field configuration
settings section on the sidebar. The following options are available to customize a field:

- Type: choose a custom field option or an existing field type.
- Input Type: determine the type of information customers should input. Available
  options are Text, Email, Telephone, or Url. The
  selection made in this field limits the format that customers can use when entering information.
- Label: enter the name for the field.
- Position: choose the way the label is aligned with the rest of the form. The label can
  be hidden, above the field, to the left of the field, or right adjusted and closer to the field.
- Description: slide the toggle to add a description for the field, which can provide
  additional instructions to customers. Click under the field on the form to add the description.
- Placeholder: enter an example to help users know how to input information where
  formatting is important, such as a phone number or email address.
- Default Value: enter a value to include in the form, by default, if the customer does
  not provide information in the field. *It is not recommended to include a default value for
  required fields*.
- Required: slide the toggle to mark this field as required if it **must** be filled in
  for every submission.
- Visibility: select when this field should be visible. Use the button on the left to
  choose whether to show or hide this field on a desktop users. Use the button on the right to
  choose whether to show or hide this field to mobile users.
- Animation: select if this field should have any animation.

![The field configuration settings on an Odoo website.](../../../../_images/field-customization.png)

## View opportunities

After a customer submits a contact form, and an opportunity is created, it is assigned based on the
[form settings]. To view opportunities, navigate to
CRM app ‣ Sales ‣ My Pipeline.

> **Note:**
>
> If leads are activated on the database, contact form submissions are generated as leads, not
> opportunities. To activate leads, navigate to CRM app ‣ Configuration ‣
> Settings, and tick the Leads checkbox. Then, click Save.
>
> Navigate to CRM app ‣ Leads to view the newly-created leads.

On the My Pipeline dashboard, click on an opportunity card in the Kanban view to open
the opportunity record. The information submitted by the customer is visible on the opportunity
record.

> **Note:**
>
> As the contact form fields are customizable, the fields on the opportunity record, where the form
> information is stored, varies accordingly.
>
> If the preconfigured contact form is used, the *Subject* field is added to the Title
> field, and the content in the Notes field, which is labeled as Your
> Question, is added to the Internal Notes tab.

> **Note:**
>
> - [Manage sales teams](../pipeline/manage_sales_teams.html)
> - [Convert leads into opportunities](convert.html)
> - [Assign leads with predictive lead scoring](../track_leads/lead_scoring.html)
> - [Website forms](../../../websites/website/web_design/building_blocks.html#website-building-blocks-form)

---

# Create leads (from email or manually)

Leads can be added to the *CRM* app from custom email aliases, and by manually creating new
records. This is in addition to the leads and opportunities created in the app through the
[website contact form](opportunities_form.html).

First, ensure the *Leads* feature is enabled in the database by navigating to CRM
app ‣ Configuration ‣ Settings. Tick the Leads checkbox, then click
Save.

## Configure email aliases

Each sales team has the option to create and utilize their own unique email alias. When messages
are sent to this address, a lead (or opportunity), is created with the information from the
message.

To create or update a sales teams’ email alias, navigate to CRM app ‣
Configuration ‣ Sales Teams. Click on a team from the list to open the team’s details page.

![The sales team details page, focused on the email alias section.](../../../../_images/email-alias.png)

In the Email Alias field, enter a name for the email alias, or edit the existing name.
In the Accept Emails From field, use the drop-down menu to choose who is allowed to send
messages to this email alias:

- Everyone: messages are accepted from any email address.
- Authenticated Partners: only accepts messages from email addresses associated with a
  a partner (contact or customer) record.
- Followers only: only accepts messages from those who are following a record related to
  the team, such as a lead or opportunity. Messages are also accepted from team members.
- Authenticated Employees: only accepts messages from email addresses that are connected
  to a record in the *Employees* app.

### Leads created from email

Leads created from email alias messages can be viewed by navigating to CRM app ‣
Leads. Click a lead from the list to open it, and view the details.

The email received by the alias is added to the *chatter* thread for the lead. The subject line of
the message is added to the title field, and the Email field is updated with the
contact’s email address.

![The chatter thread of a newly created lead in the CRM app.](../../../../_images/chatter-message.png)
> **Note:**
>
> If the *leads* feature is **not** enabled on the database, messages to the email alias are added
> to the database as opportunities.

> **Note:**
>
> [Communication in Odoo by email](../../../general/email_communication.html)

## Manually create leads

Leads can be added directly to the *CRM* app by manually creating a new record. Navigate to
CRM app ‣ Leads to view a list of existing leads.

> **Note:**
>
> Leads can also be added via the [Generate Leads](lead_mining.html) button.

At the top-left of the list, click New to open a blank Leads form.

In the first field of the new form, enter a title for the new lead. Next, enter a Contact
Name, and a Company Name.

> **Note:**
>
> If a lead is [converted to an opportunity](convert.html), the Company Name field is
> used to either link this opportunity to an existing customer, or to create a new customer.

### Manually create opportunities

To manually create an opportunity, navigate to CRM app ‣ Sales ‣ My Pipeline.
At the top-left of the page, click New to create a new opportunity Kanban card. In the
Organization/Contact field, enter the name of the company the opportunity is for.

Choose a name, and enter it in the Opportunity field. *This is a required field.* When
manually creating an opportunity, it is helpful to add a name that relates to the details of the
opportunity.

> **Tip:**
>
> In the example below, the opportunity is named `5 VP Chairs`. This identifies the product the
> customer is interested in, as well as the potential number of products.
>
> ![An example of an opportunity in the CRM pipeline.](../../../../_images/opportunity-example.png)

Enter the contact information for the opportunity in the Email and Phone
fields.

In the Expected Revenue field, enter an estimated value for the opportunity.

> **Note:**
>
> The information in the Expected Revenue and priority fields can be used to track
> performance for individual salespeople, and on a team basis. See
> [Expected revenue report](../performance/expected_revenue_report.html) and [Assign leads with predictive lead scoring](../track_leads/lead_scoring.html) for more
> information.

Then, use the  (star) icons to assign a priority.

- : low priority
- : medium priority
- : high priority
- : very high priority

> **Note:**
>
> Assigning a priority changes the order of leads in Kanban view, with higher priority leads
> displayed first.

Once all the necessary information has been entered, click Add.

![The CRM pipeline with a newly created opportunity.](../../../../_images/create-opportunities.png)

---

# Create and send quotations

Once a qualified lead has been converted into an opportunity, the next step is to create and deliver
a quotation. This process can be easily handled through Odoo’s *CRM* application.

## Create a new quotation

To create a new quotation, open the CRM app, revealing the Pipeline
page on the main *CRM* dashboard.

From here, click on any opportunity to open it. Review the existing information and update any
fields, if necessary.

> **Note:**
>
> If a quotation has already been created for this opportunity, it can be found by clicking on the
> Quotations smart button at the top of the top of the form. The number of existing
> quotations is listed on the smart button, as well.

At the top-left of the form, click the New Quotation button.

![Qualified lead form with New Quotation button emphasized.](../../../../_images/send-quotes-new-button.png)
> **Warning:**
>
> The **Sales** application **must** be installed for the New Quotation button to
> appear.

> **Warning:**
>
> The Customer field is **not** required on the opportunity form.
>
> However, customer information must be added or linked before a quotation can be sent. If the
> Customer field is left blank on the opportunity, clicking the New
> Quotation button opens a pop-up window with the following options:
>
> - Create a new customer: creates a new customer record, using any available
>   information provided on the opportunity form.
> - Link to an existing customer: opens a drop-down field with existing customer names.
>   Select a name to link this new quotation to an existing customer record.
> - Do not link to a customer: the quotation will **not** be linked to a customer, and
>   no changes are made to the customer information.

Once this button is clicked, a new quotation form appears. Confirm the information in the top half
of the form, and update any missing or incorrect fields:

- Customer: the company or contact for whom this quotation was created.
- Referrer: if this customer was referred by another customer or contact, select it from
  the drop-down menu in this field.
- Invoice Address: physical address where the invoice should be sent.
- Delivery Address: physical address where any products should be delivered.
- Quotation Template: if applicable, select a pre-configured [quotation template](../../sales/sales_quotations/quote_template.html) from this field.
- Expiration: date when this quotation is no longer valid.
- Quotation Date: creation date of draft/sent orders, confirmation date of confirmed
  orders. Note that this field is only visible if [Developer mode (debug mode)](../../../general/developer_mode.html) is active.
- Recurring Plan: if this quotation is for a recurring product or subscription, select
  the recurring plan configuration to be used.
- Pricelist: select a pricelist to be applied to this order.
- Payment Terms: select any applicable payment terms for this quotation.

![Qualified lead form with New Quotation button emphasized.](../../../../_images/send-quotes-new-quotation.png)
> **Note:**
>
> The Expiration field automatically populates based on the creation date of the
> quotation, and the default validity time frame.
>
> To update the default validity time frame, navigate to Sales app ‣
> Configuration ‣ Settings ‣ Quotations & Orders and update the Default Quotation
> Validity field. To disable automatic expiration, enter `0` in this field.
>
> When the desired changes are complete, click Save.
>
> When using a quotation template, the expiration date is based off of the Quotation
> Validity field on the template. To alter the validity date computation on a template, go to
> Sales app ‣ Configuration ‣ Sales Orders ‣ Quotation Templates.
>
> Then, click on a template to open it, and update the number in the Quotation Validity
> field.

### Order lines

After updating the customer, payment, and deadline information on the new quotation, the
Order Lines tab can be updated with the appropriate product information.

To do that, click Add a product in the Order Lines tab.

Next, type the name of an item into the Product field to search through the product
catalog. Then, select a product from the drop-down menu, or create a new one by selecting
Create or Create and Edit.

After selecting a product, update the Quantity, if necessary. Confirm the information in
the remaining fields.

To remove a line from the quotation, click the  (trash can) icon.

To organize products into sections click Add a section and type a name for the section.
Then, click the  (drag) icon to the left of the name and drag to
move the section to the appropriate location. Move each product using the same method to finish
organizing the quotation order lines.

![Categories are used to create separate sections on the order lines of a quote.](../../../../_images/product-sections.png)

#### Product catalog

To quickly add numerous products to the quotation, click the Catalog button to open the
product catalog.

All products in the database are listed as cards and can be sorted in the left panel by
Product Category and Attributes.

![The product catalog displays all products as cards.](../../../../_images/product-catalog1.png)

To add a product, click the  Add button on the product card.
Set the quantity of the item using the  (add) or
(subtract) buttons, or type the quantity in the number field between the two buttons.
To remove an item, click the  Remove button on the product card.

![The purple add and subtract buttons are used to set the quantity of an item.](../../../../_images/set-quantity.png)

Once all product quantities are set, click the Back to Quotation button to return to the
quotation. The items selected in the product catalog now appear in the Order Lines tab.

## Preview and send quotation

To see a preview of the quotation as the customer will see it, click the Preview button.
Doing so opens a preview in the Customer Portal.

After reviewing the customer preview, click Return to edit mode to return to the
quotation form in the backend.

When the quotation is ready to deliver to the customer, click the Send by Email button.

Doing so opens a pop-up window with a pre-configured email message. Information from the quotation,
including the contact information, total cost, and quotation title are be imported from the
quotation.

A PDF of the quotation is added as an attachment to the email.

> **Note:**
>
> A pre-loaded template is used to create the email message. To alter the template, click the
> internal link to the right of the Load template field, located at the bottom of the
> email pop-up window.
>
> To select a new template, select an option from the Load template drop-down menu.

Proceed to make any necessary changes to the email, then click Send. A copy of the
message is added to the *Chatter* of the of the record.

After a quotation is sent, the originating opportunity’s Quotations smart button updates
with a new count. This quotation, and all other quotations can be accessed through this smart
button at the top of the opportunity in the *CRM* app.

Any quotations attached to the opportunity that are confirmed, and have therefore been converted to
sales orders, will be deducted from the number listed on the Quotations smart button.
Instead, the value of the sales order will appear in the Orders smart button located in
the same control panel.

## Mark an opportunity won or lost

In order to keep the pipeline up to date and accurate, opportunities need to be identified as *won*
or *lost* once a customer has responded to a quotation.

To mark an opportunity as *won* or *lost*, return to the opportunity using the breadcrumbs at the
top-left of the quotation form. Or navigate to CRM app ‣ Sales ‣ My Pipeline
and click on the correct opportunity to open it.

At the top-left of the form, click on either the Won or Lost button.

If the opportunity is marked *won*, a green Won banner is added to the record, and it is
moved to the Won stage.

Marking an opportunity as *lost*, via the Lost button opens a Mark Lost
pop-up window, where a Lost Reason can be entered.

From the Lost Reason drop-down field, choose an existing lost reason. If no applicable
reason is available, create a new one by entering it into the Lost Reason field, and
clicking Create.

> **Note:**
>
> It’s best practice to try and use pre-configured Lost Reason values as much as
> possible or to limit the creation of new values only to sales team leads. Using consistent values
> for this parameter will make pipeline analysis easier and more accurate when filtering for the
> Lost Reason parameter.
>
> To set up new values for this field, navigate to CRM ‣ Configuration ‣ Lost
> Reasons, and click both New and Save for each new entry added to the
> list.

Additional notes and comments can be added in the Closing Note field.

When all the desired information has been entered in the Mark Lost pop-up window, click
Mark as Lost.

Upon clicking Mark as Lost, the pop-up window disappears, and Odoo returns to the
opportunity form, where a new red Lost banner is now present in the upper-right corner
of the opportunity.

Once an opportunity is marked as *lost*, it is no longer considered active, and it is removed from
the pipeline.

In order to view a *lost* opportunity from the pipeline, click the down arrow icon to
the right of the search bar, and select either Lost or Archived from the
drop-down menu that appears.

> **Warning:**
>
> While opportunities that have been marked as *lost* are considered *Archived*, be advised that,
> in order for an opportunity to be included as *lost* in reporting, it **must** be specifically
> marked as *lost*, not *Archived*.

---

# Lead mining

*Lead mining* is a feature that allows *CRM* users to generate new leads directly within their Odoo
database. To ensure lead qualification, lead mining output is determined by a variety of filtering
criteria, such as the country, the company size, and the industry.

## Configuration

To get started, go to CRM app ‣ Configuration ‣ Settings, and select the
Lead Mining checkbox to activate the feature. Then, click Save.

![Activate lead mining in Odoo CRM settings.](../../../../_images/activate-lead-mining.png)

## Generate leads

> **Note:**
>
> If the [Leads](convert.html) feature is not enabled, then
> lead generation creates opportunities instead.

With the *Lead Mining* setting activated, the *Generate Leads* button is added to the upper-left
corner of the *CRM* *Pipeline* (CRM app ‣ Sales ‣ My Pipeline). Lead mining
requests are also available through CRM app ‣ Configuration ‣ Lead Mining
Requests and through CRM app ‣ Leads, where the Generate Leads
button is also available.

From any of these locations, click the Generate Leads button, and a pop-up window
appears.

![The pop-up window with the selection criteria in order to generate leads in Odoo.](../../../../_images/generate-leads-popup.png)

Leads can be generated for Companies to get company information only, or for Companies and their Contacts to get
both company information and contact information for individual employees.

Filtering options for generating leads include the following:

- Countries: Filter leads based on the country (or countries) they are located in.
- States: Filter leads even further based on the state in which they are located, if
  applicable.
- Industries: Filter leads based on the specific industry they work in.
- Filter on Size: Generates a field labeled Size. Fill in the blanks to
  create a range for the desired company size based on its number of employees.

> **Note:**
>
> When using Companies and their Contacts, generated contacts can also be filtered based on their Role or
> Seniority.

Additionally, there are options for sales team assignment and internal tracking:

- Sales Team: Set which Sales Team the leads will be assigned to.
- Salesperson: Set which member of the Sales Team the leads will be assigned to.
- Default Tags: Set which tags are applied directly to the leads once found.

> **Warning:**
>
> If applicable, make sure to be aware of the latest EU regulations when receiving contact
> information. Learn more about the General Data Protection Regulation on [Odoo GDPR](http://odoo.com/gdpr).

### View leads

After leads are generated, they are assigned to the designated salesperson and team. To view
additional information regarding the lead, select one from the list and click to open it.

Additional information for the lead is provided in its chatter. This can include the number of
employees that work for the lead, the technology it uses, its timezone, and any direct contact
information.

![The chatter thread of a newly generated lead.](../../../../_images/generated-lead.png)

## Pricing

Lead mining is an *In-App Purchase* service, and each generated lead costs one [credit](../../../essentials/in_app_purchase.html#in-app-purchase-credits). When using the Companies and their Contacts option to generate leads, one additional credit is
used for each contact generated. See here for complete pricing information: [Lead Generation by Odoo
IAP](https://iap.odoo.com/iap/in-app-services/167?). Enterprise Odoo users with a valid
subscription get free credits to test IAP features before purchasing more credits for the
database. This includes demo/training databases, educational databases, and one-app-free databases.

To buy credits, navigate to CRM app ‣ Configuration ‣ Settings. In the
Lead Generation section, under the Lead Mining feature, click
Manage Service & Buy Credits to go to the Lead Generation Settings page. Click
Buy Credit to go to the *Odoo IAP* page where you’ll be able to buy packs of Lead
Generation credits.

Credits may also be purchased by navigating directly to the [Odoo IAP](https://iap.odoo.com/) page
and clicking the Lead Generation button.

![Buy credits in the Odoo IAP settings.](../../../../_images/view-my-services-setting.png)
> **Warning:**
>
> Credits are **not** interchangeable between IAP services. *Lead Generation* credits may not be
> spent on other IAP services, and no other IAP credits can be spent on *Lead Generation*.

> **Note:**
>
> [In-app purchases (IAP)](../../../essentials/in_app_purchase.html)

---

# Assign and track leads

---

# Assign leads with predictive lead scoring

The Odoo **CRM** app can automatically assign leads/opportunities to sales teams and salespeople. A
standard practice is to assign leads based on the probability of winning each lead. Companies can
prioritize the leads that are more likely to result in successful deals by quickly assigning them to
the appropriate salespeople.

Odoo automatically calculates the probability of winning each lead using a method called *predictive
lead scoring*.

## Predictive lead scoring

Predictive lead scoring is a machine-learning model that uses historical data from Odoo **CRM** to
score open leads/opportunities.

As a company processes opportunities through the CRM pipeline, Odoo collects data on which
opportunities are won and lost. Predictive lead scoring uses this data to predict the probability of
winning each new lead or opportunity.

The more opportunities that are sent through the CRM pipeline, the more data Odoo collects,
resulting in more accurate probabilities.

Specifically, Odoo’s predictive lead scoring uses the *naive Bayes* probability model:

\[\begin{equation}
P(A | B) = \frac{P(A) \times P(B | A)}{P(B)}
\end{equation}\]

Breaking down the equation:

- P(A|B) = The probability of a successful lead *in this case*
- P(A) = The overall probability of a lead being successful regardless of the conditions
- P(B|A) = The probability of this being the case given a lead is successful
- P(B) = The probability of this being the case

The term *in this case* refers to the variables that can affect a lead being successful in Odoo.
This can include variables such as the assigned Salesperson, the source of the lead, the language of
the lead, and other historical and demographic data.

Which variables are considered in this calculation can be [configured] to tailor the calculation to each business’s needs.

The probability of success of each opportunity is displayed on the opportunity form, and it updates
automatically as the opportunity progresses through the CRM pipeline.

![The probability of success displayed on the opportunity form.](../../../../_images/probability-opportunity-form.png)

When an opportunity moves to the next stage, its probability of success automatically increases
according to the predictive lead scoring algorithm.

### Configuration

Predictive lead scoring is always active in Odoo **CRM**. However, the variables used to calculate
the probability of success can be customized in the settings.

To customize the variables used by predictive lead scoring, go to CRM ‣
Configuration ‣ Settings. Under Predictive Lead Scoring, click on the
Update Probabilities button.

Then, click on the drop-down menu and the  (Delete) icon to choose which
variables the predictive lead scoring feature takes into account.

![The Update Probabilities window in the Predictive Lead Scoring settings.](../../../../_images/update-probabilities.png)

Any number of the following variables can be activated:

- State: the geographical state from which the opportunity originates
- Country: the geographical country from which the opportunity originates
- Phone Quality: whether or not a phone number is listed for the opportunity
- Email Quality: whether or not an email address is listed for the opportunity
- Source: the source of an opportunity (e.g. search engine, social media)
- Language: the spoken language specified on the opportunity
- Tags: the tags placed on the opportunity

> **Note:**
>
> The variables `Stage` and `Team` are always in effect. `Stage` refers to the CRM pipeline stage
> that an opportunity is in. `Team` refers to the sales team that is assigned to an opportunity.
> Predictive lead scoring *always* takes into account these two variables, regardless of which
> optional variables are selected.

Next, click on the date field next to the option Consider leads created as of the: to
select the date from which predictive lead scoring begins its calculations.

Lastly, click Update to save changes.

### Change the probability manually

An opportunity’s probability of success can be changed manually on the opportunity form. Click on
the probability number to edit it. The probability for a lead **cannot** be manually set to 100%.
Attemping to convert a lead with a 100% probability into an opportunity will result in an error
message:

![The error message that appears when attempting to convert a 100% probability lead into an opportunity.](../../../../_images/100-percent-lead-error.png)

Manually changing the probability overwrites the automatic probability updates for that
lead/opportunity. The AI-computed probability remains visible and automatically updates as the
opportunity moves through each stage of the pipeline or as more information is added to the lead
form. To revert to the AI-computed probability, click on the AI icon next to the probability
percentage.

![The icon used to reactivate automatic probability on an opportunity form.](../../../../_images/probability-icon.png)

## Assign leads based on probability

Odoo **CRM** can assign leads/opportunities to sales teams and salespeople based on specified rules.
Create assignment rules based on the leads’ probability of success to prioritize those that are more
likely to result in leads and opportunities.

### Configure rule-based assignment

To activate *rule-based assignment*, navigate to CRM ‣ Configuration ‣
Settings, and activate Rule-Based Assignment.

The rule-based assignment feature can be set to run Manually, meaning an Odoo user must
manually trigger the assignment, or Repeatedly, meaning Odoo automatically triggers the
assignment according to the chosen time period.

To configure automatic lead assignment, select Repeatedly for the Running
section. The frequency of this automatic assignment is customized within the Repeat
every section. Enter a specific number and select a corresponding time period to establish the
desired interval. Time periods range from Minutes to Weeks.

![The Rule-Based Assignment setting in CRM settings.](../../../../_images/rule-based-assignment.png)

If rule-based assignment is set to run Repeatedly, the assignment can still
be triggered manually using the  (Update now) icon in the
Rule-Based Assignment settings, or using the Assign Leads button on the
sales team configuration page. Once a lead has been assigned to a salesperson via this rule, the
leads are automatically converted into an opportunity by the system.

### Configure assignment rules

Next, configure the *assignment rules* for each sales team or salesperson. These rules determine
which leads Odoo assigns to which people. To get started, navigate to CRM ‣
Configuration ‣ Sales Teams, and select a sales team.

On the sales team configuration form, under Assignment Rules, click on Edit
Domain to configure the rules that Odoo uses to determine lead assignment for this sales team. The
rules can include anything that may be relevant for this company or team, and any number of rules
can be added.

Click Add Filter to start creating assignment rules. Click on the
sign on the right of the assignment rule to add another line. Click on the x symbol to
remove the line.

To create an assignment rule based on an opportunity’s probability of success, click on the far left
drop-down menu of an assignment rule line, and select Probability.

From the middle drop-down menu, select the desired equation symbol—most likely the symbol for
*greater than*, *less than*, *greater than or equal to*, or *less than or equal to*.

In the far right space, enter the desired number value of the probability. Finally, click
Save to save changes.

> **Tip:**
>
> To configure an assignment rule such that a sales team receives leads that have a probability of
> success of 20% or greater, create a Domain line that reads: `Probability >= 20`.
>
> ![Sales team domain set to probability greater than or equal to twenty percent.](../../../../_images/probability-domain.png)

Separate assignment rules can also be configured for individual team members. From the sales team
configuration page, click on a team member in the Members tab, then edit the
Domain section. Click Save to save changes.

If automatic lead assignment is configured in the settings, both the sales team and individual team
members have the option to Skip auto assignment. Check this box to omit a particular
sales team or salesperson from being assigned leads automatically by Odoo’s rule-based assignment
feature. If Skip auto assignment is activated, the sales team or salesperson can still
be assigned leads manually.

To manually assign leads to this sales team, click on the Assign Leads button at the top
of the sales team configuration page. This assigns any leads that are currently unassigned and match
this team’s specified domain.

---

# Unattended leads report

*Unattended leads* are leads that have scheduled activities that are either due or past due.
Whenever an activity is scheduled, Odoo tracks the due date, and sends email reminders to the users
the activity is assigned to.

An *unattended leads report* compiles all active leads in the pipeline with due or past due
activities, allowing a sales manager to identify which opportunities require immediate attention.

By pulling a daily unattended leads report, sales managers can remind their teams to address
outstanding activities before they become past due, helping avoid neglected leads and reinforcing
proactive behaviors in their salespeople.

> **Tip:**
> > A sales manager starts their day by pulling an unattended leads report, and upon switching to
> > list view, they see the following:
> >
> > ![List view of a sample Unattended Leads report with the activities emphasized.](../../../../_images/unattended-leads-example.png)
>
> Their team member, Mitchell, has two leads in the *Proposition* stage with activities that are
> due.
>
> The yellow 📞 (phone) icon indicates that the `Modern Open Space` lead has a phone
> call activity scheduled for today. The red ✉️ (envelope) icon indicates that the `5 VP
> Chairs` lead has an email activity scheduled that is past due.
>
> Clicking on the `5 VP Chairs` lead, the sales manager opens the record of the lead and reviews the
> chatter. They see that the email was scheduled to be sent two days ago, but Mitchell never marked
> this activity as done.
>
> ![Example of overdue activities notification in the chatter of a lead.](../../../../_images/overdue-activities-email.png)

> **Warning:**
>
> In order to pull a unattended leads report, sales teams **must** be regularly utilizing activity
> in the *CRM* pipeline, on individual lead and opportunity cards.
>
> It is **not** possible to compile a complete report if the sales people are not using the
> *Activities* feature in the *chatter*
>
> For more information, refer to [Activities](../../../essentials/activities.html)

## Create an unattended leads report

To create an unattended leads report, first navigate to CRM app ‣ Reporting ‣
Pipeline to open the Pipeline Analysis dashboard. Click into the Search…
bar at the top of the page, and remove all of the default filters.

> **Note:**
>
> The Created on filter can remain active, as this variable may be useful to include in
> the report.

Next, add custom filters by clicking the 🔻(triangle pointed down) icon to the right of
the Search… bar to open the drop-down menu that contains Filters,
Group By, and Favorites columns. Under the Filters column,
click Add Custom Filter, which opens an Add Custom Filter pop-up window.

The Add Custom Filter pop-up window allows for the creation of more specific filters.

### Add custom filters

In order to generate an unattended leads report, filters need to be created for the following
conditions:

> - [Past due activities]: limits the results to only include
>   leads with an assigned activity where the due date has past. This can be altered to include
>   activities due to occur on the date the report is generated as well.
> - [Unassigned leads]: excludes leads without an
>   assigned salesperson.
> - [Specific sales teams]: limits results to only include
>   leads assigned to one or more sales teams. This filter is optional and should not be included if
>   the report is intended for the entire company.

#### Add filter for past due activities

Click the first field for the new rule, and type `Activities` in the Search… bar, or
scroll to search through the list to locate it. Then, next to Activities, click the
> (greater than sign) to open a new drop-down menu with secondary conditions.

Type `Due Date` in the Search… bar, or scroll to search through the list. Click
Due Date to add it to the rule.

> ![Custom filter pop-up with emphasis on the options for activities and due date.](../../../../_images/activities-due.png)

Then, click into then next field and select <= from the drop-down menu. Selecting this
operator includes all activities with a due date up to, and including, the date selected in the next
field.

The third field can be left as today’s date, or adjusted as needed.

#### Exclude unassigned leads

After filtering for activities, add a New Rule. Then, click into the first field for the
new rule, and type `Salesperson` in the Search… bar, or scroll to search through the
list to locate it.

In the rule’s second field, select is set from the drop-down menu. Selecting this
operator excludes any leads not assigned to a specific salesperson.

#### Add a Sales team

> **Note:**
>
> This filter is optional. To view results for the entire company, do **not** add this filter, and
> continue to [View results]

To limit the results of the report to one or more sales teams, click New Rule. Next,
click the first field for the new rule, and type `Sales Team` in the Search… bar, or
scroll to search through the list to locate it.

In the rule’s second field, select is in from the drop-down menu. Selecting this
operator limits results to the sales teams selected in the next field.

Lastly, in the third field, select the desired sales team from the drop-down menu. Multiple teams
can be added in this field, where each parameter is treated with an “or” (e.g. “any”) operator in
the search logic.

![An example of the Custom Filter pop-up window with all of the rules configured.](../../../../_images/configured-custom-rules1.png)

An example of the **Add Custom Filter** pop-up window with all of the rules configured.

## View results

At the top of the Add Custom Filter form, there is an option to match any or
all of the rules. In order to properly run the report, only records that match **all**
of the following filters should be included. Before adding the filters, make sure all is
selected in this field.

![Example of overdue activities notification in the chatter of a lead.](../../../../_images/all-custom-filter.png)

After the filters are configured, click Add. The resulting report displays all leads
assigned to a salesperson where an activity is past due, or is due on the current date. The default
display is a bar graph, where the leads are grouped by *stage*.

To group the results by salesperson, click the 🔻(triangle pointed down) icon to the
right of the Search… bar to open the drop-down menu that contains Filters,
Group By, and Favorites columns. Under the Group By heading,
select Salesperson.

> **Note:**
>
> The option to group by Sales Team is also available under the Group By
> heading.

To change to a *list* view, click the ≣ (list) icon in the top-right corner of the
screen.

> **Note:**
> > Clicking the (toggle) icon opens a drop-down menu of additional columns that can be
> > added to the report.
> >
> > Some options that are beneficial for this report include:
> >
> > - Activities: the summary of the latest activity for this lead.
> > - Expected Closing: the estimated date on which the lead will be won.
> > - Probability: estimated success rate based on the stage.
>
> ![Custom filter pop-up with emphasis on the options for activities and due date.](../../../../_images/additional-options.png)

> **Note:**
>
> [Activities](../../../essentials/activities.html)

---

# Quality leads report

A *quality lead* is a lead that is likely to result in a sale. It should match the characteristics
most commonly believed to help salespeople close a deal, in addition to more precise criteria that
is specific to each organization.

> **Note:**
>
> The specific criteria that defines a *quality lead* is different for every organization. For more
> information, see [Define a quality lead].

A quality leads *report* compares how many quality leads each salesperson has received over a
specific amount of time, such as within the past 30 days. Sales managers can use such a report to
make more informed decisions when assigning new leads to their team

> **Tip:**
> > A sales manager pulls a quality leads report using their company’s criteria:
> >
> > - Leads must include a phone number and an email address.
> > - The email address must be from a professional domain.
> > - The source for the lead must be from a live chat conversation or an appointment with a
> >   salesperson.
>
> After running the report, the manager can see that, although everyone’s ability to close a deal
> has varied, some members of the sales team have received a higher number of quality leads than
> others.
>
> > ![An example of a quality leads report in the Odoo CRM application.](../../../../_images/example-report.png)
> >
> > Using this information, the sales manager may decide to assign more quality leads to the sales
> > people currently on the lower end, to balance out the distribution of quality leads.

## Create a quality leads report

To create a quality leads report, first navigate to CRM app ‣ Reporting ‣
Pipeline to open the Pipeline Analysis dashboard. Click into the Search…
bar at the top of the page and remove any active filters.

Click the 🔻(triangle pointed down) icon to the right of the Search… bar
to open the drop-down mega menu that contains Filters, Group By, and
Favorites columns. Click Add Custom Filter. This opens a Add
Custom Filter pop-up window.

The Add Custom Filter pop-up window allows for the creation of more specific filters.

### Add custom filters

In order to generate a quality leads report, filters need to be created for the following
conditions:

- [Starting date]: limits results to those created within
  a specific time frame.
- [Specific sales teams]: limits results to only include
  leads for one or more sales teams. This filter is optional and should not be included if the is
  intended for the entire company.
- [Exclude unassigned leads]: excludes leads without an
  assigned salesperson.
- [Include archived leads]: ensures that both active and
  inactive leads are included in the results.
- [Add rules for quality leads]: includes or excludes
  results based on criteria that is specific to a company or sales team.

![An example of the Custom Filter pop-up window with all of the rules configured.](../../../../_images/configured-custom-rules.png)

An example of the *Custom Filter* pop-up window with all of the default rules configured.

#### Add a starting date filter

Begin by first defining the rule’s parameter with a date range, by clicking into the first field, on
the left of the row, and typing `Created On` in the Search… bar, or by scrolling
through the menu’s list to locate it.

In the rule’s operator drop-down menu, define the parameter further by selecting either:

- >= (greater than or equal to) to specify a start date and include all entries *after*
  that start date (as well as the initial value itself); or
- is between to more sharply define a time frame with a clear start and end date. All
  matching entries that fit within the defined start and end dates are included in the report.

With either option, use the pop-up calendar’s day and time pickers, in the far right field, to
define the respective date range. Setting these values concludes the creation of the first rule.

#### Add a sales team filter

> **Note:**
>
> This filter is optional. To view results for the entire company, do **not** add this filter.

To limit the results of the report to one or more sales teams, click New Rule. Next,
click the first field for the new rule, and type `Sales Team` in the Search… bar, or
scroll to search through the list to locate it.

In the rule’s second field, select is in from the drop-down menu. Selecting this
operator limits results to the sales teams selected in the next field.

Lastly, in the third field, select the desired sales team from the drop-down menu. Multiple teams
can be added in this field, where each parameter is treated with an “or” (e.g. “any”) operator in
the search logic.

#### Exclude unassigned leads

Next, add a New Rule. Then, click into the first field for the new rule, and type
`Salesperson` in the Search… bar, or scroll to search through the list to locate it.

In the rule’s second field, select is set from the drop-down menu. Selecting this
operator excludes any leads not assigned to a specific salesperson.

#### Include archived leads

> **Note:**
>
> This filter is also optional, as it adds archived (inactive) leads to the report, however it is
> recommended to include this since it pulls *all* assigned leads, regardless of status, into the
> report. This ensures a more accurate representation of assigned leads is captured. However, to
> pull a report that only includes active leads, do **not** activate this feature.

Next, in the upper-right corner of the Add Custom filter pop-up window, move the
Include archived toggle to active.

![The Add Custom Filter pop-up with emphasis on the Include Archived toggle.](../../../../_images/include-archived.png)

Enabling this feature adds archived (inactive) leads to the report.

#### Add rules for quality leads

The filters added in this step vary, based on how an organization defines a *quality lead*.

##### Define a quality lead

As defined earlier, a *quality lead* is a lead that is likely to result in a won opportunity.
Although the exact criteria for a quality lead varies from organization to organization, it is often
a combination of factors commonly attributed to positive sales outcomes, in addition to factors
valued by the specific organization.

In addition to the basic filters and grouping options outlined in the general [Quality leads
report], consider the following filters when defining a
quality lead:

- Email or Phone: the information in these fields can help determine whether
  or not a lead is a professional contact.
- Source: this field links to the marketing and lead generation efforts from other Odoo
  applications, including *Live Chat*, *Social Marketing*, and *Email Marketing*.
- Stage: this filter can be used to eliminate or target leads that have reached specific
  stages.
- Medium: a lead’s source can indicate its quality level, as various channels have
  different won rates and expected revenues.
- Campaign: adding this filter helps track of the success of different marketing efforts
  to capture high quality leads.
- Lost Reason: exclude leads that may appear to be quality based on various criteria,
  but have been marked as *lost* for specified reasons.
- Tags: include or exclude results based on one or more customized tags.

> **Note:**
>
> When adding rules to a custom filter, keep the statements preceding each rule in mind. The
> statement above a rule determines whether the search results must match **all** of the rules
> below the statement, or **any** of the rules below the statement.
>
> ![Close up of the match rule options on a add custom filter pop-up window.](../../../../_images/match-all-match-any.png)

## View the report

> **Warning:**
>
> At the top of the Add Custom Filter form, there is an option to match any
> or all of the rules. In order to properly run the report, only records that match
> **all** of the following filters should be included. Before adding the filters, make sure
> all is selected in this field.
>
> ![Close up on the match all rules option on the add a custom filter pop-up window.](../../../../_images/match-all-rules.png)

After the filters are configured, click Add. The default display for the report is a bar
graph, where the leads are grouped by *stage*.

To group the results by salesperson, click the 🔻(triangle pointed down) icon to the
right of the Search… bar to open the drop-down mega menu. Under the Group
By heading, select Salesperson. In the same column, under the Group By
heading, click Add a Custom Group, then select Active on the resulting
drop-down menu to layer in lead *status*, under the parent Salesperson grouping.

The report now displays the total count of *quality leads* each salesperson has received in the
designated time period. Because there are layered Group By filters, the grouped leads
are also color-coded to identify whether they are *active* or *marked as lost*.

> **Note:**
>
> To save this search for later, click the 🔻(triangle pointed down) icon next to the
> Search… bar to open the drop-down menu. Under the Favorites heading,
> click Save current search.
>
> In the drop-down menu, rename the report from the default `Pipeline` label to `Quality Leads`,
> and click Save.

---

# Resellers

Within Odoo’s **CRM** app, leads can be forwarded to resellers (or partners). Leads can be manually
assigned, or automatically assigned, based on the resellers’ designated *level* and location.

## Configuration

To utilize the reseller features, the *Resellers* module first needs to be installed. Navigate to
the Apps application, and remove the Apps filter from the
Search… bar. Then, search for `Resellers`.

![The resellers module in Odoo.](../../../../_images/resellers-module.png)

Click Install on the Resellers module card that appears. Doing so installs
the module, and returns to the main Odoo dashboard.

After the module is installed, navigate to the CRM app. Under the
Configuration menu is a new section, titled Members, with three options
beneath it: Levels, Partner Activations, and Commission Plans.

## Levels

Partner *levels* are used to differentiate between various resellers. To view the levels, navigate
to CRM app ‣ Configuration ‣ Levels.

On the Levels page that appears, there are three default levels:

- Gold
- Silver
- Bronze

New levels can be added, as needed, by clicking New, and filling out the resulting level
form.

Existing levels can also be edited and renamed, if desired, as well. To modify a level, select it
from the list, and proceed to make any desired changes from the level form page that appears.

Level Weight is used to decide the probability a partner to be assigned a lead or
opportunity. On the level form, assign a numerical value (greater than zero) to the Level
Weight field. If the weight is zero, no leads are assigned.

> **Note:**
>
> *Level Weight* can be assigned on an individual contact record. The weight assigned on the
> individual record overwrites the default weight assigned on the level configuration form.

## Partner activations

Partner *activations* are used to identify the status of a partner. Activations are assigned on an
individual contact record, and can be used to group or filter the *Partnership Analysis* report
(CRM app ‣ Reporting ‣ Partnerships).

To view the partner levels, navigate to CRM app ‣ Configuration ‣ Partner
Activations.

Three activation types are created by default in the **CRM** app:

- Fully Operational
- Ramp-up
- First Contact

New partner activations can be added, as needed, by clicking New, and entering a
Name on the new line that appears. Then, select the desired status in the
Active column.

Existing partner activations can also be edited and renamed, if desired. To rename a status, click
the Name field of a desired level, and enter a new name.

To change the active status of an activation, slide the toggle in the Active column of
the desired activation to the *inactive* position.

![The list of default partner activations in the CRM app.](../../../../_images/activations-toggle.png)

## Partner assignments

After [levels] and [partner activations]
configured.

To update an individual partner record, navigate to CRM app ‣ Sales ‣
Customers, and click the Kanban card for the desired partner to open the customer record.

On the customer record, click the Partner Assignment tab.

Click the Partner Level field, and select an option from the drop-down menu to assign a
level. Click the Activation field, and select a partner activation type from the
drop-down list, if desired. Then, click the Level Weight field to assign a different
level weight, if necessary.

## Publish partners

With the Odoo **Website** and **Resellers** apps installed, a new webpage (`/partners`) is created
to display a list of all active partners from the **CRM** app.

Next, return to CRM app ‣ Sales ‣ Customers, and click the Kanban card for a
partner. From that partner’s contact form, click the Go to Website smart button at the
top of the page to open that partner’s webpage.

Next, click Edit at the top-right of the partner’s webpage, and use the [building
blocks](../../../websites/website/web_design/building_blocks.html) to add any additional design
elements, or information about the partner.

> **Note:**
>
> A company summary is a useful addition to this page.

After making any necessary changes to the page, click Save. At the top of the page,
slide the Unpublished toggle to the active, Published position, if needed.

Repeat these steps for all partners.

![An example of the partners webpage, displaying available partners by level and location.](../../../../_images/partners-webpage.png)

---

# Marketing attribution reports

Use the Odoo *CRM* app to compile a *marketing attribution report*, which analyzes the source of
leads, and groups them in such a way as to calculate marketing’s overall impact on lead generation,
attribution, won rate, and more.

## Leads Analysis dashboard

Begin by navigating to the Leads Analysis dashboard by going to CRM app
‣ Reporting ‣ Leads.

> **Note:**
>
> Reports can also be run on the CRM app ‣ Leads dashboard, which is **only**
> accessible if the *Leads* feature has been activated on the *Settings* page.
>
> If the *Leads* feature has **not** been activated, the CRM app ‣ Sales ‣ My
> Pipeline dashboard can also be used to run reports.
>
> Both dashboards contain the necessary *Filters* and *Group By* criteria to run an attribution
> report.

> **Note:**
>
> - [Convert leads into opportunities](../acquire_leads/convert.html)
> - [Create leads](../acquire_leads/email_manual.html)

![Open the CRM app and click on the Reporting tab at the top of the page, then click Leads.](../../../../_images/reporting-tab-and-leads.png)

The  (graph) view is shown, by default, with Active or
Inactive and Created on: [current year] filters active in the Search…
bar. The graph visualization displays the number of leads generated, by month and by sales team,
with each sales team attributed to its own color per month shown.

Switch the view to the  (list) option, by clicking the respective
icon located at the top-right of the dashboard. This allows leads to easily be displayed in the
grouping set by the *Group By* parameters.

![Click the button with four horizontal lines on the top right of the Leads Analysis page.](../../../../_images/list-view-button.png)

## Add UTM parameters

*Urchin Tracking Modules (UTMs)* are snippets of text embedded in URLs that are used to track
visitor data. This includes parameters relating to how a visitor reached the link, such as the type
of website visited, and/or marketing campaign the visit came from.

Odoo can use these UTMs as parameters in the marketing attribution report to track the metrics and
performance of marketing campaigns.

### Create UTMs

The [link tracker](../../../websites/website/reporting/link_tracker.html) in Odoo can be used to
create and configure UTMs.

UTMs can also be automatically generated by the [Email Marketing](../../../marketing/email_marketing.html) and [Marketing Automation](../../../marketing/marketing_automation.html) apps.

The UTM parameters used in a marketing attribution report are *Medium*, *Source*, and *Campaign*, in
descending order of coverage.

- *Medium* is the UTM with the widest coverage, and is used to identify the medium used to access
  the link. This can include mediums such as social media, email, or cost per click (CPC).
- *Source* is more narrow, and is used to identify the source of traffic. For example, the name of
  a website, search engine used, or a specific social media platform.
- *Campaign* is the most narrow, and can track specific marketing campaigns by name. This can
  include a contest or product name, type of sale, etc.

## Create reports

To start creating a report, click the  (down arrow) to the right of
the Search… bar to see the list of filtering and grouping parameters.

Filters, located in the left column of the search options, can be used to keep only the
results that fit the filter. For example, selecting the Won filter only shows leads that
have been won in the attribution report.

Group By, found in the middle column, is used to organize the results into groups, and
can be used with or without filters.

![Select any number of filters and groups in the search options.](../../../../_images/search-results-multiple-options.png)
> **Note:**
>
> Setting multiple Group By options creates nested groups, according to which option
> is selected first. For example, selecting Medium, followed by Source,
> and then Campaign, in Group By column, sorts all results *first* by
> medium, *then* by the specific sources in each medium, followed by the campaigns in each source.
>
> This can be verified by looking at the direction, and order, of the selections in the group tile
> that appears in the Search… bar.
>
> ![The text in the tile is `Country > City`, showing that city is a subgroup of country.](../../../../_images/group-by.png)

> **Tip:**
>
> For a useful first report:
>
> #. From the Filters column, select the Active filter to view only leads
> that are still marked as active.
> #. From the Group By column, select (in this specific order) Source,
> followed by the City or Country, depending on which grouping is more
> relevant.
>
> ![Each lead is now sorted by source, followed by city or country.](../../../../_images/campaign-and-country-groups.png)
>
> This report contains all active leads, grouped first by the source of the lead, then by the
> city or country each lead is from. This is useful to see the density of active opportunities
> sorted by location.
>
> With this data, marketing campaigns, such as conferences or billboards, can be targeted to the
> locations generating the largest amount of potential revenue. Similarly, more attention can be
> put toward increasing outreach in locations where existing marketing campaigns are less
> effective.

## Export reports

To set the measures of the report, begin by navigating to the
(pivot view) on the Leads Analysis dashboard.

Click the Measures button to view the available measures of
the report. Select the desired measures from the drop-down menu (multiple measures can be selected),
and verify the measures, filters, and groups are all displayed correctly in the pivot table. This
ensures the data is ready for export.

To quickly export the data in a list, as a .xlsx file, navigate to the
(list view). Click on the Actions  (gear) icon,
located to the right of Lead Analysis in the top-left of the page, and click
 Export All. The report downloads automatically as a .xlsx file.

For more export options, the report can be exported to the Odoo *Documents* app. From the
 (list view) of Leads Analysis page, begin by clicking
the Actions  (gear) icon again. Now, navigate to
 Spreadsheet, and click  Insert list in
spreadsheet. A pop-up window titled, Select a spreadsheet to insert your list. appears.

The report can be renamed using the `Name of the list` field, if desired. The number of items on the
report can be set with the field labeled: `Insert the first _ records of the list`. Next, select
either a new Blank spreadsheet, or export into an existing spreadsheet. Finally, click
the Confirm button.

![Set the name, number of records, and location of the export in the option menu.](../../../../_images/documents-export.png)

To export the report as a .xlsx file, for use in an external spreadsheets program, click the
Actions  (gear) icon, and select the
Export All option. If prompted, choose a file location, name the file, then click
Save.

---

# Lead distribution report

A *lead distribution report* can be used to see if active leads are being assigned equitably
across sales members. It can also be used to view the distribution of good or [quality leads](quality_leads_report.html), and see how frequently each salesperson is receiving (and keeping) leads.

Lead distribution reports can be run each week to help keep salespeople on track, while
providing them with ample good leads. These reports can also be used to see whether sales members
are staying productive, if good leads are being lost too often by one salesperson, and what
percentage of good leads are being retained overall.

## Create lead distribution reports

To create a lead distribution report, first navigate to CRM app ‣ Reporting ‣
Pipeline, which reveals the Pipeline Analysis dashboard.

Remove all the default filters in the search bar at the top of the page. Doing so
displays data related to *all* leads.

[Custom filters](../../../essentials/search.html#search-custom-filters) can now be added by clicking the
(down caret) icon, to the right of the search bar, to reveal a drop-down menu of search
and filter options.

Three columns are displayed: [Filters](../../../essentials/search.html#search-filters), [Group By](../../../essentials/search.html#search-group), and
[Favorites](../../../essentials/search.html#search-favorites). To begin, navigate to the bottom of the Filters
column, and click Add Custom Filter. This opens an Add Custom Filter pop-up
window, where the essential filters can be added one at a time.

### Essential filters

The following filter conditions are used to create a basic lead distribution report. Together they
gather all leads created within a certain timespan that have an associated contact method and have
been assigned to a sales team.

#### Lead creation date

Click the first field, under Match any of the following rules:, that has the value
Country in it. In the popover that appears, type `Created on` in the search bar, or
scroll to search through the list to locate and select it.

Then, in the second field of that row, select >= from the drop-down menu. This operator
**only** includes values greater than (or equal to) the value in the third, rightmost field.

The third field on the Add Custom Filter pop-up window should contain the earliest date
leads are selected from.

For example, setting `01/01/2024 00:00:00` only includes leads created from, and including, the
first day of 2024.

![Add a Created On rule for the start of the year onward.](../../../../_images/created-on.png)

#### Sales team

Click New rule to add another row to the form, and choose Sales Team for
this rule’s parameter. Then, click the second field of the new rule, and select contains
from the drop-down menu. Selecting this operator filters for any records that contain the words in
the third, rightmost field.

> **Note:**
>
> For certain pre-determined, limited choices like a sales team, the is in operator
> helps make for an easier and more accurate selection, via a drop-down menu in the third field,
> instead of risking a typo or incorrect value in the text box field that accompanies the
> contains operator.

In this third field, enter the name of the desired sales team(s) that are to be included in the
report. It is important for all contains argument values to be specific enough and
spelled correctly as they exist in Odoo, otherwise this risks returning multiple (or zero) values.

![Use Sales Team to filter the location the lead is associated with.](../../../../_images/sales-team-location.png)
> **Warning:**
>
> By adding more than one rule to the form, a new option emerges at the top of the pop-up window
> above all the filters, to specify whether any  or
> all  of the conditions should match. This distinction is
> important to set correctly, as it impacts the driving logic of how the filters return data.

Click the default any  menu item and be sure the all
 option is chosen instead. This setting will **only** show records that match
*all* the rules contained inside the form.

#### Contact method

> **Note:**
>
> The instruction below is not necessary, however, it’s highly recommended to add a set contact
> value to the report’s search criteria. A lot of spam, duplicate, or low quality leads can easily
> be screened out of the report simply by adding either a set Phone or
> Email rule.

Add another New rule to the form and set the first field to the first field to
Phone. Then, select is set from the drop-down menu in the second field.
Selecting this operator **only** filters for records that have a phone number associated with the
lead.

Alternatively (or in addition to the above rule), click New rule and set the first field
to Email. Then, select is set from the drop-down menu in the second field.

These rules add only leads with an associated contact method to the report.

#### Active status

Click the  (Add branch) icon to the right of the `Phone is set` line,
to add a new rule that branches from the rules above.

Two horizontal sets of fields appear below a line showing any
of: option. This setting filters for records that match **any** of the rules contained
inside. This uses the same logic as an OR (`|`) logical operator.

Set the first field to Active. Then, select is set in the next field.

Next, click the  (Add New Rule) button next to Active is set
to create a new line of fields beneath it.

Set the first field to Active. Then, select is not set in the next field.

![Use Active to include active status in the report.](../../../../_images/active-set.png)

This rule adds the activity status of the lead to the report.

> **Note:**
>
> Active status is an important filter to include when creating a lead distribution report because
> it includes **all** leads regardless of won/lost or active/inactive status in the report. This
> provides a comprehensive view of all the leads assigned to each sales member.

#### Group by

Once all filters are set, click the Add button to add these filters to the search bar.
To have the report grouped appropriately, click the  (down caret)
icon, to the right of the search bar, and click Salesperson in the Group
By section. All results are now grouped by the salesperson assigned to each lead.

Once the rules for the filter are set, click the purple Confirm button at the bottom of
the pop-up menu to save the custom filter and close the pop-up menu.

The Pipeline Analysis dashboard is now displayed again with each filter rule in the
search bar.

Click the  (Graph) icon, to the right of the search bar, to view
the report as a bar chart. Alternatively, click the  (List) icon to
view leads in a grouped list.

> **Note:**
>
> To save the filter so it can easily be re-applied, click the Save current search
> button in the Favorites section of the search bar drop-down menu.
>
> Next, type a name for the filter in the text box below. Check the Shared checkbox to
> have the filter shared with any user with access to the pipeline. Finally, click the purple
> Save button below to save the filter.
>
> The filter will now appear with the name it was given under the Favorites section of
> the drop-down menu and can be re-applied by clicking on it.

### Filter for quality leads

The following additional conditions are provided as an example of a *good*, but *not comprehensive*,
set of rules for finding quality leads. These filters should be applied on top of the
[Essential filters] in the order specified to achieve a heavily-detailed
filter.

- **Referred-by:** Filter for referrals, such as by appointment or sales member.
- **Source:** Filter for specific source UTMs, such as Facebook or LinkedIn.
- **Notes:** Filter for internal notes.
- **Tags:** Filter for categorical tags.
- **Email:** Filter for specific email domains, such as gmail.com or yahoo.com.
- **Salesperson:** Filter for leads associated with certain sales members.

These conditions can be added, removed, or modified to best fit the desired information in the
report.

> **Note:**
>
> - [Add rules for quality leads](quality_leads_report.html#quality-leads-report-add-quality-rules)
> - [Search, filter, and group records](../../../essentials/search.html)

---

# Analyze performance

---

# Pipeline Analysis

The *CRM* app manages the sales pipeline as leads/opportunities move from stage to stage,
origination to sale (**Won**) or archival (**Lost**).

After organizing the pipeline, use the search options and reports available on the *Pipeline
Analysis* page to gain insight into the effectiveness of the pipeline and its users.

To access the *Pipeline Analysis* page, go to CRM app ‣ Reporting ‣ Pipeline.

![Open the CRM app and click on the Reporting tab along the top, then click Pipeline.](../../../../_images/reporting-tab-and-pipeline-view.png)

## Navigate the pipeline analysis page

Upon accessing the Pipeline Analysis page, a bar graph showcasing the leads from the
past year automatically populates. The bars represent the number of leads in each stage of the sales
pipeline, color-coded to show the month the lead reached that stage.

![The default state of the Pipeline Analysis page is a graph, with many options to change it.](../../../../_images/pipeline-analysis-page.png)

The interactive elements of the Pipeline Analysis page manipulate the graph to report
different metrics in several views. From left-to-right, top-to-bottom, the elements include:

- Actions: represented by the ⚙️ (gear) icon, located next to the
  Pipeline Analysis page title. When clicked, a drop-down menu appears with three
  options, each with their own sub-menu: Knowledge, Dashboard,
  Spreadsheet. (See [Save and share reports] for more
  information)

  - The Knowledge option is for linking to or inserting the graph in a *Knowledge* app
    article.
  - The Dashboard option is for adding the graph to a dashboard in the *Dashboards* app.
  - The Spreadsheet option is for linking the graph in a spreadsheet in the *Documents*
    app.
- Search… bar: shows the filters and groupings currently being applied to the graph.
  To add new filters/groups, type them into the search bar, or click the ⬇️ (down arrow)
  icon, at the end of the bar, to open a drop-down menu of options. (See [Search Options] for more information)

In the upper-right corner, there are view options represented by different icons. (See [View
Options] for more information)

- Graph view: displays the data in a bar graph. This is the default view.
- Pivot view: displays the data in a customizable, categorized metrics table.
- Cohort view: displays and organizes the data, based on their Created on
  and Closed Date week (default), day, month, or year.
- List view: displays the data in a list.

Located on the far-left side of the page, beneath the Pipeline Analysis page title,
there are more configurable filter and view options.

- Measures: opens a drop-down menu of different measurement options that can be seen in
  the graph, pivot, or cohort view. The Measure drop-down menu is not available in the
  list view. (See [Measurement Options] for more information)
- Insert in Spreadsheet: opens a pop-up window with options for adding a graph or pivot
  table to a spreadsheet in the *Documents* app or a dashboard in the *Dashboards* app. This option
  is not available in the cohort or list view.

With the graph view selected, the following options are available:

- Bar Chart: switches the graph to a bar chart.
- Line Chart: switches the graph to a line chart.
- Pie Chart: switches the graph to a pie chart.
- Stacked: when selected, the results of each stage of the graph are stacked on top of
  each other. When not selected, the results in each stage are shown as individual bars.
- Descending: re-orders the stages in the graph in descending order from left-to-right.
  Click the icon a second time to deselect it. Depending on the search criteria, this option may not
  be available.
- Ascending: re-orders the stages in the graph in ascending order from left-to-right.
  Click the icon a second time to deselect it. Depending on the search criteria, this option may not
  be available.

With the pivot view selected, the following options are available:

- Flip Axis: flips the X and Y axis for the entire table.
- Expand All: when additional groupings are selected using the ➕ (plus
  sign) icons, this button opens those groupings under every row.
- Download xlsx: downloads the table as an Excel file.

### Search options

The Pipeline Analysis page can be customized with various filters and grouping options.

To add new search criteria, type the desired criteria into the search bar, or click the
⬇️ (down arrow) icon, next to the search bar, to open a drop-down menu of all options.
See the sections below for more information on what each option does.

![Clicking on the down arrow next to the search bar opens a menu of filters for the analysis.](../../../../_images/search-panel-filters-and-group-by-options.png)

FiltersGroup ByComparisonFavorites

The Filters section allows users to add pre-made and custom filters to the search
criteria. Multiple filters can be added to a single search.

- My Pipeline: show leads assigned to the current user.
- Opportunities: show leads that have been qualified as opportunities.
- Leads: show leads that have yet to be qualified as opportunities.
- Active: show active leads.
- Inactive: show inactive leads.
- Won: show leads that have been marked **Won**.
- Lost: show leads that have been marked **Lost**.
- Created On: show leads that were created during a specific period of time. By
  default, this is the past year, but it can be adjusted as needed, or removed entirely.
- Expected Closing: show leads that are expected to close (marked **Won**) during
  a specific period of time.
- Date Closed: show leads that were closed (marked **Won**) during a specific
  period of time.
- Archived: show leads that have been archived (marked **Lost**).
- Add Custom Filter: allows the user to create a custom filter with numerous
  options. (See [Add Custom Filters and Groups] for more
  information)

The Group By section allows users to add pre-made and custom groupings to the
search results. Multiple groupings can be added to split results into more manageable chunks.

> **Warning:**
>
> The order that groupings are added affects how the final results are displayed. Try
> selecting the same combinations in a different order to see what works best for each use
> case.

- Salesperson: groups the results by the Salesperson to whom a lead is assigned.
- Sales Team: groups the results by the Sales Team to whom a lead is assigned.
- City: groups the results by the city from which a lead originated.
- Country: groups the results by the country from which a lead originated.
- Company: groups the results by the company to which a lead belongs (if multiple
  companies are activated in the database).
- Stage: groups the results by the stages of the sales pipeline.
- Campaign: groups the results by the marketing campaign from which a lead
  originated.
- Medium: groups the results by the medium (Email, Google Adwords, Website, etc.)
  from which a lead originated.
- Source: groups the results by the source (Search engine, Lead Recall,
  Newsletter, etc.) from which a lead originated.
- Creation Date: groups the results by the date a lead was added to the database.
- Conversion Date: groups the results by the date a lead was converted to an
  opportunity.
- Expected Closing: groups the results by the date a lead is expected to close
  (marked “Won”).
- Closed Date: groups the results by the date a lead was closed(marked “Won”).
- Lost Reason: groups the results by the reason selected when a lead was marked
  “Lost.”
- Add Custom Group: allows the user to create a custom group with numerous
  options. (See [Adding Custom Filters and Groups] for more
  information)

The Comparison section allows users to add comparisons to the same search criteria
over another period of time.

This option is only available if the search includes time-based filters, such as
Created On, Expected Closing, or Date Closed. While
multiple time-based filters can be added at once, only one comparison can be selected at a
time.

- Previous Period: adds a comparison to the same search criteria from the previous
  period.
- Previous Year: adds a comparison to the same search criteria from the previous
  year.

The Favorites section allows users to save a search for later, so it does not need
to be recreated every time.

Multiple searches can be saved, shared with others, or even set as the default for whenever
the Pipeline Analysis page is opened.

- Save current search: save the current search criteria for later.

  - Default filter: when saving a search, check this box to make it the default
    search filter when the Pipeline Analysis page is opened.
  - Shared: when saving a search, check this box to make it available to other
    users.

#### Add custom filters and groups

In addition to the pre-made options in the search bar, the Pipeline Analysis page can
also utilize custom filters and groups.

Custom filters are complex rules that further customize the search results, while custom groups
display the information in a more organized fashion.

**To add a custom filter:**

1. On the Pipeline Analysis page, click the down arrow icon next to the
   Search… bar.
2. In the drop-down menu, click Add Custom Filter.
3. The Add Custom Filter pop-up window appears with a default rule (Country
   is in \_\_\_\_\_) comprised of three unique fields. These fields can be edited to make a custom rule,
   and multiple rules can be added to a single custom filter.
4. To edit a rule, start by clicking the first field (Country), and select an option
   from the drop-down menu. The first field determines the primary subject of the rule.
5. Next, click the second field, and select an option from the drop-down menu. The second field
   determines the relationship of the first and third fields, and is usually an **is** or **is not**
   statement, but can also be **greater than or less than** statements, and more.
6. Finally, click the third field, and select an option from the drop-down menu. The third field
   determines the secondary subject of the rule.
7. With all three fields selected, the rule is complete.

   - **To add more rules:** click New Rule and repeat steps 4-7, as needed.
   - **To delete a rule:** click the 🗑️ (trash) icon to the right of the rule.
   - **To duplicate an existing rule:** click the ➕ (plus sign) icon to the right of
     the rule.
   - **To create more complex rules:** click the Add branch icon to the right of the
     rule. This adds another modifier below the rule for adding an “all of” or “any of” statement.

![The add branch feature allows the creation of more complex all or any statements for rules.](../../../../_images/custom-filter-add-branch.png)

8. Once all rules have been added, click Add to add the custom filter to the search
   criteria.

   - **To remove a custom filter:** click the ✖️ (x) icon beside the filter in the
     search bar.

**To add a custom group:**

1. On the Pipeline Analysis page, click the down arrow icon next to the
   search bar.
2. In the drop-down menu that appears, click Add Custom Group.
3. Scroll through the options in the drop-down menu, and select one or more groups.

   - **To remove a custom group:** click the ✖️ (x) icon beside the custom group in the
     search bar.

### Measurement options

By default, the Pipeline Analysis page measures the total Count of leads
that match the search criteria, but can be changed to measure other items of interest.

To change the selected measurement, click the Measures button on the top-left of the
page, and select one of the following options from the drop-down menu:

- Days to Assign: measures the number of days it took a lead to be assigned after
  creation.
- Days to Close: measures the number of days it took a lead to be closed (marked
  **Won**).
- Days to Convert: measures the number of days it took a lead to be converted to an
  opportunity.
- Exceeded Closing Days: measures the number of days by which a lead exceeded its
  Expected Closing date.
- Expected MRR: measures the Expected Recurring Revenue of a lead.
- Expected Revenue: measures the Expected Revenue of a lead.
- Prorated MRR: measures the Prorated Monthly Recurring Revenue of a lead.
- Prorated Recurring Revenues: measures the Prorated Recurring Revenues of a lead.
- Prorated Revenue: measures the Prorated Revenue of a lead.
- Recurring Revenues: measures the Recurring Revenue of a lead.
- Count: measures the total amount of leads that match the search criteria.

### View options

After configuring filters, groupings, and measurements, the Pipeline Analysis page can
display the data in a variety of ways. By default, the page uses the graph view, but can be changed
to a pivot view, cohort view, or list view.

To change the pipeline to a different view, click one of the four view icons, located in the
top-right of the Pipeline Analysis page.

Graph ViewPivot ViewCohort ViewList View

The graph view is the default selection for the Pipeline Analysis page. It
displays the analysis as either a: bar chart, line chart, or pie chart.

This view option is useful for quickly visualizing and comparing simple relationships, like
the Count of leads in each stage, or the leads assigned to each
Salesperson.

By default, the graph measures the Count of leads in each group, but this can be
changed by clicking the Measures button, and [selecting another option] from the resulting drop-down menu.

![The Graph View displays the analysis as a Bar Chart, Line Chart, or Pie Chart.](../../../../_images/graph-view.png)
> **Note:**
>
> When using a bar chart in this view, consider deselecting the Stacked option,
> in order to make the breakdown of results more legible.

The pivot view displays the results of the analysis as a table. By default, the table groups
the results by the stages of the sales pipeline, and measures Expected Revenue.

The pivot view is useful for analyzing more detailed numbers than the graph view can handle,
or for adding the data to a spreadsheet, where custom formulas can be set up, like in an Excel
file.

![The Pivot View displays the analysis as a table.](../../../../_images/pivot-view2.png)

The three icons at the top-left of the page perform the following functions:

- Flip Axis: flips the X and Y axis for the entire table.
- Expand All: when additional groupings are selected using the ➕ (plus
  sign) icons, this button opens those groupings under every row.
- Download xlsx: downloads the table as an Excel file.

> **Note:**
>
> The Stage grouping cannot be removed, but the measurement can be changed by
> clicking the Measures button, and selecting another option.

The cohort view displays the analysis as periods of time (cohorts) that can be set to days,
weeks, months, or years. By default, Week is selected.

This view option is useful specifically for comparing how long it has taken to close leads.

![The Cohort View displays the analysis as individual weeks of the year.](../../../../_images/cohort-view.png)

From left-to-right, top-to-bottom, the columns in the chart represent the following:

- Created On: rows in this column represent the weeks of the year, in which
  records matching the search criteria exist.

  - When set to Week, a row with the label W52 2023 means the results
    occurred in: Week 52 of the Year 2023.
- Measures: the second column in the chart is the measurement of the results. By
  default, it is set to Count, but can be changed by clicking the
  Measures button, and selecting an option from the drop-down menu.
- Closed Date - By Day/Week/Month/Year: this column looks at what percentage of
  the measured results were closed in subsequent days/weeks/months/years.
- Average: this row provides the average of all other rows in the column.

The cohort view can also be downloaded as an Excel file, by clicking the Download
icon in the top-left of the page.

The list view displays a single list of all leads matching the search criteria. Clicking a
lead opens the record for closer review. Additional details such as Country,
Medium, and more can be added to the list, by clicking the Filters
icon in the top-right of the list.

This view option is useful for reviewing many records at once.

![The List View displays a single list of all records matching the search criteria.](../../../../_images/list-view1.png)

Clicking the ⚙️ (gear) icon opens the Actions drop-down menu, with options for the
following:

- Import records: opens a page for uploading a spreadsheet of data, as well as a
  template spreadsheet to easily format that data.
- Export All: downloads the list as an xlsx file for Excel.
- Knowledge: inserts a view of, or link to, the list in an article in the
  *Knowledge* app.
- Dashboard: adds the list to *My Dashboard* in the *Dashboards* app.
- Spreadsheet: links to, or inserts, the list in a spreadsheet in the *Documents*
  app.

> **Note:**
>
> On the list view, clicking New closes the list, and opens the *New Quotation*
> page. Clicking Generate Leads opens a pop-up window for lead generation.
> Neither feature is intended to manipulate the list view.

## Create reports

After understanding how to [navigate the pipeline analysis page], the
Pipeline Analysis page can be used to create and share different reports. Between the
pre-made options and custom filter and groupings, almost any combination is possible.

Once created, reports can be [saved to favorites, shared with other users, and/or added to
dashboards and spreadsheets].

A few common reports that can be created using the Pipeline Analysis page are detailed
below.

### Win/Loss reports

Win/Loss is a calculation of active or previously active leads in a pipeline that were either marked
as **Won** or **Lost** over a specific period of time. By calculating opportunities won over
opportunities lost, teams can clarify key performance indicators (KPIs) that are converting leads
into sales, such as specific teams or team members, certain marketing mediums or campaigns, and so
on.

\[\begin{equation}
Win/Loss Ratio = \frac{Opportunities Won}{Opportunities Lost}
\end{equation}\]

A win/loss report filters the leads from the past year, whether won or lost, and groups the results
by their stage in the pipeline. Creating this report requires a custom filter, and grouping the
results by Stage.

![The search criteria for win/loss reports is Created On, Stage, and Active is in true false.](../../../../_images/search-criteria-for-basic-win-loss.png)

Follow the steps below to create a win/loss report:

1. Navigate to CRM app ‣ Reporting ‣ Pipeline.
2. On the Pipeline Analysis page, click the ⬇️ (down arrow) icon, next to
   the search bar, to open a drop-down menu of filters and groupings.

   ![The Search menu containing the filters for a basic win/loss report.](../../../../_images/filters-for-basic-win-loss-report.png)
3. In drop-down menu that appears, under the Group By heading, click Stage.
4. Under the Filters heading, click Add Custom Filter to open another pop-up
   menu.
5. In the Add Custom Filter pop-up menu, click on the first field in the
   Match any of the following rules: section. By default, this field displays
   Country.
6. Clicking that first field reveals a sub-menu with numerous options to choose from. From this
   sub-menu, locate and select the Active option. Doing so automatically populates the
   remaining fields.

   The first field reads: Active. The second field reads: is. And lastly,
   the third field reads: set.

   In total, the rule reads: Active is set.
7. Click New Rule, change the first field to Active, and the last field to
   not set. In total, the rule reads Active is not set.
8. Click Add.

![The Add Custom Filter menu showing two rules: (1) Active is set, and (2) Active is not set.](../../../../_images/add-custom-active-filter.png)

The report now displays the total Count of leads, whether “Won” or “Lost,” grouped by
their stage in the CRM pipeline. Hover over a section of the report to see the number of leads in
that stage.

![A basic win/loss report showing all leads whether won or lost grouped by stage.](../../../../_images/basic-win-loss-report.png)

#### Customize win/loss reports

After [creating a win/loss report], consider using the options below to
customize the report for different needs.

> **Tip:**
>
> A sales manager might group wins and losses by salesperson, or sales team, to see who has the
> best conversion rate. Or, a marketing team might group by sources, or medium, to determine where
> their advertising has been most successful.

Filters and groupsPivot ViewList View

To add more filters and groups, click the ⬇️ (down arrow) icon, next to the search
bar, and select one or more options from the drop-down menu.

Some useful options include:

- Created on: adjusting this filter to a different period of time, such as the
  last 30 days, or the last quarter, can provide more timely results.
- Add Custom Filter: clicking this option, and scrolling through the numerous
  options in the drop-down menu, opens up additional search criteria, like Last
  Stage Update or Lost Reason.
- Add Custom Group > Active: Clicking Add Custom Group ‣ Active
  separates the results into **Won** (true) or **Lost** (false). This
  shows at what stage leads are being marked **Won** or **Lost**.
- Multiple Groupings: add multiple Group By selections to split
  results into more relevant and manageable chunks.

  - Adding Salesperson or Sales Team breaks up the total count of
    leads in each Stage.
  - Adding Medium or Source can reveal what marketing avenues generate
    more sales.

![The Search menu open and the Won and Lost filters highlighted.](../../../../_images/search-panel-filters-and-group-by-options.png)

By default, pivot view groups win/loss reports by Stage and measures
Expected Revenue.

To flesh out the table:

1. Click the ⬇️ (down arrow) next to the search bar.
2. In the pop-up menu, replace the Stage grouping with something like
   Salesperson or Medium.
3. Click the Measures button and click Count to add the number of
   leads back into the report.

   - Other useful measures for pivot view include Days to Assign and
     Days to Close.

![A win/loss report in Pivot View displays the data in table form.](../../../../_images/win-loss-pivot-view.png)
> **Warning:**
>
> In pivot view, the Insert In Spreadsheet button may be greyed out due to the
> report containing duplicate group bys. To fix this, replace the
> Stage grouping in the search bar with another option.

In list view, a win/loss report displays all leads on a single page.

To better organize the list, click the ⬇️ (down arrow) next to the search bar, and
add more relevant groupings or re-organize the existing ones. To re-order the nesting, remove
all Group By options and re-add them in the desired order.

To add more columns to the list:

1. Click the Filters icon in the top-right of the page.
2. Select options from the resulting drop-down menu. Some useful filters include:

   - **Campaign**: Shows the marketing campaign that originated each lead.
   - **Medium**: Shows the marketing medium (Banner, Direct, Email, Google Adwords, Phone,
     Website, etc.) that originated each lead.
   - **Source**: Shows the source of each lead (Newsletter, Lead Recall, Search Engine, etc.).

![A win/loss report in List View displays all leads in an easy-to-read list.](../../../../_images/win-loss-list-view.png)

## Save and share reports

After [creating a report], the search criteria can be saved, so the report
does not need to be created again in the future. Saved searches automatically update their results
every time the report is opened.

Additionally, reports can be shared with others, or added to spreadsheets/dashboards for greater
customization and easier access.

Save to FavoritesAdd to a SpreadsheetAdd to a Dashboard

To save a report for later:

1. On the Pipeline Analysis page, click the ⬇️ (down arrow) icon, next
   to the search bar.
2. In the drop-down menu that appears, under the Favorites heading, click
   Save current search.
3. In the next drop-down menu that appears, enter a name for the report.

   - Checking the Default filter box sets this report as the default analysis when
     the Pipeline Analysis page is accessed.
   - Checking the Shared box makes this report available to other users.
4. Finally, click Save. The report is now saved under the Favorites
   heading.

![Under the Favorites heading, click Save current search and save the report for later.](../../../../_images/save-to-favorites.png)

Inserting a report into a spreadsheet not only saves a copy of the report, it allows users to
add charts and formulas like in an Excel file.

To save a report as a spreadsheet:

- **In Graph or Pivot View**:

  1. Click the Insert in spreadsheet button.
  2. In the pop-up menu that appears, click Confirm.
- **In Cohort or List View**:

  1. Click the ⚙️ (gear) icon.
  2. In the drop-down menu that appears, hover over Spreadsheet.
  3. In the next drop-down menu, click either Insert in spreadsheet or
     Link in spreadsheet.

Saved reports are viewable in the *Documents* app.

> ![Pivot View reports especially benefit from being inserted in spreadsheets.](../../../../_images/pivot-view-in-spreadsheet.png)

> **Note:**
>
> After modifying a spreadsheet and adding additional formulas, consider then adding the
> entire spreadsheet to a dashboard. Using this method, the spreadsheet can be added to a
> public dashboard instead of only My Dashboard.
>
> 1. Click File ‣ Add to dashboard.
> 2. In the pop-up menu that appears, name the spreadsheet and select a Dashboard
>    Section to house the report.
> 3. Click Create.

Adding a report to a dashboard saves it for later and makes it easy to view alongside the rest
of My Dashboard.

To add a report to My dashboard:

1. On the Pipeline Analysis page, click the ⚙️ (gear) icon.
2. In the drop-down menu that appears, hover over Dashboard.
3. In the Add to my dashboard drop-down menu, enter a name for the report (by
   default, it is named Pipeline).
4. Click Add.

To view a saved report:

1. Return to the main apps page, and navigate to Dashboards app ‣ My
   Dashboard.

![To access the saved report, open the Dashboard app and click My Dashboard.](../../../../_images/add-to-dashboard.png)

> **Note:**
>
> - [Convert leads into opportunities](../acquire_leads/convert.html)
> - [Create and send quotations](../acquire_leads/send_quotes.html)
> - [Lost opportunities](../pipeline/lost_opportunities.html)

---

# Expected revenue report

*Expected revenue* is the total cash value of leads that are expected to close by a certain date,
usually the end of the current month.

An *expected revenue report* compiles all active leads in a sales pipeline that have a set expected
closing date, and compares how sales teams are performing in a given time frame.

![Close up of the expected closing date on a lead in the CRM app.](../../../../_images/expected-revenue-closing.png)

By pulling a monthly expected revenue report, sales managers can see which team members are reaching
their goals, and who may need additional assistance to close valuable deals.

## Create an expected revenue report

To create an expected revenue report, first navigate to CRM app ‣ Reporting ‣
Pipeline. This opens the Pipeline Analysis dashboard.

> **Warning:**
>
> The *Pipeline Analysis* dashboard includes several filters in the search bar by default. Remove
> these before adding any additional custom filters.

On the top-left of the report, click Measures, then select Expected Revenue
from the drop-down menu.

At the top of the page, click the 🔻(triangle pointed down) icon to the right of the
Search… bar to open the drop-down menu that contains Filters,
Group By, and Favorites columns. Under the Filters column, click
Add Custom Filter, which opens an Add Custom Filter pop-up window.

### Add custom filters

In order to generate an expected revenue report, filters need to be created for the following
conditions:

> - [Expected closing date]: limits results to only
>   include leads expected to close within a specific time frame.
> - [Exclude unassigned leads]: excludes leads
>   without an assigned salesperson.
> - [Specific sales teams]: limits results to only include
>   leads assigned to one or more sales teams. This filter is optional and should not be included if
>   the report is intended for the entire company.

#### Add filter for expected closing date

On the Add Custom Filter pop-up window, click into the first field of the new rule.
Type `Expected Closing` into the Search… bar, or scroll to select it from the list.
Click in the second field and select is set. This limits the results to only include
leads where an estimated closing date is listed.

Next, click the ➕ (plus) icon to the right of the rule to duplicate it.

> **Note:**
>
> Using the ➕ (plus) icon makes it easy to add multiple rules based on the same
> filter.

In the second field of the new rule, select is between from the drop-down menu. This
creates a set time frame during which the expected closing date must occur for leads to be included
in the results.

Click in each date field, one at a time, and use the calendar popover window to add both a start and
end date to the rule. This is usually the beginning and ending of the current month, or fiscal
quarter.

#### Exclude unassigned leads

After filtering for the expected closing date, add a New Rule. Then, click into the new
rule’s first field, and type `Salesperson` in the Search… bar, or scroll through the
list to select it. Click in the rule’s second field and select is set from the drop-down
menu. This excludes any results without an assigned salesperson.

#### Add a filter for sales teams

> **Note:**
>
> This filter is optional. To view results for the entire company, do **not** add this filter, and
> continue to [View results].

To limit the results of the report to one or more sales teams, click New Rule. Next,
click the first field for the new rule, and type `Sales Team` in the Search… bar, or
scroll to search through the list to locate it.

In the rule’s second field, select is in from the drop-down menu. Selecting this
operator limits results to the sales teams indicated in the next field.

Lastly, click into the third field, and either: make a selection from the complete list revealed in
the popover menu, or type the first few characters of the specific sales team’s title to quickly
find and select it as a parameter.

> **Note:**
>
> Multiple teams can be added to the `Sales Team` rule, where each parameter is treated with an
> “or” (e.g. “any”) operator in the search logic.

![Add Custom Filters pop-up window with custom filters configured for expected revenue report.](../../../../_images/custom-filters1.png)

## View results

At the top of the Add Custom Filter form, there is an option to match any or
all of the rules. In order to properly run the report, only records that match **all**
of the following filters should be included. Before adding the filters, make sure all is
selected in this field.

![Emphasis on the match all filters option on the Add Custom Filter pop-up window.](../../../../_images/match-all-filters.png)

At the bottom of the Add Custom Filter form, click Add.

### View options

The expected revenue report benefits from utilizing multiple views. The default graph view can be
used to identify which salespeople are expected to bring in the most revenue, while the list view
and pivot view provide more detail on specific deals.

Graph viewList viewPivot view

The *graph view* is used to visualize data, and is beneficial in identifying patterns and
trends.

*Bar charts* are used to show the distribution of data across several categories or among
several salespeople.

*Line charts* are useful to show changing trends over a period of time.

*Pie charts* are useful to show the distribution, or comparison, of data among a small number
of categories or salespeople, specifically how they form the meaningful part of a whole
picture.

The default view for the expected revenue report is the bar chart, stacked. To change to a
different graph view, click one of the icons at the top-left of the report. While both the
line chart and bar chart are available in stacked view, the pie chart is not.

![Close up view of the graph icons on the Pipeline analysis report in the CRM app.](../../../../_images/graph-view-icons.png)

Graph view icons in order: bar chart, line chart, pie chart, stacked.

The *list view* provides a list of all leads that are expected to close by the designated
date. Clicking on a lead in list view opens the record for detailed analysis, but many
insights can be gleaned from the basic view.

To switch to the list view, click the ≣ (list) icon at the top-right of the
report.

![Close up of the list view icon in the CRM app.](../../../../_images/list-icon.png)

To add additional metrics to the report, click the *additional options menu* indicated by the
toggle icon at the top-right of the list.

![Close up of the toggle icon in the CRM app.](../../../../_images/toggle-icon.png)

Clicking the toggle icon in *list view* opens the *additional options menu*.

Select any additional metrics from the drop-down menu to add them to the list view. Some
options that may be useful are Expected Closing and Probability.

The *pivot view* arranges all leads that are expected to close by the designated date into a
dynamic table.

To switch to the pivot view, click the Pivot icon at the top-right of the report.

![Close up of the pivot view icon in the CRM app.](../../../../_images/pivot-view-icon.png)

When the pivot view is selected for this report, the X-axis lists the stages in
the pipeline, while the Y-axis defaults to group the results by their creation date. To switch
these groupings, click the flip access icon (⇄) at the top of the report.

To add additional measures to the report, click the Measures button at the
top-left of the report. Select any additional metrics from the drop-down menu.

To add a group to a row or column to the pivot view, click the ➕ (plus sign) next
to Total, and then select one of the groups. To remove one, click the
➖ (minus sign) and de-select the appropriate option.

Click Insert in Spreadsheet to add the pivot view into an editable spreadsheet
format within the *Dashboards* app. If the Odoo *Documents* app is installed, the report can
be inserted into a blank or existing spreadsheet, and exported.

---

# Forecast report

The *Forecast* report in the *CRM* app allows users to view upcoming opportunities and build a
forecast of potential sales. Opportunities are grouped by the month of their expected closing date,
and can be dragged-and-dropped to adjust the deadline.

To access the *Forecast* report, navigate to CRM app ‣ Reporting ‣ Forecast.

## Navigate the forecast report

The default Forecast report includes opportunities assigned to the current user’s
pipeline, and are expected to close within four months. It also shows opportunities without an
assigned expected closing date. The opportunities are grouped by month in a
(Kanban) view.

![A sample version of the Forecast report in the CRM app.](../../../../_images/sample-report.png)

### Expected closing date

Opportunities are grouped by the date assigned in the *Expected Closing* field on an opportunity
form. To change this date directly from the Forecast page, select the Kanban card for
the desired opportunity, then click and drag the card to the desired column.

> **Note:**
>
> The default time frame for the forecast is *month*. This can be changed by clicking the  (down) icon
> next to the Search… bar at the top of the report. Under the Group By
> heading in the resulting drop-down menu, click Expected Closing to expand the list of
> available options, and select a desired amount of time from the list.

After an opportunity is added to a new month, the *Expected Closing* field on the opportunity form
is updated to the *last* date of the new month.

> **Note:**
>
> The *Expected Closing* field can also be manually updated on the opportunity card. To do that,
> click on the Kanban card for an opportunity on the Forecast page to open the
> opportunity’s detail form. Click in the Expected Closing field, and use the calendar
> popover to select a new closing date.

### Prorated revenue

The prorated revenue is the Expected Revenue amount that is displayed at the top of the
column for each month on the Forecast reporting page. This value is situated to the
right of the progress bar. The calculation for Expected Revenue is the total of the
prorated revenue specific to that particular time frame.

The prorated revenue is calculated using the formula below:

\[\text{Expected Revenue} \times \text{Probability} = \text{Prorated Revenue}\]

As opportunities are moved from one column to another, the column’s revenue is automatically updated
to reflect the change.

> **Tip:**
>
> A forecast report for June includes two opportunities:
>
> The first opportunity, `Global Solutions`, has an expected revenue of `$3,800`, and a probability
> of `90%`. This results in a prorated revenue of `$3,420`.
>
> The second opportunity, `Quote for 600 Chairs`, has an expected revenue of `$22,500`, and a
> probability of `20%`. This results in a prorated revenue of `$4,500`.
>
> The combined prorated revenue of the opportunities is `$7,920`, which is listed at the top of the
> column for the month.
>
> ![An example of the prorated revenue for one month of the forecast report.](../../../../_images/example-revenue.png)

> **Note:**
>
> For more information on how probability is assigned to opportunities, see
> [Assign leads with predictive lead scoring](../track_leads/lead_scoring.html)

## View results

Click the  (area chart) icon to change to graph view. Then, click
the corresponding icon at the top of the report to switch to a  (bar
chart),  (line chart), or  (pie
chart).

![A pie chart view of the Forecast report.](../../../../_images/pie-chart-view.png)

Click the  (pivot) icon to change to the pivot view, or the  (list) icon to change to the list view.

> **Note:**
>
> The [pivot view](../../../essentials/reporting.html#reporting-using-pivot) can be used to view and analyze data in a more
> in-depth manner. Multiple measures can be selected, and data can be viewed by month, and by
> opportunity stage.
>
> ![A sample of the forecast report in the pivot view.](../../../../_images/pivot-view1.png)

> **Note:**
>
> To save this report as a *favorite*, see [Favorites](../../../essentials/search.html#search-favorites).

---

# Optimize your Day-to-Day work

---

# Partner autocomplete

*Partner autocomplete* is an In-App Purchase (IAP) service that enriches business contacts with
information and data about that business. In any app or module where a *Contacts* form is
encountered, a business’s name can be entered into the Customer field (`partner_id`
technical field) and a suggested company can be chosen from the drop-down menu. With *partner
autocomplete*, valuable information and hard-to-find data about companies of all sizes is just a
click away.

The information provided by partner autocomplete can include general information about the business
(including full business name and logo), Phone number, Email, Tax
ID, address, and UNSPSC activities as Tags.

When getting a company’s contact information make sure to be aware of the latest EU regulations. For
more information about General Data Protection Regulation refer to: [Odoo GDPR](http://odoo.com/gdpr).

> **Warning:**
>
> Partner autocomplete only works for newly created company Contacts. Businesses that already exist
> in the **Contacts** app cannot be enriched, nor can contacts for people.

## Configuration

Go to Settings app ‣ Contacts section. If the Partner Autocomplete
feature isn’t active, tick the checkbox beside it and click Save to activate it.

![View of settings page and the activations of the feature in Odoo.](../../../../_images/settings-partner-autocomplete.png)

## Enrich contacts with corporate data

When *partner autocomplete* is enabled, Odoo displays a drop-down menu of potential match
suggestions based on the name entered in the new contact form. If one of the suggestions is
selected, the contact is populated with relevant data.

![Creating a new contact in Odoo with the Partner Autocomplete feature suggesting possible businesses.](../../../../_images/odoo-autocomplete.png)

## Pricing

As an IAP service, *Partner Autocomplete* requires prepaid credits for
each use. Each completed autocomplete request consumes one credit. Enterprise Odoo users with a
valid subscription receive complimentary credits to try out IAP features for free before purchase.
This includes demo and training databases, educational databases, and one-app-free databases.

To buy credits, confirm that Partner Autocomplete is enabled as above, then navigate to
the **Settings** app and go to the Contacts section. Then, click
Manage Service & Buy Credits under Partner Autocomplete. On the
Partner Autocomplete page, click  Buy Credit and the
IAP page loads. Choose a package and click Buy to begin the payment process.

> **Note:**
>
> If the database runs out of credits, the only information populated when clicking on the
> suggested company will be the website link and the logo.
>
> Learn about our [Privacy Policy](https://iap.odoo.com/privacy).

> **Note:**
>
> [In-app purchases (IAP)](../../../essentials/in_app_purchase.html)

---

# CRM Gamification

In Odoo’s *CRM* app, *gamification tools* provide the opportunity to evaluate and motivate users
through customizable challenges, goals, and rewards. Goals are created to target actions within the
*CRM* app, and can be tracked and rewarded automatically to participating sales teams.

## Configuration

To install the *CRM Gamification* module, navigate to the Apps application. Click
into the Search… bar at the top of the page and remove the Apps filter.
Type `CRM Gamification` to search.

On the CRM Gamification module, click Install. This module features goals
and challenges related to the *CRM* and *Sales* applications.

![View of the gamification module being installed in Odoo.](../../../../_images/gamification-module-install.png)
> **Note:**
>
> If **both** the *CRM* and *Sales* apps are installed, the *CRM Gamification* module is
> automatically installed on the database.

To access the *Gamification Tools* menu, first enable [Developer mode (debug mode)](../../../general/developer_mode.html#developer-mode).

Next, navigate to Settings app ‣ Gamification Tools.

![View if the gamification tools menu in Odoo Settings.](../../../../_images/gamification-tools-menu.png)

## Create badges

*Badges* are awarded to users when they have completed a challenge. Different badges can be awarded
based on the type of task completed, and can be issued to more than one user, depending on the time
they accomplish the goal.

To view the existing badges, or create a new one, navigate to Settings ‣
Gamification Tools ‣ Badges.

![View of the badges page in Odoo.](../../../../_images/badges2.png)
> **Note:**
>
> Some badges can be awarded outside of challenges, as well. Select the Kanban card for the desired
> badge, then click Grant. This opens a Grant Badge pop-up window. Select
> a user from the Who would you like to reward? field.
>
> Add any additional information regarding why the user is receiving the reward in the field below,
> then click Grant Badge.

To create a new badge, click New at the top-left of the page to open a blank form.
Enter a name for the Badge, followed by a description.

The Allowance to Grant field determines when a badge can be granted, and by whom:

- Everyone: this badge can be manually granted by any user.
- A selected list of users: this badge can only be granted by a select group of users.
  If this option is selected, it generates a new field, Authorized Users. Choose the
  appropriate users from this drop-down list.
- People having some badges: this badge can only be granted by users who have already
  been awarded a specific badge. If this option is selected it generates a new field,
  Required Badges. Use this drop-down list to select the badge(s) a user must have
  before they can award this badge to others.
- No one, assigned through challenges: this badge cannot be manually granted, it can
  only be awarded through challenges.

To limit the number of badges a user can send, tick the Monthly Limited Spending
checkbox. This sets a limit on the number of times a user can grant this badge. In the
Limitation Number field, enter the maximum number of times this badge can be sent per
month, per person.

![The details page for a new badge.](../../../../_images/create-badge.png)

## Create a challenge

To create a challenge, navigate to to Settings ‣ Gamification Tools ‣
Challenges. Click New in the top-left corner to open a blank challenge form.

At the top of the form, enter a Challenge Name.

### Create assignment rules

To assign the challenge to specific users, one or more assignment rules must be utilized.

Click into the first field under Assign Challenge to, and select a parameter from the
drop-down list to define the rule. Then, click into the next field to define the rule’s operator. If
necessary, click into the third field to further define the parameter.

> **Note:**
>
> To include all users with permissions in the *Sales* app, create a rule with the following
> parameters:
>
> - Groups
> - is in
> - `Sales/User: Own Documents Only`
>
> ![View of the assignation rules section of a Challenge form.](../../../../_images/assignation-rule.png)

In the Periodicity field, select a time frame for goals to be automatically assessed.

### Add goals

Challenges can be based on a single goal, or can include multiple goals with different targets. To
add a goal to the challenge, click Add a line on the Goals tab.

In the Goal Definition field, choose a goal from the drop-down list. The
Condition field automatically updates to reflect the condition set on the goal
definition.

> **Note:**
>
> The *CRM Gamification* module contains preconfigured goals geared towards salesteams:
>
> - New Leads
> - Time to Qualify a Lead
> - Days to Close a Deal
> - New Opportunities
> - New Sales Orders

Enter a Target for the goal based on the Suffix.

Repeat these steps for each additional goal.

![The goals tab of a challenge form.](../../../../_images/challenge-goals.png)

### Add rewards

Next, click the Reward tab. Choose the [badges] to be awarded
For 1st User and For Every Succeeding User by selecting them from the
drop-down lists.

> **Note:**
>
> Badges are granted when a challenge is finished. This is either at the end of a running period,
> at the end date of a challenge, or when the challenge is manually closed.

After setup is complete, click the Start Challenge button at the top-left of the page to
begin the challenge.

---

# CRM activities and activity plans

Within the *CRM* app, *activities* are follow-up tasks tied to *leads* and *opportunities* that are
visible in the chatter. A set of preconfigured activity types is available in the *CRM* app, but
custom activity types may also be created to suit business needs. To view the list of available
activity types in the *CRM* app, open the app and navigate to Configuration ‣
Activity Types. This page shows both Odoo-created activities and any custom activities.

> **Note:**
>
> Different applications support different activity types. To see the complete list of activity
> types, go to the Settings app, then scroll to the Discuss section,
> and click the Activity Types link.

## Default and custom activity types

The preconfigured activity types for the *CRM* app are:

> - Email: Adds a reminder to the chatter prompting the salesperson to send an email.
> - Call: Opens a calendar link where the salesperson can schedule a phone call.
> - Meeting: Opens a calendar link where the salesperson can schedule a meeting.
> - To Do: Adds a general reminder task to the chatter.
> - Upload Document: Adds a link on the activity where an external document can be
>   uploaded. Note that the *Documents* app is **not** required to utilize this activity type.

> **Note:**
>
> If other Odoo applications are installed, such as *Sales* or *Accounting*, additional activity
> types may appear in the *CRM* app’s *Activity Types* page.

### Create a custom activity type

To create a custom activity type, navigate to the *Activity Types* page and click New at
the top-left of the page to open a blank form. Start by entering a Name for the new
activity type.

![The Activity Type form in its totality.](../../../../_images/activity-type-form.png)

#### Activity settings

##### Action

The *Action* field specifies what action the activity prompts from the salesperson assigned to the
opportunity. Some actions trigger specific behaviors after an activity is scheduled instead of when
the activity is added to an opportunity.

- If Upload Document is selected, a link to upload a document is added directly to the
  planned activity in the chatter.
- If either Phonecall or Meeting are selected, users have the option to open
  their calendar to schedule a time for this activity.
- If Request Signature is selected, a link is added to the planned activity in the
  chatter that opens a signature request pop-up window.

> **Note:**
>
> The actions available for an activity type may vary depending on the applications currently
> installed in the database.

##### Default user

To automatically assign this activity to a specific user when this activity type is scheduled,
choose a name from the Default User drop-down menu. If this field is left blank, the
activity is assigned to the user who creates the activity.

##### Default summary

The Default Summary serves as the title for activities when choosing them on
opportunities and leads. These will be visible to users such as salespeople and managers, whereas
the Name at the top of an Activity Type form is how the activity appears
within the *CRM* app’s configuration.

##### Schedule

Set a default deadline for the custom activity in the Schedule field. To do so,
configure the desired number of days, weeks, or months. Then,
decide if the deadline should occur after previous activity completion date or
after previous activity deadline.

> **Note:**
>
> The default setting of after previous activity deadline means the date the deadline
> is set for, regardless of whether or not the deadline was actually met. To ensure that an
> activity is scheduled only when the preceding activity is complete, use the after
> previous activity completion date option.

##### Default Note

To include notes whenever this activity type is created, enter them into the Default
Note field. This can be used to include instructions for another user, as in the sample text in
this field.

> **Note:**
>
> The information in all of the preceding fields is automatically included when an activity is
> created within an opportunity. However, the info can still be altered before the activity is
> scheduled or saved.

#### Next activity

To automatically suggest or trigger a new activity after an activity has been marked complete, the
Chaining Type must be set.

##### Suggest the next activity

If an activity has the Chaining Type set to Suggest Next Activity, and has
activities listed in the Suggest field, users are presented with recommendations for
activities as next steps.

![The next activity section with the Chaining Type set to Suggest Next Activity.](../../../../_images/suggest-next-activity.png)

In the Chaining Type field, select Suggest Next Activity. Upon doing so, the
field underneath changes to: Suggest. Click the Suggest field drop-down menu
to select any activities to recommend as follow-up tasks to this activity type.

##### Trigger the next activity

When an activity has the Chaining Type set to Trigger Next Activity, marking
the activity as *Done* immediately launches the next activity listed in the Trigger
field.

Setting the Chaining Type to Trigger Next Activity immediately launches the
next activity once the previous one is completed.

If Trigger Next Activity is selected in the Chaining Type field, the field
beneath changes to: Trigger. From the Trigger field drop-down menu, select
the activity that should be launched once this activity is completed.

![The next activity section with the Chaining Type set to Trigger Next Activity.](../../../../_images/trigger-next-activity.png)

##### Email templates

Select or create an email template to be suggested when the activity is added to an opportunity. The
template will appear alongside the activity in the chatter and can be sent as-is or edited by a
user.

## Activity tracking

To keep the pipeline up to date with the most accurate view of the status of activities, as soon as
a lead is interacted with, the associated activity should be marked as *Done*. This ensures the next
activity can be scheduled as needed. It also prevents the pipeline from becoming cluttered with
past-due activities.

The pipeline is most effective when it is kept up-to-date and accurate to the interactions it is
tracking.

## Activity plans

*Activity plans* are preconfigured sequences of activities. When an activity plan is launched, every
activity in the sequence and any activities set to trigger off of activities within the sequence are
scheduled automatically.

To create a new plan, navigate to CRM app ‣ Configuration ‣ Activity Plans.
Click New at the top-left of the page to open a blank Lead Activity Plans
form.

Enter a name for the new plan in the Plan Name field. On the Activities To
Create tab, click Add a line to add a new activity.

Select an Activity Type from the drop-down menu. Click Search More to see a
complete list of available activity types, or to create a [new one].

Next, in the Summary field, either leave this blank to use activity’s *Default Summary*
or enter a new summary of what the activity entails. Entering a new summary does not overwrite an
existing Default Summary. The contents of this field are included with the scheduled activity, and
can be edited later.

In the Assignment field, select one of the following options:

> - Ask at launch: Activities are assigned to a user when the plan is scheduled. By
>   default, they will be assigned to the user creating the activity, even if they’re not the user
>   responsible for the opportunity the activity is being created on.
> - Default user: Activities are always assigned to a specific user.

If Default user is selected in the Assignment field, choose a user in the
Assigned to field.

> **Note:**
> > Activity plans can feature activities that are assigned to default users and users assigned at
> > the plan launch.
>
> ![A blank Lead Activity Plan form.](../../../../_images/create-activity-plan.png)

Next, configure the timeline for the activity. Activities can be scheduled to occur either before
the plan date or after. Scheduling activities before the plan date can be useful for activities
scheduled in the future that require some preparation beforehand. Use the Interval and
Units fields to set the deadline for this activity. Lastly, in the Trigger
field, select whether the activity should occur before or after the plan date.

> **Tip:**
>
> An activity plan is created to handle high priority leads. Specifically, these leads should be
> contacted quickly, with a meeting scheduled within two days of the initial contact. The plan is
> configured with the following activities:
>
> - Email two days **before** plan date
> - Meeting zero days **before** plan date
> - Make quote three days **after** plan date
> - Upload document three days **after** plan date
> - Follow-up five days **after** plan date
>
> This sets the *plan date* as the meeting deadline, which is the objective of the plan. Before
> that date, there is lead time to contact the customer and prepare for the meeting. After that
> date, the salesperson has time to create a quote, upload the document, and follow-up.

Repeat these steps for each activity included in the plan.

### Use an activity plan

To use an activity plan with a *CRM* opportunity, navigate to CRM app and click on
the Kanban card of an opportunity to open it.

Above the opportunity’s chatter, click Activity to open the Schedule
Activity pop-up window.

In the Plan field, select the desired activity plan to launch from the section above the
individual activities. This generates a Plan Summary, listing out the activities
included in the plan. Select a Due Date using the calendar popover. This automatically
updates the Plan summary with deadlines based on the intervals configured in the
[activity plan].

Select a user in the Responsible field. This user is assigned to any of the activities
on the plan that were configured with Ask at launch in the Assignment field.

![The schedule activity pop-up window with an Activity plan selected.](../../../../_images/schedule-activity-plan.png)

Click Schedule. The details of the plan are added to the Planned Activities
section of the chatter, in addition to each of the activities that make up the plan.

![The chatter thread of a CRM opportunity with a launched activity plan.](../../../../_images/activity-plan-chatter.png)
> **Note:**
>
> - [Activities](../../../essentials/activities.html)
> - [Email templates](../../../general/companies/email_template.html)

---

# Lead enrichment

*Lead enrichment* is an In-App Purchase (IAP) service that provides business information for a
contact attached to a lead. Using lead enrichment requires credits and is available for existing
leads in an Odoo database. Enterprise Odoo users with a valid subscription receive free credits to
test IAP. This applies to demo/training, educational, and one-app-free
databases.

The information provided by lead enrichment can include general information about the business
(including full business name and logo) and its size, revenue, social media accounts, known
technology use, and more.

The *Leads* feature [must be configured](../acquire_leads/convert.html#crm-configure-leads) in the **CRM** app’s settings
page in order to use lead enrichment.

![Chatter showing lead enrichment data.](../../../../_images/lead-enrichment-data.png)
> **Warning:**
>
> When collecting a company’s contact information, be aware of the latest EU regulations. For more
> information about the General Data Protection Regulation, refer to the [Odoo GDPR](http://odoo.com/gdpr).

## Lead enrichment set up

To set up lead enrichment in the **CRM** app, navigate to CRM app ‣ Configuration
‣ Settings. Under the Lead Generation section, select the checkbox next to
Lead Enrichment, and select either Enrich leads on demand only or
Enrich all leads automatically. Click the Save button to activate the
changes.

![The CRM lead generation settings page with lead enrichment activation highlighted and enrich leads on demand only chosen.](../../../../_images/lead-enrichment-activate.png)

## Automatic and manual enrichment

Lead enrichment is based on the customer’s email domain set on the lead. There are two different
ways that a lead can be enriched: *automatically* or *manually*.

### Automatically enrich leads

On the *Settings* page, if *Enrich all leads automatically* was selected, no user action is required
to enrich the lead. Once every 60 minutes, a scheduled action contacts a remote database and
enriches any unenriched leads.

To change the behind-the-scenes rules for automatic lead enrichment, activate [developer mode](../../../general/developer_mode.html#developer-mode). With developer mode active, type “scheduled actions” in the main Odoo dashboard
to bring up the  (Search for a menu) screen. Click Settings
/ Technical / Automation / Scheduled Actions to navigate to the Scheduled Actions page. In the
search bar, type “enrich leads” and click the CRM: enrich leads IAP action. From this
page, automatic lead enrichment can be changed, including the execution interval, priority, and
more. The minimum value for the Execute Every field is 5 minutes.

### Manually enrich leads

If *Lead Enrichment* is set to Enrich leads on demand only, leads must be manually
enriched. This is done by clicking the Enrich button in the lead’s page top menu. This
retrieves the same information as automatic enrichment at the same cost (one credit per enrichment).
This method of enrichment is useful when not every lead needs to be enriched or when cost is an
issue.

Multiple leads can be manually enriched in a single step using the *list* view. First, navigate to
the CRM app ‣ Leads, then click the  (List)
button. Click the checkboxes for the leads that need manual enrichment. Finally, click the
 (Actions) icon, then select Enrich from the resulting
drop-down menu. Multiple leads can also be enriched at once from the *My Pipeline* and *Pipeline*
pages. To do so, open the **CRM** app. On the *My Pipeline* page, click the
(Remove) icon in the search bar to show the entire pipeline, if desired. Then click the
 (List) button to switch to the list view and select the leads
to enrich.

## Pricing

Lead enrichment is an In-App Purchase (IAP) feature, and each enriched lead costs one credit. If the
database has no available credits, only the lead’s website and logo are provided during enrichment.
Pricing information for credits can be found on the [Lead Generation](https://iap.odoo.com/iap/in-app-services/167) page.

To buy credits, navigate to CRM app ‣ Configuration ‣ Settings. In the
Lead Generation section, under the Lead Enrichment feature, click on
Manage Service & Buy Credits.

> **Note:**
>
> Because credits are not interchangeable between IAP services, clicking the Manage
> Service & Buy Credits link under the Lead Mining sub-header does **not** lead to a
> web page where *Lead Enrichment* credits can be purchased.

Credits may also be purchased by navigating to the Settings app and scrolling to the
Contacts section. Under the Odoo IAP feature, click View My
Services. From there, every active IAP service in the database can be viewed and credits can be
purchased by selecting one and clicking the Buy Credit link.

![Buy credits in the Odoo IAP settings.](../../../../_images/view-my-services-setting1.png)
> **Note:**
>
> [In-app purchases (IAP)](../../../essentials/in_app_purchase.html)

---

# Membership / Partnership module

The Membership / Partnership module allows for the creation and sale of memberships. Memberships can
be sold through both sales orders and subscriptions products so that businesses can organize and
interact with customers as members. This allows for:

- measuring membership activity, inactivity, sign ups, and churn rates
- viewing membership renewals and expirations
- following up on membership dues and associated payments
- communicating with members, including sending email blasts based on members’ current status
- assigning different membership levels to members
- organizing members-only events
- creating membership lists populated with contact info and other details about members.

## The Membership / Partnership module vs. the Membership app

Beginning with 19.0, the **Membership** app has been replaced by the Membership / Partnership
module. This module captures all of the functionality of the **Membership** app, but in a module
that is better integrated with other essential apps without requiring a specific **Accounting**
module. This replacement does not break any existing membership information when upgrading to 19.0.

## App integrations with the Membership / Partnership module

Once activated, the Membership / Partnership module is fully integrated with both the **Sales** and
**Subscriptions** apps. The module is also compatible with the **eCommerce** app, allowing customers
to purchase memberships through business’s websites.

Finally, the Membership / Partnership module is compatible with pricelists both before and after
sales. Price rules can be set before memberships are sold and applied after they are active.

## Activating the new module

The Memberships / Partnerships module can be activated within the **CRM** app. To activate the
Memberships / Partnerships module, go to CRM app ‣ Configuration ‣ Settings. In
the CRM section, check the Membership / Partnership box to activate the
module. The name given to affiliates can also be customized. By default, it is set to `Members`.

> **Note:**
>
> - [Sales](../../sales.html)
> - [Subscriptions](../../subscriptions.html)
> - [CRM](../../crm.html)
> - [Contacts](../../../essentials/contacts.html)
> - [Pricelists](../../sales/products_prices/prices/pricing.html)
> - [eCommerce](../../../websites/ecommerce.html)
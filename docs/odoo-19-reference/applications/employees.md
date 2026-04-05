# Employees — Contracts, Payroll & Appraisals

> **Odoo 19.0 Reference**
> Source: www.odoo.com/documentation/19.0 — HTML converted via markdownify

## Purpose

Employee records, contracts, departments, job positions, onboarding, offboarding, and retention reporting. Use when extending HR modules or configuring the employee lifecycle.

---

# Employees

Odoo **Employees** centralizes [personnel files](employees/new_employee.html), employment
[contracts](payroll/contracts.html), and [departmental hierarchies](employees/departments.html) in
one system. In addition, each employee record tracks [certifications](employees/certifications.html) and [training](employees/learning.html), earned [badges](employees/badges.html), and all assigned [equipment](employees/equipment.html). Customizable
[onboarding](employees/onboarding.html) and [offboarding](employees/offboarding.html) programs
ensure all employees are trained and ready for work, and all required steps are taken when they
leave.

Properly configuring the settings in the **Employees** app ensures the dashboard shows each
employee’s real-time attendance and work location—data that drives payroll accuracy, capacity
planning, and compliance reporting.

[#### New employees

Set up new employee records.](employees/new_employee.html)[#### Onboarding

Ensure new employees are properly trained and ready to work.](employees/onboarding.html)[#### Departments

Create and manage the departments employees are a part of.](employees/departments.html)[#### Learning

Create and manage virtual and in-person employee training.](employees/learning.html)[#### Contracts

Manage and create employee contracts.](payroll/contracts.html)[#### Certifications

Certify employees as subject-matter experts with certifications.](employees/certifications.html)[#### Badges

Grant badges to employees for performance and achievements.](employees/badges.html)[#### Equipment

Manage and track employee equipment.](employees/equipment.html)[#### Offboarding

Take care of employee records when collaboration ends.](employees/offboarding.html)[#### Employee retention report

Gain insight into a company’s retention rate.](employees/retention_report.html)

## Settings

To view and configure the available settings, navigate to Employees app ‣
Configuration ‣ Settings.

### Employees

- Presence Display: Select how the employee’s availability status is calculated.

  - Based on attendances: Employees are marked available when [checked into](attendances/check_in_check_out.html#attendances-check-in) the **Attendances** app.
  - Based on user status in system: Employees are marked available when they [log
    in to Odoo](attendances/check_in_check_out.html).
- Advanced Presence Control: When enabled, presence status can be calculated from
  operational signals rather than check-ins or logins:

  - Based on number of emails sent: An employee is marked present if they send at least
    # emails per hour; otherwise, they are marked absent. Enter the minimum number of emails that
    must be sent in the Sent Emails field.
  - Based on IP Address: An employee is marked present only when connected from one of
    the specified corporate IP addresses. Enter the IP addresses in the IP Addresses
    field, separating each address with a comma.
- Skills Management: Enable this option to display the [resumé tab](employees/new_employee.html#employees-resume) on employee profiles. This allows for the display of [work experience](employees/new_employee.html#employees-resume), [skills](employees/new_employee.html#employees-skills), and [certifications](employees/certifications.html).

### Work organization

Using the drop-down menu, select the default Company Working Hours. The default options
are a Standard 40 hours/week or an Appointment Resource Default Calendar.

The available working hours listed are the same as the configured [working schedules](payroll/working_schedules.html) in the **Payroll** app. Working hours can be created and modified from
both the **Payroll** and **Employees** apps.

### Contract

Define the number of days in advance that a manager is notified about an upcoming contract or work
permit expiration in the respective Contract Expiration Notice Period and
Work Permit Expiration Notice Period fields.

### Salary configurator

Define how long an offer remains valid when extending a job offer or changing a salary. Enter the
duration, in days, in the Salary Package Configurator field.

This field only appears if the **Salary Configurator** module is installed.

### Extra time off allocation

During salary package negotiations, enable the checkbox in this section if additional time off
requests are allowed. When enabled, select the [Time Off Type](time_off.html#time-off-time-off-types)
created for the additional days using the drop-down menu.

The default available options are Paid Time Off, Compensatory Days, and
Extra Time Off. If other time off types are configured in the **Time Off** app, they are
available in the drop-down menu.

This field only appears if the **Salary Configurator** module is installed.

---

# New employees

When a new employee is hired, the first step is to create a new employee record. This record is a
centralized place where all important information about the employee is stored, including
[general information], [job history and skills], [various work information], [personal
details], [payroll-related information], and
various [settings] that affect integrations with other apps in the
database.

To begin, open the Employees app, then click the New button in the
upper-left corner. Doing so reveals a blank employee form.

Proceed to fill out the required information, along with any additional details.

> **Note:**
>
> The employee form automatically saves as data is entered. However, the form can be saved manually
> at any time by clicking the  (Save manually) icon.

## General information

Fill out the following employee details in the top section of the employee form.

- Employee’s Name: Enter the employee’s name. This field is required.
- (Work Email): Enter the employee’s work email address.
- (Work Phone): Enter the employee’s work phone number.
- (Work Mobile): Enter the employee’s work mobile number.
- (Tags): Select any tags from the drop-down menu to add relevant tags to
  the employee. Any tag can be created in this field by typing it in. Once created, the new tag is
  available for all employee records. There is no limit to the amount of tags that can be added on
  an employee form.
- Photo: Upload a photo of the employee in the photo placeholder.

![The top-half of a new employee form, all filled out.](../../../_images/gen-info.png)

## Work tab

This tab is visible for all employees, and does not require any other apps to be installed.

### Work

- Company: Select the company the new employee was hired by using the drop-down menu, or
  create a new company by typing the name in the field, and clicking Create or
  Create and edit… from the mini drop-down menu that appears. This field is required,
  but only appears when in a multi-company database.
- Department: Select the employee’s department from the drop-down menu.
- Job Position: Select the employee’s job position from the drop-down menu. If using the
  **Recruitment** app, this list reflects configured job positions.
- Job Title: This field is automatically populated with the selection made in the
  Job Position field. Adjust the text, if desired, to best reflect the employee’s role.

  > **Tip:**
  >
  > Specific details can be added in the Job Title field, if desired.
  >
  > For example, a sales representative position configured as Sales Associate in the
  > **Recruitment** app can be selected for the Job Position field.
  >
  > The Job Title field can be more specific, such as `Sales Associate - Subscriptions`
  > if the employee is focused solely on subscription sales.
  >
  > ![Both job position fields entered but with different information.](../../../_images/job-title-fields.png)
- Manager: Select the employee’s manager using the drop-down menu.

### Location

- Work Address: Select the Work Address from the drop-down menu. The current
  company populates this field, by default. To modify the address, hover over the first line (if
  there are multiple lines) of the address to reveal an  (Internal
  Link) arrow. Click the  (Internal Link) arrow to open up the
  company form, and make any edits. Use the breadcrumb links to navigate back to the new employee
  form when done.

  If a new work address is needed, add the address by typing it in the field, then click
  Create (new address) to add the address, or Create and edit… to add the
  new address and edit the address form.
- Work Location: Select where the employee works using the drop-down menu. The default
  options are Home, Office, or Other.

  To add a new location, type in the location name, then click Create (new location) to
  add the location, or Create and edit… to add the location, assign a Work
  Address, and a Cover Image.

### Usual work location

This section states where the employee is expected to work on any given workday. Using the drop-down
menu for each day of the work week, select where the employee works that day. The selected location
is reflected on the employee’s Kanban card, indicating their location that day.

Use the drop-down menu to select the default location the employee works, for each day of the week.
The default options are Home, Office, or Other.

A new location can be typed into the field, then click either Create (new location) to
add the location, or Create and edit… to add the new location and edit the form.

After edits are done, click Save & Close, and the new location is added, and populates
the field.

Leave the field blank (Unspecified) for non-working days, such as Saturday and Sunday.

> **Note:**
>
> It is also possible to add or modify work locations by navigating to Employees
> app ‣ Configuration ‣ Work Locations. To modify a location, click on an existing location,
> then make any changes on the form.
>
> Click New to create a new location, then enter the following information on the form.
> All fields are **required**.
>
> - Work Location: Enter the name for the location. This can be as general or specific
>   as needed, such as `Home` or `Building 1, Second Floor`, respectively.
> - Work Address: Using the drop-down menu, select the address for the location.
> - Cover Image: Click on the icon to select it for the Cover Image.
>   Options are a  (home) icon, an
>   (building) icon, and a  (map marker) icon.
> - Company: Using the drop-down menu, select the company the location applies to. The
>   current company populates this field, by default. This field **only** appears in a
>   multi-company database.
>
> ![A new work location form with all fields filled out.](../../../_images/location.png)

### Note

Enter any relevant notes in this field.

### Organization chart

The related departments appear in this section, illustrating where in the company the employee
works.

> **Note:**
>
> After a Department is selected, the department’s configured manager automatically
> populates the Manager field.

> **Note:**
>
> To make edits to the selected Department, Manager, or
> Company, click the  (Internal link) arrow next to
> the respective selection. The  (Internal link) arrow opens the
> selected form, allowing for modifications. Click Save after any edits are made.

## Resumé tab

### Resumé

Enter the employee’s work history in the Resumé tab. Each resumé line must be entered
individually. When creating an entry for the first time, click Create Resume Lines, and
a *Create Resumé Line* form appears. After an entry is added, the Create Resume Lines
button is replaced with an ADD button. Enter the following information for each entry:

- Type: Click the corresponding button to reflect the *type* of experience being added.
  The available options are Other Experience, Education,
  Training, or Internal Certification.
- Title: Type in the title from the previous work experience.
- Duration: Enter the start and end dates for the work experience using the calendar
  module.
- Certificate: If there is a relevant certificate to attach, click the Upload
  your file button, select the desired file, and click Select. The file name appears in
  the field, not an image of the certificate.
- Description: Enter any relevant details in this field.

Once all the information is entered, click the Save & Close button if there is only one
entry to add, or click the Save & New button to save the current entry and create
another resumé line.

![A resumé entry form with all the information populated.](../../../_images/resume-lines.png)
> **Note:**
>
> After the new employee form is saved, the current position and company is automatically added to
> the Resumé tab, with the end date listed as `Current`.

### Skills & certifications

An employee’s skills and certifications can be entered in the Resumé tab in the same
manner that a resumé line is created.

To add a skill to an employee record, the skill type must first be configured. By default, Odoo
comes with two Skill Types preconfigured: *Languages* and *Soft Skills*.
[Configure the rest of the skill types] before adding any skills to the
employee record.

When adding the first skill to an employee record, a Pick a skill from the list button
appears in the Skills section of the Resumé tab. Click the Pick a
skill from the list button, and a blank *Update Skills* pop-up window loads. Configure the
following information for each skill:

- Category: Select a [skill type] by clicking it.
- Skill: After selecting the Category, all corresponding skills associated
  with that selected Category appear in individual buttons. For example, selecting
  Language as the Skill Type presents a variety of languages to select from
  in the Skills section. Click the appropriate preconfigured skill from the list.

  > **Warning:**
  >
  > If the desired skill does not appear in the list, it is **not** possible to add the new skill
  > from this window. New skills must be added from the [Skill Types]
  > dashboard.
- Skill Level: Pre-defined skill levels associated with the selected
  Category appear. Click on a Skill Level to select it. Skill levels can be
  created and modified from the [Skill Types] dashboard.

Click the Save & Close button if there is only one skill to add, or click the
Save & New button to save the current entry and immediately add another skill.

At any point, a new line can be added by clicking the ADD button.

![A skill form with the information filled out.](../../../_images/skills.png)
> **Warning:**
>
> Only users with Officer: Manage all employees or Administrator rights for
> the **Employees** app can add or edit skills.

#### Skill types

To add a skill to an employee’s form, the Skill Types must be configured. Navigate to
Employees app ‣ Configuration ‣ Skill Types to view the currently configured
skill types and create new skill types.

> **Note:**
>
> The default skill of Languages is preconfigured with twenty-one skills, and the
> default Soft Skills is preconfigured with fifteen skills.

Click the New button in the upper-left corner, and a new Skill Type form
loads. Fill out the following details for the new skill type. Repeat this for all the needed skill
types.

- Skill Type: Enter the name of the skill type. This acts as the parent category for
  more specific skills and should be generic.
- Color: Click on the existing color to view the available colors. Click the desired
  color to select it.
- Certification: Click the toggle to indicate the skill is a certification. The toggle
  turns green, indicating it is active and the skill can be added to the [certifications] tab.
- Skills: Click Add a line and enter the Name for the new skill,
  then repeat for all other needed skills.
- Levels: Click Add a line, and enter a Name and
  Progress percentage (`0`-`100`) for each level.

  Set a Default Level by clicking the toggle on the desired line (only one level can be
  selected). The toggle turns green to indicate the default level. Typically, the lowest level is
  chosen, but any level can be selected.

  > **Tip:**
  >
  > To add math skills in yellow, enter `Math` in the Skill Type field, and click the
  > colored circle next to Color, and select yellow. Then, in the Skills
  > field, enter `Algebra`, `Calculus`, and `Trigonometry`. Next, in the Levels field,
  > enter `Beginner`, `Intermediate`, and `Expert`, with the Progress listed as `25`,
  > `50`, and `100`, respectively. Click Set Default on the `Beginner` line to set this
  > as the default skill level.
  >
  > ![A skill form for a Math skill type, with all the information entered.](../../../_images/math-skills.png)

> **Note:**
>
> Once the form is completely filled out, click the  (Save
> manually) icon at the top of the screen, and the Levels rearrange in descending
> order, with the highest level at the top, and the lowest at the bottom, regardless of the default
> level and the order they were entered.

## Certifications tab

This tab houses all the employee’s certifications, which can be important for employees who are
required to hold specific certifications to perform their job, such as a CPA certification for accountants, or a CSM
certification for a construction manager.

The tab lists each Certification in a line, and displays the validity period in the
From and To fields.

> **Note:**
>
> This tab **only** appears if at least one [skill type] is configured
> as *certification*. When adding certifications, **only** skill types marked as a certification
> can be selected.

To add a certification, click Add a line in the *Certifications* tab and a blank *Create
Certification* pop-up window loads. Enter the following information on the form:

- Category: Click on the type of certification being added.
- Skill: Click on the specific skill for the certification.
- Skill Level: Click on the level the certification is for.
- Validity: Click into the two fields, and select the start and end dates for the
  certification, using the calendar selector.

When the form is complete, click Save & New to add the certification and add another, or
Save & Close to add the certification and close the pop-up window.

![The certification pop-up with everything configured for a C/C++ Advanced certification.](../../../_images/certifications.png)

## Personal tab

No information in the Personal tab is required to create an employee, however, some
information in this section may be necessary for the company’s payroll department.

In order to properly process payslips and ensure all deductions are accounted for, it is recommended
to check with the accounting department and payroll department to ensure all required fields are
populated. For example, to pay employees with direct deposit, they **must** have a trusted account
listed in the Bank Accounts field.

Enter the various information in the following sections and fields of the Personal tab.
Fields are entered either using a drop-down menu, ticking a checkbox, or typing in the information.

> > **Note:**
> >
> > Depending on the localization setting, other fields may be present. For example, for the United
> > States localization, a SSN No (Social Security Number) field is present.

### Private contact

- Email: Enter the employee’s personal email address.
- Phone: Enter the employee’s personal phone number.
- Bank Accounts: Enter the bank account number using the drop-down menu. If the bank
  account does not exist, [create a new bank account] and select it.

#### Add a bank account

When an employee is added to the database, their bank account must also be added. To add a new bank
account, type the account number into the Bank Accounts field in the *Personal* tab of
the employee form, then click Create and edit...

A *Create Bank Accounts* pop-up window loads with the bank account number populating the
Account Number field. Next, enter the Clearing Number (also referred to as a
*routing number*) in the corresponding field.

The employee’s name populates the Account Holder and Account Holder Name
fields by default, but can be updated if needed.

Next, select the Bank using the drop-down menu. If the bank is not already configured,
click Create and edit… and a blank *Create Bank* pop-up window loads, with the bank
name populating the Name field. Next, enter the Bank Identifier Code, also
referred to as a BIC or SWIFT code. If applicable, select the Intermediary Bank using
the drop-down menu. This bank acts as a facilitator between banks for international wire transfers,
when needed. Enter the Bank Address, Phone, and Email in the
corresponding fields. Once the form is complete, click Save, and the new bank populates
the Bank field.

Click the Send Money toggle. This changes the toggle color to green, and the status
changes from Untrusted in gray text, to Trusted in green text.

The Employee field is populated with the employee’s name, and cannot be modified.

Finally, add any relevant notes in the Note tab.

![The Create Bank Account form with all the information filled out.](../../../_images/bank.png)
> **Warning:**
>
> To ensure payments are processed and sent to the bank account, mark the bank account as
> Trusted. Having an Untrusted bank account for an employee causes an error
> in the **Payroll** application when processing direct deposits.
>
> If issuing paper checks or paying via cash, the Bank field does not need to be
> configured.

### Emergency contact

This section details the person to contact in the event of an emergency.

- Contact: Enter the emergency contact’s name.
- Phone: Enter the emergency contact’s phone number. It is recommended to enter a phone
  number that the person has the most access to, typically a mobile phone.

### Citizenship

This section outlines all the information relating to the employee’s citizenship. This section is
primarily for employees who are working in a different country than their citizenship. For employees
working outside of their home country, for example on a work visa, this information may be required.
Different fields may be visible, depending on the localization installed.

- Nationality (Country): Select the country the employee is from using the drop-down
  menu.
- Non-resident: Click this checkbox if the employee lives in a foreign country.
- Identification No: Enter the employee’s identification number in this field.
- SSN No: Enter the employee’s social security number.
- Passport No: Enter the employee’s passport number.

### Family

This section is used for tax purposes, and affects the **Payroll** app. Enter the following
information in the fields.

- Disabled: Check this box if the employee is considered legally disabled.
- Marital Status: Select the marital status for the employee using the drop-down menu.
  The default options are Single, Married, Legal Cohabitant,
  Widower, and Divorced.

  If Married or Legal Cohabitant is selected, two additional fields appear:
  Spouse Legal Name and Spouse Birthdate. Enter these fields with the
  respective information.
- Dependent Children: Enter the number of dependent children. This number is the same
  number used for calculating tax deductions, and should follow all tax regulations regarding
  applicable dependents.

### Documents

This section allows for uploading any relevant documents on the employee form. Click the
Upload your file button next to the corresponding document name, navigate to the file,
then click Select to upload the file.

The documents that can be uploaded are:

- ID Card Copy: Upload any relevant ID’s that may be required by the payroll or HR
  department.
- Driving License: Upload the employee’s driver’s license. This field may be necessary
  if the employee drives as part of their job, or is given a company car to use.
- SIM Card Copy: Upload a copy of the SIM card if the employee is using a work-issued
  mobile phone.
- Internet Subscription Invoice: If the employee is receiving benefits or compensation
  for their internet service, upload their invoice in this field.

  > **Note:**
  >
  > The Internet Subscription Invoice field is for documentation purposes only.
  > Employees must use the **Expenses** app to request reimbursement for expenses, or define
  > compensation in the *Payroll* tab.

### Personal information

This section houses information used for payroll and tax purposes.

- Legal Name: Enter the employee’s legal name in this field. By default, the name
  entered in the [general information section] populates this field.
  This is the name that typically is used for filing taxes.
- Birthday: Select the birthday of the employee using the calendar selector.
- Place of Birth: Enter the city or town the employee was born in the first field, and
  select the country using the drop-down menu.
- Gender: Select the employee’s gender from the drop-down menu. The default options are
  Male, Female, and Other.
- Payslip Language: Select the language used when printing the employee’s payslips.
  Each language must be [added to the database](../../general/users/language.html) to appear in the
  drop-down menu.

### Visa & work permit

This section should be filled in if the employee is working on some type of work permit or visa.
This section may be left blank if they do not require any work permits or visas for employment.

- Visa No: Enter the employee’s visa number. When entered, an Expires on
  field appears. Select the date the visa expires using the calendar.
- Work Permit No: Enter the employee’s work permit number. When entered, an
  Expires on field appears. Select the date the work permit expires using the calendar.
- Visa Expiration Date: Select the date the employee’s visa expires using the calendar.
- Document: Click Upload your file, then navigate to the work permit or visa
  file in the file explorer, and click Select to upload it.

  > **Note:**
  >
  > Typically, an employee needs either a visa *or* a work permit, not both. For this reason, only
  > one document can be added to the Document field.

### Location

This section is visible for all employees, and does not require any other apps to be installed for
this section to be visible. Enter the following information in this section:

- Private Address: Enter the employee’s home address in this field.
- Home-Work Distance: Enter the number, in miles or kilometers, the employee commutes to
  work, in one direction. The unit of measure can be changed from kilometers (km) to
  miles (mi) using the drop-down menu. This field is only necessary if the employee is
  receiving any type of commuter benefits or tax deductions based on commute distances.

### Education

This section allows for only one entry, and should be populated with the highest degree the employee
has earned.

- Certificate Level: Select the highest degree the employee has earned using the
  drop-down menu. The default options are Graduate, Bachelor,
  Master, Doctor, and Other.
- Field of Study: Type in the subject the employee studied, such as `Business` or
  `Computer Science`.

## Payroll tab

Depending on the installed [payroll localization](../payroll/payroll_localizations.html), the
sections and fields in this tab may vary considerably. Due to the specific nature of localizations
and the variety of information that may be requested in this tab, it is recommended to check with
the accounting department to fill out this section correctly.

The following fields are universal for all payroll localizations:

> **Note:**
>
> [Payroll localizations](../payroll/payroll_localizations.html)

### Contract overview

This section details all the various details from the employee contract. Refer to the
[contracts](../payroll/contracts.html) document for detailed information on creating and modifying
employee contracts.

### Employer costs

This section details the various costs the employer incurs for the employee, including:

- Yearly Cost: This field is automatically updated based on the Wage entered
  in the *Contract Overview* section, but can be modified, if needed. If it is modified, the
  Wage field updates to reflect the new Yearly Cost.
- Monthly Cost: This field automatically displays the monthly cost according to the
  Yearly Cost. This field cannot be modified.
- Wage on Signature: Enter the employee’s expected monthly wage according to the
  contract in this field.

### Schedule

This section defines when the employee is expected to work. Configure the following fields:

- Work Entry Source: Determine how the employee’s work entries are created in the
  **Payroll** app using the drop-down menu. Working Schedules is selected by default. If
  the **Attendances** or **Planning** apps are installed, their respective options are available.
- Working Hours: Select the hours the employee is expected to work, using the drop-down
  menu. By default, a Standard 40 hours/week working schedule is selected. If the
  **Timesheets** app is installed, an Appointment Resource Default Calendar option is
  also available.

  To view and modify the specific daily working hours, click the
  (Internal link) arrow at the end of the Working Hours line. Working hours
  can be modified or deleted here.

  > > **Note:**
  > >
  > > Working Hours are related to a company’s working schedules, and an employee
  > > **cannot** have working hours that are outside of a company’s working schedule.
  > >
  > > Each individual working schedule is company-specific. For multi-company databases, each company
  > > **must** have its own working hours set.
  > >
  > > If an employee’s working hours are not configured as a working schedule for the company, new
  > > working schedules can be added, or existing working schedules can be modified.
  > >
  > > Working hours can be modified in both the **Employees** and **Payroll** apps, where they are
  > > referred to as Working Schedules.
  > >
  > > For more information on how to create or modify Working Schedules, refer to the
  > > [working schedules](../payroll/working_schedules.html) documentation.
  > >
  > > After the new working time is created, or an existing one is modified, the Working
  > > Hours can be selected on the employee form.

## Salary adjustments tab

This *Salary Adjustments* tab houses all salary adjustments in a list view. Salary adjustments are
wage garnishments or voluntary portions of an employee’s payslip set aside each pay period.

Add each individual [salary adjustment](../payroll/salary_attachments.html#payroll-salary-adjustment-create) to this tab.

## Settings tab

This tab provides various fields for different applications within the database. Depending on what
applications are installed, different fields may appear in this tab.

### User

- User: Select a user in the database to link to this employee using the drop-down menu.

  > **Warning:**
  >
  > Employees do **not** need to be users of the database, and do **not** count towards the Odoo
  > subscription billing, while users **do** count towards billing. If the new employee should also
  > be a user, the user **must** [be created].
- Timezone: Select the timezone for the employee using the drop-down menu.

#### Create a user

After the employee is created, click the Create User button on the upper-left corner of
the employee record, and a *Create User* pop-up window appears.

The employee name populates the Name field by default. If the Email Address,
Phone, Company, and photo fields are populated on the employee
form, the corresponding fields are auto-populated on the *Create User* form.

Once the form is completed, click the Save button. The user is created, and populates
the Related User field.

Alternatively, select the  Invite teammates via email option that
appears in the User drop-down menu, and an *Invite teammates* pop-up window loads, with
the same fields as the *Create User* pop-up window. Fill out the form, then click Send
Invitation. An email invitation is sent to the user, informing them their account has been created.

Users can also be created manually. For more information on how to manually add a user, refer to the
[Users](../../general/users.html) document.

![The invite a user pop-up window, configured.](../../../_images/new-user1.png)

### Approvers

To see this section, the user must have either Administrator or Officer:
Manage all employees rights set for the **Employees** application. For the category to appear, the
respective app must be installed. For example, if the **Time Off** app is not installed, the
Time Off approver field does not appear. Only one selection can be made for each field.

> > **Warning:**
> >
> > The users that appear in the drop-down menu for the Approvers section **must** have
> > *Administrator* rights set for the corresponding human resources role.
> >
> > To check who has these rights, go to the Settings app and click
> >  Manage Users in the *Users* section. Then, click on an
> > employee and go to the Access Rights tab. Scroll to the *Human Resources* section
> > and check the various settings.
> >
> > - In order for the user to appear as an approver for Expenses, they **must** have
> >   either Team Approver, All Approver, or Administrator set
> >   for the Expenses role.
> > - In order for the user to appear as an approver for Time Off, they **must** have
> >   either Officer:Manage all Requests or Administrator set for the
> >   Time Off role.
> > - In order for the user to appear as an approver for Timesheets, they **must**
> >   have either Officer:Manage all contracts or Administrator set for the
> >   Payroll role.
> > - In order for the user to appear as an approver for Attendances, they **must**
> >   have Administrator set for the Payroll role.

- HR Responsible: Select the user responsible for validating the employee’s contracts
  using the drop-down menu.
- Expense: Select the user responsible for approving all expenses for the employee using
  the drop-down menu.
- Time Off: Select the user responsible for approving all time off requests from this
  employee using the drop-down menu.
- Timesheet: Select the user responsible for approving all the employee’s timesheet
  entries using the drop-down menu.
- Attendance: Select the user responsible for approving all attendance entries for the
  employee using the drop-down menu.

> **Note:**
>
> If any approver field is left empty, the approval is done by an Administrator or Approver.

### Application settings

This section affects the **Fleet** and **Manufacturing** apps. Enter the following information in
this section.

- Hourly Cost: Enter the hourly cost for the employee, in a `##.##` format. This cost is
  factored in when the employee is working at a [work center](../../inventory_and_mrp/manufacturing/advanced_configuration/using_work_centers.html).

  > **Note:**
  >
  > Manufacturing costs are added to the costs for producing a product if the value of the
  > manufactured product is **not** a fixed amount. This cost does **not** affect the **Payroll**
  > application.
- Fleet Mobility Card: If applicable, enter the Fleet Mobility Card number.
  This is typically a credit card for gas purchases or other vehicle-related costs.

### Appraisal

This field is **only** visible if the **Appraisals** application is installed.

- Next Appraisal Date: The date automatically populates the date of the next appraisal
  which is computed according to the settings configured in the **Appraisals** application. This
  date can be modified using the calendar selector.

### Planning

This section is **only** visible if the **Planning** app is installed, as this section affects what
the employee can be assigned in the **Planning** app.

- Roles: Select all the roles the employee can perform using the drop-down menu. There
  are no preconfigured roles available, so all roles must be [configured in the Planning app](../../services/planning.html#planning-roles). There is no limit to the number of roles assigned to an employee.
- Default Role: Select the default role the employee will typically perform using the
  drop-down menu. If the Default Role is selected before the Roles field is
  configured, the selected role is automatically added to the list of Roles.

### Attendance/Point of Sale/Manufacturing

This section determines how employees sign in to the **Attendances**, **Point Of Sale**, and
**Manufacturing** apps and only appears if any of those apps are installed.

- PIN Code: Enter the employee’s PIN code in this field. This code is used to sign in
  and out of **Attendances** app kiosks, the **Point Of Sale** app, and the **Manufacturing** app’s
  *Shop Floor* companion module.
- RFID/Badge Number: Click Generate at the end of the RFID/Badge
  Number line to create a unique number. Once generated, the number populates the
  RFID/Badge Number field, and Generate changes to Print Badge.
  Click Print Badge to create a PDF file of the employee’s badge. The badge can be
  printed and used to log into a POS system or [check in](../attendances/kiosks.html#attendances-kiosk-mode-entry) on an **Attendances** app kiosk.

  If the employee uses an RFID token or already has an ID badge issued with a barcode, click
  Read a badge and the system allows the barcode or RFID token to be read. Once read,
  the number populates the RFID/Badge Number field.
- Overtime Ruleset: Select the overtime rules to be used when calculating overtime for
  the employee using the drop-down menu.

---

# Onboarding

When a new employee is hired, it is important to have an onboarding procedure that can be followed.
This ensures that information, equipment, and training are provided to the employee and any other
necessary steps for the business are assigned to the correct individuals.

Proper onboarding ensures that new employees are given all the information and tools needed to be
successful in their roles and have a smooth transition to their new job.

> **Note:**
>
> Depending on the installed applications, additional steps may appear in the onboarding plan.

## View onboarding plan

Before onboarding can begin, it is recommended to check the default onboarding plan that comes
preconfigured with the **Employees** app. To view the current default plan, navigate to
Employees app ‣ Configuration ‣ Onboarding / Offboarding, then click
Onboarding to view the detailed onboarding plan form.

The plan form displays the following information:

- Plan Name: The specific name for the onboarding plan.
- Model: Specifies where this plan can be used. In this case, in the **Employees** app.
  This field cannot be modified.
- Department: If left blank (the default setting) this plan is available for all
  departments. Limit the use of the plan to a specific department by selecting the department using
  the drop-down menu.
- Activities To Create: This tab lists all the onboarding steps. Each row displays:

  - Activity Type: The specific activity for the step. The default options are
    To-Do, Email, Call, Meeting,
    Document, and Certifications. If the **Sign** app is installed, a
    Signature option is available.
  - Summary: A one line description of the step.
  - Assignment: Chooses who completes the activity, relative to the new hire:

    - Ask at launch: Choose the user in the Assigned To field when
      [launching the onboarding plan].
    - Default user: Choose a user who always handles this activity. Defined in the
      Assigned to field.
    - Coach: Assigns the employee’s coach as defined on the employee record.
    - Manager: Assigns the employee’s manager as defined on the employee record.
    - Employee: The new hire completes the activity.
    - Fleet Manager: Assigns the designated **Fleet** app manager. This option is only
      available if the **Fleet** app is installed.
  - Assigned to: This field remains blank, unless Default user is selected
    for the Assignment field. If Default user is selected, this field is
    populated with the selected user.
  - Interval: The time when the activity is active.
  - Unit: The set time interval, either days, weeks, or
    months.
  - Trigger: How scheduling is determined for the activity. Options are either
    Before Plan Date or After Plan Date.

    > **Tip:**
    >
    > A laptop must be set up and registered to a new employee the day before they start work. The
    > person who performs this step should always be the IT Manager, Abby Jones.
    >
    > To configure this activity with these parameters, the Activity Type is set to
    > To-Do, with a summary of Assign Laptop. The Assignment
    > field is set to Default user, and the Assigned to field is set to
    > Abby Jones. The Interval is 1, and the Unit
    > is set to days. The Trigger is Before Plan Date.
    >
    > ![An activity configured to assign a laoptop the day before an employee starts work.](../../../_images/activity-plan.png)

> **Note:**
>
> In a multi-company database, a Company field also appears. Selecting a company for an
> onboarding plan restricts the plan to *only* that company.

### Onboarding plan steps

The default Onboarding plan includes three default steps. All steps are
To-Do activities, and are scheduled for the day the onboarding plan is launched
(0 days Before Plan Date).

- Setup IT Materials: The manager must gather and configure all IT materials.
- Plan Training: The manager must plan the training for the new employee.
- Training: The new employee must complete the training planned by the manager.

![The three default steps in the Onboarding plan.](../../../_images/onboarding1.png)

## Modify onboarding plan

A single onboarding plan works only if the flow works for the entire company.

> **Note:**
>
> If the onboarding plan is universal, add to or modify the default onboarding plan. If
> department-specific onboarding plans are needed, [create a new onboarding plan] and limit the plan to a department.

To modify the default plan, first navigate to Employees app ‣ Configuration ‣
Onboarding / Offboarding, then click on Onboarding.

To modify a step, click on it. In the *Open: Activities* pop-up window, make any desired
modifications to the step, then click Save.

To add a new step, click Add a line at the bottom of the listed activities in the
*Activities To Create* tab, and a blank *Create Activities* pop-up window appears. Enter all the
information in the pop-up window, then click Save & Close if there are no other steps to
add, or click Save & New if more steps are needed.

## Create onboarding plan

Some companies require different onboarding plans, when there are department-specific onboarding
procedures that do not apply to the whole company. For these cases, a new department-specific
onboarding plan must be created.

To create a new onboarding plan, navigate to Employees app ‣ Configuration ‣
Onboarding / Offboarding. Click the New button in the upper-left corner, and a blank
*Employee Plans* form loads.

Enter the Plan Name, and select the Department using the drop-down menu.
This creates a plan *exclusively* for that department.

Add the various onboarding activities by clicking Add a line in the *Activities To
Create* tab, and [configure each activity].

> **Tip:**
>
> A company specializing in the manufacturing and selling of outdoor metal furniture may have a
> large factory that produces the products, and a separate sales office. This company may have two
> separate onboarding plans, one for factory workers, and one for office workers.
>
> The onboarding plan for the factory workers is set for the Manufacturing department,
> and includes specialized tasks relating to factory jobs. These include gathering the new
> employees uniform and safety gear, assigning a safety course, emailing their team about the new
> hire, going over benefits, and more.
>
> ![An onboarding plan configured for factory workers.](../../../_images/factory-onboarding.png)

## Launch onboarding plan

After an employee has been hired and their employee profile [is created](../recruitment/offer_job_positions.html#recruitment-new-employee), navigate to the desired employee’s profile by clicking on their Kanban
card on the **Employees** app dashboard, then click the Launch Plan button on their
employee profile, and a blank *Launch Plan* pop-up window loads.

The top of the screen displays a button for each available plan, as well as a button for the various
available activities. Click the desired onboarding plan to select it. Then, using the calendar
selector, set a date in the Due Date field. This is typically the employee’s first day,
but any date can be selected.

The *Plan Summary* section of the *Launch Plan* pop-up window displays all the steps in the selected
plan, along with the user icon for the person assigned to each activity.

Click the Schedule button, and Odoo schedules everything in the plan according to their
respective due dates.

All scheduled activities appear in the both chatter of the employee profile, and in the chatter of
the users with assignments relating to the plan.

> **Note:**
>
> If any activity assignments were configured to Ask at launch, an Assigned
> to field appears on the *Launch Plan* pop-up window. Using the drop-down menu, select the user
> responsible for all the unassigned activities.

![All onboarding tasks scheduled in the chatter.](../../../_images/onboarding-chatter.png)
> **Warning:**
>
> Onboarding can only be launched for [users](../../general/users.html) of the database. If there
> is any missing information on the employee’s profile, a warning listing the information needed
> appears.

---

# Departments

All employees in the **Employees** app fall under specific departments within a company.

## Create new departments

To make a new department, navigate to Employees app ‣ Departments, then click the
New button in the top-left corner to reveal a blank department form. Fill out the
following information on the department form:

- Department Name: Enter a name for the department.
- Manager: Select the department manager using the drop-down menu.
- Parent Department: If the new department is housed within another department (has a
  parent department), select the parent department using the drop-down menu.
- Company: Select the company the department is part of using the drop-down menu. This
  field only appears in a multi-company database.
- Color: Select a color for the department. Click the colored box to display all the
  color options. Click on a color to select it.

After the form is completed, click the  (Save manually) icon to
manually save the changes. When saved, a DEPARTMENT ORGANIZATION chart appears in the
right of the department card, illustrating where the department lies in the organization, and how
many employees are within each listed department.

![The department for with all fields filled out.](../../../_images/department-form.png)
> **Note:**
>
> The form auto-saves while data is entered, however the Department Organization chart
> does **not** appear until the form is manually saved. If the form is not saved, the
> Department Organization chart is visible upon opening the department card from the
> Departments dashboard.

## Departments dashboard

To view the currently configured departments, navigate to Employees app ‣
Departments. All departments appear in a Kanban view, and are listed in alphabetical order.

The default view for the Departments dashboard is a [Kanban view]. It is possible to view the departments in two other forms: a
[list view] and a [hierarchy view].

![The departments dashboard view with all the department cards in a Kanban view.](../../../_images/departments.png)

### Kanban view

Each department has its own Kanban card on the main Departments dashboard. Each
department card displays the following information, if available:

- Name: The name of the department.
- Manager: The name and image of the department manager.
- Company: The company the department is part of, including the location icon.
- Employees: The number of employees within the department.
- Appraisals: The number of appraisals scheduled for employees in the department.
- Time Off Requests: The number of unapproved time off requests for employees in the
  department [awaiting approval](../time_off/management.html#time-off-manage-time-off) . This **only** appears if there
  are requests to approve.
- Allocation Requests: The number of unapproved allocation requests for employees in the
  department [awaiting approval](../time_off/management.html#time-off-manage-allocations). This **only** appears if there
  are requests to approve.
- New Applicants: The number of [new applicants](../recruitment/recruitment-flow.html#recruitment-new) for a position
  within the department. This **only** appears if there are new applicants.
- Expenses: The number of employees in the department with [open expenses to
  approve](../../finance/expenses/approve_expenses.html). This **only** appears if there are any
  expenses waiting for approval.
- Absence: The number of employees with approved time off for the current day.
- Color bar: the selected color for the department appears as a vertical bar on the left side of the
  department card.

> **Note:**
>
> Click on an alert in a department card, such as Time Off Requests, to reveal a list
> view of the requests to approve for that department.

### List view

To view the departments in a list view, click the  (list) icon
in the top-right corner. The departments appear in a list view, which displays the
Department Name, Company, Manager, Employees,
Parent Department, and Color for each department.

The departments are sorted alphabetically by Department Name, by default.

![The departments presented in a list view.](../../../_images/list.png)

### Hierarchy view

To view the departments in a hierarchy view, click the
(Hierarchy) icon in the top-right corner. The departments appear in an organizational
chart format, with the highest-level department at the top (typically `Executive Management`), and
all other departments beneath it. All child departments of the first-level child departments are
folded.

Each department card displays the Department Name, the Manager (and their
profile image), the Number of Employees in the department, and the number of any child
departments.

Click the Unfold button on a department card to expand it. Once expanded, the
Unfold button changes to a Fold button. To collapse the department, click
the Fold button. Only **one** department *per row* can be unfolded at a time.

Click anywhere on a department card to open the department form. Click the (#) Employees
smart button to view a list of all the employees in that department.

![The departments presented in a hierarchy view.](../../../_images/hierarchy.png)

---

# Learning

The **Employees** app tracks two kinds of learning: virtual [eLearning]
courses, or [onsite] in-person training. Both certifications and training
attendance records are kept in the **Employees** app, and all completed courses and certifications
are logged in the *Resume* tab of each [employee record](new_employee.html#employees-resume).

## eLearning

To train employees using eLearning courses, the **eLearning** app must be [installed](../../general/apps_modules.html#general-install).

> **Note:**
>
> Courses can be [created] either through the **Employees** app *or* the
> **eLearning** app.

First, navigate to Employees app ‣ Learning ‣ eLearning, and the
eLearning Courses dashboard loads. All currently configured courses appear in a list
view. Each course displays the following information:

- Name: The name of the course.
- Tags: Add relevant tags, such as level, topic, etc.
- Responsible: The user responsible for the course, including inviting participants and
  updating the course as needed. The creator of the course does **not** have to be the
  Responsible person.
- Course Type: This field determines the format of the course. The two available options
  are:

  - Training: The content must be viewed *in order*.
  - Documentation: The employee can view the content in the order they choose.

![The default list view of the eLearning courses in the Employees app.](../../../_images/courses.png)

### Create an eLearning course

No courses come preconfigured in the **Employees** app. Courses must be created, in either the
**Empoyees** app or the **eLearning** app.

> **Note:**
>
> Once a course is available, it is accessible from both apps.

To create an eLearning course, navigate to Employees app ‣ Learning ‣
eLearning. Click the New button in the upper-left corner, and a blank *eLearning
Course* form loads.

Follow the directions for [creating a course](../../websites/elearning.html#elearning-course-creation), including adding the
[content](../../websites/elearning.html#elearning-content), [description](../../websites/elearning.html#elearning-description), [options](../../websites/elearning.html#elearning-options), and [karma](../../websites/elearning.html#elearning-karma) tabs.

> **Warning:**
>
> Only users with the proper [access rights](../../general/users/access_rights.html) can view,
> modify, or create any learning course.

### Invite employees

From the eLearning Courses dashboard, invite employees to take a course. Navigate to
Employees app ‣ Learning ‣ eLearning, click on the desired course from the
list, and the course form loads. Click the Add Attendees button and an *Enroll Attendees
to (Course Title)* pop-up window loads.

Add all desired employees to the Recipients field using the drop-down menu. All
employees in the database are available in this list.

> **Note:**
>
> To filter only employees, click into the Recipients field, then click
> Search more….
>
> In the *Search: Recipients* pop-up window that loads, filter the results by clicking into the
> search box and selecting Employees in the  Filters
> column. Only employees are presented, excluding other companies or vendors. Click the checkbox to
> the left of the Name column to select all employees.

The email uses the default `Elearning: Add Attendees to Course` Mail Template, which
includes a dynamic subject line that includes the course’s name.

Make any desired changes to the email, attach any necessary files, then click Send to
invite the employees.

Once the invitation is sent, the recipients appear in the attendees list. Click the
 Attendees smart button to view all invited attendees.

Once the employee completes the eLearning course, the training appears on their employee record, in
the [Resume](new_employee.html#employees-resume) tab.

> **Note:**
>
> Alternatively, click the Invite button, and an *Invite Attendees to (Course Name)*
> pop-up window loads. Copy the course link by clicking the  (Copy)
> icon to copy the link and send it to employees. Or, click the Send Email toggle to
> [email employees].

![The invitation email to send employees the course.](../../../_images/email-invite.png)

## Onsite

The **Employees** app can also track in-person training. These can take any format, from lectures to
interactive training. To create onsite training courses, the **Events** app must be [installed](../../general/apps_modules.html#general-install).

Onsite training can be created either through the **Employees** app *or* the **Events** app. All
courses created appear in both apps.

> **Note:**
>
> Once an onsite training is available, it is accessible from both apps.

To view all currently configured onsite courses navigate to Employees app ‣
Learning ‣ Onsite, and the Onsite Courses dashboard loads. All onsite courses appear
in a default Kanban view, organized by stage.

Click on an onsite training card to view the details.

### Create an onsite course

To create a new onsite training, navigate to Employees app ‣ Learning ‣ Onsite.
Click the New button in the top-left corner and a blank *Onsite Courses* event form
loads.

[Fill out the event form](../../marketing/events/create_events.html#events-event-form) to configure the onsite training course. When
completed, the option to publish it to the website is available, if desired. This option is only
available if the **Website** app is installed.

### Invite employees

Once the onsite training is configured, the next step is to invite employees. Navigate to
Employees app ‣ Learning ‣ Onsite and click on the course Kanban card. Click
the Invite button in the upper-left corner, and a blank mailing form loads.

The form only allows for inviting employees via Email. The Subject is
`Event: (Event Title)` by default, and can be changed if desired.

Next, add the employees to the [Recipients](../../marketing/email_marketing.html#email-marketing-recipients) in the respective
field, then create the [body of the email](../../marketing/email_marketing.html#email-marketing-mail-body).

Click Send, and a confirmation pop-up window loads. Click Send to all on the
pop-up window and the invitations are sent.

---

# Certifications

When jobs require specific knowledge, training, or certifications, it is necessary to track
employees’ certifications to ensure they are properly trained and that the necessary documentation
is in place.

When jobs require specific knowledge, track employee certifications (e.g., classes, tests, seminars)
to verify required skills. Odoo accepts any certification type without restriction.

> **Warning:**
>
> To add certifications to an employee profile and to access the *Certifications* report, the
> **Surveys** app **must** be installed.

## Create certifications

No certifications are preconfigured in Odoo’s **Employees** app; therefore, all certifications must
be added to the database. To create a certification, navigate to the Employees app
‣ Configuration ‣ Skill Types. Click the New button in the upper-left corner, and a
blank *Skill Types* form loads.

Enter the following information on the form:

- Skill Type: Enter the type of certification being added. This acts as the *category*,
  and individual certifications are nested beneath it.
- Color: Click on the existing color to view the available colors. Click the desired
  color to select it.
- Certification: Click the toggle to indicate the skill is a certification. The toggle
  turns green when it is active.
- Skills: Click Add a line and enter the Name for the specific
  certification.
- Levels: Click Add a line, and enter a Name and
  Progress percentage (`0`-`100`) for each level. Set a Default Level by
  clicking the toggle on the desired line (only one level can be selected).

> **Tip:**
>
> A United States-based company requires its employees to complete various OSHA training and certify that the training is
> complete.
>
> The company creates a new skill type and enters OSHA Training in the Skill
> Type field.
>
> The various courses are entered in the *Skills* section, including OSHA 3115 - Fall
> Protection, OSHA 3095 - Electrical Standards, and more.
>
> There is only one level in the *Levels* section, Certified, which is set to
> 100%.
>
> ![The skill type form configured for various OSHA training courses.](../../../_images/osha.png)

## View certifications

To view a full list of all employee certifications, navigate to the Employees app
‣ Learning ‣ Certifications.

All certifications appear in a list view, grouped by certification *type*. Each certification entry
displays the following:

- Employee: The employee’s name, along with their avatar image.
- Certification: The name of the certification.
- From: When the employee received the certification.
- To: The date the certification expires. If the certification has no expiration date,
  Indefinite appears in this field.

![The list of employee certifications.](../../../_images/employee-certifications.png)
> **Warning:**
>
> **Only** skill type records with the *Certification* toggle set to active appear on the
> Certifications report. All other certifications appear in the resume section of the
> [employee form](new_employee.html#employees-resume).

### View certifications by expiration status

When managing a large number of employees with a variety of certifications, it can be difficult to
determine which employees need to keep necessary certifications current in the default list view. In
this scenario, it is beneficial to view the certifications by expiration status.

To do so, navigate to the Employees app ‣ Learning ‣ Certifications. Next,
clear the default  Type grouping in the search bar. Next, click the
 (Toggle Search Panel) icon, then click Custom Group
, to reveal a drop-down menu. Click Validity Stop, then click away
from the drop-down menu to close it.

After doing so, all the certifications are grouped by expiration month, in descending order, with
the oldest at the top.

The entries are color-coded. Current certifications that are still valid appear in black, expired
certifications appear in gray, and certifications that are going to expire within the next 90 days
appear in orange.

![The list of employee certifications, grouped by status.](../../../_images/status.png)
> **Note:**
>
> The time frame can be set to either Year, Quarter, Week, or
> Day. To change the presented time frame groups, click the search bar, then click
>  Validity Stop , and select the desired time
> frame.

## Log a certification

To log a certification for an employee, navigate to the Employees app ‣ Learning
‣ Certifications. Click New to load a blank certification form. Enter the following
information on the form:

- Employee: Select the employee who received the certification using the drop-down menu.
- Category: Click the *type* of certification received.
- Skill: Select the specific certification received. The presented options change if the
  Category is changed.
- Skill Level: If the selected certification has a set of *skill levels*, those levels
  appear in this section. Click on a level to select the level achieved from the certification.
- Validity: Set the validity start and end dates in the two fields. The current date is
  populated in the first field, and indefinite is populated in the To field,
  by default.

Once all the fields are configured, click the Save button. The certification is logged
for the employee, and appears on the *Certifications* report and the employee record.

![A certification form filled out for a 10-hour OSHA safety course.](../../../_images/add-cert.png)

## Certifications Report

To view a report of all employee certifications, navigate to the Employees app ‣
Reporting ‣ Certifications.

All certifications appear in a list view, grouped by employee. Each certification entry displays the
following:

- Employee: The employee’s name, along with their avatar image.
- Certification Type: The *skill type* configured for the certification. This can be
  thought of as the certification *category*.
- Certification: The name of the certification.
- Validity Start: When the employee received the certification.
- Certification Level: The level the employee achieved for the certification. This is
  determined by the configured levels on the *skill type*.
- Current Level: The corresponding percentage for the Certification Level
  the employee achieved.

![The list of employee certifications.](../../../_images/certifications-list.png)
> **Warning:**
>
> **Only** certification records with the *Display Type* set to *Certification* on their
> [certification form] appear on the Employee
> Certifications report. All other certifications appear in the resume section of the
> [employee form](new_employee.html#employees-resume).

---

# Badges

In Odoo, employees can earn badges, either automatically through [challenges created in the CRM
app](../../sales/crm/optimize/gamification.html), through **eLearning** courses, or manually, as
managers decide to award them.

Badges are a way to gamify the work day, can be created for any reason, and can be granted to any
user.

> **Warning:**
>
> Badges can **only** be awarded to [users of the database](../../general/users.html), *and* if
> the **eLearning** app is installed.

## View available badges

To view the available badges that are configured by default, navigate to Employees
app ‣ Configuration ‣ Badges.

All badges appear in a default Kanban view, with the badge’s Name and image displayed.
Additionally, the number of users awarded the badge for both the current month, and in total,
appears, along with the badge description, and the avatar for each user who received the badge.

Each badge has a Grant button to [award the badge] from the
Badges dashboard.

![All the available badges, on the Badges dashboard.](../../../_images/badges.png)

## Create badges

Badges can be created in the database when the default badges are not sufficient. This can be done
from the Badges dashboard in the **Employees** app, or from the **CRM** app.

To add a badge in the **Employees** app, first navigate to Employees app ‣
Configuration ‣ Badges, then click the New button in the upper-left corner.

Fill out the badge form as outlined in the [CRM documentation](../../sales/crm/optimize/gamification.html#crm-create-rewards).

> **Note:**
>
> [CRM Gamification](../../sales/crm/optimize/gamification.html#crm-create-rewards)

## View employee badges

To view badges awarded to an employee, open the **Employees** app, and click on an employee record.
Click on the Received Badges tab to view any awarded badges.

> **Note:**
>
> If this tab is not visible, it means there is no Related User in the
> Settings tab. Once a user is populated in the Related User field, the
> Badges tab appears.

## Grant badges

To grant a badge to an employee, open the employee record, and click into the Received
Badges tab. Click the Grant a Badge button to load a Reward Employee pop-up
window.

Using the drop-down menu, select the badge being awarded in the What are you thankful
for? field. The default options are Good Job, Problem Solver, and
Brilliant.

> **Note:**
>
> Additional options appear (e.g., Get Started, Power user,
> community Hero) which are associated with challenges. These are automatically granted
> through completed challenges. While these can be awarded at any time, it is advised to grant
> badges manually that are *not* associated with a challenge.

Next, enter a brief summary of why the badge is being granted in the field displaying
Describe what they did and why it matters (will be public) field. Last, click the
Reward Employee button, and the badge is awarded, and is visible in the
Badges tab.

> **Note:**
>
> Users cannot grant themselves badges. An error message appears if attempted.

![The 'Reward Employee' field populated.](../../../_images/badge1.png)

---

# Equipment

Many employees are given various items to use while they work, such as laptops, phones, and
printers. Most companies track their equipment, to see who is using what, as well as having a record
of important information regarding the equipment, such as serial numbers, warranty information, and
maintenance history.

> **Note:**
>
> To track employee equipment, the **Maintenance** app *must* be installed.

## Individual employee equipment

Employee equipment is tracked on the employee record. To view all equipment currently assigned to an
employee, navigate to the Employees app, and click on the desired employee record.

At the top of the record, an  Equipment Count smart button appears, with
a number indicating how many, if any, items are currently assigned to that employee.

Click the  Equipment Count smart button, and all equipment currently
assigned to the employee appears in individual Kanban cards.

Each Kanban card displays the equipment’s name and model on the first line, followed by the serial
number (if available), and lastly, the employee’s name. Any current maintenance requests appear at
the bottom of the card in a red box.

![A Kanban view of all equipment for an employee.](../../../_images/equipment.png)
> **Note:**
>
> A serial number is **not** required when logging equipment.

## All employee equipment

To view all equipment for all employees, start on the [equipment record of an individual
employee].

> **Note:**
>
> It does not matter what employee is selected, or whether they have any equipment assigned to
> them. This step is only used to get to the Equipment list.

In the Kanban view of the employee’s equipment, clear the default Assigned Employee
filter in the search bar. This presents *all* equipment in the database, including those assigned to
individual employees and whole departments.

Click into the search bar, and select Employee in the  Group
By column. The equipment is now organized in a Kanban view, by employee.

In the Kanban view displaying all employee equipment records, equipment can be reassigned by
clicking and dragging an equipment card to the desired employee. This changes ownership of the
equipment.

![A Kanban view of all equipment for all employees.](../../../_images/all-equipment.png)

## Add equipment to an employee record

To add equipment to an employee’s record, open the Employees app, click on the
desired employee record, then click the  Equipment Count smart button at
the top.

All equipment currently assigned to the employee appears in individual Kanban cards. To add a new
equipment record, click the New button in the upper-left corner, and a blank
Equipment form loads.

[Fill out the equipment form](../../inventory_and_mrp/maintenance/add_new_equipment.html) for the
employee’s equipment.

> **Note:**
>
> Instead of filling out a new Equipment form for the same item, a form can be
> duplicated, then updated.
>
> On the Equipment form, click the  (Actions) icon in the
> upper-left corner, then select  Duplicate.
>
> An identical form appears, with *all* the information filled out, except for the
> Serial Number.
>
> Enter the Serial Number on the form, and make any other necessary changes, such as
> the assigned Employee.
>
> ![A duplicate equipment form with all the information filled out except the serial number.](../../../_images/equipment-form.png)

---

# Offboarding

When an employee leaves the company, it is important to have an [offboarding plan] to ensure all necessary steps are followed, such as returning equipment,
revoking access to business systems, filling out HR forms, having an exit interview, and more.
Depending on the company, there could be several different offboarding plans, configured for
specific departments or divisions, that have different requirements and steps from the main
offboarding plan.

In addition to an offboarding plan, the employee record must be [updated to reflect their
departure], log the reason why they left, and close any open activities
associated with the employee.

## View offboarding plan

Before offboarding can begin, it is recommended to check the default offboarding plan that comes
preconfigured with the **Employees** app. To view the current default plan, navigate to
Employees app ‣ Configuration ‣ Onboarding / Offboarding. Click
Offboarding to view the detailed offboarding plan form.

### Offboarding plan steps

The default Offboarding plan is minimal, with two default steps (three if the **Fleet**
app is installed). All steps are *To-Do* activities, and are scheduled for the day the offboarding
plan is launched (0 days Before Plan Date). The default steps are:

- Organize knowledge transfer inside the team: The manager must ensure all knowledge the
  employee has relating to their job position is either documented or shared with colleagues so
  there is no knowledge gap.
- Take Back Fleet: The fleet manager ensures any vehicles assigned to the employee are
  either [unassigned (available for other employees) or the next driver is assigned](../fleet/new_vehicle.html#fleet-new-vehicle-new-driver). This step only appears if the **Fleet** app is installed.
- Take Back HR Materials: The manager must obtain any documents and materials the HR
  department requires. It is recommended to check with the HR department to ensure everything
  required for this step is completed.

![The three default steps in the Offboarding plan.](../../../_images/offboarding.png)

## Modify offboarding plan

The default offboarding plan is minimal, so that modifications can be made to accommodate any
company’s offboarding needs. Every company has different requirements, therefore it is necessary to
add the required steps to the offboarding plan.

If the offboarding plan is universal, add or modify the default offboarding plan. If the offboarding
plan needed is only for a specific department, then [a new plan should be created], specifically for that department.

To modify the default plan, first navigate to Employees app ‣ Configuration ‣
Onboarding / Offboarding, then click on Offboarding.

To modify a step, click on the step and an *Open: Activities* pop-up window appears. Make any
desired modifications to the step, then click Save to accept the changes and close the
pop-up window.

To add a new step, click Add a line at the bottom of the listed activities in the
Activities To Create tab, and a blank Create Activities pop-up window
appears. Enter all the information in the pop-up window, then click Save & Close if
there are no other steps to add, or click Save & New if more steps are needed.

Configure all the desired steps for the offboarding plan.

## Create offboarding plan

For some companies, specific offboarding plans may be necessary for some departments. For these
cases, a new department-specific offboarding plan may be needed.

To create a new onboarding plan, navigate to Employees app ‣ Configuration ‣
Onboarding / Offboarding. Click the New button in the upper-left corner, and a blank
*Employee Plans* form loads.

Enter the Plan Name, and select the Department using the drop-down menu.
This creates a plan *exclusively* for that department.

Add the various offboarding activities by clicking Add a line in the *Activities To
Create* tab, and [configure each activity].

Enter the following information on the form:

- Plan Name: The specific name for the plan.
- Model: This field specifies where this plan can be used. In this case, in the
  **Employees** app. This field is not able to be modified.
- Department: If left blank (the default setting) the plan is available for all
  departments. To make the plan department-specific, select a department using the drop-down menu.

Next, add the various steps for the plan by clicking Add a line at the bottom of the
listed activities in the *Activities To Create* tab, and a blank *Create Activities* pop-up window
appears.

Enter the following information in the pop-up window:

- Activity Type: Using the drop-down menu, select the specific activity to be scheduled.
  The default options are To-Do, Email, Call,
  Meeting, Document, or Certifications. If the **Sign** app is
  installed, a Signature option is available.
- Summary: Enter a short description for the step.
- Assignment: Using the drop-down menu, select the person assigned to perform the
  activity. The default options are: Ask at launch, Default user,
  Coach, Manager, and Employee. If the **Fleet** app is
  installed, a Fleet Manager option is available.

  > **Note:**
  >
  > The selection for the Assignment role is in relation to the employee. If
  > Coach is selected, the employee’s coach is assigned to the activity.
  >
  > If Default user is selected, an Assigned to field appears. Using the
  > drop-down menu, select the user who will always be assigned this activity.
- Interval: Configure the fields in this line to determine the due date of the activity.
  Enter a number in the first field, then, using the drop-down menus in the following two fields,
  configure when the due date should be created; (`#`) of days, weeks, or
  months, either Before Plan Date or After Plan Date.

When the Create Activities form is completed, click Save & Close if there
are no other steps to add, or click Save & New to add more steps, as needed.

> **Tip:**
>
> A company specializing in after-school art programs has two separate offboarding plans, one for
> the teachers working in the field, and one for office workers.
>
> The offboarding plan for the teachers is set for the Art Program Teachers department,
> and includes specialized tasks relating to those jobs. These include ensuring all art supplies
> are catalogued and returned, all student feedback forms are turned in, and all access badges and
> keys for the various locations are returned.
>
> ![An offboarding plan configured for art teachers.](../../../_images/offboarding-teachers.png)

## Launch offboarding plan

After an employee has given notice (typically two weeks) or once the company has decided to
terminate the working relationship with the employee, the offboarding plan should be launched.
Navigate to the Employees app and click on the departing employee profile. Click
the Launch Plan button, and a blank *Launch Plan* pop-up window loads.

![The Launch Plan button on the employee profile.](../../../_images/launch-plan-button.png)

The top of the screen displays a button for each available plan, as well as a button for the various
available activities. Click the desired offboarding plan to select it. Then, using the calendar
selector, set a date in the Due Date field. This is typically the employee’s last day,
but any date can be selected.

The *Plan Summary* section of the *Launch Plan* pop-up window displays all the steps in the selected
plan, along with the user icon for the person assigned to each activity.

Click the Schedule button, and Odoo schedules everything in the plan, according to their
respective due dates.

## Archive an employee

In Odoo, when an employee leaves the company they must be *archived*. This step should be done
*after* the employee has been fully offboarded. To archive an employee, first navigate to the
Employees app. From here, locate the employee who is leaving the company, and click
on their employee card.

The employee form loads, displaying all their information. Click the
(gear) icon in the top-left corner, and a drop-down menu appears. Click
 Archive, and an *Employee Termination* pop-up window appears.

Fill out the following fields on the form:

- Employees: The selected employee populates this field by default. Multiple employees
  can be archived at once by adding the additional employees to archive in this field.
- Departure Reason: Select a reason the employee is leaving from the drop-down menu. The
  default options are:

  - Fired: Select this option when an employee is being let go, and the company has
    given notice.
  - Resigned: Select this option when the employee no longer wishes to be employed, and
    the employee has given notice.
  - Retired: Select this option when the employee is retiring.
  > **Note:**
  >
  > If a new departure reason is needed, a new one can be created. Close the *Employee Termination*
  > pop-up window, and navigate to Employees app ‣ Configuration ‣ Departure
  > Reasons. Click the New button, and a blank line appears at the bottom of the list.
  > Enter the new reason, and click Save.
- Contract End Date: Using the calendar selector, select the last day the employee is
  working for the company.
- Detailed Reason: Enter a short description for the employee’s departure in this field.
- Close Activities: Click the checkbox next to each type of activity to close or delete
  any open activities associated with it. It is recommended to click **all** checkboxes that are
  applicable. The available options are:

  - Contract: Applies an end date for the current contract.
  - Company Car: Removes the employee as the driver for their current company car, and
    [assigns the next driver](../fleet/new_vehicle.html#fleet-new-vehicle-new-driver), if applicable.
  - Equipment: Unassigns the employee from any assigned equipment.
  - Appraisals: Cancels all appraisals scheduled after the contract end date.

When the form is complete, click Apply. The employee record is archived, and a red
Archived banner appears in the top-right corner of the employee form. The chatter logs
the various details, including the Departure Date, Departure Reason,
Contract End Date, the dates for the last work entries, and the employee version that
was archived.

![The employee termination form with all fields filled out.](../../../_images/termination.png)
> **Note:**
>
> If any issues exist that prevent Odoo from archiving the employee, the detailed reasons appear in
> a red warning box in the *Employee Termination* pop-up window. The warning states `The plan
> "(Plan Name)" cannot be launched`, then lists the various steps that must be done before
> archiving the employee.

---

# Employee retention report

It is possible to determine the retention rate for a company by modifying an existing report.

First, navigate to Employees app ‣ Reporting ‣ Contracts to open the
Employee Analysis report. This report shows the number of all employees for the
Last 365 Days, in a default  Line Chart.

![The default Employees Analysis report.](../../../_images/employees-analysis.png)

Next, click the Measures  button in the upper-left corner,
revealing a drop-down menu. Click # Departure Employee in the list, then click away from
the drop-down menu to close it. Now, the report shows all the employees who were archived for the
Last 365 Days.

To view this information in an easier format, click the  (Pivot)
icon in the upper-right corner, and the data is presented in a pivot table.

The various employees, organized by department, populate the rows. The columns display the following
totals: the monthly Wage, the Fuel Card budget, total Annual
Employee Budget (also referred to as the *annual salary*), the number of New Employees,
as well as the number of Departure Employees (employees who left).

![The Employees Analysis report, modified to show departed employees only.](../../../_images/pivot-departures.png)

## Employee retention rate comparison report

It is possible to compare data only for employees who left, compared to the total current employees,
between two separate time periods. This is commonly referred to as the *employee retention rate*.

To view these metrics, first open the Employee Analysis report by navigating to
Employees app ‣ Reporting ‣ Contracts. Click the
(Pivot) icon in the upper-right corner to view the information in a pivot table.

Next, click the Measures  button in the upper-left corner,
revealing a drop-down menu. Click # New Employees, Annual Employee Budget,
Fuel Card, and Wage in the list, to deselect these metrics and hide them in
the table. Then, click Count at the bottom of the list to enable that metric.

Click away from the drop-down menu to close it. Now, the report shows all the employees who left the
company (# Departure Employee), as well as the total number of employees
(Count), for the Last 365 Days.

To compare the data for the current year with the previous year, click the
(down arrow) in the search bar, revealing multiple filter and grouping options. Click
Last 365 Days in the  Filters column, to turn off that
filter. Then, click Date, and click the current year (in this example, 2024)
from the resulting drop-down menu.

Once a selection is made beneath Date in the  Filters
column, a  Comparison column appears. Click Date: Previous
Year in the new column, then click off of the drop-down menu to close it.

> **Note:**
>
> In Odoo, in order to access the  Comparison column, a specific time
> *other than* Last 365 Days **must** be selected. If not, the
> Comparison column is **not** visible.

Now, the pivot table displays the total number of employees who left the company (#
Departure Employee), as well as the total number of employees (Count) in the columns.
These are further divided by the two different years, and also displays the Variation
between the two.

The rows display the departments, and lists each individual employee for each department, in the
rows.

For a more concise view of this report, click  Total above the
top row of the departments and employees, to collapse the rows. Now, the table presents the total
number of employees who left the company for both years, compared to the total number of employees
for both years, including the difference, in a percentage.

> **Tip:**
>
> In this example, 3 employees out of 83 left in 2023, and 8
> employees out of 202 left in 2024. There was a 166.67% increase in the
> employees who left in 2024 as compared to 2023. Additionally, there was a 143.37%
> increase in the total number of employees in 2024 as compared to 2023.
>
> ![The report modified to show the difference between two years of employees who left.](../../../_images/comparison-years.png)

To view more detailed rates for each department, click  Total in
the single row, revealing a drop-down menu, and click Department. Click away from the
drop-down to close it, and now the pivot table displays the total number of employees who left
(# Departure Employee), the total number of employees (Count), and the
Variation (in a percentage) for both 2023 and 2024, organized by department.

> **Tip:**
>
> In this example, it can be determined that the Management department had the best
> retention rate in 2024 as compared to 2023, with a Variation rate of
> -100%. Additionally, it can be determined that the Management / Research &
> Development department had the most turnover, with a Variation of 300%.
>
> ![The expanded employee retention report by department.](../../../_images/department-totals.png)
# Website — Builder, eCommerce & SEO

> **Odoo 19.0 Reference**
> Source: www.odoo.com/documentation/19.0 — HTML converted via markdownify

## Purpose

Odoo Website builder: pages, building blocks, themes, SEO, multi-website, domain configuration, analytics, and CDN. Use when building or customising an Odoo-powered website or eCommerce store.

---

# Website

**Odoo Website** offers a user-friendly platform for creating and managing your website. It includes
various tools and features to help you design, publish, and maintain web pages without needing
advanced technical skills. You can easily customize layouts, add multimedia content, and integrate
with other Odoo apps to expand your website’s functionality.

[#### Web design

Design your website using building blocks and website themes.](website/web_design.html)[#### Structure

Manage website pages, menus, and search engine optimization.](website/structure.html)[#### Configuration

Configure domain names, address autocompletion, Google Search Console, cookies bar,
translations, multiple websites, form spam protection, content delivery network (CDN).](website/configuration.html)[#### Reporting

Monitor your website’s traffic with website analytics and set up link trackers.](website/reporting.html)[#### Mail groups

Configure mail groups to allow website visitors to participate in public discussions via
email.](website/mail_groups.html)

> **Note:**
>
> Odoo offers a [free custom domain name](website/configuration/domain_names.html#domain-name-register) to all Odoo Online databases
> for one year. Visitors can then access your website with an address such as `www.example.com`
> rather than the default `example.odoo.com`.

> **Note:**
>
> - [Odoo Tutorials: Website](https://www.odoo.com/slides/website-25)
> - [Odoo Tutorials: eCommerce](https://www.odoo.com/slides/ecommerce-26)
> - [Unsplash](../general/integrations/unsplash.html)

---

# Web design

Design your website using [building blocks](web_design/building_blocks.html), customize
its [theme](web_design/themes.html) with various options, structure and present content
with [elements](web_design/elements.html), and display or hide building blocks using
[visibility settings](web_design/visibility.html).

[#### Building blocks

Design your website by dragging and dropping building blocks, then editing them to fit your
content and layout needs.](web_design/building_blocks.html)[#### General theme

Customize your website’s theme by adjusting its colors, fonts, and layout.](web_design/themes.html)[#### Elements

Structure and present content effectively with elements such as titles, lists, etc.](web_design/elements.html)[#### Visibility

Display or hide building blocks based on several criteria.](web_design/visibility.html)

> **Note:**
>
> [Odoo Tutorials: Website](https://www.odoo.com/slides/website-25)

---

# Building blocks

You can design your website by [dragging and dropping building blocks], then [editing them] to fit your
content and layout needs.

> **Note:**
>
> [Odoo Tutorial: Design your website: text and colors](https://www.odoo.com/slides/slide/design-your-website-text-and-colors-6930?fullscreen=1)

## Add a building block

To add a block to a [website page](../structure/pages.html), access the page, click
Edit, then drag and drop the desired building block into the appropriate location. Two
types of building blocks are available: Categories and Inner Content.
Inner Content building blocks can only be added into Categories building
blocks.

When clicking a category block, a popup appears, allowing you to select between multiple
templates for each category.

> **Note:**
> > Search for a specific block in the Insert a block popup using the search bar.
>
> ![Pop-up block selection](../../../../_images/insert-a-block.png)

Once the category block is placed, you can drag and drop Inner content blocks
within it. The Inner content blocks allow you to add elements, such as videos, images,
social media buttons, etc., into pre-existing category blocks.

> **Note:**
>
> - You can also add a building block on the login page. To do so, navigate to the website’s
>   homepage, add `/web/login` to the URL and press `Enter`.
> - Access to certain blocks requires installing their respective application or module
>   (e.g., eCommerce for the Products block).

> **Tip:**
>
> Add all your social media accounts in one place with the inner content Social Media
> block. Toggle the switch on or off next to the desired platform and copy/paste your account URL.
>
> ![Social Media inner content block](../../../../_images/social-media-inner-content-block.png)

### Form

The Form block is used to collect information from website visitors and, if applicable,
create records in your database. To add a form to a website page, drag and drop the
Contact & Forms category block, then select a block in the popup.

![Example of a form block](../../../../_images/form-block.png)

#### Action

By default, when the form is submitted, an email containing the information entered by the visitor
is automatically sent. Depending on the apps installed on your database, additional actions that can
automatically create records may become available. To choose a different action, click
Edit, click the form, navigate to the Style tab, and select the desired
Action:

- Apply for a Job ([Recruitment](../../../hr/recruitment.html))
- Create a Customer ([eCommerce](../../ecommerce.html))
- Create a Ticket ([Helpdesk](../../../services/helpdesk.html))
- Create an Opportunity ([CRM](../../../sales/crm.html))
- Subscribe to Newsletter ([Email Marketing](../../../marketing/email_marketing.html))
- Create a Task ([Project](../../../services/project.html))
- More models: to generate other types of records

By default, submitting the form redirects visitors to a *Thank you* page. Use the URL
field to send them to a different page. Alternatively, you can choose not to redirect and keep
them on the form’s page by selecting Nothing or Show Message in the
On Success field.

#### Fields

To add a new field to the form, navigate to the Style tab and click the
+ Field button next to the Form or Field section. To modify any
field on the form, select the field, then use the options available in the Field
section of the Style tab. For example, you can:

- Change the field Type.

  > **Note:**
  >
  > It is also possible to select an Existing Field from the database and use the data
  > it contains. The fields available depend on the selected action. Property fields added to the
  > database can also be used.

  > **Note:**
  >
  > Click here to preview all field types.
  >
  > ![All types of form fields](../../../../_images/all-types-of-field.png)
  >
  > Some fields are visually similar, but the data entered must follow a specific format.
- Edit the field’s Label and adapt its Position.
- Enable a field Description. Toggle the switch on and click the default description on
  the form to modify it.
- Add a Placeholder or Default value.
- Specify if the field is Required.
- Edit the field’s [visibility](visibility.html) settings.
- Add an [animation](elements.html#website-elements-animations).

Once you have made the desired changes, click Save.

#### Add an Odoo contact form on a non-Odoo website

You can display an Odoo contact form on another website using an iframe. To do so, follow these
steps:

1. **Prepare the Odoo form:** Create a contact form on a page in Odoo Website and remove the
   [header design](../structure/header_footer.html#website-header-footer-header-design) and the [footer design](../structure/header_footer.html#website-header-footer-footer-design). Make sure only the contact form remains on the page.
2. **Generate an embeddable code:** Copy the URL of the Odoo form page and paste it into an iframe
   generator, such as [La Digitale.dev](https://ladigitale.dev/digitools/generateur-iframe) or
   [iFrame Generator](https://www.iframe-generator.com/) . Adjust the width and height for proper
   display.
3. **Add the embedded code to the non-Odoo website:** Open the relevant page’s HTML (in the code
   editor or CMS) and insert the embedded code where the form should be displayed.

> **Tip:**
>
> Example of an embedded code:
>
> ```
> <iframe src="https://example.com/odoo-form"
>         style="border:0;"
>         name="odooForm"
>         scrolling="no"
>         frameborder="0"
>         marginheight="0"
>         marginwidth="0"
>         height="400px"
>         width="600px"
>         allowfullscreen>
>  </iframe>
> ```

### Embed code

Embedding code allows you to integrate content from third-party services into a page, such as videos
from YouTube, maps from Google Maps, social media posts from Instagram, etc.

After dragging and dropping the Embed Code block from the Inner Content
section into a page, click the block, then go to the Style tab and click
Edit. Replace the placeholder code with your custom embed code.

![Add the link to the embedded code you want to point to](../../../../_images/embed-code-pop-up.png)
> **Warning:**
>
> Do not copy/paste code you do not understand, as it could put your data at risk.

## Move, switch, duplicate or delete a building block

Pull the turquoise borders on the block to reduce or increase the space at the top or bottom of it.

Change the block order by clicking  (chevron up) or
 (chevron down) and move the block on the page by clicking
 (arrows). When you have multiple [columns], move a column to the left or right by clicking
 (chevron left) or
(chevron right).

To duplicate a building block, click  (duplicate). Once duplicated, the
new block appears on the page beneath the original one.

> **Note:**
>
> Alternatively, click the  (duplicate) icon at the top of the
> Style tab to duplicate the selected block.

To delete a block, click  (trash).

> ![Extend margins on building block](../../../../_images/padding-building-block.png)

## Edit a building block

To edit the content of a building block, click it and go to the Style tab.
Available customization options vary depending on the type of block selected.

> **Note:**
>
> - [Web design elements](elements.html)
> - [Visibility](visibility.html)

### Background

To modify the background of a building block, select the block, go to the Style tab,
and click the color dot or another Background option. You can change the
color and/or add an image, video, and/or shape. Once you’ve selected a shape, new fields appear to
allow you to customize the shape.

> **Note:**
>
> - Position an element (image, text, etc.) behind or in front of another one by using the
>   Send to back or Bring to front icons.
>
>   ![Change block position](../../../../_images/change-block-position.png)
> - To resize a block, click and drag the dots around its edges to adjust it as needed.
>
>   ![Adapt block size](../../../../_images/adapt-block-size.png)

> **Note:**
>
> [General theme](themes.html)

### Layout: grid and columns

For most building blocks, you can choose between two layout styles: [grid] or [columns (cols)]. To change
the default layout style, click the block, go to the Style tab, and set the
Layout field to Grid or Cols.

#### Grid

The Grid layout allows you to reposition and resize elements, such as images or text, by
dragging and dropping them. When Grid is selected, additional options are available to
Add Elements by clicking Image, Text, or Button.

![When the grid layout is selected, choose an image and drag and drop it where needed.](../../../../_images/grid-layout.png)

#### Cols

Choosing the Cols layout allows you to determine the number of elements per line within
the block. To do so, select the block to modify, click the dropdown next to the Cols
field, and adjust the number. You can then modify a specific column’s settings using the options in
the Column section of the Style tab.

> **Note:**
>
> By default, [on mobile devices](visibility.html), only one element (column) is visible per line
> to ensure that content remains easily readable and accessible on smaller screens. To adjust
> the value, click the  (mobile icon) at the top of the website editor
> and adapt the number of columns. Shapes are hidden by default on mobiles.

## Save a custom building block

You can save a customized building block to reuse it elsewhere. To do so, select it, navigate to
the Style tab, and click the  (floppy disk) icon.
Click the Save button in the popup to confirm saving your custom block.

To add a saved building block to the page, navigate to the Blocks tab and drag and drop
the Custom block from the Categories section. In the popup that opens, click
the desired block in the Custom category.

> **Note:**
>
> In the Insert a block popup, click  (edit) to rename the
> custom block or  (delete) to delete it.

## Create an anchor link

Anchor links are hyperlinks that direct users to a **specific section** of a page. To create an
anchor link for a block, follow these steps:

1. Click Edit and select the block you want to link to.
2. Click  (link) at the top of the Style tab.
3. To edit the default anchor name, click Edit in the green popup message that opens.
4. Replace the anchor name and click Save & copy.

Once the anchor is saved, you can [link to it](elements.html#website-elements-links) from anywhere on your
website.

---

# General theme

Odoo offers various options to shape your website’s theme, including its
[colors], [fonts], and
[layout].

When setting up your website for the first time, you are prompted to select a theme. Hover your
mouse over the themes to see an extended preview of each one. Click on a theme to select it.

> **Note:**
>
> - If you leave without selecting a theme, your website is created using the default one.
> - You can [switch themes later] if needed.

In the website builder, the Theme tab offers various options to customize your website’s
general theme. To access it, click Edit and go to the Theme tab.

Once you have made the desired changes, click on Save to confirm and apply them to your
website.

## Theme

In the Website section, click on Switch Theme to open the theme selector.
Hover your mouse over the themes to see an extended preview of each one. Click on a theme to apply
it to your website.

## Colors

Odoo’s website editor features two main types of colors: [theme colors]
and [status colors].

### Theme colors

Theme colors refer to the set of colors displayed across all pages of your website. These are made
of five colors: three main colors and two light and dark colors.

To edit your website’s colors, go to the Colors section in the website editor, then:

- Click on the color dot you want to change, then select a Solid color or click on
  Custom to pick a specific color tone manually (or add its #HEX or RGBA code).
- Click on the paint palette icon and choose a color palette. As a result, all color customizations
  are reset; click a color dot to change a specific color.

Odoo automatically creates Color Presets for your chosen palette. These are predefined
color combinations applied to different elements of your website to provide a structured and
visually appealing design. When you select a color palette, its presets define how those colors are
distributed across different elements from a building block, such as buttons, backgrounds, and text.
If you want to modify them, click on Color Presets and click on a preset to customize it
further. Each color preset contains colors for your building block’s background, text, headings,
links, primary buttons, and secondary buttons.

![Color presets](../../../../_images/color-presets.png)

To apply a color preset to a building block on your site, select the building block, go to the
Customize tab, click the color dot located next to Background, and choose a
Theme.

> **Note:**
>
> Changing a color preset automatically updates the colors of both the default preset and the
> building blocks where the preset is used.

### Status colors

Status colors are used to indicate the status of certain actions (e.g., Success,
Warning, etc.). They’re used in pop-up messages that appear to provide feedback to
users and website visitors. To customize your website’s Status Colors, scroll down to
the Advanced section and click on the dots to change their color.

> **Tip:**
> ![Status color selection](../../../../_images/advanced.png)
> ![Success pop-up](../../../../_images/success.png)

## Page layout

The Page layout option in the Website section allows you to change the
overall display and spacing of building blocks and website elements on pages. Click the dropdown
menu and select the desired layout. Under Page Layout, customize your
Background by choosing an Image, using a selected image in a
Pattern, or leaving it blank.

## Fonts

Odoo allows you to customize the font family and size for specific elements on your website,
including paragraphs, headings, buttons, and input fields.

- Font Family: In the Paragraph, Headings, and
  Button sections, select a font from the dropdown menu.
- Font Size: In the Paragraph, Headings, Button, and
  Input Fields sections, use the Font Size field to set a default size.
  Click the  (arrow) icon to expand the section and define custom sizes
  (e.g., based on the heading level, button size, etc.).

Additionally, each element-specific section offers extra styling options, such as
Line Height and Margins, for further customization.

### Custom fonts

It is possible to use fonts on your website that are not offered by default in Odoo. To add a custom
font, click the dropdown menu related to the Font Family field and select Add
a Custom Font at the bottom of the dropdown menu. In the pop-up window:

- To add a Google font, click on Select a Google Font and click on the desired font
  in the list. Toggle off the Serve font from Google servers if your website is operated
  from a location where regulations require compliance with laws such as, but not limited to, the
  European Union’s GDPR. This will ensure that the Google Font is stored on your website’s server
  instead of Google’s.
- To upload a custom font from your computer, click on Choose File.

Once done, click on Save and Reload.

## Button styles

To customize the style of your website’s primary and secondary buttons, navigate to the
Button section in the website editor and edit the relevant options:

- Click the arrow next to the Primary Style or Secondary Style fields and
  select one of the available styles for each type of button: Fill, Outline,
  or Flat. When selecting Outline, the Border Width option
  appears below, allowing you to adjust the width of the button’s outline.
- [Modify the fonts].
- Adjust the Padding to change the size of the spacing (in pixels) around the buttons’
  labels.
- Customize the buttons’ border radius using the Round Corners option.
- Add an animation when a button is clicked in the On Click Effect dropdown menu.

![Primary and secondary buttons](../../../../_images/buttons.png)
> **Note:**
>
> You can define custom Small and Large sizes for the buttons’
> Padding, Font Size, and Round Corners: Click on the
>  (arrow) icon and use the related fields.
>
> ![Button padding, font size and round corners settings](../../../../_images/button-settings.png)

## Link style

In the Link section, click on Link Style to choose the appearance of links
on your website. Select No Underline, Underline On Hover, or
Always Underline in the dropdown menu.

---

# Elements

Elements help structure and present content effectively. They range from text-based components like
[titles], [lists] and
[text highlights] to interactive ones such as
[buttons] and [links]. Visual elements
like [images], [icons],
[videos], and [animations] can
also be added to improve content presentation and organization.

To add or modify a website element:

1. Navigate to the relevant website page and click on Edit.
2. Click the section on the page where you want to add or modify an element.
3. Make the necessary changes.
4. Click on Save.

> **Note:**
>
> The default styles for headings, buttons, links, and paragraph text, for example, are defined in
> the [Theme tab](themes.html) of the website editor.

![Type / to add website elements.](../../../../_images/elements-webdesign.png)

## Titles

Titles define headings and organize website content into different levels for clarity and structure.
To insert a title, type `/title`, choose the heading style (Heading 1,
Heading 2, or Heading 3), and type the text.

> **Note:**
>
> Alternatively, type the text, select it, and choose the appropriate style from the
> Inline Text section in the Customize tab of the website editor. Additional
> formatting options, such as fonts and colors, are also available in this section.

## Buttons

Buttons are interactive elements that allow to link to another page or to a page anchor. To insert a
button:

1. Type `/button`.
2. Enter the button’s label in the Link Label field.
3. Add the URL or Email. Type `/` to search for a page and `#` to link to an anchor.
4. Set the Style, Size, and Layout to
   define the button’s appearance.
5. If needed, toggle the switch to open the linked page or anchor in a new tab.
6. Click Apply to save changes.

> **Note:**
>
> To modify an existing button, click the button and edit the options in the
> Inline text section of the website editor.

## Images

To insert an image:

1. Type `/image`.
2. [Search the Unsplash database](../../../general/integrations/unsplash.html) or click
   Upload an image to choose a file from your local images.
3. Click Add.
4. To customize the image, click on the image and edit the options in the Image
   section of the website editor. For example:

   - Replace the image.
   - Define an [alt tag](https://help.siteimprove.com/support/solutions/articles/80000448480-where-are-alt-tags-used-and-why-are-they-important)
     in the Description field.
   - Enter a title tag in the Tooltip field. This text will appear when visitors hover
     their mouse over the image.
   - Add a Shape; some shapes also allow for color customization.
   - Adjust the image’s Width, e.g., to improve performance. A smaller size may be
     suggested if it is sufficient for display.
   - Resize the image using the Transform tool.
   - Adjust the Padding to add space (in pixels) around the image.
   - Etc.

## Videos

To add a video, type `/video`, insert the URL, and turn on the desired options:

- Autoplay: to automatically play the video when the page is accessed. The video is
  automatically muted by default.
- Loop: to play the video on a loop.
- Hide player controls
- Hide fullscreen button
- Start at: to define the timestamp where the video should start, in `MM:SS` format.

## Icons

To insert an icon, type `/image`, go to the Icons tab, select an icon, and click
Add. To modify an icon, click on it and use the Icon section of the website
editor to customize options, such as Color, Size, [Animations], Shape, etc.

## Links

Links are used to connect different pages and resources, guiding visitors and improving navigation.
To add a link, type `/link`, then, in the pop-up that opens, enter the link’s Label and
add the URL or Email. Type `/` to search for a page and `#` to link to an [anchor](building_blocks.html#website-building-blocks-anchor).

> **Note:**
>
> By default, the Style field is set to Link. Select a different style to
> transform the link into a [button].

## Lists

Lists help organize content clearly, making information easier to read and improving web pages’
structures. Type `/list` and choose from three different types of lists: Bulleted lists,
Numbered lists, or Checklists.

## Text highlights

Highlights can be added to titles and text using in the Inline Text section of the
website editor. To add a highlight:

1. Select the text or title you want to highlight.
2. In the website editor, click on Highlight.
3. Select the highlight style.
4. Modify its Color.
5. Choose its Thickness.

![Highlight texts and titles](../../../../_images/highlights-elements.png)

## Animations

Animations are used to add movement to [building blocks](building_blocks.html) and website
elements such as images and text. Three types of animation are available: On Scroll,
On Appearance, and On Hover (for images only).

To add an animation to a website element:

1. Click on the element.
2. In the website editor, go to the relevant section for the element (e.g., Button,
   Column, Inline Text, etc.).
3. In the Animation field, select the desired animation type.
4. Customize the animation settings as needed. Available options vary based on the selected
   animation type.

### Animations on scroll

For animations on scroll, it is possible to:

> - Choose In to add the animation when the element enters the screen and Out
>   to add it when it leaves the screen.
> - Select an Effect.
> - Choose the Direction of the effect.
> - Adapt the Intensity of the effect.
> - Define the Scroll Zone, where the first value represents the percentage of the screen
>   shown when the effect starts, and the second value represents its percentage at the end.

### Animations on appearance

For animations on appearance, it is possible to:

> - Choose among different effects.
> - Choose the Direction of the effect.
> - Pick a Trigger option to define when the animation occurs: either the
>   First Time only or Every Time.
> - Adapt the Intensity of the effect.
> - If you want the animation to be triggered after a number of seconds, define this number in the
>   Start After field.
> - Choose a Duration for the animation.

### Animations on hover (for images only)

Animations On hover can be added to [images]. You can
choose the Effect of the animation, as well as the Color and the
Stroke Width.

> **Note:**
>
> [Odoo HTML editor](../../../essentials/html_editor.html)

---

# Visibility

You can choose to display or hide building blocks based on a visitor’s:

- device type (mobile or computer),
- country (IP-based geolocation),
- website language,
- [UTM parameters](../reporting/link_tracker.html), and
- login state.

## Mobile/computer

To toggle the visibility of a building block based on the visitor’s device type:

- Open the website editor and select a block.
- In the Customize tab, under the block’s customization options, look for
  Visibility.

  - Click the  (Show/Hide on Desktop) button to hide
    the block for users visiting your website from a computer.
  - Click the  (Show/Hide on Mobile) button to hide the block
    for users visiting your website from a mobile device.
- Click Save to apply the changes.

It is also sometimes possible to hide elements within blocks. It is mostly used to hide specific
elements inside blocks that may be too wide to be correctly displayed on mobile devices. To see if
the option is available, select an element within a block and look for the Visibility
option under the element’s customization option.

> **Tip:**
>
> The selected image is hidden on mobile devices.
>
> ![Example of an column element hidden on mobile devices](../../../../_images/element-visibility.png)

## Conditions

To access the country, website language, UTM parameters, and login state conditions:

- Open the website editor and select a building block.
- In the Customize tab, look for Visibility.
- Click No condition and select Conditionally instead to display the
  different options:

  - Country: the country of the visitor’s IP address.
  - Languages: the website language used by the visitor.

    > **Note:**
    >
    > This option is only available if more than one [language is installed](../configuration/translate.html).
  - UTM Campaign: the selected campaign.
  - UTM Medium: the selected medium of any campaign.
  - UTM Source: the selected source of any campaign.
  - Users: select whether the visitor should be Logged In or
    Logged Out to view the block. By default, the option is set to Visible
    for Everyone.
- For one or more of the first five options, choose if the block should be Visible for
  or Hidden for, then click Choose a record… and select it.

> **Note:**
>
> - You can select multiple records for each option by clicking Choose a record…
>   again.
> - Click the  (remove) button to remove an option.

Click Save to apply the changes.

> **Tip:**
>
> A block with the following configuration will only be displayed to visitors with a Belgian IP
> address, for which the website is displayed in French, unless they visit the page using the
> `Sales` campaign tracked URL.
>
> ![Example of a block configured with several visibility conditions](../../../../_images/visibility-conditions.png)

## Invisible elements

Blocks and elements with custom visibility settings are listed at the bottom of the website editor
sidebar. You can preview how the page would look like by clicking the
(visible) button to hide a block or element, or the
(hidden) to show it in the website editor.

![Blocks and elements with custom visibility settings displayed at the bottom of the editor](../../../../_images/invisible-elements.png)

---

# Structure

Structure your website using [pages](structure/pages.html), provide consistent visual
and navigational framework with [headers and footers](structure/header_footer.html) and
optimize your online presence with [Search Engine Optimization (SEO)](structure/seo.html).

[#### Pages

Create pages for your website and customize their content and appearance to your needs.](structure/pages.html)[#### Headers and footers

Create a consistent look and feel for your website by customizing the header and footer, and
help users navigate through web pages effectively by providing clear menus, links, and calls
to action.](structure/header_footer.html)[#### Search Engine Optimization (SEO)

Improve your website’s visibility and ranking in search engine results.](structure/seo.html)

> **Note:**
>
> [Odoo Tutorials: Website](https://www.odoo.com/slides/website-25)

---

# Pages

Odoo allows you to [create] different kinds of webpages,
including with the help of [AI], [publish] them, and define their structure and visibility by configuring
[page properties]. Pages can be [duplicated], [deleted], and [redirected].

> **Note:**
>
> **Static** pages, such as the homepage or [custom] pages,
> contain fixed content that does not change dynamically. You can manually create these pages,
> define their URLs, and adapt their [properties] as needed.
>
> **Dynamic** pages, on the other hand, display content that changes automatically based on the
> data in the database and user interaction (e.g., filtering). They are generated automatically by
> Odoo, for example, when installing an app or module (e.g., `/shop` or `/blog`) or publishing a
> new [product](../../ecommerce.html) or [blog post](../../blog.html). Dynamic pages are managed
> differently from static pages.

## Page creation

Website pages can be created from the **frontend** and the **backend**.

> 1. To create a new website page:
>
>    - Either open the **Website** app, click New  in the top-right
>      corner, then select Page;
>    - Or go to Website ‣ Site ‣ Pages and click New.
> 2. In the New Page pop-up, select a template. Templates are grouped by type:
>
>    - Basic: Multi-purpose page. A blank page is also available to start from scratch.
>    - About: Information about the brand and company.
>    - Landing Pages: Summary of company content and information.
>    - Gallery: Photos and media showcase.
>    - Services: Overview of the services offered by the company.
>    - Pricing Plans: Overview of the subscriptions and prices.
>    - Team: The people behind the company.
>    - Custom: Custom-created templates. To add a custom template, open the page you
>      want to save as a template and [edit the page’s properties].
> 3. In the New Page pop-up:
>
>    - Enter a Page Title. This title is used in the menu and the page’s URL.
>    - Disable Add to menu if the page should not appear in the menu.
>    - Enable Generate text to use the [AI] tool to
>      build the page.
> 4. Click Create.
> 5. If needed, [customize the page’s content and appearance](../web_design.html) using the website
>    editor or [translate](../configuration/translate.html#translate-translate) it, then click Save.
> 6. [Publish] the page.

### AI webpage generator

To generate content using AI when [creating a new page], follow
these steps:

1. After choosing a template, in the New Page pop-up, toggle the AI Generate
   Text switch.
2. In the Instructions field, enter a short description of the page being created. This
   should include a few important keywords that define the page’s focus and scope.
3. Select one of the tone options for the page, such as Concise,
   Professional, Friendly, Persuasive, or
   Informative.
4. Click Create with AI. It may take a few moments for the webpage to load.

![The new page pop-up window with the "AI Generate text" options.](../../../../_images/generate-page.png)
> **Note:**
>
> - The AI application does **not** need to be installed on the database to use the webpage
>   generator.
> - Content created by the AI generator can be customized using the [website editor](../web_design.html).
> - The AI webpage generator is not available for the *Blank* page type.
> - The webpage generator may create [buttons](../web_design/elements.html#website-elements-buttons). Before publishing
>   the webpage, confirm that all buttons are linked to an active webpage.

> **Note:**
>
> - [Web design](../web_design.html)
> - [AI](../../../productivity/ai.html)

## Publishing/unpublishing pages

Pages need to be published to make them visible to website visitors. To publish or unpublish a
page, access it and toggle the switch in the upper-right corner from Unpublished
to Published, or vice versa.

![Unpublished/Published toggle](../../../../_images/un-published-toggle.png)
> **Note:**
>
> It is also possible to:
>
> > - Publish/unpublish a page from the [page properties].
> > - Publish/unpublish several pages at once. To do so, go to Website ‣ Site
> >   ‣ Pages, select the pages, then click  Actions and select
> >    Publish or  Unpublish.

## Page properties

To modify a [static page’s] properties, access the page you wish to
modify, then go to Website ‣ Site ‣ Properties, where the following properties
can be adapted:

> - Page Title: Modify the page’s title.
> - Page URL: Modify the page URL in the field. In this case, you can redirect the
>   old URL to the new one if needed. To do so, enable Redirect Old URL, then select the
>   Type of [redirection]:
>
>   > - 301 Moved permanently: to redirect the page permanently.
>   > - 302 Moved temporarily: to redirect the page temporarily.
> - In Menu: Disable if the page should not appear in the menu. Click the
>    Edit Menu link to modify the menu.
> - Is Homepage: Enable if the *static* page should serve as the homepage of the website.
> - Published: Enable it to publish the page.
> - Publishing Date: To publish the page at a specific date and time, click the field,
>   set the date and time, then press **Enter** or click Apply to validate the selection.
> - Indexed: Disable if the page should not appear in search engine results.
> - Visibility: Select who can access the page:
>
>   > - Public: Everyone can access the page.
>   > - Signed In: Only signed-in users can access the page.
>   > - Restricted Group: Select the [user access group(s)](../../../general/users/access_rights.html) in the Authorized Groups field.
>   > - With Password: Type the password required to access the page in the
>   >   Password field.
> - Is a Template: Toggle the switch to save the page as a template. It is now available
>   in the Custom category when [creating a new page].

### Duplicating pages

To duplicate a page, access the page, then go to Website ‣ Site ‣ Properties,
and click Duplicate Page. In the Confirmation window, enter a
Page Name, then click Ok. By default, the new page is not published; it is
added after the originally duplicated page in the menu. Use the [menu editor](header_footer.html)
to remove it from the menu or change its position.

> **Note:**
>
> You can also duplicate one or several pages by going to Website ‣ Site ‣
> Pages. Select the relevant page(s), click  Actions, and select
>  Duplicate.

### Deleting pages

To delete a page, proceed as follows:

1. Access the page, then go to Website ‣ Site ‣ Properties and click
   Delete Page.
2. The Delete Page pop-up shows all links referring to the page you want to delete,
   organized by category. To ensure website visitors do not land on an error page, update all links
   on the website that refer to the page. To do so, expand a category, then click on a
   link to open it in a new window. Alternatively, you can set up a [redirection] for the deleted page.
3. Once you have updated the links (or set up a [redirect]),
   tick the I am sure about this. checkbox, then click Delete.

> **Note:**
>
> You can also delete one or several pages by going to Website ‣ Site ‣ Pages.
> Select the relevant page(s), click  Actions, and select
>  Delete.

## URL redirect mapping

URL redirect mapping involves sending visitors and search engines to a URL other than the one they
initially requested. This technique is used, for example, to prevent broken links when
[deleting a page], [modifying its URL], or migrating the site from another platform to an Odoo
[domain](../configuration/domain_names.html). It can also be used to improve [Search Engine Optimization (SEO)](seo.html).

> **Note:**
>
> - A redirect record is added automatically every time you [modify a page’s URL] and enable Redirect Old URL.
> - Redirections can be configured for [static and dynamic pages].

To access existing URL redirections and create new ones, [activate the developer mode](../../../general/developer_mode.html) and go to Website ‣ Configuration ‣
Redirects. To create a redirection, click New in the Rewrite view, then
adapt the fields:

- Name: Enter a name to identify the redirect.
- Action: Select the type of redirection:

  > - 404 Not found: Visitors land on a 404 error page when they try to access an
  >   unpublished or deleted page.
  > - 301 Moved permanently: for permanent redirections of unpublished or deleted
  >   [static pages]. The new URL is shown in search engine results,
  >   and the redirect is cached by browsers.
  > - 302 Moved temporarily: for short-term redirections, for example, if you are
  >   redesigning or updating a page. The new URL is neither cached by browsers nor shown in search
  >   engine results.
  > - 308 Redirect / Rewrite: for permanent redirections where the original URL is
  >   rewritten (typically used for [dynamic pages]). The URL is
  >   renamed; the new name appears in search engine results and is cached by browsers. Use this
  >   redirect type to rename a dynamic page, for example, if you wish to rename `/shop` into
  >   `/market`.
- URL from: Enter the URL to be redirected (e.g., `/about-the-company`) or search for
  the desired [dynamic page] and select it from the list.
- URL to: For 301, 302, and 308 redirects, enter the URL to be redirected to. If you
  want to redirect to an external URL, include the protocol (e.g., `https://`).
- Website: Select a specific website.
- Active: Toggle the switch off to deactivate the redirection.
- Sequence: To define the order in which redirections are performed, e.g., in the case
  of redirect chains (i.e., a series of redirects where one URL is redirected to another one, which
  is itself further redirected to another URL).

> **Warning:**
>
> 301 and 302 redirects are commonly used to redirect traffic from [unpublished] or [deleted] *static* pages to
> new pages. The 308 redirect is typically used for permanent URL rewrites, especially for
> *dynamic* pages. A 404 status is used when a page no longer exists, and no redirection is
> configured.

> **Note:**
>
> - [Google documentation on redirects and search](https://developers.google.com/search/docs/crawling-indexing/301-redirects)
> - [Search Engine Optimization (SEO)](seo.html)

---

# Headers and footers

The website header is the top section of a web page and usually contains elements such as the logo,
the [menu], the search bar, the sign-in/customer account
button, etc. The footer is displayed at the bottom of a web page and usually contains information
such as contact details, links, legal notices, and other options.

## Header design

To modify the header’s design, click on Edit, then click on the header. The following
options are available in the Header section of the Customize tab in the
website editor:

- Choose a Template from the drop-down menu.
- Select Background settings to change the color palette through different
  [Theme styles](../web_design/themes.html#website-themes-theme-colors), Custom color options, and
  Gradient ones.
- When adding a Border to the header, its size, style, and color can be defined.
- Adapt Round corners to fit the design.
- Add a Shadow and define its Color, Offset, Blur,
  and Spread.
- Add a Scroll Effect. Hover on an effect to preview it.
- Choose the Header Position between Regular, Hidden, and
  Over The Content. When Over The Content is selected, you can customize
  the Background and Text Color.
- Show or hide Elements such as text, the search bar, Sign in button, social
  media links, Contact us button, and logo.

To finalize changes, click on Save.

> **Note:**
>
> To hide the header, click on Edit, click on the header, and go to the
> Theme tab of the website editor. Scroll down to the Advanced section and
> toggle the Show Header switch to hide/show the header.

## Header content

Menus organize the header’s content and help users navigate through web pages effectively.
User-friendly and well-structured menus also play a crucial role in improving
[search engine rankings](seo.html).

### Menu editor

The menu editor allows to edit the website’s header and add
[menu items] and
[mega menus].

To edit the header’s content, go to Website ‣ Site ‣ Menu Editor. From there,
you can:

- **rename** a menu item or change its URL using the Edit Menu Item icon;
- **delete** a menu item using the Delete Menu Item icon;
- **move** a menu item by dragging and dropping it to the desired place in the menu;
- **create a regular drop-down menu** by dragging and dropping the sub-menu items to the right,
  underneath their parent menu.

![Menu editor with sub-menus](../../../../_images/menu-editor.png)
> **Note:**
> > You can also access the menu editor by clicking Edit, selecting any menu item, and
> > clicking the Edit Menu icon.
>
> ![Access the Menu editor while in Edit mode.](../../../../_images/edit-menu-icon.png)

### Add menu items

By default, pages are added to the menu as drop-down menu items when
[they are created](pages.html). To add a new menu item, follow these steps:

1. Go to Website ‣ Site ‣ Menu Editor.
2. In the menu editor, click Add Menu Item.
3. In the pop-up window, enter the Name to be displayed in the menu.
4. Type `/` in the URL or Email field to search for a page on your website or `#` to
   search for an existing custom anchor.
5. Click OK.
6. Edit the [menu structure] if needed, then
   Save.

#### Menu item design

To modify the menu items, click on Edit, click on a menu item, then go to the
Navbar section of the website editor. The following options are available:

- Adapt the Mobile Alignment.
- Choose the Font for the menu items.
- Change the font size, color, and alignment in the Format field.
- Select a Links Style to highlight the current page in the menu.
- Change the [style of the header buttons](../web_design/themes.html#website-themes-button-styles).
- Choose to display the Sub Menus On Hover or On Click.

> **Note:**
>
> The fields available in the Navbar section can vary depending on the chosen template.

To finalize changes, click on Save.

### Mega menus

Mega menus are similar to drop-down menus, but instead of a simple list of sub-menus, they display a
panel divided into groups of navigation options. This makes them suitable for websites with large
amounts of content or [e-commerce websites](../../ecommerce.html), as they can help include all of
your web pages or [e-commerce categories](../../ecommerce/configuration/categories_variants.html#ecommerce-categories-variants-categories) in the
menu while still making all menu items visible at once.

![Mega menu in the navigation bar.](../../../../_images/mega-menu1.png)

To create a mega menu, go to Website ‣ Site ‣ Menu Editor and click
Add Mega Menu Item. Enter the Name of the mega menu in the pop-up, click
OK, then Save.

To adapt the options and content of the mega menu, click on a mega menu item in the header, then
click Edit. Mega menus are composed of building blocks, which means you can customize
each component individually. For example:

- Edit the text directly in the building block.
- Edit a menu item’s URL by selecting the menu item and clicking the Edit link button
  in the small preview pop-up. Type `/` to search for a page on your website, or `#` to search for
  an existing custom anchor.

  ![Edit a mega menu option.](../../../../_images/mega-menu-option.png)
- Move a menu item by dragging and dropping the related block to the desired position in the mega
  menu.
- Delete a menu item by deleting the related block.

To adapt the general layout of the mega menu, go to the Customize tab of the website
editor, then, in the Mega Menu section:

- Choose a Template.
- Pick the Size: either Full-Width or Narrow.

To finalize changes, click on Save.

### Hide a dynamic menu item for non-logged in users

To hide a dynamic menu item (i.e., a menu item generated automatically by Odoo, for example, when
you install an app or module, such as `Events`, `Courses`, etc.) for non-logged in users, follow
these steps:

1. [Enable developer mode](../../../general/developer_mode.html#developer-mode).
2. Go to Website ‣ Configuration ‣ Menus.
3. Expand the list of menus for the relevant website if needed, then click the menu item you wish to
   hide.
4. In the Visible Groups section, click Add a line under
   Group Name.
5. Search for the group User types / Portal, select it, then click Select.
6. Save.

> **Note:**
>
> To hide the `Shop` menu item, [restrict ecommerce access to logged-in users](../../ecommerce/configuration/customer_accounts.html).

## Footer design

To modify the footer, click on Edit, click on the footer, and in the Footer
section of the Customize tab in the website editor:

- Select a Template.
- Choose its Colors.
- Choose a Slideout Effect: Regular (i.e., no effect),
  Slide Hover, or Shadow.
- Toggle the Copyright switch to hide or show the copyright.
- Choose the Border size.
- Add a Shadow.
- Add a Scroll Top Button and choose its position.
- Hide or show the footer by toggling the Page visibility switch.

To finalize changes, click on Save.

---

# Search Engine Optimization (SEO)

Search Engine Optimization, often abbreviated as SEO, is a digital marketing strategy to improve a
website’s visibility and ranking in search engine results (e.g., in Google). It involves optimizing
various elements on your website, including its content, social sharing, URLs, images, and page
speed.

> **Note:**
>
> - Several modules are provided to help build the website’s content, such as
>   [eCommerce](../../ecommerce.html), [Blog](../../blog.html), [eLearning](../../elearning.html), and [Forum](../../forum.html).
> - All provided [themes](../web_design/themes.html) are built with the [Bootstrap](https://getbootstrap.com/) CSS framework to ensure responsive layouts across desktop,
>   tablet, or mobile, which can support SEO.

> **Note:**
>
> [Magic Sheet - Optimize your website [PDF]](https://drive.google.com/drive/folders/1Ywip4tWF2DPkcBaEbeXJxIZg2CjkwKgb)

## Content optimization

To optimize a webpage’s SEO, access the page, then go to Website ‣ Site ‣
Optimize SEO.

![Search Engine Optimization](../../../../_images/search-engine-optimization.png)
> **Note:**
>
> Changing the title of a blog post or the name of a product automatically updates the link to the
> related webpage. The old link still functions as a
> [301 redirect](pages.html#website-pages-url-redirection) is created, maintaining the SEO.

> **Note:**
>
> - Click Fill with AI to automatically generate a meta title, a description, and get
>   keyword suggestions.
> - Remove incorrect URLs from the Broken Link field and select valid ones to
>   prevent errors.

### Keywords and meta tags

There are two types of keywords in SEO, which serve different purposes.

#### In-text keywords

In-text keywords appear naturally throughout a page’s visible content (titles, headings, and body
text) and help search engines determine the topic and relevance of the page. These keywords have a
real impact on ranking. They cannot be edited in the optimize SEO pop-up.

> **Warning:**
>
> It is strongly recommended to only use one H1 title per page for SEO.

#### Meta tags and meta keywords

**Meta tags** are HTML elements that provide information about a webpage to search engines and
website visitors. They play a crucial role in SEO by helping search engines understand the content
and context of a webpage and attract visitors with appealing content. They can be edited in the
optimize SEO pop-up. There are two types of meta tags:

- Title tags specify a webpage’s title and are displayed as a clickable link in search
  engine results. They should be concise, descriptive, and relevant to the page’s content. You can
  update the title tag of your webpage or keep it empty to use the default value based on the page’s
  content.
- Description tags summarize the webpage’s content, often displayed in search engine
  results below the title. They are used to encourage the user to visit the page.
  Update the description tag of the webpage, or keep it empty to use the default description based
  on the page’s content.

> **Note:**
>
> The Preview card displays how the title and description tags should appear in search
> results. It also includes the URL of your page.

**Meta keywords** are placed in a hidden HTML tag `<meta name="keywords">`. Once used to describe a
page’s topic, this tag is now ignored by major search engines and has little or no impact on SEO.
To edit Keywords, enter the keywords you consider essential in this field and click
Add to see how they are used at different levels in your content (H1, H2, page title,
page description, page content) and the related searches in Google. The tool also suggests relevant
keywords.

### Images

The size of images has a significant impact on page speed, which is an essential criterion for
search engines to optimize SEO ranking.

> **Note:**
>
> Compare how your website ranks using [Google Page Speed](https://pagespeed.web.dev/?utm_source=psi&utm_medium=redirect)
> or [Pingdom Website Speed Test](https://tools.pingdom.com/).

Odoo automatically compresses uploaded images and converts them to `Webp`. With this file format,
photos are smaller, which increases the page loading speed and, therefore, gives a better ranking in
SEO. All images used in Odoo official [themes](../web_design/themes.html) are also compressed by
default.

> **Note:**
>
> Third-party themes may not compress images efficiently.

**To modify an image** from a webpage, select the image, click Edit, then go to the
Customize tab, and adapt the Format in the Image section.

> **Warning:**
>
> Alt tags are used to provide context to what an image is displaying, informing search engine
> crawlers and allowing them to index an image correctly. Adding alt tags keywords in the
> Description field is essential from an SEO perspective. This description is added to
> the HTML code of your image, and it is shown when the image cannot be displayed.

#### Image for social share

When you share a page on social media, the website logo is selected by default.
Search the [Unsplash image library](../../../general/integrations/unsplash.html) or upload any
other image by clicking the  (upload) button.

> **Note:**
>
> To set a default social share image, go to Website ‣ Configuration ‣
> Settings. Under the Tracking & SEO section, enable
> Default Social Share Image.

> **Note:**
>
> The Social Preview card displays how the page’s information would appear when
> shared.

## Indexation

Website indexation is the process by which search engines, such as Google, discover, analyze, and
store information about a website’s content in their database. Search engine bots, known as crawlers
or spiders, visit web pages and follow links to collect data, including text, images, and other
media. The purpose of indexation is to make a website’s content searchable and discoverable to
users. Without being indexed, a website or a specific page on that site will not appear in search
engine results, regardless of how relevant or well-designed it is. Indexation is a fundamental step
in SEO, serving as the foundation for a website’s visibility
and organic traffic.

> **Note:**
>
> **When you first create your website on Odoo, it will not appear directly in search engine
> results.** Search engines need time to crawl and index it, which can take anywhere from a few
> days to several weeks. For Google, you can use the [Search Console](../configuration/google_search_console.html) and request indexing for specific URLs, though this
> does not guarantee faster results. If you have an existing website and are migrating, your
> previous website may still appear instead of the new one during that timeframe.

### SEO impact when migrating your existing website to Odoo

In most cases, migrating to Odoo will not negatively impact the website’s SEO. While no platform can
guarantee that rankings will remain unchanged, follow these best practices to significantly reduce
the risk.

- Keep the existing content.
- Implement [redirects](pages.html#website-pages-url-redirection) from old URLs to their new
  counterparts.
- Monitor traffic and indexation to make sure that everything is going well, using
  [Google Search Console](../configuration/google_search_console.html).

By doing this, search engines reindex the site and maintain its visibility in search results.

> **Note:**
>
> It is normal to experience a traffic decrease in the first days.

### Prevent a page from being indexed

To effectively prevent a page from appearing in search engine results, use one of the following
methods:

> - **noindex tag:** Access the page’s [properties](pages.html#website-pages-page-properties) and toggle
>   the Indexed switch off.
>
>   > **Note:**
>   >
>   > This option is not yet available for [dynamic pages](pages.html#website-pages-page-type).
> - **404 or 403:** Configure the page to return a 404 (Not Found) or 403 (Forbidden) HTTP status
>   code. These codes signal to search engines that the page does not exist or is inaccessible,
>   leading to its eventual removal from the index.
>
>   > - **404:** [Configure a 404 redirection.](pages.html#website-pages-url-redirection)
>   > - **403:** Access the page’s [properties](pages.html#website-pages-page-properties)
>   >   and toggle the Visibility switch off or [unpublish the page](pages.html#website-pages-un-publish-page).
> - **Google Search Console:** Use Google Search Console to request the removal of specific URLs from
>   Google’s index.

> **Note:**
>
> - [Google Search Console](../configuration/google_search_console.html)
> - [Pages](pages.html)

### Prevent a website from being indexed

To prevent a website from appearing in search engine results, go to
Configuration ‣ Settings, then in the Website Info section, add a
random value in the Domain field. Doing so automatically inserts the following tag into
the page source:

```
<meta name="robots" content="noindex"/>
```

This tag instructs search engines not to index the site. After applying the change, it may take
several days or weeks for search engines to update their results and remove the website.

> **Tip:**
>
> This can be used to prevent websites from test databases from appearing in search results.

## Sitemap

The sitemap points out website pages and their relation to each other to search engine crawlers.
Odoo generates a `/sitemap.xml` file, including all URLs. For performance reasons, this file is
cached and updated every 12 hours.

> **Note:**
>
> If your website has a lot of pages, Odoo automatically creates a Sitemap Index file, respecting
> the [sitemaps.org protocol](http://www.sitemaps.org/protocol.html), grouping sitemap URLs in
> 45000 chunks per file.

Every sitemap entry has three attributes that are computed automatically:

- `<loc>`: the URL of a page.
- `<lastmod>`: last modification date of the resource, computed automatically based on the related
  object. For a page related to a product, this could be the last modification date of the product
  or the page.
- `<priority>`: modules may implement their priority algorithm based on their content (for example,
  a forum might assign a priority based on the number of votes on a specific post). The priority of
  a static page is defined by its priority field, which is normalized (16 is the default).

> **Note:**
>
> To prevent pages from appearing in a sitemap, go to Site ‣ Properties, and
> toggle off the Indexed feature.
>
> > ![toggle off the “Indexed” field](../../../../_images/page-properties.png)

## robots.txt

A `robots.txt` file instructs search engine crawlers which parts of a website they are permitted to
access. Its primary purpose is to:

> - **Prevent overloading the website:** By guiding crawlers away from certain sections, robots.txt
>   helps manage server load.
> - **Control access to resources and detailed descriptions:** It can prevent crawlers from accessing
>   media files (images, videos), CSS stylesheets, and JavaScript files, and from reading the content
>   (text) of specific pages.

When indexing your website, search engines first look at the robots.txt file. Odoo automatically
creates one robot.txt file available on `mydatabase.odoo.com/robots.txt`.

> **Note:**
>
> Reputable bots adhere to robots.txt; others may require blocking via
> [Cloudflare](../configuration/domain_names.html#domain-name-naked-cloudflare) on your custom domain.

### Edit robots.txt

By editing a robots.txt file, you can control which site pages are accessible to search engine
crawlers. To add custom instructions to the file, go to Website ‣ Configuration
‣ Settings, scroll down to the SEO section, and click Edit robots.txt.

> **Tip:**
>
> If you do not want robots to crawl the `/about-us` page of your site, you can edit the
> robots.txt file to add `Disallow: /about-us`.

> **Warning:**
>
> While `robots.txt` prevents content from being crawled, **it does not guarantee that a page
> will not be indexed**. A page can still appear in search results if it is linked to from other
> crawled pages (indexed by “reference”). Google generally does not recommend using robots.txt to
> block webpages that you wish to keep out of search results entirely.

## Advanced features

### Structured data markup

Structured data markup is used to generate rich snippets in search engine results. It is a way for
websites to send structured data to search engine crawlers, helping them understand your content and
create well-presented search results.

By default, Google supports many [rich snippets](https://developers.google.com/search/blog/2009/05/introducing-rich-snippets)
for content types, including Reviews, People, Products, Businesses, Events, and Organizations.

Microdata is a set of tags, introduced with HTML5, that help search engines better understand your
content and display it in a relevant way. Odoo implements microdata as defined in the schema.org
[specification](https://schema.org/docs/gs.html) for events, eCommerce products, forum posts, and
contact addresses. This allows your product pages to be displayed in Google using extra information
like the price and rating of a product:

![snippets in search engine results](../../../../_images/rich-snippet.png)

### Hreflang HTML tags

Odoo automatically includes `hreflang` and `x-default` tags in the code of your website’s
multilingual pages. These HTML attributes are crucial in informing search engines about a specific
page’s language and geographical targeting.

> **Note:**
>
> [Translations](../configuration/translate.html)

---

# Configuration

---

# Domain names

Domain names are text-based addresses identifying online locations, such as websites. They provide a
more memorable and recognizable way for people to navigate the internet than numerical IP addresses.

**Odoo Online** and **Odoo.sh** databases use a **subdomain** of the `odoo.com` **domain** by
default (e.g., `mycompany.odoo.com`).

However, you can use a custom domain name instead by [registering a free domain name] (only available for Odoo Online databases) or by [configuring a
domain name you already own].

> **Note:**
>
> - [Odoo Tutorials: Register a free domain name [video]](https://www.odoo.com/slides/slide/register-a-free-domain-name-1663)
> - [Magic Sheet - Website domain configuration [PDF]](https://drive.google.com/drive/folders/1sXbp7sC6TKG2v-8hcRAMhA6ftKmRxba_)

## Register a free domain name with Odoo

To register a one-year free domain name for your Odoo Online database, sign in to your account and
go to the [database manager](https://www.odoo.com/my/databases). Click the
(gear) button next to the database name and select  Domain
Names.

![Accessing a database's domain names configuration](../../../../_images/domain-names.png)

Search for the desired domain name and check its availability.

![Searching for an available domain name](../../../../_images/domain-search.png)
> **Note:**
>
> Ensure the Website app is installed if the domain name registration option does not appear.

Select the desired domain name, fill in the Domain Owner form, and click
Register. The chosen domain name is directly linked to the database.

![Filling in the domain owner information](../../../../_images/domain-owner.png)

Next, you should [map your domain name to your Odoo website].

> **Warning:**
>
> A verification email from `noreply@domainnameverification.net` will be sent to the email address
> provided in the Domain Owner form. It is essential to verify your email address to
> keep the domain active and receive the renewal quote before expiration.

The domain name registration is free for the first year. After this period, Odoo will continue to
manage the domain in partnership with **Gandi.net**, the domain name registrar, and you will be
charged [Gandi.net’s renewal rate](https://www.gandi.net/en/domain). Odoo sends a renewal
quotation every year to the email address mentioned in the Domain Owner form several
weeks before the expiration date of the domain. The domain is renewed automatically when the
quotation is confirmed.

> **Note:**
>
> - The offer is only available for **Odoo Online** databases.
> - The offer is limited to **one** domain name per client.
> - The offer is limited to the registration of a **new** domain name.
> - The offer is available to *One App Free* plans. Ensure that your website contains enough
>   original content for Odoo to verify that your request is legitimate and respects [Odoo’s
>   Acceptable Use Policy](https://www.odoo.com/acceptable-use). Given the high number of
>   requests, it can take Odoo several days to review them.

### DNS records

To manage your free domain name DNS records, open the [database manager](https://www.odoo.com/my/databases), click the  (gear) button next to
the database name, select  Domain Names, and click DNS.

- A: the A record holds the IP address of the domain. It is automatically created and
  **cannot** be edited or deleted.
- CNAME: CNAME records forward one domain or subdomain to another domain. One is
  automatically created to map the `www.` subdomain to the database. If the database is renamed, the
  CNAME record **must** also be renamed.
- MX: MX records instruct servers on where to deliver emails.
- TXT: TXT records can be used for different purposes (e.g., to verify domain name
  ownership).

Any modification to the DNS records can take up to **72 hours** to propagate worldwide on all
servers.

> **Note:**
>
> [Contact Odoo support](https://www.odoo.com/help) if you need assistance to manage your domain
> name.

### Mailbox

The one-year free domain name offer does **not** include a mailbox. There are two options to link
your domain name with a mailbox.

#### Use a subdomain

You can create a subdomain (e.g., `subdomain.yourdomain.com`) to use as an alias domain for the
database. It allows users to create records in the database from emails received on their
`email@subdomain.yourdomain.com` alias.

To do so, open the [database manager](https://www.odoo.com/my/databases), click the
 (gear) button next to the database name and select
Domain Names. Click DNS, then Add DNS record and select
CNAME. Next, enter the desired subdomain in the Name field (e.g.,
`subdomain`), the original database domain with a period at the end (e.g., `mycompany.odoo.com.`) in
the Content field, and click Add record.

Then, add the alias domain as your *own domain* by clicking Use my own domain, entering
the alias domain (e.g., `subdomain.yourdomain.com`), clicking Verify, and then
I confirm, it’s done.

Finally, go to your database and open the Settings. Under the Alias Domain
field, enter the alias domain (e.g., `subdomain.yourdomain.com`), click Create, and then
Save.

#### Use an external email provider

To use an external email provider, you should configure an MX record. To do so, open the [database
manager](https://www.odoo.com/my/databases), click the  (gear) button
next to the database name and select  Domain Names. Click
DNS, then Add DNS record and select MX. The values you should
enter for the Name, Content, and Priority fields depend on the
external email provider.

> **Note:**
>
> - [Google Workspace: MX record values](https://support.google.com/a/answer/174125?hl=en)
> - [Outlook and Exchange Online: Add an MX record for email](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/create-dns-records-at-any-dns-hosting-provider?view=o365-worldwide#add-an-mx-record-for-email-outlook-exchange-online)

##### Google Workspace

To use your free domain name on Gmail, register to [Google Workspace](https://workspace.google.com).

During the registration process, select Set up using your existing domain when asked to
Choose a way to set up your account, and enter your domain (e.g., `yourdomain.com`) when
asked What’s your business’s domain name?.

###### Domain ownership verification

1. Sign in to Google Workspace. When asked to verify you own your domain, click Switch to
   manual verification.

   ![Switching to manual domain verification on Google Workspace](../../../../_images/workspace-verify-switch.png)
2. Select `gandi.net` as the Domain host and click Continue.

   ![Selecting the domain host on Google Workspace](../../../../_images/workspace-verify-domain.png)
3. Copy the content of the Value field under TXT record. Leave the window
   open.

   ![Copying the TXT value on Google Workspace](../../../../_images/workspace-verify-code.png)
4. Open the [database manager](https://www.odoo.com/my/databases), click the
   (gear) button next to the database name and select  Domain
   Names. Click DNS, then Add DNS record and select TXT.
5. Enter `@` in the Name field, paste the Value provided by Google in the
   Content field, and click Add record.

   ![Creating a TXT record to verify domain name ownership](../../../../_images/workspace-txt.png)
6. Go back to Google Workspace, tick the box at the bottom, and click Confirm.

> **Note:**
>
> [Google Workspace Admin Help: Verify your domain with a TXT record](https://support.google.com/a/answer/16018515)

###### Redirect emails to Gmail

1. Open the [database manager](https://www.odoo.com/my/databases), click the
   (gear) button next to the database name and select  Domain
   Names. Click DNS, then Add DNS record, and select MX.
2. Enter `@` in the Name field, `1` in the Priority field,
   `smtp.google.com.` in the Content field, and click Add record.

   ![Creating an MX record to redirect emails to Gmail](../../../../_images/workspace-mx.png)
3. Open the [Google Workspace Admin console](https://admin.google.com/ac/domains/manage), click
   Activate Gmail for your domain, and follow the steps.

> **Note:**
>
> [Google Workspace Admin Help: Set up MX records for Google Workspace](https://support.google.com/a/answer/16004259)

## Configure an existing domain name

If you already have a domain name, you can use it for your Odoo website.

> **Warning:**
>
> To avoid potential [SSL certificate validation] issues, it is strongly
> recommended to follow these five steps, in the specified order:
>
> 1. Set up [URL redirections](../structure/pages.html#website-pages-url-redirection) before transferring the domain
>    name to preserve the website’s SEO.
> 2. [Add a CNAME record.]
> 3. [Redirect your naked domain name.] (This step is optional, but
>    recommended.)
> 4. [Map your domain name to your Odoo database.]
> 5. [Map your domain name to your Odoo website.]

### Add a CNAME record

Adding a CNAME record to forward your domain name to the address of your Odoo database is required.

Odoo OnlineOdoo.sh

The CNAME record’s target address should be your database’s address as defined at its creation
(e.g., `mycompany.odoo.com`).

The CNAME record’s target address should be the project’s main address, which can be found on
Odoo.sh by going to Settings ‣ Project Name, or a specific branch
(production, staging or development) by going to Branches ‣ select the
branch ‣ Settings ‣ Custom domains, and clicking How to set up my domain?. A
message indicates which address your CNAME record should target.

The specific instructions depend on your DNS hosting service.

> **Note:**
>
> - [GoDaddy: Add a CNAME record](https://www.godaddy.com/help/add-a-cname-record-19236)
> - [Namecheap: How to create a CNAME record for your domain](https://www.namecheap.com/support/knowledgebase/article.aspx/9646/2237/how-to-create-a-cname-record-for-your-domain)
> - [OVHcloud: Add a new DNS record](https://docs.ovh.com/us/en/domains/web_hosting_how_to_edit_my_dns_zone/#add-a-new-dns-record)
> - [Cloudflare: Manage DNS records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/)

### Redirect a naked domain

> **Note:**
>
> Although optional, completing this step is advised.

To let visitors use your naked domain name (a domain name without any subdomains or prefixes)
(`yourdomain.com`), creating a 301 redirect (a permanent redirect from one URL to another)
to `www.yourdomain.com` is required:

- from `http://yourdomain.com` to `https://www.yourdomain.com`, and
- from `https://yourdomain.com` to `https://www.yourdomain.com`.

The specific instructions depend on your DNS hosting service. However, not all of them offer to
redirect a naked domain with a secure HTTPS connection. If you encounter any issue, we recommend
[using Cloudflare].

#### Using Cloudflare to secure and redirect a naked domain

1. [Sign up and log in to Cloudflare](https://dash.cloudflare.com/sign-up).
2. Enter your domain name on [Cloudflare’s dashboard](https://dash.cloudflare.com/login) and
   select Quick scan for DNS records.
3. Choose a plan (the free plan is sufficient).
4. Follow Cloudflare’s instructions and recommendations to complete the activation.
5. Add a CNAME record to redirect your naked domain (`yourdomain.com`) to the `www` subdomain
   (e.g., `www.yourdomain.com`) by clicking DNS in the navigation menu, then clicking
   the Add record button, and using the following configuration:

   - Type: CNAME
   - Name: `@` (or `yourdomain.com`)
   - Target: e.g., `www.yourdomain.com`
   - Proxy status: Proxied![Adding a CNAME DNS record to Cloudflare to redirect a naked domain to a www subdomain](../../../../_images/cloudflare-cname-www.png)
6. Add another second CNAME record to redirect the `www` subdomain (e.g., `www.yourdomain.com`) to
   your database address (e.g., `mycompany.odoo.com`) using the following configuration:

   - Type: CNAME
   - Name: e.g., `www.yourdomain.com`
   - Target: e.g., `mycompany.odoo.com`
   - Proxy status: DNS only![Adding a CNAME DNS record to Cloudflare to redirect a www subdomain to an Odoo database](../../../../_images/cloudflare-cname-db.png)
7. Define a redirect rule to permanently redirect (301) your naked domain (e.g., `yourdomain.com`)
   to both `http://` and `https://` by going to Rules ‣ Create rule ‣ Products,
   and clicking Create a Rule under Redirect Rules:

   - Enter any Rule name.
   - Under the If incoming requests match… section, select Custom filter
     expression and use the following configuration:

     - Field: Hostname
     - Operator: equals
     - Value: e.g., `yourdomain.com`
   - Under the Then… section, use the following configuration:

     - Type: Dynamic
     - Expression: e.g., `concat("https://www.yourdomain.com", http.request.uri.path)`
     - Status code: 301
     - Preserve query string: enabled![Defining a Cloudflare redirect rule to create a permanent redirect (301)](../../../../_images/cloudflare-redirect-rule.png)
8. Go to SSL/TLS and set the encryption mode to Full.

   ![Setting the encryption mode to full on Cloudflare](../../../../_images/cloudflare-encryption.png)

### Map a domain name to an Odoo database

> **Warning:**
>
> Ensure you have [added a CNAME record] to your domain name’s DNS
> **before** mapping your domain name to your Odoo database.
>
> Failing to do so may prevent the validation of the [SSL certificate] and
> could result in a *certificate name mismatch* error. Web browsers often display this as a
> warning, such as *“Your connection is not private”*.
>
> If you encounter this error after mapping the domain name to your database, wait up to five
> days, as the validation may still happen. If not, you can [submit a support ticket](https://www.odoo.com/help-form), including screenshots of your CNAME records.

Odoo OnlineOdoo.sh

Open the [database manager](https://www.odoo.com/my/databases), click the
(gear) button next to the database name, select  Domain
Names, and click Use my own domain. Then, enter the domain name (e.g.,
`www.yourdomain.com`), click Verify and I confirm, it’s done.

![Mapping a domain name to an Odoo Online database](../../../../_images/map-database-online.png)

On Odoo.sh, go to Branches ‣ select your branch ‣ Settings ‣ Custom
domains, type the domain name to add, then click Add domain.

![Mapping a domain name to an Odoo.sh branch](../../../../_images/map-database-sh.png)
> **Note:**
>
> [Odoo.sh branches: settings tab](../../../../administration/odoo_sh/getting_started/branches.html#odoo-sh-branches-tabs-settings)

#### SSL encryption (HTTPS protocol)

**SSL encryption** allows visitors to navigate a website through a secure connection, which appears
as the *https://* protocol at the beginning of a web address rather than the non-secure *http://*
protocol.

Odoo generates a separate SSL certificate for each domain [mapped to a database] using [Let’s Encrypt’s certificate authority and ACME protocol](https://letsencrypt.org/how-it-works/).

> **Note:**
>
> - Certificate generation may take up to 24 hours.
> - Several attempts to validate your certificate are made for five days after you map your domain
>   name to your database.
> - If you use another service, you can keep using it or change to Odoo’s.

> **Warning:**
>
> No SSL certificate is generated for naked domains (domain names without any subdomains
> or prefixes).

#### Web base URL of a database

> **Note:**
>
> If the Website app is installed on your database, skip this section and continue from the
> [Map a domain name to a website] section.

The *web base URL* or root URL of a database affects your main website address and all the
links sent to your customers (e.g., quotations, portal links, etc.).

To make your custom domain name the *web base URL* of your database, access your database using your
custom domain name and log in as an administrator (a user part of the Settings access right
group under Administration).

> **Warning:**
>
> If you access your database with the original Odoo address (e.g., `mycompany.odoo.com`), the *web
> base URL* of your database will be updated accordingly. To prevent the automatic update of the
> *web base URL* when an administrator logs in to the database, activate the [developer mode](../../../general/developer_mode.html#developer-mode), go to Settings ‣ Technical ‣ System Parameters ‣ New,
> and enter `web.base.url.freeze` as the Key and `True` as the Value.

> **Note:**
>
> You can also set the web base URL manually. To do so, activate the [developer mode](../../../general/developer_mode.html#developer-mode), go to Settings ‣ Technical ‣ System Parameters, and
> search for the `web.base.url` key (create it if necessary) and enter the full address of your
> website as the value (e.g., `https://www.yourdomain.com`). The URL must include the protocol
> `https://` (or `http://`) and *not* end with a slash (`/`).

### Map a domain name to an Odoo website

Mapping your domain name to your website is different than mapping it to your database:

- It defines your domain name as the main one for your website, helping search engines to index your
  website correctly.
- It defines your domain name as the base URL for your database, including portal links sent by
  email to your customers.
- If you have multiple websites, it maps your domain name to the appropriate website.

Go to Website ‣ Configuration ‣ Settings. If you have multiple websites, select
the one you want to configure. In the Domain field, enter the address of your website
(e.g., `https://www.yourdomain.com`) and Save.

> **Warning:**
>
> Mapping your domain name to your Odoo website prevents Google Search from indexing your original
> database address (e.g., `mycompany.odoo.com`).
>
> If both addresses are already indexed, it may take some time before the indexation of the second
> address is removed from Google Search. You can use the [Google Search Console](https://search.google.com/search-console/welcome) to fix the issue.

> **Note:**
>
> If you have multiple websites and companies on your database, make sure to select the right
> Company under Website ‣ Configuration ‣ Settings. Doing so
> indicates Odoo which URL to use as the [base URL] according to
> the company in use.

---

# Address autocomplete

You can use the Google Places API on your website to ensure that your users’ delivery addresses
exist and are understood by the carrier. The Google Places API allows developers to access detailed
information about places using HTTP requests. The autocompletion predicts a list of places when the
user starts typing the address.

![Address autocomplete example](../../../../_images/address-autocomplete-example.png)
> **Note:**
>
> - [Google Maps Platform](https://mapsplatform.google.com/maps-products)
> - [Google Developers Documentation: Google Places API](https://developers.google.com/maps/documentation/places/web-service/autocomplete)

To do so, go to Website ‣ Configuration ‣ Settings and enable
Address Autocomplete in the SEO section.

![Enable address autocomplete](../../../../_images/enable-address-autocomplete.png)

Insert your Google Places API key in the API Key field. If you don’t have
one, create yours on the [Google Cloud Console](https://console.cloud.google.com/getting-started)
and follow these steps.

## Step 1: Enable the Google Places API

**Create a New Project:**
To enable the **Google Places API**, you first need to create a project. To do so, click
Select a project in the top left corner, New Project, and follow the prompts
to set up your project.

**Enable the Google Places API:**
Go to the Enabled APIs & Services and click + ENABLE APIS AND SERVICES.
Search for “Places API” and select it. Click on the “Enable” button.

> **Note:**
>
> Google’s pricing depends on the number of requests and their complexity.

## Step 2: Create API Credentials

Go to [APIs & Services –> Credentials](https://console.cloud.google.com/apis/credentials).

**Create credentials:**
To create your credentials, go to Credentials, click Create Credentials, and
select API key.

> **Note:**
>
> For security purposes, you can restrict the usage of your API key. You can go to the
> API restrictions section to specify which APIs your key can access. For the Google
> Places API, you can restrict it to only allow requests from specific websites or apps.

> **Warning:**
>
> - Save Your API Key: copy your API key and securely store it.
> - Do not share it publicly or expose it in client-side code.

---

# Google Search Console

Google Search Console is a free web service provided by Google that allows website owners to
monitor, maintain, and troubleshoot their site’s presence in Google Search results. It offers
valuable insights into how Google views and interacts with your site, helping you optimize its
performance.

To enable Google Search Console for your website, go to [Google Search Console](https://search.google.com/search-console/welcome). Then, select the property type
[Domain property] or [URL prefix property].

![Google Search Console domain or URL prefix](../../../../_images/add-domain-or-url-prefix.png)

## Domain property

A domain property in Search Console tracks all versions of your website, including subdomains and
protocols (http/https). This comprehensive view allows you to analyze your overall website’s search
performance and make informed decisions to optimize its visibility. Enter the domain, e.g.,
`example.com` and click Continue.

> **Note:**
>
> - The domain property type can only be verified via
>   [DNS record](https://support.google.com/webmasters/answer/9008080?hl=en#domain_name_verification&zippy=%2Chtml-tag).
> - Google suggests creating at least one domain property to represent your site, as it is the most
>   complete view of your website information.

## URL prefix property

This type of verification is usually simpler as you have multiple verification methods, such as
using your existing Google Analytics or Tag Manager account. It also makes sense to view a section
of your website separately. For example, if you work with a consultant on a specific part of your
website, you might want to verify this part separately to limit access to your data. Enter the URL,
e.g., `https://example.odoo.com/` and click Continue.

## Site ownership verification

Before using Google Search Console for your website, you must verify your site ownership. This
verification process is a security measure that protects both you and Google. It ensures that only
authorized users have access to sensitive data and that you have control over how your website is
treated in Google Search.

Five methods are available to do this:

1. [HTML file upload]
2. [DNS record](https://support.google.com/webmasters/answer/9008080?hl=en#domain_name_verification&zippy=%2Chtml-tag)
3. [HTML tag](https://support.google.com/webmasters/answer/9008080?hl=en#meta_tag_verification&zippy=%2Chtml-tag)
4. [Google Analytics tracking code](https://support.google.com/webmasters/answer/9008080?hl=en#google_analytics_verification)
5. [Google Tag Manager container snippet](https://support.google.com/webmasters/answer/9008080?hl=en#google_tag_manager_verification)

> **Note:**
>
> The best method for you depends on your comfort level and technical expertise. For beginners,
> using a file upload or HTML tag might be easiest. Those options are convenient if you already use
> [Google Analytics](../reporting/analytics.html#analytics-google-analytics) or [Google Tag Manager](../reporting/analytics.html#analytics-google-tag-manager). You need to access your domain registrar’s settings for domain
> verification.

### HTML file upload

This method involves uploading an HTML file provided by Google containing the verification code you
have to put in your Odoo’s Website Settings. Google verifies ownership by checking for this code.

1. Once you added your website URL under the URL prefix option and clicked continue,
   expand the HTML file section where you find a download  button.

   ![HTML file download](../../../../_images/html-file-download.png)
2. Download your HTML verification file and copy the verification code (e.g., `google123abc.html`).

   ![Open and copy html file](../../../../_images/open-copy-html-file.png)
3. In your Odoo database, go to Website ‣ Configuration ‣ Settings,
   and enable Google Search Console in the SEO section. Paste the
   verification code (e.g., `google123abc.html`) in the dedicated field.

   ![Paste html code in Odoo](../../../../_images/paste-html-code-settings.png)
4. In Google Search Console, click Verify. If you perform the steps above correctly,
   verification should be done immediately.

### HTML tag

This method involves copying a meta tag provided by Google and pasting it into your Odoo website.
To verify your site ownership using an HTML tag, follow these instructions:

1. Expand the HTML tag section.

   ![Open HTML tag section.](../../../../_images/gsc-html-tag.png)
2. Copy the HTML tag to clipboard.
3. On your Odoo website, click Edit in the upper-right corner, go to
   the Theme tab, scroll down to the Advanced section, then
   click <head> and </body> next to Code Injection.
   Paste the copied tag into the first field (<head>), and click Save.

   ![Paste tag in head field.](../../../../_images/gsc-paste-tag.png)
4. Return to GSC and click Verify.

> **Note:**
>
> [Domain names](domain_names.html)

---

# Cookies bar

**Cookies** are small text files sent to your device when you visit a website. They are processed
and stored by your browser and record visitor information like login details, preferences, and
browsing history. **Essential cookies** are necessary for the website to function, while
**optional cookies** are used to analyze behavior or display ads.

Data protection laws require notifying visitors about data collection methods and purposes.
**Cookies bar** fulfill this obligation by informing visitors on their first visit and allowing them
to decide whether to store all or only essential cookies on their device.

> **Note:**
>
> - Cookies bars are required to obtain visitors’ consent for optional cookies only. Consent is not
>   required for essential cookies.
> - Odoo is compliant with [Google consent mode v2](https://support.google.com/tagmanager/answer/13695607).

## Configuration

To add a cookies bar on your website, go to Website ‣ Configuration ‣
Settings and enable Cookies Bar in the Tracking & SEO section. This
activates Block tracking 3rd-party services by default, including social media, video
hosting platforms, and Google services. Click Add domains to the block list to include
other external websites. These services remain blocked on your website until visitors accept
optional cookies.

> **Note:**
>
> Using third-party cookies without a cookies bar does not prevent them from being triggered. Only
> the presence of a cookie bar **and** the visitor’s refusal ensure that these cookies are blocked.

## Cookies policy

When you enable the cookies bar for your website, Odoo creates the **Cookie Policy** page
(`/cookie-policy`) containing a list of cookies set by default, with their purpose and examples.

> **Note:**
>
> Click here to preview the list of default cookies
>
> | Category | Role | Name |
> | --- | --- | --- |
> | Essential - Session & Security | Authenticate visitors, protect visitor data and allow the website to deliver the services visitors expects, such as maintaining the content of their cart, or allowing file uploads. The website will not work properly without these cookies. | session\_id (Odoo) |
> | Essential - Preferences | Remember information about the preferred look or behavior of the website, such as the preferred language or region. The website will continue to function without these cookies, but the visitor’s experience may be affected. | frontend\_lang (Odoo) |
> | Optional - Interaction History | Collect information about your interactions with the website, the pages you’ve seen, and any specific marketing campaign that brought you to the website. The website will work without these cookies, but some features or services may not perform optimally. | im\_livechat\_previous\_operator (Odoo), utm\_campaign (Odoo), utm\_source (Odoo), utm\_medium (Odoo) |
> | Optional - Advertising & Marketing | Make advertising more engaging to visitors and more valuable to publishers and advertisers, such as providing more relevant ads when you visit other websites that display ads or to improve reporting on ad campaign performance. Note that some third-party services may install additional cookies on your browser in order to identify you. | \_\_gads (Google), \_\_gac (Google) |
> | Optional - Analytics | Understand how visitors engage with the website, via Google Analytics. The website will still work without these cookies. | \_ga (Google), \_gat (Google), \_gid (Google), \_gac\_\* (Google) |

> **Note:**
>
> It is not possible to let visitors customize or select which optional cookies they want to allow.

> **Note:**
>
> You could add a link to this page in your website’s footer, for example.

### Edit the Cookies policy page

To access it, click the Cookie Policy hyperlink in the cookies bar or open the page from
Website ‣ Site ‣ Pages.

To adapt the content of the page according to your needs, click the Edit button.

> **Note:**
>
> You have to list every cookie you added yourself on the `/cookie-policy` page including their
> name, role, category and duration.

> **Note:**
>
> To check the duration of cookies, use your browser’s developer tools.

> **Note:**
>
> [Pages](../structure/pages.html)

## Customization

To adapt the display of the cookies bar on your website, click Edit on the website
editor, go to the Invisible Elements section at the bottom of the panel, and click
Cookies Bar. You can modify the Layout and Size of the
cookies bar, and enable Backdrop to gray out the page in the background when the cookies
bar is displayed on the screen.

Click anywhere in the building block to further customize the appearance of the cookies bar using
Block, Column and/or Inline Text customization options.

To edit the contents of the cookies bar (i.e., the consent message), click directly in the building
block.

---

# Translations

Your website can be translated into multiple languages, allowing visitors to view its content in
their preferred language.

## Configuration

Before translating a website into one or more languages, [install them on the database](../../../general/users/language.html). To do so:

- Go to Website ‣ Configuration ‣ Settings.
- Under the General section, click  Install new
  languages.
- In the dialog box, select one or more Languages from the dropdown menu, click
  Add, then Close.

Next, add the installed language(s) to the website by selecting them under the Languages
field and clicking Save.

> **Note:**
>
> To remove a language from a website, click the  (Delete) icon next to
> it.

## Language selector

Once another language is added to a website, the language selector is displayed in the website’s
header and footer, allowing visitors to switch between languages.

> **Note:**
>
> - Refresh your browser if the language selector or a language option does not appear.
> - If the visitor’s browser language is not available, the website will use the website’s default
>   language. To edit it, go to Website ‣ Configuration ‣ Settings. Under the
>   General section, select the language using the Default field.

To hide or customize the appearance of one of the language selectors, open the website in the
default language, click Edit, then select the language selector.

- To edit the header’s language selector:

  1. In the sidebar, scroll down to the Language Selector section.
  2. Set the Style to Dropdown or Inline.
  3. Set the Label to Text, Flag, Flag and Text,
     Code, or Flag and Code.
  4. Click Save.
  > **Note:**
  >
  > To hide the language selector in the header, go to the Show/Hide Elements section
  > and click the  (Language selector) button next to the
  > Actions field.
- To edit the footer’s language selector:

  1. Set the Language selector field to Dropdown, Inline,
     or None.
  2. Set the Label to Text, Flag, Flag and Text,
     Code, or Flag and Code.
  3. Click Save.

> **Note:**
>
> You can [display or hide website elements](../web_design/visibility.html#website-visibility-conditions) based on the
> website’s language.

## Translate a page

To translate a website page, switch to the language to translate and click Edit ‣
Translate in the top-right corner to activate the translation mode.

> **Note:**
>
> - In this mode, only translatable text can be edited. Any other type of modification with the
>   website builder must be carried out while using the default language.
> - Depending on the language added, some default content may already be translated. However, the
>   content you added manually should be translated using the Translate feature.
> - When text is highlighted in green, it indicates that it has already been translated (manually
>   or automatically). When text is highlighted in yellow, it indicates that it has not been
>   translated.

Click the green button next to the Translated to field to automatically translate all
text highlighted in yellow. You can also manually translate or adapt text, whether it is highlighted
in green or yellow, by selecting it and editing it. Click Save when you are done
translating.

![Entering the translation mode](../../../../_images/text-translation.png)
> **Note:**
>
> - The core URL structure remains consistent across languages, while specific elements like
>   product names or categories are translated. For example,
>   `https://www.mywebsite.com/shop/product/my-product-1` is the default version of a product page,
>   while `https://www.mywebsite.com/fr/shop/product/mon-produit-1` is the translated version of
>   the same product page. The structure (`/shop/product/`) remains unchanged, but the product name
>   (`my-product`) is translated (`mon-produit`).
> - Some elements can also be translated from the backend (e.g., product names).

### Translate SEO-related elements

To translate an [image’s alt tag](../structure/seo.html#seo-images) (i.e., the image’s Description
field) and title tag (i.e., the image’s Tooltip field), switch to the language to
translate, click Edit ‣ Translate, and select the image. In the
Translate Attribute box, enter the translation for the alt and/or the
title tags.

To add translated [meta tags](../structure/seo.html#seo-meta-tags), go to Website ‣ Site ‣
Optimize SEO. In the Keywords section, select the language and add the keywords.

> **Note:**
>
> When viewing a website in its default language, all keywords are displayed, regardless of their
> language. However, when viewing a website in another language, only the keywords relevant to that
> language are displayed.

> **Note:**
>
> [Search Engine Optimization](../structure/seo.html)

---

# Multiple websites

Odoo allows you to create multiple websites from the same database. This can be useful, for example,
if you have multiple brands operating under your organization, or to create separate websites for
different products/services, or different audiences. In these cases, having different websites can
help avoid confusion and make it easier to tailor your digital outreach strategies and reach your
target audience.

Each website can be designed and configured independently with its own [domain name](domain_names.html), [theme](../web_design/themes.html), [pages](../structure/pages.html), [menus](../structure/header_footer.html), [languages](translate.html), [products](../../ecommerce/configuration/products.html), assigned sales team, etc. They can also
[share content and pages].

> **Note:**
>
> Duplicate content (i.e., pages and content shared between multiple websites) can have a negative
> impact on [Search Engine Optimization (SEO)](../structure/seo.html).

## Website creation

To create a new website, proceed as follows:

1. Go to Website ‣ Configuration ‣ Settings.
2. Click + New Website.

   ![New website button](../../../../_images/create-website.png)
3. Specify the Website Name and Website domain. Each website must be
   published under its own [domain](domain_names.html).
4. Adapt the Company name, Languages and Default language
   if needed.
5. Click the Create button.

You can then start building your new website.

> **Note:**
>
> By default, all website-related apps that you have installed (e.g. **eCommerce**,
> **Forum**, **Blog**, etc.) and their related website pages are also available on the
> new website. You can remove them by amending the website’s menu.

## Switching websites

To switch from one website to another, click the menu next to the +New button in the
top right corner and select the website you want to switch to.

![Website selector](../../../../_images/switch-websites.png)
> **Note:**
>
> When you switch websites, you are redirected to the homepage of the other website.

## Website-specific configuration

Most website settings are website-specific, which means they can be enabled/disabled per website. To
adapt the settings for a website, go to Website ‣ Configuration ‣ Settings.
Select the desired website in the field Settings of Website at the top of the
Settings page, in the **yellow** banner. Then, adapt the options for that specific
website.

> **Note:**
>
> - Websites are created with the default settings; the settings are not copied from one website to
>   the other.
> - In a [multi-company environment](../../../general/companies.html), each website can be
>   linked to a specific company in your database so that only company-related data (e.g.,
>   products, jobs, events, etc.) is displayed on the website. To display company-specific data,
>   set the desired company in the Company field.

### Content availability

By default, pages, products, events, etc. created from the frontend (using the
+New button) are only available on the website from which it was created. Records
created from the backend, however, are made available on all websites by default. The content’s
availability can be changed in the backend, in the Website field. For example, for
products, go to eCommerce ‣ Products, then select the product and go to the
Sales tab. For forums, go to Configuration ‣ Forums, then select the
forum.

![Website field in Forum form](../../../../_images/forum-multi-website.png)

Records and features can be made available:

- On all websites: leave the Website field empty;
- Only on one website: set the Website field accordingly;
- On some websites: in this case, you should duplicate the item and set the Website
  field.

#### Website pages

To modify the website on which a page is to be published, proceed as follows:

1. Go to Website ‣ Site ‣ Pages.
2. Open the search panel and select the website on which the page is currently published.

   ![Display pages per website](../../../../_images/pages-switch-websites.png)
3. Tick the check box next to the page(s) you want to change.
4. Click the Website field and select the website, or empty it to publish the page on
   all websites.

> **Note:**
>
> Each website must have its own homepage; you may not use the same homepage for several websites.

## eCommerce features

eCommerce features such as products, eCommerce categories, pricelists, discounts, payment providers,
etc. can be restricted to [a specific website].

### Customer accounts

You can [allow your customers to use the same account](../../ecommerce/configuration/customer_accounts.html) on all of your websites by enabling the Shared
Customer Accounts check box in the website settings.

### Pricing

Products can be priced differently based on the website using [pricelists](../../ecommerce/configuration/prices.html#ecommerce-prices-selectable-pricelists). The following configuration is required:

1. Go to Website ‣ Configuration ‣ Settings.
2. Scroll down to the Shop - Products section and select the Pricelists
   option Multiple prices per product.
3. Click Pricelists to define new pricelists or edit existing ones.
4. Select the pricelist or click New to create a new one, then select the
   Configuration tab and set the Website field.

## Reporting

### Analytics

Each website has its own [analytics](../reporting/analytics.html#analytics-plausible). To switch between websites, click
the buttons in the upper right corner.

![Switch websites in analytics](../../../../_images/analytics-switch-websites.png)

### Other reporting data

Other reporting data such as eCommerce dashboard data, online sales analyses and visitors can be
grouped by website if necessary. Open the search panel and select Group by –> Website.

---

# Forms spam protection

[Cloudflare Turnstile] and [Google reCAPTCHA v3]
protect website forms, web sign-up pages, and password reset pages against spam and abuse. They
attempt to distinguish between human and bot submissions using non-interactive challenges based on
telemetry and visitor behavior.

> **Warning:**
>
> We recommend using **Cloudflare Turnstile** as reCAPTCHA v3 may not be compliant with local data
> protection regulations.

> **Note:**
>
> All pages using the Form, Newsletter Block, Newsletter Popup
> snippets, and the eCommerce Extra Step During Checkout form are protected by both
> tools. **Web sign-up pages** and **password reset pages** are also protected.

> **Note:**
>
> - [Cloudflare Turnstile’s documentation](https://developers.cloudflare.com/turnstile/)
> - [Google’s reCAPTCHA v3 guide](https://developers.google.com/recaptcha/docs/v3)

## Cloudflare Turnstile configuration

### On Cloudflare

- [Create](https://dash.cloudflare.com/sign-up) a Cloudflare account or use an existing one and
  [log in](https://dash.cloudflare.com/login).
- On the dashboard navigation sidebar, click Turnstile.
- On the Turnstile Sites page, click Add Site.
- Add a Site name to identify it easily.
- Enter or select the website’s Domain (e.g., *example.com* or *subdomain.example.com*).
- Select a Widget Mode:

  - The Managed mode is **recommended**, as visitors can be prompted to check a box
    confirming they are human if deemed necessary by Turnstile.

    ![Cloudflare Turnstile human verification widget](../../../../_images/turnstile-human.png)
  - For the Non-interactive and Invisible modes, visitors are never
    prompted to interact. In Non-interactive mode, a loading widget can be displayed to
    warn visitors that Turnstile protects the form; however, the widget is not supported by Odoo.

    > **Note:**
    >
    > If the Turnstile check fails, visitors are not able to submit the form, and the following
    > error message is displayed:
    >
    > ![Cloudflare Turnstile verification error message](../../../../_images/turnstile-error.png)
- Click Create.

![Adding a website to Cloudflare Turnstile](../../../../_images/turnstile-configuration.png)

The generated keys are then displayed. Leave the page open for convenience, as copying the keys in
Odoo is required next.

### On Odoo

- From the database dashboard, click Settings. Under Integrations, enable
  Cloudflare Turnstile and click Save.
- Open the Cloudflare Turnstile page, copy the Site Key, and paste it into the
  CF Site Key field in Odoo.
- Open the Cloudflare Turnstile page, copy the Secret Key, and paste it into the
  CF Secret Key field in Odoo.
- Click Save.

> **Note:**
>
> Navigate to Turnstile on your Cloudflare account to view the solve rates and access more
> settings.

## reCAPTCHA v3 configuration

> **Warning:**
>
> reCAPTCHA v3 may not be compliant with local data protection regulations.

### On Google

Open [the reCAPTCHA website registration page](https://www.google.com/recaptcha/admin/create). Log
in or create a Google account if necessary.

On the website registration page:

- Give the website a Label.
- Leave the reCAPTCHA type on Score based (v3).
- Enter one or more Domains (e.g., *example.com* or *subdomain.example.com*).
- Under Google Cloud Platform, a project is automatically selected if one was already
  created with the logged-in Google account. If not, one is automatically created. Click
  Google Cloud Platform to select a project yourself or rename the automatically created
  project.
- Agree to the terms of service.
- Click Submit.

![reCAPTCHA website registration example](../../../../_images/recaptcha-google-configuration.png)

A new page with the generated keys is then displayed. Leave it open for convenience, as copying the
keys to Odoo is required next.

### On Odoo

- From the database dashboard, click Settings. Under Integrations, enable
  reCAPTCHA if needed.

  > **Warning:**
  >
  > Do not disable the reCAPTCHA feature or uninstall the Google reCAPTCHA
  > integration module, as many other modules would also be removed.
- Open the Google reCAPTCHA page, copy the Site key, and paste it into the
  Site Key field in Odoo.
- Open the Google reCAPTCHA page, copy the Secret key, and paste it into the
  Secret Key field in Odoo.
- Change the default Minimum score (`0.70`) if necessary, using a value between `1.00`
  and `0.00`. The higher the threshold is, the more difficult it is to pass the reCAPTCHA, and vice
  versa. Out of the 11 levels, only the following four score levels are available by default:
  `0.1`, `0.3`, `0.7` and `0.9`.
- Click Save.

> **Note:**
>
> [Interpret reCAPTCHA scores - Google documentation](https://cloud.google.com/recaptcha/docs/interpret-assessment-website#interpret_scores)

You can notify visitors that reCAPTCHA protects a form. To do so, open the website editor and
navigate to the form. Then, click somewhere on the form, and on the right sidebar’s
Customize tab, toggle Show reCAPTCHA Policy found under the Form
section.

![reCAPTCHA policy message displayed on a form](../../../../_images/recaptcha-policy.png)
> **Note:**
>
> If the reCAPTCHA check fails, the following error message is displayed:
>
> ![Google reCAPTCHA verification error message](../../../../_images/recaptcha-error.png)

> **Note:**
>
> Analytics and additional settings are available on [Google’s reCAPTCHA administration page](https://www.google.com/recaptcha/admin/). For example, you can receive email alerts if Google
> detects suspicious traffic on your website or view the percentage of suspicious requests, which
> could help you determine the right minimum score.

---

# Set up a content delivery network (CDN)

## Deploying with KeyCDN

A CDN or *content distribution network*, is a geographically
distributed network of servers that provides high speed internet content. The CDN provides quick, high-quality content delivery for content-heavy websites.

This document will guide you through the setup of a [KeyCDN](https://www.keycdn.com) account with an Odoo powered website.

### Create a pull zone in the KeyCDN dashboard

On the KeyCDN dashboard, start by navigating to the Zones menu item on the left. On
the form, give a value to the Zone Name, which will appear as part of the CDN’s URL. Then, set the Zone
Status to active to engage the zone. For the Zone Type set the value to
Pull, and then, finally, under the Pull Settings, enter the
Origin URL— this address should be the full Odoo database URL.

> **Tip:**
>
> Use `https://yourdatabase.odoo.com` and replace the *yourdatabase* subdomain prefix with the
> actual name of the database. A custom URL can be used, as
> well, in place of the Odoo subdomain that was provided to the database.

![KeyCDN's Zone configuration page.](../../../../_images/keycdn-zone.png)

Under the General Settings heading below the zone form, click the Show all
settings button to expand the zone options. This should be the last option on the page. After
expanding the General Settings ensure that the CORS option is
enabled.

Next, scroll to the bottom of the zone configuration page and Save the changes. KeyCDN
will indicate that the new zone will be deployed. This can take about 10 minutes.

![KeyCDN deploying the new Zone.](../../../../_images/zone-url.png)
> **Note:**
>
> A new Zone URL has been generated for your Zone, in this example it is
> `pulltest-xxxxx.kxcdn.com`. This value will differ for each database.

Copy this Zone URL to a text editor for later, as it will be used in the next steps.

### Configure the Odoo instance with the new zone

In the Odoo Website app, go to the Settings and then activate the
Content Delivery Network (CDN) setting and copy/paste the Zone URL value
from the earlier step into the CDN Base URL field. This field is only visible and
configurable when the [developer mode](../../../general/developer_mode.html#developer-mode) is activated.

> **Note:**
>
> Ensure that there are two *forward slashes* (`//`) before the CDN Base URL and one
> forward slash (`/`) after the CDN Base URL.

Save the settings when complete.

![Activate the CDN setting in Odoo.](../../../../_images/cdn-base-url.png)

Now the website is using the CDN for the resources matching the CDN filters regular
expressions.

In the HTML of the Odoo website, the CDN integration is evidenced
as working properly by checking the URL of images. The *CDN Base
URL* value can be seen by using your web browser’s Inspect feature on the Odoo website.
Look for it’s record by searching within the Network tab inside of devtools.

![The CDN Base URL can be seen using the inspect function on the Odoo website.](../../../../_images/test-pull.png)

### Prevent security issues by activating cross-origin resource sharing (CORS)

A security restriction in some browsers (such as Mozilla Firefox and Google Chrome) prevents a
remotely linked CSS file to fetch relative resources on this same external server.

If the CORS option isn’t enabled in the CDN
Zone, the more obvious resulting problem on a standard Odoo website will be the lack of *Font
Awesome* icons because the font file declared in the *Font Awesome* CSS won’t be loaded from the
remote server.

When these cross-origin resource issues occur, a security error message similar to the output
below will appear in the web browser’s developer console:

`Font from origin 'http://pulltest-xxxxx.kxcdn.com' has been blocked from loading /shop:1 by
Cross-Origin Resource Sharing policy: No 'Access-Control-Allow-Origin' header is present on the
requested resource. Origin 'http://yourdatabase.odoo.com' is therefore not allowed access.`

![Error message populated in the browser console.](../../../../_images/odoo-security-message.png)

Enabling the CORS option in the CDN settings fixes this issue.

---

# Reporting

---

# Website analytics

Website analytics helps website owners monitor how people use their site. It provides data on
visitor demographics, behavior, and interactions, helping improve websites and marketing strategies.

You can track your Odoo website’s traffic using [Plausible.io] or
[Google Analytics]. We recommend using Plausible.io as it is privacy-friendly,
lightweight, and easy to use.

## Plausible.io

Odoo hosts its own Plausible.io server. The Plausible Analytics dashboard is integrated into Odoo
and can be accessed via Website ‣ Reporting ‣ Analytics.

Databases hosted on Odoo Online and using an `odoo.com` domain name benefit from a free,
ready-to-use Plausible.io solution with automatically generated credentials and a preconfigured
Plausible account. To enable it, go to Website ‣ Configuration ‣ Settings,
then, in the Tracking & SEO section, enable Plausible Analytics. The
credentials are automatically filled in the Shared Link Auth and the Site
fields.

> **Note:**
>
> **If you already have a Plausible.io account** and you want to connect it to your Odoo Online
> database, you must create two `ir.config.parameters` to use Plausible.io’s servers. To do so,
> enable the [developer mode](../../../general/developer_mode.html#developer-mode) and go to General Settings ‣
> Technical ‣ System Parameters. Click New and fill in the following
> Key and Value fields:
>
> > | Key | Value |
> > | --- | --- |
> > | `website.plausible_script` | `https://plausible.io/js/plausible.js` |
> > | `website.plausible_server` | `https://plausible.io` |
>
> Then, go to the Plausible website and follow the steps to
> [set up your account] and link it to your Odoo database.
>
> Deactivating the free Plausible.io account linked to your **Odoo Online** database
> will also remove the existing keys. As a result, new keys will be generated, while all
> historical data will remain associated with the old keys. If you plan to deactivate the
> account, it is recommended to save the existing keys to preserve access to that data.

If you use a custom [domain name](../configuration/domain_names.html) (e.g., `example.com`),
or if your database is hosted on Odoo.sh or On-premise, you need to create your own Plausible.io
account or use an existing one and link it to your database. To do so, follow these steps:

1. [Create](https://plausible.io/register) or [sign in](https://plausible.io/login) to a
   :   Plausible.io account.
2. If you are creating a new account, go through the registration and activation steps.
   On the Add site info page, enter your website Domain name without
   including `www` or `http` (e.g., `example.odoo.com`) and, if necessary, change the
   Reporting Timezone. Click Install Plausible to proceed to the next step.
3. Once done, click the Plausible.io logo in the upper-left part of the page to access the [list of
   websites](https://plausible.io/sites), then click the
   (ellipsis) icon next to the website and select  Settings.

   ![Click the gear icon in the list of websites.](../../../../_images/plausible-gear-icon-settings.png)
4. In the sidebar, select Visibility, then click Add Shared link.
5. Enter a Name, keep the Password protect option disabled, as the Plausible
   analytics dashboard integration in Odoo does not support it, then click Create
   shared link.
6. Copy the shared link.

   ![Copy the shared link URL from Plausible.io](../../../../_images/plausible-copy-shared-link.png)
7. In Odoo, go to Website ‣ Configuration ‣ Settings.
8. In the Tracking & SEO section, enable Plausible Analytics, then paste the
   Shared Link Auth and click Save.

> **Note:**
>
> - If you have [multiple websites](../configuration/multi_website.html), add them to your
>   Plausible.io account by going to <https://plausible.io/sites> and clicking + Add
>   Website. In the Odoo Website settings, ensure that the correct website is selected from the
>   dropdown menu at the top of the page before pasting the Shared link.
> - Odoo automatically pushes two custom goals: `Lead Generation` and `Shop`.
>   Custom goals can be added via Plausible.io. To do so, click the
>   (ellipsis) button on the relevant website card, then navigate to Goals
>   in the sidebar menu, and click Add goal.

> **Note:**
>
> [Plausible Analytics documentation](https://plausible.io/docs)

## Google Analytics

To follow your Odoo website’s traffic with Google Analytics:

1. Create or sign in to a Google account using the following link: <https://analytics.google.com>.
2. - If you are setting up Google Analytics for the first time, click Start measuring
     and go through the account creation step.
   - If you already have a Google Analytics account, sign in and click the  icon
     in the bottom-left corner of the page to access the Admin page. Then, click
     + Create and select Property from the drop-down menu.
3. Complete the next steps: [property creation](https://support.google.com/analytics/answer/9304153?hl=en/&visit_id=638278591144564289-3612494643&rd=2#property),
   business details and business objectives.
4. When you reach the Data collection step, choose the Web platform.

   ![Choose a platform for your Google Analytics property.](../../../../_images/GA-platform.png)
5. Set up your data stream: Specify your Website URL and a Stream name, then
   click Create & continue.
6. Copy the Measurement ID.

   ![Measurement ID in Google Analytics.](../../../../_images/GA-measurement-id.png)
7. In Odoo, go to Website ‣ Configuration ‣ Settings.
8. In the Tracking & SEO section, enable Google Analytics, then paste the
   Measurement ID and click Save.

> **Note:**
>
> If you have [multiple websites](../configuration/multi_website.html) with separate domains, it
> is recommended to create [one property](https://support.google.com/analytics/answer/9304153?hl=en/&visit_id=638278591144564289-3612494643&rd=2#property)
> per domain. In Odoo, in the Website settings, make sure to select the website in the field
> next to `+New website` at the top left of the page before pasting the Measurement ID.

> **Note:**
>
> [Google documentation on setting up Analytics for a website](https://support.google.com/analytics/answer/1008015?hl=en/)

## Google Tag Manager

Google Tag Manager is a tag management system that allows you to easily update
measurement codes and related code fragments, collectively known as tags on your website or mobile
app, directly through the code injector.

> **Note:**
>
> GTM is not an analytics tool and does not offer reporting features.
> It is used to collect data and works alongside Google Analytics to provide more detailed
> insights. In order to use GTM properly, it is recommended to configure Google Analytics as well.
>
> For more information refer to the [documentation on linking Google Analytics and
> Google Tag Manager](https://support.google.com/tagmanager/answer/9442095?hl=en).

> **Warning:**
>
> - Some GTM tags use data layers (e.g., advanced eCommerce tracking data layers) to retrieve
>   variables and send them to Google Analytics. Data layers are currently not managed in Odoo.
> - Google Tag Manager may not be compliant with local data protection regulations.

To configure GTM, proceed as follows:

1. Create or sign in to a Google account by going to <https://tagmanager.google.com/>.
2. In the Accounts tab, click Create Account.
3. Enter an Account Name and select the account’s Country.
4. Enter your website’s URL in the Container name field and select the Target
   platform.
5. Click Create and agree to the Terms of Service.
6. Copy the `<head>` and `<body>` codes from the popup window. Then, go to your website, click
   Edit, go to the Theme tab, scroll down to the Advanced
   section, then click <head> and </body> next to Code Injection
   to paste the codes, then click Save.

> **Note:**
>
> The data is collected in the marketing tools used to monitor the website (e.g., Google Analytics,
> Plausible, Facebook Pixel), not in Odoo.

> **Note:**
>
> [Setting up click triggers on Google](https://support.google.com/tagmanager/answer/7679320?hl=en&ref_topic=7679108&sjid=17684856364781654579-EU)

---

# Link tracker

The link tracker is used to create tracked links to measure the effectiveness of marketing
campaigns, making it easier to identify which channels drive the most traffic and make more
informed decisions.

To create and manage tracked links, [install](../../../general/apps_modules.html#general-install) the Link Tracker
(`website links`) module.

## Create traceable URLs

To create and manage tracked links, navigate to Website ‣ Site ‣ Link Tracker.
Fill in the following information and click Generate tracked link to create a tracking
URL.

1. URL: The URL that is the target of the campaign. It is automatically populated with
   the URL used to access the menu.
2. Campaign: The specific campaign the link should be associated with. This parameter is
   used to distinguish the different campaigns.
3. Medium: The medium describes the category or method through which the visitor arrives
   at your site, such as organic search, paid search, social media ad, email, etc.
4. Source: The source identifies the specific platform or website that referred the
   visitor, such as a search engine, newsletter, or website.

![Create a link tracker URL](../../../../_images/create-link-trackers.png)
> **Note:**
>
> The Campaign, Medium, and Source are UTM parameters incorporated in the tracked URL. These can be used, for example,
> to customize the [visibility](../web_design/visibility.html#website-visibility-conditions) of website building blocks.

## Tracked links overview

To get an overview of your tracked links, go to Website ‣ Site ‣ Link Tracker
and scroll down to Your tracked links section.

![Get an overview of all the links you track.](../../../../_images/your-tracked-link.png)

### Statistics

To measure the performance of tracked links, click the track link and scroll down to the
Statistics section to get an overview of the number of clicks for the tracked link.
By default, the graph shows the total number of clicks. You can change the period to
Last Month or Last Week using the options on the right side of the heading.

---

# Mail groups

The **mail groups** feature allows website visitors to have a public discussion by email. They can
join a group to receive emails from other group members (i.e., website users who have subscribed to
the group) and send new ones to all group members.

To activate the feature, [install](../../general/apps_modules.html#general-install) the Website Mail Group
(`website_mail_group`) module.

> **Note:**
>
> The **mail groups** feature is not to be confused with the
> [Mailing lists](../../marketing/email_marketing/mailing_lists.html) in the Email Marketing app.

## Configuring mail groups

To configure mail groups, proceed as follows:

1. Configure a custom email alias domain by accessing the **General settings**, scrolling down to
   the Discuss section, enabling the Custom Email Server feature, and
   entering the Alias domain (e.g., `@mycompany.com`).
2. Go to Website ‣ Configuration ‣ Mailing Lists, then click New.
3. Specify a Group Name, the Email Alias, and a Description.
4. Enable Moderate this group and specify the Moderators if you wish to
   [moderate messages] from this group. Alternatively, if the
   group is not moderated, you can define Responsible Users who can manage the messages
   in the group.
5. In the Privacy tab, define who can subscribe to the mail group:

   - Everyone: to make the mail group public so anyone can subscribe to it;
   - Members only: to only allow users defined as members to subscribe to the mail group;
   - Selected group of users: to only allow users from the Authorized group
     to subscribe to the mail group.
6. If the mail group is moderated, you can automatically notify authors when their message is
   pending moderation by enabling Automatic notification in the Notify
   Members tab and writing the Notification message.
7. If you wish to send out guidelines to new subscribers, enable Send guidelines to new
   subscribers and write them in the Guidelines tab. This is particularly useful when
   the mail group is moderated.

## Using mail groups

### Subscribing/unsubscribing

Based on the [configuration of the mail group],
users can subscribe to and unsubscribe from mail groups from the website page (`/groups` by default).

![Mail group web page.](../../../_images/mail-group-page.png)

Internal users can also do this from Website ‣ Configuration ‣ Mailing Lists,
using the Join and Leave buttons.

### Sending messages

To send messages to a mail group, website users can email the [mail group’s email address]. Internal users can also create messages directly from
Odoo. To do so, go to Website ‣ Configuration ‣ Mailing Lists, select the mail
group, click the Emails smart button, and click New. Then, fill in the
fields and click Send.

> **Note:**
>
> - The list of messages can also be accessed by selecting the group from the `/groups` website
>   page.
> - Group members can also unsubscribe from the group, access the mail group page, and send emails
>   to the group using the URLs in the footer of any group email they have received.
>
>   ![URLs in the footer of a group email.](../../../_images/mail-group-URLs.png)

## Moderating mail group messages

If the Moderate this group feature has been enabled for the
[mail group], one of the Moderators must
approve the group’s messages before they are dispatched to the other members.

To moderate messages, go to Website ‣ Configuration ‣ Mailing Lists, select the
mail group, and click the To review smart button. You can moderate messages using the
buttons at the end of the message line or select a message to view its content and moderate it
accordingly.

> ![Moderation buttons in the message line.](../../../_images/mail-group-moderation.png)

The following actions are available:

- Accept: to accept the email and send it to the mail group members.
- Reject: to reject the email. In the pop-up window that opens, click
  Reject Silently to reject the email without notifying the author, or specify an
  explanation for rejecting the message, then click Send & Reject to reject the message
  and send the explanation to the author.
- Whitelist: to whitelist the author, i.e. automatically accept all of their emails. As
  a result, a [moderation rule] is created for the author’s
  email address with the status Always allow.
- Ban: to blacklist the author, i.e. automatically discard all their emails. In the
  pop-up window that opens, click Ban to ban the author without notifying them, or
  specify an explanation, then click Send & Ban to ban the author and send them the
  explanation. As a result, a [moderation rule] is created for
  the author’s email address with the status Permanent ban.

> **Note:**
>
> Messages can also be moderated from the group’s list of messages. Go to Website
> ‣ Groups ‣ Mailing List Groups, select the mail group and click the Emails smart
> button.

## Whitelisting/Blacklisting authors

You can whitelist or blacklist an author either directly [from a mail group message], or by creating a moderation rule. To do so, go to
Website ‣ Configuration ‣ Moderation Rules and click New. Then,
select the Group, specify the author’s Email and set the Status
field.

> **Note:**
>
> You can also access the mail group’s moderation rules by going to Website ‣
> Configuration ‣ Mailing Lists, selecting the group, then clicking the Moderations
> smart button.
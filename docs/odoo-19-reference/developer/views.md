# Views — Form, List, Kanban, Graph, Pivot & More

> **Odoo 19.0 Reference**
> Source: www.odoo.com/documentation/19.0 — HTML converted via markdownify

## Purpose

Defines the XML architecture of all Odoo view types: form, list, kanban, graph, pivot, calendar, map, and cohort. Use when building or customising any Odoo UI view.

---

# View records

Views are what define how records should be displayed to end-users. They are specified in XML and
stored as records themselves, meaning they can be edited independently from the models that they
represent. They are flexible and allow a high level of customization of the screens that they
control. There exist various [types of views]. Each represents a
visualization mode: *form*, *list*, *kanban*, etc.

## Generic structure

Basic views generally share the common minimal structure defined below. Placeholders are denoted in
all caps.

```
<record id="ADDON.MODEL_view_TYPE" model="ir.ui.view">
  <field name="name">NAME</field>
  <field name="model">MODEL</field>
  <field name="arch" type="xml">
    <VIEW_TYPE>
      <views/>
    </VIEW_TYPE>
  </field>
</record>
```

## View types

[Form](view_architectures.html#reference-view-architectures-form)
:   Display and edit the data from a single record.

[List](view_architectures.html#reference-view-architectures-list)
:   View and edit multiple records.

[Search](view_architectures.html#reference-view-architectures-search)
:   Apply filters and perform searches. The results are displayed in the current list, kanban… view.

[Kanban](view_architectures.html#reference-view-architectures-kanban)
:   Display records as “cards”, configurable as a small template.

[Qweb](view_architectures.html#reference-view-architectures-qweb)
:   Templating of reporting, website…

[Graph](view_architectures.html#reference-view-architectures-graph)
:   Visualize aggregations over a number of records or record groups.

[Pivot](view_architectures.html#reference-view-architectures-pivot)
:   Display aggregations as a [pivot table](https://en.wikipedia.org/wiki/Pivot_table).

[Calendar](view_architectures.html#reference-view-architectures-calendar)
:   Display records as events in a daily, weekly, monthly, or yearly calendar.

[Cohort](view_architectures.html#reference-view-architectures-cohort) Enterprise feature
:   Display and understand the way some data changes over a period of time.

[Gantt](view_architectures.html#reference-view-architectures-gantt) Enterprise feature
:   Display records as a Gantt chart.

[Grid](view_architectures.html#reference-view-architectures-grid) Enterprise feature
:   Display computed information in numerical cells; are hardly configurable.

[Map](view_architectures.html#reference-view-architectures-map) Enterprise feature
:   Display records on a map, and the routes between them.

## Fields

View records expose a number of fields.

*class* odoo.addons.base.models.ir\_ui\_view.IrUiView[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/addons/base/models/ir_ui_view.py#L139)
:   name
    :   Only useful as a mnemonic/description of the view when looking for one in a list of some sort.
        Most Odoo view names start with the name of the addon and end with the type of view being
        discussed.

        Requirement
        :   Optional

        Type
        :   [`Char`](../backend/orm.html#odoo.fields.Char "odoo.fields.Char")

    model
    :   The model linked to the view, if applicable.

        Requirement
        :   Mandatory

        Type
        :   [`Char`](../backend/orm.html#odoo.fields.Char "odoo.fields.Char")

    arch
    :   The description of the view layout depending on the [view type](view_architectures.html).

        Requirement
        :   Optional

        Type
        :   [`Text`](../backend/orm.html#odoo.fields.Text "odoo.fields.Text")

    groups\_id
    :   The groups allowed to use/access the current view.

        If the view extends an existing view, the extension will be applied only for a given user, if
        that user has access to the provided `groups_id`.

        Requirement
        :   Optional

        Type
        :   [`Many2many`](../backend/orm.html#odoo.fields.Many2many "odoo.fields.Many2many") -> `Groups`

    priority
    :   When requesting a view by specifying the `model` and `type`, the matching view with the lowest
        priority is returned (it is the default view).

        It also defines the order of views application during [view resolution]. When a view is requested by `id` and its
        mode is not `primary`, its *closest* parent with `mode` = `primary` is matched.

        Requirement
        :   Optional

        Type
        :   [`Integer`](../backend/orm.html#odoo.fields.Integer "odoo.fields.Integer")

    inherit\_id
    :   Reference to the parent view on which the [inheritance] will be applied. Its value is used by default. Specify
        the parent using the `ref` attribute with `ref="ADDON.MODEL_parent_view_TYPE"`.

        The addon name (before the dot) is not necessary if the inheritance is done on a record of the
        same module.

        See [Inheritance] for more information.

        Requirement
        :   Optional

        Type
        :   [`Many2one`](../backend/orm.html#odoo.fields.Many2one "odoo.fields.Many2one")

    mode
    :   Only applies if this view inherits from an other one (`inherit_id` is set).

        extension
        :   If the view is requested, the closest primary view is looked up (via `inherit_id`). Then,
            all views inheriting from it with this view’s model are applied.

        primary
        :   The closest primary view is fully resolved (even if it uses a different model than the
            current one). Then, the view’s [inheritance specs] are applied, and the result is used as if it
            were this view’s actual arch.

        A case in which one would want to override `mode` while using `inherit_id` is delegation
        inheritance. In that case, your derived model is separated from its parent, and views
        matching with one won’t match with the other. Assuming one inherits from a view associated
        with the parent model and wants to customize the derived view to show data from the derived
        model, the `mode` of the derived view needs to be set to `primary` because it is the base (and
        maybe only) view for that derived model. Otherwise, the [view matching] rules won’t apply.

        See [Inheritance] for more information.

        Requirement
        :   Optional

        Type
        :   [`Selection`](../backend/orm.html#odoo.fields.Selection "odoo.fields.Selection"): `extension` / `primary`

        Default
        :   `extension`

> **Note:**
>
> The current context and user access rights may also impact the view abilities.

## Inheritance

Inheritance allows for customizing delivered views. It makes it possible, for example, to add
content as modules are installed, or to deliver different displays according to the action.

Inherit views generally share the common structure defined below. Placeholders are denoted in all
caps. This synthetic view will update a node targeted by an XPath, and another targeted by its name
and attributes.

```
<record id="ADDON.MODEL_view_TYPE" model="ir.ui.view">
    <field name="model">MODEL</field>
    <field name="inherit_id" ref="VIEW_REFERENCE"/>
    <field name="mode">MODE</field>
    <field name="arch" type="xml">
        <xpath expr="XPATH" position="POSITION">
            <CONTENT/>
        </xpath>
        <NODE ATTRIBUTES="VALUES" position="POSITION">
            <CONTENT/>
        </NODE>
    </field>
</record>
```

The `inherit_id` and `mode` fields determine the [view resolution]. The `xpath` or `NODE` elements indicate the
[inheritance specs]. The `expr` and `position`
attributes specify the [inheritance position].

### View resolution

Resolution generates the final `arch` for a requested/matched `primary` view as follow:

1. if the view has a parent, the parent is fully resolved, then the current view’s inheritance specs
   are applied;
2. if the view has no parent, its `arch` is used as-is;
3. the current view’s children with mode `extension` are looked up, and their inheritance specs are
   applied depth-first (a child view is applied, then its children, then its siblings).

The inheritance is applied according to the `inherit_id` field. If several view records inherit the
same view, the order is determined by the `priority`.

The result of applying children views yields the final `arch`.

### Inheritance specs

Inheritance specs are applied sequentially and are comprised of:

1. an element locator to match the inherited element in the parent view;
2. children element to modify the inherited element.

There are three types of element locators:

- An `xpath` element with an `expr` attribute. `expr` is an [XPath](https://en.wikipedia.org/wiki/XPath) expression[1] applied to the current `arch`,
  matching the first node it finds;
- A `field` element with a `name` attribute, matching the first field with the same `name`.

  > **Note:**
  >
  > All other attributes are ignored.
- Any other element, matching the first element with the same `name` and identical attributes.

  > **Note:**
  >
  > The attributes `position` and `version` are ignored.

[1]
:   An extension function is added for simpler matching in QWeb views:
    `hasclass(*classes)` matches if the context node has all the specified classes.

> **Tip:**
>
> ```
> <xpath expr="page[@name='pg']/group[@name='gp']/field" position="inside">
>     <field name="description"/>
> </xpath>
>
> <div name="name" position="replace">
>     <field name="name2"/>
> </div>
> ```

### Inheritance position

The inheritance specs accept an optional `position` attribute, defaulting to `inside`, that
specifies how the matched node should be modified.

inside
:   The content of the inheritance spec is appended to the matched node.

    > **Tip:**
    >
    > ```
    > <notebook position="inside">
    >     <page string="New feature">
    >         ...
    >     </page>
    > </notebook>
    > ```

after
:   The content of the inheritance spec is appended to the matched node’s parent after the matched
    node.

    > **Tip:**
    >
    > ```
    > <xpath expr="//field[@name='x_field']" position="after">
    >     <field name="x_other_field"/>
    > </xpath>
    > ```

before
:   The content of the inheritance spec is appended to the matched node’s parent before the matched
    node.

    > **Tip:**
    >
    > ```
    > <field name=x_field" position="before">
    >     <field name="x_other_field"/>
    > </field>
    > ```

replace
:   The content of the inheritance spec replaces the matched node. Any text node containing only `$0`
    within the contents of the spec is replaced by a copy of the matched node, effectively wrapping
    the matched node.

    > **Tip:**
    >
    > ```
    > <xpath expr="//field[@name='x_field']" position="replace">
    >     <div class="wrapper">
    >         $0
    >     </div>
    > </xpath>
    > ```

attributes
:   The content of the inheritance spec should be made of only `attribute` elements, each with a
    `name` attribute and an optional body.

    - If the `attribute` element has a body, a new attributed named after its `name` is added to the
      matched node with the `attribute` element’s text as value.
    - If the `attribute` element has no body, the attribute named after its `name` is removed from the
      matched node.
    - If the `attribute` element has an `add` attribute, a `remove` attribute, or both, the value of
      the matched node’s attribute named after `name` is recomputed to account for the value(s) of
      `add`, `remove`, and an optional `separator` attribute defaulting to `,`. `add` includes its
      value(s), separated by `separator`. `remove` removes its value(s), separated by `separator`.

    > **Tip:**
    >
    > ```
    > <field name="x_field" position="attributes">
    >     <attribute name="invisible">True</attribute>
    >     <attribute name="class" add="mt-1 mb-1" remove="mt-2 mb-2" separator=" "/>
    > </field>
    > ```

move
:   The attribute `position="move"` is set on the content of the inheritance spec to specify how nodes
    are moved relatively to the inheritance spec’s element locator, on which the attribute `position`
    must also be set, with values `inside`, `replace`, `after`, or `before`.

    > **Tip:**
    >
    > ```
    > <xpath expr="//@target" position="after">
    >     <xpath expr="//@node" position="move"/>
    > </xpath>
    >
    > <field name="target_field" position="after">
    >     <field name="my_field" position="move"/>
    > </field>
    > ```

## Model commons

*class* odoo.addons.base.models.ir\_ui\_view.Base[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/addons/base/models/ir_ui_view.py#L2725)
:   get\_views(*views*, *options=None*)[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/addons/base/models/ir_ui_view.py#L2900)
    :   Returns the fields\_views of given views, along with the fields of
        the current model, and optionally its filters for the given action.

        The return of the method can only depend on the requested view types,
        access rights (views or other records), view access rules, options,
        context lang and TYPE\_view\_ref (other context values cannot be used).

        Python expressions contained in views or representing domains (on
        python fields) will be evaluated by the client with all the context
        values as well as the record values it has.

        Parameters
        :   - **views** – list of [view\_id, view\_type]
            - **options** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")) –

              a dict optional boolean flags, set to enable:

              `toolbar`
              :   includes contextual actions when loading fields\_views

              `load_filters`
              :   returns the model’s filters

              `action_id`
              :   id of the action to get the filters, otherwise loads the global
                  filters or the model

        Returns
        :   dictionary with fields\_views, fields and optionally filters

    get\_view([*view\_id | view\_type='form'*])[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/addons/base/models/ir_ui_view.py#L3134)
    :   Get the detailed composition of the requested view like model, view
        architecture.

        The return of the method can only depend on the requested view types,
        access rights (views or other records), view access rules, options,
        context lang and TYPE\_view\_ref (other context values cannot be used).

        Parameters
        :   - **view\_id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") *or* [*None*](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")) – id of the view or None
            - **view\_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) – type of the view to return if view\_id is None,
              one of `'form'`, `'list'`, …
            - **options** –

              options to return additional features

              param bool mobile
              :   true if the web client is currently using the
                  responsive mobile view (to use kanban views instead of list
                  views for x2many fields)

        Returns
        :   composition of the requested view (including inherited views
            and extensions)

        Return type
        :   [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")

        Raises
        :   [**AttributeError**](https://docs.python.org/3/library/exceptions.html#AttributeError "(in Python v3.13)") –

            - if the inherited view has unknown position to work with other
              than ‘before’, ‘after’, ‘inside’, ‘replace’
            - if some tag other than ‘position’ is found in parent view

---

# View architectures

## Generic architecture

The architecture of a view is defined by XML data interpreted by the JavaScript framework.

For most views, there is a `*.rng` file defining the attributes and possible architectures.
Some views are not ruled by such a file either because they accept HTML content, or for performance
reasons.

> **Note:**
>
> The current context and user access rights may impact the view abilities.

> **Note:**
>
> [View records](view_records.html)

## Python expression

When evaluating node attributes, e.g. the `readonly` modifier, it is possible to provide a **Python
expression** that will be executed in an environment that has access to the following variables:

- The names of all fields present in the current view, containing the value of the current record,
  except for `column_invisible` in [list view];
  relational fields are given as a list of IDs;
- The ID of the current record;
- `parent`: the record that refers to the container; only inside sub-views of [relational
  fields](../../../applications/studio/fields.html#studio-fields-relational-fields);
- `context (dict)`: the current view’s context;
- `uid (int)`: the id of the current user;
- `today (str)`: the current local date in the `YYYY-MM-DD` format;
- `now (str)`: the current local datetime in the `YYYY-MM-DD hh:mm:ss` format.

> **Tip:**
>
> ```
> <field name="field_a" readonly="True"/>
> <field name="field_b" invisible="context.get('show_me') and field_a == 4"/>
> ```

> **Tip:**
>
> ```
> <field name="field_a"/>
> <field name="x2m">
>     <!-- sub-view -->
>     <form>
>         <field name="field_b" invisible="parent.field_a"/>
>     </form>
> </field>
> ```

## Form

Form views are used to display the data from a single record. They are composed of regular [HTML](https://en.wikipedia.org/wiki/HTML)
with additional semantic and structural components.

The root element of form views is `form`.

```
<form>
    ...
</form>
```

### Root attributes

Optional attributes can be added to the root element `form` to customize the view.

string
:   The view title. It is displayed only if you open an action that has no name and whose target is
    `new` (opening a dialog).

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

create
:   Disable/enable record creation on the view.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

edit
:   Disable/enable record edition on the view.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

duplicate
:   Disable/enable record duplication on the view through the **Action** dropdown.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

delete
:   Disable/enable record deletion on the view through the Action dropdown.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

js\_class
:   The name of the JavaScript component the webclient will instantiate instead of the form view.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

disable\_autofocus
:   Disable automatic focusing on the first field in the view.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `False`

### Semantic components

Semantic components tie into the Odoo system and allow interaction with it.

Form views accept the following children semantic components: [field], [label],
[button],
[Chatter widget], and
[Attachments preview widget].

Placeholders are denoted in all caps.

#### `field`: display field values

The `field` element renders (and allows editing of, possibly) a single field of the current record.

Using the same field multiple times in a form view is supported, and the fields can receive
different values for the `invisible` and `readonly` attributes. These fields may have the same
values but can be displayed differently. However, the behavior is not guaranteed when several fields
exist with different values for the `required` attribute.

```
<form>
    <field name="FIELD_NAME"/>
</form>
```

The `field` element can have the following attributes:

name
:   The name of the field to render.

    Requirement
    :   Mandatory

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

widget
:   The widget used to represent the field. The selected widget can change the way the field is
    rendered and/or the way it can be edited. It refers to a Javascript implementation (an Owl
    component) registered to the `fields` registry.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

id
:   The node id. Useful when there are several occurrences of the same field in the view (see
    [label: display field labels]).

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   The field name

string
:   The label of the field.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   The `string` attribute of the model’s field

help
:   The tooltip displayed when hovering the field or its label.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

options
:   The configuration options for the field’s widget (including default widgets), as a Python
    expression that evaluates to a dict.

    For relation fields, the following options are available: `no_create`, `no_quick_create`,
    `no_open`, and `no_create_edit`.

    > **Tip:**
    >
    > ```
    > <field name="tag_ids" widget="many2many_tags" options="{'color_field': 'FIELD_NAME', 'no_quick_create': True}"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `{}`

readonly
:   Whether the field can be modified by the user (`False`) or is read-only (`True`), as a Python
    expression that evaluates to a bool.

    > **Tip:**
    >
    > ```
    > <field name="fname_a" readonly="True"/>
    > <field name="fname_b" readonly="name_a in [fname_b, parent.fname_d]"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `False`

required
:   Whether the field can be left empty (`False`) or must be set (`True`), as a Python expression
    that evaluates to a bool.

    > **Tip:**
    >
    > ```
    > <field name="fname_a" required="True"/>
    > <field name="fname_b" required="fname_c != 3"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `False`

invisible
:   Whether the element is visible (`False`) or hidden (`True`), as a Python expression that
    evaluates to a bool.

    > **Note:**
    >
    > There are two uses for the `invisible` attribute:
    >
    > - Usability: to avoid overloading the view and to make it easier for the user to read,
    >   depending on the content.
    > - Technical: a field must be present (invisible is enough) in the view to be used in a
    >   Python expression.

    > **Tip:**
    >
    > ```
    > <field name="fname_b" invisible="fname_c != 3 and fname_a == parent.fname_d"/>
    > <group invisible="fname_c != 4">
    >     <field name="fname_c"/>
    >     <field name="fname_d"/>
    > <group>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `False`

groups
:   The comma-separated list of user groups to whom the element is displayed. Users who do not belong
    to at least one of these groups are unable to see the element. Groups can be prefixed with the
    negative `!` operator to exclude them.

    > **Tip:**
    >
    > ```
    > <field name="FIELD_NAME" groups="base.group_no_one,!base.group_multi_company"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

domain
:   The filters to apply when displaying existing records for selection, as a Python expression that
    evaluates to a [domain](../backend/orm.html#reference-orm-domains).

    > **Tip:**
    >
    > ```
    > <field name="fname" domain="[('fname_a', '=', parent.fname_b)]"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `[]`

    Scope
    :   Relational fields

context
:   The context to use when fetching possible values and creating or searching records, as a Python
    expression that evaluates to a dict.

    > **Tip:**
    >
    > ```
    > <field name="fname" context="{
    >     'TYPE_view_ref': 'ADDON.MODEL_view_TYPE',
    >     'group_by': 'FIELD_NAME',
    >     'default_FIELD_NAME': ANY,
    >     'search_default_FIELD_NAME': True,
    >     'OTHER_BUSINESS_KEY': ANY,
    >   }"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `{}`

    Scope
    :   Relational fields

nolabel
:   Whether the field label should be hidden.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `False`

    Scope
    :   Fields that are a direct child of a `group` element

placeholder
:   The help message to display on *empty* fields. It can replace field labels in complex forms.
    However, it *should not* be an example of data, as users may confuse placeholder text with filled
    fields.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

mode
:   The comma-separated list of display modes (view types) to use for the field’s linked records.
    Allowed modes are: `list`, `form`, `kanban`, and `graph`.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `list`

    Scope
    :   [`One2many`](../backend/orm.html#odoo.fields.One2many "odoo.fields.One2many") and [`Many2many`](../backend/orm.html#odoo.fields.Many2many "odoo.fields.Many2many") fields

class
:   The [HTML class](https://en.wikipedia.org/wiki/HTML_attribute) to set on the generated element.

    The styling uses the [Bootstrap](https://getbootstrap.com) framework and [UI icons](icons.html#reference-user-interface-ui-icons). Common Odoo classes include:

    - `oe_inline`: prevents the usual line break following fields, and limits their span;
    - `oe_left`, `oe_right`: [floats](https://developer.mozilla.org/en-US/docs/Web/CSS/float) the
      element to the corresponding direction;
    - `oe_read_only`, `oe_edit_only`: only displays the element in the corresponding form mode;
    - `oe_avatar`: for image fields, displays images as an “avatar” (max 90x90 square);
    - `oe_stat_button`: defines a particular rendering to dynamically display information while being
      clickable to target an action.

    > **Tip:**
    >
    > ```
    > <field name="fname" class="oe_inline oe_left oe_avatar"/>
    > ```

    > **Tip:**
    >
    > ```
    > <button type="object" name="ACTION" class="oe_stat_button" icon="FONT_AWESOME" help="HELP">
    >    <div class="o_field_widget o_stat_info">
    >       <span class="o_stat_value"><FIELD/></span>
    >       <span class="o_stat_text">TEXT</span>
    >    </div>
    > </button>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

filename
:   The name of the related field providing the name of the file.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

    Scope
    :   [`Binary`](../backend/orm.html#odoo.fields.Binary "odoo.fields.Binary") fields

password
:   Whether the field stores a password and thus its data should not be displayed.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `False`

    Scope
    :   [`Char`](../backend/orm.html#odoo.fields.Char "odoo.fields.Char") fields

kanban\_view\_ref
:   The XMLID of the specific Kanban [view record](view_records.html) that should be used when
    selecting records in a mobile environment.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

    Scope
    :   Relational fields

default\_focus
:   Whether the field is focused when the view opens. It can be applied to only one field of a view.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `False`

> **Note:**
>
> [Relational fields](../../../applications/studio/fields.html#studio-fields-relational-fields) nodes can contain specific subviews.
>
> ```
> <field name="children_ids">
>    <list>
>       <field name="name"/>
>    </list>
>    <form>
>       <field name="id"/>
>       <field name="name"/>
>    </form>
> </field>
> ```

#### `label`: display field labels

When a [field] component is not placed directly
inside a [group], or when its `nolabel` attribute is
set, the field’s label is not automatically displayed alongside its value. The `label` component is
the manual alternative of displaying the label of a field.

```
<form>
    <div class="col col-md-auto">
        <label for="FIELD_NAME" string="LABEL"/>
        <div>
            <field name="FIELD_NAME" class="oe_inline"/>
        </div>
    </div>
</form>
```

The `label` element can have the following attributes:

for
:   The reference to the field associated with the label. It can be either the name of the field, or
    its id (the `id` attribute set on the [field]).

    When there are several occurrences of the same field in the view, and there are several `label`
    components associated with these field nodes, these labels must have unique `for` attribute; in
    this case, referencing the `id` attribute of the corresponding field nodes.

    Requirement
    :   Mandatory

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

string
:   The label to display.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   The field’s label coming from the field definition on the model

class
:   The [HTML class](https://en.wikipedia.org/wiki/HTML_attribute) to set on the generated element.

    The styling uses the [Bootstrap](https://getbootstrap.com) framework and [UI icons](icons.html#reference-user-interface-ui-icons). Common Odoo classes include:

    - `oe_inline`: prevents the usual line break following fields, and limits their span;
    - `oe_left`, `oe_right`: [floats](https://developer.mozilla.org/en-US/docs/Web/CSS/float) the
      element to the corresponding direction;
    - `oe_read_only`, `oe_edit_only`: only displays the element in the corresponding form mode;
    - `oe_avatar`: for image fields, displays images as an “avatar” (max 90x90 square);
    - `oe_stat_button`: defines a particular rendering to dynamically display information while being
      clickable to target an action.

    > **Tip:**
    >
    > ```
    > <field name="fname" class="oe_inline oe_left oe_avatar"/>
    > ```

    > **Tip:**
    >
    > ```
    > <button type="object" name="ACTION" class="oe_stat_button" icon="FONT_AWESOME" help="HELP">
    >    <div class="o_field_widget o_stat_info">
    >       <span class="o_stat_value"><FIELD/></span>
    >       <span class="o_stat_text">TEXT</span>
    >    </div>
    > </button>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

invisible
:   Whether the element is visible (`False`) or hidden (`True`), as a Python expression that
    evaluates to a bool.

    > **Note:**
    >
    > There are two uses for the `invisible` attribute:
    >
    > - Usability: to avoid overloading the view and to make it easier for the user to read,
    >   depending on the content.
    > - Technical: a field must be present (invisible is enough) in the view to be used in a
    >   Python expression.

    > **Tip:**
    >
    > ```
    > <field name="fname_b" invisible="fname_c != 3 and fname_a == parent.fname_d"/>
    > <group invisible="fname_c != 4">
    >     <field name="fname_c"/>
    >     <field name="fname_d"/>
    > <group>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `False`

#### `button`: display action buttons

```
<form>
    <button type="object" name="ACTION" string="LABEL"/>
    <button type="object" name="ACTION" icon="FONT_AWESOME"/>
</form>
```

The `button` element can have the following attributes:

type
:   The type of the button indicating how it behaves. It can have two different values:

    object
    :   Call a method on the view’s model. The button’s `name` is the method that is called with the
        current record ID and the current `context`.

    action
    :   Load and execute an `ir.actions` action record. The button’s `name` is the XMLID of the
        action to load. The `context` is extended with the view’s model (as `active_model`) and with
        the current record (as `active_id`).

    > **Tip:**
    >
    > ```
    > <button type="object" name="action_create_new" string="Create document"/>
    > <button type="action" name="addon.action_create_view" string="Create and Edit"/>
    > ```

    Requirement
    :   Mandatory if the `special` attribute is not set

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

name
:   The method to call if the `type` is `object`. The [XMLID](../../glossary.html#term-external-identifier) of the
    action to load if the `type` is `action`, either in raw format or in `%(XMLID)d` format.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

string
:   The button’s text if there is no `icon`, the `alt` text for the icon otherwise.

    > **Tip:**
    >
    > ```
    > <button type="object" name="action_create_new" string="Create document"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

icon
:   The icon to use to display the button. See [icons](icons.html#reference-user-interface-ui-icons) for
    the reference list.

    > **Tip:**
    >
    > ```
    > <button type="object" name="remove" icon="fa-trash"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

help
:   The tooltip message shown when hovering with the mouse cursor.

    > **Tip:**
    >
    > ```
    > <button type="object" name="remove" icon="fa-trash" help="Revoke"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

context
:   The context that is merged into the view’s context when performing the button’s call, as a Python
    expression that evaluates to a dict.

    > **Tip:**
    >
    > ```
    > <button name="button_confirm" type="object" context="{'BUSINESS_KEY': ANY}" string="LABEL"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `{}`

groups
:   The comma-separated list of user groups to whom the element is displayed. Users who do not belong
    to at least one of these groups are unable to see the element. Groups can be prefixed with the
    negative `!` operator to exclude them.

    > **Tip:**
    >
    > ```
    > <field name="FIELD_NAME" groups="base.group_no_one,!base.group_multi_company"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

invisible
:   Whether the element is visible (`False`) or hidden (`True`), as a Python expression that
    evaluates to a bool.

    > **Note:**
    >
    > There are two uses for the `invisible` attribute:
    >
    > - Usability: to avoid overloading the view and to make it easier for the user to read,
    >   depending on the content.
    > - Technical: a field must be present (invisible is enough) in the view to be used in a
    >   Python expression.

    > **Tip:**
    >
    > ```
    > <field name="fname_b" invisible="fname_c != 3 and fname_a == parent.fname_d"/>
    > <group invisible="fname_c != 4">
    >     <field name="fname_c"/>
    >     <field name="fname_d"/>
    > <group>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `False`

class
:   The [HTML class](https://en.wikipedia.org/wiki/HTML_attribute) to set on the generated element.

    The styling uses the [Bootstrap](https://getbootstrap.com) framework and [UI icons](icons.html#reference-user-interface-ui-icons). Common Odoo classes include:

    - `oe_inline`: prevents the usual line break following fields, and limits their span;
    - `oe_left`, `oe_right`: [floats](https://developer.mozilla.org/en-US/docs/Web/CSS/float) the
      element to the corresponding direction;
    - `oe_read_only`, `oe_edit_only`: only displays the element in the corresponding form mode;
    - `oe_avatar`: for image fields, displays images as an “avatar” (max 90x90 square);
    - `oe_stat_button`: defines a particular rendering to dynamically display information while being
      clickable to target an action.

    > **Tip:**
    >
    > ```
    > <field name="fname" class="oe_inline oe_left oe_avatar"/>
    > ```

    > **Tip:**
    >
    > ```
    > <button type="object" name="ACTION" class="oe_stat_button" icon="FONT_AWESOME" help="HELP">
    >    <div class="o_field_widget o_stat_info">
    >       <span class="o_stat_value"><FIELD/></span>
    >       <span class="o_stat_text">TEXT</span>
    >    </div>
    > </button>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

special
:   The behavior of the button for form views opened in dialog. It can have two different values:

    save
    :   Save the record and close the dialog.

    cancel
    :   Close the dialog without saving.

    > **Tip:**
    >
    > ```
    > <button special="cancel" icon="fa-trash"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

confirm
:   The confirmation message to display (and for the user to accept) before performing the button’s
    action.

    > **Tip:**
    >
    > ```
    > <button name="action_destroye_gate" string="Send the goa'uld" type="object" confirm="Do you confirm the action?"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

data-hotkey
:   The hotkey ([keyboard\_shortcut](https://en.wikipedia.org/wiki/Keyboard_shortcut), similar to an [accesskey](https://www.w3.org/TR/html5/editing.html#the-accesskey-attribute)) that is bound to the button. It is
    enabled when the `alt` key is pressed together with the selected character, or together with the
    `shift` key and the selected character when `shift+` is prepended to the value.

    > **Tip:**
    >
    > ```
    > <button type="object" name="action_confirm" string="Confirm" data-hotkey="c"/>
    > <button type="object" name="action_tear" string="Tear the sheet" data-hotkey="shift+k"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

#### Chatter widget

The [chatter widget](../backend/mixins.html#reference-mixins-mail-chatter) is the communication and log tool allowing
to email colleagues and customers directly from a record (task, order, invoice, event, note…).

It is added with a `div` element with the class `oe_chatter` when the model inherits the
`mail.thread` mixin.

> **Tip:**
>
> ```
> <form>
>     <sheet>
>         ...
>     </sheet>
>     <div class="oe_chatter">
>         <field name="message_follower_ids"/>
>         <field name="activity_ids"/>
>         <field name="message_ids" options="OPTIONS"/>
>     </div>
> </form>
> ```

#### Attachments preview widget

The attachment preview widget is added with an *empty* `div` element with the class
`o_attachment_preview`.

> **Tip:**
>
> ```
> <form>
>     <sheet>
>         ...
>     </sheet>
>     <div class="o_attachment_preview"/>
> <form>
> ```

### Structural components

Structural components provide structure or “visual” features with little logic. They are used as
elements or sets of elements in form views.

Form views accept the following children structural components: [group], [sheet],
[notebook],
[notebook],
[newline],
[separator],
[header],
[footer],
[Buttons container], and
[Title container].

Placeholders are denoted in all caps.

#### `group`: define columns layouts

The `group` element is used to define column layouts in forms. By default, groups define 2 columns,
and most direct children of groups take a single column.

[field] elements that are direct children of groups
display a `label` by default, and the label and the field itself have a `colspan` of `1` each.

Children are laid out horizontally (they try to fill the next column before changing row).

```
 <form>
     <group>
         ...
     </group>
</form>
```

The `group` element can have the following attributes:

string
:   The title displayed for the group.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

col
:   The number of columns in a `group`.

    Requirement
    :   Optional

    Type
    :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")

    Default
    :   `2`

colspan
:   The number of columns taken by a child element.

    Requirement
    :   Optional

    Type
    :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")

    Default
    :   `1`

invisible
:   Whether the element is visible (`False`) or hidden (`True`), as a Python expression that
    evaluates to a bool.

    > **Note:**
    >
    > There are two uses for the `invisible` attribute:
    >
    > - Usability: to avoid overloading the view and to make it easier for the user to read,
    >   depending on the content.
    > - Technical: a field must be present (invisible is enough) in the view to be used in a
    >   Python expression.

    > **Tip:**
    >
    > ```
    > <field name="fname_b" invisible="fname_c != 3 and fname_a == parent.fname_d"/>
    > <group invisible="fname_c != 4">
    >     <field name="fname_c"/>
    >     <field name="fname_d"/>
    > <group>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `False`

> **Note:**
>
> |  |
> | --- |
> | ../../../_images/form_group.svg |
> | ``` <group>     <field name="a" string="custom"/>     <field name="b"/> </group> <group string="title 1">     <group string="title 2">         <field name="c"/>         <field name="d"/>     </group>     <group>         <field name="e"/>         <field name="f"/>         <field name="g"/>     </group> </group> <group col="12">     <group colspan="8">         <field name="h"/>     </group>     <group colspan="4">         <field name="i"/>     </group> </group> ``` |

#### `sheet`: make the layout responsive

The `sheet` element can be used as a direct child of the [form] root element for a narrower and more responsive form layout
(centered page, margin…). It usually contains [group] elements.

```
<form>
    <sheet>
        ...
    </sheet>
</form>
```

#### `notebook` & `page`: add tabbed sections

The `notebook` element defines a tabbed section. Each tab is defined through a `page` child element.

The `notebook` element should not be placed within `group` elements.

```
<form>
    <notebook>
        <page string="LABEL">
            ...
        </page>
    </notebook>
</form>
```

The `page` element can have the following attributes:

string
:   The title of the tab.

    Requirement
    :   Optional

    Type
    :   `str`

    Default
    :   `''`

invisible
:   Whether the element is visible (`False`) or hidden (`True`), as a Python expression that
    evaluates to a bool.

    > **Note:**
    >
    > There are two uses for the `invisible` attribute:
    >
    > - Usability: to avoid overloading the view and to make it easier for the user to read,
    >   depending on the content.
    > - Technical: a field must be present (invisible is enough) in the view to be used in a
    >   Python expression.

    > **Tip:**
    >
    > ```
    > <field name="fname_b" invisible="fname_c != 3 and fname_a == parent.fname_d"/>
    > <group invisible="fname_c != 4">
    >     <field name="fname_c"/>
    >     <field name="fname_d"/>
    > <group>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `False`

> **Note:**
>
> |  |
> | --- |
> | ../../../_images/form_notebook.svg |
> | ``` <form>     <notebook>         <page string="Page1">             ...         </page>         <page string="Page2">             ...         </page>     </notebook> </form> ``` |

#### `newline`: start new group rows

The `newline` element is used within [group]
elements to end the current row early and immediately switch to a new row, without filling any
remaining column beforehand.

```
<form>
    <group>
        ...
        <newline/>
        ...
    </group>
</form>
```

> **Note:**
>
> |  |
> | --- |
> | ../../../_images/form_newline.svg |
> | ``` <form>     <group string="Title 1">         <group string="Title 1.1">...</group>         <newline/>         <group string="Title 1.2">...</group>         <group string="Title 1.3">...</group>     </group> </form> ``` |

#### `separator`: add horizontal spacing

The `separator` element adds vertical spacing between elements within a group.

```
<form>
    ...
    <separator/>
    ...
</form>
```

The `<separator>` element can have the following attributes:

string
:   The title as a section title.

    Requirement
    :   Optional

    Type
    :   `str`

    Default
    :   `''`

> **Note:**
>
> |  |
> | --- |
> | ../../../_images/form_separator.svg |
> | ``` <form>     <group>         <FIELD/>         <separator string="Title 1"/>         <FIELD/>         <group>             <FIELD/>             <separator string="Title 2"/>             <FIELD/>         </group>         <group>             <FIELD/>             <FIELD/>         </group>     </group> </form> ``` |

> **Note:**
>
> The `separator` element can be used to achieve visual separation between elements within the same
> inner `group` element while keeping them horizontally aligned.

#### `header`: display workflow buttons and a status

The `header` element combined with the [sheet]
element provides a full-width location above the sheet itself generally used to display workflow
[button] elements and a [field] element rendered as status widget.

```
<form>
    <header>
        <BUTTONS/>
    </header>
    <sheet>
        ...
    </sheet>
</form>
```

> **Tip:**
>
> ```
> <header>
>     <button string="Reset" type="object" name="set_draft" invisible="state != 'done'"/>
>     <field name="state" widget="statusbar" statusbar_visible="draft,posted" options="{'clickable': 1}"/>
> </header>
> ```

#### `footer`: display dialog buttons

The `footer` element is used to display [buttons]
elements at the end of dialogs.

```
<form>
    <sheet>
        ...
    </sheet>
    <footer>
        <BUTTONS/>
    </footer>
</form>
```

> **Tip:**
>
> ```
> <footer>
>     <button string="Save" special="save"/>
>     <button string="Feature action" type="object" name="my_action" class="btn-primary"/>
>     <button string="Discard" special="cancel"/>
> </footer>
> ```

When no `footer` element is specified, the view’s standard buttons (like Save or Discard) will be
present by default. It is also possible to avoid replacing the standard buttons in form or x2many
dialogs by using the `replace` attribute. This attribute defaults to `True` if not specified but
setting it to `False` (or 0) will make it so that the specified `footer` will be added next to the
default buttons instead of replacing them.

> **Tip:**
>
> ```
> <footer replace="0">
>     <button string="Custom added action" type="object" name="my_action" class="btn-primary"/>
> </footer>
> ```

#### Buttons container

A [button] elements container can be created with a
`div` element with the class `button_box`.

```
<form>
    <div name="button_box">
        <BUTTONS/>
    </div>
<form>
```

> **Note:**
>
> |  |
> | --- |
> | ../../../_images/form_button_box.svg |
> | ``` <form>     <div name="button_box">         <button type="edit" name="edit" icon="fa-edit" string="Button1"/>         <button type="object" name="my_action" icon="fa-dollar">             <field name="total_inv" widget="statinfo" string="Invoices"/>         </button>     </div> <form> ``` |

#### Title container

A title [field] element container can be created with
a `div` element with the class `oe_title`.

```
<form>
    <sheet>
        <div class="oe_title">
            <h1><FIELD/></h1>
        </div>
    </sheet>
<form>
```

## Settings

Settings views are a customization of the [form] view. They
are used to display settings in a centralized place. They differ from generic form views in that
they have a search bar and a sidebar.

> **Tip:**
>
> ```
> <app string="CRM" name="crm">
>     <setting type="header" string="Foo">
>         <field name="foo" title="Foo?."/>
>         <button name="nameAction" type="object" string="Button"/>
>     </setting>
>     <block title="Title of group Bar">
>         <setting help="this is bar" documentation="/applications/technical/web/settings/this_is_a_test.html">
>             <field name="bar"/>
>         </setting>
>         <setting string="This is Big BAR" company_specific="1">
>             <field name="bar"/>
>         </setting>
>     </block>
>     <block title="Title of group Foo">
>         <setting string="Personalize setting" help="this is full personalize setting">
>             <div>This is a different setting</div>
>         </setting>
>     </block>
> </app>
> ```

### Components

Settings views accept the [field], [label] and [button] elements of [form] views, as well as three additional children elements:
[app], [block], and [setting].

Placeholders are denoted in all caps.

#### `app`: declare the application

The `app` element is used to declare the application on the settings view. It creates an entry with
the logo of the application on the sidebar of the view. It also acts as delimiter when searching.

```
<form>
    <app string="NAME" name="TECHNICAL_NAME">
    ...
    </app>
</form>
```

The `app` element can have the following attributes:

string
:   The name of the application.

    Requirement
    :   Mandatory

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

name
:   The technical name of the application (the name of the module).

    Requirement
    :   Mandatory

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

logo
:   The [relative path](https://en.wikipedia.org/wiki/URL) to the logo.

    Requirement
    :   Optional

    Type
    :   [path](https://en.wikipedia.org/wiki/Path_(computing))

    Default
    :   A path computed with the `name` attribute: `/name/static/description/icon.png`

groups
:   The comma-separated list of user groups to whom the element is displayed. Users who do not belong
    to at least one of these groups are unable to see the element. Groups can be prefixed with the
    negative `!` operator to exclude them.

    > **Tip:**
    >
    > ```
    > <field name="FIELD_NAME" groups="base.group_no_one,!base.group_multi_company"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

invisible
:   Whether the element is visible (`False`) or hidden (`True`), as a Python expression that
    evaluates to a bool.

    > **Note:**
    >
    > There are two uses for the `invisible` attribute:
    >
    > - Usability: to avoid overloading the view and to make it easier for the user to read,
    >   depending on the content.
    > - Technical: a field must be present (invisible is enough) in the view to be used in a
    >   Python expression.

    > **Tip:**
    >
    > ```
    > <field name="fname_b" invisible="fname_c != 3 and fname_a == parent.fname_d"/>
    > <group invisible="fname_c != 4">
    >     <field name="fname_c"/>
    >     <field name="fname_d"/>
    > <group>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `False`

#### `block`: declare a group of settings

The `block` element is used to declare a group of settings. This group can have a title and a
description.

```
 <form>
     <app string="NAME" name="TECHNICAL_NAME">
         ...
         <block title="TITLE">
             ...
         </block>
         ...
     </app>
</form>
```

The `block` element can have the following attributes:

title
:   The title of the block of settings. One can search on its value.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

help
:   The description of the block of settings. One can search on its value.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

groups
:   The comma-separated list of user groups to whom the element is displayed. Users who do not belong
    to at least one of these groups are unable to see the element. Groups can be prefixed with the
    negative `!` operator to exclude them.

    > **Tip:**
    >
    > ```
    > <field name="FIELD_NAME" groups="base.group_no_one,!base.group_multi_company"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

invisible
:   Whether the element is visible (`False`) or hidden (`True`), as a Python expression that
    evaluates to a bool.

    > **Note:**
    >
    > There are two uses for the `invisible` attribute:
    >
    > - Usability: to avoid overloading the view and to make it easier for the user to read,
    >   depending on the content.
    > - Technical: a field must be present (invisible is enough) in the view to be used in a
    >   Python expression.

    > **Tip:**
    >
    > ```
    > <field name="fname_b" invisible="fname_c != 3 and fname_a == parent.fname_d"/>
    > <group invisible="fname_c != 4">
    >     <field name="fname_c"/>
    >     <field name="fname_d"/>
    > <group>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `False`

#### `setting`: declare the setting

The `setting` element is used to declare the setting itself.

The first [field] element in the setting is used as
the main field. It is placed on the left panel if it is a boolean field, and on the top of the right
panel otherwise. The field is also used to create the setting label if a `string` attribute is not
defined.

The `setting` element can also contain additional elements (e.g., HTML). All of those elements are
rendered in the right panel.

```
<form>
    <app string="NAME" name="TECHNICAL_NAME">
        <block title="TITLE">
            ...
            <setting string="SETTING_NAME">
                ...
                <field name="FIELD_NAME"/>
                ...
            </setting>
            ...
        </block>
    </app>
</form>
```

The `<setting>` element can have the following attributes:

type
:   By default, a setting is visually separated on two panels (left and right), and is used to edit a
    given [field]. By defining `type="header"`, a
    special kind of setting is rendered instead. This setting is used to modify the scope of the
    other settings. For example, on the Website application, this setting is used to indicate to
    which website the other settings apply. The header setting is visually represented as a banner on
    top of the screen.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

string
:   The text used as the label of the setting.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   The first field’s label

title
:   The text used as a tooltip.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

help
:   The description of the setting. This text is displayed just below the setting label (with the
    class `text-muted`).

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

company\_dependent
:   Whether the setting is company-specific. If set, an icon is displayed next to the setting label.

    It accepts only the value `'1'`.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

documentation
:   The [path](https://en.wikipedia.org/wiki/Path_(computing)) to the documentation on the setting. If set, a clickable icon is displayed next to
    the setting label. The path can be both an absolute or a [relative path](https://en.wikipedia.org/wiki/URL). In the latter case, it
    is relative to `https://www.odoo.com/documentation/<version>`.

    Requirement
    :   Optional

    Type
    :   `path_`

    Default
    :   `''`

groups
:   The comma-separated list of user groups to whom the element is displayed. Users who do not belong
    to at least one of these groups are unable to see the element. Groups can be prefixed with the
    negative `!` operator to exclude them.

    > **Tip:**
    >
    > ```
    > <field name="FIELD_NAME" groups="base.group_no_one,!base.group_multi_company"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

invisible
:   Whether the element is visible (`False`) or hidden (`True`), as a Python expression that
    evaluates to a bool.

    > **Note:**
    >
    > There are two uses for the `invisible` attribute:
    >
    > - Usability: to avoid overloading the view and to make it easier for the user to read,
    >   depending on the content.
    > - Technical: a field must be present (invisible is enough) in the view to be used in a
    >   Python expression.

    > **Tip:**
    >
    > ```
    > <field name="fname_b" invisible="fname_c != 3 and fname_a == parent.fname_d"/>
    > <group invisible="fname_c != 4">
    >     <field name="fname_c"/>
    >     <field name="fname_d"/>
    > <group>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `False`

## List

The root element of list views is `list` (the previous name was `tree`).

> **Note:**
>
> |  |
> | --- |
> | ../../../_images/list.svg |
> | ``` <list>     ... </list> ``` |

### Root attributes

Optional attributes can be added to the root element `list` to customize the view.

string
:   The view title. It is displayed only if you open an action that has no name and whose target is
    `new` (opening a dialog).

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

create
:   Disable/enable record creation on the view.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

edit
:   Disable/enable record edition on the view.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

delete
:   Disable/enable record deletion on the view through the Action dropdown.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

import
:   Disable/enable record import from data on the view.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

export\_xlsx
:   Disable/enable record export to data on the view.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

editable
:   Make the view’s records editable in-place, and allow creating new records from a row of the list.
    It can have two different values:

    top
    :   New records are created from the top of the list.

    bottom
    :   New records are created from the bottom of the list.

    The architecture for the inline [form] view is derived
    from the list view. Most attributes valid on a form view’s fields and buttons are thus accepted
    by list views, although they may not have any meaning if the list view is non-editable.

    > **Warning:**
    >
    > This behavior is disabled if the `edit` attribute is set to `False`.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

multi\_edit
:   Activate the multi-editing feature that allows updating a field to the same value for multiple
    records at once.

    It accepts only the value `'1'`.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

open\_form\_view
:   Display a button at the end of each row to open the record in a form view.

    It has no effect if the view is non-editable.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `False`

default\_group\_by
:   The name of the field on which the records should be grouped by default if no grouping is
    specified via the action or the current [search].

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

default\_order
:   A comma-separated list of fields names that overrides the ordering defined on the model through
    the [`_order`](../backend/orm.html#odoo.models.BaseModel._order "odoo.models.BaseModel._order") attribute.

    To inverse the sorting order of a field, postfix it with `desc`, separated by a space.

    > **Tip:**
    >
    > ```
    > <list default_order="sequence,name desc">
    >     ...
    > </list>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

decoration-<style>
:   The style that should be applied to matching records’ rows, as a Python expression that evaluates
    to a bool.

    `<style>` must be replaced by one of `bf` (bold), `it` (italic), `info`, `warning`, `danger`,
    `muted`, `primary`, and `success`.

    > **Tip:**
    >
    > ```
    > <list decoration-danger="field_qty &gt; field_limit">
    >     ...
    > </list>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `False`

limit
:   The default size of a page. It must be strictly positive.

    Requirement
    :   Optional

    Type
    :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")

    Default
    :   `80` for list views, `40` for X2many lists in form views

groups\_limit
:   The default number of groups on a page when the list view is grouped. It must be strictly
    positive.

    Requirement
    :   Optional

    Type
    :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")

    Default
    :   `80` for list views, `40` for X2many lists in form views

expand
:   Whether the first level of groups should be opened by default when the list view is grouped.

    > **Warning:**
    >
    > It may be slow, depending on the number of groups.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `False`

sample
:   Whether the view should be populated with a set of sample records if none are found for the
    current model.

    These fake records have heuristics for certain field names/models. For example, a field
    `display_name` on the model `res.users` will be populated with sample people names, while an
    `email` field will be in the form `firstname.lastname@sample.demo`.

    The user is unable to interact with these data, and they will be discarded as soon as an action
    is performed (record created, column added, etc.).

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `False`

### Components

List views accept the following children elements: [field], [button], [groupby], [header], [control, and create].

Placeholders are denoted in all caps.

#### `field`: display field values

The `field` element renders (and allows editing of, possibly) a single field of all current records
as a column.

Using the same field multiple times in a list view is not supported

```
<list>
    <field name="FIELD_NAME"/>
</list>
```

The `field` element can have the following attributes:

name
:   The name of the field to render.

    Requirement
    :   Mandatory

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

widget
:   The widget used to represent the field. The selected widget can change the way the field is
    rendered and/or the way it can be edited. It refers to a Javascript implementation (an Owl
    component) registered to the `fields` registry.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

string
:   The label of the field.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   The `string` attribute of the model’s field

optional
:   Make the visibility of the field optional. The field’s column can be hidden or shown through a
    button on the view’s header.

    It can have two different values:

    show
    :   The field is shown by default.

    hide
    :   The field is hidden by default.

    > **Tip:**
    >
    > ```
    > <field name="fname_a" optional="show"/>
    > <field name="fname_b" optional="hide"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

readonly
:   Whether the field can be modified by the user (`False`) or is read-only (`True`), as a Python
    expression that evaluates to a bool.

    > **Tip:**
    >
    > ```
    > <field name="fname_a" readonly="True"/>
    > <field name="fname_b" readonly="name_a in [fname_b, parent.fname_d]"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `False`

required
:   Whether the field can be left empty (`False`) or must be set (`True`), as a Python expression
    that evaluates to a bool.

    > **Tip:**
    >
    > ```
    > <field name="fname_a" required="True"/>
    > <field name="fname_b" required="fname_c != 3"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `False`

invisible
:   Whether the element is visible (`False`) or hidden (`True`), as a Python expression that
    evaluates to a bool.

    > **Note:**
    >
    > There are two uses for the `invisible` attribute:
    >
    > - Usability: to avoid overloading the view and to make it easier for the user to read,
    >   depending on the content.
    > - Technical: a field must be present (invisible is enough) in the view to be used in a
    >   Python expression.

    > **Tip:**
    >
    > ```
    > <field name="fname_b" invisible="fname_c != 3 and fname_a == parent.fname_d"/>
    > <group invisible="fname_c != 4">
    >     <field name="fname_c"/>
    >     <field name="fname_d"/>
    > <group>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `False`

column\_invisible
:   Whether the column is visible (`False`) or hidden (`True`), as a Python expression that evaluates
    to a bool.

    Unlike `invisible`, it affects the entire column, and is evaluated without the subtree values.

    > **Tip:**
    >
    > ```
    > <field name="product_is_late" column_invisible="parent.has_late_products == False"/>
    > <button type="object" name="action_confirm" column_invisible="context.get('hide_confirm')"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `False`

groups
:   The comma-separated list of user groups to whom the element is displayed. Users who do not belong
    to at least one of these groups are unable to see the element. Groups can be prefixed with the
    negative `!` operator to exclude them.

    > **Tip:**
    >
    > ```
    > <field name="FIELD_NAME" groups="base.group_no_one,!base.group_multi_company"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

decoration-<style>
:   The style that should be applied to matching records’ field, as a Python expression that
    evaluates to a bool.

    `<style>` must be replaced by one of `bf` (bold), `it` (italic), `info`, `warning`, `danger`,
    `muted`, `primary`, and `success`.

    > **Tip:**
    >
    > ```
    > <field name="name" decoration-bf="1"/>
    > <field name="quantity" decoration-info="state == 'draft'"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `False`

sum, avg
:   The aggregate to display at the bottom of the column. The aggregation is computed on only
    records that are currently displayed. The aggregation operation must match the corresponding
    field’s `aggregator`.

    > **Tip:**
    >
    > ```
    > <field name="sent" sum="Total" />
    > <field name="clicks_ratio" avg="Average"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

width
:   The list view always tries to optimize the available space among columns. For some field types,
    this is done by enforcing a width, depending on the field type. For instance, we know exactly the
    number of pixels required to display a date, so we can ensure that a column for a date field
    doesn’t take more space than what is strictly necessary, thus leaving the extra space for the
    other columns. However, the framework can’t guess the adequate width for every field types. For
    instance, char fields can be used to encode large values, or 3-letter country codes. In the
    latter case, one can set the width directly in the arch (e.g. `width="40px"`). It represents
    the width (always in pixels) required to render the values inside the cells. The width of the
    column will then be the sum of the given value and the cells’ left and right paddings.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

nolabel
:   Whether the field’s column header should remain empty. If set, the column will not be sortable.

    It accepts only the value `'1'`

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

> **Note:**
>
> When a list view is grouped, numeric fields are aggregated and displayed for each group. Also, if
> there are too many records in a group, a pager appears on the right of the group row. For this
> reason, it is a bad practice to have a numeric field in the last column when the list view is in
> a situation where it can be grouped. However, it does not pose a problem for X2many fields in a
> form view, as they cannot be grouped.

> **Note:**
>
> |  |
> | --- |
> | ../../../_images/list_field.svg |
> | ``` <list>     <field name="name" string="My Custom Name"/>     <field name="amount" sum="Total"/>     <field name="currency_id"/>     <field name="tax_id"/> </list> ``` |

#### `button`: display action buttons

```
<list>
    <button type="object" name="ACTION" string="LABEL"/>
    <button type="object" name="ACTION" icon="FONT_AWESOME"/>
</list>
```

The `button` element can have the following attributes:

type
:   The type of the button indicating how it behaves. It can have two different values:

    object
    :   Call a method on the view’s model. The button’s `name` is the method that is called with the
        current record ID and the current `context`.

    action
    :   Load and execute an `ir.actions` action record. The button’s `name` is the XMLID of the
        action to load. The `context` is extended with the view’s model (as `active_model`) and with
        the current record (as `active_id`).

    > **Tip:**
    >
    > ```
    > <button type="object" name="action_create_new" string="Create document"/>
    > <button type="action" name="addon.action_create_view" string="Create and Edit"/>
    > ```

    Requirement
    :   Mandatory if the `special` attribute is not set

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

name
:   The method to call if the `type` is `object`. The [XMLID](../../glossary.html#term-external-identifier) of the
    action to load if the `type` is `action`, either in raw format or in `%(XMLID)d` format.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

string
:   The button’s text if there is no `icon`, the `alt` text for the icon otherwise.

    > **Tip:**
    >
    > ```
    > <button type="object" name="action_create_new" string="Create document"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

icon
:   The icon to use to display the button. See [icons](icons.html#reference-user-interface-ui-icons) for
    the reference list.

    > **Tip:**
    >
    > ```
    > <button type="object" name="remove" icon="fa-trash"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

help
:   The tooltip message shown when hovering with the mouse cursor.

    > **Tip:**
    >
    > ```
    > <button type="object" name="remove" icon="fa-trash" help="Revoke"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

context
:   The context that is merged into the view’s context when performing the button’s call, as a Python
    expression that evaluates to a dict.

    > **Tip:**
    >
    > ```
    > <button name="button_confirm" type="object" context="{'BUSINESS_KEY': ANY}" string="LABEL"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `{}`

groups
:   The comma-separated list of user groups to whom the element is displayed. Users who do not belong
    to at least one of these groups are unable to see the element. Groups can be prefixed with the
    negative `!` operator to exclude them.

    > **Tip:**
    >
    > ```
    > <field name="FIELD_NAME" groups="base.group_no_one,!base.group_multi_company"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

invisible
:   Whether the element is visible (`False`) or hidden (`True`), as a Python expression that
    evaluates to a bool.

    > **Note:**
    >
    > There are two uses for the `invisible` attribute:
    >
    > - Usability: to avoid overloading the view and to make it easier for the user to read,
    >   depending on the content.
    > - Technical: a field must be present (invisible is enough) in the view to be used in a
    >   Python expression.

    > **Tip:**
    >
    > ```
    > <field name="fname_b" invisible="fname_c != 3 and fname_a == parent.fname_d"/>
    > <group invisible="fname_c != 4">
    >     <field name="fname_c"/>
    >     <field name="fname_d"/>
    > <group>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `False`

column\_invisible
:   Whether the column is visible (`False`) or hidden (`True`), as a Python expression that evaluates
    to a bool.

    Unlike `invisible`, it affects the entire column, and is evaluated without the subtree values.

    > **Tip:**
    >
    > ```
    > <field name="product_is_late" column_invisible="parent.has_late_products == False"/>
    > <button type="object" name="action_confirm" column_invisible="context.get('hide_confirm')"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `False`

class
:   The [HTML class](https://en.wikipedia.org/wiki/HTML_attribute) to set on the generated element.

    The styling uses the [Bootstrap](https://getbootstrap.com) framework and [UI icons](icons.html#reference-user-interface-ui-icons). Common Odoo classes include:

    - `oe_inline`: prevents the usual line break following fields, and limits their span;
    - `oe_left`, `oe_right`: [floats](https://developer.mozilla.org/en-US/docs/Web/CSS/float) the
      element to the corresponding direction;
    - `oe_read_only`, `oe_edit_only`: only displays the element in the corresponding form mode;
    - `oe_avatar`: for image fields, displays images as an “avatar” (max 90x90 square);
    - `oe_stat_button`: defines a particular rendering to dynamically display information while being
      clickable to target an action.

    > **Tip:**
    >
    > ```
    > <field name="fname" class="oe_inline oe_left oe_avatar"/>
    > ```

    > **Tip:**
    >
    > ```
    > <button type="object" name="ACTION" class="oe_stat_button" icon="FONT_AWESOME" help="HELP">
    >    <div class="o_field_widget o_stat_info">
    >       <span class="o_stat_value"><FIELD/></span>
    >       <span class="o_stat_text">TEXT</span>
    >    </div>
    > </button>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

> **Note:**
>
> |  |
> | --- |
> | ../../../_images/list_button.svg |
> | ``` <list>     <field name="name"/>     <button type="edit" name="edit" icon="fa-edit" title="Edit"/>     <button type="object" name="my_method" string="Button1" column_invisible="context.get('hide_button')" invisible="amount &gt; 3"/>     <field name="amount"/>     <field name="currency_id"/>     <field name="tax_id"/> </list> ``` |

#### `groupby`: define group headers

The `groupby` element is used to define group headers with [button] elements when grouping records on
[`Many2one`](../backend/orm.html#odoo.fields.Many2one "odoo.fields.Many2one") fields. It also accepts [field] elements, which can be used for modifiers. These fields
thus belong on the Many2one co-model. These extra fields are fetched in batch.

```
<list>
    ...
    <groupby name="FIELD_NAME">
        <BUTTONS/>
        <FIELDS/>
    </groupby>
</list>
```

The `groupby` element can have the following attributes:

name
:   The name of the a [`Many2one`](../backend/orm.html#odoo.fields.Many2one "odoo.fields.Many2one") field to use as header.

    A special [button] element with `type="edit"` can
    be defined to open the Many2one field’s form view.

    Requirement
    :   Mandatory

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

> **Note:**
>
> |  |
> | --- |
> | ../../../_images/list_groupby.svg |
> | ``` <list>     <field name="name"/>     <field name="amount"/>     <field name="currency"/>     <field name="tax_id"/>      <groupby name="partner_id">         <button type="edit" name="edit" icon="fa-edit" title="Edit"/>         <field name="email"/>         <button type="object" name="my_method" string="Button1" invisible="email == 'jhon@conor.com'"/>     </groupby> </list> ``` |

> **Note:**
>
> Fields inside the `groupby` element are used only to fetch and store the value, but they are
> never displayed.

#### `header`: display workflow buttons

```
<list>
    <header>
        <BUTTONS/>
    </header>
    ...
</list>
```

The `header` element accepts the following children elements:

button
:   The `button` element allows defining buttons in the control panel. It is the same element as the
    [button element in list views], but it accepts
    one more attribute when placed inside a `header` element:

    display
    :   Make the button available at all time, without having to select records.

        It accepts only the value `always`.

        > **Tip:**
        >
        > ```
        > <header>
        >     <button name="toDoAlways" type="object" string="Always displayed" display="always"/>
        >     <button name="toDoSelection" type="object" string="Displayed if selection"/>
        > </header>
        > ```

        Requirement
        :   Optional

        Type
        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

        Default
        :   `''`

> **Note:**
>
> |  |
> | --- |
> | ../../../_images/list_header.svg |
> | ``` <list>     <header>         <button type="object" name="to_draft" string="Button1" invisible="context.get('hide_button')"/>     </header>     <field name="name"/>     <field name="amount"/>     <field name="currency"/>     <field name="tax_id"/> </list> ``` |

#### `control`: customize create and delete actions

The `control` element allows to customize the create and delete actions. In particular, it allows
to add special create buttons with specific contexts, to use regular view buttons as create
actions, and to make the create and delete actions available only under certain conditions.

> **Warning:**
>
> The `control` element is only supported in list views inside [`One2many`](../backend/orm.html#odoo.fields.One2many "odoo.fields.One2many") or
> [`Many2many`](../backend/orm.html#odoo.fields.Many2many "odoo.fields.Many2many") fields.

```
<list>
   <control>
       <create string="LABEL"/>
       <BUTTONS/>
       <delete invisible="parent.is_sent">
    </control>
    ...
</list>
```

The `control` element takes no attributes. It accepts the following children elements:

create
:   The given `create` elements replace the default Add a line button.
    A `create` element can have the following attributes:

    string
    :   The button’s text.

        Requirement
        :   Mandatory

        Type
        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    context
    :   The context that is merged into the view’s context when performing the button’s call, as a Python
        expression that evaluates to a dict.

        Requirement
        :   Optional

        Type
        :   [Python expression]

        Default
        :   `{}`

    invisible
    :   Whether the element is visible (`False`) or hidden (`True`), as a Python expression that evaluates to a
        bool. The parent record and the context can be used in the expresion.

        Requirement
        :   Optional

        Type
        :   [Python expression]

        Default
        :   `False`

button
:   Like [regular view buttons]

delete
:   The `delete` element allows to conditionnaly hide the delete icon, row by row. There can only be
    one child of this type. It can have only one attribute:

    invisible
    :   Same as for `create`, except that in this case the record itself can also be used in the
        expresion.

> **Note:**
>
> |  |
> | --- |
> | ../../../_images/list_control.svg |
> | ``` <list>     <field name="name"/>     <field name="amount"/>     <field name="currency"/>     <field name="tax_id"/>     <control>         <create string="Add an item"/>         <create string="Add a section" context="{'default_type': 'section'}"/>         <create string="Add a note" context="{'default_type': 'note'}"/>     </control> </list> ``` |

## Search

Search views are different from other view types in that they are not used to display content.
Although they apply to a specific model, they are used to filter another view’s content (usually
aggregated views; e.g., [List] and
[Graph]).

The root element of search views is `search`.

It takes no attributes.

> **Note:**
>
> |  |
> | --- |
> | ../../../_images/search.svg |
> | ``` <search>     ... </search> ``` |

### Components

Search views accept the following children elements: [field], [filter], [separator], [group], and [searchpanel].

Placeholders are denoted in all caps.

#### `field`: filter based on field values

The `field` element defines domains or contexts with user-provided values. When search domains are
generated, field domains are joined with each other and with filters using the **AND** operator.

```
<search>
    <field name="FIELD_NAME"/>
</search>
```

The `field` element can have the following attributes:

name
:   The name of the field to filter on.

    Requirement
    :   Mandatory

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

string
:   The label of the field.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   The `string` attribute of the model’s field

operator
:   By default, fields generate domains of the form `[(name, {operator}, value)]`, where `name`
    is the field’s name and `value` is the value provided by the user, possibly filtered or
    transformed (e.g., a user is expected to provide the *label* of a selection field’s value, not
    the value itself).

    The `operator` attribute allows overriding the default operator, which depends on the field’s
    type (e.g., `=` for float fields, but `ilike` for char fields and `child_of` for many2one).

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `=`

filter\_domain
:   The domain to use as the field’s search domain, as a Python expression that evaluates to a
    [domain](../backend/orm.html#reference-orm-domains).

    It can use the `self` variable to inject the provided value in the custom domain. It can be used
    to generate significantly more flexible domains than with the `operator` attribute alone (e.g.,
    search on multiple fields at once).

    If both the `operator` and `filter_domain` attributes are provided, `filter_domain` takes
    precedence.

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `[]`

context
:   The context to merge into the context of the view that the search view is targeting, as a Python
    expression that evaluates to a dict.

    It can contain user-provided values, which are available under the `self` variable.

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `{}`

domain
:   The filters to apply to the completion results for fields that allow for auto-completion (e.g.,
    [`Many2one`](../backend/orm.html#odoo.fields.Many2one "odoo.fields.Many2one")).

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `[]`

groups
:   The comma-separated list of user groups to whom the element is displayed. Users who do not belong
    to at least one of these groups are unable to see the element. Groups can be prefixed with the
    negative `!` operator to exclude them.

    > **Tip:**
    >
    > ```
    > <field name="FIELD_NAME" groups="base.group_no_one,!base.group_multi_company"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

invisible
:   Whether the element is visible (`False`) or hidden (`True`), as a Python expression that
    evaluates to a bool.

    > **Note:**
    >
    > There are two uses for the `invisible` attribute:
    >
    > - Usability: to avoid overloading the view and to make it easier for the user to read,
    >   depending on the content.
    > - Technical: a field must be present (invisible is enough) in the view to be used in a
    >   Python expression.

    > **Tip:**
    >
    > ```
    > <field name="fname_b" invisible="fname_c != 3 and fname_a == parent.fname_d"/>
    > <group invisible="fname_c != 4">
    >     <field name="fname_c"/>
    >     <field name="fname_d"/>
    > <group>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `False`

> **Note:**
>
> |  |
> | --- |
> | ../../../_images/search_field.svg |
> | ``` <search>     <field name="name" string="My Custom Name"/>     <field name="amount"/>     <field name="currency_id"/>     <field name="ref" filter_domain="[('name', 'like', self)]"/> </search> ``` |

#### `filter`: create pre-defined filters

The `filter` element is used to create pre-defined filters that can be toggled in the search view.
It allows adding data to the search context the context passed to the data view for
searching/filtering, or appending new sections to the search filter.

```
<search>
    <filter string="LABEL" domain="DOMAIN"/>
</search>
```

The `filter` element can have the following attributes:

name
:   The technical name of the filter. It can be used to [enable it by default] or as an [inheritance hook](view_records.html#reference-view-records-inheritance).

    Requirement
    :   Mandatory

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

string
:   The label of the filter.

    Requirement
    :   Mandatory

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

help
:   The tooltip displayed when hovering the filter.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

domain
:   The domain to append to the action’s domain as part of the search domain.

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `[]`

date
:   The name of the `date` or `datetime` field to filter on.

    When used, this attribute creates a set of filters available in a sub-menu of the
    Filters menu. The available filters are time-dependent but not dynamic in the sense
    that their domains are evaluated at the time of the control panel instantiation.

    > **Tip:**
    >
    > ```
    > <filter string="Creation Date" name="filter_create_date" date="create_date"/>
    > ```

    By default, these filters contain a dropdown with different sub-filters that allow you to filter based on months, quarters and years.
    Additionally, you can create custom sub-filters that allow filtering using domains.
    These custom filters must have the following attributes: `name`, `string` and `domain`.

    > **Tip:**
    >
    > ```
    > <filter string="Creation Date" name="filter_create_date" date="create_date">
    >    <filter name="create_date_last_30_days" string="Last 30 Days" domain="[('create_date', '&gt;', datetime.datetime.combine(context_today() - relativedelta(days=30), datetime.time(23, 59, 59)).to_utc())]"/>
    > </filter>
    > ```

    Note that all custom filters defined this way are mutually exclusive with each other and with the other sub-filters.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

start\_month
:   The earliest month that will show up in the dropdown of a date filter, as an offset relative to the current month.

    > **Tip:**
    >
    > ```
    > <filter string="Creation Date" name="filter_create_date" date="create_date" start_month="-3"/>
    > ```
    >
    > If the current month is February, the earliest month selectable in the dropdown will be November.

    Requirement
    :   Optional

    Type
    :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")

    Default
    :   `-2`

    Scope
    :   Filters with a non-empty `date` attribute

end\_month
:   The latest month that will show up in the dropdown of a date filter, as an offset relative to the current month.

    > **Tip:**
    >
    > ```
    > <filter string="Creation Date" name="filter_create_date" date="create_date" end_month="2"/>
    > ```
    >
    > If the current month is February, the latest month selectable in the dropdown will be March.

    Requirement
    :   Optional

    Type
    :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")

    Default
    :   `0`

    Scope
    :   Filters with a non-empty `date` attribute

start\_year
:   The earliest year that will show up in the dropdown of a date filter, as an offset relative to the current year.

    > **Tip:**
    >
    > ```
    > <filter string="Creation Date" name="filter_create_date" date="create_date" start_year="-3"/>
    > ```
    >
    > If the current year is 2024, the earliest year selectable in the dropdown will be 2021.

    Requirement
    :   Optional

    Type
    :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")

    Default
    :   `-2`

    Scope
    :   Filters with a non-empty `date` attribute

end\_year
:   The latest year that will show up in the dropdown of a date filter, as an offset relative to the current year.

    > **Tip:**
    >
    > ```
    > <filter string="Creation Date" name="filter_create_date" date="create_date" end_year="2"/>
    > ```
    >
    > If the current year is 2024, the latest year selectable in the dropdown will be 2025.

    Requirement
    :   Optional

    Type
    :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")

    Default
    :   `0`

    Scope
    :   Filters with a non-empty `date` attribute

default\_period
:   The default period of the time-based filter (with a `date` attribute). It must be one of, or a
    comma-separated list of valid filter ids.

    Valid filter ids include the following:

    - `first_quarter`, `second_quarter`, `third_quarter` and `fourth_quarter`.
    - One of `month`, `month-x` and `month+x`, where `x` is a non-zero integer value between `start_month` and `end_month`.
    - One of `year`, `year-x` and `year+x`, where `x` is a non-zero integer value between `start_year` and `end_year`.
    - The `name` of any custom filter defined within the filter, prepended with `custom_`.

    The filter must be in the default set of filters activated at the view initialization.

    > **Tip:**
    >
    > ```
    > <filter string="Creation Date" name="filter_create_date" date="create_date" default_period="year,month-1"/>
    > ```

    > **Tip:**
    >
    > ```
    > <filter string="Creation Date" name="filter_create_date" date="create_date" default_period="custom_create_date_last_30_days">
    >    <filter name="create_date_last_30_days" string="Last 30 Days" domain="[('create_date', '&gt;', datetime.datetime.combine(context_today() - relativedelta(days=30), datetime.time(23, 59, 59)).to_utc())]"/>
    > </filter>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `month`, or the closest value to the current month if unavailable

    Scope
    :   Filters with a non-empty `date` attribute

invisible
:   Whether the element is visible (`False`) or hidden (`True`), as a Python expression that
    evaluates to a bool.

    > **Note:**
    >
    > There are two uses for the `invisible` attribute:
    >
    > - Usability: to avoid overloading the view and to make it easier for the user to read,
    >   depending on the content.
    > - Technical: a field must be present (invisible is enough) in the view to be used in a
    >   Python expression.

    > **Tip:**
    >
    > ```
    > <field name="fname_b" invisible="fname_c != 3 and fname_a == parent.fname_d"/>
    > <group invisible="fname_c != 4">
    >     <field name="fname_c"/>
    >     <field name="fname_d"/>
    > <group>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `False`

groups
:   The comma-separated list of user groups to whom the element is displayed. Users who do not belong
    to at least one of these groups are unable to see the element. Groups can be prefixed with the
    negative `!` operator to exclude them.

    > **Tip:**
    >
    > ```
    > <field name="FIELD_NAME" groups="base.group_no_one,!base.group_multi_company"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

context
:   The context merged into the action’s domain to generate the search domain

    The context key `group_by` set with a field as value can be used to define a group available in
    the Group By menu. When the field is of type `date` or `datetime`, the filter
    generates a submenu of the Group By menu with the following interval options
    available: Year, Quarter, Month, Week, and
    Day.

    > **Tip:**
    >
    > ```
    > <filter string="Category" name="groupby_category" context="{'group_by': 'category_id'}"/>
    > <filter string="Creation Date" name="groupby_create_date" context="{'group_by': 'create_date:week'}"/>
    > ```

    > **Note:**
    >
    > The results of `formatted_read_group` grouped on a field may be influenced by its `group_expand`
    > attribute, allowing to display empty groups when needed. For more information, please refer to
    > [`Field`](../backend/orm.html#odoo.fields.Field "odoo.fields.Field").

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `{}`

> **Warning:**
>
> Sequences of filters (without non-filters elements separating them) are treated as inclusively
> composited: they will be composed with `OR` rather than the usual `AND`.
>
> ```
> <filter domain="[('state', '=', 'draft')]"/>
> <filter domain="[('state', '=', 'done')]"/>
> ```
>
> Records whose `state` field is `draft` or `done` are shown.
>
> ```
> <filter domain="[('state', '=', 'draft')]"/>
> <separator/>
> <filter domain="[('delay', '&lt;', 15)]"/>
> ```
>
> Records whose `state` field is `draft` **and** `delay` field is below 15.

> **Note:**
>
> |  |
> | --- |
> | ../../../_images/search_filter.svg |
> | ``` <search>     <filter string="My Custom Name" domain="[('name', 'ilike', 'AAA')]"/>     <filter string="My orders" domain="[('user_id', '=', uid)]"/>     <filter string="Category" context="{'group_by': 'category_id'}"/> </search> ``` |

#### `separator`: separate groups of filters

The `separator` element is used to separates groups of [filters] in simple search views. For more complex search views,
the [group] element is recommended.

```
<search>
    <FILTERS/>
    <separator/>
    <FILTERS/>
</search>
```

The `separator` element takes no attributes.

#### `group`: separate groups of filters

The `group` element is used to separate groups of [filters] in cluttered search views. In simpler search views, it
can be substituted for the [separator] element.

```
<search>
    <group>
        <FILTERS/>
    </group>
</search>
```

The `group` element takes no attributes.

#### `searchpanel`: display search panels

The `searchpanel` element displays a search panel to the left of multi-records views. It allows for
quickly filtering data on the basis of given fields.

```
<search>
    <searchpanel>
        <FIELDS/>
    </searchpanel>
</search>
```

The `searchpanel` element accepts only `field` children elements.

The `field` element used as a child element of a `searchpanel` element can have the following
attributes:

name
:   The name of the field to filter on.

    Requirement
    :   Mandatory

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

string
:   The label of the field.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   The `string` attribute of the model’s field

select
:   The behavior and display of the field. It can have two different values:

    one
    :   At most one value can be selected. Supported field types are `many2one` and `selection`.

    multi
    :   Several values can be selected. Supported field types are `many2one`, `many2many` and
        `selection`.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `one`

groups
:   The comma-separated list of user groups to whom the element is displayed. Users who do not belong
    to at least one of these groups are unable to see the element. Groups can be prefixed with the
    negative `!` operator to exclude them.

    > **Tip:**
    >
    > ```
    > <field name="FIELD_NAME" groups="base.group_no_one,!base.group_multi_company"/>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

icon
:   The icon of the field.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

color
:   The color of the field.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

When the `field` element has the `select=one` attribute set, it can have the following additional
attributes:

hierarchize
:   Whether child categories should appear under their parent category, or at the same hierarchy
    level.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

    Scope
    :   [`Many2one`](../backend/orm.html#odoo.fields.Many2one "odoo.fields.Many2one") fields

depth
:   If set to a non zero integer, the hierarchy (if any) will be unfold up to the given level.

    Requirement
    :   Optional

    Type
    :   integer

    Default
    :   `0`

    Scope
    :   [`Many2one`](../backend/orm.html#odoo.fields.Many2one "odoo.fields.Many2one") fields

When the `field` element has the `select=multi` attribute set, it can have the following additional
attributes:

enable\_counters
:   Whether the record counters is computed and displayed if non-zero.

    > **Note:**
    >
    > This attribute exists to avoid impacting performance. Another way to address performance
    > issues is to override the `search_panel_select_range` and `search_panel_select_multi_range`
    > methods.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `False`

expand
:   Whether categories and filters with no records should be shown.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `False`

limit
:   The maximal number of values to fetch for the field. If the limit is reached, no values are
    displayed on the search panel, and an error message is shown instead. If set to 0, all values are
    fetched.

    Requirement
    :   Optional

    Type
    :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")

    Default
    :   `200`

domain
:   The conditions that the records have to satisfy.

    > **Tip:**
    >
    > ```
    > <searchpanel>
    >     <field name="department_id"/>
    >     <field name="manager_id" select="multi" domain="[('department_id', '=', department_id)]"/>
    > </searchpanel>
    > ```

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `[]`

groupby
:   The name of the field name on which values should be grouped.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

    Scope
    :   [`Many2one`](../backend/orm.html#odoo.fields.Many2one "odoo.fields.Many2one") and [`Many2many`](../backend/orm.html#odoo.fields.Many2many "odoo.fields.Many2many") fields

### Search defaults

Search fields and filters can be configured through the action’s `context` using
`search_default_{name}` keys. For fields, the value must be the value to set to the field. For
filters, it must be a boolean value or a number.

> **Tip:**
>
> With `foo`, a field, and `bar`, a filter, the following action context will search `foo` on
> `acro` and enable `bar` by default:
>
> ```
> {
>     'search_default_foo': 'acro',
>     'search_default_bar': 1
> }
> ```

A numeric value (between 1 and 99) can be used to define the order of default *groupby* filters.

> **Tip:**
>
> With `foo` and `bar`, two *groupby* filters, the following action context will first enable
> `bar`, then `foo`.
>
> ```
> {
>     'search_default_foo': 2,
>     'search_default_bar': 1
> }
> ```

## Kanban

Kanban views are used as a [kanban board](https://en.wikipedia.org/wiki/Kanban_board)
visualisation: they display records as “cards”, halfway between a [list] and a [form] view.

Records may be grouped in columns for use in workflow visualisation or manipulation (e.g., tasks or
work-progress management), or ungrouped (used simply to visualize records).

The root element of Kanban views is `kanban`.

> **Note:**
>
> |  |
> | --- |
> | ../../../_images/kanban.svg |
> | ``` <kanban>     ... </kanban> ``` |

> **Note:**
>
> Kanban views load and display a maximum of ten columns. Any column after that is closed but can
> still be opened by the user.

### Root attributes

Optional attributes can be added to the root element `kanban` to customize the view.

string
:   The view title. It is displayed only if you open an action that has no name and whose target is
    `new` (opening a dialog).

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

create
:   Disable/enable record creation on the view.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

edit
:   Disable/enable record edition on the view.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

delete
:   Disable/enable record deletion on the view through the Action dropdown.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

default\_group\_by
:   The name of the field on which the records should be grouped by default if no grouping is
    specified via the action or the current [search].

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

default\_order
:   A comma-separated list of fields names that overrides the ordering defined on the model through
    the [`_order`](../backend/orm.html#odoo.models.BaseModel._order "odoo.models.BaseModel._order") attribute.

    To inverse the sorting order of a field, postfix it with `desc`, separated by a space.

    > **Tip:**
    >
    > ```
    > <list default_order="sequence,name desc">
    >     ...
    > </list>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

class
:   Add HTML classes to the root HTML element of the view.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

examples
:   The key in the `KanbanExamplesRegistry` of the examples that can be browsed when creating a new
    column in the grouped kanban view.

    > **Note:**
    >
    > [Use of the examples attribute in the utm module](https://github.com/odoo/odoo/blob/19.0/addons/utm/static/src/js/utm_campaign_kanban_examples.js)

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

group\_create
:   Whether the Add a new column bar is visible.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

group\_delete
:   Whether columns can be deleted via the cog menu.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

group\_edit
:   Whether columns can be edited via the cog menu.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

groups\_draggable
:   Whether columns can be reordered.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

records\_draggable
:   Whether records can be dragged when the kanban view is grouped.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

archivable
:   Whether records belonging to a column can be archived and unarchived when the `active` field is
    defined on the model.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

quick\_create
:   Whether it should be possible to create records without switching to the form view.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True` when the kanban view is grouped by many2one, selection, char, or boolean fields,
        otherwise `False`

quick\_create\_view
:   The reference of the [form] view to open when using the
    quick creation of records.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

on\_create
:   The custom action to call when clicking on Create.

    If set to `'quick_create'`, the quick creation of records is used instead. If the quick creation
    is disabled, the standard create action is called.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

can\_open
:   By default, clicking on a kanban card opens the corresponding record in a form view.
    This behavior can be disabled by setting the attribute `can_open` to `False`.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

highlight\_color
:   Name of the integer field used to color the left border of the kanban cards.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

sample
:   Whether the view should be populated with a set of sample records if none are found for the
    current model.

    These fake records have heuristics for certain field names/models. For example, a field
    `display_name` on the model `res.users` will be populated with sample people names, while an
    `email` field will be in the form `firstname.lastname@sample.demo`.

    The user is unable to interact with these data, and they will be discarded as soon as an action
    is performed (record created, column added, etc.).

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `False`

### Components

Kanban views accept the following children elements: [templates], [field], [header], [progressbar].

#### `templates`: define cards structure

The `templates` element is used to define the [QWeb templates](../frontend/qweb.html#reference-qweb) that structure
the kanban cards.

The definition of a card’s structure can be split into multiple templates for clarity, but at least
one root `card` template must be defined.

An additional template can be defined: `menu`. If defined, it is rendered inside a dropdown
that can be toggled with a vertical ellipsis (⋮) on the top right of the card.

The templates are written in [JavaScript QWeb](../frontend/qweb.html#reference-qweb-javascript).

```
<kanban>
   <templates>
      <t t-name="card">
         <field name="name"/>
      </t>
   </templates>
</kanban>
```

> **Warning:**
>
> These are QWeb templates, not [Owl](https://github.com/odoo/owl) templates, meaning that
> directives like `t-on-click` aren’t available.

##### Fields

Inside those templates, the `field` element allows to render a field. It can have the following
attributes:

name
:   The name of the field to render.

    Requirement
    :   Mandatory

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

widget
:   The widget used to represent the field. The selected widget can change the way the field is
    rendered and/or the way it can be edited. It refers to a Javascript implementation (an Owl
    component) registered to the `fields` registry.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

By default, field nodes are replaced by a `span` containing their formatted value, unless the
`widget` attribute is specified, in which case their rendering and behavior depends on the
corresponding widget. The `widget` attribute can have different values including:

> handle
> :   Allows reordering records with a drag and drop, using the corresponding field as order.
>
> kanban\_color\_picker
> :   Allows editing a color (integer) field. Combined with the root attribute `highlight_color`,
>     allows editing the color of the cards.

See the [Field section](../frontend/javascript_reference.html#reference-js-widgets) to discover
various widgets and their options.

##### Rendering Context

Kanban templates being rendered with the [QWeb engine](../frontend/qweb.html#reference-qweb-javascript), they have
a *rendering context*, a set of variables available in the templates, containing useful information
and tools. Here’re the available variables:

record
:   An object with all the fields defined in the view. Each field has two attributes: `value`
    and `raw_value`. The former is formatted according to current user parameters, while the latter
    is the raw value (e.g. the `id` for a many2one field). This object is useful for instance, for
    using field values inside `t-if` conditions. For display purposes, we recommend using the
    `<field>` tag.

    > **Tip:**
    >
    > ```
    > <kanban>
    >    <templates>
    >       <field name="is_company"/>
    >       <t t-name="card">
    >          <field name="name"/>
    >          <field t-if="!record.is_company.raw_value" name="parent_id">
    >       </t>
    >    </templates>
    > </kanban>
    > ```

widget
:   An object with 2 keys defining the available actions for the user:

    - `editable`: true if the user can edit records, false otherwise;
    - `deletable`: true if the user can delete records, false otherwise.

    This is useful to conditionally display elements requiring specific access rights.

    > **Tip:**
    >
    > ```
    > <kanban>
    >    <templates>
    >       <t t-name="card">
    >          <field name="name"/>
    >       </t>
    >       <t t-name="menu">
    >          <a t-if="widget.deletable" role="menuitem" type="delete" class="dropdown-item">Delete</a>
    >       </t>
    >    </templates>
    > </kanban>
    > ```

context
:   The current context propagated from either the action that opens the kanban view, or the one2many
    or many2many field that embeds the kanban view in a form view.

read\_only\_mode
:   Indicates that the view is readonly.

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

selection\_mode
:   Whether the kanban view is opened when selecting a many2one or many2many field (in mobile
    environment).

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

luxon
:   The [luxon](https://moment.github.io/luxon/api-docs/index.html) object, allowing to
    manipulate date and datetime field values.

JSON
:   The Javascript [JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)
    namespace object containing a `parse` method allowing to parse json field values into Javascript
    Objects.

##### Buttons and links

While most of the kanban templates are standard [QWeb templates](../frontend/qweb.html#reference-qweb), the kanban
view processes `button` and `a` elements is a special way. Buttons and links with a `type` attribute
perform different operations than their standard HTML function. The `type` attribute can have the
values `action` and `object` of [regular buttons],
or the following values:

> open
> :   Clicking the element opens the card’s record in form view.
>
> delete
> :   Clicking the element deletes the card’s record and removes the card.
>
> archive
> :   Clicking the element archives the card’s record and removes the card.
>
> unarchive
> :   Clicking the element unarchives the card’s record and removes the card.
>
> set\_cover
> :   Clicking the element allows to select an image to set as cover image of the record.

##### Widgets

The `widget` element allows to insert dynamically generated (in Javascript) html inside the cards. It
has a mandatory `name` attribute, referring to a Javascript implementation (an Owl component)
registered to the `view_widgets` registry.

See the [Widget section](../frontend/javascript_reference.html#reference-javascript-reference-view-widgets) to discover various
widgets and their options.

##### Layouts

Several card layouts can be easily obtained using standard html elements and [Bootstrap utility
classes](https://getbootstrap.com/docs/5.0/utilities/api/). By default, the card is a [flexbox
container](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Basic_concepts_of_flexbox)
with `column` direction.

> **Tip:**
>
> ```
> <kanban>
>    <templates>
>       <t t-name="card">
>          <field class="fw-bold fs-5" name="display_name"/>
>          <field class="text-muted" name="parent_id"/>
>          <field name="tag_ids" widget="many2many_tags"/>
>       </t>
>    </templates>
> </kanban>
> ```

The `footer` html element is styled to stick to the bottom of the card, and is as a flexbox
container with `row` direction, allowing to easily display several fields on the same line.

> **Tip:**
>
> ```
> <kanban>
>    <templates>
>       <t t-name="card">
>          <field class="fw-bold fs-5" name="display_name"/>
>          <field class="text-muted" name="parent_id"/>
>          <field name="tag_ids" widget="many2many_tags"/>
>          <footer>
>             <field name="priority" widget="priority"/> <!-- bottom left corner -->
>             <field class="ms-auto" name="activity_ids" widget="kanban_activity"/> <!-- bottom right corner -->
>          </footer>
>       </t>
>    </templates>
> </kanban>
> ```

To display some content, like an image, on the side of the card, one can use `aside` and `main` html
elements, with the `flex-row` classname on the card. The `main` node is a flexbox container like the
card is when there’s no `aside`.

> **Tip:**
>
> ```
> <kanban>
>    <templates>
>       <t t-name="card" class="flex-row">
>          <aside>
>             <field name="avatar_128" widget="image" alt="Avatar"/>
>          </aside>
>          <main class="ms-2">
>             <field class="fw-bold fs-5" name="display_name"/>
>             <field class="text-muted" name="parent_id"/>
>             <field name="tag_ids" widget="many2many_tags"/>
>             <footer>
>                <field name="priority" widget="priority"/>
>                <field class="ms-auto" name="activity_ids" widget="kanban_activity"/>
>             </footer>
>          </main>
>       </t>
>    </templates>
> </kanban>
> ```

> **Note:**
>
> The classname `o_kanban_aside_full` set on the `aside` element removes the padding so that the
> image spreads to the borders of the card.

#### `field`: declare more fields to fetch

The `field` element can also be used *outside* the kanban [templates]. In that case, it allows to declare fields that are
not displayed in the card, but still need to be fetched, for instance because their value is used
in a `t-if` condition.

> **Tip:**
>
> ```
> <kanban>
>    <templates>
>       <field name="is_company"/>
>       <t t-name="card">
>          <field name="name"/>
>          <field t-if="!record.is_company.raw_value" name="parent_id">
>       </t>
>    </templates>
> </kanban>
> ```

#### `header`: display buttons in the control panel

The `header` element is used to insert custom buttons in the control panel.

```
<kanban>
   <header>
      ...
   </header>
   ...
</kanban>
```

The `header` element accepts only `button` children elements, similar to [list views’ button] elements.

The `button` element used as a child element of the `header` element can have the following
additional attributes:

display
:   The display mode of the button. It can have two different values:

    display
    :   The button is displayed only when some records are selected; their action applies to the
        selected records.

    always
    :   The button is displayed at all times, even if no records are selected.

    > **Warning:**
    >
    > Only the `always` display mode is available because it is not yet possible to select records
    > in a kanban view.

    > **Tip:**
    >
    > ```
    > <header>
    >     <button name="toDoAlways" type="object" string="Always displayed" display="always"/>
    >     <button name="toDoSelection" type="object" string="Displayed if selection"/>
    > </header>
    > ```

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `display`

#### `progressbar`: show progress bars on top of columns

The `progressbar` element is used to define a progress bar to display on top of kanban columns in
grouped kanban views.

```
<kanban>
    <progressbar field="FIELD_NAME"/>
    ...
</kanban>
```

The `progressbar` element can have the following attributes:

field
:   The name of the field on which the progress bar’s sub-groups
    are based.

    Requirement
    :   Mandatory

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

colors
:   The mapping of the progress bar’s field values to the color values `muted`, `success`, `warning`,
    and `danger`.

    Requirement
    :   Mandatory

    Type
    :   [JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)

sum\_field
:   The name of the field to use in a sum displayed next to the progress bar. If not set, the total
    number of records is displayed instead.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

> **Note:**
>
> |  |
> | --- |
> | ../../../_images/kanban_progressbar.svg |
> | ``` <kanban>     <progressbar field="activity_state"                  colors="{'planned': 'success', 'today': 'warning', 'overdue': 'danger'}"                  sum_field="expected_revenue"/>     <templates>         ...     </templates> </kanban> ``` |

#### `control`: customize create and delete actions

Like for [list views].

## QWeb

QWeb views are standard [QWeb Templates](../frontend/qweb.html#reference-qweb) templates inside a view’s
`arch`. They don’t have a specific root element. Because QWeb views don’t
have a specific root element, their type must be specified explicitly (it can
not be inferred from the root element of the `arch` field).

QWeb views have two use cases:

- they can be used as frontend templates, in which case
  [template](../backend/data.html#reference-data-template) should be used as a shortcut.
- they can be used as actual qweb views (opened inside an action), in which
  case they should be defined as regular view with an explicit `type` (it
  can not be inferred) and a model.

The main additions of qweb-as-view to the basic qweb-as-template are:

- qweb-as-view has a special case for a `<nav>` element bearing the CSS
  class `o_qweb_cp_buttons`: its contents should be buttons and will be
  extracted and moved to the control panel’s button area, the `<nav>` itself
  will be removed, this is a work-around to control panel views not existing
  yet
- qweb-as-view rendering adds several items to the standard qweb rendering
  context:

  `model`
  :   the model to which the qweb view is bound

  `domain`
  :   the domain provided by the search view

  `context`
  :   the context provided by the search view

  `records`
  :   a lazy proxy to `model.search(domain)`, this can be used if you just
      want to iterate the records and not perform more complex operations
      (e.g. grouping)
- qweb-as-view also provides additional rendering hooks:

  - `_qweb_prepare_context(view_id, domain)` prepares the rendering context
    specific to qweb-as-view
  - `qweb_render_view(view_id, domain)` is the method called by the client
    and will call the context-preparation methods and ultimately
    `env['ir.qweb'].render()`.

## Graph

The graph view is used to visualize aggregations over a number of records or
record groups. Its root element is `<graph>` which can take the following
attributes:

`type` (optional)
:   one of `bar` (default), `pie` and `line`, the type of graph to use

`stacked` (optional)
:   only used for `bar` charts. Set to `0` to prevent the bars within a group
    to be stacked initially.

`disable_linking` (optional)
:   set to `1` to prevent from redirecting clicks on graph to list view

`order` (optional)
:   if set, x-axis values will be sorted by default according their measure with
    respect to the given order (`asc` or `desc`). Only used for `bar` and
    `pie` charts.

`string` (optional)
:   string displayed in the breadcrumbs when redirecting to list view.

sample
:   Whether the view should be populated with a set of sample records if none are found for the
    current model.

    These fake records have heuristics for certain field names/models. For example, a field
    `display_name` on the model `res.users` will be populated with sample people names, while an
    `email` field will be in the form `firstname.lastname@sample.demo`.

    The user is unable to interact with these data, and they will be discarded as soon as an action
    is performed (record created, column added, etc.).

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `False`

The only allowed element within a graph view is `field` which can have the
following attributes:

`name` (mandatory)
:   the name of a field to use in the view. If used for grouping (rather
    than aggregating)

`invisible` (optional)
:   if true, the field will not appear either in the active measures nor in the
    selectable measures.

`type` (optional)
:   if set to `measure`, the field will be used as an aggregated value within a
    group instead of a grouping criteria. It only works for the last field
    with that attribute but it is useful for other fields with string attribute
    (see below).

`interval` (optional)
:   on date and datetime fields, groups by the specified interval (`day`,
    `week`, `month`, `quarter` or `year`) instead of grouping on the
    specific datetime (fixed second resolution) or date (fixed day resolution).
    Default is `month`.

`string` (optional)
:   only used for field with `type="measure"`. The name that will be used to
    display the field in the graph view, overrides the default python String
    attribute of the field.

The measures are automatically generated from the model fields; only the
aggregatable fields are used. Those measures are also alphabetically
sorted on the string of the field.

> **Warning:**
>
> graph view aggregations are performed on database content, non-stored
> function fields can not be used in graph views

In Graph views, a `field` can have a `widget` attribute to dictate its format.
The widget should be a field formatter, of which the most interesting are
`float_time`, and `monetary`.

```
<field name="working_hours_close" widget="float_time"/>
```

## Pivot

The pivot view is used to visualize aggregations as a [pivot table](https://en.wikipedia.org/wiki/Pivot_table). Its root
element is `<pivot>` which can take the following attributes:

`disable_linking` (optional)
:   Set to `1` to remove table cell’s links to list view.

`display_quantity` (optional)
:   Set to `1` to display the Quantity column by default.

`default_order` (optional)
:   The name of the measure and the order (asc or desc) to use as default order
    in the view.

    ```
    <pivot default_order="foo asc">
       <field name="foo" type="measure"/>
    </pivot>
    ```

The only allowed element within a pivot view is `field` which can have the
following attributes:

`name` (mandatory)
:   the name of a field to use in the view. If used for grouping (rather
    than aggregating)

`string` (optional)
:   the name that will be used to display the field in the pivot view,
    overrides the default python String attribute of the field.

`type` (optional)
:   indicates whether the field should be used as a grouping criteria or as an
    aggregated value within a group. Possible values are:

    `row` (default)
    :   groups by the specified field, each group gets its own row.

    `col`
    :   creates column-wise groups

    `measure`
    :   field to aggregate within a group

    `interval`
    :   on date and datetime fields, groups by the specified interval (`day`,
        `week`, `month`, `quarter` or `year`) instead of grouping on the
        specific datetime (fixed second resolution) or date (fixed day resolution).

`invisible` (optional)
:   if true, the field will not appear either in the active measures nor
    in the selectable measures (useful for fields that do not make sense aggregated,
    such as fields in different units, e.g. € and $).

sample
:   Whether the view should be populated with a set of sample records if none are found for the
    current model.

    These fake records have heuristics for certain field names/models. For example, a field
    `display_name` on the model `res.users` will be populated with sample people names, while an
    `email` field will be in the form `firstname.lastname@sample.demo`.

    The user is unable to interact with these data, and they will be discarded as soon as an action
    is performed (record created, column added, etc.).

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `False`

The measures are automatically generated from the model fields; only the
aggregatable fields are used. Those measures are also alphabetically
sorted on the string of the field.

> **Warning:**
>
> like the graph view, the pivot aggregates data on database content
> which means that non-stored function fields can not be used in pivot views

In Pivot view a `field` can have a `widget` attribute to dictate its format.
The widget should be a field formatter, of which the most interesting are
`date`, `datetime`, `float_time`, and `monetary`.

For instance a timesheet pivot view could be defined as:

```
<pivot string="Timesheet">
    <field name="employee_id" type="row"/>
    <field name="date" interval="month" type="col"/>
    <field name="unit_amount" type="measure" widget="float_time"/>
</pivot>
```

## Calendar

Calendar views display records as events in a daily, weekly, monthly or yearly
calendar.

> **Note:**
>
> By default the calendar view will be centered around the current date
> (today). You can pass a specific initial date to the context of the action in
> order to set the initial focus of the calendar on the period (see `mode`) around
> this date (the context key to use being `initial_date`)

Their root element is `<calendar>`. Available attributes on the root node are:

date\_start
:   Name of the record’s field holding the start date for the event.

    Requirement
    :   Mandatory

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

date\_stop
:   Name of the record’s field holding the end date for the event.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

date\_delay
:   Alternative to `date_stop`. Provides the duration of the event instead of
    its end date (unit: hour).

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

scales
:   Comma-separated list of available scales, among `day`, `week`, `month`,
    `year`. By default, all scales are available.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `"day,week,month,year"`

mode
:   Default scale of the calendar.

    Requirement
    :   Optional

    Type
    :   `"day"`, `"week"`, `"month"` or `"year"`

    Default
    :   `"week"`

color
:   Name of the record’s field to use for *color segmentation*. Records in the
    same color segment are allocated the same highlight color in the calendar.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

all\_day
:   Name of the record’s boolean field indicating whether the corresponding
    event is flagged as day-long, in which case duration is irrelevant.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

aggregate
:   Name of the record’s field to use to display aggregated values next to
    filters, in the filter side panel. The aggregator can be explicitly given
    (e.g. `aggregate="expected_revenue:sum"`). If not given, the aggregator of
    the field is used. Supported aggregators are `sum`, `avg`, `min`, `max`,
    `count` and `count_distinct`.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

event\_limit
:   Limits the number of events displayed in calendar cells, in `month` scale, and
    for all-day events in `week` and `day` scales. If there are more events than
    the limit, a “more” button is added to show the rest of the events in a popover.

    Requirement
    :   Optional

    Type
    :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")

    Default
    :   5

show\_unusual\_days
:   If set to true weekend days and public holidays have a greyed out background.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `False`

hide\_date
:   Set it to true to hide the date part in the record’s popover.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `False`

hide\_time
:   Set it to true to hide the time part in the record’s popover.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   False

month\_overflow
:   By default, in month mode, the last days of the previous month and the first
    days of the next months are displayed, as well as their events. This option
    allows to disable this such that those sibling days are greyed out and their
    events aren’t displayed.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

show\_date\_picker
:   By default, a mini calendar (in month mode) is displayed in the side panel,
    next to the main calendar. This option allows to remove it by setting it to
    `False`.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

event\_open\_popup
:   If true, open events in dialog to edit them, otherwise, open them in a
    classical form view.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `False`

form\_view\_id
:   View to open when the user creates or edits an event. By default, uses the
    form view of the current action, if any.

    Requirement
    :   Optional

    Type
    :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")

quick\_create
:   Enables quick event creation on click: only asks the user for a `name` and
    tries to create a new event with just that and the clicked event time. Falls
    back to a full form view if the quick creation fails.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

create\_name\_field
:   Name of the record’s field holding the display name of the record. This field
    is used when creating records through the ‘quick create’ mechanism.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `name`

quick\_create\_view\_id
:   Id of the form view to open when the attribute `quick_create` is set and the
    user creates an event, instead of the default dialog which only allows to
    specify a name.

    Requirement
    :   Optional

    Type
    :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")

multi\_create\_view
:   Reference of a form view. When set, in **month** scale, allows to create (and
    delete) records in batches by clicking on calendar cells or by selecting an
    area of calendar cells. One record is then created for each selected cell and
    for each active filter’s value, with the values of the multi create form view,
    which is displayed in the side panel. In delete mode, all records displayed
    in selected cells are deleted.

    Note: if the side panel contains multiple filter sections, only the first one
    is used, to avoid a combinatorial explosion.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

create
:   Disable/enable record creation on the view.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

edit
:   Disable/enable record edition on the view.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

delete
:   Disable/enable record deletion on the view.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `True`

string
:   The view title. It is displayed only if you open an action that has no name and whose target is
    `new` (opening a dialog).

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    Default
    :   `''`

### Components

Calendar views accept a single type of child elements: `<field>`. Those fields
are displayed in a popover, in the given order, which opens when a record
(a calendar event) is clicked.

> **Note:**
>
> Fields in the popover are readonly. If the `edit` action is available,
> an `Edit` button is displayed in the popover, to open a form view where fields
> can be edited.

Field nodes can have the following attributes:

name
:   The name of the field to render.

    Requirement
    :   Mandatory

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

widget
:   The widget used to represent the field. The selected widget can change the way the field is
    rendered and/or the way it can be edited. It refers to a Javascript implementation (an Owl
    component) registered to the `fields` registry.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

invisible
:   Python expression indicating whether the field should be displayed or not.
    Other fields of the model can be used in the expression, as long as those
    fields are also declared here.

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `False`

options
:   Python expression encoding an object of options for the field. In particular,
    the option `icon`, allowing to specify, as classnames, which icon to display
    in front of the field in the popover (for instance, `fa fa-users`). If no
    icon is given, the option `string` can be set, and its value is then used as
    label, displayed in front of the field.

    Requirement
    :   Optional

    Type
    :   [Python expression]

    Default
    :   `{}`

Specifying a `<field>` in a calendar arch also allows to customize the filter
side panel, by setting the `filters` attribute. Extra attributes are then
available for that matter:

filters
:   If set to true, the field can be used as filter, from the side panel of the
    calendar.

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `False`

avatar\_field
:   Only for relational fields. Specify the name of the field on the co-model to
    use to display as avatar in front of field values in the side panel filters.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

color
:   Specify which field to use to colorize the checkbox in the side panel filters.
    By default, the color attribute of the calendar view is used to match events
    with values in the filters.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

write\_model
:   Allows to create new filter values on the fly. The given model is then used
    as model for those filters. To combine with `write_field`.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

write\_field
:   Combined with `write_model`, specifies the field name, in the given model,
    to use to encode the filter value.

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

filter\_field
:   Combined with `write_model`, specifies the field name, in the given model,
    to use to encode the status of the filter (whether it is checked or not).

    Requirement
    :   Optional

    Type
    :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

## Activity

The Activity view is used to display the activities linked to the records. The
data are displayed in a chart with the records forming the rows and the activity
types the columns. The first cell of each row displays a (customizable, see
`templates`, quite similarly to [Kanban]) card representing
the corresponding record. When clicking on others cells, a detailed description
of all activities of the same type for the record is displayed.

> **Warning:**
>
> The Activity view is only available when the `mail` module is installed,
> and for the models that inherit from the `mail.activity.mixin`.

The root element of the Activity view is `<activity>`, it accepts the following
attributes:

`string` (mandatory)
:   A title, which should describe the view

Possible children of the view element are:

`field`
:   declares fields to use in activity *logic*. If the field is simply displayed
    in the activity view, it does not need to be pre-declared.

    Possible attributes are:

    `name` (required)
    :   the name of the field to fetch

`templates`
:   defines the [QWeb Templates](../frontend/qweb.html#reference-qweb) templates. Cards definition may be
    split into multiple templates for clarity, but activity views *must* define at
    least one root template `activity-box`, which will be rendered once for each
    record.

    The activity view uses mostly-standard [javascript qweb](../frontend/qweb.html#reference-qweb-javascript) and provides the following context variables
    (see [Kanban] for more details):

    `widget`
    :   the current `ActivityRecord()`, can be used to fetch some
        meta-information. These methods are also available directly in the
        template context and don’t need to be accessed via `widget`

    `record`
    :   an object with all the requested fields as its attributes. Each field has
        two attributes `value` and `raw_value`

## Cohort

Enterprise feature

The cohort view is used to display and understand the way some data changes over
a period of time. For example, imagine that for a given business, clients can
subscribe to some service. The cohort view can then display the total number
of subscriptions each month, and study the rate at which client leave the service
(churn). When clicking on a cell, the cohort view will redirect you to a new action
in which you will only see the records contained in the cell’s time interval;
this action contains a list view and a form view.

> **Note:**
>
> By default the cohort view will use the same list and form views as those
> defined on the action. You can pass a list view and a form view
> to the context of the action in order to set/override the views that will be
> used (the context keys to use being `form_view_id` and `list_view_id`)

For example, here is a very simple cohort view:

```
<cohort string="Subscription" date_start="date_start" date_stop="date" interval="month"/>
```

The root element of the Cohort view is <cohort>, it accepts the following
attributes:

`string` (mandatory)
:   A title, which should describe the view

`date_start` (mandatory)
:   A valid date or datetime field. This field is understood by the view as the
    beginning date of a record

`date_stop` (mandatory)
:   A valid date or datetime field. This field is understood by the view as the
    end date of a record. This is the field that will determine the churn.

`disable_linking` (optional)
:   Set to `1` to prevent from redirecting clicks on cohort cells to list view.

`mode` (optional)
:   A string to describe the mode. It should be either ‘churn’ or
    ‘retention’ (default). Churn mode will start at 0% and accumulate over time
    whereas retention will start at 100% and decrease over time.

`timeline` (optional)
:   A string to describe the timeline. It should be either ‘backward’ or ‘forward’ (default).
    Forward timeline will display data from date\_start to date\_stop, whereas backward timeline
    will display data from date\_stop to date\_start (when the date\_start is in future / greater
    than date\_stop).

`interval` (optional)
:   A string to describe a time interval. It should be ‘day’, ‘week’, ‘month’’
    (default) or ‘year’.

`measure` (optional)
:   A field that can be aggregated. This field will be used to compute the values
    for each cell. If not set, the cohort view will count the number of occurrences.

`<field>` (optional)
:   allows to specify a particular field in order to manage it from the available measures, it’s
    main use is for hiding a field from the selectable measures:

    `name` (mandatory)
    :   the name of the field to use in the view.

    `string` (optional)
    :   the name that would be used to display the field in the cohort view, overrides the
        default python String attribute of the field.

    `invisible` (optional)
    :   if true, the field will not appear either in the active measures nor in the selectable
        measures (useful for fields that do not make sense aggregated, such as fields in different
        units, e.g. € and $).
        If the value is a domain, the domain is evaluated in the context of the current row’s
        record, if `True` the corresponding attribute is set on the cell.

    `widget` (optional)
    :   alternate representations for a field’s display.

sample
:   Whether the view should be populated with a set of sample records if none are found for the
    current model.

    These fake records have heuristics for certain field names/models. For example, a field
    `display_name` on the model `res.users` will be populated with sample people names, while an
    `email` field will be in the form `firstname.lastname@sample.demo`.

    The user is unable to interact with these data, and they will be discarded as soon as an action
    is performed (record created, column added, etc.).

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `False`

## Grid

Enterprise feature

### Limitations

This view is a work in progress and may have to be expanded or altered.

- only `date` column fields have been tested, `selection` and `many2one`
  are nominally implemented and supported but have not been tested,
  `datetime` is not implemented at all.
- column cells are hardly configurable and must be numerical
- cell adjustment is disabled by default and must be configured to be enabled
- `create`, `edit` and `delete` ACL metadata doesn’t get automatically
  set on the view root due to limitations in `fields_view_get`
  post-processing (there’s a fixed explicit list of the view types getting
  those attributes)

### Schema

The grid view has its own schema and additional validation in this module. The
view architecture is:

`<grid>` (1)
:   architecture root element

    - mandatory `string` attribute
    - optional `create`, `edit` and `delete` attributes
    - optional `adjustment` and `adjust_name` attributes

      `adjustment` can be either `object` or `action` to indicate
      whether a cell’s adjustment should be performed through a method call
      or an action execution. `adjust_name` provides respectively the method
      name and the action id.

      In both cases, the adjustment parameters are provided as a
      `grid_adjust` context member, in the `object` case, the parameters
      are also provided as positional function parameters (next to an empty
      list of ids):

      `row_domain`
      :   the domain matching the entire row of the adjusted cell

      `column_field`
      :   the name of the column for the adjusted cell

      `column_value`
      :   the value of the column for the adjusted cell

      `cell_field`
      :   the measure field of the adjusted cell

      `change`
      :   the difference between the old value of the cell and the adjusted one,
          may be positive or negative
    - optional `hide_line_total` and `hide_column_total` attributes

      `hide_line_total`
      :   set to true to hide total line (default false)

      `hide_column_total`
      :   set to true to hide total column (default false)
    - optional `barchart_total` attribute

      `barchart_total`
      :   set to `true` in order to display a bar chart at the bottom of the grid, based on
          the totals of the columns (default false).
    - optional `create_inline` and `display_empty` attributes

      `create_inline`
      :   set to `true` in order to display an additional row at bottom of the grid with an
          `Add a line` button (default false). When this option is set to `true`, the `Add a line` button
          from the control panel is hidden. When no data is available and when `display_empty` is
          not set (so when the help content is displayed), the the `Add a line` button from the
          control panel is shown in order to let the user create a first record.

      `display_empty`
      :   set to `true` in order to keep displaying the grid when there is no data (default false). This can
          be useful when you want the user to be able to keep track of the current period (as dates
          are displayed in the columns headers). As a reminder, when no data are present and when this
          attribute is no set, the help content is displayed instead of the grid.

`<button>` (0+)
:   Regular Odoo action buttons, displayed in the view header

    - mandatory `string` attribute (the button label)
    - mandatory `type` attribute, either `object` or `action`

      > **Note:**
      >
      > workflow buttons are not supported
    - mandatory `name` attribute, either the name of the method to call, or
      the ID of the action to execute
    - optional `context`

    The server callback is provided with all the record ids displayed in the
    view, either as the ids passed to the method (`object` button) or as
    the context’s `active_ids` (`action` buttons)

`<field type="row">` (1+)
:   Row grouping fields, will be replaced by the search view’s groupby filter
    if any.

    The order of `row` fields in the view provides their grouping depth:
    if the first field is `school` and the second is `age` the records
    will be grouped by `school` first and by `age` within each school.

`<field type="col">` (1)
:   Column grouping field.

    The col field can contain 0+ `<range>` elements which specify
    customisable column ranges. `range` elements have the following
    mandatory attributes

    `name`
    :   can be used to override the default range (the first one by default)
        through the `grid_range` context value

    `string`
    :   the range button’s label (user-visible)

    `span`
    :   symbolic name of the span of all columns to display at once in the
        view, may trigger pagination.

        For `date` fields, valid spans are currently `week` and `month`.

    `step`
    :   symbolic name of the step between one column and the previous/next

        For `date` fields, the only valid span is currently `day`.

`<field type="measure">` (1)
:   Cell field, automatically accumulated (by `read_group`).

    The measure field can take a `widget` attribute to customise its
    display.

### Server interactions

Aside from optional buttons, the grid view currently calls two methods:

- `read_grid` (provided on all models by the module) returns almost the
  entirety of the grid’s content as a dict:

  - the row titles is a list of dictionaries with the following keys:

    `values` (required)
    :   this maps to a dictionary with a key per `row` field, the values are
        *always* of the form `[value, label]`.

    `domain` (required)
    :   the domain of any record at the source of this row, in case it’s
        necessary to copy a record during cell adjustment
  - the column titles is a list of dictionaries with at least one key:

    `values` (required)
    :   see row title values

    `domain` (required)
    :   see column domain value

    `current` (optional)
    :   boolean, marks/highlights a column
  - the grid data as a list (of rows) of list (of cells) of cell dicts each
    with the following keys:

    `value`
    :   the numeric value associated with the cell

    `domain`
    :   the domain matching the cell’s records (should be assumed opaque)

    `size`
    :   the number of records grouped in the cell

    `readonly` (optional)
    :   a boolean indicating that this specific cell should not be
        client-editable

    `classes` (optional)
    :   a list of classes (as strings) to add on the cell’s container (between
        the cell’s TD and the cell’s potentially-editable element).

        In case of conflicts between this list and the base classes (prefixed
        with `o_grid_cell_`), the classes in this list are ignored.

    Note that the grid data is *dense*, if querying the database yields no
    group matching a cell a cell will generate an “empty” cell with default
    values for required keys.
  - `prev` and `next` which can be either falsy (no pagination) or a
    context item to merge into the view’s own context to `read_grid` the
    previous or next page, it should be assumed to be opaque
- `read_grid_domain(field, range)` (provided on al models by the module)
  returns the domain matching the current configured “span” of the grid. This
  is also done internally by `read_grid`, but can be useful or necessary to
  call independently to use with separate e.g. `search_count` or
  `read_group`.
- `adjust_grid`, for which there currently isn’t a blanket implementation
  and whose semantics are likely to evolve with time and use cases

### Server Hooks

`read_grid` calls a number of hooks allowing the customisation of its
operations from within without having to override the entire method:

`_grid_format_cell(group, cell_field)`
:   converts the output of a read\_group (group-by-group) into cells in the
    format described above (as part of “the grid data”)

`_grid_make_empty_cell(row_domain, column_domain, view_domain)`
:   generates an empty version of a cell (if there is no corresponding group)

`_grid_column_info(name, range)`
:   generates a ColumnMetadata object based on the column type, storing values
    either returned directly (as part of `read_grid`) or used query and
    reformat `read_group` into `read_grid`:

    `grouping`
    :   the actual grouping field/query for the columns

    `domain`
    :   domain to apply to `read_group` in case the column field is
        paginated, can be an empty list

    `prev` and `next`
    :   context segments which will be sent to `read_grid` for pages before
        and after the current one. If `False`, disables pagination in that
        direction

    `values`
    :   column values to display on the “current page”, each value is a
        dictionary with the following keys:

        `values`
        :   dictionary mapping field names to values for the entire column,
            usually just `name` -> a value

        `domain`
        :   domain matching this specific column

        `is_current`
        :   `True` if the current column should be specifically outlined in
            the grid, `False` otherwise

        `format`
        :   how to format the values of that column/type from `read_group`
            formatting to `read_grid` formatting (matching `values` in
            ColumnInfo)

### ACL

- if the view is not editable, individual cells won’t be editable
- if the view is not creatable, the `Add a Line` button will not be
  displayed (it currently creates a new empty record)

### Context Keys

`grid_range`
:   selects which range should be used by default if the view has multiple
    ranges

`grid_anchor`
:   if applicable, used as the default anchor of column ranges instead of
    whatever `read_grid` defines as its default.

    For date fields, the reference date around which the initial span will be
    computed. The default date anchor is “today” (in the user’s timezone)

## Gantt

Enterprise feature

Gantt views appropriately display Gantt charts (for scheduling).

The root element of gantt views is `<gantt/>`, it has no children but can
take the following attributes:

string
:   string (default: `''`)

    This view title is displayed only if you open an action that has no name and
    whose target is ‘new’ (opening a dialog)

create
:   bool (default: `True`)

    Disable/enable record creation on the view.

edit
:   bool (default: `True`)

    Disable/enable record edition on the view.

delete
:   bool (default: `True`)

    Disable/enable record deletion on the view through the **Action** dropdown.

`date_start` (required)
:   name of the field providing the start datetime of the event for each
    record.

`date_stop` (required)
:   name of the field providing the end duration of the event for each
    record.

`dependency_field`
:   name of the `many2many` field that provides the dependency relation between two records.
    If B depends on A, `dependency_field` is the field that allows getting A
    from B. Both this field and `dependency_inverted_field` field are used to
    draw dependency arrows between pills and reschedule them.

`dependency_inverted_field` (required if `dependency_field` is provided)
:   name of the `many2many` field that provides the invert dependency relation than
    `dependency_field`. If B depends on A, `dependency_inverted_field` is
    the field that allows getting B from A.

`color`
:   name of the field used to color the pills according to its value

`decoration-{$name}`
:   [python expression](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not) that evaluates to a bool

    allow changing the style of a cell’s text based on the corresponding
    record’s attributes.

    `{$name}` can be one of the following [bootstrap contextual color](https://getbootstrap.com/docs/3.3/components/#available-variations) (`danger`,
    `info`, `secondary`, `success` or `warning`).

    Define a conditional display of a record in the style of a row’s text based on the corresponding
    record’s attributes.

    Values are Python expressions. For each record, the expression is evaluated
    with the record’s attributes as context values and if `true`, the
    corresponding style is applied to the row. Here are some of the other values
    available in the context:

    - `uid`: the id of the current user,
    - `today`: the current local date as a string of the form `YYYY-MM-DD`,
    - `now`: same as `today` with the addition of the current time.
      This value is formatted as `YYYY-MM-DD hh:mm:ss`.

    ```
    <gantt decoration-info="state == 'draft'"
          decoration-danger="state == 'help_needed'"
          decoration-bf="state == 'busy'">
      ...
    </gantt>
    ```

`default_group_by`
:   name of a field to group tasks by

`disable_drag_drop`
:   if set to true, the gantt view will not have any drag&drop support

`consolidation`
:   field name to display consolidation value in record cell

`consolidation_max`
:   dictionary with the “group by” field as key and the maximum consolidation
    value that can be reached before displaying the cell in red
    (e.g. `{"user_id": 100}`)

`consolidation_exclude`
:   name of the field that describes if the task has to be excluded
    from the consolidation
    if set to true it displays a striped zone in the consolidation line

`create`, `cell_create`, `edit`, `delete`, `plan`
:   allows *dis*abling the corresponding action in the view by setting the
    corresponding attribute to `false` (default: `true`).

    - `create`: If enabled, an `Add` button will be available in the control
      panel to create records.
    - `cell_create`: If enabled and `create` enabled, a “**+**” button will be
      displayed while hovering on a time slot cell to create a new record on that slot.
    - `edit`: If enabled, the opened records will be in edit mode (thus editable).
    - `plan`: If enabled and `edit` enabled, a “magnifying glass” button will be displayed
      on time slots to plan unassigned records into that time slot.

    > **Tip:**
    >
    > When you do not want to create records on the gantt view and the beginning and end
    > dates are required on the model, the planning feature should be disabled
    > because no record will ever be found.

`offset`
:   Depending on the scale, the number of units to add to today to compute the
    default period. Examples: An offset of +1 in default\_scale week will open the
    gantt view for next week, and an offset of -2 in default\_scale month will open
    the gantt view of 2 months ago.

`progress`
:   name of a field providing the completion percentage for the record’s event,
    between 0 and 100

`string`
:   title of the gantt view

`precision`
:   JSON object specifying snapping precisions for the pills in each scale.

    Possible values for scale `day` are (default: `hour`):

    - `hour`: records times snap to full hours (ex: 7:12 becomes 8:00)
    - `hour:half`: records times snap to half hours (ex: 7:12 becomes 7:30)
    - `hour:quarter`: records times snap to half hours (ex: 7:12 becomes 7:15)

    Possible values for scale `week` are (default: `day:half`):

    - `day`: records times snap to full days (ex: 7:28 AM becomes 11:59:59 PM of the previous day, 10:32 PM becomes 12:00 PM of the current day)
    - `day:half`: records times snap to half hours (ex: 7:28 AM becomes 12:00 PM)

    Possible values for scale `month` are (default: `day:half`):

    - `day`: records times snap to full days (ex: 7:28 AM becomes 11:59:59 PM of the previous day, 10:32 PM becomes 12:00 PM of the current day)
    - `day:half`: records times snap to half hours (ex: 7:28 AM becomes 12:00 PM)

    Scale `year` always snap to full day.

    Example of precision attribute: `{"day": "hour:quarter", "week": "day:half", "month": "day"}`

`total_row`
:   boolean to control whether the row containing the total count of records should
    be displayed. (default: `false`)

`collapse_first_level`
:   boolean to control whether it is possible to collapse each row if grouped by
    one field. (default: `false`, the collapse starts when grouping by two fields)

`display_unavailability`
:   boolean to mark the dates returned by the `gantt_unavailability` function of
    the model as available inside the gantt view. Records can still be scheduled
    in them, but their unavailability is visually displayed. (default: `false`)

`default_scale`
:   default scale when rendering the view. Possible values are (default: `month`):

    - `day`
    - `week`
    - `month`
    - `year`

`scales`
:   comma-separated list of allowed scales for this view. By default, all scales
    are allowed. For possible scale values to use in this list, see `default_scale`.

`templates`
:   defines the [QWeb Templates](../frontend/qweb.html#reference-qweb) template `gantt-popover` which is used
    when the user hovers over one of the records in the gantt view.

    The gantt view uses mostly-standard [javascript qweb](../frontend/qweb.html#reference-qweb-javascript) and provides the following context variables:

    `widget`
    :   the current `GanttRow()`, can be used to fetch some
        meta-information. The `getColor` method to convert in a color integer is
        also available directly in the template context without using `widget`.

    `on_create`
    :   If specified when clicking the add button on the view, instead of opening a generic dialog, launch a client action.
        this should hold the xmlid of the action (eg: `on_create="%(my_module.my_wizard)d"`

`form_view_id`
:   view to open when the user create or edit a record. Note that if this attribute
    is not set, the gantt view will fall back to the id of the form view in the
    current action, if any.

`dynamic_range`
:   if set to true, the gantt view will start at the first record,
    instead of starting at the beginning of the year/month/day.

`pill_label`
:   If set to true, the time appears in the pill label when the scale is set on week or month. (e.g.
    `7:00 AM - 11:00 AM (4h) - DST Task 1`)

`thumbnails`
:   This allows to display a thumbnail next to groups name if the group is a relationnal field.
    This expects a python dict which keys are the name of the field on the active model.
    Values are the names of the field holding the thumbnail on the related model.

    Example: tasks have a field user\_id that reference res.users. The res.users model has a field image that holds the avatar,
    then:

    ```
    <gantt
       date_start="date_start"
       date_stop="date_stop"
       thumbnails="{'user_id': 'image_128'}"
     >
     </gantt>
    ```

    will display the users avatars next to their names when grouped by user\_id.

sample
:   Whether the view should be populated with a set of sample records if none are found for the
    current model.

    These fake records have heuristics for certain field names/models. For example, a field
    `display_name` on the model `res.users` will be populated with sample people names, while an
    `email` field will be in the form `firstname.lastname@sample.demo`.

    The user is unable to interact with these data, and they will be discarded as soon as an action
    is performed (record created, column added, etc.).

    Requirement
    :   Optional

    Type
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    Default
    :   `False`

## Map

Enterprise feature

This view is able to display records on a map and the routes between them. The records are represented by pins. It also allows the visualization of fields from the model in a popup tied to the record’s pin.

> **Note:**
>
> The model on which the view is applied should contain a `res.partner` many2one since the view relies on the `res.partner`’s address and coordinates fields to localize the records.

### API

The view uses location data platforms’ API to fetch the tiles (the map’s background), do the geoforwarding (converting addresses to a set of coordinates) and fetch the routes.
The view implements two API, OpenStreetMap and MapBox. OpenStreetMap is used by default and is able to fetch [tiles](https://wiki.openstreetmap.org/wiki/Tile_data_server) and do [geoforwarding](https://nominatim.org/release-docs/develop/). This API does not require a token.
As soon as a valid [MapBox](https://docs.mapbox.com/api/) token is provided in the general settings the view switches to the MapBox API. This API is faster and allows the computation of routes. A token can be obtained by [signing up](https://account.mapbox.com/auth/signup/) to MapBox.

### Structural components

The view’s root element is `<map>`. It can have the following attributes:

`res_partner`
:   Contains the `res.partner` many2one. If not provided the view resorts to create an empty map.

`default_order`
:   If a field is provided the view overrides the model’s default order. The field must be part of the model on which the view is applied, not from `res.partner`.

`routing`
:   if `1` display the routes between the records. The view needs a valid MapBox token and at least two located records (i.e the records have a `res.partner` many2one and the partner has an address or valid coordinates).

`hide_name`
:   if `1` hide the name from the pin’s popup (default: `0`).

`hide_address`
:   if `1` hide the address from the pin’s popup (default: `0`).

`hide_title`
:   if `1` hide the title from the pin list (default: `0`).

`panel_title`
:   String to display as title of the pin list. If not provided, the title is the action’s name or “Items” if the view is not in an action.

`limit`
:   Maximum number of records to fetch (default: `80`). It must be a positive integer.

The `<map>` element can contain multiple `<field>` elements. Each `<field>` element is interpreted as a line in the pin’s popup. The field’s attributes are the following:

`name`
:   The field to display.

`string`
:   String to display before the field’s content. It can be used as a description.

For example here is a map:
:   ```
    <map res_partner="partner_id" default_order="date_begin" routing="1" hide_name="1">
        <field name="partner_id" string="Customer Name"/>
    </map>
    ```
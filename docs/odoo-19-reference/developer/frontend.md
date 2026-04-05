# Frontend — Owl Framework, Components & Hooks

> **Odoo 19.0 Reference**
> Source: www.odoo.com/documentation/19.0 — HTML converted via markdownify

## Purpose

Owl — Odoo's component framework. Covers components, props, state, hooks, lifecycle, slots, and the overall web client architecture. Use when building custom JavaScript components.

---

# Framework Overview

## Introduction

The Odoo Javascript framework is a set of features/building blocks provided by
the `web/` addon to help build odoo applications running in the browser. At
the same time, the Odoo Javascript framework is a single page application,
usually known as the *web client* (available at the url `/web`).

The web client started as an application made with a custom class and widget
system, but it is now transitioning to using native javascript classes instead,
and Owl as a component system. This explains why both systems are currently in
use in the codebase.

From a high-level perspective, the web client is a single-page application: it
does not need to request a full page from the server each time the user performs
an action. Instead, it only requests what it needs and then replaces/updates the
current screen accordingly. Also, it manages the url to keep it in sync with
the current state.

The javascript framework (all or some parts) is also used in other situations,
such as the Odoo website or the point of sale. This reference is mostly focused
on the web client.

> **Note:**
>
> It is common in the Odoo ecosystem to see the words *frontend* and *backend*
> as synonyms for the odoo website (public) and the web client, respectively.
> This terminology is not to be confused with the more common use of
> browser-code (frontend) and server (backend).

> **Note:**
>
> In this documentation, the word *component* always refers to new Owl
> components, and *widget* refers to old Odoo widgets.

> **Note:**
>
> All new development should be done in Owl, if possible!

## Code structure

The `web/static/src` folder contains all the `web/` javascript (and css and
templates) codebase. Here is a list of the most important folders:

- `core/` most of the low level features
- `fields/` all field components
- `views/` all javascript views components (`form`, `list`, …)
- `search/` control panel, search bar, search panel, …
- `webclient/` the web client specific code: navbar, user menu, action service, …

The `web/static/src` is the root folder. Everything inside can simply be
imported by using the `@web` prefix. For example, here is how one can import
the `memoize` function located in `web/static/src/core/utils/functions`:

```
import { memoize } from "@web/core/utils/functions";
```

## WebClient Architecture

As mentioned above, the web client is an owl application. Here is a slightly
simplified version of its template:

```
<t t-name="web.WebClient">
    <body class="o_web_client">
        <NavBar/>
        <ActionContainer/>
        <MainComponentsContainer/>
    </body>
</t>
```

As we can see, it basically is a wrapper for a navbar, the current action and
some additional components. The `ActionContainer` is a higher order component
that will display the current action controller (so, a client action, or a
specific view in the case of actions of type `act_window`). Managing actions
is a huge part of its work: the action service keeps in memory a stack of
all active actions (represented in the breadcrumbs), and coordinates each
change.

Another interesting thing to note is the `MainComponentsContainer`: it is
simply a component that displays all components registered in the
`main_components` registry. This is how other parts of the system can extend
the web client.

## Environment

As an Owl application, the Odoo web client defines its own environment (components
can access it using `this.env`). Here is a description of what Odoo adds to
the shared `env` object:

| Key | Value |
| --- | --- |
| `qweb` | required by Owl (contains all templates) |
| `bus` | [main bus], used to coordinate some generic events |
| `services` | all deployed [services](services.html#frontend-services) (should usually be accessed with the `useService` hook) |
| `debug` | string. If non empty, the web client is in [debug mode] |
| `_t` | translation function |
| `isSmall` | boolean. If true, the web client is currently in mobile mode (screen width <= 767px) |

So, for example, to translate a string in a component (note: templates are
automatically translated, so no specific action is required in that case), one
can do this:

```
const someString = this.env._t('some text');
```

> **Note:**
>
> Having a reference to the environment is quite powerful, because it provides
> access to all services. This is useful in many cases: for example,
> user menu items are mostly defined as a string, and a function taking the `env`
> as unique argument. This is enough to express all user menu needs.

## Building Blocks

Most of the web client is built with a few types of abstractions: registries,
services, components and hooks.

### Registries

[Registries](registries.html#frontend-registries) are basically a simple key/value mapping
that stores some specific kind of objects. They are an important part of the
extensibility of the UI: once some object is registered, the rest of the web
client can use it. For example, the field registry contains all field components
(or widgets) that can be used in views.

```
import { Component } from "@odoo/owl";
import { registry } from "./core/registry";

class MyFieldChar extends Component {
    // some code
}

registry.category("fields").add("my_field_char", MyFieldChar);
```

Note that we import the main registry from `@web/core/registry` then open the
sub registry `fields`.

### Services

[Services](services.html#frontend-services) are long lived pieces of code that provide a
feature. They may be imported by components (with `useService`) or by other
services. Also, they can declare a set of dependencies. In that sense, services
are basically a DI (dependency injection) system. For example, the `notification`
service provides a way to display a notification, or the `rpc` service is the
proper way to perform a request to the Odoo server.

The following example registers a simple service that displays a notification
every 5 second:

```
import { registry } from "./core/registry";

const serviceRegistry = registry.category("services");

const myService = {
    dependencies: ["notification"],
    start(env, { notification }) {
        let counter = 1;
        setInterval(() => {
            notification.add(`Tick Tock ${counter++}`);
        }, 5000);
    }
};

serviceRegistry.add("myService", myService);
```

### Components and Hooks

[Components](owl_components.html#frontend-components) and [hooks](hooks.html#frontend-hooks) are ideas coming from the
[Owl component system](https://github.com/odoo/owl/blob/master/doc/readme.md).
Odoo components are simply owl components that are part of the web client.

[Hooks](https://github.com/odoo/owl/blob/master/doc/reference/hooks.md) are a
way to factorize code, even if it depends on lifecycle. This is a
composable/functional way to inject a feature in a component. They can be seen
as a kind of mixin.

```
function useCurrentTime() {
    const state = useState({ now: new Date() });
    const update = () => state.now = new Date();
    let timer;
    onWillStart(() => timer = setInterval(update, 1000));
    onWillUnmount(() => clearInterval(timer));
    return state;
}
```

## Context

An important concept in the Odoo javascript is the *context*: it provides a way
for code to give more context to a function call or a rpc, so other parts of the
system can properly react to that information. In some way, it is like a bag of
information that is propagated everywhere. It is useful in some situations, such
as letting the Odoo server know that a model rpc comes from a specific form view,
or activating/disabling some features in a component.

There are two different contexts in the Odoo web client: the *user context* and
the *action context* (so, we should be careful when using the word *context*: it
could mean a different thing depending on the situation).

> **Note:**
>
> The `context` object may be useful in many cases, but one should be careful
> not to overuse it! Many problems can be solved in a standard way without
> modifying the context.

### User Context

The *user context* is a small object containing various informations related to
the current user. It is available through the `user` service:

```
class MyComponent extends Component {
    setup() {
        const user = useService("user");
        console.log(user.context);
    }
}
```

It contains the following information:

| Name | Type | Description |
| --- | --- | --- |
| `allowed_company_ids` | `number[]` | the list of active company ids for the user |
| `lang` | `string` | the user language code (such as “en\_us”) |
| `tz` | `string` | the user current timezone (for example “Europe/Brussels”) |

In practice, the `orm` service automatically adds the user context to each of
its requests. This is why it is usually not necessary to import it directly in
most cases.

> **Note:**
>
> The first element of the `allowed_company_ids` is the main company of the user.

### Action Context

The [ir.actions.act\_window](../backend/actions.html#reference-actions-window) and
[ir.actions.client](../backend/actions.html#reference-actions-client) support an optional `context` field.
This field is a `char` that represents an object. Whenever the corresponding
action is loaded in the web client, this context field will be evaluated as an
object and given to the component that corresponds to the action.

```
<field name="context">{'search_default_customer': 1}</field>
```

It can be used in many different ways. For example, the views add the
action context to every requests made to the server. Another important use is to
activate some search filter by default (see example above).

Sometimes, when we execute new actions manually (so, programmatically, in javascript),
it is useful to be able to extend the action context. This can be done with the
`additional_context` argument.

```
// in setup
let actionService = useService("action");

// in some event handler
actionService.doAction("addon_name.something", {
    additional_context:{
        default_period_id: defaultPeriodId
    }
});
```

In this example, the action with xml\_id `addon_name.something` will be loaded,
and its context will be extended with the `default_period_id` value. This is a
very important usecase that lets developers combine actions together by providing
some information to the next action.

## Python Interpreter

The Odoo framework features a built-in small python interpreter. Its purpose
is to evaluate small python expressions. This is important, because views in
Odoo have modifiers written in python, but they need to be evaluated by the
browser.

Example:

```
import { evaluateExpr } from "@web/core/py_js/py";

evaluateExpr("1 + 2*{'a': 1}.get('b', 54) + v", { v: 33 }); // returns 142
```

The `py` javascript code exports 5 functions:

tokenize(*expr*)
:   Arguments
    :   - **expr** (`string()`) – the expression to tokenize

    Returns
    :   Token[] a list of token

parse(*tokens*)
:   Arguments
    :   - **tokens** (`Token`) – a list of tokens

    Returns
    :   AST an abstract syntax tree structure representing the expression

parseExpr(*expr*)
:   Arguments
    :   - **expr** (`string()`) – a string representing a valid python expression

    Returns
    :   AST an abstract syntax tree structure representing the expression

evaluate(*ast*[, *context*])
:   Arguments
    :   - **ast** (`AST()`) – a AST structure that represents an expression
        - **context** (`Object()`) – an object that provides an additional evaluation context

    Returns
    :   any the resulting value of the expression, with respect to the context

evaluateExpr(*expr*[, *context*])
:   Arguments
    :   - **expr** (`string()`) – a string representing a valid python expression
        - **context** (`Object()`) – an object that provides an additional evaluation context

    Returns
    :   any the resulting value of the expression, with respect to the context

## Domains

Broadly speaking, domains in Odoo represent a set of records that matches some
specified conditions. In javascript, they are usually represented either as a
list of conditions (or of operators: `|`, `&` or `!` in prefix notation), or as string
expressions. They don’t have to be normalized (the `&` operator is implied if
necessary). For example:

```
// list of conditions
[]
[["a", "=", 3]]
[["a", "=", 1], ["b", "=", 2], ["c", "=", 3]]
["&", "&", ["a", "=", 1], ["b", "=", 2], ["c", "=", 3]]
["&", "!", ["a", "=", 1], "|", ["a", "=", 2], ["a", "=", 3]]

// string expressions
"[('some_file', '>', a)]"
"[('date','>=', (context_today() - datetime.timedelta(days=30)).strftime('%Y-%m-%d'))]"
"[('date', '!=', False)]"
```

String expressions are more powerful than list expressions: they can contain
python expressions and unevaluated values, that depends on some evaluation context.
However, manipulating string expressions is more difficult.

Since domains are quite important in the web client, Odoo provides a `Domain`
class:

```
new Domain([["a", "=", 3]]).contains({ a: 3 }) // true

const domain = new Domain(["&", "&", ["a", "=", 1], ["b", "=", 2], ["c", "=", 3]]);
domain.contains({ a: 1, b: 2, c: 3 }); // true
domain.contains({ a: -1, b: 2, c: 3 }); // false

// next expression returns ["|", ("a", "=", 1), ("b", "<=", 3)]
Domain.or([[["a", "=", 1]], "[('b', '<=', 3)]"]).toString();
```

Here is the `Domain` class description:

*class* Domain([*descr*])
:   Arguments
    :   - **descr** (`string | any[] | Domain()`) – a domain description

    Domain.contains(*record*)
    :   Arguments
        :   - **record** (`Object()`) – a record object

        Returns
        :   boolean

        Returns true if the record matches all the condition specified by the domain

    Domain.toString()
    :   Returns
        :   string

        Returns a string description for the domain

    Domain.toList([*context*])
    :   Arguments
        :   - **context** (`Object()`) – evaluation context

        Returns
        :   any[]

        Returns a list description for the domain. Note that this method takes an
        optional `context` object that will be used to replace all free variables.

        ```
        new Domain(`[('a', '>', b)]`).toList({ b:3 }); // [['a', '>', 3]]
        ```

The `Domain` class also provides 4 useful static methods to combine domains:

```
// ["&", ("a", "=", 1), ("uid", "<=", uid)]
Domain.and([[["a", "=", 1]], "[('uid', '<=', uid)]"]).toString();

// ["|", ("a", "=", 1), ("uid", "<=", uid)]
Domain.or([[["a", "=", 1]], "[('uid', '<=', uid)]"]).toString();

// ["!", ("a", "=", 1)]
Domain.not([["a", "=", 1]]).toString();

// ["&", ("a", "=", 1), ("uid", "<=", uid)]
Domain.combine([[["a", "=", 1]], "[('uid', '<=', uid)]"], "AND").toString();
```

*static* Domain.and(*domains*)
:   Parameters
    :   **domains** (*string**[**]* *|* *any**[**]**[**]* *|* *Domain**[**]*) – a list of domain representations

    Returns
    :   Domain

    Returns a domain representing the intersection of all domains.

*static* Domain.or(*domains*)
:   Parameters
    :   **domains** (*string**[**]* *|* *any**[**]**[**]* *|* *Domain**[**]*) – a list of domain representations

    Returns
    :   Domain

    Returns a domain representing the union of all domains.

*static* Domain.not(*domain*)
:   Parameters
    :   **domain** (*string* *|* *any**[**]* *|* *Domain*) – a domain representation

    Returns
    :   Domain

    Returns a domain representing the negation of the domain argument

*static* Domain.combine(*domains*, *operator*)
:   Parameters
    :   - **domains** (*string**[**]* *|* *any**[**]**[**]* *|* *Domain**[**]*) – a list of domain representations
        - **operator** (*'AND'* *or* *'OR'*) – an operator

    Returns
    :   Domain

    Returns a domain representing either the intersection or the union of all the
    domains, depending on the value of the operator argument.

## Bus

The web client [environment] object contains an event
bus, named `bus`. Its purpose is to allow various parts of the system to properly
coordinate themselves, without coupling them. The `env.bus` is an owl
[EventBus](https://github.com/odoo/owl/blob/master/doc/reference/event_bus.md),
that should be used for global events of interest.

```
// for example, in some service code:
env.bus.on("WEB_CLIENT_READY", null, doSomething);
```

Here is a list of the events that can be triggered on this bus:

| Message | Payload | Trigger |
| --- | --- | --- |
| `ACTION_MANAGER:UI-UPDATED` | a mode indicating what part of the ui has been updated (‘current’, ‘new’ or ‘fullscreen’) | the rendering of the action requested to the action manager is done |
| `ACTION_MANAGER:UPDATE` | next rendering info | the action manager has finished computing the next interface |
| `MENUS:APP-CHANGED` | none | the menu service’s current app has changed |
| `ROUTE_CHANGE` | none | the url hash was changed |
| `RPC:REQUEST` | rpc id | a rpc request has just started |
| `RPC:RESPONSE` | rpc id | a rpc request is completed |
| `WEB_CLIENT_READY` | none | the web client has been mounted |
| `FOCUS-VIEW` | none | the main view should focus itself |
| `CLEAR-CACHES` | none | all internal caches should be cleared |
| `CLEAR-UNCOMMITTED-CHANGES` | list of functions | all views with uncommitted changes should clear them, and push a callback in the list |

## Browser Object

The javascript framework also provides a special object `browser` that
provides access to many browser APIs, like `location`, `localStorage`
or `setTimeout`. For example, here is how one could use the
`browser.setTimeout` function:

```
import { browser } from "@web/core/browser/browser";

// somewhere in code
browser.setTimeout(someFunction, 1000);
```

It is mostly interesting for testing purposes: all code using the browser object
can be tested easily by mocking the relevant functions for the duration of the
test.

It contains the following content:

|  |  |  |
| --- | --- | --- |
| `addEventListener` | `cancelAnimationFrame` | `clearInterval` |
| `clearTimeout` | `console` | `Date` |
| `fetch` | `history` | `localStorage` |
| `location` | `navigator` | `open` |
| `random` | `removeEventListener` | `requestAnimationFrame` |
| `sessionStorage` | `setInterval` | `setTimeout` |
| `XMLHttpRequest` |  |  |

## Debug mode

Odoo can sometimes operate in a special mode called the `debug` mode. It is used
for two main purposes:

- display additional information/fields for some particular screens,
- provide some additional tools to help developer debug the Odoo interface.

The `debug` mode is described by a string. An empty string means that the `debug`
mode is not active. Otherwise, it is active. If the string contains `assets` or
`tests`, then the corresponding specific sub modes are activated (see below). Both
modes can be active at the same time, for example with the string `assets,tests`.

The `debug` mode current value can be read in the [environment]:
`env.debug`.

> **Note:**
>
> To show menus, fields or view elements only in debug mode, you should target
> the group `base.group_no_one`:
>
> ```
> <field name="fname" groups="base.group_no_one"/>
> ```

> **Note:**
>
> - [Activate the debug mode](../../../applications/general/developer_mode.html#developer-mode)

### Assets mode

The `debug=assets` sub mode is useful to debug javascript code: once activated,
the [assets](assets.html#reference-assets) bundles are no longer minified, and source-maps
are generated as well. This makes it useful to debug all kind of javascript code.

### Tests mode

There is another sub mode named `tests`: if enabled, the server injects the
bundle `web.assets_tests` in the page. This bundle contains mostly test tours
(tours whose purpose is to test a feature, not to show something interesting to
users). The `tests` mode is then useful to be able to run these tours.

> **Note:**
>
> - [Owl Repository](https://github.com/odoo/owl)

---

# Owl components

The Odoo Javascript framework uses a custom component framework called Owl. It
is a declarative component system, loosely inspired by Vue and React. Components
are defined using [QWeb templates](qweb.html), enriched with some Owl
specific directives. The official
[Owl documentation](https://github.com/odoo/owl/blob/master/doc/readme.md)
contains a complete reference and a tutorial.

> **Warning:**
>
> Although the code can be found in the `web` module, it is maintained from a
> separate GitHub repository. Any modification to Owl should therefore be made
> through a pull request on <https://github.com/odoo/owl>.

> **Note:**
>
> Currently, all Odoo versions (starting in version 14) share the same Owl version.

## Using Owl components

The [Owl documentation](https://github.com/odoo/owl/blob/master/doc/readme.md) already documents in detail the Owl framework, so this
page will only provide Odoo specific information. But first, let us see how we
can make a simple component in Odoo.

```
import { Component, xml, useState } from "@odoo/owl";

class MyComponent extends Component {
    static template = xml`
        <div t-on-click="increment">
            <t t-esc="state.value">
        </div>
    `;

    setup() {
        this.state = useState({ value: 1 });
    }

    increment() {
        this.state.value++;
    }
}
```

This example shows that Owl is available as a library in the global namespace as
`owl`: it can simply be used like most libraries in Odoo. Note that we
defined here the template as a static property, but without using the `static`
keyword, which is not available in some browsers (Odoo javascript code should
be Ecmascript 2019 compliant).

We define here the template in the javascript code, with the help of the `xml`
helper. However, it is only useful to get started. In practice, templates in
Odoo should be defined in an xml file, so they can be translated. In that case,
the component should only define the template name.

In practice, most components should define 2 or 3 files, located at the same
place: a javascript file (`my_component.js`), a template file (`my_component.xml`)
and optionally a scss (or css) file (`my_component.scss`). These files should
then be added to some assets bundle. The web framework will take care of
loading the javascript/css files, and loading the templates into Owl.

Here is how the component above should be defined:

```
import { Component, useState } from "@odoo/owl";

class MyComponent extends Component {
    static template = 'myaddon.MyComponent';

    ...
}
```

And the template is now located in the corresponding xml file:

```
<?xml version="1.0" encoding="UTF-8" ?>
<templates xml:space="preserve">

<t t-name="myaddon.MyComponent">
  <div t-on-click="increment">
    <t t-esc="state.value"/>
  </div>
</t>

</templates>
```

> **Note:**
>
> Template names should follow the convention `addon_name.ComponentName`.

> **Note:**
>
> - [Owl Repository](https://github.com/odoo/owl)

## Best practices

First of all, components are classes, so they have a constructor. But constructors
are special methods in javascript that are not overridable in any way. Since this
is an occasionally useful pattern in Odoo, we need to make sure that no component
in Odoo directly uses the constructor method. Instead, components should use the
`setup` method:

```
// correct:
class MyComponent extends Component {
    setup() {
        // initialize component here
    }
}

// incorrect. Do not do that!
class IncorrectComponent extends Component {
    constructor(parent, props) {
        // initialize component here
    }
}
```

Another good practice is to use a consistent convention for template names:
`addon_name.ComponentName`. This prevents name collision between odoo addons.

## Reference List

The Odoo web client is built with [Owl](https://github.com/odoo/owl) components.
To make it easier, the Odoo javascript framework provides a suite of generic
components that can be reused in some common situations, such as dropdowns,
checkboxes or datepickers. This page explains how to use these generic components.

| Technical Name | Short Description |
| --- | --- |
| [ActionSwiper] | a swiper component to perform actions on touch swipe |
| [CheckBox] | a simple checkbox component with a label next to it |
| [ColorList] | a list of colors to choose from |
| [Dropdown] | full-featured dropdown |
| [Notebook] | a component to navigate between pages using tabs |
| [Pager] | a small component to handle pagination |
| [SelectMenu] | a dropdown component to choose between different options |
| [TagsList] | a list of tags displayed in rounded pills |

### ActionSwiper

#### Location

`@web/core/action_swiper/action_swiper`

#### Description

This is a component that can perform actions when an element is swiped
horizontally. The swiper is wrapping a target element to add actions to it.
The action is executed once the user has released the swiper passed
a portion of its width.

```
<ActionSwiper onLeftSwipe="Object" onRightSwipe="Object">
  <SomeElement/>
</ActionSwiper>
```

The simplest way to use the component is to use it around your target element directly
in an xml template as shown above. But sometimes, you may want to extend an existing element
and would not want to duplicate the template. It is possible to do just that.

If you want to extend the behavior of an existing element, you must place the element
inside, by wrapping it directly. Also, you can conditionnally add props to manage when the
element might be swipable, its animation and the minimum portion to swipe to perform the action.

You can use the component to interact easily with records, messages, items in lists and much more.

![Example of ActionSwiper usage](../../../_images/actionswiper.png)

The following example creates a basic ActionSwiper component.
Here, the swipe is enabled in both directions.

```
<ActionSwiper
  onRightSwipe="
    {
      action: '() => Delete item',
      icon: 'fa-delete',
      bgColor: 'bg-danger',
    }"
  onLeftSwipe="
    {
      action: '() => Star item',
      icon: 'fa-star',
      bgColor: 'bg-warning',
    }"
>
  <div>
    Swipable item
  </div>
</ActionSwiper>
```

> **Note:**
>
> Actions are permuted when using right-to-left (RTL) languages.

#### Props

| Name | Type | Description |
| --- | --- | --- |
| `animationOnMove` | `Boolean` | optional boolean to determine if a translate effect is present during the swipe |
| `animationType` | `String` | optional animation that is used after the swipe ends (`bounce` or `forwards`) |
| `onLeftSwipe` | `Object` | if present, the actionswiper can be swiped to the left |
| `onRightSwipe` | `Object` | if present, the actionswiper can be swiped to the right |
| `swipeDistanceRatio` | `Number` | optional minimum width ratio that must be swiped to perform the action |

You can use both `onLeftSwipe` and `onRightSwipe` props at the same time.

The `Object`’s used for the left/right swipe must contain:

> - `action`, which is the callable `Function` serving as a callback.
>   Once the swipe has been completed in the given direction, that action
>   is performed.
> - `icon` is the icon class to use, usually to represent the action.
>   It must be a `string`.
> - `bgColor` is the background color, given to decorate the action.
>   can be one of the following [bootstrap contextual color](https://getbootstrap.com/docs/3.3/components/#available-variations) (`danger`,
>   `info`, `secondary`, `success` or `warning`).
>
> Those values must be given to define the behavior and the visual aspect
> of the swiper.

#### Example: Extending existing components

In the following example, you can use `xpath`’s to wrap an existing element
in the ActionSwiper component. Here, a swiper has been added to mark
a message as read in mail.

```
<xpath expr="//*[hasclass('o_Message')]" position="after">
  <ActionSwiper
    onRightSwipe="messaging.device.isMobile and messageView.message.isNeedaction ?
      {
        action: () => messageView.message.markAsRead(),
        icon: 'fa-check-circle',
        bgColor: 'bg-success',
      } : undefined"
  />
</xpath>
<xpath expr="//ActionSwiper" position="inside">
  <xpath expr="//*[hasclass('o_Message')]" position="move"/>
</xpath>
```

### CheckBox

#### Location

`@web/core/checkbox/checkbox`

#### Description

This is a simple checkbox component with a label next to it. The checkbox is
linked to the label: the checkbox is toggled whenever the label is clicked.

```
<CheckBox value="boolean" disabled="boolean" t-on-change="onValueChange">
  Some Text
</CheckBox>
```

#### Props

| Name | Type | Description |
| --- | --- | --- |
| `value` | `boolean` | if true, the checkbox is checked, otherwise it is unchecked |
| `disabled` | `boolean` | if true, the checkbox is disabled, otherwise it is enabled |

### ColorList

#### Location

`@web/core/colorlist/colorlist`

#### Description

The ColorList let you choose a color from a predefined list. By default, the component displays the current
selected color, and is not expandable until the `canToggle` props is present. Different props can change its
behavior, to always expand the list, or make it act as a toggler once it is clicked, to display the list of
available colors until a choice is selected.

#### Props

| Name | Type | Description |
| --- | --- | --- |
| `canToggle` | `boolean` | optional. Whether the colorlist can expand the list on click |
| `colors` | `array` | list of colors to display in the component. Each color has a unique `id` |
| `forceExpanded` | `boolean` | optional. If true, the list is always expanded |
| `isExpanded` | `boolean` | optional. If true, the list is expanded by default |
| `onColorSelected` | `function` | callback executed once a color is selected |
| `selectedColor` | `number` | optional. The color `id` that is selected |

Color `id`’s are the following:

| Id | Color |
| --- | --- |
| `0` | `No color` |
| `1` | `Red` |
| `2` | `Orange` |
| `3` | `Yellow` |
| `4` | `Light blue` |
| `5` | `Dark purple` |
| `6` | `Salmon pink` |
| `7` | `Medium blue` |
| `8` | `Dark blue` |
| `9` | `Fuchsia` |
| `12` | `Green` |
| `11` | `Purple` |

### Dropdown

#### Location

`@web/core/dropdown/dropdown` and `@web/core/dropdown/dropdown_item`

#### Description

The Dropdown lets you show a menu with a list of items when a toggle is
clicked on. They can be combined with DropdownItems to invoke callbacks
and close the menu when items are selected.

Dropdowns are surprisingly complicated components, the list of features they
provide is as follow:

- Toggle the item list on click
- Close on outside click
- Call a function when items are selected
- Optionally close the item list when an item is selected
- SIY: style it yourself
- Support sub dropdowns, up to any level
- Configurable hotkey to open/close a dropdown or select a dropdown item
- Keyboard navigation (arrows, tab, shift+tab, home, end, enter and escape)
- Reposition itself whenever the page scrolls or is resized
- Smartly chose the direction it should open (right-to-left direction is automatically handled).
- Direct siblings dropdowns: when one is open, toggle others on hover

To properly use a `<Dropdown/>` component, you need to populate two
[OWL slots](https://github.com/odoo/owl/blob/master/doc/reference/slots.md) :

- `default` slot: it contains the *toggle* elements of your dropdown. By default, click events will
  be attached to this element to open and close the dropdown.
- `content` slot: it contains the *elements* of the dropdown menu itself and is rendered inside a popover.
  Although it is not mandatory, you can put some `DropdownItem` inside this slot, the dropdown will
  automatically close when these items are selected.

```
<Dropdown>
  <!-- The content of the "default" slot is the component's toggle -->
  <button class="my-btn" type="button">
    Click me to toggle the dropdown menu!
  </button>

  <!-- The "content" slot is rendered inside the menu that pops up next to the toggle -->
  <t t-set-slot="content">
    <DropdownItem onSelected="selectItem1">Menu Item 1</DropdownItem>
    <DropdownItem onSelected="selectItem2">Menu Item 2</DropdownItem>
  </t>
</Dropdown>
```

#### Dropdown Props

| Name | Type | Description |
| --- | --- | --- |
| `menuClass` | `String` | Optional classname added to the dropdown’s menu |
| `disabled` | `Boolean` | Optional, if true, disables the dropdown so the user is not able to open it anymore. (default: `false`) |
| `items` | `Array` | Optional list of items to be displayed as DropdownItems inside the dropdown’s menu |
| `position` | `String` | Optionally defines the desired menu opening position. RTL direction is automatically applied. Should be a valid [usePosition](hooks.html#frontend-hooks-useposition) hook position. (default: `bottom-start`) |
| `beforeOpen` | `Function` | Optional function called just before opening. May be asynchronous. |
| `onOpened` | `Function` | Optional function called just after opening. |
| `onStateChanged` | `Function` | Optional function called after opening or closing (gives a boolean as single argument that represents whether the dropdown is open or not). |
| `state` | `Object` | Optional object with `open()`, `close()` and `isOpen` properties to manually control when the dropdown opens and closes. |
| `manual` | `Boolean` | Optional, when true, the Dropdown component will not add click event listeners to the toggler. This allows for more control as when to open the dropdown. (This should be used in tandem with the `state` prop) |
| `navigationOptions` | `Boolean` | Optionally overrides the navigation options of the dropdown, (see `web/core/navigation/navigation`). |
| `holdOnHover` | `Boolean` | Optional, if true, keeps the Dropdown’s menu at the same position while the mouse is hovering it, creating a better UX when the menu’s content changes. |
| `menuRef` | `Function` | Optional, allows to get a ref of the dropdown’s menu, (expects a function returned from `useChildRef`) |

#### DropdownItem Props

| Name | Type | Description |
| --- | --- | --- |
| `class` | `String` or `Object` | Optional value added to the root span classname (supports both strings and [OWL classname object notation](https://github.com/odoo/owl/blob/master/doc/reference/templates.md#dynamic-class-attribute)). |
| `onSelected` | `Function` | Optional function called when the dropdown item is selected. |
| `closingMode` | `"none"` | `"closest"` | `"all"` | Optional, controls which parent dropdown should close when the item is selected: `none`: the dropdown will not close, `closest`: the direct parent will close, `all`: every nested parent dropdown will close (default: `all`) |
| `attrs` | `Object` | Optional object representing attributes that are added to the root element. `<DropdownItem attrs="{ title: 'A tooltip', 'data-hotkey': 'shift+a' }">`. (If `href` is set, the element will automatically become an `a` element). |

> **Warning:**
>
> When writing custom css for you components, do not forget that the menu elements are not next to the toggle
> but inside the overlay container, at the bottom of the document. Thus, use the `menuClass` and `class` props to more
> easily write your selectors. (This DOM magic let us avoid lots of z-index issues.)

#### Nested Dropdown

Dropdown can be nested, to do this simply put new Dropdown components inside other dropdown’s content slot. When the parent
dropdown is open, child dropdowns will open automatically on hover.

By default, selecting a DropdownItem will close the whole Dropdown tree.

> **Tip:**
>
> This example shows how one could make a nested File dropdown menu, with submenus for the New sub elements.
>
> ```
> <Dropdown>
>   <button>File</button>
>   <t t-set-slot="content">
>     <DropdownItem onSelected="() => this.onItemSelected('file-save')">Save</DropdownItem>
>     <DropdownItem onSelected="() => this.onItemSelected('file-open')">Open</DropdownItem>
>
>     <Dropdown>
>       <button>New</button>
>       <t t-set-slot="content">
>         <DropdownItem onSelected="() => this.onItemSelected('file-new-document')">Document</DropdownItem>
>         <DropdownItem onSelected="() => this.onItemSelected('file-new-spreadsheet')">Spreadsheet</DropdownItem>
>       </t>
>     </Dropdown>
>   </t>
> </Dropdown>
> ```
>
> In the example bellow, we recursively call a template to display a tree-like structure.
>
> ```
> <t t-name="addon.MainTemplate">
>   <div>
>     <t t-call="addon.RecursiveDropdown">
>       <t t-set="name" t-value="'Main Menu'" />
>       <t t-set="items" t-value="state.menuItems" />
>     </t>
>   </div>
> </t>
>
> <t t-name="addon.RecursiveDropdown">
>   <Dropdown>
>     <button t-esc="name"></button>
>     <t t-set-slot="content">
>       <t t-foreach="items" t-as="item" t-key="item.id">
>
>         <!-- If this item has no child: make it a <DropdownItem/> -->
>         <DropdownItem t-if="!item.childrenTree.length" onSelected="() => this.onItemSelected(item)" t-esc="item.name"/>
>
>         <!-- Else: recursively call the current dropdown template. -->
>         <t t-else="" t-call="addon.RecursiveDropdown">
>           <t t-set="name" t-value="item.name" />
>           <t t-set="items" t-value="item.childrenTree" />
>         </t>
>       </t>
>     </t>
>   </Dropdown>
> </t>
> ```

#### Controlled Dropdown

If needed, you can also open or close the dropdown using code. To do this you must use the `useDropdownState` hook along
with the `state` prop. `useDropdownState` returns an object that has an `open` and a `close` method (as well as an `isOpen` getter).
Give the object to the `state` prop of the dropdown you want to control and calling the respective functions should now open and
close your dropdown.

You can also set `manual` to `true` if you don’t want the default click handlers to be added on the toggle.

> **Tip:**
>
> The following example shows a dropdown that opens automatically when mounted and only has a 50% chance
> of closing when clicking on the button inside.
>
> ```
> import { Component, onMounted } from "@odoo/owl";
> import { Dropdown } from "@web/core/dropdown/dropdown";
> import { DropdownItem } from "@web/core/dropdown/dropdown_item";
> import { useDropdownState } from "@web/core/dropdown/dropdown_hooks";
>
> class MyComponent extends Component {
>
>   static components = { Dropdown, DropdownItem };
>   static template = xml`
>     <Dropdown state="this.dropdown">
>       <div>My Dropdown</div>
>
>       <t t-set-slot="content">
>         <button t-on-click="() => this.mightClose()">Close It!<button>
>       </t>
>     </Dropdown>
>   `;
>
>   setup() {
>     this.dropdown = useDropdownState();
>
>     onMounted(() => {
>       this.dropdown.open();
>     });
>   }
>
>   mightClose() {
>     if (Math.random() > 0.5) {
>       this.dropdown.close();
>     }
>   }
> }
> ```

#### DropdownGroup

**Location:** `@web/core/dropdown/dropdown_group`

You can use the DropdownGroup component to make Dropdowns share a common group, this means that when
one of these Dropdown is open, the others will automatically open themselves on mouse hover, without
the need for a click.

To do this, either surround all the Dropdowns with a single DropdownGroup or surround them with
DropdownGroups with the same `group` key.

> **Tip:**
>
> In the example bellow, all dropdown in the snippet bellow will share the same group:
>
> ```
> <DropdownGroup>
>   <Dropdown>...</Dropdown>
>   <Dropdown>...</Dropdown>
>   <Dropdown>...</Dropdown>
> </DropdownGroup>
> ```
>
> Whereas in the following snippet, only the first, second and fourth dropdown share the same group:
>
> ```
> <DropdownGroup group="'my-group'">
>   <Dropdown>...</Dropdown>
>   <Dropdown>...</Dropdown>
> </DropdownGroup>
>
> <DropdownGroup group="'my-other-group'">
>   <Dropdown>...</Dropdown>
> </DropdownGroup>
>
> <DropdownGroup group="'my-group'">
>   <Dropdown>...</Dropdown>
> </DropdownGroup>
> ```

### Notebook

#### Location

`@web/core/notebook/notebook`

#### Description

The Notebook is made to display multiple pages in a tabbed interface. Tabs can be located
at the top of the element to display horizontally, or at the left for a vertical layout.

There are two ways to define your Notebook pages to instanciate, either by using `slot`’s,
or by passing a dedicated `props`.

A page can be disabled with the `isDisabled` attribute, set directly on the slot node, or
in the page declaration, if the Notebook is used with the `pages` given as props. Once disabled,
the corresponding tab is greyed out and set as inactive as well.

#### Props

| Name | Type | Description |
| --- | --- | --- |
| `anchors` | `object` | optional. Allow anchors navigation to elements inside tabs that are not visible. |
| `className` | `string` | optional. Classname set on the root of the component. |
| `defaultPage` | `string` | optional. Page `id` to display by default. |
| `icons` | `array` | optional. List of icons used in the tabs. |
| `orientation` | `string` | optional. Whether tabs direction is `horizontal` or `vertical`. |
| `onPageUpdate` | `function` | optional. Callback executed once the page has changed. |
| `pages` | `array` | optional. Contain the list of `page`’s to populate from a template. |

> **Tip:**
> > The first approach is to set the pages in the slots of the component.
> >
> > ```
> > <Notebook orientation="'vertical'">
> >   <t t-set-slot="page_1" title="'Page 1'" isVisible="true">
> >     <h1>My First Page</h1>
> >     <p>It's time to build Owl components. Did you read the documentation?</p>
> >   </t>
> >   <t t-set-slot="page_2" title="'2nd page'" isVisible="true">
> >     <p>Wise owl's silent flight. Through the moonlit forest deep, guides my path to code</p>
> >   </t>
> > </Notebook>
> > ```
> >
> > The other way to define your pages is by passing the props. This can be useful if some pages share
> > the same structure. Create first a component for each page template that you may use.
> >
> > ```
> > import { Component, xml } from "@odoo/owl";
> > import { Notebook } from "@web/core/notebook/notebook";
> >
> > class MyTemplateComponent extends Component {
> >   static template = xml`
> >     <h1 t-esc="props.title" />
> >     <p t-esc="props.text" />
> >   `;
> > }
> >
> > class MyComponent extends Component {
> >   static template = xml`
> >     <Notebook defaultPage="'page_2'" pages="pages" />
> >   `;
> >
> >   get pages() {
> >     return [
> >       {
> >         Component: MyTemplateComponent,
> >         title: "Page 1",
> >         props: {
> >           title: "My First Page",
> >           text: "This page is not visible",
> >         },
> >       },
> >       {
> >         Component: MyTemplateComponent,
> >         id: "page_2",
> >         title: "Page 2",
> >         props: {
> >           title: "My second page",
> >           text: "You're at the right place!",
> >         },
> >       },
> >     ]
> >   }
> > }
> > ```
>
> Both examples are shown here:
>
> ![Examples with vertical and horizontal layout](../../../_images/notebook1.png)

### Pager

#### Location

`@web/core/pager/pager`

#### Description

The Pager is a small component to handle pagination. A page is defined by an `offset` and a `limit` (the size of the page). It displays the current page and the `total` number of elements, for instance, “9-12 / 20”. In the previous example, `offset` is 8, `limit` is 4 and `total` is 20. It has two buttons (“Previous” and “Next”) to navigate between pages.

> **Note:**
>
> The pager can be used anywhere but its main use is in the control panel. See the [usePager](hooks.html#frontend-hooks-usepager) hook in order to manipulate the pager of the control panel.

```
<Pager offset="0" limit="80" total="50" onUpdate="doSomething" />
```

#### Props

| Name | Type | Description |
| --- | --- | --- |
| `offset` | `number` | Index of the first element of the page. It starts with 0 but the pager displays `offset + 1`. |
| `limit` | `number` | Size of the page. The sum of `offset` and `limit` corresponds to the index of the last element of the page. |
| `total` | `number` | Total number of elements the page can reach. |
| `onUpdate` | `function` | Function that is called when page is modified by the pager. This function can be async, the pager cannot be edited while this function is executing. |
| `isEditable` | `boolean` | Allows to click on the current page to edit it (`true` by default). |
| `withAccessKey` | `boolean` | Binds access key `p` on the previous page button and `n` on the next page one (`true` by default). |

### SelectMenu

#### Location

`@web/core/select_menu/select_menu`

#### Description

This component can be used when you want to do more than using the native `select` element. You can define your own option template, allowing to search
between your options, or group them in subsections.

> **Note:**
>
> Prefer the native HTML `select` element, as it provides by default accessibility features, and has a better user interface on mobile devices.
> This component is designed to be used for more complex use cases, to overcome limitations of the native element.

#### Props

| Name | Type | Description |
| --- | --- | --- |
| `choices` | `array` | optional. List of `choice`’s to display in the dropdown. |
| `class` | `string` | optional. Classname set on the root of the SelectMenu component. |
| `groups` | `array` | optional. List of `group`’s, containing `choices` to display in the dropdown. |
| `multiSelect` | `boolean` | optional. Enable multiple selections. When multiple selection is enabled, selected values are displayed as [tag]’s in the SelectMenu input. |
| `togglerClass` | `string` | optional. classname set on the toggler button. |
| `required` | `boolean` | optional. Whether the selected value can be unselected. |
| `searchable` | `boolean` | optional. Whether a search box is visible in the dropdown. |
| `searchPlaceholder` | `string` | optional. Text displayed as the search box placeholder. |
| `value` | `any` | optional. Current selected value. It can be from any kind of type. |
| `onSelect` | `function` | optional. Callback executed when an option is chosen. |

The shape of a `choice` is the following:

> - `value` is actual value of the choice. It is usually a technical string, but can be from `any` type.
> - `label` is the displayed text associated with the option. This one is usually a more friendly and translated `string`.

The shape of a `group` is the following:

> - `choices` is the list of `choice`’s to display for this group.
> - `label` is the displayed text associated with the group. This is a `string` displayed at the top of the group.

> **Tip:**
>
> In the following example, the SelectMenu will display four choices. One of them is displayed on top of the options,
> since no groups are associated with it, but the other ones are separated by the label of their group.
>
> ```
> import { Component, xml } from "@odoo/owl";
> import { SelectMenu } from "@web/core/select_menu/select_menu";
>
> class MyComponent extends Component {
>   static template = xml`
>     <SelectMenu
>       choices="choices"
>       groups="groups"
>       value="'value_2'"
>     />
>   `;
>
>   get choices() {
>     return [
>         {
>           value: "value_1",
>           label: "First value"
>         }
>     ]
>   }
>   get groups() {
>     return [
>       {
>           label: "Group A",
>           choices: [
>               {
>                 value: "value_2",
>                 label: "Second value"
>               },
>               {
>                 value: "value_3",
>                 label: "Third value"
>               }
>           ]
>       },
>       {
>           label: "Group B",
>           choices: [
>               {
>                 value: "value_4",
>                 label: "Fourth value"
>               }
>           ]
>       }
>     ]
>   }
> }
> ```
>
> You can also customize the appearance of the toggler and set a custom template for the choices, using the appropriate component `slot`’s.
>
> ```
> <SelectMenu
>   choices="choices"
>   groups="groups"
>   value="'value_2'"
> >
>   Make a choice!
>   <t t-set-slot="choice" t-slot-scope="choice">
>     <span class="coolClass" t-esc="'👉 ' + choice.data.label + ' 👈'" />
>   </t>
> </SelectMenu>
> ```
>
> ![Example of SelectMenu usage and customization](../../../_images/select_menu.png)
>
> When SelectMenu is used with multiple selection, the `value` props must be an `Array` containing the values of the selected choices.
>
> ![Example of SelectMenu used with multiple selection](../../../_images/select_menu_multiSelect.png)
>
> For more advanced use cases, you can customize the bottom area of the dropdown, using the `bottomArea` slot. Here, we choose to display
> a button with the corresponding value set in the search input.
>
> ```
> <SelectMenu
>     choices="choices"
> >
>     <span class="select_menu_test">Select something</span>
>     <t t-set-slot="bottomArea" t-slot-scope="select">
>         <div t-if="select.data.searchValue">
>             <button class="btn text-primary" t-on-click="() => this.onCreate(select.data.searchValue)">
>                 Create this article "<i t-esc="select.data.searchValue" />"
>             </button>
>         </div>
>     </t>
> </SelectMenu>
> ```
>
> ![Example of SelectMenu's bottom area customization](../../../_images/select_menu_bottomArea.png)

### TagsList

#### Location

`@web/core/tags_list/tags_list`

#### Description

This component can display a list of tags in rounded pills. Those tags can either simply list a few values, or can be editable, allowing the removal of items.
It can be possible to limit the number of displayed items using the `itemsVisible` props. If the list is longer than this limit, the number of additional items is
shown in a circle next to the last tag.

#### Props

| Name | Type | Description |
| --- | --- | --- |
| `displayBadge` | `boolean` | optional. Whether the tag is displayed as a badge. |
| `displayText` | `boolean` | optional. Whether the tag is displayed with a text or not. |
| `itemsVisible` | `number` | optional. Limit of visible tags in the list. |
| `tags` | `array` | list of `tag`’s elements given to the component. |

The shape of a `tag` is the following:

> - `colorIndex` is an optional color id.
> - `icon` is an optional icon displayed just before the displayed text.
> - `id` is a unique identifier for the tag.
> - `img` is an optional image displayed in a circle, just before the displayed text.
> - `onClick` is an optional callback that can be given to the element. This allows the parent element to handle any functionality depending on the tag clicked.
> - `onDelete` is an optional callback that can be given to the element. This makes the removal of the item from the list of tags possible, and must be handled by the parent element.
> - `text` is the displayed `string` associated with the tag.

> **Tip:**
>
> In the next example, a TagsList component is used to display multiple tags.
> It’s at the developer to handle from the parent what would happen when the tag is pressed, or when the delete button is clicked.
>
> ```
> import { Component, xml } from "@odoo/owl";
> import { TagsList } from "@web/core/tags_list/tags_list";
>
> class Parent extends Component {
>   static template = xml`<TagsList tags="tags" />`;
>   static components = { TagsList };
>
>   setup() {
>     this.tags = [{
>         id: "tag1",
>         text: "Earth"
>     }, {
>         colorIndex: 1,
>         id: "tag2",
>         text: "Wind",
>         onDelete: () => {...}
>     }, {
>         colorIndex: 2,
>         id: "tag3",
>         text: "Fire",
>         onClick: () => {...},
>         onDelete: () => {...}
>     }];
>   }
> }
> ```
>
> Depending the attributes given to each tag, their appearance and behavior will differ.
>
> ![Examples of TagsList using different props and attributes](../../../_images/tags_list.png)

---

# Hooks

[Owl hooks](https://github.com/odoo/owl/blob/master/doc/reference/hooks.md) are a
way to factorize code, even if it depends on some component lifecycle. Most hooks
provided by Owl are related to the lifecycle of a component, but some of them (such as
[useComponent](https://github.com/odoo/owl/blob/master/doc/reference/hooks.md#usecomponent))
provide a way to build specific hooks.

Using these hooks, it is possible to build many customized hooks that help solve
a specific problem, or make some common tasks easier. The rest of this page
documents the list of hooks provided by the Odoo web framework.

| Name | Short Description |
| --- | --- |
| [useAssets] | load assets |
| [useAutofocus] | focus automatically an element referenced by autofocus |
| [useBus] | subscribe and unsubscribe to a bus |
| [usePager] | Display the pager of the control panel of a view. |
| [usePosition] | position an element relative to a target |
| [useSpellCheck] | activate spellcheck on focus for input or textarea |

## useAssets

### Location

`@web/core/assets`

### Description

See the section on [lazy loading assets](assets.html#frontend-assets-lazy-loading) for
more details.

## useAutofocus

### Location

`@web/core/utils/hooks`

### Description

Focus an element referenced by a t-ref=”autofocus” in the current component as
soon as it appears in the DOM and if it was not displayed before.

```
import { useAutofocus } from "@web/core/utils/hooks";

class Comp {
  setup() {
    this.inputRef = useAutofocus();
  }
  static template = "Comp";
}
```

```
<t t-name="Comp">
  <input t-ref="autofocus" type="text"/>
</t>
```

### API

useAutofocus()
:   Returns
    :   the element reference.

## useBus

### Location

`@web/core/utils/hooks`

### Description

Add and clear an event listener to a bus. This hook ensures that
the listener is properly cleared when the component is unmounted.

```
import { useBus } from "@web/core/utils/hooks";

class MyComponent {
  setup() {
    useBus(this.env.bus, "some-event", event => {
      console.log(event);
    });
  }
}
```

### API

useBus(*bus*, *eventName*, *callback*)
:   Arguments
    :   - **bus** (`EventBus()`) – the target event bus
        - **eventName** (`string()`) – the name of the event that we want to listen to
        - **callback** (`function()`) – listener callback

## usePager

### Location

`@web/search/pager_hook`

### Description

Display the [Pager](owl_components.html#frontend-pager) of the control panel of a view. This hooks correctly sets `env.config` to provide the props to the pager.

```
import { usePager } from "@web/search/pager_hook";

class CustomView {
  setup() {
    const state = owl.hooks.useState({
      offset: 0,
      limit: 80,
      total: 50,
    });
    usePager(() => {
      return {
        offset: this.state.offset,
        limit: this.state.limit,
        total: this.state.total,
        onUpdate: (newState) => {
          Object.assign(this.state, newState);
        },
      };
    });
  }
}
```

### API

usePager(*getPagerProps*)
:   Arguments
    :   - **getPagerProps** (`function()`) – function that returns the pager props.

## usePosition

### Location

`@web/core/position_hook`

### Description

Helps positioning an HTMLElement (the `popper`) relatively to another
HTMLElement (the `reference`). This hook ensures the positioning is updated when
the window is resized/scrolled.

```
import { usePosition } from "@web/core/position_hook";
import { Component, xml } from "@odoo/owl";

class MyPopover extends Component {
  static template = xml`
    <div t-ref="popper">
      I am positioned through a wonderful hook!
    </div>
  `;

  setup() {
    // Here, the reference is the target props, which is an HTMLElement
    usePosition(this.props.target);
  }
}
```

> **Warning:**
>
> You should indicate your `popper` element using a [t-ref directive](https://github.com/odoo/owl/blob/master/doc/reference/hooks.md#useref).

### API

usePosition(*reference*[, *options*])
:   Arguments
    :   - **reference** (`HTMLElement or ()=>HTMLElement()`) – the target HTMLElement to be positioned from
        - **options** (`Options()`) – the positioning options (see table below)

| Option | Type | Description |
| --- | --- | --- |
| `popper` | string | this is a [useRef reference](https://github.com/odoo/owl/blob/master/doc/reference/hooks.md#useref) for the element that will get positioned. Default is `"popper"`. |
| `container` | HTMLElement | the container from which the popper is expected not to overflow. If overflowing occurs, other popper positions are tried until a not overflowing one is found. (default: the `<html/>` node) |
| `margin` | number | added margin between popper and reference elements (default: `0`) |
| `position` | Direction[-Variant] | the desired position. It is a string composed of one `Direction` and one `Variant` separated by a dash character. `Direction` could be: `top`, `bottom`, `right`, `left`. `Variant` could be: `start`, `middle`, `end`, `fit`. The variant can be omitted (default variant is `middle`). The `fit` variant means that the popper would have the exact same width or height, depending on the chosen direction. Examples of valid positions: `right-end`, `top-start`, `left-middle`, `left`, `bottom-fit`. (default position: `bottom`) |
| `onPositioned` | (el: HTMLElement, position: PositioningSolution) => void | a callback that will be called everytime a positioning occurs (e.g. on component mounted/patched, document scroll, window resize…). Can be used i.e. for dynamic styling regarding the current position. The `PositioningSolution` is an object having the following type: `{ direction: Direction, variant: Variant, top: number, left: number }`. |

> **Tip:**
>
> ```
> import { Component, xml, useRef } from "@odoo/owl";
> import { usePosition } from "@web/core/position_hook";
>
> class DropMenu extends Component {
>   static template = xml`
>     <button t-ref="toggler">Toggle Menu</button>
>     <div t-ref="menu">
>       <t t-slot="default">
>         This is the menu default content.
>       </t>
>     </div>
>   `;
>
>   setup() {
>     const toggler = useRef("toggler");
>     usePosition(
>       () => toggler.el,
>       {
>         popper: "menu",
>         position: "right-start",
>         onPositioned: (el, { direction, variant }) => {
>           el.classList.add(`dm-${direction}`); // -> "dm-top" "dm-right" "dm-bottom" "dm-left"
>           el.style.backgroundColor = variant === "middle" ? "red" : "blue";
>         },
>       },
>     );
>   }
> }
> ```

## useSpellCheck

### Location

`@web/core/utils/hooks`

### Description

Activate the spellcheck state to an input or textarea on focus by a `t-ref="spellcheck"` in
the current component. This state is then removed on blur, as well as the red outline, which
improves readability of the content.

The hook can also be used on any HTML element with the `contenteditable` attribute. To disable
spellcheck completely on elements that might be enabled by the hook, set explicitly the
`spellcheck` attribute as `false` on the element.

> **Tip:**
>
> In the following example, the spellcheck will be enabled on the first input, the textarea and
> the div with `contenteditable="true"`.
>
> ```
> import { useSpellCheck } from "@web/core/utils/hooks";
>
> class Comp {
>   setup() {
>     this.simpleRef = useSpellCheck();
>     this.customRef = useSpellCheck({ refName: "custom" });
>     this.nodeRef = useSpellCheck({ refName: "container" });
>   }
>   static template = "Comp";
> }
> ```
>
> ```
> <t t-name="Comp">
>   <input t-ref="spellcheck" type="text"/>
>   <textarea t-ref="custom"/>
>   <div t-ref="container">
>     <input type="text" spellcheck="false"/>
>     <div contenteditable="true"/>
>   </div>
> </t>
> ```

### API

useSpellCheck([*options*])
:   Arguments
    :   - **options** (`Options()`) – the spellcheck options (see table below)

| Option | Type | Description |
| --- | --- | --- |
| `refName` | string | this is a [useRef reference](https://github.com/odoo/owl/blob/master/doc/reference/hooks.md#useref) for the element that will be spellcheck enabled. |
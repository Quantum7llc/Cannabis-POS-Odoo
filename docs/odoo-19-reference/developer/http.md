# HTTP — Controllers, Routing & RPC

> **Odoo 19.0 Reference**
> Source: www.odoo.com/documentation/19.0 — HTML converted via markdownify

## Purpose

Web controllers and routing for HTTP endpoints, JSON-RPC, and file downloads. Covers @route, request/response objects, authentication, and CORS. Use when exposing custom URLs or API endpoints.

---

# Web Controllers

## Controllers

Controllers need to provide extensibility, much like
[`Model`](orm.html#odoo.models.Model "odoo.models.Model"), but can’t use the same mechanism as the
pre-requisites (a database with loaded modules) may not be available yet (e.g.
no database created, or no database selected).

Controllers thus provide their own extension mechanism, separate from that of
models:

Controllers are created by [inheriting](https://docs.python.org/3/tutorial/classes.html#tut-inheritance "(in Python v3.13)") from `Controller`.
Routes are defined through methods decorated with [`route()`](#odoo.http.route "odoo.http.route"):

```
class MyController(odoo.http.Controller):
    @route('/some_url', auth='public')
    def handler(self):
        return stuff()
```

To *override* a controller, [inherit](https://docs.python.org/3/tutorial/classes.html#tut-inheritance "(in Python v3.13)") from its
class and override relevant methods, re-exposing them if necessary:

```
class Extension(MyController):
    @route()
    def handler(self):
        do_before()
        return super(Extension, self).handler()
```

- decorating with [`route()`](#odoo.http.route "odoo.http.route") is necessary to keep the method
  (and route) visible: if the method is redefined without decorating, it
  will be “unpublished”
- the decorators of all methods are combined, if the overriding method’s
  decorator has no argument all previous ones will be kept, any provided
  argument will override previously defined ones e.g.:

  ```
  class Restrict(MyController):
      @route(auth='user')
      def handler(self):
          return super(Restrict, self).handler()
  ```

  will change `/some_url` from public authentication to user (requiring a
  log-in)

## API

### Routing

@odoo.http.route(*route=None*, *\*\*routing*)[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/http.py#L725)
:   Decorate a controller method in order to route incoming requests
    matching the given URL and options to the decorated method.

    > **Warning:**
    >
    > It is mandatory to re-decorate any method that is overridden in
    > controller extensions but the arguments can be omitted. See
    > `Controller` for more details.

    Parameters
    :   - **route** (*Union**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* *Iterable**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*]**]*) – The paths that the decorated
          method is serving. Incoming HTTP request paths matching this
          route will be routed to this decorated method. See [werkzeug
          routing documentation](http://werkzeug.pocoo.org/docs/routing/)
          for the format of route expressions.
        - **type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) – The type of request, either `'jsonrpc'` or
          `'http'`. It describes where to find the request parameters
          and how to serialize the response.
        - **auth** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) –

          The authentication method, one of the following:

          - `'user'`: The user must be authenticated and the current
            request will be executed using the rights of the user.
          - `'bearer'`: The user is authenticated using an “Authorization”
            request header, using the Bearer scheme with an API token.
            The request will be executed with the permissions of the
            corresponding user. If the header is missing, the request
            must belong to an authentication session, as for the “user”
            authentication method.
          - `'public'`: The user may or may not be authenticated. If he
            isn’t, the current request will be executed using the shared
            Public user.
          - `'none'`: The method is always active, even if there is no
            database. Mainly used by the framework and authentication
            modules. The request code will not have any facilities to
            access the current user.
        - **methods** (*Iterable**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*]*) – A list of http methods (verbs) this
          route applies to. If not specified, all methods are allowed.
        - **cors** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) – The Access-Control-Allow-Origin cors directive value.
        - **csrf** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")) – Whether CSRF protection should be enabled for the
          route. Enabled by default for `'http'`-type requests, disabled
          by default for `'jsonrpc'`-type requests.
        - **readonly** (*Union**[*[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *Callable**[**[**registry**,* *request**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*]**]*) – Whether this endpoint should open a cursor on a read-only
          replica instead of (by default) the primary read/write database.
        - **handle\_params\_access\_error** (*Callable**[**[*[*Exception*](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.13)")*]**,* *Response**]*) – Implement a custom behavior if an error occurred when retrieving
          the record from the URL parameters (access error or missing error).
        - **captcha** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) – The action name of the captcha. When set the
          request will be validated against a captcha implementation. Upon
          failing these requests will return a UserError.
        - **save\_session** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")) – Whether it should set a session\_id cookie
          on the http response and save dirty session on disk. `False`
          by default for `auth='bearer'`. `True` by default otherwise.

### Request

The request object is automatically set on `odoo.http.request` at
the start of the request.

*class* odoo.http.Request(*httprequest*)[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/http.py#L1763)
:   Wrapper around the incoming HTTP request with deserialized request
    parameters, session utilities and request dispatching logic.

    update\_env(*user=None*, *context=None*, *su=None*)[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/http.py#L1826)
    :   Update the environment of the current request.

        Parameters
        :   - **user** (int or `res.users record`) – optional user/user id to change the current user
            - **context** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")) – optional context dictionary to change the current context
            - **su** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")) – optional boolean to change the superuser mode

    update\_context(*\*\*overrides*)[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/http.py#L1839)
    :   Override the environment context of the current request with the
        values of `overrides`. To replace the entire context, please
        use [`update_env()`](#odoo.http.Request.update_env "odoo.http.Request.update_env") instead.

    csrf\_token(*time\_limit=None*)[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/http.py#L1904)
    :   Generates and returns a CSRF token for the current session

        Parameters
        :   **time\_limit** (*Optional**[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*]*) – the CSRF token should only be
            valid for the specified duration (in second), by default
            48h, `None` for the token to be valid as long as the
            current user’s session is.

        Returns
        :   ASCII token string

        Return type
        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    validate\_csrf(*csrf*)[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/http.py#L1926)
    :   Is the given csrf token valid ?

        Parameters
        :   **csrf** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) – The token to validate.

        Returns
        :   `True` when valid, `False` when not.

        Return type
        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    default\_lang()[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/http.py#L1957)
    :   Returns default user language according to request specification

        Returns
        :   Preferred language if specified or ‘en\_US’

        Return type
        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    get\_http\_params()[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/http.py#L1965)
    :   Extract key=value pairs from the query string and the forms
        present in the body (both application/x-www-form-urlencoded and
        multipart/form-data).

        Returns
        :   The merged key-value pairs.

        Return type
        :   [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")

    make\_response(*data*, *headers=None*, *cookies=None*, *status=200*)[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/http.py#L2021)
    :   Helper for non-HTML responses, or HTML responses with custom
        response headers or cookies.

        While handlers can just return the HTML markup of a page they want to
        send as a string if non-HTML data is returned they need to create a
        complete response object, or the returned data will not be correctly
        interpreted by the clients.

        Parameters
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) – response body
            - **status** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) – http status code
            - **headers** (`[(name, value)]`) – HTTP headers to set on the response
            - **cookies** ([*collections.abc.Mapping*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.13)")) – cookies to set on the client

        Returns
        :   a response object.

        Return type
        :   [`Response`](#odoo.http.Response "odoo.http.Response")

    make\_json\_response(*data*, *headers=None*, *cookies=None*, *status=200*)[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/http.py#L2044)
    :   Helper for JSON responses, it json-serializes `data` and
        sets the Content-Type header accordingly if none is provided.

        Parameters
        :   - **data** – the data that will be json-serialized into the response body
            - **status** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")) – http status code
            - **headers** (*List**[**(*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)**]*) – HTTP headers to set on the response
            - **cookies** ([*collections.abc.Mapping*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.13)")) – cookies to set on the client

        Return type
        :   [`Response`](#odoo.http.Response "odoo.http.Response")

    not\_found(*description=None*)[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/http.py#L2063)
    :   Shortcut for a [HTTP 404](http://tools.ietf.org/html/rfc7231#section-6.5.4) (Not Found)
        response

    render(*template*, *qcontext=None*, *lazy=True*, *\*\*kw*)[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/http.py#L2086)
    :   Lazy render of a QWeb template.

        The actual rendering of the given template will occur at then end of
        the dispatching. Meanwhile, the template and/or qcontext can be
        altered or even replaced by a static response.

        Parameters
        :   - **template** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) – template to render
            - **qcontext** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")) – Rendering context to use
            - **lazy** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")) – whether the template rendering should be deferred
              until the last possible moment
            - **kw** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")) – forwarded to werkzeug’s Response object

    reroute(*path*, *query\_string=None*)[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/http.py#L2104)
    :   Rewrite the current request URL using the new path and query
        string. This act as a light redirection, it does not return a
        3xx responses to the browser but still change the current URL.

*class* odoo.http.JsonRPCDispatcher(*request*)[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/http.py#L2512)
:   *classmethod* is\_compatible\_with(*request*)[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/http.py#L2521)
    :   Determine if the current request is compatible with this
        dispatcher.

    dispatch(*endpoint*, *args*)[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/http.py#L2525)
    :   [JSON-RPC 2](http://www.jsonrpc.org/specification) over HTTP.

        Our implementation differs from the specification on two points:

        1. The `method` member of the JSON-RPC request payload is
           ignored as the HTTP path is already used to route the request
           to the controller.
        2. We only support parameter structures by-name, i.e. the
           `params` member of the JSON-RPC request payload MUST be a
           JSON Object and not a JSON Array.

        In addition, it is possible to pass a context that replaces
        the session context via a special `context` argument that is
        removed prior to calling the endpoint.

        Successful request:

        ```
        --> {"jsonrpc": "2.0", "method": "call", "params": {"arg1": "val1" }, "id": null}

        <-- {"jsonrpc": "2.0", "result": { "res1": "val1" }, "id": null}
        ```

        Request producing a error:

        ```
        --> {"jsonrpc": "2.0", "method": "call", "params": {"arg1": "val1" }, "id": null}

        <-- {"jsonrpc": "2.0", "error": {"code": 1, "message": "End user error message.", "data": {"code": "codestring", "debug": "traceback" } }, "id": null}
        ```

    handle\_error(*exc: [Exception](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.13)")*) → [collections.abc.Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.13)")[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/http.py#L2573)
    :   Handle any exception that occurred while dispatching a request to
        a `type='jsonrpc'` route. Also handle exceptions that occurred when
        no route matched the request path, that no fallback page could
        be delivered and that the request `Content-Type` was json.

        Parameters
        :   **exc** – the exception that occurred.

        Returns
        :   a WSGI application

*class* odoo.http.HttpDispatcher(*request*)[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/http.py#L2441)
:   *classmethod* is\_compatible\_with(*request*)[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/http.py#L2446)
    :   Determine if the current request is compatible with this
        dispatcher.

    dispatch(*endpoint*, *args*)[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/http.py#L2450)
    :   Perform http-related actions such as deserializing the request
        body and query-string and checking cors/csrf while dispatching a
        request to a `type='http'` route.

        See `load()` method for the compatible
        endpoint return types.

    handle\_error(*exc: [Exception](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.13)")*) → [collections.abc.Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.13)")[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/http.py#L2479)
    :   Handle any exception that occurred while dispatching a request
        to a `type='http'` route. Also handle exceptions that occurred
        when no route matched the request path, when no fallback page
        could be delivered and that the request `Content-Type` was not
        json.

        Parameters
        :   **exc** ([*Exception*](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.13)")) – the exception that occurred.

        Returns
        :   a WSGI application

### Response

odoo.http.Response[[source]](https://github.com/odoo/odoo/blob/19.0/odoo/http.py#L1484)
:   alias of `odoo.http._Response`
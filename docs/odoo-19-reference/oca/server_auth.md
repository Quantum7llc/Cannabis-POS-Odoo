# OCA/server-auth


> **OCA Community Modules (19.0)**
> Source: https://github.com/OCA/server-auth/tree/19.0

## Purpose

OCA authentication modules: TOTP two-factor, OAuth2, SAML2, password policy, and login audit logging. Use when hardening Odoo authentication or adding SSO.

---


## Module Overview


# server-auth

server-auth

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[auth_oauth_multi_token](auth_oauth_multi_token/) | 19.0.1.0.0 |  | Allow multiple connection with the same OAuth account
[auth_oidc](auth_oidc/) | 19.0.1.0.0 |  | Allow users to login through OpenID Connect Provider
[auth_session_timeout](auth_session_timeout/) | 19.0.1.0.0 |  | This module disable all inactive sessions since a given delay
[auth_user_case_insensitive](auth_user_case_insensitive/) | 19.0.1.0.0 |  | Makes the user login field case insensitive
[impersonate_login](impersonate_login/) | 19.0.1.0.0 |  | tools

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to Odoo Community Association (OCA)
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----
OCA, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit
organization whose mission is to support the collaborative development of Odoo features
and promote its widespread use.
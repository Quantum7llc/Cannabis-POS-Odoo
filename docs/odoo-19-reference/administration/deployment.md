# Deployment — On-Premise Install, Nginx & Docker

> **Odoo 19.0 Reference**
> Source: www.odoo.com/documentation/19.0 — HTML converted via markdownify

## Purpose

On-premise Odoo deployment: packages, source install, Nginx reverse proxy, worker configuration, email gateway, GeolP, and community-to-enterprise migration. Use when deploying or maintaining a self-hosted Odoo instance.

---

# On-premise

## Register a database

To register your database, enter your subscription code in the banner in the app dashboard. If the
registration is successful, the banner will turn green and display the database expiration date.

> **Note:**
>
> The expiration date is also displayed at the bottom of the Settings page.

## Duplicate a database

Duplicate a database by accessing the database manager on your server
(`<odoo-server>/web/database/manager`). Typically, you want to duplicate your production database
into a neutralized testing database. It can be done by checking the neutralize box when prompted,
which executes all `neutralize.sql` scripts for every installed module.

## Common error messages and solutions

### Registration error

In case of a registration error, the following message should be displayed.

![Database registration error message](../_images/error-message-sub-code.png)

To resolve the issue:

- Check the **validity of your Odoo Enterprise subscription** by verifying if your subscription
  details have the tag In Progress on your [Odoo Account](https://accounts.odoo.com/my/subscription) or contact your Account Manager.
- Ensure that **no other database is linked** to the subscription code, as only one database can be
  linked per subscription.

  > **Note:**
  >
  > If a test or a development database is needed, you can [duplicate a database].
- Verify that **no databases share the same UUID** (Universally Unique Identifier) by opening your
  [Odoo Contract](https://accounts.odoo.com/my/subscription). If two or more databases share the
  same UUID, their name will be displayed.

  ![Database UUID error message](../_images/unlink-db-name-collision.png)

  If that is the case, manually change the database(s) UUID or [send a support ticket](https://www.odoo.com/help).
- As the update notification must be able to reach Odoo’s subscription validation servers, ensure
  your **network and firewall settings** allow the Odoo server to open outgoing connections
  towards:

  - Odoo 18.0 and above: `services.odoo.com` on port `80`
  - Odoo 17.0 and below: `services.openerp.com` on port `80`

  These ports must be kept open even after registering a database, as the update notification runs
  once a week.

### Too many users error

If you have more users in a local database than provisioned in your Odoo Enterprise subscription,
the following message should be displayed.

![Too many users on a database error message](../_images/add-more-users1.png)

When the message appears, you have 30 days to act before the database expires. The countdown is
updated every day.

To resolve the issue, either:

- **Add more users** to your subscription by clicking the Upgrade your subscription link
  displayed in the message to validate the upsell quotation and pay for the extra users.
- [Deactivate users](../applications/general/users.html#users-deactivate) and **reject** the upsell quotation.

Once your database has the correct number of users, the expiration message disappears automatically
after a few days, when the next verification occurs.

### Database expired error

If your database expires before you renew your subscription, the following message should be
displayed.

![Database expired error message](../_images/database-expired.png)

This message appears if you fail to act before the end of the 30-day countdown.

To resolve the issue, either:

- Click the Renew your subscription link displayed in the message and complete the
  process. If you pay by wire transfer, your subscription will be renewed when the payment arrives
  which can take a few days. Credit card payments are processed immediately.
- [Send a support ticket](https://www.odoo.com/help).

---

# Packaged installers

Odoo provides packaged installers for Debian-based Linux distributions (Debian, Ubuntu, etc.),
RPM-based Linux distributions (Fedora, CentOS, RHEL, etc.), and Windows for the Community and
Enterprise editions.

Official **Community** nightly packages with all relevant dependency requirements are available on
the [nightly server](https://nightly.odoo.com).

> **Note:**
>
> Nightly packages may be difficult to keep up to date.

Official **Community** and **Enterprise** packages can be downloaded from the [Odoo download page](https://www.odoo.com/page/download).

> **Note:**
>
> It is required to be logged in as a paying on-premise customer or partner to download the
> Enterprise packages.

## Linux

### Prepare

Odoo needs a [PostgreSQL](https://www.postgresql.org/) server to run properly.

Debian/UbuntuFedora

The default configuration for the Odoo ‘deb’ package is to use the PostgreSQL server on the
same host as the Odoo instance. Execute the following command to install the PostgreSQL
server:

```
$ sudo apt install postgresql -y
```

Make sure that the `sudo` command is available and well configured and, only then, execute the
following command to install the PostgreSQL server:

```
$ sudo dnf install -y postgresql-server
$ sudo postgresql-setup --initdb --unit postgresql
$ sudo systemctl enable postgresql
$ sudo systemctl start postgresql
```

> **Warning:**
>
> `wkhtmltopdf` is not installed through **pip** and must be installed manually in [version 0.12.6](https://github.com/wkhtmltopdf/packaging/releases/tag/0.12.6.1-3) for it to support headers
> and footers. Check out the [wkhtmltopdf wiki](https://github.com/odoo/odoo/wiki/Wkhtmltopdf)
> for more details on the various versions.

### Repository

Odoo S.A. provides a repository that can be used to install the **Community** edition by executing
the following commands:

Debian/UbuntuFedora

```
$ wget -q -O - https://nightly.odoo.com/odoo.key | sudo gpg --dearmor -o /usr/share/keyrings/odoo-archive-keyring.gpg
$ echo 'deb [signed-by=/usr/share/keyrings/odoo-archive-keyring.gpg] https://nightly.odoo.com/19.0/nightly/deb/ ./' | sudo tee /etc/apt/sources.list.d/odoo.list
$ sudo apt-get update && sudo apt-get install odoo
```

Use the usual `apt-get upgrade` command to keep the installation up-to-date.

```
$ sudo dnf config-manager --add-repo=https://nightly.odoo.com/19.0/nightly/rpm/odoo.repo
$ sudo dnf install -y odoo
$ sudo systemctl enable odoo
$ sudo systemctl start odoo
```

> **Note:**
>
> Currently, there is no nightly repository for the Enterprise edition.

### Distribution package

Instead of using the repository, packages for both the **Community** and **Enterprise** editions can
be downloaded from the [Odoo download page](https://www.odoo.com/page/download).

UbuntuFedora

> **Note:**
>
> Odoo 19 ‘deb’ package currently supports [Ubuntu Noble (24.04LTS)](https://releases.ubuntu.com/noble).

Once downloaded, execute the following commands **as root** to install Odoo as a service,
create the necessary PostgreSQL user, and automatically start the server:

```
# apt update
# apt install <path_to_installation_package>
```

> **Note:**
>
> Odoo 19 ‘rpm’ package supports Fedora 42.

Once downloaded, the package can be installed using the ‘dnf’ package manager:

```
$ sudo dnf localinstall odoo_19.0.latest.noarch.rpm
$ sudo systemctl enable odoo
$ sudo systemctl start odoo
```

## Windows

> > **Warning:**
> >
> > Windows packaging is offered for the convenience of testing or running single-user local
> > instances but production deployment is discouraged due to a number of limitations and risks
> > associated with deploying Odoo on a Windows platform.

1. Download the installer from the [nightly server](https://nightly.odoo.com) (Community only) or
   the Windows installer from the [Odoo download page](https://www.odoo.com/page/download) (any
   edition.
2. Execute the downloaded file.

   > **Warning:**
   >
   > On Windows 8 and later, a warning titled *Windows protected your PC* may be displayed. Click
   > **More Info** and then **Run anyway** to proceed.
3. Accept the [UAC](https://en.wikipedia.org/wiki/User_Account_Control) prompt.
4. Go through the installation steps.

Odoo launches automatically at the end of the installation.

---

# Source install

The source ‘installation’ is not about installing Odoo but running it directly from the source
instead.

Using the Odoo source can be more convenient for module developers as it is more easily accessible
than using packaged installers.

It makes starting and stopping Odoo more flexible and explicit than the services set up by the
packaged installers. Also, it allows overriding settings using [command-line parameters](../../developer/reference/cli.html#reference-cmdline) without needing to edit a configuration file.

Finally, it provides greater control over the system’s setup and allows to more easily keep (and
run) multiple versions of Odoo side-by-side.

## Fetch the sources

There are two ways to obtain the source code of Odoo: as a ZIP **archive** or through **Git**.

### Archive

Community edition:

- [Odoo download page](https://www.odoo.com/page/download)
- [GitHub Community repository](https://github.com/odoo/odoo)
- [Nightly server](https://nightly.odoo.com)

Enterprise edition:

- [Odoo download page](https://www.odoo.com/page/download)
- [GitHub Enterprise repository](https://github.com/odoo/enterprise)

### Git

> **Note:**
>
> It is required to have [Git](https://git-scm.com/) installed, and it is recommended to have a
> basic knowledge of Git commands to proceed.

To clone a Git repository, choose between cloning with HTTPS or SSH. In most cases, the best option
is HTTPS. However, choose SSH to contribute to Odoo source code or when following the [Getting
Started developer tutorial](../../developer/tutorials/server_framework_101.html).

LinuxWindowsMac OS

Clone with HTTPSClone with SSH

```
$ git clone --branch 19.0 --single-branch https://github.com/odoo/odoo.git
$ git clone --branch 19.0 --single-branch https://github.com/odoo/enterprise.git
```

```
$ git clone --branch 19.0 --single-branch git@github.com:odoo/odoo.git
$ git clone --branch 19.0 --single-branch git@github.com:odoo/enterprise.git
```

Clone with HTTPSClone with SSH

```
C:\> git clone --branch 19.0 --single-branch https://github.com/odoo/odoo.git
C:\> git clone --branch 19.0 --single-branch https://github.com/odoo/enterprise.git
```

```
C:\> git clone --branch 19.0 --single-branch git@github.com:odoo/odoo.git
C:\> git clone --branch 19.0 --single-branch git@github.com:odoo/enterprise.git
```

Clone with HTTPSClone with SSH

```
$ git clone --branch 19.0 --single-branch https://github.com/odoo/odoo.git
$ git clone --branch 19.0 --single-branch https://github.com/odoo/enterprise.git
```

```
$ git clone --branch 19.0 --single-branch git@github.com:odoo/odoo.git
$ git clone --branch 19.0 --single-branch git@github.com:odoo/enterprise.git
```

> **Note:**
>
> **The Enterprise git repository does not contain the full Odoo source code**. It is only a
> collection of extra add-ons. The main server code is in the Community edition. Running the
> Enterprise version means running the server from the Community version with the `addons-path`
> option set to the folder with the Enterprise edition. It is required to clone both the Community
> and Enterprise repositories to have a working Odoo Enterprise installation.

## Prepare

### Python

Odoo requires **Python 3.10** or later to run.

Changed in version 17: Minimum requirement updated from Python 3.7 to Python 3.10.

LinuxWindowsMac OS

Use a package manager to download and install Python 3 if needed.

[Download the latest version of Python 3](https://www.python.org/downloads/windows/) and
install it.

During installation, check **Add Python 3 to PATH**, then click **Customize Installation** and
make sure that **pip** is checked.

Use a package manager ([Homebrew](https://brew.sh/), [MacPorts](https://www.macports.org))
to download and install Python 3 if needed.

> **Note:**
>
> If Python 3 is already installed, make sure that the version is 3.10 or above, as previous
> versions are not compatible with Odoo.
>
> LinuxWindowsMac OS
>
> ```
> $ python3 --version
> ```
>
> ```
> C:\> python --version
> ```
>
> ```
> $ python3 --version
> ```
>
> Verify that [pip](https://pip.pypa.io) is also installed for this version.
>
> LinuxWindowsMac OS
>
> ```
> $ pip3 --version
> ```
>
> ```
> C:\> pip --version
> ```
>
> ```
> $ pip3 --version
> ```

### PostgreSQL

Odoo uses PostgreSQL as its database management system.

Changed in version 19: Minimum requirement updated from PostgreSQL 12 to PostgreSQL 13.

LinuxWindowsMac OS

Use a package manager to download and install PostgreSQL (supported versions: 13.0 or above).
It can be achieved by executing the following:

```
$ sudo apt install postgresql postgresql-client
```

[Download PostgreSQL](https://www.postgresql.org/download/windows) (supported versions: 13.0
or above) and install it.

Use [Postgres.app](https://postgresapp.com) to download and install PostgreSQL (supported
version: 13.0 or above).

> **Note:**
>
> To make the command line tools bundled with Postgres.app available, make sure to set up the
> `$PATH` variable by following the [Postgres.app CLI tools instructions](https://postgresapp.com/documentation/cli-tools.html).

By default, the only user is `postgres`. As Odoo forbids connecting as `postgres`, create a new
PostgreSQL user.

LinuxWindowsMac OS

```
$ sudo -u postgres createuser -d -R -S $USER
$ createdb $USER
```

> **Note:**
>
> Because the PostgreSQL user has the same name as the Unix login, it is possible to connect
> to the database without a password.

1. Add PostgreSQL’s `bin` directory (by default:
   `C:\Program Files\PostgreSQL\<version>\bin`) to the `PATH`.
2. Create a postgres user with a password using the pg admin gui:

   1. Open **pgAdmin**.
   2. Double-click the server to create a connection.
   3. Select Object ‣ Create ‣ Login/Group Role.
   4. Enter the username in the **Role Name** field (e.g., `odoo`).
   5. Open the **Definition** tab, enter a password (e.g., `odoo`), and click **Save**.
   6. Open the **Privileges** tab and switch **Can login?** to `Yes` and **Create database?**
      to `Yes`.

```
$ sudo -u postgres createuser -d -R -S $USER
$ createdb $USER
```

> **Note:**
>
> Because the PostgreSQL user has the same name as the Unix login, it is possible to connect
> to the database without a password.

### Dependencies

LinuxWindowsMac OS

Using **distribution packages** is the preferred way of installing dependencies.
Alternatively, install the Python dependencies with **pip**.

Debian/UbuntuInstall with pip

On Debian/Ubuntu, the following commands should install the required packages:

```
$ cd odoo #CommunityPath
$ sudo ./setup/debinstall.sh
```

The `setup/debinstall.sh` script will parse the [debian/control](https://github.com/odoo/odoo/blob/19.0/debian/control) file and install the found packages.

> **Warning:**
>
> Using pip may lead to security issues and broken dependencies; only do this if you
> know what you are doing.

As some of the Python packages need a compilation step, they require system libraries to
be installed.

On Debian/Ubuntu, the following command should install these required libraries:

```
$ sudo apt install python3-pip libldap2-dev libpq-dev libsasl2-dev
```

Odoo dependencies are listed in the `requirements.txt` file located at the root of
the Odoo Community directory.

> **Note:**
>
> The Python packages in `requirements.txt` are based on their stable/LTS
> Debian/Ubuntu corresponding version at the moment of the Odoo release. For example,
> for Odoo 15.0, the `python3-babel` package version is 2.8.0 in Debian Bullseye and
> 2.6.0 in Ubuntu Focal. The lowest version is then chosen in the
> `requirements.txt`.

> **Note:**
>
> It can be preferable not to mix Python module packages between different instances of
> Odoo or with the system. However, it is possible to use [virtualenv](https://pypi.org/project/virtualenv/) to create isolated Python environments.

Navigate to the path of the Odoo Community installation (`CommunityPath`) and run
**pip** on the requirements file to install the requirements for the current user.

```
$ cd /CommunityPath
$ pip install -r requirements.txt
```

Before installing the dependencies, download and install the [Build Tools for Visual
Studio](https://visualstudio.microsoft.com/downloads/). Select **C++ build tools** in the
**Workloads** tab and install them when prompted.

Odoo dependencies are listed in the `requirements.txt` file located at the root of the Odoo
Community directory.

> > **Note:**
> >
> > It can be preferable not to mix Python module packages between different instances of
> > Odoo or with the system. However, it is possible to use [virtualenv](https://pypi.org/project/virtualenv/) to create isolated Python environments.

Navigate to the path of the Odoo Community installation (`CommunityPath`) and run **pip** on
the requirements file in a terminal **with Administrator privileges**:

```
C:\> cd \CommunityPath
C:\> pip install setuptools wheel
C:\> pip install -r requirements.txt
```

Odoo dependencies are listed in the `requirements.txt` file located at the root of the Odoo
Community directory.

> > **Note:**
> >
> > It can be preferable not to mix Python module packages between different instances of
> > Odoo or with the system. However, it is possible to use [virtualenv](https://pypi.org/project/virtualenv/) to create isolated Python environments.

Navigate to the path of the Odoo Community installation (`CommunityPath`) and run **pip** on
the requirements file:

```
$ cd /CommunityPath
$ pip3 install setuptools wheel
$ pip3 install -r requirements.txt
```

> **Warning:**
>
> Non-Python dependencies must be installed with a package manager ([Homebrew](https://brew.sh/), [MacPorts](https://www.macports.org)).
>
> 1. Download and install the **Command Line Tools**:
>
>    ```
>    $ xcode-select --install
>    ```
> 2. Use the package manager to install non-Python dependencies.

> **Note:**
>
> For languages using a **right-to-left interface** (such as Arabic or Hebrew), the `rtlcss`
> package is required.
>
> LinuxWindowsMac OS
>
> 1. Download and install **nodejs** and **npm** with a package manager.
> 2. Install `rtlcss`:
>
>    ```
>    $ sudo npm install -g rtlcss
>    ```
>
> 1. Download and install [nodejs](https://nodejs.org/en/download).
> 2. Install `rtlcss`:
>
>    ```
>    C:\> npm install -g rtlcss
>    ```
> 3. Edit the system environment’s variable `PATH` to add the folder where `rtlcss.cmd` is
>    located (typically: `C:\Users\<user>\AppData\Roaming\npm\`).
>
> 1. Download and install **nodejs** with a package manager ([Homebrew](https://brew.sh/),
>    [MacPorts](https://www.macports.org)).
> 2. Install `rtlcss`:
>
>    ```
>    $ sudo npm install -g rtlcss
>    ```

> **Warning:**
>
> `wkhtmltopdf` is not installed through **pip** and must be installed manually in [version 0.12.6](https://github.com/wkhtmltopdf/packaging/releases/tag/0.12.6.1-3) for it to support headers
> and footers. Check out the [wkhtmltopdf wiki](https://github.com/odoo/odoo/wiki/Wkhtmltopdf)
> for more details on the various versions.

## Running Odoo

Once all dependencies are set up, Odoo can be launched by running `odoo-bin`, the command-line
interface of the server. It is located at the root of the Odoo Community directory.

To configure the server, either specify [command-line arguments](../../developer/reference/cli.html#reference-cmdline-server) or
a [configuration file](../../developer/reference/cli.html#reference-cmdline-config).

> **Note:**
>
> For the Enterprise edition, add the path to the `enterprise` add-ons to the `addons-path`
> argument. Note that it must come before the other paths in `addons-path` for add-ons to be loaded
> correctly.

Common necessary configurations are:

- PostgreSQL user and password.
- Custom addon paths beyond the defaults to load custom modules.

A typical way to run the server would be:

LinuxWindowsMac OS

```
$ cd /CommunityPath
$ python3 odoo-bin --addons-path=addons -d mydb
```

Where `CommunityPath` is the path of the Odoo Community installation, and `mydb` is the name
of the PostgreSQL database.

```
C:\> cd CommunityPath/
C:\> python odoo-bin -r dbuser -w dbpassword --addons-path=addons -d mydb
```

Where `CommunityPath` is the path of the Odoo Community installation, `dbuser` is the
PostgreSQL login, `dbpassword` is the PostgreSQL password, and `mydb` is the name of the
PostgreSQL database.

```
$ cd /CommunityPath
$ python3 odoo-bin --addons-path=addons -d mydb
```

Where `CommunityPath` is the path of the Odoo Community installation, and `mydb` is the name
of the PostgreSQL database.

After the server has started (the INFO log `odoo.modules.loading: Modules loaded.` is printed), open
<http://localhost:8069> in a web browser and log into the Odoo database with the base administrator
account: use `admin` as the email and, again, `admin` as the password.

> **Note:**
>
> - From there, create and manage new [users](../../applications/general/users.html).
> - The user account used to log into Odoo’s web interface differs from the [`--db_user`](../../developer/reference/cli.html#cmdoption-odoo-bin-r) CLI argument.

> **Note:**
>
> [The list of CLI arguments for odoo-bin](../../developer/reference/cli.html)

---

# Bugfix updates

## Introduction

In order to benefit from the latest improvements, security fixes, bug corrections and
performance boosts, you may need to update your Odoo installation from time to time.

This guide only applies when are using Odoo on your own hosting infrastructure.
If you are using one of the Odoo Cloud solutions, updates are automatically performed for you.

The terminology surrounding software updates is often confusing, so here are some preliminary
definitions:

Updating (an Odoo installation)
:   Refers to the process of obtaining the latest revision of the source code for
    your current Odoo Edition. For example, updating your Odoo Enterprise 13.0 to the
    latest revision.
    This does not directly cause any change to the contents of your Odoo database, and
    can be undone by reinstalling the previous revision of the source code.

Upgrading (an Odoo database)
:   Refers to a complex data processing operation where the structure and contents of your
    database is permanently altered to make it compatible with a new release of Odoo.
    This operation is irreversible and typically accomplished via Odoo’s
    [database upgrade service](https://upgrade.odoo.com), when you decide to
    switch to a newer release of Odoo.
    Historically, this process has also been known as a “migration” because it involves moving data
    around inside the database, even though the database may end up at the same physical location
    after the upgrade.

This page describes the typical steps needed to *update* an Odoo installation to the latest
version. If you’d like more information about upgrading a database, please visit the
[Odoo Upgrade page](https://upgrade.odoo.com) instead.

## In a nutshell

Updating Odoo is accomplished by simply reinstalling the latest version of your Odoo
Edition on top of your current installation. This will preserve your data without any alteration,
as long as you do not uninstall PostgreSQL (the database engine that comes with Odoo).

The main reference for updating is logically our [installation guide](../on_premise.html),
which explains the common installation methods.

Updating is also most appropriately accomplished by the person who deployed Odoo initially,
because the procedure is very similar.

> **Note:**
>
> We always recommend to download a complete new up-to-date Odoo version, rather than
> manually applying patches, such as the security patches that come with Security
> Advisories.
> The patches are mainly provided for installations that are heavily customized, or for
> technical personnel who prefer to apply minimal changes temporarily while testing a
> complete update.

## Step 1: Download an updated Odoo version

The central download page is <https://www.odoo.com/page/download>. If you see a “Buy” link for the
Odoo Enterprise download, make sure you are logged into Odoo.com with the same login that is
linked to your Odoo Enterprise subscription.

Alternatively, you can use the unique download link that was included with your Odoo Enterprise
purchase confirmation email.

> **Note:**
>
> Downloading an updated version is not necessary if you installed via Github (see below)

## Step 2: Make a backup of your database

The update procedure is quite safe and should not alter you data. However it’s always best to take
a full database backup before performing any change on your installation, and to store it somewhere
safe, on a different computer.

If you have not disabled the database manager screen (see [here](deploy.html#security) why you should), you
can use it (link at bottom of your database selection screen) to download a backup of your
database(s). If you disabled it, use the same procedure than for your usual backups.

## Step 3: Install the updated version

Choose the method that matches your current installation:

### Packaged Installers

If you installed Odoo with an installation package downloaded on our website (the recommended method),
updating is very simple.
All you have to do is download the installation package corresponding to your system (see step #1)
and install it on your server. They are updated daily and include the latest security fixes.
Usually, you can simply double-click the package to install it on top of the current installation.
After installing the package, be sure to restart the Odoo service or reboot your server,
and you’re all set.

### Source Install (Tarball)

If you have originally installed Odoo with the “tarball” version (source code archive), you have
to replace the installation directory with a newer version. First download the latest tarball
from Odoo.com. They are updated daily and include the latest security fixes (see step #1)
After downloading the package, extract it to a temporary location on your server.

You will get a folder labeled with the version of the source code, for example “odoo-13.0+e.20190719”,
that contains a folder “odoo.egg-info” and the actual source code folder named “odoo” (for Odoo 10
and later) or “openerp” for older versions.
You can ignore the odoo.egg-info folder. Locate the folder where your current installation is deployed,
and replace it with the newer “odoo” or “openerp” folder that was in the archive you just extracted.

Be sure to match the folder layout, for example the new “addons” folder included in the source code
should end up exactly at the same path it was before. Next, watch out for any specific configuration
files that you may have manually copied or modified in the old folder, and copy them over to the
new folder.
Finally, restart the Odoo service or reboot the machine, and you are all set.

### Source Install (Github)

If you have originally installed Odoo with a full Github clone of the official repositories, the
update procedure requires you to pull the latest source code via git.
Change into the directory for each repository (the main Odoo repository, and the Enterprise
repository), and run the following commands:

```
git fetch
git rebase --autostash
```

The last command may encounter source code conflicts if you had edited the Odoo source code locally.
The error message will give you the list of files with conflicts, and you will need to resolve
the conflicts manually, by editing them and deciding which part of the code to keep.

Alternatively, if you prefer to simply discard the conflicting changes and restore the official
version, you can use the following command:

```
git reset --hard
```

Finally, restart the Odoo service or reboot the machine, and you should be done.

### Docker

Please refer to our [Docker image documentation](https://hub.docker.com/_/odoo/) for
specific update instructions.

---

# System configuration

This document describes basic steps to set up Odoo in production or on an
internet-facing server. It follows [installation](../on_premise.html), and is
not generally necessary for a development systems that is not exposed on the
internet.

> **Warning:**
>
> If you are setting up a public server, be sure to check our [Security] recommendations!

## dbfilter

Odoo is a multi-tenant system: a single Odoo system may run and serve a number
of database instances. It is also highly customizable, with customizations
(starting from the modules being loaded) depending on the “current database”.

This is not an issue when working with the backend (web client) as a logged-in
company user: the database can be selected when logging in, and customizations
loaded afterwards.

However it is an issue for non-logged users (portal, website) which aren’t
bound to a database: Odoo needs to know which database should be used to load
the website page or perform the operation. If multi-tenancy is not used that is not an
issue, there’s only one database to use, but if there are multiple databases
accessible Odoo needs a rule to know which one it should use.

That is one of the purposes of [`--db-filter`](../../developer/reference/cli.html#cmdoption-odoo-bin-db-filter):
it specifies how the database should be selected based on the hostname (domain)
that is being requested. The value is a [regular expression](https://docs.python.org/3/library/re.html), possibly
including the dynamically injected hostname (`%h`) or the first subdomain
(`%d`) through which the system is being accessed.

For servers hosting multiple databases in production, especially if `website`
is used, dbfilter **must** be set, otherwise a number of features will not work
correctly.

### Configuration samples

- Show only databases with names beginning with ‘mycompany’

in [the configuration file](../../developer/reference/cli.html#reference-cmdline-config-file) set:

```
[options]
dbfilter = ^mycompany.*$
```

- Show only databases matching the first subdomain after `www`: for example
  the database “mycompany” will be shown if the incoming request
  was sent to `www.mycompany.com` or `mycompany.co.uk`, but not
  for `www2.mycompany.com` or `helpdesk.mycompany.com`.

in [the configuration file](../../developer/reference/cli.html#reference-cmdline-config-file) set:

```
[options]
dbfilter = ^%d$
```

> **Note:**
>
> Setting a proper [`--db-filter`](../../developer/reference/cli.html#cmdoption-odoo-bin-db-filter) is an important part
> of securing your deployment.
> Once it is correctly working and only matching a single database per hostname, it
> is strongly recommended to block access to the database manager screens,
> and to use the `--no-database-list` startup parameter to prevent listing
> your databases, and to block access to the database management screens.
> See also [security].

## PostgreSQL

By default, PostgreSQL only allows connection over UNIX sockets and loopback
connections (from “localhost”, the same machine the PostgreSQL server is
installed on).

UNIX socket is fine if you want Odoo and PostgreSQL to execute on the same
machine, and is the default when no host is provided, but if you want Odoo and
PostgreSQL to execute on different machines [1] it will
need to [listen to network interfaces](https://www.postgresql.org/docs/12/static/runtime-config-connection.html) [2], either:

- Only accept loopback connections and [use an SSH tunnel](https://www.postgresql.org/docs/12/static/ssh-tunnels.html) between the
  machine on which Odoo runs and the one on which PostgreSQL runs, then
  configure Odoo to connect to its end of the tunnel
- Accept connections to the machine on which Odoo is installed, possibly
  over ssl (see [PostgreSQL connection settings](https://www.postgresql.org/docs/12/static/runtime-config-connection.html) for details), then configure
  Odoo to connect over the network

### Configuration sample

- Allow tcp connection on localhost
- Allow tcp connection from 192.168.1.x network

in `/etc/postgresql/<YOUR POSTGRESQL VERSION>/main/pg_hba.conf` set:

```
# IPv4 local connections:
host    all             all             127.0.0.1/32            md5
host    all             all             192.168.1.0/24          md5
```

in `/etc/postgresql/<YOUR POSTGRESQL VERSION>/main/postgresql.conf` set:

```
listen_addresses = 'localhost,192.168.1.2'
port = 5432
max_connections = 80
```

### Configuring Odoo

Out of the box, Odoo connects to a local postgres over UNIX socket via port
5432. This can be overridden using [the database options](../../developer/reference/cli.html#reference-cmdline-server-database) when your Postgres deployment is not
local and/or does not use the installation defaults.

The [packaged installers](packages.html) will automatically
create a new user (`odoo`) and set it as the database user.

- The database management screens are protected by the `admin_passwd`
  setting. This setting can only be set using configuration files, and is
  simply checked before performing database alterations. It should be set to
  a randomly generated value to ensure third parties can not use this
  interface.
- All database operations use the [database options](../../developer/reference/cli.html#reference-cmdline-server-database), including the database management
  screen. For the database management screen to work requires that the PostgreSQL user
  have `createdb` right.
- Users can always drop databases they own. For the database management screen
  to be completely non-functional, the PostgreSQL user needs to be created with
  `no-createdb` and the database must be owned by a different PostgreSQL user.

  > **Warning:**
  >
  > the PostgreSQL user *must not* be a superuser

#### Configuration sample

- connect to a PostgreSQL server on 192.168.1.2
- port 5432
- using an ‘odoo’ user account,
- with ‘pwd’ as a password
- filtering only db with a name beginning with ‘mycompany’

in [the configuration file](../../developer/reference/cli.html#reference-cmdline-config-file) set:

```
[options]
admin_passwd = mysupersecretpassword
db_host = 192.168.1.2
db_port = 5432
db_user = odoo
db_password = pwd
dbfilter = ^mycompany.*$
```

### SSL Between Odoo and PostgreSQL

Since Odoo 11.0, you can enforce ssl connection between Odoo and PostgreSQL.
in Odoo the db\_sslmode control the ssl security of the connection
with value chosen out of ‘disable’, ‘allow’, ‘prefer’, ‘require’, ‘verify-ca’
or ‘verify-full’

[PostgreSQL Doc](https://www.postgresql.org/docs/12/static/libpq-ssl.html)

## Builtin server

Odoo includes built-in HTTP, cron, and live-chat servers, using either multi-threading or
multi-processing.

The **multi-threaded** server is a simpler server primarily used for development, demonstrations,
and its compatibility with various operating systems (including Windows). A new thread is spawned
for every new HTTP request, even for long-lived connections such as websocket. Extra daemonic cron
threads are spawned too. Due to a Python limitation (GIL), it doesn’t make the best use of the
hardware.

The multi-threaded server is the default server, also for docker containers. It is selected by
leaving the [`--workers`](../../developer/reference/cli.html#cmdoption-odoo-bin-workers) option out or setting it to `0`.

The **multi-processing** server is a full-blown server primarily used for production. It is not
liable to the same Python limitation (GIL) on resource usage and hence makes the best use of the
hardware. A pool of workers is created upon server startup. New HTTP requests are queued by the OS
until there are workers ready to process them. An extra event-driven HTTP worker for the live chat
is spawned on an alternative port. Extra cron workers are spawned too. A configurable process
reaper monitors resource usage and can kill/restart failed workers.

The multi-processing server is opt-in. It is selected by setting the [`--workers`](../../developer/reference/cli.html#cmdoption-odoo-bin-workers) option to a non-null integer.

> **Note:**
>
> Because it is highly customized for Linux servers, the multi-processing server is not available
> on Windows.

### Worker number calculation

- Rule of thumb : (#CPU \* 2) + 1
- Cron workers need CPU
- 1 worker ~= 6 concurrent users

### memory size calculation

- We consider 20% of the requests are heavy requests, while 80% are simpler ones
- A heavy worker, when all computed field are well designed, SQL requests are well designed, … is estimated to consume around 1GB of RAM
- A lighter worker, in the same scenario, is estimated to consume around 150MB of RAM

Needed RAM = #worker \* ( (light\_worker\_ratio \* light\_worker\_ram\_estimation) + (heavy\_worker\_ratio \* heavy\_worker\_ram\_estimation) )

### LiveChat

In multi-processing, a dedicated LiveChat worker is automatically started and listens on
the [`--gevent-port`](../../developer/reference/cli.html#cmdoption-odoo-bin-gevent-port). By default, the HTTP requests will keep
accessing the normal HTTP workers instead of the LiveChat one. You must deploy a proxy in front of
Odoo and redirect incoming requests whose path starts with `/websocket/` to the LiveChat worker.
You must also start Odoo in [`--proxy-mode`](../../developer/reference/cli.html#cmdoption-odoo-bin-proxy-mode) so it uses the real
client headers (such as hostname, scheme, and IP) instead of the proxy ones.

### Configuration sample

- Server with 4 CPU, 8 Thread
- 60 concurrent users
- 60 users / 6 = 10 <- theoretical number of worker needed
- (4 \* 2) + 1 = 9 <- theoretical maximal number of worker
- We’ll use 8 workers + 1 for cron. We’ll also use a monitoring system to measure cpu load, and check if it’s between 7 and 7.5 .
- RAM = 9 \* ((0.8\*150) + (0.2\*1024)) ~= 3GB RAM for Odoo

in [the configuration file](../../developer/reference/cli.html#reference-cmdline-config-file):

```
[options]
limit_memory_hard = 1677721600
limit_memory_soft = 629145600
limit_request = 8192
limit_time_cpu = 600
limit_time_real = 1200
max_cron_threads = 1
workers = 8
```

## HTTPS

Whether it’s accessed via website/web client or web service, Odoo transmits
authentication information in cleartext. This means a secure deployment of
Odoo must use HTTPS[3]. SSL termination can be implemented via
just about any SSL termination proxy, but requires the following setup:

- Enable Odoo’s [`proxy mode`](../../developer/reference/cli.html#cmdoption-odoo-bin-proxy-mode). This should only be enabled when Odoo is behind a reverse proxy
- Set up the SSL termination proxy ([Nginx termination example](https://nginx.com/resources/admin-guide/nginx-ssl-termination/))
- Set up the proxying itself ([Nginx proxying example](https://nginx.com/resources/admin-guide/reverse-proxy/))
- Your SSL termination proxy should also automatically redirect non-secure
  connections to the secure port

### Configuration sample

- Redirect http requests to https
- Proxy requests to odoo

in [the configuration file](../../developer/reference/cli.html#reference-cmdline-config-file) set:

```
proxy_mode = True
```

in `/etc/nginx/sites-enabled/odoo.conf` set:

```
#odoo server
upstream odoo {
  server 127.0.0.1:8069;
}
upstream odoochat {
  server 127.0.0.1:8072;
}
map $http_upgrade $connection_upgrade {
  default upgrade;
  ''      close;
}

# http -> https
server {
  listen 80;
  server_name odoo.mycompany.com;
  rewrite ^(.*) https://$host$1 permanent;
}

server {
  listen 443 ssl;
  server_name odoo.mycompany.com;
  proxy_read_timeout 720s;
  proxy_connect_timeout 720s;
  proxy_send_timeout 720s;

  # SSL parameters
  ssl_certificate /etc/ssl/nginx/server.crt;
  ssl_certificate_key /etc/ssl/nginx/server.key;
  ssl_session_timeout 30m;
  ssl_protocols TLSv1.2;
  ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;
  ssl_prefer_server_ciphers off;

  # log
  access_log /var/log/nginx/odoo.access.log;
  error_log /var/log/nginx/odoo.error.log;

  # Redirect websocket requests to odoo gevent port
  location /websocket {
    proxy_pass http://odoochat;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $connection_upgrade;
    proxy_set_header X-Forwarded-Host $http_host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Real-IP $remote_addr;

    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";
    proxy_cookie_flags session_id samesite=lax secure;  # requires nginx 1.19.8
  }

  # Redirect requests to odoo backend server
  location / {
    # Add Headers for odoo proxy mode
    proxy_set_header X-Forwarded-Host $http_host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_redirect off;
    proxy_pass http://odoo;

    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";
    proxy_cookie_flags session_id samesite=lax secure;  # requires nginx 1.19.8
  }

  # common gzip
  gzip_types text/css text/scss text/plain text/xml application/xml application/json application/javascript;
  gzip on;
}
```

### HTTPS Hardening

Add the `Strict-Transport-Security` header to all requests, in order to prevent
browsers from ever sending a plain HTTP request to this domain. You will need
to maintain a working HTTPS service with a valid certificate on this domain at
all times, otherwise your users will see security alerts or be entirely unable
to access it.

Force HTTPS connections during a year for every visitor in NGINX with the line:

```
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";
```

Additional configuration can be defined for the `session_id` cookie. The `Secure`
flag can be added to ensure it is never transmitted over HTTP and `SameSite=Lax`
to prevent authenticated [CSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery).

```
# requires nginx 1.19.8
proxy_cookie_flags session_id samesite=lax secure;
```

## Odoo as a WSGI Application

It is also possible to mount Odoo as a standard [WSGI](https://wsgi.readthedocs.org/) application. Odoo
provides the base for a WSGI launcher script as `odoo-wsgi.example.py`. That
script should be customized (possibly after copying it from the setup directory) to correctly set the
configuration directly in `odoo.tools.config` rather than through the
command-line or a configuration file.

However the WSGI server will only expose the main HTTP endpoint for the web
client, website and webservice API. Because Odoo does not control the creation
of workers anymore it can not setup cron or livechat workers

### Cron Workers

Starting one of the built-in Odoo servers next to the WSGI server is required to process cron jobs.
That server must be configured to only process crons and not HTTP requests using the
[`--no-http`](../../developer/reference/cli.html#cmdoption-odoo-bin-no-http) cli option or the `http_enable = False` configuration
file setting.

On Linux-like systems, using the multi-processing server over the multi-threading one is recommended
to benefit from better hardware usage and increased stability, i.e., using
the [`--workers=-1`](../../developer/reference/cli.html#cmdoption-odoo-bin-workers) and [`--max-cron-threads=n`](../../developer/reference/cli.html#cmdoption-odoo-bin-max-cron-threads) cli options.

### LiveChat

Using a gevent-compatible WSGI server is required for the correct operation of the live chat
feature. That server should be able to handle many simultaneous long-lived connections but doesn’t
need a lot of processing power. All requests whose path starts with `/websocket/` should be
directed to that server. A regular (thread/process-based) WSGI server should be used for all other
requests.

The Odoo cron server can also be used to serve the live chat requests. Just drop
the [`--no-http`](../../developer/reference/cli.html#cmdoption-odoo-bin-no-http) cli option from the cron server and make sure requests
whose path starts with `/websocket/` are directed to this server, either on
the [`--http-port`](../../developer/reference/cli.html#cmdoption-odoo-bin-http-port) (multi-threading server) or on
the [`--gevent-port`](../../developer/reference/cli.html#cmdoption-odoo-bin-gevent-port) (multi-processing server).

## Serving static files and attachments

For development convenience, Odoo directly serves all static files and attachments in its modules.
This may not be ideal when it comes to performances, and static files should generally be served by
a static HTTP server.

### Serving static files

Odoo static files are located in each module’s `static/` folder, so static files can be served
by intercepting all requests to `/MODULE/static/FILE`, and looking up the right module
(and file) in the various addons paths.

It is recommended to set the `Content-Security-Policy: default-src 'none'` header on all images
delivered by the web server. It is not strictly necessary as users cannot modify/inject content
inside of modules’ `static/` folder and existing images are final (they do not fetch new
resources by themselves). However, it is good practice.

Using the above NGINX (https) configuration, the following `map` and `location` blocks should be
added to serve static files via NGINX.

```
map $sent_http_content_type $content_type_csp {
    default "";
    ~image/ "default-src 'none'";
}

server {
    # the rest of the configuration

    location @odoo {
        # copy-paste the content of the / location block
    }

    # Serve static files right away
    location ~ ^/[^/]+/static/.+$ {
        # root and try_files both depend on your addons paths
        root ...;
        try_files ... @odoo;
        expires 24h;
        add_header Content-Security-Policy $content_type_csp;
    }
}
```

The actual `root` and `try_files` directives are dependant on your installation, specifically on
your [`--addons-path`](../../developer/reference/cli.html#cmdoption-odoo-bin-addons-path).

> **Tip:**
>
> Debian packageGit sources
>
> Say Odoo has been installed via the **debian packages** for Community and Enterprise, and
> that the [`--addons-path`](../../developer/reference/cli.html#cmdoption-odoo-bin-addons-path) is
> `'/usr/lib/python3/dist-packages/odoo/addons'`.
>
> The `root` and `try_files` should be:
>
> ```
> root /usr/lib/python3/dist-packages/odoo/addons;
> try_files $uri @odoo;
> ```
>
> Say Odoo has been installed via the **sources**, that both the Community and Enterprise git
> repositories were cloned in `/opt/odoo/community` and `/opt/odoo/enterprise`
> respectively, and that the [`--addons-path`](../../developer/reference/cli.html#cmdoption-odoo-bin-addons-path) is
> `'/opt/odoo/community/odoo/addons,/opt/odoo/community/addons,/opt/odoo/enterprise'`.
>
> The `root` and `try_files` should be:
>
> ```
> root /opt/odoo;
> try_files /community/odoo/addons$uri /community/addons$uri /enterprise$uri @odoo;
> ```

### Serving attachments

Attachments are files stored in the filestore which access is regulated by Odoo. They cannot be
directly accessed via a static web server as accessing them requires multiple lookups in the
database to determine where the files are stored and whether the current user can access them or
not.

Nevertheless, once the file has been located and the access rights verified by Odoo, it is a good
idea to serve the file using the static web server instead of Odoo. For Odoo to delegate serving
files to the static web server, the [X-Sendfile](https://tn123.org/mod_xsendfile/) (apache) or
[X-Accel](https://www.nginx.com/resources/wiki/start/topics/examples/x-accel/) (nginx) extensions
must be enabled and configured on the static web server. Once it is set up, start Odoo with the
[`--x-sendfile`](../../developer/reference/cli.html#cmdoption-odoo-bin-x-sendfile) CLI flag (this unique flag is used for both
X-Sendfile and X-Accel).

> **Note:**
>
> - The X-Sendfile extension for apache (and compatible web servers) does not require any
>   supplementary configuration.
> - The X-Accel extension for NGINX **does** require the following additionnal configuration:
>
>   ```
>   location /web/filestore {
>       internal;
>       alias /path/to/odoo/data-dir/filestore;
>       add_header Content-Security-Policy $upstream_http_content_security_policy;
>       add_header X-Content-Type-Options nosniff;
>   }
>   ```
>
>   In case you don’t know what is the path to your filestore, start Odoo with the
>   [`--x-sendfile`](../../developer/reference/cli.html#cmdoption-odoo-bin-x-sendfile) option and navigate to the `/web/filestore` URL
>   directly via Odoo (don’t navigate to the URL via NGINX). This logs a warnings, the message
>   contains the configuration you need.

## Security

For starters, keep in mind that securing an information system is a continuous process,
not a one-shot operation. At any moment, you will only be as secure as the weakest link
in your environment.

So please do not take this section as the ultimate list of measures that will prevent
all security problems. It’s only intended as a summary of the first important things
you should be sure to include in your security action plan. The rest will come
from best security practices for your operating system and distribution,
best practices in terms of users, passwords, and access control management, etc.

When deploying an internet-facing server, please be sure to consider the following
security-related topics:

- Always set a strong super-admin admin password, and restrict access to the database
  management pages as soon as the system is set up. See [Database Manager Security].
- Choose unique logins and strong passwords for all administrator accounts on all databases.
  Do not use ‘admin’ as the login. Do not use those logins for day-to-day operations,
  only for controlling/managing the installation.
  *Never* use any default passwords like admin/admin, even for test/staging databases.
- Do **not** install demo data on internet-facing servers. Databases with demo data contain
  default logins and passwords that can be used to get into your systems and cause significant
  trouble, even on staging/dev systems.
- Use appropriate database filters ( [`--db-filter`](../../developer/reference/cli.html#cmdoption-odoo-bin-db-filter))
  to restrict the visibility of your databases according to the hostname.
  See [dbfilter].
  You may also use [`-d`](../../developer/reference/cli.html#cmdoption-odoo-bin-d) to provide your own (comma-separated)
  list of available databases to filter from, instead of letting the system fetch
  them all from the database backend.
- Once your `db_name` and `dbfilter` are configured and only match a single database
  per hostname, you should set `list_db` configuration option to `False`, to prevent
  listing databases entirely, and to block access to the database management screens
  (this is also exposed as the [`--no-database-list`](../../developer/reference/cli.html#cmdoption-odoo-bin-no-database-list)
  command-line option)
- Make sure the PostgreSQL user ([`--db_user`](../../developer/reference/cli.html#cmdoption-odoo-bin-r)) is *not* a super-user,
  and that your databases are owned by a different user. For example they could be owned by
  the `postgres` super-user if you are using a dedicated non-privileged `db_user`.
  See also [Configuring Odoo].
- Keep installations updated by regularly installing the latest builds,
  either via GitHub or by downloading the latest version from
  <https://www.odoo.com/page/download> or <http://nightly.odoo.com>
- Configure your server in multi-process mode with proper limits matching your typical
  usage (memory/CPU/timeouts). See also [Builtin server].
- Run Odoo behind a web server providing HTTPS termination with a valid SSL certificate,
  in order to prevent eavesdropping on cleartext communications. SSL certificates are
  cheap, and many free options exist.
  Configure the web proxy to limit the size of requests, set appropriate timeouts,
  and then enable the [`proxy mode`](../../developer/reference/cli.html#cmdoption-odoo-bin-proxy-mode) option.
  See also [HTTPS].
- If you need to allow remote SSH access to your servers, make sure to set a strong password
  for **all** accounts, not just `root`. It is strongly recommended to entirely disable
  password-based authentication, and only allow public key authentication. Also consider
  restricting access via a VPN, allowing only trusted IPs in the firewall, and/or
  running a brute-force detection system such as `fail2ban` or equivalent.
- Consider installing appropriate rate-limiting on your proxy or firewall, to prevent
  brute-force attacks and denial of service attacks. See also [Blocking Brute Force Attacks]
  for specific measures.

  Many network providers provide automatic mitigation for Distributed Denial of
  Service attacks (DDOS), but this is often an optional service, so you should consult
  with them.
- Whenever possible, host your public-facing demo/test/staging instances on different
  machines than the production ones. And apply the same security precautions as for
  production.
- If your public-facing Odoo server has access to sensitive internal network resources
  or services (e.g. via a private VLAN), implement appropriate firewall rules to
  protect those internal resources. This will ensure that the Odoo server cannot
  be used accidentally (or as a result of malicious user actions) to access or disrupt
  those internal resources.
  Typically this can be done by applying an outbound default DENY rule on the firewall,
  then only explicitly authorizing access to internal resources that the Odoo server
  needs to access.
  [Systemd IP traffic access control](http://0pointer.net/blog/ip-accounting-and-access-lists-with-systemd.html)
  may also be useful to implement per-process network access control.
- If your public-facing Odoo server is behind a Web Application Firewall, a load-balancer,
  a transparent DDoS protection service (like CloudFlare) or a similar network-level
  device, you may wish to avoid direct access to the Odoo system. It is generally
  difficult to keep the endpoint IP addresses of your Odoo servers secret. For example
  they can appear in web server logs when querying public systems, or in the headers
  of emails posted from Odoo.
  In such a situation you may want to configure your firewall so that the endpoints
  are not accessible publicly except from the specific IP addresses of your WAF,
  load-balancer or proxy service. Service providers like CloudFlare usually maintain
  a public list of their IP address ranges for this purpose.
- If you are hosting multiple customers, isolate customer data and files from each other
  using containers or appropriate “jail” techniques.
- Setup daily backups of your databases and filestore data, and copy them to a remote
  archiving server that is not accessible from the server itself.
- Deploying Odoo on Linux is strongly recommended over Windows. Should you choose nevertheless
  to deploy on a Windows platform, a thorough security hardening review of the server should be
  conducted and is outside of the scope of this guide.

### Blocking Brute Force Attacks

For internet-facing deployments, brute force attacks on user passwords are very common, and this
threat should not be neglected for Odoo servers. Odoo emits a log entry whenever a login attempt
is performed, and reports the result: success or failure, along with the target login and source IP.

The log entries will have the following form.

Failed login:

```
2018-07-05 14:56:31,506 24849 INFO db_name odoo.addons.base.res.res_users: Login failed for db:db_name login:admin from 127.0.0.1
```

Successful login:

```
2018-07-05 14:56:31,506 24849 INFO db_name odoo.addons.base.res.res_users: Login successful for db:db_name login:admin from 127.0.0.1
```

These logs can be easily analyzed by an intrusion prevention system such as `fail2ban`.

For example, the following fail2ban filter definition should match a
failed login:

```
[Definition]
failregex = ^ \d+ INFO \S+ \S+ Login failed for db:\S+ login:\S+ from <HOST>
ignoreregex =
```

This could be used with a jail definition to block the attacking IP on HTTP(S).

Here is what it could look like for blocking the IP for 15 minutes when
10 failed login attempts are detected from the same IP within 1 minute:

```
[odoo-login]
enabled = true
port = http,https
bantime = 900  ; 15 min ban
maxretry = 10  ; if 10 attempts
findtime = 60  ; within 1 min  /!\ Should be adjusted with the TZ offset
logpath = /var/log/odoo.log  ;  set the actual odoo log path here
```

### Database Manager Security

[Configuring Odoo] mentioned `admin_passwd` in passing.

This setting is used on all database management screens (to create, delete,
dump or restore databases).

If the management screens must not be accessible at all, you should set `list_db`
configuration option to `False`, to block access to all the database selection and
management screens.

> **Warning:**
>
> It is strongly recommended to disable the Database Manager for any internet-facing
> system! It is meant as a development/demo tool, to make it easy to quickly create
> and manage databases. It is not designed for use in production, and may even expose
> dangerous features to attackers. It is also not designed to handle large databases,
> and may trigger memory limits.
>
> On production systems, database management operations should always be performed by
> the system administrator, including provisioning of new databases and automated backups.

Be sure to setup an appropriate `db_name` parameter
(and optionally, `dbfilter` too) so that the system can determine the target database
for each request, otherwise users will be blocked as they won’t be allowed to choose the
database themselves.

If the management screens must only be accessible from a selected set of machines,
use the proxy server’s features to block access to all routes starting with `/web/database`
except (maybe) `/web/database/selector` which displays the database-selection screen.

If the database-management screen should be left accessible, the
`admin_passwd` setting must be changed from its `admin` default: this
password is checked before allowing database-alteration operations.

It should be stored securely, and should be generated randomly e.g.

```
$ python3 -c 'import base64, os; print(base64.b64encode(os.urandom(24)))'
```

which generates a 32-character pseudorandom printable string.

### Reset the master password

There may be instances where the master password is misplaced, or compromised, and needs to be
reset. The following process is for system administrators of an Odoo on-premise database detailing
how to manually reset and re-encrypt the master password.

> **Note:**
>
> [Odoo.com account](../odoo_accounts.html)

When creating a new on-premise database, a random master password is generated. Odoo recommends
using this password to secure the database. This password is implemented by default, so there is a
secure master password for any Odoo on-premise deployment.

> **Warning:**
>
> When creating an Odoo on-premise database the installation is accessible to anyone on the
> internet, until this password is set to secure the database.

The master password is specified in the Odoo configuration file (`odoo.conf` or `odoorc` (hidden
file)). The Odoo master password is needed to modify, create, or delete a database through the
graphical user interface (GUI).

#### Locate configuration file

First, open the Odoo configuration file (`odoo.conf` or `odoorc` (hidden file)).

WindowsLinux

The configuration file is located at: `c:\ProgramFiles\Odoo{VERSION}\server\odoo.conf`

Depending on how Odoo is installed on the Linux machine, the configuration file is located in
one of two different places:

- Package installation: `/etc/odoo.conf`
- Source installation: `~/.odoorc`

#### Change old password

Once the appropriate file has been opened, proceed to modify the old password in the configuration
file to a temporary password.

Graphical user interfaceCommand-line interface

After locating the configuration file, open it using a (GUI). This can be achieved by simply double clicking on the file. Then, the device
should have a default GUI to open the file with.

Next, modify the master password line `admin_passwd = $pbkdf2-sha…` to `admin_passwd =
newpassword1234`, for example. This password can be anything, as long as it is saved
temporarily. Make sure to modify all characters after the `=`.

> **Tip:**
>
> The line appears like this:
> `admin_passwd =
> $pbkdf2-sh39dji295.59mptrfW.9z6HkA$w9j9AMVmKAP17OosCqDxDv2hjsvzlLpF8Rra8I7p/b573hji540mk/.3ek0lg%kvkol6k983mkf/40fjki79m`
>
> The modified line appears like this: `admin_passwd = newpassword1234`

Modify the master password line using the following Unix command detailed below.

Connect to the Odoo server’s terminal via Secure Shell (SSH) protocol, and edit the
configuration file. To modify the configuration file, enter the following command:
**sudo nano /etc/odoo.conf**

After opening the configuration file, modify the master password line `admin_passwd =
$pbkdf2-sha…` to `admin_passwd = newpassword1234`. This password can be anything, as long as
it is saved temporarily. Make sure to modify all characters after the `=`.

> **Tip:**
>
> The line appears like this:
> `admin_passwd =
> $pbkdf2-sh39dji295.59mptrfW.9z6HkA$w9j9AMVmKAP17OosCqDxDv2hjsvzlLpF8Rra8I7p/b573hji540mk/.3ek0lg%kvkol6k983mkf/40fjki79m`
>
> The modified line appears like this: `admin_passwd = newpassword1234`

> **Warning:**
>
> It is essential that the password is changed to something else, rather than triggering a new
> password reset by adding a semicolon `;` at the beginning of the line. This ensures the database
> is secure throughout the entire password reset process.

#### Restart Odoo server

After setting the temporary password, a restart of the Odoo server is **required**.

Graphical user interfaceCommand-line interface

To restart the Odoo server, first, type `services` into the Windows Search bar.
Then, select the Services application, and scroll down to the Odoo
service.

Next, right click on Odoo, and select Start or Restart.
This action manually restarts the Odoo server.

Restart the Odoo server by typing the command: **sudo service odoo15 restart**

> **Note:**
>
> Change the number after `odoo` to fit the specific version the server is running on.

#### Use web interface to re-encrypt password

First, navigate to `/web/database/manager` or `http://server_ip:port/web/database/manager` in a
browser.

> **Note:**
>
> Replace `server_ip` with the IP address of the database. Replace `port` with the numbered port
> the database is accessible from.

Next, click Set Master Password, and type in the previously-selected temporary password
into the Master Password field. Following this step, type in a New Master
Password. The New Master Password is hashed (or encrypted), once the
Continue button is clicked.

At this point, the password has been successfully reset, and a hashed version of the new password
now appears in the configuration file.

> **Note:**
>
> For more information on Odoo database security, see this documentation:
> [Database Manager Security].

## Supported Browsers

Odoo supports the latest version of the following browsers.

- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Apple Safari

[1]
:   to have multiple Odoo installations use the same PostgreSQL database,
    or to provide more computing resources to both software.

[2]
:   technically a tool like [socat](http://www.dest-unreach.org/socat/) can be used to proxy UNIX sockets across
    networks, but that is mostly for software which can only be used over
    UNIX sockets

[3]
:   or be accessible only over an internal packet-switched network, but that
    requires secured switches, protections against [ARP spoofing](https://en.wikipedia.org/wiki/ARP_spoofing) and
    precludes usage of WiFi. Even over secure packet-switched networks,
    deployment over HTTPS is recommended, and possible costs are lowered as
    “self-signed” certificates are easier to deploy on a controlled
    environment than over the internet.

---

# Email gateway

The Odoo mail gateway allows you to inject directly all the received emails in Odoo.

Its principle is straightforward: your SMTP server executes the “mailgate” script for every new
incoming email.

The script takes care of connecting to your Odoo database through XML-RPC, and send the emails via
the `MailThread.message_process()` feature.

## Prerequisites

- Administrator access to the Odoo database.
- Your own mail server such as Postfix or Exim.
- Technical knowledge on how to configure an email server.

## For Postfix

In you alias config (`/etc/aliases`):

```
email@address: "|/odoo-directory/addons/mail/static/scripts/odoo-mailgate.py -d <database-name> -u <userid> -p <password>"
```

> **Note:**
>
> Resources
>
> - [Postfix](http://www.postfix.org/documentation.html)
> - [Postfix aliases](http://www.postfix.org/aliases.5.html)
> - [Postfix virtual](http://www.postfix.org/virtual.8.html)

## For Exim

```
*: |/odoo-directory/addons/mail/static/scripts/odoo-mailgate.py -d <database-name> -u <userid> -p <password>
```

> **Note:**
>
> Resources
>
> - [Exim](https://www.exim.org/docs.html)

> **Note:**
>
> If you do not have access/manage your email server, use [incoming mail servers](../../applications/general/email_communication/email_servers_inbound.html#email-inbound-custom-domain-incoming-server).

---

# Geo IP

> **Note:**
>
> This documentation only applies to On-premise databases.

## Installation

1. Download both the GeoLite2 City and Country
   [databases](https://dev.maxmind.com/geoip/geoip2/geolite2/). You should end up with two files
   called `GeoLite2-City.mmdb` and `GeoLite2-Country.mmdb`.
2. Move the files to the folder `/usr/share/GeoIP/`.

   ```
   mv ~/Downloads/GeoLite2-City.mmdb /usr/share/GeoIP/
   mv ~/Downloads/GeoLite2-Country.mmdb /usr/share/GeoIP/
   ```
3. Restart the server

> **Note:**
>
> If you don’t want to locate the geoip database in `/usr/share/GeoIP/`, use the
> [`--geoip-city-db`](../../developer/reference/cli.html#cmdoption-odoo-bin-geoip-city-db) and
> [`--geoip-country-db`](../../developer/reference/cli.html#cmdoption-odoo-bin-geoip-country-db) options of the Odoo command line
> interface. These options take the absolute path to the GeoIP database file and use it as the
> GeoIP database. For example:
>
> ```
> ./odoo-bin --geoip-city-db= ~/Downloads/GeoLite2-City.mmdb
> ```
>
> - [CLI documentation](../../developer/reference/cli.html).

## Test GeoIP geolocation in your Odoo website

Edit a web page to include some geo-ip information such as the country name of the current
request IP address. To do so:

1. Go to your website. Open the web page that you want to test `GeoIP`.
2. Choose Customize ‣ HTML/CSS/JS Editor.
3. Add the following piece of XML in the page :

   ```
   <h1 class="text-center" t-esc="request.geoip.country.name or 'geoip failure'"/>
   ```
4. Save and refresh the page.

Geo-ip is working if you read your country name displayed in bold in the middle of the page.

In case you read “**geoip failure**” instead then the geolocalization failed. The common causes are:

1. The browsing IP address is the localhost (`127.0.0.1`) or a local area network one. If you
   don’t know, you can access your website using mobile data.
2. You are using a reverse-proxy (apache, nginx) in front of Odoo but didn’t start Odoo with the
   proxy-mode enabled. See [`proxy mode`](../../developer/reference/cli.html#cmdoption-odoo-bin-proxy-mode).
3. The GeoIP database is corrupt, missing or unaccessible. In such case a warning was logged in the
   server logs.

---

# Switch from Community to Enterprise

Depending on your current installation, there are multiple ways to upgrade
your community version.
In any case the basic guidelines are:

- Backup your community database

  ![../../_images/db_manager.png](../../_images/db_manager.png)
- Shutdown your server
- Install the web\_enterprise module
- Restart your server
- Enter your Odoo Enterprise Subscription code

![../../_images/enterprise_code.png](../../_images/enterprise_code.png)

## On Linux, using an installer

- Backup your community database
- Stop the odoo service

  ```
  $ sudo service odoo stop
  ```
- Install the enterprise .deb (it should install over the community package)

  ```
  $ sudo dpkg -i <path_to_enterprise_deb>
  ```
- Update your database to the enterprise packages using

  ```
  $ python3 /usr/bin/odoo-bin -d <database_name> -i web_enterprise --stop-after-init
  ```
- You should be able to connect to your Odoo Enterprise instance using your usual mean of identification.
  You can then link your database with your Odoo Enterprise Subscription by entering the code you received
  by e-mail in the form input

## On Linux, using the source code

There are many ways to launch your server when using sources, and you probably
have your own favourite. You may need to adapt sections to your usual workflow.

- Shutdown your server
- Backup your community database
- Update the `--addons-path` parameter of your launch command (see [Source install](source.html))
- Install the web\_enterprise module by using

  ```
  $ -d <database_name> -i web_enterprise --stop-after-init
  ```

  Depending on the size of your database, this may take some time.
- Restart your server with the updated addons path of point 3.
  You should be able to connect to your instance. You can then link your database with your
  Odoo Enterprise Subscription by entering the code you received by e-mail in the form input

## On Windows

- Backup your community database
- Uninstall Odoo Community (using the Uninstall executable in the installation folder) -
  PostgreSQL will remain installed

  ![../../_images/windows_uninstall.png](../../_images/windows_uninstall.png)
- Launch the Odoo Enterprise Installer and follow the steps normally. When choosing
  the installation path, you can set the folder of the Community installation
  (this folder still contains the PostgreSQL installation).
  Uncheck `Start Odoo` at the end of the installation

  ![../../_images/windows_setup.png](../../_images/windows_setup.png)
- Using a command window, update your Odoo Database using this command (from the Odoo
  installation path, in the server subfolder)

  ```
  $ ..\python\python.exe odoo-bin -d <database_name> -i web_enterprise --stop-after-init
  ```
- No need to manually launch the server, the service is running.
  You should be able to connect to your Odoo Enterprise instance using your usual
  mean of identification. You can then link your database with your Odoo Enterprise
  Subscription by entering the code you received by e-mail in the form input
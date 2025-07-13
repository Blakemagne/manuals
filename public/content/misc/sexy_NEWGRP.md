# 📚 NEWGRP Manual

> *Beautiful, readable documentation for command-line tools*

---

[NEWGRP(1)](NEWGRP.html)                        User Commands                       [NEWGRP(1)](NEWGRP.html)


## 📑 Table of Contents

- [Name](#name)
  - [Library](#library)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Return Value](#return-value)
  - [Errors](#errors)
  - [Standards](#standards)
  - [History](#history)
- [Examples](#examples)
- [See Also](#see-also)
- [Name](#name)
  - [Library](#library)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Return Value](#return-value)
  - [Errors](#errors)
  - [Standards](#standards)
  - [History](#history)
  - [Notes](#notes)
  - [Bugs](#bugs)
- [See Also](#see-also)
- [Name](#name)
  - [Library](#library)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Return Value](#return-value)
  - [Errors](#errors)
  - [Versions](#versions)
  - [Standards](#standards)
  - [History](#history)
  - [Notes](#notes)
  - [Bugs](#bugs)
- [See Also](#see-also)
- [Name](#name)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Bugs](#bugs)
  - [Author](#author)
  - [Reporting Bugs](#reporting-bugs)
  - [Copyright](#copyright)
- [See Also](#see-also)
- [Name](#name)
  - [Library](#library)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Return Value](#return-value)
  - [Errors](#errors)
  - [Attributes](#attributes)
  - [Standards](#standards)
  - [Posix.1-2008.](#posix.1-2008.)
  - [History](#history)
  - [Notes](#notes)
- [See Also](#see-also)
- [Name](#name)
  - [Library](#library)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Return Value](#return-value)
  - [Errors](#errors)
  - [Standards](#standards)
  - [Posix.1-2008.](#posix.1-2008.)
  - [History](#history)
  - [Posix.1-2001.](#posix.1-2001.)
  - [Notes](#notes)
  - [Bugs](#bugs)
- [See Also](#see-also)
- [Name](#name)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Author](#author)
  - [Reporting Bugs](#reporting-bugs)
  - [Copyright](#copyright)
- [See Also](#see-also)
- [Name](#name)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Author](#author)
  - [Reporting Bugs](#reporting-bugs)
  - [Copyright](#copyright)
- [See Also](#see-also)
- [Name](#name)
- [Synopsis](#synopsis)
- [Description](#description)
- [Options](#options)
- [Authors](#authors)
- [See Also](#see-also)
  - [Reporting Bugs](#reporting-bugs)
  - [Availability](#availability)
- [Name](#name)
  - [Library](#library)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Return Value](#return-value)
  - [Errors](#errors)
  - [Versions](#versions)
  - [Standards](#standards)
  - [Posix.1-2008.](#posix.1-2008.)
  - [History](#history)
  - [Notes](#notes)
- [See Also](#see-also)
- [Name](#name)
- [Synopsis](#synopsis)
- [Description](#description)
- [Files](#files)
- [See Also](#see-also)
- [Name](#name)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Author](#author)
  - [Reporting Bugs](#reporting-bugs)
  - [Copyright](#copyright)
- [See Also](#see-also)
- [Name](#name)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Configuration](#configuration)
- [Files](#files)
- [See Also](#see-also)


## Name {#name}

```
newgrp - log in to a new group
```



## Synopsis {#synopsis}


```
newgrp [-] [group]
```



## Description {#description}

```
The newgrp command is used to change the current group ID during a
login session. If the optional - flag is given, the user's environment
will be reinitialized as though the user had logged in, otherwise the
current environment, including current working directory, remains
unchanged.

newgrp changes the current real group ID to the named group, or to the
default group listed in /etc/passwd if no group name is given.  newgrp
also tries to add the group to the user groupset. If not root, the user
will be prompted for a password if she does not have a password (in
/etc/shadow if this user has an entry in the shadowed password file, or
in /etc/passwd otherwise) and the group does, or if the user is not
listed as a member and the group has a password. The user will be
denied access if the group password is empty and the user is not listed
as a member.

If there is an entry for this group in /etc/gshadow, then the list of
members and the password of this group will be taken from this file,
otherwise, the entry in /etc/group is considered.
```



### Configuration {#configuration}

```
The following configuration variables in /etc/login.defs change the
behavior of this tool:

SYSLOG_SG_ENAB (boolean)
    Enable "syslog" logging of sg activity.
```



### Files {#files}

```
/etc/passwd
    User account information.

/etc/shadow
    Secure user account information.

/etc/group
    Group account information.

/etc/gshadow
    Secure group account information.
```



## See Also {#see-also}

```
id(1), login(1), su(1), sg(1), gpasswd(1), group(5), gshadow(5).
```


shadow-utils 4.13                 05/30/2024                         [NEWGRP(1)](NEWGRP.html)

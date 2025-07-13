# 📚 FGETPWENT Manual

> *Beautiful, readable documentation for command-line tools*

---

[fgetpwent(3)](fgetpwent.html)                                                                              Library Functions Manual                                                                             [fgetpwent(3)](fgetpwent.html)


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
- [Name](#name)
  - [Library](#library)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Return Value](#return-value)
  - [Errors](#errors)
  - [Standards](#standards)
  - [Posix.1-2008.](#posix.1-2008.)
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
- [Files](#files)
  - [Attributes](#attributes)
  - [Standards](#standards)
  - [History](#history)
- [See Also](#see-also)


## Name {#name}

```
fgetpwent - get password file entry
```



### Library {#library}

```
Standard C library (libc, -lc)
```



## Synopsis {#synopsis}

```
#include <stdio.h>
#include <sys/types.h>
#include <pwd.h>

struct passwd *fgetpwent(FILE *stream);
```


   Feature Test Macro Requirements for glibc (see [feature_test_macros(7)](feature_test_macros.html)):

```
fgetpwent():
    Since glibc 2.19:
        _DEFAULT_SOURCE
    glibc 2.19 and earlier:
        _SVID_SOURCE
```



## Description {#description}

```
The fgetpwent() function returns a pointer to a structure containing the broken out fields of a line in the file stream.  The first time it is called it returns the first entry; thereafter, it re‐
turns successive entries.  The file referred to by stream must have the same format as /etc/passwd (see passwd(5)).

The passwd structure is defined in <pwd.h> as follows:

    struct passwd {
        char   *pw_name;       /* username */
        char   *pw_passwd;     /* user password */
        uid_t   pw_uid;        /* user ID */
        gid_t   pw_gid;        /* group ID */
        char   *pw_gecos;      /* real name */
        char   *pw_dir;        /* home directory */
        char   *pw_shell;      /* shell program */
    };
```



### Return Value {#return-value}

```
The fgetpwent() function returns a pointer to a passwd structure, or NULL if there are no more entries or an error occurs.  In the event of an error, errno is set to indicate the error.
```



### Errors {#errors}

```
ENOMEM Insufficient memory to allocate passwd structure.
```



### Files {#files}

```
/etc/passwd
       password database file
```



### Attributes {#attributes}

```
For an explanation of the terms used in this section, see attributes(7).
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬──────────────────────────┐
│ Interface                                                                                                                                             │ Attribute     │ Value                    │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼──────────────────────────┤
│ fgetpwent()                                                                                                                                           │ Thread safety │ MT-Unsafe race:fgetpwent │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴──────────────────────────┘
```



### Standards {#standards}

```
None.
```



### History {#history}

```
SVr4.
```



## See Also {#see-also}

```
endpwent(3), fgetpwent_r(3), fopen(3), getpw(3), getpwent(3), getpwnam(3), getpwuid(3), putpwent(3), setpwent(3), passwd(5)
```


Linux man-pages 6.7                                                                              2023-10-31                                                                                    [fgetpwent(3)](fgetpwent.html)

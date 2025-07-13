# 📚 PTSNAME, Manual

> *Beautiful, readable documentation for command-line tools*

---

[ptsname(3)](ptsname.html)                                                                                Library Functions Manual                                                                               [ptsname(3)](ptsname.html)


## 📑 Table of Contents

- [Name](#name)
- [Synopsis](#synopsis)
- [Description](#description)
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
- [Files](#files)
  - [Attributes](#attributes)
  - [Standards](#standards)
  - [History](#history)
- [See Also](#see-also)
- [Name](#name)
- [Synopsis](#synopsis)
- [Description](#description)
- [Environment](#environment)
- [Files](#files)
- [See Also](#see-also)
- [Authors](#authors)
- [Name](#name)
- [Synopsis](#synopsis)
- [Description](#description)
- [Options](#options)
  - [Exit Codes](#exit-codes)
- [See Also](#see-also)
- [Examples](#examples)
- [Authors](#authors)
  - [Copyright](#copyright)
  - [Notes](#notes)
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
- [Synopsis](#synopsis)
- [Description](#description)
  - [Interactive Commands](#interactive-commands)
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
  - [Notes](#notes)
- [Examples](#examples)
- [See Also](#see-also)
- [Name](#name)
- [Synopsis](#synopsis)
- [Description](#description)
- [Examples](#examples)
  - [Reporting Bugs](#reporting-bugs)
  - [Copyright](#copyright)
- [See Also](#see-also)
- [Name](#name)
- [Synopsis](#synopsis)
- [Description](#description)
- [Options](#options)
  - [Caveats](#caveats)
- [Files](#files)
  - [Exit Values](#exit-values)
- [See Also](#see-also)
- [Name](#name)
- [Synopsis](#synopsis)
- [Description](#description)
- [Options](#options)
  - [Compatibility](#compatibility)
  - [Bugs](#bugs)
- [See Also](#see-also)
  - [Reporting Bugs](#reporting-bugs)
  - [Availability](#availability)
- [Name](#name)
  - [Library](#library)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Attributes](#attributes)
  - [Standards](#standards)
  - [History](#history)
  - [Notes](#notes)
- [See Also](#see-also)
- [Name](#name)
  - [Library](#library)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Return Value](#return-value)
  - [Errors](#errors)
  - [Attributes](#attributes)
  - [Versions](#versions)
  - [Standards](#standards)
  - [History](#history)
- [See Also](#see-also)


## Name {#name}

```
ptsname, ptsname_r - get the name of the slave pseudoterminal
```



### Library {#library}

```
Standard C library (libc, -lc)
```



## Synopsis {#synopsis}

```
#include <stdlib.h>

char *ptsname(int fd);
int ptsname_r(int fd, char buf[.buflen], size_t buflen);
```


   Feature Test Macro Requirements for glibc (see [feature_test_macros(7)](feature_test_macros.html)):

```
ptsname():
    Since glibc 2.24:
        _XOPEN_SOURCE >= 500
    glibc 2.23 and earlier:
        _XOPEN_SOURCE

ptsname_r():
    _GNU_SOURCE
```



## Description {#description}

```
The ptsname() function returns the name of the slave pseudoterminal device corresponding to the master referred to by the file descriptor fd.

The  ptsname_r() function is the reentrant equivalent of ptsname().  It returns the name of the slave pseudoterminal device as a null-terminated string in the buffer pointed to by buf.  The buflen
argument specifies the number of bytes available in buf.
```



### Return Value {#return-value}

```
On success, ptsname() returns a pointer to a string in static storage which will be overwritten by subsequent calls.  This pointer must not be freed.  On failure, NULL is returned.

On success, ptsname_r() returns 0.  On failure, an error number is returned to indicate the error.
```



### Errors {#errors}

```
EINVAL (ptsname_r() only) buf is NULL.  (This error is returned only for glibc 2.25 and earlier.)

ENOTTY fd does not refer to a pseudoterminal master device.

ERANGE (ptsname_r() only) buf is too small.
```



### Attributes {#attributes}

```
For an explanation of the terms used in this section, see attributes(7).
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬────────────────────────┐
│ Interface                                                                                                                                               │ Attribute     │ Value                  │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼────────────────────────┤
│ ptsname()                                                                                                                                               │ Thread safety │ MT-Unsafe race:ptsname │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼────────────────────────┤
│ ptsname_r()                                                                                                                                             │ Thread safety │ MT-Safe                │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴────────────────────────┘
```



### Versions {#versions}

```
A version of ptsname_r() is documented on Tru64 and HP-UX, but on those implementations, -1 is returned on error, with errno set to indicate the error.  Avoid using this function in portable  pro‐
grams.
```



### Standards {#standards}

```
ptsname():
       POSIX.1-2008.

ptsname_r() is a Linux extension, that is proposed for inclusion in the next major revision of POSIX.1 (Issue 8).
```



### History {#history}

```
ptsname():
       POSIX.1-2001.  glibc 2.1.

ptsname() is part of the UNIX 98 pseudoterminal support (see pts(4)).
```



## See Also {#see-also}

```
grantpt(3), posix_openpt(3), ttyname(3), unlockpt(3), pts(4), pty(7)
```


Linux man-pages 6.7                                                                              2023-10-31                                                                                      [ptsname(3)](ptsname.html)

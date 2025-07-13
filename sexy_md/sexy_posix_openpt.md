# 📚 POSIX_OPENPT Manual

> *Beautiful, readable documentation for command-line tools*

---

[posix_openpt(3)](posix_openpt.html)                                                                           Library Functions Manual                                                                          [posix_openpt(3)](posix_openpt.html)


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


## Name {#name}

```
posix_openpt - open a pseudoterminal device
```



### Library {#library}

```
Standard C library (libc, -lc)
```



## Synopsis {#synopsis}

```
#include <stdlib.h>
#include <fcntl.h>

int posix_openpt(int flags);
```


   Feature Test Macro Requirements for glibc (see [feature_test_macros(7)](feature_test_macros.html)):

```
posix_openpt():
    _XOPEN_SOURCE >= 600
```



## Description {#description}

```
The posix_openpt() function opens an unused pseudoterminal master device, returning a file descriptor that can be used to refer to that device.

The flags argument is a bit mask that ORs together zero or more of the following flags:

O_RDWR Open the device for both reading and writing.  It is usual to specify this flag.

O_NOCTTY
       Do not make this device the controlling terminal for the process.
```



### Return Value {#return-value}

```
On  success, posix_openpt() returns a file descriptor (a nonnegative integer) which is the lowest numbered unused file descriptor.  On failure, -1 is returned, and errno is set to indicate the er‐
ror.
```



### Errors {#errors}

```
See open(2).
```



### Attributes {#attributes}

```
For an explanation of the terms used in this section, see attributes(7).
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
│ Interface                                                                                                                                                              │ Attribute     │ Value   │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
│ posix_openpt()                                                                                                                                                         │ Thread safety │ MT-Safe │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘
```



### Standards {#standards}


### Posix.1-2008. {#posix.1-2008.}



### History {#history}

```
glibc 2.2.1.  POSIX.1-2001.

It is part of the UNIX 98 pseudoterminal support (see pts(4)).
```



### Notes {#notes}

```
Some older UNIX implementations that support System V (aka UNIX 98) pseudoterminals don't have this function, but it can be easily implemented by opening the pseudoterminal multiplexor device:

    int
    posix_openpt(int flags)
    {
        return open("/dev/ptmx", flags);
    }

Calling posix_openpt() creates a pathname for the corresponding pseudoterminal slave device.  The pathname of the slave device can be obtained using ptsname(3).  The slave device  pathname  exists
only as long as the master device is open.
```



## See Also {#see-also}

```
open(2), getpt(3), grantpt(3), ptsname(3), unlockpt(3), pts(4), pty(7)
```


Linux man-pages 6.7                                                                              2023-10-31                                                                                 [posix_openpt(3)](posix_openpt.html)

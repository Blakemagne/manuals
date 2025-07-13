# 📚 ULIMIT Manual

> *Beautiful, readable documentation for command-line tools*

---

[ulimit(3)](ulimit.html)                                                                                 Library Functions Manual                                                                                [ulimit(3)](ulimit.html)


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
- [Name](#name)
- [Synopsis](#synopsis)
- [Description](#description)
- [Options](#options)
  - [Caveats](#caveats)
  - [Configuration](#configuration)
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
  - [Library](#library)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Return Value](#return-value)
  - [Errors](#errors)
  - [Versions](#versions)
  - [Standards](#standards)
  - [History](#history)
  - [Notes](#notes)
- [See Also](#see-also)
- [Name](#name)
  - [Library](#library)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Return Value](#return-value)
  - [Attributes](#attributes)
  - [Standards](#standards)
  - [Posix.1-2008.](#posix.1-2008.)
  - [History](#history)
- [Examples](#examples)
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
- [See Also](#see-also)


## Name {#name}

```
ulimit - get and set user limits
```



### Library {#library}

```
Standard C library (libc, -lc)
```



## Synopsis {#synopsis}

```
#include <ulimit.h>

[[deprecated]] long ulimit(int cmd, long newlimit);
```



## Description {#description}

```
Warning: this routine is obsolete.  Use getrlimit(2), setrlimit(2), and sysconf(3) instead.  For the shell command ulimit, see bash(1).

The ulimit() call will get or set some limit for the calling process.  The cmd argument can have one of the following values.

UL_GETFSIZE
       Return the limit on the size of a file, in units of 512 bytes.

UL_SETFSIZE
       Set the limit on the size of a file.

3      (Not implemented for Linux.)  Return the maximum possible address of the data segment.

4      (Implemented but no symbolic constant provided.)  Return the maximum number of files that the calling process can open.
```



### Return Value {#return-value}

```
On success, ulimit() returns a nonnegative value.  On error, -1 is returned, and errno is set to indicate the error.
```



### Errors {#errors}

```
EPERM  An unprivileged process tried to increase a limit.
```



### Attributes {#attributes}

```
For an explanation of the terms used in this section, see attributes(7).
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
│ Interface                                                                                                                                                              │ Attribute     │ Value   │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
│ ulimit()                                                                                                                                                               │ Thread safety │ MT-Safe │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘
```



### Standards {#standards}


### Posix.1-2008. {#posix.1-2008.}



### History {#history}

```
SVr4, POSIX.1-2001.  POSIX.1-2008 marks it as obsolete.
```



## See Also {#see-also}

```
bash(1), getrlimit(2), setrlimit(2), sysconf(3)
```


Linux man-pages 6.7                                                                              2023-10-31                                                                                       [ulimit(3)](ulimit.html)

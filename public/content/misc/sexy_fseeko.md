# 📚 FSEEKO, Manual

> *Beautiful, readable documentation for command-line tools*

---

[fseeko(3)](fseeko.html)                                                                                 Library Functions Manual                                                                                [fseeko(3)](fseeko.html)


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


## Name {#name}

```
fseeko, ftello - seek to or report file position
```



### Library {#library}

```
Standard C library (libc, -lc)
```



## Synopsis {#synopsis}

```
#include <stdio.h>

int fseeko(FILE *stream, off_t offset, int whence);
off_t ftello(FILE *stream);
```


   Feature Test Macro Requirements for glibc (see [feature_test_macros(7)](feature_test_macros.html)):

```
fseeko(), ftello():
    _FILE_OFFSET_BITS == 64 || _POSIX_C_SOURCE >= 200112L
```



## Description {#description}

```
The  fseeko()  and  ftello()  functions are identical to fseek(3) and ftell(3) (see fseek(3)), respectively, except that the offset argument of fseeko() and the return value of ftello() is of type
off_t instead of long.

On some architectures, both off_t and long are 32-bit types, but defining _FILE_OFFSET_BITS with the value 64 (before including any header files) will turn off_t into a 64-bit type.
```



### Return Value {#return-value}

```
On successful completion, fseeko() returns 0, while ftello() returns the current offset.  Otherwise, -1 is returned and errno is set to indicate the error.
```



### Errors {#errors}

```
See the ERRORS in fseek(3).
```



### Attributes {#attributes}

```
For an explanation of the terms used in this section, see attributes(7).
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
│ Interface                                                                                                                                                              │ Attribute     │ Value   │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
│ fseeko(), ftello()                                                                                                                                                     │ Thread safety │ MT-Safe │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘
```



### Standards {#standards}


### Posix.1-2008. {#posix.1-2008.}



### History {#history}

```
glibc 2.1.  POSIX.1-2001, SUSv2.
```



### Notes {#notes}

```
The declarations of these functions can also be obtained by defining the obsolete _LARGEFILE_SOURCE feature test macro.
```



## See Also {#see-also}

```
fseek(3)
```


Linux man-pages 6.7                                                                              2023-10-31                                                                                       [fseeko(3)](fseeko.html)

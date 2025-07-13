# 📚 WMEMMOVE Manual

> *Beautiful, readable documentation for command-line tools*

---

[wmemmove(3)](wmemmove.html)                Library Functions Manual                [wmemmove(3)](wmemmove.html)


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
- [Name](#name)
  - [Library](#library)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Return Value](#return-value)
  - [Attributes](#attributes)
  - [Standards](#standards)
  - [C11, Posix.1-2008.](#c11,-posix.1-2008.)
  - [History](#history)
  - [Posix.1-2001, C99.](#posix.1-2001,-c99.)
- [See Also](#see-also)


## Name {#name}

```
wmemmove - copy an array of wide-characters
```



### Library {#library}

```
Standard C library (libc, -lc)
```



## Synopsis {#synopsis}

```
#include <wchar.h>

wchar_t *wmemmove(wchar_t dest[.n], const wchar_t src[.n], size_t n);
```



## Description {#description}

```
The  wmemmove()  function  is the wide-character equivalent of the mem‐
move(3) function.  It copies n wide characters from the array  starting
at src to the array starting at dest.  The arrays may overlap.

The programmer must ensure that there is room for at least n wide char‐
acters at dest.
```



### Return Value {#return-value}

```
wmemmove() returns dest.
```



### Attributes {#attributes}

```
For  an  explanation  of  the  terms  used in this section, see attrib‐
utes(7).
┌───────────────────────────────────────────┬───────────────┬─────────┐
│ Interface                                 │ Attribute     │ Value   │
├───────────────────────────────────────────┼───────────────┼─────────┤
│ wmemmove()                                │ Thread safety │ MT-Safe │
└───────────────────────────────────────────┴───────────────┴─────────┘
```



### Standards {#standards}


### C11, Posix.1-2008. {#c11,-posix.1-2008.}



### History {#history}


### Posix.1-2001, C99. {#posix.1-2001,-c99.}



## See Also {#see-also}

```
memmove(3), wmemcpy(3)
```


Linux man-pages 6.7               2023-10-31                       [wmemmove(3)](wmemmove.html)

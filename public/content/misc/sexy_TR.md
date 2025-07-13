# 📚 TR Manual

> *Beautiful, readable documentation for command-line tools*

---

[TR(1)](TR.html)                                                                                          User Commands                                                                                          [TR(1)](TR.html)


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


## Name {#name}

```
tr - translate or delete characters
```



## Synopsis {#synopsis}

```
tr [OPTION]... STRING1 [STRING2]
```



## Description {#description}

```
Translate, squeeze, and/or delete characters from standard input, writing to standard output.  STRING1 and STRING2 specify arrays of characters ARRAY1 and ARRAY2 that control the action.
```


       **`-c`**, -C, --complement
              use the complement of ARRAY1

       **`-d`**, --delete
              delete characters in ARRAY1, do not translate

       **`-s`**, --squeeze-repeats
              replace each sequence of a repeated character that is listed in the last specified ARRAY, with a single occurrence of that character

       **`-t`**, --truncate-set1
              first truncate ARRAY1 to length of ARRAY2

       **`--help display`** this help and exit

       **`--version`**
              output version information and exit

```
ARRAYs are specified as strings of characters.  Most represent themselves.  Interpreted sequences are:

\NNN   character with octal value NNN (1 to 3 octal digits)

\\     backslash

\a     audible BEL

\b     backspace

\f     form feed

\n     new line

\r     return

\t     horizontal tab

\v     vertical tab

CHAR1-CHAR2
       all characters from CHAR1 to CHAR2 in ascending order

[CHAR*]
       in ARRAY2, copies of CHAR until length of ARRAY1

[CHAR*REPEAT]
       REPEAT copies of CHAR, REPEAT octal if starting with 0

[:alnum:]
       all letters and digits

[:alpha:]
       all letters

[:blank:]
       all horizontal whitespace

[:cntrl:]
       all control characters

[:digit:]
       all digits

[:graph:]
       all printable characters, not including space

[:lower:]
       all lower case letters

[:print:]
       all printable characters, including space

[:punct:]
       all punctuation characters

[:space:]
       all horizontal or vertical whitespace

[:upper:]
       all upper case letters

[:xdigit:]
       all hexadecimal digits

[=CHAR=]
       all characters which are equivalent to CHAR

Translation occurs if -d is not given and both STRING1 and STRING2 appear.  -t is only significant when translating.  ARRAY2 is extended to length of ARRAY1 by repeating its last character as nec‐
essary.   Excess  characters  of  ARRAY2  are  ignored.   Character classes expand in unspecified order; while translating, [:lower:] and [:upper:] may be used in pairs to specify case conversion.
Squeezing occurs after translation or deletion.
```



### Bugs {#bugs}

```
Full support is available only for safe single-byte locales, in which every possible input byte represents a single character.  The C locale is safe in GNU systems, so you can avoid this issue  in
the shell by running LC_ALL=C tr instead of plain tr.
```



### Author {#author}

```
Written by Jim Meyering.
```



### Reporting Bugs {#reporting-bugs}

```
GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
```



### Copyright {#copyright}

```
Copyright © 2023 Free Software Foundation, Inc.  License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.  There is NO WARRANTY, to the extent permitted by law.
```



## See Also {#see-also}

```
Full documentation <https://www.gnu.org/software/coreutils/tr>
or available locally via: info '(coreutils) tr invocation'
```


GNU coreutils 9.4                                                                                April 2024                                                                                           [TR(1)](TR.html)

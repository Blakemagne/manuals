# 📚 READLINK Manual

> *Beautiful, readable documentation for command-line tools*

---

[READLINK(1)](READLINK.html)                                                                                    User Commands                                                                                    [READLINK(1)](READLINK.html)


## 📑 Table of Contents

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


## Name {#name}

```
readlink - print resolved symbolic links or canonical file names
```



## Synopsis {#synopsis}

```
readlink [OPTION]... FILE...
```



## Description {#description}

```
Note realpath(1) is the preferred command to use for canonicalization functionality.

Print value of a symbolic link or canonical file name
```


       **`-f`**, --canonicalize
              canonicalize by following every symlink in every component of the given name recursively; all but the last component must exist

       **`-e`**, --canonicalize-existing
              canonicalize by following every symlink in every component of the given name recursively, all components must exist

       **`-m`**, --canonicalize-missing
              canonicalize by following every symlink in every component of the given name recursively, without requirements on components existence

       **`-n`**, --no-newline
              do not output the trailing delimiter

       **`-q`**, --quiet

       **`-s`**, --silent
              suppress most error messages (on by default)

       **`-v`**, --verbose
              report error messages

       **`-z`**, --zero
              end each output line with NUL, not newline

       **`--help display`** this help and exit

       **`--version`**
              output version information and exit


### Author {#author}

```
Written by Dmitry V. Levin.
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
readlink(2), realpath(1), realpath(3)

Full documentation <https://www.gnu.org/software/coreutils/readlink>
or available locally via: info '(coreutils) readlink invocation'
```


GNU coreutils 9.4                                                                                April 2024                                                                                     [READLINK(1)](READLINK.html)

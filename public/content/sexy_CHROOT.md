# 📚 CHROOT Manual

> *Beautiful, readable documentation for command-line tools*

---

[CHROOT(8)](CHROOT.html)                                                                                      User Commands                                                                                      [CHROOT(8)](CHROOT.html)


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


## Name {#name}

```
chroot - run command or interactive shell with special root directory
```



## Synopsis {#synopsis}

```
chroot [OPTION] NEWROOT [COMMAND [ARG]...]
chroot OPTION
```



## Description {#description}

```
Run COMMAND with root directory set to NEWROOT.
```


       **`--groups`**=G_LIST
              specify supplementary groups as g1,g2,..,gN

       **`--userspec`**=USER:GROUP
              specify user and group (ID or name) to use

       **`--skip-chdir`**
              do not change working directory to '/'

       **`--help display`** this help and exit

       **`--version`**
              output version information and exit

```
If no command is given, run '"$SHELL" -i' (default: '/bin/sh -i').
```


   Exit status:
```
125    if the chroot command itself fails

126    if COMMAND is found but cannot be invoked

127    if COMMAND cannot be found
```


       -      the exit status of COMMAND otherwise


### Author {#author}

```
Written by Roland McGrath.
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
chroot(2)

Full documentation <https://www.gnu.org/software/coreutils/chroot>
or available locally via: info '(coreutils) chroot invocation'
```


GNU coreutils 9.4                                                                                April 2024                                                                                       [CHROOT(8)](CHROOT.html)

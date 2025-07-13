# 📚 SETSID Manual

> *Beautiful, readable documentation for command-line tools*

---

[SETSID(1)](SETSID.html)                                                                                      User Commands                                                                                      [SETSID(1)](SETSID.html)


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


## Name {#name}

```
setsid - run a program in a new session
```



## Synopsis {#synopsis}

```
setsid [options] program [arguments]
```



## Description {#description}

```
setsid runs a program in a new session. The command calls fork(2) if already a process group leader. Otherwise, it executes a program in the current process. This default behavior is possible to
override by the --fork option.
```



## Options {#options}

       **`-c`**, --ctty
           Set the controlling terminal to the current one.

       **`-f`**, --fork
           Always create a new process.

       **`-w`**, --wait
           Wait for the execution of the program to end, and return the exit status of this program as the exit status of setsid.

       **`-V`**, --version
           Display version information and exit.

       **`-h`**, --help
           Display help text and exit.


### Authors {#authors}

```
Rick Sladkey <jrs@world.std.com>
```



## See Also {#see-also}

```
setsid(2)
```



### Reporting Bugs {#reporting-bugs}

```
For bug reports, use the issue tracker at https://github.com/util-linux/util-linux/issues.
```



### Availability {#availability}

```
The setsid command is part of the util-linux package which can be downloaded from Linux Kernel Archive <https://www.kernel.org/pub/linux/utils/util-linux/>.
```


util-linux 2.39.3                                                                                2023-10-23                                                                                       [SETSID(1)](SETSID.html)

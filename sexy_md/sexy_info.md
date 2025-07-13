# 📚 INFO Manual

> *Beautiful, readable documentation for command-line tools*

---

[INFO(1)](INFO.html)                                                                                        User Commands                                                                                        [INFO(1)](INFO.html)


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


## Name {#name}

```
info - read Info documents
```



## Synopsis {#synopsis}

```
info [OPTION]... [MENU-ITEM...]
```



## Description {#description}

```
Read documentation in Info format.
```


   Frequently-used options:
       **`-a`**, --all
              use all matching manuals

       **`-k`**, --apropos=STRING
              look up STRING in all indices of all manuals

       **`-d`**, --directory=DIR
              add DIR to INFOPATH

       **`-f`**, --file=MANUAL
              specify Info manual to visit

       **`-h`**, --help
              display this help and exit

       **`--index-search`**=STRING
              go to node pointed by index entry STRING

       **`-n`**, --node=NODENAME
              specify nodes in first visited Info file

       **`-o`**, --output=FILE
              output selected nodes to FILE

       **`--subnodes`**
              recursively output menu items

       **`-v`**, --variable VAR=VALUE
              assign VALUE to Info variable VAR

       **`--version`**
              display version information and exit

       **`-w`**, --where, --location
              print physical location of Info file

```
The  first  non-option argument, if present, is the menu entry to start from; it is searched for in all 'dir' files along INFOPATH.  If it is not present, info merges all 'dir' files and shows the
result.  Any remaining arguments are treated as the names of menu items relative to the initial node visited.

For a summary of key bindings, type H within Info.
```



## Examples {#examples}

```
info   show top-level dir menu

info info-stnd
       show the manual for this Info program

info emacs
       start at emacs node from top-level dir

info emacs buffers
       select buffers menu entry in emacs manual

info emacs -n Files
       start at Files node within emacs manual

info '(emacs)Files'
       alternative way to start at Files node

info --subnodes -o out.txt emacs
       dump entire emacs manual to out.txt

info -f ./foo.info
       show file ./foo.info, not searching dir
```



### Reporting Bugs {#reporting-bugs}

```
Email bug reports to bug-texinfo@gnu.org, general questions and discussion to help-texinfo@gnu.org.
Texinfo home page: http://www.gnu.org/software/texinfo/
```



### Copyright {#copyright}

```
Copyright © 2023 Free Software Foundation, Inc.  License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.  There is NO WARRANTY, to the extent permitted by law.
```



## See Also {#see-also}

```
The full documentation for info is maintained as a Texinfo manual.  If the info program is properly installed at your site, the command

       info info

should give you access to the complete manual.  (Or, if you have Emacs, M-x info will lead to the manual.)
```


GNU texinfo 7.1                                                                                 October 2023                                                                                        [INFO(1)](INFO.html)

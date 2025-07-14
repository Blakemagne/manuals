# 📚 SSH-ARGV0 Manual

> *Beautiful, readable documentation for command-line tools*

---

[SSH-ARGV0(1)](SSH-ARGV0.html)                General Commands Manual               [SSH-ARGV0(1)](SSH-ARGV0.html)


## 📑 Table of Contents

- [Name](#name)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Interactive Commands](#interactive-commands)
- [See Also](#see-also)
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
- [Synopsis](#synopsis)
- [Description](#description)
- [Files](#files)
- [Examples](#examples)
- [See Also](#see-also)
- [Authors](#authors)
- [Name](#name)
  - [Library](#library)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Return Value](#return-value)
  - [Errors](#errors)
  - [Attributes](#attributes)
  - [Versions](#versions)
  - [Versions](#versions)
  - [Standards](#standards)
  - [History](#history)
  - [Notes](#notes)
  - [Bugs](#bugs)
- [See Also](#see-also)
- [Name](#name)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Default Key Bindings](#default-key-bindings)
  - [Command Parsing And Execution](#command-parsing-and-execution)
  - [Parsing Syntax](#parsing-syntax)
  - [Commands](#commands)
  - [Clients And Sessions](#clients-and-sessions)
  - [Windows And Panes](#windows-and-panes)
  - [Key Bindings](#key-bindings)
- [Options](#options)
  - [Hooks](#hooks)
  - [Mouse Support](#mouse-support)
  - [Formats](#formats)
  - [Styles](#styles)
  - [Names And Titles](#names-and-titles)
  - [Global And Session Environment](#global-and-session-environment)
  - [Status Line](#status-line)
  - [Buffers](#buffers)
  - [Miscellaneous](#miscellaneous)
  - [Exit Messages](#exit-messages)
  - [Terminfo Extensions](#terminfo-extensions)
  - [Control Mode](#control-mode)
- [Environment](#environment)
- [Files](#files)
- [Examples](#examples)
- [See Also](#see-also)
- [Authors](#authors)
- [Name](#name)
- [Synopsis](#synopsis)
- [Description](#description)
- [Examples](#examples)
  - [Author](#author)
  - [Reporting Bugs](#reporting-bugs)
  - [Copyright](#copyright)
- [See Also](#see-also)
- [Name](#name)
  - [Library](#library)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Return Value](#return-value)
- [Environment](#environment)
  - [Attributes](#attributes)
  - [Standards](#standards)
  - [History](#history)
  - [Notes](#notes)
  - [Bugs](#bugs)
- [Examples](#examples)
- [See Also](#see-also)
- [Name](#name)
  - [Library](#library)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Return Value](#return-value)
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
  - [Posix.1-2008.](#posix.1-2008.)
  - [History](#history)
  - [Posix.1-2001, Posix.2.](#posix.1-2001,-posix.2.)
  - [Notes](#notes)
  - [Bugs](#bugs)
- [Examples](#examples)
- [See Also](#see-also)
- [Name](#name)
- [Synopsis](#synopsis)
- [Description](#description)
- [Options](#options)
- [Files](#files)
- [Authors](#authors)
- [See Also](#see-also)


## Name {#name}

```
ssh-argv0 — replaces the old ssh command-name as hostname handling
```



## Synopsis {#synopsis}

```
hostname | user@hostname [-l login_name] [command]

hostname   |  user@hostname  [-afgknqstvxACNTX1246]  [-b  bind_address]
[-c cipher_spec] [-e escape_char] [-i  identity_file]  [-l  login_name]
[-m   mac_spec]   [-o   option]   [-p   port]   [-F   configfile]   [-L
port:host:hostport] [-R port:host:hostport] [-D port] [command]
```



## Description {#description}

```
ssh-argv0 replaces the old ssh command-name as hostname  handling.   If
you  link  to  this  script  with a hostname then executing the link is
equivalent to having executed ssh with that hostname  as  an  argument.
All other arguments are passed to ssh and will be processed normally.
```



## Options {#options}

```
See ssh(1).
```



### Files {#files}

```
See ssh(1).
```



### Authors {#authors}

```
OpenSSH  is a derivative of the original and free ssh 1.2.12 release by
Tatu Ylonen.  Aaron Campbell, Bob Beck, Markus  Friedl,  Niels  Provos,
Theo  de  Raadt and Dug Song removed many bugs, re-added newer features
and created OpenSSH.  Markus Friedl contributed  the  support  for  SSH
protocol  versions  1.5  and  2.0.   Natalie Amery wrote this ssh-argv0
script and the associated documentation.
```



## See Also {#see-also}

```
ssh(1)
```


Debian Project                 September 7, 2001                  [SSH-ARGV0(1)](SSH-ARGV0.html)

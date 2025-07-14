# 📚 TTY Manual

> *Beautiful, readable documentation for command-line tools*

---

[TTY(1)](TTY.html)                           User Commands                          [TTY(1)](TTY.html)


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
- [Environment](#environment)
- [Files](#files)
  - [Exit Status](#exit-status)
- [See Also](#see-also)
- [Authors](#authors)
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
  - [Moduli Generation](#moduli-generation)
  - [Certificates](#certificates)
  - [Fido Authenticator](#fido-authenticator)
  - [Key Revocation Lists](#key-revocation-lists)
  - [Allowed Signers](#allowed-signers)
- [Environment](#environment)
  - [Ssh_Sk_Provider](#ssh_sk_provider)
- [Files](#files)
- [See Also](#see-also)
- [Authors](#authors)
- [Name](#name)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Exit Status](#exit-status)
- [Environment](#environment)
- [Files](#files)
- [See Also](#see-also)
  - [History](#history)
  - [Bugs](#bugs)
- [Name](#name)
  - [Library](#library)
- [Synopsis](#synopsis)
- [Description](#description)
  - [Return Value](#return-value)
  - [Errors](#errors)
  - [Note](#note)
- [Files](#files)
  - [Attributes](#attributes)
  - [Versions](#versions)
  - [Standards](#standards)
  - [Posix.1-2008.](#posix.1-2008.)
  - [History](#history)
  - [Notes](#notes)
- [Examples](#examples)
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
tty - print the file name of the terminal connected to standard input
```



## Synopsis {#synopsis}

```
tty [OPTION]...
```



## Description {#description}

```
Print the file name of the terminal connected to standard input.
```


       `-s`, --silent, --quiet
              print nothing, only return an exit status

       `--help display` this help and exit

       `--version`
              output version information and exit


### Author {#author}

```
Written by David MacKenzie.
```



### Reporting Bugs {#reporting-bugs}

```
GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
```



### Copyright {#copyright}

```
Copyright  ©  2023  Free Software Foundation, Inc.  License GPLv3+: GNU
GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free  to  change  and  redistribute  it.
There is NO WARRANTY, to the extent permitted by law.
```



## See Also {#see-also}

```
Full documentation <https://www.gnu.org/software/coreutils/tty>
or available locally via: info '(coreutils) tty invocation'
```


GNU coreutils 9.4                 April 2024                            [TTY(1)](TTY.html)

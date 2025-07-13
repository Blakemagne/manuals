# 📚 XDG-OPEN Manual

> *Beautiful, readable documentation for command-line tools*

---

[XDG-OPEN(1)](XDG-OPEN.html)                                                                                   xdg-open Manual                                                                                   [XDG-OPEN(1)](XDG-OPEN.html)


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


## Name {#name}

```
xdg-open - opens a file or URL in the user's preferred application
```



## Synopsis {#synopsis}


```
xdg-open {file | URL}

xdg-open {--help | --manual | --version}
```



## Description {#description}

```
xdg-open opens a file or URL in the user's preferred application. If a URL is provided the URL will be opened in the user's preferred web browser. If a file is provided the file will be opened in
the preferred application for files of that type. xdg-open supports file, ftp, http and https URLs.

xdg-open is for use inside a desktop session only. It is not recommended to use xdg-open as root.
```



## Options {#options}

       **`--help`**
           Show command synopsis.

       **`--manual`**
           Show this manual page.

       **`--version`**
           Show the xdg-utils version information.


### Exit Codes {#exit-codes}

```
An exit code of 0 indicates success while a non-zero exit code indicates failure. The following failure codes can be returned:

1
    Error in command line syntax.

2
    One of the files passed on the command line did not exist.

3
    A required tool could not be found.

4
    The action failed.
```



## See Also {#see-also}

```
xdg-mime(1), xdg-settings(1), MIME applications associations specification[1]
```



## Examples {#examples}

```
xdg-open 'http://www.freedesktop.org/'

```

```
Opens the freedesktop.org website in the user's default browser.

    xdg-open /tmp/foobar.png

Opens the PNG image file /tmp/foobar.png in the user's default image viewing application.
```



### Authors {#authors}

```
Kevin Krammer
    Author.

Jeremy White
    Author.
```



### Copyright {#copyright}

```
Copyright © 2006
```



### Notes {#notes}

        1. MIME applications associations specification
           http://www.freedesktop.org/wiki/Specifications/mime-apps-spec/

xdg-utils 1.0                                                                                    08/01/2022                                                                                     [XDG-OPEN(1)](XDG-OPEN.html)

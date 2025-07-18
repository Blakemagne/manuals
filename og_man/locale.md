locale(1)                   General Commands Manual                  locale(1)

NAME
       locale - get locale-specific information

SYNOPSIS
       locale [option]
       locale [option] -a
       locale [option] -m
       locale [option] name...

DESCRIPTION
       The  locale  command  displays information about the current locale, or
       all locales, on standard output.

       When invoked without arguments, locale displays the current locale set‐
       tings for each locale category (see locale(5)), based on  the  settings
       of  the  environment variables that control the locale (see locale(7)).
       Values for variables set in the environment are printed without  double
       quotes, implied values are printed with double quotes.

       If  either the -a or the -m option (or one of their long-format equiva‐
       lents) is specified, the behavior is as follows:

       --all-locales
       -a     Display a list of all available locales.  The -v  option  causes
              the  LC_IDENTIFICATION metadata about each locale to be included
              in the output.

       --charmaps
       -m     Display  the  available  charmaps  (character  set   description
              files).   To  display  the current character set for the locale,
              use locale -c charmap.

       The locale command can also be provided with  one  or  more  arguments,
       which  are  the  names  of  locale  keywords  (for  example,  date_fmt,
       ctype-class-names, yesexpr, or decimal_point) or locale categories (for
       example, LC_CTYPE or LC_TIME).  For each  argument,  the  following  is
       displayed:

       •  For a locale keyword, the value of that keyword to be displayed.

       •  For  a  locale category, the values of all keywords in that category
          are displayed.

       When arguments are supplied, the following options are meaningful:

       --category-name
       -c     For a category name argument, write the name of the locale cate‐
              gory on a separate line preceding the list of keyword values for
              that category.

              For a keyword name argument, write the name of the locale  cate‐
              gory  for  this keyword on a separate line preceding the keyword
              value.

              This option improves readability when  multiple  name  arguments
              are specified.  It can be combined with the -k option.

       --keyword-name
       -k     For  each  keyword  whose value is being displayed, include also
              the name of that keyword, so that the output has the format:

                  keyword="value"

       The locale command also knows about the following options:

       --verbose
       -v     Display additional information for some command-line option  and
              argument combinations.

       --help
       -?     Display  a  summary  of  command-line  options and arguments and
              exit.

       --usage
              Display a short usage message and exit.

       --version
       -V     Display the program version and exit.

FILES
       /usr/lib/locale/locale-archive
              Usual default locale archive location.

       /usr/share/i18n/locales
              Usual default path for locale definition files.

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001.

EXAMPLES
       $ locale
       LANG=en_US.UTF-8
       LC_CTYPE="en_US.UTF-8"
       LC_NUMERIC="en_US.UTF-8"
       LC_TIME="en_US.UTF-8"
       LC_COLLATE="en_US.UTF-8"
       LC_MONETARY="en_US.UTF-8"
       LC_MESSAGES="en_US.UTF-8"
       LC_PAPER="en_US.UTF-8"
       LC_NAME="en_US.UTF-8"
       LC_ADDRESS="en_US.UTF-8"
       LC_TELEPHONE="en_US.UTF-8"
       LC_MEASUREMENT="en_US.UTF-8"
       LC_IDENTIFICATION="en_US.UTF-8"
       LC_ALL=

       $ locale date_fmt
       %a %b %e %H:%M:%S %Z %Y

       $ locale -k date_fmt
       date_fmt="%a %b %e %H:%M:%S %Z %Y"

       $ locale -ck date_fmt
       LC_TIME
       date_fmt="%a %b %e %H:%M:%S %Z %Y"

       $ locale LC_TELEPHONE
       +%c (%a) %l
       (%a) %l
       11
       1
       UTF-8

       $ locale -k LC_TELEPHONE
       tel_int_fmt="+%c (%a) %l"
       tel_dom_fmt="(%a) %l"
       int_select="11"
       int_prefix="1"
       telephone-codeset="UTF-8"

       The following example compiles a custom locale from the ./wrk directory
       with the localedef(1) utility under the $HOME/.locale  directory,  then
       tests  the  result with the date(1) command, and then sets the environ‐
       ment variables LOCPATH and LANG in the shell profile file so  that  the
       custom locale will be used in the subsequent user sessions:

       $ mkdir -p $HOME/.locale
       $ I18NPATH=./wrk/ localedef -f UTF-8 -i fi_SE $HOME/.locale/fi_SE.UTF-8
       $ LOCPATH=$HOME/.locale LC_ALL=fi_SE.UTF-8 date
       $ echo "export LOCPATH=\$HOME/.locale" >> $HOME/.bashrc
       $ echo "export LANG=fi_SE.UTF-8" >> $HOME/.bashrc

SEE ALSO
       localedef(1), charmap(5), locale(5), locale(7)

Linux man-pages 6.7               2023-10-31                         locale(1)

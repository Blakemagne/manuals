DIRNAME(1)                       User Commands                      DIRNAME(1)

NAME
       dirname - strip last component from file name

SYNOPSIS
       dirname [OPTION] NAME...

DESCRIPTION
       Output each NAME with its last non-slash component and trailing slashes
       removed;  if  NAME contains no /'s, output '.' (meaning the current di‐
       rectory).

       -z, --zero
              end each output line with NUL, not newline

       --help display this help and exit

       --version
              output version information and exit

EXAMPLES
       dirname /usr/bin/
              -> "/usr"

       dirname dir1/str dir2/str
              -> "dir1" followed by "dir2"

       dirname stdio.h
              -> "."

AUTHOR
       Written by David MacKenzie and Jim Meyering.

REPORTING BUGS
       GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
       Report any translation bugs to <https://translationproject.org/team/>

COPYRIGHT
       Copyright © 2023 Free Software Foundation, Inc.   License  GPLv3+:  GNU
       GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
       This  is  free  software:  you  are free to change and redistribute it.
       There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       basename(1), readlink(1)

       Full documentation <https://www.gnu.org/software/coreutils/dirname>
       or available locally via: info '(coreutils) dirname invocation'

GNU coreutils 9.4                 April 2024                        DIRNAME(1)

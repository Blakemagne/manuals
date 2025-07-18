SSH-ARGV0(1)                General Commands Manual               SSH-ARGV0(1)

NAME
       ssh-argv0 — replaces the old ssh command-name as hostname handling

SYNOPSIS
       hostname | user@hostname [-l login_name] [command]

       hostname   |  user@hostname  [-afgknqstvxACNTX1246]  [-b  bind_address]
       [-c cipher_spec] [-e escape_char] [-i  identity_file]  [-l  login_name]
       [-m   mac_spec]   [-o   option]   [-p   port]   [-F   configfile]   [-L
       port:host:hostport] [-R port:host:hostport] [-D port] [command]

DESCRIPTION
       ssh-argv0 replaces the old ssh command-name as hostname  handling.   If
       you  link  to  this  script  with a hostname then executing the link is
       equivalent to having executed ssh with that hostname  as  an  argument.
       All other arguments are passed to ssh and will be processed normally.

OPTIONS
       See ssh(1).

FILES
       See ssh(1).

AUTHORS
       OpenSSH  is a derivative of the original and free ssh 1.2.12 release by
       Tatu Ylonen.  Aaron Campbell, Bob Beck, Markus  Friedl,  Niels  Provos,
       Theo  de  Raadt and Dug Song removed many bugs, re-added newer features
       and created OpenSSH.  Markus Friedl contributed  the  support  for  SSH
       protocol  versions  1.5  and  2.0.   Natalie Amery wrote this ssh-argv0
       script and the associated documentation.

SEE ALSO
       ssh(1)

Debian Project                 September 7, 2001                  SSH-ARGV0(1)

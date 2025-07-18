SFTP(1)                     General Commands Manual                    SFTP(1)

NAME
       sftp — OpenSSH secure file transfer

SYNOPSIS
       sftp   [-46AaCfNpqrv]  [-B  buffer_size]  [-b  batchfile]  [-c  cipher]
            [-D  sftp_server_command]  [-F  ssh_config]   [-i   identity_file]
            [-J   destination]   [-l   limit]   [-o   ssh_option]   [-P  port]
            [-R  num_requests]  [-S  program]  [-s  subsystem  |  sftp_server]
            [-X sftp_option] destination

DESCRIPTION
       sftp  is a file transfer program, similar to ftp(1), which performs all
       operations over an encrypted ssh(1) transport.  It may  also  use  many
       features of ssh, such as public key authentication and compression.

       The  destination  may be specified either as [user@]host[:path] or as a
       URI in the form sftp://[user@]host[:port][/path].

       If the destination includes a path and it is not a directory, sftp will
       retrieve files automatically if a non-interactive authentication method
       is used; otherwise it will do so after successful interactive authenti‐
       cation.

       If no path is specified, or if the path is a directory, sftp  will  log
       in  to  the specified host and enter interactive command mode, changing
       to the remote directory if one was  specified.   An  optional  trailing
       slash can be used to force the path to be interpreted as a directory.

       Since  the  destination  formats  use  colon characters to delimit host
       names from path names or port numbers, IPv6 addresses must be  enclosed
       in square brackets to avoid ambiguity.

       The options are as follows:

       -4      Forces sftp to use IPv4 addresses only.

       -6      Forces sftp to use IPv6 addresses only.

       -A      Allows  forwarding  of  ssh-agent(1) to the remote system.  The
               default is not to forward an authentication agent.

       -a      Attempt to continue interrupted transfers rather than overwrit‐
               ing existing partial or complete copies of files.  If the  par‐
               tial contents differ from those being transferred, then the re‐
               sultant file is likely to be corrupt.

       -B buffer_size
               Specify the size of the buffer that sftp uses when transferring
               files.  Larger buffers require fewer round trips at the cost of
               higher memory consumption.  The default is 32768 bytes.

       -b batchfile
               Batch  mode  reads a series of commands from an input batchfile
               instead of stdin.  Since it lacks user interaction,  it  should
               be  used  in conjunction with non-interactive authentication to
               obviate the need to enter a password at  connection  time  (see
               sshd(8) and ssh-keygen(1) for details).

               A  batchfile  of  ‘-’  may  be used to indicate standard input.
               sftp will abort if any of the  following  commands  fail:  get,
               put,  reget,  reput,  rename, ln, rm, mkdir, chdir, ls, lchdir,
               copy, cp, chmod, chown, chgrp, lpwd, df, symlink, and lmkdir.

               Termination on error can be suppressed on a command by  command
               basis  by prefixing the command with a ‘-’ character (for exam‐
               ple, -rm /tmp/blah*).  Echo of the command may be suppressed by
               prefixing the command with a ‘@’ character.  These two prefixes
               may be combined in any order, for example -@ls /bsd.

       -C      Enables compression (via ssh's -C flag).

       -c cipher
               Selects the cipher to use for encrypting  the  data  transfers.
               This option is directly passed to ssh(1).

       -D sftp_server_command
               Connect  directly  to  a  local  sftp  server  (rather than via
               ssh(1)).  A command and arguments may be specified, for example
               "/path/sftp-server -el debug3".  This option may be  useful  in
               debugging the client and server.

       -F ssh_config
               Specifies   an  alternative  per-user  configuration  file  for
               ssh(1).  This option is directly passed to ssh(1).

       -f      Requests that files be flushed to disk immediately after trans‐
               fer.  When uploading files, this feature is only enabled if the
               server implements the "fsync@openssh.com" extension.

       -i identity_file
               Selects the file from which the identity (private key) for pub‐
               lic key authentication is read.  This option is directly passed
               to ssh(1).

       -J destination
               Connect to the target host by first making an  sftp  connection
               to the jump host described by destination and then establishing
               a  TCP forwarding to the ultimate destination from there.  Mul‐
               tiple jump hops may be specified separated by comma characters.
               This is a shortcut to specify a ProxyJump configuration  direc‐
               tive.  This option is directly passed to ssh(1).

       -l limit
               Limits the used bandwidth, specified in Kbit/s.

       -N      Disables  quiet  mode, e.g. to override the implicit quiet mode
               set by the -b flag.

       -o ssh_option
               Can be used to pass options  to  ssh  in  the  format  used  in
               ssh_config(5).  This is useful for specifying options for which
               there  is  no separate sftp command-line flag.  For example, to
               specify an alternate port use: sftp -oPort=24.   For  full  de‐
               tails  of  the options listed below, and their possible values,
               see ssh_config(5).

                     AddressFamily
                     BatchMode
                     BindAddress
                     BindInterface
                     CanonicalDomains
                     CanonicalizeFallbackLocal
                     CanonicalizeHostname
                     CanonicalizeMaxDots
                     CanonicalizePermittedCNAMEs
                     CASignatureAlgorithms
                     CertificateFile
                     CheckHostIP
                     Ciphers
                     Compression
                     ConnectionAttempts
                     ConnectTimeout
                     ControlMaster
                     ControlPath
                     ControlPersist
                     GlobalKnownHostsFile
                     GSSAPIAuthentication
                     GSSAPIDelegateCredentials
                     HashKnownHosts
                     Host
                     HostbasedAcceptedAlgorithms
                     HostbasedAuthentication
                     HostKeyAlgorithms
                     HostKeyAlias
                     Hostname
                     IdentitiesOnly
                     IdentityAgent
                     IdentityFile
                     IPQoS
                     KbdInteractiveAuthentication
                     KbdInteractiveDevices
                     KexAlgorithms
                     KnownHostsCommand
                     LogLevel
                     MACs
                     NoHostAuthenticationForLocalhost
                     NumberOfPasswordPrompts
                     PasswordAuthentication
                     PKCS11Provider
                     Port
                     PreferredAuthentications
                     ProxyCommand
                     ProxyJump
                     PubkeyAcceptedAlgorithms
                     PubkeyAuthentication
                     RekeyLimit
                     RequiredRSASize
                     SendEnv
                     ServerAliveInterval
                     ServerAliveCountMax
                     SetEnv
                     StrictHostKeyChecking
                     TCPKeepAlive
                     UpdateHostKeys
                     User
                     UserKnownHostsFile
                     VerifyHostKeyDNS

       -P port
               Specifies the port to connect to on the remote host.

       -p      Preserves modification times, access times, and modes from  the
               original files transferred.

       -q      Quiet  mode: disables the progress meter as well as warning and
               diagnostic messages from ssh(1).

       -R num_requests
               Specify how many requests may be outstanding at any  one  time.
               Increasing  this  may  slightly improve file transfer speed but
               will increase memory usage.  The default is 64 outstanding  re‐
               quests.

       -r      Recursively  copy  entire  directories when uploading and down‐
               loading.  Note that sftp does not follow symbolic links encoun‐
               tered in the tree traversal.

       -S program
               Name of the program to use for the encrypted  connection.   The
               program must understand ssh(1) options.

       -s subsystem | sftp_server
               Specifies  the SSH2 subsystem or the path for an sftp server on
               the remote host.  A path is useful when the remote sshd(8) does
               not have an sftp subsystem configured.

       -v      Raise logging level.  This option is also passed to ssh.

       -X sftp_option
               Specify an option that controls aspects of SFTP protocol behav‐
               iour.  The valid options are:

               nrequests=value
                       Controls how many concurrent SFTP  read  or  write  re‐
                       quests may be in progress at any point in time during a
                       download  or upload.  By default 64 requests may be ac‐
                       tive concurrently.

               buffer=value
                       Controls the maximum buffer  size  for  a  single  SFTP
                       read/write  operation  used  during download or upload.
                       By default a 32KB buffer is used.

INTERACTIVE COMMANDS
       Once in interactive mode, sftp understands a set of commands similar to
       those of ftp(1).  Commands are case insensitive.  Pathnames  that  con‐
       tain  spaces  must  be enclosed in quotes.  Any special characters con‐
       tained within pathnames that are recognized by glob(3) must be  escaped
       with backslashes (‘\’).

       bye     Quit sftp.

       cd [path]
               Change  remote  directory  to  path.  If path is not specified,
               then change directory to the one the session started in.

       chgrp [-h] grp path
               Change group of file path to grp.   path  may  contain  glob(7)
               characters and may match multiple files.  grp must be a numeric
               GID.

               If  the  -h  flag  is specified, then symlinks will not be fol‐
               lowed.  Note that this is only supported by servers that imple‐
               ment the "lsetstat@openssh.com" extension.

       chmod [-h] mode path
               Change permissions of file path  to  mode.   path  may  contain
               glob(7) characters and may match multiple files.

               If  the  -h  flag  is specified, then symlinks will not be fol‐
               lowed.  Note that this is only supported by servers that imple‐
               ment the "lsetstat@openssh.com" extension.

       chown [-h] own path
               Change owner of file path to own.   path  may  contain  glob(7)
               characters and may match multiple files.  own must be a numeric
               UID.

               If  the  -h  flag  is specified, then symlinks will not be fol‐
               lowed.  Note that this is only supported by servers that imple‐
               ment the "lsetstat@openssh.com" extension.

       copy oldpath newpath
               Copy remote file from oldpath to newpath.

               Note that this is only supported by servers that implement  the
               "copy-data" extension.

       cp oldpath newpath
               Alias to copy command.

       df [-hi] [path]
               Display  usage  information for the filesystem holding the cur‐
               rent directory (or path if specified).  If the -h flag is spec‐
               ified, the capacity information will be displayed using "human-
               readable" suffixes.  The -i flag requests display of inode  in‐
               formation in addition to capacity information.  This command is
               only     supported    on    servers    that    implement    the
               “statvfs@openssh.com” extension.

       exit    Quit sftp.

       get [-afpR] remote-path [local-path]
               Retrieve the remote-path and store it on the local machine.  If
               the local path name is not specified, it is given the same name
               it has on the remote machine.  remote-path may contain  glob(7)
               characters  and  may  match  multiple  files.   If  it does and
               local-path is specified, then local-path must specify a  direc‐
               tory.

               If  the  -a  flag  is specified, then attempt to resume partial
               transfers of existing files.  Note that resumption assumes that
               any partial copy of the local file matches the remote copy.  If
               the remote file contents differ from  the  partial  local  copy
               then the resultant file is likely to be corrupt.

               If the -f flag is specified, then fsync(2) will be called after
               the file transfer has completed to flush the file to disk.

               If the -p flag is specified, then full file permissions and ac‐
               cess times are copied too.

               If the -R flag is specified then directories will be copied re‐
               cursively.   Note that sftp does not follow symbolic links when
               performing recursive transfers.

       help    Display help text.

       lcd [path]
               Change local directory to path.  If path is not specified, then
               change directory to the local user's home directory.

       lls [ls-options [path]]
               Display local directory listing of either path or  current  di‐
               rectory  if  path is not specified.  ls-options may contain any
               flags supported by the local system's ls(1) command.  path  may
               contain glob(7) characters and may match multiple files.

       lmkdir path
               Create local directory specified by path.

       ln [-s] oldpath newpath
               Create a link from oldpath to newpath.  If the -s flag is spec‐
               ified  the  created  link is a symbolic link, otherwise it is a
               hard link.

       lpwd    Print local working directory.

       ls [-1afhlnrSt] [path]
               Display a remote directory listing of either path or  the  cur‐
               rent  directory  if  path  is  not specified.  path may contain
               glob(7) characters and may match multiple files.

               The following flags are recognized and alter the  behaviour  of
               ls accordingly:

               -1      Produce single columnar output.

               -a      List files beginning with a dot (‘.’).

               -f      Do  not  sort  the  listing.  The default sort order is
                       lexicographical.

               -h      When used with a long format option, use unit suffixes:
                       Byte, Kilobyte, Megabyte, Gigabyte, Terabyte, Petabyte,
                       and Exabyte in order to reduce the number of digits  to
                       four  or  fewer  using  powers  of 2 for sizes (K=1024,
                       M=1048576, etc.).

               -l      Display additional details  including  permissions  and
                       ownership information.

               -n      Produce  a long listing with user and group information
                       presented numerically.

               -r      Reverse the sort order of the listing.

               -S      Sort the listing by file size.

               -t      Sort the listing by last modification time.

       lumask umask
               Set local umask to umask.

       mkdir path
               Create remote directory specified by path.

       progress
               Toggle display of progress meter.

       put [-afpR] local-path [remote-path]
               Upload local-path and store it on the remote machine.   If  the
               remote path name is not specified, it is given the same name it
               has on the local machine.  local-path may contain glob(7) char‐
               acters   and   may  match  multiple  files.   If  it  does  and
               remote-path is specified, then remote-path must specify  a  di‐
               rectory.

               If  the  -a  flag  is specified, then attempt to resume partial
               transfers of existing files.  Note that resumption assumes that
               any partial copy of the remote file matches the local copy.  If
               the local file contents differ from the remote local copy  then
               the resultant file is likely to be corrupt.

               If the -f flag is specified, then a request will be sent to the
               server  to  call  fsync(2) after the file has been transferred.
               Note that this is only supported by servers that implement  the
               "fsync@openssh.com" extension.

               If the -p flag is specified, then full file permissions and ac‐
               cess times are copied too.

               If the -R flag is specified then directories will be copied re‐
               cursively.   Note that sftp does not follow symbolic links when
               performing recursive transfers.

       pwd     Display remote working directory.

       quit    Quit sftp.

       reget [-fpR] remote-path [local-path]
               Resume download of remote-path.  Equivalent to get with the  -a
               flag set.

       reput [-fpR] local-path [remote-path]
               Resume  upload  of  local-path.   Equivalent to put with the -a
               flag set.

       rename oldpath newpath
               Rename remote file from oldpath to newpath.

       rm path
               Delete remote file specified by path.

       rmdir path
               Remove remote directory specified by path.

       symlink oldpath newpath
               Create a symbolic link from oldpath to newpath.

       version
               Display the sftp protocol version.

       !command
               Execute command in local shell.

       !       Escape to local shell.

       ?       Synonym for help.

SEE ALSO
       ftp(1),   ls(1),    scp(1),    ssh(1),    ssh-add(1),    ssh-keygen(1),
       ssh_config(5), glob(7), sftp-server(8), sshd(8)

       T.  Ylonen  and  S.  Lehtinen,  SSH File Transfer Protocol, draft-ietf-
       secsh-filexfer-00.txt, January 2001, work in progress material.

Debian                         December 16, 2022                       SFTP(1)

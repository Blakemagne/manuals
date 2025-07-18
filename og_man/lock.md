UNIMPLEMENTED(2)              System Calls Manual             UNIMPLEMENTED(2)

NAME
       afs_syscall,  break,  fattach,  fdetach,  ftime, getmsg, getpmsg, gtty,
       isastream, lock, madvise1, mpx, prof, profil,  putmsg,  putpmsg,  secu‐
       rity, stty, tuxcall, ulimit, vserver - unimplemented system calls

SYNOPSIS
       Unimplemented system calls.

DESCRIPTION
       These system calls are not implemented in the Linux kernel.

RETURN VALUE
       These system calls always return -1 and set errno to ENOSYS.

NOTES
       Note that ftime(3), profil(3), and ulimit(3) are implemented as library
       functions.

       Some  system  calls,  like  alloc_hugepages(2), free_hugepages(2), iop‐
       erm(2), iopl(2), and vm86(2) exist only on certain architectures.

       Some system calls, like ipc(2), create_module(2),  init_module(2),  and
       delete_module(2)  exist  only when the Linux kernel was built with sup‐
       port for them.

SEE ALSO
       syscalls(2)

Linux man-pages 6.7               2023-10-31                  UNIMPLEMENTED(2)

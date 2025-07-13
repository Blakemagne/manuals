# SSH Manual

OpenSSH remote login client

## Name

ssh - OpenSSH remote login client

## Synopsis

ssh connects and logs into the specified destination, which may be specified as either [user@]hostname or a URI of the form ssh://[user@]hostname[:port].

## Description

ssh (SSH client) is a program for logging into a remote machine and for executing commands on a remote machine. It is intended to provide secure encrypted communications between two untrusted hosts over an insecure network.

## Common Options

**-4** Forces ssh to use IPv4 addresses only.

**-6** Forces ssh to use IPv6 addresses only.

**-A** Enables forwarding of connections from an authentication agent such as ssh-agent.

**-a** Disables forwarding of the authentication agent connection.

**-C** Requests compression of all data.

**-F configfile** Specifies an alternative per-user configuration file.

**-i identity_file** Selects a file from which the identity (private key) for public key authentication is read.

**-L port:host:hostport** Specifies that connections to the given TCP port or Unix socket on the local (client) host are to be forwarded to the given host and port, or Unix socket, on the remote side.

**-p port** Port to connect to on the remote host.

**-q** Quiet mode. Causes most warning and diagnostic messages to be suppressed.

**-v** Verbose mode. Causes ssh to print debugging messages about its progress.

## Examples

Connect to a remote host:
```
ssh user@hostname
```

Connect using a specific port:
```
ssh -p 2222 user@hostname
```

Forward a local port:
```
ssh -L 8080:localhost:80 user@hostname
```

## Files

**~/.ssh/config** - User configuration file
**~/.ssh/known_hosts** - Host keys for all hosts the user has logged into

## See Also

scp(1), sftp(1), ssh-add(1), ssh-agent(1), ssh-keygen(1), ssh-keyscan(1), sshd(8)
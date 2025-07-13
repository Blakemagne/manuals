# TMUX Manual

Terminal multiplexer

## Name

tmux - terminal multiplexer

## Synopsis

tmux is a terminal multiplexer: it enables a number of terminals to be created, accessed, and controlled from a single screen.

## Description

tmux may be controlled from an attached client by using a key combination of a prefix key, 'C-b' (Ctrl-b) by default, followed by a command key.

## Key Bindings

The default command key bindings are:

**C-b ?** List all key bindings.

**C-b d** Detach the current client.

**C-b c** Create a new window.

**C-b n** Change to the next window.

**C-b p** Change to the previous window.

**C-b l** Move to the previously selected window.

**C-b w** Choose the current window interactively.

**C-b 0 to 9** Select windows 0 to 9.

**C-b %** Split the current pane into two, left and right.

**C-b `"`** Split the current pane into two, top and bottom.

**C-b o** Select the next pane in the current window.

## Common Options

**-s session-name** Create a new session with the given name.

**-d** Detach the session (for use with new-session).

**-t target** Specify the target session, window, or pane.

## Examples

Create a new session:
```
tmux new-session -s mysession
```

Detach from current session:
```
Ctrl-b d
```

List sessions:
```
tmux list-sessions
```

Attach to a session:
```
tmux attach-session -t mysession
```

Split window horizontally:
```
Ctrl-b %
```

Split window vertically:
```
Ctrl-b "
```

## Files

**~/.tmux.conf** - User configuration file
**/etc/tmux.conf** - System-wide configuration file

## See Also

screen(1), sh(1)
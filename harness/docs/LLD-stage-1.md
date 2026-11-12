# Low-level design: door 1, the pretend door

## Why this door exists

The real subscription door needs your laptop signed into Antigravity. Tests must run with that door closed. So the first code is a door that returns lines we wrote in advance.

The real door, later, must use the same call: `complete(messages) -> Reply`.

## What you are allowed to change

Only the body of `PretendProvider.complete` in `src/harness/provider.py`.

Leave the tests alone. Leave `Reply` and `ScriptFinished` alone unless a test forces a change. Do not add libraries. Do not open a socket.

## Behavior

- `script` is a list of strings, copied when the door is created.
- `complete(messages)` ignores `messages` in this stage.
- The first call returns `Reply` whose `text` is script line 0.
- The next call returns the next line.
- When no lines are left, raise `ScriptFinished`.

## Out of this stage

Tool calls, images, the subscription URL, files, and the loop.

# Low-level design: Phase 1, Mock provider

Status: complete.

## Purpose

The subscription provider needs your laptop signed into Antigravity. Tests must run without that call. Phase 1 is a mock provider that returns lines we wrote in advance.

The subscription provider uses the same call: `complete(messages) -> Reply`.

## What changed

The body of `PretendProvider.complete` in `src/harness/provider.py`.

## Behavior

- `script` is a list of strings, copied when the provider is created.
- `complete(messages)` ignores `messages` in this phase.
- The first call returns `Reply` whose `text` is script line 0.
- The next call returns the next line.
- When no lines are left, raise `ScriptFinished`.

## Out of this phase

Tool calls, images, the subscription command, files, and the loop.

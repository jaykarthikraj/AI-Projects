# Low-level design: Phase 2, Subscription provider

Status: complete.

Pictures: `sdlc-05-real-plug.jpg` and `sdlc-06-find-bridge.jpg`.

## What we measured

On your laptop, this command returned the sentence `hello from the bridge`:

```powershell
agy -p "Reply with exactly these four words: hello from the bridge"
```

`agy` is the Antigravity command at `C:\Users\karth\AppData\Local\agy\bin\agy.exe`. Python carries the sentence to that command. `agy` returns the answer.

## What you added

`AntigravityProvider` in `src/harness/provider.py`. It has the same call as the mock provider: `complete(messages) -> Reply`. It runs `agy -p` with the last message and wraps the printed sentence in a `Reply`.

The four mock-provider tests stay. The Phase 2 tests call a stand-in command, so they do not use the subscription. One manual command called the real `agy`.

## Out of this phase

Tools, PDFs, the loop, images, speech, and your own model.

# Door 2: the subscription plug

Pictures: `sdlc-05-real-plug.jpg` and `sdlc-06-find-bridge.jpg`.

## What we measured

On your laptop, this command returned the sentence `hello from the bridge`:

```powershell
agy -p "Reply with exactly these four words: hello from the bridge"
```

`agy` is the Antigravity command at `C:\Users\karth\AppData\Local\agy\bin\agy.exe`. That command is our bridge. Adi's separate program is not required.

## What you add

A second door, `AntigravityProvider`, in `src/harness/provider.py`. It has the same call as the pretend door: `complete(messages) -> Reply`. It runs `agy -p` with the last message and wraps the printed sentence in a `Reply`.

The four pretend-door tests stay. New tests call a stand-in command, so they do not use the subscription. One manual command calls the real `agy`.

## Out of this door

Tools, PDFs, the loop, images, speech, and your own model.

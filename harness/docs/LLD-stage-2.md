# Door 2: the subscription plug

Pictures: `sdlc-05-real-plug.jpg` and `sdlc-06-find-bridge.jpg`.

## What this door is

The pretend door returns lines we wrote. This door sends one message to the Antigravity subscription already on your laptop and returns one real sentence.

Adi named the helper program Gemini Bridge. It runs on the laptop that is signed into Antigravity. Our harness talks to that program. He said he would share it. We use his program. We do not write a second one from guesswork.

## Your job right now

Find the bridge. Do not add Python yet.

In PowerShell, run:

```powershell
where.exe agy
```

`agy` is the Antigravity command-line tool. A good result is a file path. If Windows says it cannot find `agy`, paste that line to me and stop.

Then answer one question: did Adi send you a folder or file called Gemini Bridge? Look in your mail, chat with Adi, and Downloads. If you find it, paste the folder path. If you cannot find it, say "not found" and stop.

## What we build after the bridge is found

A second door with the same call you already know: `complete(messages) -> Reply`. It sends the last message to the bridge and wraps the real sentence in a `Reply`. The four pretend-door tests stay as they are. The new check is one manual call on your signed-in laptop.

## Out of this door

Tools, PDFs, the loop, images, speech, and your own model.

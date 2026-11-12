# High-level design

One page. The pictures are in `Start-here.pdf`.

## What we are building

A general-purpose harness on your Windows laptop. It is the same kind of tool as Antigravity: one program that can do many jobs, because it has tools. We do not write a new program for each job.

## What was agreed on 9 Nov

This is the later call, so it wins where the papers disagree.

- The work stays on your laptop. Colab is not part of this build.
- The thinking comes from the Antigravity subscription you already have, through the local bridge. We do not buy a second API for version 1.
- The harness may handle text, images, and frames from video. Speech stays out.
- There is one loop. You connect the tools. The model chooses the next step.
- A model running on your own graphics card is the last module, after the loop works.

## The four parts

1. **Door.** Something we can call to get a reply. Two doors, same shape: a pretend door for tests, and the subscription door for real replies.
2. **Loop.** Send the conversation. If the reply is plain words, stop. If the reply asks for a tool, run the tool and call again.
3. **Tools.** Small Python functions: read a file, list a folder, and later run a command. A scraper is a tool, not a second program.
4. **Folder.** The memory. The model forgets. The folder does not.

## What is out until a later stage

Book, film, speech, Colab, and your own model.

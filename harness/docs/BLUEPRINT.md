# Blueprint and order of work

This is the timeline. It is an order, not a calendar. We do not pick dates until door 1 passes, because the pace is "you finish a door, we read it, then the next door."

| Door | You build | Done when | Testing effort |
| --- | --- | --- | --- |
| 1. Pretend door | `PretendProvider.complete` | Four offline tests pass | 4 automated tests. No manual test. |
| 2. Subscription plug | `AntigravityProvider.complete` calls `agy -p` | Stand-in tests pass, and one manual call returns a real sentence | 3 automated tests with a stand-in command. 1 manual call to `agy`. |
| 3. One PDF | A folder turns one PDF into text cards with page numbers | A test finds the words on page 12 | 2 tests on a tiny fixture PDF. |
| 4. The loop | Ask, run one read tool, stop on plain words | A scripted conversation reads one file and stops | 1 scripted multi-step test. |
| 5. Kill and resume | Write the conversation to a notebook and continue after a kill | Resume continues, and a finished side effect does not run twice | 1 kill-and-resume test. |
| 6. One question | Ask about that PDF | The reply cites the page, or says the sources do not cover it | 2 scripted answers. |

Doors that stay shut: book, film, speech, Colab, your own model.

Door 1 is done. Its low-level design is `LLD-stage-1.md`. Door 2 is open. Its low-level design is `LLD-stage-2.md`. The first action is to find the bridge, before any new Python.

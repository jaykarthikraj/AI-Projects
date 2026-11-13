# Implementation blueprint

This is the phase plan. It is an order, not a calendar. A phase is one build increment: design, code, test, review, then the next phase.

| Phase | SDLC name | You build | Exit criterion | Test effort | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | Mock provider | `PretendProvider.complete` | Four offline tests pass | 4 automated tests. No manual test. | Complete |
| 2 | Subscription provider | `AntigravityProvider.complete` calls `agy -p` | Stand-in tests pass, and one manual call returns a real sentence | 3 automated tests with a stand-in command. 1 manual call to `agy`. | Complete |
| 3 | PDF ingestion | A folder turns one PDF into text cards with page numbers | A test finds the words on page 12 | 2 tests on a tiny fixture PDF. | Next |
| 4 | Agent loop | Ask, run one read tool, stop on plain words | A scripted conversation reads one file and stops | 1 scripted multi-step test. | Not started |
| 5 | Checkpoint and resume | Write the conversation to a notebook and continue after a stop | Resume continues, and a finished side effect does not run twice | 1 resume test. | Not started |
| 6 | Cited answer | Ask about that PDF | The reply cites the page, or says the sources do not cover it | 2 scripted answers. | Not started |

Deferred: book, film, speech, Colab, and your own model.

Low-level design for Phase 1: `LLD-phase-1.md`. Test record: `TEST-phase-1.md`.

Low-level design for Phase 2: `LLD-phase-2.md`.

Phase 3 gets its low-level design when we open it.

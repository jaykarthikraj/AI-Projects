# Test effort: Phase 1, Mock provider

Status: complete. Four automated tests passed. No manual test. No network. No key.

| Test | What it proves |
| --- | --- |
| `test_first_reply_is_the_first_scripted_line` | One call returns the first scripted line, as a `Reply`. |
| `test_second_call_returns_the_next_line` | Calls walk the script in order. |
| `test_empty_script_fails_with_script_finished` | An empty script is an error, not a blank success. |
| `test_pretend_door_does_not_open_a_network_connection` | The mock provider still answers if the network is broken. |

Run them from the `harness` folder:

```
python -m pytest
```

Phase 1 is complete. `complete` hands back the next scripted line, and it raises `ScriptFinished` when the script is finished.

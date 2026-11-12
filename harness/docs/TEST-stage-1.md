# Test effort: door 1

Four automated tests. No manual test. No network. No key.

| Test | What it proves |
| --- | --- |
| `test_first_reply_is_the_first_scripted_line` | One call returns the first scripted line, as a `Reply`. |
| `test_second_call_returns_the_next_line` | Calls walk the script in order. |
| `test_empty_script_fails_with_script_finished` | An empty script is an error, not a blank success. |
| `test_pretend_door_does_not_open_a_network_connection` | The door still answers if the network is broken. |

Run them from the `harness` folder:

```
python -m pytest
```

Door 1 is done when those four pass and you can explain `complete` out loud in one sentence: "It hands back the next scripted line, and it raises when the script is finished."

We review that sentence together before door 2.

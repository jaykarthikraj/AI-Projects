"""Doors the loop can call.

PretendProvider answers from a written script. AntigravityProvider answers
by running the local agy command.
"""

import subprocess


class ScriptFinished(Exception):
    """Raised when the pretend door has no scripted lines left."""


class BridgeError(Exception):
    """Raised when agy does not return a reply."""


class Reply:
    """What a door returns. Stage 1 is plain text only."""

    def __init__(self, text: str) -> None:
        self.text = text


class PretendProvider:
    """A door that replies from a written script, one line per call."""

    def __init__(self, script: list[str]) -> None:
        self._script = list(script)

    def complete(self, messages: list[str]) -> Reply:
        """Return the next scripted line."""
        if not self._script:
            raise ScriptFinished()
        text = self._script.pop(0)
        return Reply(text)


class AntigravityProvider:
    """A door that sends the last message to agy and returns the printed sentence."""

    def __init__(self, command: list[str] | None = None) -> None:
        self._command = ["agy", "-p"] if command is None else command

    def complete(self, messages: list[str]) -> Reply:
        if not messages:
            raise BridgeError("no message to send")
        completed = subprocess.run(
            [*self._command, messages[-1]],
            capture_output=True,
            text=True,
            check=False,
        )
        if completed.returncode != 0:
            detail = completed.stderr.strip() or "agy failed"
            raise BridgeError(detail)
        text = completed.stdout.strip()
        if not text:
            raise BridgeError("agy returned an empty reply")
        return Reply(text)
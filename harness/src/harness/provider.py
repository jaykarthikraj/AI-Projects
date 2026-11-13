"""Stage 1 contract: a door the loop can call without the internet.

The real Antigravity subscription door comes later, and it must fit this
same shape. You implement PretendProvider.complete. Do not add network code.
"""


class ScriptFinished(Exception):
    """Raised when the pretend door has no scripted lines left."""


class Reply:
    """What a door returns. Stage 1 is plain text only."""

    def __init__(self, text: str) -> None:
        self.text = text


class PretendProvider:
    """A door that replies from a written script, one line per call.

    script is a list of strings. The first complete() call returns the first
    string. The next call returns the next string. When the list is used up,
    complete() raises ScriptFinished.
    """

    def __init__(self, script: list[str]) -> None:
        self._script = list(script)

    def complete(self, messages: list[str]) -> Reply:
        """Return the next scripted line.
        messages is the conversation so far. Stage 1 does not read it.
        The argument is here so the real door can use the same call later.
        """
        if not self._script:
            raise ScriptFinished()
        text = self._script.pop(0)
        return Reply(text)

import sys

import pytest

from harness.provider import AntigravityProvider, BridgeError, Reply


def test_stand_in_command_returns_its_printed_line():
    door = AntigravityProvider([sys.executable, "-c", "print('hello from the bridge')"])
    reply = door.complete(["Hello"])
    assert isinstance(reply, Reply)
    assert reply.text == "hello from the bridge"


def test_empty_messages_fail():
    door = AntigravityProvider([sys.executable, "-c", "print('unused')"])
    with pytest.raises(BridgeError):
        door.complete([])


def test_failed_command_raises_bridge_error():
    door = AntigravityProvider([sys.executable, "-c", "import sys; sys.exit(1)"])
    with pytest.raises(BridgeError):
        door.complete(["Hello"])
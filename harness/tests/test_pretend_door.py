"""Stage 1 tests. They fail until PretendProvider.complete is written."""

import socket

import pytest

from harness.provider import PretendProvider, Reply, ScriptFinished


def test_first_reply_is_the_first_scripted_line():
    door = PretendProvider(["hello back"])
    reply = door.complete(["Hello"])
    assert isinstance(reply, Reply)
    assert reply.text == "hello back"


def test_second_call_returns_the_next_line():
    door = PretendProvider(["one", "two"])
    assert door.complete(["a"]).text == "one"
    assert door.complete(["b"]).text == "two"


def test_empty_script_fails_with_script_finished():
    door = PretendProvider([])
    with pytest.raises(ScriptFinished):
        door.complete(["Hello"])


def test_pretend_door_does_not_open_a_network_connection(monkeypatch):
    def refuse(*_args, **_kwargs):
        raise AssertionError("the pretend door tried to use the network")

    monkeypatch.setattr(socket, "socket", refuse)
    monkeypatch.setattr(socket, "create_connection", refuse)
    door = PretendProvider(["offline reply"])
    assert door.complete(["Hello"]).text == "offline reply"

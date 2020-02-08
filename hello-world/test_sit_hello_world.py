import pytest
from hello_world import hello

def test_say_hello():
    assert hello() == "Hello, World!"
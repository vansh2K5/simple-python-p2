from tests.main import greet


def test_greet_contains_hello():
    """Basic sanity test to ensure greet() returns a message with 'Hello'."""
    message = greet("Jenkins")
    assert "Hello" in message

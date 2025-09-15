from leads_to_raags.core import hello

def test_hello():
    assert hello("uv") == "Hello, uv!"
    assert hello() == "Hello, world!"

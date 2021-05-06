from main import hello_message

def test_hello_message():
    actual = hello_message("John Doe");
    expected = "Hi John Doe"
    assert actual == expected

def test_hello_message_with_int():
    actual = hello_message(32);
    expected = "I am not a string"
    assert actual == expected



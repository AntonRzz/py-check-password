import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, results",
    [
        ("Pass@word1", True),
        ("Password123!", True),
        ("A1@abcdef", True),
        ("Pass1@", False),
        ("1234@#", False),
        ("ThisIsAVeryLongPassword1@", False),
        ("Password123456789!", False),
        ("password1234", False),
        ("PASSWORD@123", False),
        ("Password123", False),
        ("Pass@word", False),
        ("12345678", False),
        ("@#&*()123", False),
        ("qwerty", False),
        ("Str@ng", False),
    ]
)
def test_check_password(
    password: str,
    results: bool
) -> None:
    assert check_password(password) == results

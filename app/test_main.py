import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, results",
    [
        ("Valid1@", True),
        ("ValidPassword123@", True),
        ("short1@", False),
        ("VeryLongPassword123@", False),
        ("12345678", False),
        ("password@", False),
        ("password1", False),
        ("1@Short", False),
        ("Valid@123", True),
        ("NoSpecialChar1", False),
        ("NoUppercase1@", False),
        ("Valid1#password", False),
    ]
)
def test_check_password(
    password: str,
    results: bool
) -> None:
    assert check_password(password) == results

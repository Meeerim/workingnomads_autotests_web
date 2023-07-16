import dataclasses


@dataclasses.dataclass
class User:
    full_name: str = "Meerim Sk "
    first_name: str = "Meerim"
    last_name: str = "Sk"
    email: str = "skmeerim1999@gmail.com"
    existed_email: str = "skmeerim@gmail.com"
    invalid_password: str = "Password12345"
    password: str = "Password0805"


user = User()

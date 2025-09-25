from ninja import Schema


class AuthInput(Schema):
    username: str
    password: str


class UserOut(Schema):
    id: int
    username: str
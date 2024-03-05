from dataclasses import dataclass


@dataclass
class Register:
    user_id: int
    user_name: str
    full_name: str
    phone_number: int

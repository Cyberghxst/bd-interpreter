from enum import Enum

class TokenTypes(Enum):
    closer = 0
    dollar = 1
    function_name = 2
    opener = 3
    text = 4


class Collection:
    functions = ['print', 'lowercase', 'uppercase']
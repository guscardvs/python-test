import secrets
from typing import List


text = "snake_case"
integer_list = [secrets.randbelow(10) for _ in range(10)]

def to_camel(string: str) -> str:
    pass

def even_only(int_list: List[int]) -> List[str]:
    pass

print(to_camel(text)) # Expected: snakeCase
print(even_only(integer_list)) # Expected: list with only even numbers ex.: [2,4,6]

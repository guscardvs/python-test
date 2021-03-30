import secrets
from typing import Dict, List


text = "snake_case"
integer_list = [secrets.randbelow(10) for _ in range(10)]
dictionary = {
    "name": ["Gustavo", "Eduardo"],
    "email": ["self.gustavocorrea@gmail.com", "edunascimento.mariano@gmail.com"],
}


def to_camel(string: str) -> str:
    ...


def even_only(int_list: List[int]) -> List[int]:
    ...


def to_record(dictionary: Dict[str, List[str]]) -> List[Dict[str, str]]:
    ...

class Person:
    def __init__(self, name: str) -> None:
        self.name = name
    
        

print(to_camel(text))  # Expected: snakeCase
print(even_only(integer_list))  # Expected: list with only even numbers ex.: [2,4,6]
print(to_record(dictionary))
# Expected:
# [
#   {"name":"Gustavo", "email":"self.gustavocorrea@gmail.com"},
#   {"name":"Eduardo", "email":"edunascimento.mariano@gmail.com"}
# ]
print(str(Person("Gustavo"))) # Expected: "My name is Gustavo"

import secrets

text = "snake_case"
integer_list = [secrets.randbelow(10) for _ in range(10)]

def to_camel(string):
    ...

def even_only(int_list):
    ...

print(to_camel(text)) # Expected: snakeCase
print(even_only(integer_list)) # Expected: list with only even numbers ex.: [2,4,6]

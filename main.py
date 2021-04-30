import sys


def sock_merchant(array_length: int, array: list[int]):
    ...


if __name__ == "__main__":

    array_length = int(input())

    array = list(map(int, sys.stdin.readline().rstrip().split()))

    result = sock_merchant(array_length, array)

    print(str(result) + "\n")

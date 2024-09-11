import re
import math


def calc_entropy(string: str) -> int:
    lower_case = len(re.findall(r"[a-z]", string))
    upper_case = len(re.findall(r"[A-Z]", string))
    digits = len(re.findall(r"[0-9]", string))
    special_chars = len(re.findall(r"[!-/:-@[-`{-~]", string))

    lenght: list[int] = []
    pool_size: list[int] = []

    if lower_case != 0:
        lenght.append(lower_case)
        pool_size.append(26)
    if upper_case != 0:
        lenght.append(upper_case)
        pool_size.append(26)
    if digits != 0:
        lenght.append(digits)
        pool_size.append(10)
    if special_chars != 0:
        lenght.append(special_chars)
        pool_size.append(32)

    return round(math.log2(sum(pool_size) ** sum(lenght)), 3)


if __name__ == "__main__":
    password = input("\nPassword: ")
    entropy = calc_entropy(password)
    print(f"Entropy: {entropy} bits")

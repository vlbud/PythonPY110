def task(camel_case_str: str) -> str:
    return "".join(filter(lambda x: x.islower(), camel_case_str))  # TODO отфильтровать только буквы нижнего регистра


if __name__ == "__main__":
    word = "AbCdEfGh"
    print(task(word))

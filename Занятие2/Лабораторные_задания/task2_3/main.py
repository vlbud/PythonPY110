def pow_gen(base: int):
    counter = 0
    while True:
        yield base ** counter
        counter += 1  # TODO записать функцию-генератор


if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))

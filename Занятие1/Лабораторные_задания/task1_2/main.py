def task() -> int:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    return max(len(i) for i in list_words)  # TODO найти длину самого длинного слова


if __name__ == "__main__":
    print(task())

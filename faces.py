def main():
    words = input().strip()
    convert(words)


def convert(str):
    print(str.replace(":(", "🙁").replace(":)", "🙂"))


main()

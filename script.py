
INP = "input.txt"
OUT = "output.txt"

IS_KEY_STR = True
IS_VAL_STR = True

DICT = "output"
QUOTE = '"'
BRACKET = "{"

def read_pairs():
    output = {}
    with open(INP, "r") as file:
        for line in file.readlines():
            stripped = line.strip()
            if stripped:
                key, value, *_ = (stripped.split("\t"))
                output[key] = value
    return output


def write_pairs(d):
    with open(OUT, "w") as file:
        file.write("{} = {}\n".format(DICT, BRACKET))
        for key, value in d.items():
            file.write(
                f'\t{QUOTE if IS_KEY_STR else ""}{key}{QUOTE if IS_KEY_STR else ""}: {QUOTE if IS_VAL_STR else ""}{value}{QUOTE if IS_VAL_STR else ""},\n'
            )
        file.write("}")


def main():
    pairs = read_pairs()
    write_pairs(pairs)


if __name__ == "__main__":
    main()

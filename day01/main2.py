def read_lines_from_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines


def main():
    # file_path = "test.txt"
    file_path = "input.txt"

    input = read_lines_from_file(file_path)

    left_list = split_list(input, 0)
    right_list = split_list(input, 1)

    diff = 0
    for left, right in zip(left_list, right_list):
        diff += int(left) * right_list.count(left)

    print(diff)


def split_list(list_to_split, index):
    result = []
    for line in list_to_split:
        result.append(line.split()[index])

    return result


if __name__ == "__main__":
    main()

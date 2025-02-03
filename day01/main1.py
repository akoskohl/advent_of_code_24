def read_lines_from_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines


def main():
    # file_path = 'input.txt'
    file_path = "input.txt"
    input = read_lines_from_file(file_path)

    left_list = split_list(input, 0)
    left_list.sort()
    right_list = split_list(input, 1)
    right_list.sort()

    difference = 0
    for left, right in zip(left_list, right_list):
        difference += abs(int(left) - int(right))

    print(difference)


def split_list(list_to_split, index):
    result = []
    for line in list_to_split:
        result.append(line.split()[index])

    return result


if __name__ == "__main__":
    main()

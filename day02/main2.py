def read_lines_from_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines


def is_safe_report(levels):
    increasing = all(
        levels[i] < levels[i + 1] and 1 <= levels[i + 1] - levels[i] <= 3
        for i in range(len(levels) - 1)
    )
    decreasing = all(
        levels[i] > levels[i + 1] and 1 <= levels[i] - levels[i + 1] <= 3
        for i in range(len(levels) - 1)
    )
    return increasing or decreasing


def is_safe_with_dampener(levels):
    if is_safe_report(levels):
        return True
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i + 1 :]
        if is_safe_report(new_levels):
            return True
    return False


def main():
    file_path = "test.txt"
    # file_path = "input.txt"
    input = read_lines_from_file(file_path)

    safe_reports = 0
    for line in input:
        levels = list(map(int, line.strip().split()))
        if is_safe_with_dampener(levels):
            safe_reports += 1

    print(safe_reports)


if __name__ == "__main__":
    main()

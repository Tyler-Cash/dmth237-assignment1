def read_file(file_name):
    list_of_strings = []
    with open(file_name, 'r') as file:
        for line in file:
            list_of_strings.append(line.replace('\n', ''))
    return list_of_strings


def print_list(print_list):
    print('lines: ', end='')
    for item in print_list:
        print(str(item), end=' ')
    print('')


def match_language():
    strings = read_file('randomstrings.txt')


if "__main__":
    match_language()

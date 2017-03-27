import re

# (0 + 1)∗(00000011111 + 11111100000) (0 + 1)∗
pattern_a = r'[01]*(00000011111|11111100000)[01]*'

#  (0 + 1)∗ 0(01)^5 1 (0 + 1)∗
pattern_b = r'(([01]*)(0(01){5}1)([01]*))'

# (0 + 1)∗ 000000(0 + 1)^14 111111 (0 + 1)∗
pattern_c = r'(([01]*)(000000[01]{14}111111)([01]*))'


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

    # Matches pattern for q6) a) and then prints matches
    results = [in_array + 1 for in_array, line_value in enumerate(strings) if re.match(pattern_a, line_value)]
    print('---------MATCHES FOR Q6) A)---------')
    print_list(results)

    # Matches pattern for q6) b) and then prints matches
    results = [in_array + 1 for in_array, line_value in enumerate(strings) if re.match(pattern_b, line_value)]
    print('---------MATCHES FOR Q6) B)---------')
    print_list(results)

    # Matches pattern for q6) c) and then prints matches
    results = [in_array + 1 for in_array, line_value in enumerate(strings) if re.match(pattern_c, line_value)]
    print('---------MATCHES FOR Q6) C)---------')
    print_list(results)


if "__main__":
    match_language()

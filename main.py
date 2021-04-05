import re


def read_file(file_name):
    with open(file_name) as a:
        f = a.readlines()

    return f


def main(start_date, end_date):
    is_needed_time = False
    line_counter = 0
    reading_file = read_file("access.log")
    for line in reading_file:
        if end_date in line:
            break
        if start_date in line:
            is_needed_time = True
        if is_needed_time:
            if re.findall(r'^([a-zA-Z0-9.]+)( - - )(\[.*?])(\s\"POST.*?\")(\s200\s).*$', line):
                print(line)
                line_counter += 1

    print(line_counter)


if __name__ == '__main__':
    main("[23/Mar/2009:17:18:26", "[25/Mar/2009:12:24:11")

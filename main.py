def read_file(fileName):
    with open(fileName, 'rb') as a:
        f = a.readlines()
        
    return f
    

def main(startDate, endDate, phrase, codeStatus):
    is_needed_time = False
    line_counter = 0
    rFile = read_file("access.log")
    
    for line in rFile:
        if endDate in line:
            is_needed_time = False
            break
        if startDate in line:
            is_needed_time = True
        if is_needed_time and phrase in line:
            if codeStatus in line:
                print(line, "\n")
                line_counter += 1

    print(line_counter)


if __name__ == '__main__':
    main(b"[23/Mar/2009:17:18:26", b"[25/Mar/2009:12:12:10", b"POST", b"\" 200")

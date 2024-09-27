def get_multiplied_digits(num):
    str_num = str(num)
    first = int(str_num[0])
    if len(str_num) > 1:
        return first * get_multiplied_digits(int(str_num[1:]))
    else:
        return first

print(get_multiplied_digits(40203))



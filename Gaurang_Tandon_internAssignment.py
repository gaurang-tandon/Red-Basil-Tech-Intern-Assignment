while True:
    try:
        my_input = int(input(f"Binary Input :\t\t"))
    except ValueError:
        continue
    if my_input<0:
        my_input = my_input*-1
    if len(str(my_input))>8:
        continue
    else:
        binaries = {'0','1'}
        temp_set = set(str(my_input))
        if binaries == temp_set or temp_set == {'0'} or temp_set == {'1'}:
            answer_val = 0
            bin_val = my_input
            i = 0
            while(bin_val != 0):
                temp_dec = bin_val % 10
                answer_val = answer_val + temp_dec * pow(2, i)
                bin_val = bin_val//10
                i += 1
            print(f"Decimal Value :\t\t{answer_val}")
        else:
            continue
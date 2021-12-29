# --------------- Python Program To Convert Binary Input Into Decimal Value ----------------- #

# Infinite loop to run the program until the user decide to stop it by keyboard input(Ctrl+C)
while True:
    # To check if the input contains only numeric characters
    try:
        # Taking input and reading it as integer value as asked in the assignment
        my_input = int(input(f"Binary Input :\t\t"))
    # If the input contains any aplhabetical character it will be caught as an exception
    # and the loop will continue to its next iteration i.e. waiting for another input
    except ValueError:
        continue
    # to check if the input contains a negative value
    # converting it to positive value as asked in the end of the assignment pdf
    if my_input<0:
        my_input = my_input*-1
    # to check that the input is within 8 digits, if not then loop will continue to next iteration
    if len(str(my_input))>8:
        continue
    # to convert the binary value to decimal if all the conditions are favourable
    else:
        binaries = {'0','1'} # predefining binary digits to compare 
        temp_set = set(str(my_input)) # temp_set should only contain unique elements ie {'0','1'},{'0'},{'1'}
        # to check if the input contained of any numeric digits other than 0 and/or 1
        # if contains only 0 and/or 1 if block is executed 
        if binaries == temp_set or temp_set == {'0'} or temp_set == {'1'}:
            # declaring integer variable to store the value of binary through the while loop
            answer_val = 0
            # temporary variable to hold the input value which will be changed in the loop
            bin_val = my_input
            i = 0
            while(bin_val != 0):
                # binary to decimal conversion
                # getting last binary bit one at a time to convert it into its decimal value
                temp_dec = bin_val % 10
                # decimal no = nth_bit * 2^(n-1) # since i is starting from 0 it will always be (n-1)
                answer_val = answer_val + temp_dec * pow(2, i)
                # changing the temporary binary value
                bin_val = bin_val//10
                # raising the value of i for next iteration of loop for higher binary bit value
                i += 1
            # printing answer to console
            print(f"Decimal Value :\t\t{answer_val}")
        # if input contains numeric digits other than 0 and/or 1 loop continnues to next iteration
        # for different input
        else:
            continue
# Input : "Mr John Smith", 13
# Output : Mr%20John%20Smith


def replace_spaces(input, total_length):

    space_count = 0

    for i in range(total_length):
        if input[i] == " ":
            space_count += 1

    total_char_length = total_length + (space_count * 2)

    for i in range(total_length - 1, 0, -1):

        if input[i] == " ":
            input[total_char_length - 1] = "0"
            input[total_char_length - 2] = "2"          # input[total_char_length - 3:total_char_length] = '%20'
            input[total_char_length - 3] = "%"
            total_char_length -= 3
        else:
            input[total_char_length - 1] = input[i]
            total_char_length -= 1

    return input


class Test:

    str = list("Mr John Smith    ")

    input = replace_spaces(str, 13)

    print(input)










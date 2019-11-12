#For example, “abcd” and “dabc” are Permutation of each other

def check_permutations(str1,str2):

    if len(str1) != len(str2):
        return False
    
    arr_value = [0] * 128

    for char in str1:
        value = ord(char)
        arr_value[value] += 1

    for char in str2:
        value = ord(char)
        arr_value[value] -= 1

        if arr_value[value] < 0:
            return False

    return True


class Test:
    a = 'abcd'

    b = 'bacd'

    print(check_permutations(a, b))
















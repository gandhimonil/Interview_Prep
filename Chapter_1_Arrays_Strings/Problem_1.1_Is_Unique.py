# Input : s = “abcd”
# Output: True
# “abcd” doesn’t contain any duplicates. Hence the output is True.
#
#
#
# Input : s = “abbd”
# Output: False
# “abbd” contains duplicates. Hence the output is False.


def is_unique(str):
    if len(str) > 128:
        return False

    boolean = [False] * 128

    for char in str:
        value = ord(char)
        if boolean[value]:
            return False

        boolean[value] = True

    return True


class Test:
    s = "abbd"
    print(is_unique(s))

    r = "abcd"
    print(is_unique(r))
    





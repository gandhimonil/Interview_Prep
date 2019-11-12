class Palindrome_Permutation:

    '''function checks if a string is a permutation of a palindrome or not'''
    def pal_perm(self, string):

        table = [0 for _ in range(ord('z') - ord('a') + 1)]

        countodd = 0

        for char in string:

            value = self.char_number(char)

            if value != -1:

                table[value] += 1

                if table[value] % 2:
                    countodd += 1
                else:
                    countodd -= 1

        return countodd <= 1


    def char_number(self, char):

        a = ord('a')
        z = ord('z')

        A = ord('A')
        Z = ord('Z')

        val = ord(char)

        if a <= val <= z:
            return val - a
        if A <= val <= Z:
            return val - A
        return -1


instance = Palindrome_Permutation()

print(instance.pal_perm('Able was I ere I saw Elba'))

print(instance.pal_perm('Random Words'))

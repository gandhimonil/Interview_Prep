class String_Compression:

    def string_compression(self, string):

        counter = 0

        compressed = []

        for i in range(len(string)):
            if i != 0 and string[i] != string[i - 1]:
                compressed.append(string[i - 1] + str(counter))
                counter = 0
            counter += 1

        compressed.append(string[-1] + str(counter))

        # returns original string if compressed string isn't smaller, the key is the length of the string
        return min(string, ''.join(compressed), key=len)


instance = String_Compression()

print(instance.string_compression('aabcccccaaa'))
print(instance.string_compression('abcdef'))
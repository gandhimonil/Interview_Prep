class String_Rotation:


    def is_substring(self, string, sub):
        return string.find(sub) != -1

    def string_rotation(self,s1, s2):
        if len(s1) == len(s2) != 0:
            return self.is_substring(s1 + s1, s2)
        return False


s = String_Rotation()

print(s.string_rotation('waterbottle', 'erbottlewat'))
print(s.string_rotation('foo', 'foofoo'))
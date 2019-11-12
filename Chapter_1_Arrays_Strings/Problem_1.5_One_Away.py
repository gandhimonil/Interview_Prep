class One_Away:

    def one_away(self, s1, s2):
        '''Check if a string can converted to another string with a single edit'''

        if len(s1) == len(s2):
            self.one_edit_replace(s1,s2)
        elif len(s1) - 1 == len(s2):
            self.one_edit_insert(s2, s1)
        elif len(s1) + 1 == len(s2):
            self.one_edit_insert(s1,s2)
        else:
            return False

    def one_edit_replace(self, string1, string2):

        boolean = False

        for c1, c2 in zip(string1, string2):

            if c1 != c2:
                if boolean:
                    return False
                boolean = True

        return True

    def one_edit_insert(self, string1, string2):

        edited = False

        i, j = 0, 0

        while i < len(string1) and j < len(string2):
            if string1[i] != string2[j]:

                if edited:
                    return False

                edited = True

                j += 1
            else:
                i += 1
                j += 1
        return True





instance = One_Away()

instance.one_away('pale', 'ple')

instance.one_away('pales', 'pale')

instance.one_away('pale', 'bale')


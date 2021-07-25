import re


class Solution:
    def strongPasswordChecker(self, password: str) -> int:

        # 1 - determine if any size changes needed
        minimum = 6
        maximum = 20
        length = len(password)
        add_count = minimum - length if length < minimum else 0
        delete_count = length - maximum if length > maximum else 0

        # 2 - validate character use
        # search for if the pattern exists
        # if it is NOT found --> character is needed  --> 1
        # if it IS     found --> character is present --> 0
        upper = 1 if re.search(r'([A-Z]+)', password) is None else 0
        lower = 1 if re.search(r'([a-z]+)', password) is None else 0
        digit = 1 if re.search(r'(\d+)', password) is None else 0
        # add the total number of character types missing
        characters_needed = upper + lower + digit

        # 3 - find repeating characters of length 3 or greater
        # 'aaa'   --> mod(0) --> 1 change or 1 delete  'aab'  ,'aaA'  ,'aa1'
        # 'aaaa'  --> mod(1) --> 1 change or 2 deletes 'aaba' ,'aaAa' ,'aa1a'
        # 'aaaaa' --> mod(2) --> 1 change or 3 deletes 'aabaa','aaAaa','aa1aa'

        # establish null case
        three_sets = 0
        one_delete = 0
        two_delete = 0
        # look for a character
        # capture when an additional 2+ of the same character exist
        # find all instances where the pattern is matched
        m = re.findall(r'(.)(\1{2,})', password)
        if m:
            for key, val in m:
                length = len(key + val)

                three_sets += length // 3
                one_delete += 1 if length % 3 == 0 else 0
                two_delete += 2 if length % 3 == 1 else 0
                # don't need a three_delete
                # that is implicit to the # of sets

        set_reduction = three_sets

        # logic for number of steps #
        ###############################
        # generic case
        steps = max(three_sets, characters_needed)
        # low end
        if add_count:
            # case 'aaaaaa' has 2 sets and 2 characters needed
            steps = max(three_sets, characters_needed, add_count)
        # high end (20)
        if delete_count:
            # start with all sets

            # subtract out as many single deletes as you can
            set_reduction -= min(delete_count, one_delete) // 1
            # reduce the available deletes
            delete_count1 = max(delete_count - one_delete, 0)  # /1
            # subtract out as many double deletes as you can
            set_reduction -= min(delete_count1, two_delete) // 2
            # reduce the available deletes
            delete_count2 = max(delete_count - one_delete - two_delete, 0)
            # subtract out as many remaining
            set_reduction -= delete_count2 // 3

            steps = delete_count + max(set_reduction, characters_needed)
        return steps


if __name__ == '__main__':
    print(Solution().strongPasswordChecker("1111111111"))

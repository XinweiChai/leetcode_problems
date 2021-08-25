class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        seen = {}

        def can_win(choices, remainder):
            # if the largest choice exceeds the remainder, then we can win!
            if choices[-1] >= remainder:
                return True

            # if we have seen this exact scenario play out, then we know the outcome
            seen_key = tuple(choices)
            if seen_key in seen:
                return seen[seen_key]

            # we haven't won yet.. it's the next player's turn.
            for index in 0, len(choices) - 1:
                if not can_win(choices[:index] + choices[index + 1:], remainder - choices[index]):
                    seen[seen_key] = True
                    return True

            # uh-oh if we got here then next player won all permutations, we can't force their hand
            # actually, they were able to force our hand :(
            seen[seen_key] = False
            return False

        # let's do some quick checks before we journey through the tree of permutations
        summed_choices = (maxChoosableInteger + 1) * maxChoosableInteger / 2

        # if all the choices added up are less then the total, no-one can win
        if summed_choices < desiredTotal:
            return False

        # if the sum matches desiredTotal exactly then you win if there's an odd number of turns
        if summed_choices == desiredTotal:
            return maxChoosableInteger % 2

        # slow: time to go through the tree of permutations
        choices = list(range(1, maxChoosableInteger + 1))
        return can_win(choices, desiredTotal)

    def canIWin2(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        def win(M, T, m, state):
            if T <= 0: return False
            if m[state] != 0: return m[state] == 1
            for i in range(M):
                if (state & (1 << i)) > 0: continue
                if not win(M, T - i - 1, m, state | (1 << i)):
                    m[state] = 1
                    return True
            m[state] = -1
            return False

        M = maxChoosableInteger
        T = desiredTotal
        s = M * (M + 1) / 2
        if s < T: return False
        if T <= 0: return True
        if s == T: return (M % 2) == 1

        m = [0] * (1 << M)
        return win(M, T, m, 0)

if __name__ == '__main__':
    print(Solution().canIWin(10, 11))

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
                   2: ['a', 'b', 'c'],
                   3: ['d', 'e', 'f'],
                   4: ['g', 'h', 'i'],
                   5: ['j', 'k', 'l'],
                   6: ['m', 'n', 'o'],
                   7: ['p', 'q', 'r', 's'],
                   8: ['t', 'u', 'v'],
                   9: ['w', 'x', 'y', 'z']
                   }
        combinations = []
        for idx, digit in enumerate(digits):
            digit = int(digit)
            if idx == 0:
                combinations.extend([char for char in mapping[digit]])
                continue
            digit_combos = []
            for idx in range(len(combinations)):
                for char_map in mapping[digit]:
                    digit_combos.append(combinations[idx] + char_map)
            combinations = digit_combos
        return combinations   
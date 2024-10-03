class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        sorted_strs = sorted(strs)
        first = sorted_strs[0]
        last = sorted_strs[-1]

        for i in range(min(len(first), len(last))):
            if (first[i] != last[i]):
                return common
            common += first[i]
        
        return common

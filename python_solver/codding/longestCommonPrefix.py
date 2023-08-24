def longestCommonPrefix(strs: list[str]) -> str:
    commonPrefix = ""
    strs.sort()
    for i in range(min(len(strs[0]), len(strs[-1]))):
        if strs[0][i]!=strs[-1][i]:
            return commonPrefix
        commonPrefix += strs[0][i]
        
    return commonPrefix
        

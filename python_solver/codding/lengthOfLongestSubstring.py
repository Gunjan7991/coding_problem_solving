def lengthOfLongestSubstring(s: str) -> int:
    l = 0 
    seen = {}
    length = 0
    for r in range(len(s)):
        char = s[r]
        if char in seen and seen[char]>=l:
            l = seen[char]+1 # update see to one plus the inital index
        else:
            length = max(length, r-l+1)
        seen[char] = r
    
    return length
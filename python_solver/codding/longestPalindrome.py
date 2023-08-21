def longestPalindrome(s: str) -> str:
    """
    Longest Palindrome:
        Dificulty: Medium
        In this problem,  we have to identify
    """
    # If the input string is already a palindrome, return it
    if s == s[::-1]:
        return s

    # Initialize an empty list to store weights
    weight = []

    # Create a modified string with "$" between characters
    new_s = "$" + "$".join(s) + "$"

    # Iterate through each character in the modified string
    for pos, char in enumerate(new_s):
        # Initialize pointers and value for expanding palindrome
        left, right, value = pos, pos, 1

        # Check if we can expand around the center
        while (
            left > 0 and right < len(new_s) - 1 and new_s[left - 1] == new_s[right + 1]
        ):
            value += 2
            left -= 1
            right += 1

        # Append the calculated value (weight) to the list
        weight.append(value)

    # Find the position with the highest weight
    b_pos = weight.index(max(weight))

    # Calculate left and right indices for extracting the substring
    left = b_pos - (max(weight) // 2)
    right = b_pos + (max(weight) // 2)

    # Extract the longest palindromic substring and remove "$" symbols
    longest_palindrome = new_s[left : right + 1 : 1].replace("$", "")

    return longest_palindrome

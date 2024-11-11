def decode_message( s: str, p: str) -> bool:
    str_len, pat_len = len(s), len(p)
    
    # Initialize a table for dynamic programming
    match = [[False] * (pat_len + 1) for _ in range(str_len + 1)]
    
    # Base case: empty pattern matches empty string
    match[0][0] = True
    
    # Handle patterns with '*' at the beginning that can match an empty sequence
    for col in range(1, pat_len + 1):
        if p[col - 1] == '*':
            match[0][col] = match[0][col - 1]
    
    # Populate the table by comparing the pattern with the string
    for row in range(1, str_len + 1):
        for col in range(1, pat_len + 1):
            current_pattern = p[col - 1]
            if current_pattern == '*':
                # '*' can either match nothing or extend the previous match
                match[row][col] = match[row - 1][col] or match[row][col - 1]
            elif current_pattern == '?' or current_pattern == s[row - 1]:
                # '?' matches any single character, or characters match exactly
                match[row][col] = match[row - 1][col - 1]
    
    # The final result is stored in the bottom-right corner of the table
    return match[str_len][pat_len]

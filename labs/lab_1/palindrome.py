def palindrome(string, l, h):
    if l >= h:
        return True

    if string[l] != string[h]:
        return False
    else:
        return palindrome(string, l + 1, h - 1)


string = ""
sol = palindrome(string, 0, len(string) - 1)
print(sol)

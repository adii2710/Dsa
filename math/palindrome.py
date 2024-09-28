word="heh"

# def isPalindrome(word):
#     st=""
#     for i in range(-1, -len(word)-1, -1):
#         st +=word[i]
    
#     return st


def isPalindrome(word):
    if word==word[::-1]:
        return True
    return False

print(isPalindrome(word))
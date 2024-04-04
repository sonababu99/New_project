#program to find if 2 strings or sentences are anagram or not
def anagram(s1,s2):
    return sorted(s1) == sorted(s2)
print(anagram("silent","listen"))

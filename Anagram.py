def anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    f1 = {}
    f2 ={}
    for ch in s1:
        if ch in f1:
            f1[ch] += 1
        else:
            f1[ch] = 1
    for ch in s2:
        if ch in f2:
            f2[ch] += 1
        else:
            f2[ch] = 1
    for key in f1:
        if key not in f2 or f1[key] != f2[key]:
            return False
    return True

#s1 = input("Enter S1: ")
#s2 = input("Enter s2: ")
#print(anagram(s1,s2))


def anagrams2(s1,s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)   #Time complexity - O(nlogn)

s1 = input("Enter s1 ")
s2 = input("Enter s2 ")
print(anagrams2(s1,s2))

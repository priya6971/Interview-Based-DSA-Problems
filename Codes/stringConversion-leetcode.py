
def canConvert(str1, str2):
    dictionary = {}
    hashset = set()

    for i in range(len(str1)):
        hashset.add(str2[i])
        if str1[i] in dictionary and dictionary[str1[i]] != str2[i]:
            return False
        dictionary[str1[i]] = str2[i]

    if str1 != str2 and len(hashset) == 26 and len(dictionary) == 26:
        return False
    return True

str1 = "leetcode"
str2 = "codeleet"
if canConvert(str1, str2):
    print("True")
else:
    print("False")
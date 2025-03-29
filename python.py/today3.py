def is_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)
print(is_anagrams("suri","irus"))
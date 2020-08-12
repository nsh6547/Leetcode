import collections
strs= ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrams = collections.defaultdict(list)

for word in strs:
    anagrams[''.join(sorted(word))].append(word)
    print(anagrams)

print(" ")
print (anagrams.values())
print(anagrams)
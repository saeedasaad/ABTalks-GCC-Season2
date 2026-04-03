from collections import defaultdict

def groupAnagrams(strs):

    anagram_map = defaultdict(list)
    for word in strs:
        key = ''.join(sorted(word))
        anagram_map[key].append(word)
    return list(anagram_map.values())

if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = groupAnagrams(words)
    print("Input:", words)
    print("Grouped Anagrams:", result)
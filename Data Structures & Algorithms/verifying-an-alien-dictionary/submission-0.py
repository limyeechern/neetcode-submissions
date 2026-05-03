class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        hashmap = {c : i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            print(word1)
            print(word2)

            for j in range(len(word1)):
                if j == len(word2):
                    return False
                if hashmap[word2[j]] > hashmap[word1[j]]:
                    break
                if hashmap[word2[j]] < hashmap[word1[j]]:
                    return False
                
        return True

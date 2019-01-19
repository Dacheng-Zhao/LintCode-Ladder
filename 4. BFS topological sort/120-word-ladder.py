
import collections
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        # dict.add(end)
        # queue = collections.deque([start])
        # distance = 0
        # visited = collections.deque([start])
        
        # while queue:
        #     distance += 1 
        #     for i in range(len(queue)):
        #         word = queue.popleft()
        #         visited.append(word)
        #         if word == end:
        #             return distance
                    
        #         for j in range(len(word)):
        #             word_left = word[:j]
        #             word_right = word[j + 1 :]
        #             for char in 'abcdefghijklmnopqrstuvwxyz':
        #                 new_word = word_left + char + word_right
        #                 if new_word in dict and new_word not in visited:
        #                     queue.append(new_word)
        #                     visited.append(new_word)
                            
        # return 0
        
        dict.add(end)
        queue = collections.deque([start])
        visited = set([start])
        
        distance = 0
        while queue:
            distance += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return distance
                
                for next_word in self.get_next_words(word):
                    if next_word not in dict or next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word) 

        return 0
        
    # O(26 * L^2)
    # L is the length of word
    def get_next_words(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words
                
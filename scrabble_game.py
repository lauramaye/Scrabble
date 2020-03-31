class Game:

    def __init__(self, type):
        self.type = type
        print("%s game created" % self.type)

    def getType(self):
        return "%s Game" % (self.type)

class ScrabbleGame(Game):

    def __init__(self):
        type = "Scrabble"
        super().__init__(type)
        self.possible_scores = {
            1: ['a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r'],
            2: ['d', 'g'],
            3: ['b', 'c', 'm', 'p'],
            4: ['f', 'h', 'v', 'w', 'y'],
            5: ['k'],
            8: ['j', 'x'],
            10: ['q', 'z']
        }

    def compareWords(self, word1, word2):
        '''
        Checks to see if a character in word1 appears in word2
        Returns:
        - "true": if a character in word1 appears in word2
        - "false": if there is no character in word1 that is in word2
        '''
        character_found = "false"
        for i in word1:
            for k in word2:
                if i.lower() == k.lower():
                    character_found = "true"
        return character_found

    def isSubstringOf(self, word_portion, word):
        '''
        Checks to see if word_portion appears in word.
        Returns:
        - "true": if the word_portion appears in the word
        - "false": if the word_portion does not appear in the word
        '''
        is_substring = "false"
        word_to_lower, word_portion_to_lower = word.lower(), word_portion.lower()
        if word_portion_to_lower in word_to_lower:
            is_substring = "true"
        return is_substring

    def checkScore(self, word):
        '''
        check the score of a word, if it was to be played.
        No need to check if it is in the dictonary, but keep in mind
        that the checking of each letter is not case sensitive.
        Returns:
        score (int)
        '''
        score = 0
        word_lower = word.lower()
        for char in word:
            for i in self.possible_scores:
                if char in self.possible_scores[i]:
                    score = score + i
        return score

    def compareWords(self, word1, word2):
        '''
        compares possible score of word1 with the possible score of word2. Both are strings.
        Returns:
        - word1 (as string): if word1's score is higher
        - word2 (as string): if word2's score is higher
        - -1: if both scores are equal.
        '''
        score1 = self.checkScore(word1)
        score2 = self.checkScore(word2)
        if score1 > score2:
            return word1
        elif score2 > score1:
            return word2
        else:
            return -1




scrabble_1 = ScrabbleGame()
game_type = scrabble_1.getType()
print(game_type)
compare = scrabble_1.compareWords("mouse", "cat")
print(compare)

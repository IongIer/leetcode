from string import ascii_lowercase

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dict={k:v for k,v in zip(list(ascii_lowercase), code)}
        
        words_morse = []
        for word in words:
            words_morse.append("".join(list(map(dict.get, list(word)))))
        return len(set(words_morse))
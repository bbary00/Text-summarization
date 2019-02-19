import unittest
import roman


def convert(text):
    """Converts romanian numbers in text to common numbers"""
    #Creating a dictionary of roman-arabic pairs
    roman_pairs = dict([roman.toRoman(arabic), arabic] for arabic in range(1, 4001))
    text = text.split()
    for word in text:
        #Searching for coincidence in dict keys word by word
        if word in roman_pairs.keys():
            # Check whether our word is last, then check previous word for English letter
            # If English - don't change 
            if word is text[-1] and ord(text[text.index(word) - 1][0]) not in range(65, 123):
                text[text.index(word)] = str(roman_pairs[word])
            # If not last check following
            elif not (word is text[-1]) and ord(text[text.index(word) + 1][0]) not in range(65, 123):
                text[text.index(word)] = str(roman_pairs[word])
            else:
                pass
    return ' '.join(text)


class TestRomanianConvert(unittest.TestCase):

    def test_ukr(self):

    # Big Ukrainian letter i(I) can't be at the beginning of the sentence grammatically.
    # So I skip the case of converting this as a ukrainian symbol.

        self.assertEqual(
            convert('У XXI сторіччі, а саме після MMLXXIII буде доступе I ст.'),
            'У 21 сторіччі, а саме після 2073 буде доступе 1 ст.')
        self.assertEqual(
            convert('В кінці VI в. до н.е. скіфи сформували свою державу'),
            'В кінці 6 в. до н.е. скіфи сформували свою державу')
        self.assertEqual(
            convert('Але на кінець IV - початок III століття'),
            'Але на кінець 4 - початок 3 століття')
        self.assertEqual(
            convert('Держава антів проіснувала близько трьох століть (кінець IV - початок VII ст. )'),
            'Держава антів проіснувала близько трьох століть (кінець 4 - початок 7 ст. )')

    def test_eng(self):
        """Letter 'I' should not be converted to number"""

        self.assertEqual(convert('I love LNU'), 'I love LNU')
        self.assertEqual(convert('I like my mentor'), 'I like my mentor')
        self.assertEqual(convert('If I were you'), 'If I were you')
        self.assertEqual(convert('My size is XL'), 'My size is XL')
        self.assertEqual(convert('My brother and I would like to live in 10th century'),
                         'My brother and I would like to live in 10th century')



if __name__ == "__main__":
    unittest.main()

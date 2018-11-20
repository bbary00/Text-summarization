import re
from collections import Counter
from pprint import pprint as pp
import operator

for i in range(1, 18):
    path_text = 'C:\\Users\\admin\\Desktop\\Data\\Primal\\Trash\\text' + str(i) + '.txt'
    path_data = 'C:\\Users\\admin\\Desktop\\Data\\Primal\\Cleaned\\data' + str(i) + '.txt'
    path_dict = 'C:\\Users\\admin\\Desktop\\Data\\Primal\\Dictionary\\dict' + str(i) + '.txt'
    with open(path_text, 'rt') as file:
        with open(path_data, 'w') as f:
            with open(path_dict, 'w') as d:
                text = file.read().replace('\n', '')
                pattern = '[!?.,\"\-\'()«»;:+-=*%^&$#@№]'
                text = re.sub(pattern, ' ', text)
                #print(text)
                f.write(str(text))
                f.write('\n\n')
                text = text.lower().split()
                dictionary = {word: text.count(word) for word in text}
                dictionary = sorted(dictionary.items(), key=operator.itemgetter(1))
                d.write(str(dictionary))
                #pp(dictionary)
                #print('\n\n')
                #print(text)
                f.write(str(text))


"""Place all files in a Data folder in your desktop"""


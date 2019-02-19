from string import punctuation
from nltk.collocations import *


def get_text():
    """Read text from .txt file"""
    # Paste a path
    path_text = 'PATH'
    with open(path_text) as file:
        text = file.read()
    return text


def get_sent(text):
    """Tokenizing text into sentences. Here I have problems with abbreviations
    such as ñò. since sentences are divided by dots"""

    from nltk.tokenize import sent_tokenize
    sentences = sent_tokenize(text)
    return sentences


def get_cleaned_words(text):
    """Tokenize text into words(tokens) and clean them from punctuation marks and stopwords"""

    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    text = text.lower()
    words = word_tokenize(text)
    stopwords = set(stopwords.words('ukrainian') + list(punctuation) + ['\'\'', '\"\"', '«', '»', '\n'])
    cleaned_words = [word for word in words if word not in stopwords]
    return cleaned_words


def ngrams(words):
    """Finding n-grams in the text. It is not used in this version."""

    import nltk
    bigram = nltk.collocations.BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(words)


def stemming(words):
    """Finding words with the same root. Isn't used in this version"""

    from nltk.stem.lancaster import LancasterStemmer
    st = LancasterStemmer()
    steamed = [st.stem(word) for word in words]
    return steamed


def word_evaluation(words):
    """Construct a frequency distribution of words"""

    from nltk.probability import FreqDist
    freq = FreqDist(words)
    from heapq import nlargest
    n = nlargest(20, freq, key=freq.get)
    return freq


def finding_sent(freq, sent):
    """Evaluation of sentences and finding most valuable"""

    from heapq import nlargest
    from collections import defaultdict
    from nltk.tokenize import word_tokenize
    ranking = defaultdict(int)
    for i, sen in enumerate(sent):
        for w in word_tokenize(sen.lower()):
            if w in freq:
                ranking[i] += freq[w]
    n = int(input('Enter how many sentences to output (must be less then {}): '.format(len(sent))))
    assert n <= len(sent)
    s_idx = nlargest(n, ranking, key=ranking.get)
    summary = [sent[j] for j in sorted(s_idx)]
    print(' '.join(summary))


data = get_text()
token_sentences = get_sent(data)
tokens = get_cleaned_words(data)
ngrams(tokens)
s_words = stemming(tokens)
main_tokens = word_evaluation(tokens)
finding_sent(main_tokens, token_sentences)

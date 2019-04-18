from string import punctuation
from database_work import save_data
from stemming import stem



def get_text(path):
    """Read text from .txt file"""
    text = path
    # with open(path) as file:
    #     text = file.read()
    return text


def get_sent(text):
    """Tokenizing text into sentences."""

    from nltk.tokenize import sent_tokenize
    sentences = sent_tokenize(text)
    # print(sentences)
    return sentences


def get_cleaned_words(text):
    """Tokenize text into words(tokens)
     and clean them from punctuation marks and stopwords"""

    with open('stopwords/ukrainian.txt', 'r') as f:
        f.readline()
        stopwords = f.read().split()
    with open('stopwords/punct.txt', 'r') as f:
        f.readline()
        punct = f.read().split()
    punct += list(punctuation)
    stopwords = set(stopwords + punct)
    cleaned_words = []
    stemmed_sent = []
    from nltk.tokenize import word_tokenize
    for sent in text:
        sent_list = []
        for word in word_tokenize(sent.lower()):
            stemmed = stem(word)
            if word not in stopwords and word[0] not in punct and word[-1] \
                    not in punct:
                cleaned_words.append(word)
                sent_list.append(stemmed)
        stemmed_sent.append(sent_list)
    return (cleaned_words, stemmed_sent)


def word_evaluation(words):
    """Construct a frequency distribution of words"""

    from collections import Counter
    d = dict(sorted(dict(Counter(words)).items(),
               key=lambda x: x[1], reverse=True))
    n = list(d.keys())
    n = [stem(token) for token in n[:20]]
    return n


def finding_sent(freq, sent):
    """Evaluation of sentences and finding most valuable"""
    from collections import defaultdict
    from nltk.tokenize import word_tokenize
    ranking = defaultdict(int)
    for i in range(len(sent)):
        for w in sent[i]:
            if w.lower() in freq:
                ranking[i] += 1
    ranking = sorted(ranking.items(), key=lambda x:x[1], reverse=True)
    ranking = [i[0] for i in ranking]
    return ranking


def summarize(path, sent, perc):
    """Main function to import"""

    data = get_text(path)
    token_sentences = get_sent(data)
    tokens, stemmed_sent = get_cleaned_words(token_sentences)
    main_tokens = word_evaluation(tokens)
    ranking = finding_sent(main_tokens, stemmed_sent)
    if not perc:
        n = int(sent)
        s_idx = ranking[:n]
        summary = [token_sentences[i] for i in sorted(s_idx)]
    else:
        p = int(perc)
        p = len(token_sentences) * p // 100
        s_idx_p = ranking[:p]
        summary = [token_sentences[j] for j in sorted(s_idx_p)]
    s = '\n'.join(summary)
    # print(' '.join(summary))
    return s


#
# if __name__ == '__main__':
#     with open('test.txt', 'r', encoding='utf-8', errors='ignore') as f:
#         text = f.read()
#     print(summarize(text, 4))

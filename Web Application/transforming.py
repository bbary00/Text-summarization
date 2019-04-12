﻿from string import punctuation
from database_work import save_data
# from gensim.summarization import summarize
# from gensim.summarization import keywords


def get_text(path):
    """Read text from .txt file"""
    text = path
    # with open(path) as file:
    #     text = file.read()
    return text


def get_sent(text):
    """Tokenizing text into sentences. Here I have problems with abbreviations
    such as ст. since sentences are divided by dots"""

    from nltk.tokenize import sent_tokenize
    sentences = sent_tokenize(text)
    # print(sentences)
    return sentences


def get_cleaned_words(text):
    """Tokenize text into words(tokens) and clean them from punctuation marks and stopwords"""

    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    text = text.lower()
    words = word_tokenize(text)
    stopwords = set(stopwords.words('english') + list(punctuation) + ['\'\'', '\"\"', '«', '»', '\n', '``', '’', "'s"])
    cleaned_words = [word for word in words if word not in stopwords]
    return cleaned_words


def word_evaluation(words):
    """Construct a frequency distribution of words"""

    freq = set(words)
    d = {}
    for i in freq:
        d[i] = words.count(i)
    d = dict(sorted(d.items(), key=lambda x: x[1]))
    n = list(d.keys())
    return n[:20]


def finding_sent(freq, sent):
    """Evaluation of sentences and finding most valuable"""

    from collections import defaultdict
    from nltk.tokenize import word_tokenize
    ranking = defaultdict(int)
    for i, sen in enumerate(sent):
        for w in word_tokenize(sen):
            if w.lower() in freq:
                ranking[i] += 1
                continue
            if len(w) >= 4:
                k = len(w) // 2
                if any([i.startswith(w[:k].lower()) for i in freq]):
                    ranking[i] += 1
    # print(ranking)
    ranking = sorted(ranking.items(), key=lambda x:x[1], reverse=True)
    ranking = [i[0] for i in ranking]
    # print(ranking, '\n\n\n')
    return ranking


def summarize(path, sent):
    """Main function to import"""

    from heapq import nlargest
    data = get_text(path)
    token_sentences = get_sent(data)
    # for i, j in enumerate(token_sentences):
    #     print(i, ' : ', j)
    tokens = get_cleaned_words(data)
    # ngrams(tokens)
    # s_words = stemming(tokens)
    main_tokens = word_evaluation(tokens)
    # print(dict(main_tokens))
    ranking = finding_sent(main_tokens, token_sentences)
    # print(ranking, 'here\n\n')
    # n = int(input('Enter how many sentences to output (must be less then {}): '.format(len(token_sentences))))
    n = int(sent)
    # p = int(input('Enter how many sentences to output in percent 1-99: '))
    # p = int(perc)
    # p = len(token_sentences) * p // 100
    # print(p)
    s_idx = ranking[:n]
    # s_idx_p = nlargest(p, ranking, key=ranking.get)
    # print(s_idx)
    summary = [token_sentences[j] for j in sorted(s_idx)]
    s = ' '.join(summary)
    save_data(1, data, s)
    # print('\n\n')
    # summary = [token_sentences[j] for j in sorted(s_idx_p)]
    # s = ' '.join(summary)
    # print(' '.join(summary))
    return s


# sum = summarize(text, sent)
# import json
# summ = {'text': summarize('C:\\Users\\admin\\Desktop\\qqq.txt')}
# print(summ)
# with open('C:\\Users\\admin\\Desktop\\js.json', 'w') as f:
#     json.dump(
#         summ,
#         f,
#         sort_keys=False,
#         indent=4,
#         ensure_ascii=False,
#         separators=(',', ': ')
#     )
#
# with open('C:\\Users\\admin\\Desktop\\js.json', 'r') as f:
#     data = json.load(f)
#     print(data)

# coding=utf8


from string import punctuation
# from gensim.summarization import summarize
# from gensim.summarization import keywords


def get_text(path):
    """Read text from .txt file"""
    text = path.encode('ascii', 'ignore')
    # with open(path) as file:
    #     text = file.read()
    return text


def get_sent(text):
    """Tokenizing text into sentences. Here I have problems with abbreviations such as since sentences are divided by dots"""
    from nltk.tokenize import sent_tokenize
    sentences = sent_tokenize(text)
    return sentences


def get_cleaned_words(text):
    """Tokenize text into words(tokens) and clean them from punctuation marks and st$"""
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    text = text.lower()
    words = word_tokenize(text)
    stopwords = set(stopwords.words('english') + list(punctuation) + ['\'\'', '\"\"', '«', '»', '\n', '\'s', '``', '’'])
    cleaned_words = [word for word in words if word not in stopwords]
    return cleaned_words


def word_evaluation(words):
    """Construct a frequency distribution of words"""
    freq = set(words)
    d = {}
    for i in freq:
        d[i] = words.count(i)
    d = sorted(d.items(), key = lambda x: x[1], reverse=True)
    n = [i[0] for i in d]
    number = min(20, len(n))
    return n[:number]


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
                if any([wo.startswith(w[:k].lower()) for wo in freq]):
                    ranking[i] += 1
    ranking = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
    ranking = [i[0] for i in ranking]
    return ranking



def summarize(path, sent):
    """Main function to import"""
    from heapq import nlargest
    data = get_text(path)
    token_sentences = get_sent(data)
    tokens = get_cleaned_words(data)
    # ngrams(tokens)
    # s_words = stemming(tokens)
    main_tokens = word_evaluation(tokens)
    # print(dict(main_tokens))
    ranking = finding_sent(main_tokens, token_sentences)
    # n = int(input('Enter how many sentences to output (must be less then {}): '.fo$
    n = int(sent)
    # p = int(input('Enter how many sentences to output in percent 1-99: '))
    # p = int(perc)
    # p = len(token_sentences) * p // 100
    # print(p)
    s_idx = ranking[:n]
    # s_idx_p = nlargest(p, ranking, key=ranking.get)
    summary = [token_sentences[j] for j in sorted(s_idx)]
    s = ' '.join(summary)
    # print('\n\n')
    # summary = [token_sentences[j] for j in sorted(s_idx_p)]
    # s = ' '.join(summary)
    # print(' '.join(summary))
    return s
import re


"""Dictionary with suffixes"""
ends = {
    'prefixes': r'^(без|по-|екс-|премєр-|від|од|пере|між|над|об|пре|перед|під|понад|пред|роз|через|при|прі|архі|із|зі|без|роз|через|по|за|най)',
    'adverb': r'(учи|ючи|ачи|ячи|ши|ив|ів|[иі]?вши(сь)?)$',
    'infinitive': r'([тс][яь])$',
    'adjective': r'(ими|(н|ин|ичн|ист|ічн|їн|їст|їчн|ев|єв|ов|уват|куват|юват|оват|овит|анн|енн)?(их|ий|ій|им|а|е|ої|ого|ими))$',
    'participle': r'(ий|ого|ому|им|ім|ою|ій|их|йми|их|ан)$',
    'verb': r'([еєиї]+ш|[еєиї]+(мо)|[аяиїую]ть|ла|ло|ов|ив|ав|али|вши|ме|ти)$',
    'noun': r'([еє](ві|ні|нем|нами)|[еє][юйм]|[ая](ми|ти|ті|та|тами)|[ая][мх]|о[юмк]|ові|їв|ів|а|ев|ов|еи|и|й|о|у|ь|я|і|ї|є|е|ю)$',
    'vowel': r'[аеиоуюяіїє]',
    'vowel_end': r'[аеиоуюяіїєь]$'
}


def ukstemmer_search_preprocess(word):
    """Pre-process"""
    word = word.lower()
    word = word.replace("'", "")
    return word


def cut(st_part, reg, to):
    """Find the biggest suffix in a given suffix group and cut it"""
    rex = re.compile(reg)
    found_suffixes = rex.findall(st_part)
    if found_suffixes:
        if type(found_suffixes[0]) is tuple:
            found_suffixes = list(found_suffixes[0])
        length = [len(suf) for suf in found_suffixes]
        reg = found_suffixes[length.index(max(length))]
        return re.sub(reg, to, st_part)
    return st_part


def stemming(word):
    word = ukstemmer_search_preprocess(word)
    if not re.search(ends['vowel'], word):
        return word
    p = re.search(ends['vowel'], word)
    first_part = word[0:p.span()[1]]
    last_part = word[p.span()[1]:]
    return first_phase(first_part, last_part, word)


def first_phase(start, end, word):
    try_cut = cut(end, '[іи]сть$', '')
    if end != try_cut:
        end = try_cut
        return second_phase(start, end, word)

    try_cut = cut(end, ends['adverb'], '')
    if end != try_cut:
        end = try_cut
        return second_phase(start, end, word)

    try_cut = cut(end, ends['infinitive'], '')
    if end != try_cut:
        end = try_cut
        end = cut(end, ends['verb'], '')
        return second_phase(start, end, word)

    try_cut = cut(end, ends['adjective'], '')
    if end != try_cut:
        end = try_cut
        return second_phase(start, end, word)

    try_cut = cut(end, ends['participle'], '')
    if end != try_cut:
        end = try_cut
        return second_phase(start, end, word)

    try_cut = cut(end, ends['verb'], '')
    if end != try_cut:
        end = try_cut
        return second_phase(start, end, word)

    try_cut = cut(end, ends['noun'], '')
    if end != try_cut:
        end = try_cut
        return second_phase(start, end, word)

    return second_phase(start, end, word)


def second_phase(start, end, word):
    cut(end, ends['vowel_end'], '')
    cut(end, 'нн$', u'н')
    if len(start + end) < 3:
        return word
    stem = start + end
    if len(re.sub(ends['prefixes'], '', word)) > 2:
        stem = re.sub(ends['prefixes'], '', stem)
    return stem


def stem(word):
    # with open('Harri.txt', encoding='utf-8', errors='ignore') as f:
    #     text = f.read()
    # print(text)
    # words = get_cleaned_words(text)
    # print("Len words: {}".format(len(words)))
    # print("Unique words: {}".format(len(list(set(words)))))
    # st = time.time()
    # d = {}
    # st_words = []
    # for i in range(len(words)):
    #     st_words.append(stemming(words[i]))
    # for i in st_words:
    #     d[i] = []
    # for i in range(len(words)):
    #     target = stemming(words[i])
    #     if target in d.keys() and words[i] not in d[target]:
    #         d[target].append(words[i])
    # d = sorted(d.items(), key=lambda x: len(x[1]))
    # pp(d)
    # end = time.time()
    # print("Work was done for {} sec".format(end-st))
    # print('Len after stemming: {}'.format(len(list(set(st_words)))))
    return stemming(word)


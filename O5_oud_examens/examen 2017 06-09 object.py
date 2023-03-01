'''
        TIJD:    35 min
        geschat: 45 min

'''


class Dictionary:

    def __init__(self, source_language, target_language):
        self.__source_language_ = source_language
        self.__target_language_ = target_language
        self.__translations_ = dict()

    def get_source_language(self):
        return self.__source_language_

    def get_target_language(self):
        return self.__target_language_

    def get_translations(self):
        return self.__translations_

    def get_nb_entries(self):
        return len(self.get_translations().keys())

    def get_all_translations_for(self, source_word):
        return self.get_translations().get(source_word, frozenset())

    def get_a_translation_for(self, source_word):
        if source_word in self.get_translations():
            return self.get_all_translations_for(source_word)[0]

    def add_translation_for(self, source_word, target_words):
        self.get_translations()[source_word] = \
            self.get_all_translations_for(source_word).union(frozenset(target_words))

    def remove_translation_for(self, source_word, target_word):
        if source_word in self.get_translations():
            if len(self.get_all_translations_for(source_word)) == 1:
                del self.get_translations()[source_word]
            else:
                self.get_translations()[source_word] = \
                    self.get_all_translations_for(source_word) - frozenset(target_word)

    def get_all_words(self, target_word):
        return set(map(lambda pairs: pairs[0],
                       filter(lambda pairs: target_word in pairs[1],
                              self.get_translations().items())))

    def __add__(self, other):
        if isinstance(other, Dictionary) \
                and self.get_source_language() == other.get_source_language() \
                and self.get_target_language() == other.get_target_language():
            for source, target in other.get_translations().items():
                self.add_translation_for(source, target)
            return self

    ## EXTRA
    def __str__(self):
        header = "source: " + str(self.get_source_language()) + \
                 " - target: " + str(self.get_target_language()) + \
                 "  |  nb of translations: " + str(self.get_nb_entries()) + \
                 "\n" + "----------------------------------------------------------------------" + "\n"
        body = ""

        for source, targets in self.get_translations().items():
            target_txt = ""
            for target in targets:
                target_txt += str(target) + ", "
            source_text = str(source) + " : " + target_txt + "\n"
            body += source_text

        return header + body


import string
import random

def randomString(stringLength = 10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


words = [randomString(c) for k in range(1, 10) for c in range(3, 5)]
langs = [randomString(2) for k in range(1, 3)]

dics = []
for N in range(2):
    dic = Dictionary(random.choice(langs),random.choice(langs))
    for n in range(random.randrange(1, 2), random.randrange(5, 9)):
        dic.add_translation_for(random.choice(words), random.choices(words, k = n))
    dics.append(dic)

for dic in dics:
    print(dic)

print(dics[-1] + dics[-2])

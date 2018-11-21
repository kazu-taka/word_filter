class WordFilter:
    def __init__(self, word_filter):
        self.word_filter = word_filter

    def detect(self, word):
        return self.word_filter in word

    def censor(self, word, replace_word="<censored>"):
        return word.replace(self.word_filter, replace_word)


my_filter = WordFilter("アーセナル")

# C-1
# NGワードが含まれている場合
print(my_filter.detect("昨日のアーセナルの試合アツかった！"))  # Trueを返す ※出力されるわけではありません！

# NGワードが含まれていない場合
print(my_filter.detect("昨日のリバプールの試合アツかった！"))  # Falseを返す ※出力されるわけではありません！

# C-2
# NGワードが含まれている場合
print(my_filter.censor("昨日のアーセナルの試合アツかった！"))  # "昨日の<censored>の試合アツかった！" を返す ※出力されるわけではありません！

# NGワードが含まれていない場合
print(my_filter.censor("昨日のリバプールの試合アツかった！"))  # "昨日のリバプールの試合アツかった！" を返す ※出力されるわけではありません！

# C-3
# NGワードが含まれている場合
print(my_filter.censor("昨日のアーセナルの試合アツかった！", "TEST"))  # "昨日の<censored>の試合アツかった！" を返す ※出力されるわけではありません！

# NGワードが含まれていない場合
print(my_filter.censor("昨日のリバプールの試合アツかった！", "TEST"))  # "昨日のリバプールの試合アツかった！" を返す ※出力されるわけではありません！

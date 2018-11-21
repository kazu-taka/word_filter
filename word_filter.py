class WordFilter:
    def __init__(self, word_filter):
        self.word_filter = word_filter

    def detect(self, word):
        return self.word_filter in word


my_filter = WordFilter("アーセナル")

# NGワードが含まれている場合
print(my_filter.detect("昨日のアーセナルの試合アツかった！"))  # Trueを返す ※出力されるわけではありません！

# NGワードが含まれていない場合
print(my_filter.detect("昨日のリバプールの試合アツかった！"))  # Falseを返す ※出力されるわけではありません！

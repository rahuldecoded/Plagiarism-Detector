class RollingHash:
    def __init__(self, text, size_word):
        self.text = text
        self.hash = 0
        self.size_word = size_word
        self.hashtable = []

        for i in range(0, size_word):
            self.hash += (ord(self.text[i]) - ord("a") + 1) * (33 ** (size_word - i - 1))

        self.window_start = 0
        self.window_end = size_word

    def move_window(self):
        if self.window_end < len(self.text):
            self.hash -= (ord(self.text[self.window_start]) - ord("a") + 1) * 33 ** (self.size_word - 1)
            self.hash *= 33
            self.hash += ord(self.text[self.window_end]) - ord("a") + 1
            self.window_start += 1
            self.window_end += 1

    def window_text(self):
        return self.text[self.window_start:self.window_end]


def rabin_karp_engine(word, text):
    if word == "" or text == "":
        return None
    if len(word) > len(text):
        return None

    rolling_hash = RollingHash(text, len(word))
    word_hash = RollingHash(word, len(word))
    for i in range(len(text) - len(word) + 1):
        if rolling_hash.hash == word_hash.hash:
            if rolling_hash.window_text() == word:
                return i
        rolling_hash.move_window()
    return None


def rabin_karp(main_content, other_content):
    user_content = []
    for sentence in main_content:
        for word in sentence:
            user_content.append(word)
    user_content_len = len(user_content)
    user_content = " ".join(user_content)

    available_content = []
    for sentence in other_content:
        for word in sentence:
            available_content.append(word)
    available_content_len = len(available_content)

    count = 0
    for i in available_content:
        temp = rabin_karp_engine(i, user_content)
        if temp is not None:
            count = count + 1
    # return (2 * count) / (available_content_len + user_content_len) * 100
    return count * 100 / user_content_len

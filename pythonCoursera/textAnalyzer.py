# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

givenString = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."


class TextAnalyzer(object):
    def __init__(self, text):
        # remove punctuation
        formatted_text = text.replace('.', '').replace('!', '').replace('?', '').replace(',', '')

        # make text lowercase
        formatted_text = formatted_text.lower()

        self.fmtText = formatted_text

    def freq_all(self):
        # split text into words
        word_list = self.fmtText.split(' ')

        # Create dictionary
        freq_map = {}
        for word in set(word_list):  # use set to remove duplicates in list
            freq_map[word] = word_list.count(word)

        return freq_map

    def freq_of(self, word):
        # get frequency map
        freq_dict = self.freqAll()

        if word in freq_dict:
            return freq_dict[word]
        else:
            return 0


class ShinyNew(object):
    def __init__(self, a=1, b=2):
        self.a = a
        self.b = b

    def show_attributes(self):
        print(self.a, self.b)


def print_funcs():
    print(__name__ == 'funcs')
    print(type(return_none()))
    obj = ShinyNew(2, 3)
    print(dir(obj))
    print(type(dir(obj)[-2]))
    analyzed = TextAnalyzer(givenString)
    print("Formatted Text:", analyzed.fmtText)
    freq_map = analyzed.freq_all()
    print(freq_map)
    word = "lorem"
    frequency = analyzed.freqOf(word)
    print("The word", word, "appears", frequency, "times.")


def return_none():
    pass


def return_none():
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__funcs__':
    print_funcs()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/


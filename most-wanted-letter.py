import re

def checkio(text):
    text = text.lower()
    max_values = 0
    max_char = 'z'
    for char in text:
        max = text.count(char)
        print max, char
        if (max == max_values and ord(char) < ord(max_char) or max > max_values) and re.search('[a-z]', char):
            max_values = max
            max_char = char
    return max_char
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio(u"abe") == "a", "The First."
    print("Start the long test")
    assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
    print("The local tests are done.")

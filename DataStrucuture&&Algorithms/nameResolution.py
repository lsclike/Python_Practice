class Resolution:
    this_is_class_namespace = 'who?'

    def __init__(self, word):
        self._word = word

    def talk(self):
        print(self._word)

if __name__ == '__main__':
    test = Resolution('joke')
    print(test.this_is_class_namespace)
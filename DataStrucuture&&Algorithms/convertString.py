class CaesarCipher:

    def __init__(self, shift):

        encoder = [None] * 26
        decoder = [None] * 26

        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))

        self._forward =''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self, message):

        return self._transform(message, self._forward)

    def decrypt(self, message):

        return self._transform(message, self._backward)

    def _transform(self, origin, code):

        msg = list(origin)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)

if __name__=='__main__':
    cipher = CaesarCipher(5)
    message = 'WHY ALL CAPITAL'
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrypt(coded)
    print('Answer: ', answer)


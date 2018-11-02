class CaesarCipher:

    def __init__(self, shift):

        encoder = [None] * 58
        decoder = [None] * 58

        for k in range(58):
            encoder[k] = chr((k + shift) % 58 + ord('A'))
            decoder[k] = chr((k - shift) % 58 + ord('A'))

        self._forward =''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self, message):

        return self._transform(message, self._forward)

    def decrypt(self, message):

        return self._transform(message, self._backward)

    def _transform(self, origin, code):

        msg = list(origin)
        for k in range(len(msg)):
            j = ord(msg[k]) - ord('A')
            msg[k] = code[j]
        return ''.join(msg)

if __name__=='__main__':
    cipher = CaesarCipher(5)
    message = 'WHY ALL CAPITAL s'
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrypt(coded)
    print('Answer: ', answer)


key = 'abcdefghijklmnopqrstuvwxyz.'
# 평문을 받아서 암호화하고 암호문을 반환한다.


def encrypt(combien, plaintext):
    result = ''

    for l in plaintext.lower():
        try:
            i = (key.index(l) + combien) % 26
            result += key[i]

        except ValueError:
            result += l

    return result.lower()


combien = 2

text = 'i love you.'
encrypted = encrypt(combien, text)
print('암호문: ', encrypted)

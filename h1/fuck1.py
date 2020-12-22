def fuck(str):
    for k in range(1, 26):
        r = ''
        for i in str:
            a = ((ord(i) - 65) + 26 - k)%26
            r += chr(a + 65)
        print(r)
    return str

if __name__ == '__main__':
    fuck('ESPESTCOPIPCNTDPYPPODACZRCLXXTYR')
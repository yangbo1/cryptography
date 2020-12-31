# 生成RSA的参数
    # 找两个大素数 p、q
    # n = p*q
    # φ(n) = (p-1)*(q-1)
    # 随机选b (1<b<φ(n))  其中(b, φ(n)) = 1 (欧式算法)
    #
    # 求 a = b逆modφ(n) 即 a = egcd(b, φ(n))
    #
    # 公钥 (n, b)
    # 私钥 (p, q, a)

# 使用
    # Bob生成RSA参数， 把公钥给Alice，让Alice发消息给Bob， Alice拿到n和b
    # Alic 将明文^b mod n 加密成 密文 发给Bob
    # Bob使用私钥 pqa解密：密文^a mod n 得到明文



def egcd(a, m, i=1):
    # a*x = 1 mod m = m * k + 1
    k = 1
    while (m*k + i)%a != 0:
        k += 1
    return (m * k + i) // a
def gcd(a,b):
    while b > 0:
        a, b = b, a%b
    return a

# 同余方程组
# x ≡ 12 (mod 25)
# x ≡ 9 (mod 26)
# x ≡ 23 (mod 27)
def mm(lista, listm):
    M = 1
    for m in listm:
        M *= m
    print('M=', M)
    listM = [int(M/mi) for mi in listm]
    print('listM=', listM)
    listy = [egcd(listM[i], listm[i]) for i in range(len(listM))]
    print('listy=', listy)
    r = 0
    for i in range(len(lista)):
        r += lista[i]*listM[i]*listy[i]
    return r%M

def ordn(a, n):
    k = 1
    while a**k % n != 1:
        k += 1
    return k

def IsPrime(num):
    #根据质数的定义，其必须大于0
    if num == 1:
        return False
    #循环需要判断的次数
    for i in range(2, num // 2 + 1):
        #如果该数有其他的因子返回False，即不是质数
        if num % i == 0:
            return False
    return True
def fuck(p):
    for i in range(1, int(p/2)):
        if IsPrime(i) and p%i == 0 and IsPrime(p//i):
            return i, p//i

def decode(code, a, n):
    r = []
    for m in code:
        r.append(m**a % n)
    return r
# 计算Zn的字母
def Zn(code, i=2):
    if i == 0:
        return chr(code+97)
    a1 = code // (26**i)
    m1 = code % (26**i)
    return chr(a1+97) + Zn(m1, i-1)

# 求通与方程两个不同的解 y位密文 m为p或q
def uv(y , m):
    u1 = y ** int((m+1)/4) % m

    return u1, -u1 % m

if __name__ == '__main__':
    # print(gcd(680261, 678709))
    # print(egcd(28, 75))
    print(egcd(104729, 15485863))

    lista = [12, 9, 23]
    # lista = [2, 3, 2]
    listm = [25, 26, 27]
    # listm = [3, 5, 7]
    print(mm(lista, listm))

    print(ordn(2, 11))
    p, q = fuck(31313)
    print('分解：', p, q)
    fai = (p-1)*(q-1)
    print('φ(n)=', fai)
    a = egcd(4913, fai)
    print('解密指数=', a)

    s = '6340 8309 14010 8936 27358 25023 16481 25809 23614 7135 24996 30590 27570 26486 30388 9395 27584 14999 4517 12146 29421 26439 1606 17881 25774 7647 23901 7372 25774 18436 12056 13547 7908 8635 2149 1908 22076 7372 8686 1304 4082 11803 5314 107 7359 22470 7372 22827 15698 30317 4685 14696 30388 8671 29956 15705 1417 26905 25809 28347 26277 7897 20240 21519 12437 1108 27106 18743 24144 10685 25234 30155 23005 8267 9917 7994 9694 2149 10042 27705 15930 29748 8635 23645 11738 24591 20240 27212 27486 9741 2149 29329 2149 5501 14015 30155 18154 22319 27705 20321 23254 13624 3249 5443 2149 16975 16087 14600 27705 19386 7325 26277 19554 23614 7553 4734 8091 23973 14015 107 3183 17347 25234 4595 21498 6360 19837 8463 6000 31280 29413 2066 369 23204 8425 7792 25973 4477 30989'
    code = [int(i) for i in s.split(' ')]
    decode = decode(code, a, p*q)
    print('decode=', decode)

    print(Zn(2398))
    s = ''
    for i in decode:
        s += Zn(i)
    print(s)

    # 计算 y = EK (32767);
    # EK (x) = x(x + B) mod n,
    # Ÿ• B ∈ Zn ¥˙ò‹©. b½
    # ,
    p = 199
    q = 211
    n = p*q
    B = 1357
    y = 32767*(32767+B) % n

    print('y = EK (32767)=', y)

    # 4/3 mod 1000000007
    print(egcd(3, 1000000007, 4))

    y = (y + egcd(4, n, B**2)) % n

    print(y)
    # 计算四个可能解
    u1, u2 = uv(y, p)
    v1, v2 = uv(y, q)
    print('u1=', u1)
    print('u2=', u2)
    print('v1=', v1)
    print('v2=', v2)
    x1 = mm([u1, v1], [p, q])
    x2 = mm([u1, v2], [p, q])
    x3 = -x1 % n
    x4 = -x2 % n
    print('x1=', x1)
    print('x2=', x2)
    print('x3=', x3)
    print('x4=', x4)
    print(x1**2 % n)
    print(x2**2 % n)
    print(x3**2 % n)
    print(x4**2 % n)

    x1 = (x1 - egcd(2, n, B)) % n
    x2 = (x2 - egcd(2, n, B)) % n
    x3 = (x3 - egcd(2, n, B)) % n
    x4 = (x4 - egcd(2, n, B)) % n

    print('x1=', x1)
    print('x2=', x2)
    print('x3=', x3)
    print('x4=', x4)
    print(x1*(x1+B) % n)
    print(x2*(x2+B) % n)
    print(x3*(x3+B) % n)
    print(x4*(x4+B) % n)
    # print((100-20) % 7)
    # print((100%7-20%7) % 7)
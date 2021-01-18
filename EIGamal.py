
# β= α^a  mod p
# Alice 想发消息给Bob 明文x=1299, p=2579 α=2 a = 765
# 选随机数 k，假设k=853
# 计算β = α^a mod p = 2^765 mod 2579 = 949
# 计算y1 = α^k mod p = 2^863 mod 2579 = 435
# y2 = x * β^k mod p = 1299 * 949^853 mod 2579 = 2396
# Bob收到y = (y1, y2) = (435, 2396)
# 恢复明文 x = y2 * (y1^a)^-1 mod p = 2396 * (435^765)^-1 mod 2579 = 1299

# 费马小定理求逆元 求(a^b) mod p逆元
def inv(a, b, p):
    #a^b = 1 mod p
    # 由a^p−1≡1(mod p)得a×a^p−2≡1(mod p)
    # a^(p-1)≡ 1 mod p = a^(p-1-b) * a^b 所以a^(p-1-b)就是逆元
    return a**(p-1-b)
print(2396%2579 * (435**1813 %2579) % 2579)
if __name__ == '__main__':
    # ElGamal  p = 31847, α = 7,
    # β = 18074, ¶
    # 1 求 a;
    # 2 加密明文 x = 389 (选随机数 k = 511), 并解密
    a = 1
    p = 31847
    aef = 7
    bt = 18074
    while aef**a % p != bt:
        a += 1
    print('a=', a)

    print(7**21839 % p)
    x = 389
    k = 511
    #加密
    y1 = aef**k % p
    y2 = x*(bt**k) % p
    print('加密y1,y2=', y1, y2)

    #解密
    x = (y2%p * inv(y1, a, p) % p ) % p
    print('解密x=', x)



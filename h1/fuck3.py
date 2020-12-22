import numpy as np

def fuckm(n):
    # n*x = 1 mod 26 = 26 * k + 1
    k = 1
    while (26*k + 1)%n != 0:
        k += 1
    return (26 * k + 1) / n

def fuckb(K):
    A = np.zeros((len(K),len(K)))
    for i in range(len(K)):
        for j in range(len(K[i])):
            A[i, j] = (-1)**(i+j) * np.linalg.det(np.delete(np.delete(K, i, axis=0), j, axis=1))
    return np.transpose(A)%26

def fuck3(K):
    return np.dot(fuckm(int(np.linalg.det(K))%26), fuckb(K)) % 26

def fuckyou(str, K):
    #y = x*K 加密
    #x = y*K逆 解密
    r = ''
    i = 3
    while i<len(str)+1:
        a = np.dot(np.array([ord(str[i-3])-97, ord(str[i-2])-97, ord(str[i-1])-97]), K) % 26
        for j in a:
            r += chr((j+97))
        i += 3
    return r.upper()
if __name__ == '__main__':
    K = np.array(
        [(1, 11, 12),
         (4, 23, 2),
         (17, 15, 9)]
    )
    print(fuck3(K))
    print(fuckyou('lookingforwardtoournationalday', K))
    print(fuckyou(fuckyou('lookingforwardtoournationalday', K), np.array(
        [(25, 11, 22),
         (10, 13, 4),
         (17, 24, 1)]
    )))

    print(fuckyou('breathtaking', np.array([(3,  21,  20),
                                           (4,  15,  23),
                                           (6, 14,  5)])))
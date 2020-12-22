import numpy as np

def fuckm(n):
    # n*x = 1 mod 26 = 26 * k + 1
    k = 1
    while (26*k + 1)%n != 0:
        k += 1
    return (26 * k + 1) / n

def gcd(a,b):
    if a%b == 0:
        return b
    else :
        return gcd(b,a%b)

def fuckb(K):
    A = np.zeros((len(K),len(K)))
    for i in range(len(K)):
        for j in range(len(K[i])):
            A[i, j] = (-1)**(i+j) * np.linalg.det(np.delete(np.delete(K, i, axis=0), j, axis=1))
    return np.transpose(A)%26

def fuck3(K):
    return np.dot(fuckm(int(round(np.linalg.det(K)))%26), fuckb(K)) % 26

def fuck(str, ss):
    x = orda(str)
    y = orda(ss.lower())
    print(x)
    print(y)
    k = 2
    while k < len(str):
        for i in range(0, len(str), k*k):
            a = []
            b = []
            for j in range(k):
                a.append(x[i+j*k:i+(j+1)*k])
            A = np.array(a)
            print(A)
            for j in range(k):
                b.append(y[i+j*k:i+(j+1)*k])
            B = np.array(b)
            print(B)
            det = int(round(np.linalg.det(A))) % 26
            print('det=', det)

            if gcd(det, 26)>1:
                k+=1
                break
            dd = fuckm(det)
            print('dd=', dd)
            AA = fuck3(A)
            print('AA=', AA)
            print('K=', np.dot(AA, B)%26)
def orda(str):
    l = []
    for i in str:
        l.append(ord(i) - 97)
    return l
if __name__ == '__main__':
    str = 'breathtaking'
    # str = 'friday'
    ss = 'RUPOTENTOIFV'
    # ss = 'PQCFKU'
    fuck(str, ss)

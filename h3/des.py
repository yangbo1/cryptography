import numpy as np

C = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
E = [32,1,2,3,4,5,
    4,5,6,7,8,9,
    8,9,10,11,12,13,
    12,13,14,15,16,17,
    16,17,18,19,20,21,
    20,21,22,23,24,25,
    24,25,26,27,28,29,
    28,29,30,31,32,1]
IP =   [58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7]

IP1 =  [57,49,41,33,25,17,9,1,
        58,50,42,34,26,18,10,2,
        59,51,43,35,27,19,11,3,
        60,52,44,36,63,55,47,39,
        31,23,15,7,62,54,46,38,
        30,22,14,6,61,53,45,37,
        29,21,13,5,28,20,12,4]

IP2 =  [14,17,11,24,1,5,
        3,28,15,6,21,10,
        23,19,12,4,26,8,
        16,7,27,20,13,2,
        41,52,31,37,47,55,
        30,40,51,45,33,48,
        44,49,39,56,34,53,
        46,42,50,36,29,32]
S = [
    [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,
0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,
4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13],
    [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,
3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,
0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,
13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9],
    [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,
13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,
13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,
1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12],
    [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15,
13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9,
10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,
3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14],
    [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9,
14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6,
4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14,
11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3],
    [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11,
10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8,
9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6,
4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13],
    [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1,
13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6,
1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,
6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12],
    [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7,
1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2,
7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,
2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
]

SP = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,
2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]
# 置换
def K(a, P):
    r = ''
    for i in range(len(P)):
        r += a[P[i]-1]
    return r
def B(A):
    B = ''
    for i in range(0, len(A), 6):
        b = A[i:i+6]
        # print(b)
        x = b[0]+b[-1]
        y = b[1:-1]
        B += '{:04b}'.format(S[int(i/6)][int(x, 2)*16 + int(y, 2)])
    return B
if __name__ == '__main__':

    a = '0000000100100011010001010110011110001001101010111100110111101111'
    print('a=', a)
    # 计算一轮k1 64位->56位
    KK = K(a, IP1)
    print('KK=', KK)
    # 分成2组C0 D0分别为28位 左右
    C0 = KK[0:28]
    D0 = KK[28:56]
    print('C0=', C0)
    print('D0=', D0)

    # 求K1 C0 D0分别左移
    print('C1=', C0[1:]+C0[0])
    print('D1=', D0[1:]+D0[0])
    C1D1 = C0[1:]+C0[0]+D0[1:]+D0[0]
    print('C1D1=', C1D1)
    # 置换2 56位->48
    k1 = K(C1D1, IP2)
    print('k1=', k1)

    # 明文进行IP置换 64->64
    ip = K(a, IP)
    print('ip=', ip)
    # 分一半L0 R0各32
    L0 = ip[0:32]
    R0 = ip[32:]
    print('L0=', L0)
    print('R0=', R0)

    # 再对R0进行E扩展置换 32->48
    ER0 = K(R0, E)
    print('E(R0)=', ER0)

    # 计算 ER0⊕K1 48位
    A = bin(int(ER0, 2)^int(k1, 2))[2:].zfill(len(ER0))
    print('A=', A)

    # 进行S盒子计算 A48位 分为8组每组6位，进行8个盒子计算
    B = B(A)
    print('B=', B)

    # 再进行置换P
    pb = K(B, SP)
    print('P(B)=', pb)

    # 计算 R1 = P(B) ⊕ L0
    R1 = bin(int(pb, 2)^int(L0, 2))[2:].zfill(len(pb))
    print('R1=', R1)

    # 计算L1||R1
    L1 = R0

    print('L1||R1=', L1 + R1)
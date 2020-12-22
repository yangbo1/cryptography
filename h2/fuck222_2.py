P = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024, 0.067, 0.075, 0.019, 0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.023, 0.001, 0.020, 0.001]
print(len(P))
def countT(str):
    sum = 0
    d = count(str)
    for j in range(len(d)):
        sum += d[j][1]*(d[j][1]-1)
    return sum/(len(str)*(len(str)-1))
MPT = [0 for i in range(10)]
# 求从1到m的重合指数
def countM(str, m):
    for i in range(1, m+1):
        for j in range(i):
            # print('m=', i, str[j::i])
            print('m=', i, countT(str[j::i]))
            if i == 6:
                PT = countsss(str[j::i])
                MPT[j+1] = PT
def countsss(str):
    PT = [0 for i in range(26)]
    d = countd(str)
    for i in range(26):
        if chr(i+65) in d:
            PT[i] = d[chr(i+65)] / len(str)
        else:
            PT[i] = 0
    print(str, PT)
    return PT

def countd(str):
    d = {}
    for i in str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d
def count(str):
    d = {}
    for i in str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return sorted(d.items(), key=lambda item: item[1], reverse=True)
def countn(str):
    d = {}
    dc = {}
    for k in range(3, 8):
        for i in range(len(str)-k+1):
            # print(str[i:i+k])
            if str[i:i+k] in d:
                d[str[i:i+k]] += 1
                if str[i:i+k] in dc:
                    s = list(dc[str[i:i+k]])
                    s.append(i+1)
                    dc[str[i:i + k]] = s
                else:
                    dc[str[i:i+k]] = [i+1]
            else:
                d[str[i:i+k]] = 1
                if str[i:i+k] in dc:
                    s = list(dc[str[i:i+k]])
                    s.append(i+1)
                    dc[str[i:i + k]] = s
                else:
                    dc[str[i:i+k]] = [i+1]
    print(dc)
    return sorted(d.items(), key=lambda item: item[1], reverse=True)
def fuckMg():
    print(MPT)
    MG = [[]]
    for k in range(1, 7):
        list = []
        for g in range(26):
            Mg = 0
            for i in range(26):
                # print(P[i], MPT[k][(i+g)%26])
                print(k, i, g)
                Mg +=  P[i] * MPT[k][(i+g)%26]
            print(Mg)
            list.append(Mg)
        MG.append(list)
    # print(MG[0])
    # print(MG[1])
    # print(MG[2])
    # print(MG[3])
    # print(MG[4])
    # print(MG[5])
    # print(MG[6])
    return MG
if __name__ == '__main__':
    # print(countn('FSHF PMGH TFVM AZPP ZYUB MMGZ SOVI NFUMKCZM ZSOM GZVN FFWK IVAH YZAZ SOGF KTUYGTIM GHTI MZYI BNIY WOCF USAM FZSY BUAHYCDL MFOC ILGD ZVIN CFIA VUNQ HYMI SAZMCHRU ZCHV WSFK BHAO HFPV HEHC IBIC HIVFPTIM GHTI MZYV ZSYB UAZS OSUT NHCM GHFCDOCF ULVC ZSOV ISAP ZHBA VBZS HICI BOHNCILC FNIN ZBZM DISA ZSPF CTIM ZFSM GHFC'.replace(' ','')))
    # print(count('CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBWRVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAKLXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJELXVRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHRZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJTAMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBIPEEWEVKAKOEWADREMXMTBHHCHRTKDNVRZCHRCLQOHPWQAIIWXNRMGWOIIFKEE'.replace(' ','')))
    # print(countT('CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBWRVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAKLXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJELXVRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHRZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJTAMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBIPEEWEVKAKOEWADREMXMTBHHCHRTKDNVRZCHRCLQOHPWQAIIWXNRMGWOIIFKEE'.replace(' ','')))
    # print(countM('CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBWRVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAKLXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJELXVRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHRZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJTAMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBIPEEWEVKAKOEWADREMXMTBHHCHRTKDNVRZCHRCLQOHPWQAIIWXNRMGWOIIFKEE'.replace(' ',''), 5))
    # print(countn('CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBWRVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAKLXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJELXVRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHRZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJTAMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBIPEEWEVKAKOEWADREMXMTBHHCHRTKDNVRZCHRCLQOHPWQAIIWXNRMGWOIIFKEE'.replace(' ','')))

    print(count('KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUDDKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYCQKYVXCHKFTPONCQQRHJVAJUWETMCMSPKQDYHJVDAHCTRLSVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMVGKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTJRWXBAFSPEZQNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHIFFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIYCWHJVLNHIQIBTKHJVNPIST'.replace(' ', '')))
    print(countT('KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUDDKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYCQKYVXCHKFTPONCQQRHJVAJUWETMCMSPKQDYHJVDAHCTRLSVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMVGKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTJRWXBAFSPEZQNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHIFFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIYCWHJVLNHIQIBTKHJVNPIST'.replace(' ', '')))
    tn = countn(
        'KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUDDKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYCQKYVXCHKFTPONCQQRHJVAJUWETMCMSPKQDYHJVDAHCTRLSVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMVGKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTJRWXBAFSPEZQNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHIFFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIYCWHJVLNHIQIBTKHJVNPIST'.replace(
            ' ', ''))
    print(tn)
    print(countM('KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUDDKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYCQKYVXCHKFTPONCQQRHJVAJUWETMCMSPKQDYHJVDAHCTRLSVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMVGKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTJRWXBAFSPEZQNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHIFFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIYCWHJVLNHIQIBTKHJVNPIST'.replace(' ', ''), 6))
    print(tn[0])

    MG = fuckMg()
    for i in range(len(MG)):
        if len(MG[i]) == 0:
            continue
        print(MG[i])
        minlist = [abs(k-0.065) for k in MG[i]]
        print(minlist.index(min(minlist)))
        print(chr(minlist.index(min(minlist)) + 97))
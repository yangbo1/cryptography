import numpy as np

# P = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
P = [4, 19, 0, 14, 8, 13, 18, 7, 17, 3, 11, 2, 20, 12, 22, 5, 6, 24, 15, 1, 21, 10, 9, 23, 16, 25]
m = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
M = ['d', 'l', 'r', 'y', 'v', 'o', 'h', 'e', 'a', 'x', 'w', 'p', 't', 'b', 'g', 'f', 'j', 'q', 'n', 'm', 'u', 's', 'k', '0', 'c', 'i']
m = ['d', 'l', 'r', '0', '0', 'o', 'h', 'e', 'a', '0', '0', '0', 't', '0', 'g', 'f', '0', '0', 'n', 'm', 'u', 's', '0', '0', 'c', 'i']

def aa(str):
    r = ''
    for i in str:
        if M[ord(i)-65] == '0':
            r += i
        else:
            r += M[ord(i)-65]
    return r
#通过一个简单的遍历得到a的乘法逆元，也可以通过gmpy2库中的invert函数实现
def get_inverse(a):
    for i in range(1,27):
        if a*i%26==1:
            return i
def gcd(a,b):
    if a%b == 0:
        return b
    else :
        return gcd(b,a%b)

def count(str):
    d = {}
    for i in str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return sorted(d.items(), key=lambda item:item[1], reverse=True)
def doublecount(str):
    d = {}
    print(len(str))
    for i in range(len(str)):
        if str[i] == 'H':
            # print(str[i-1] + str[i])
            if str[i-1] + str[i] in d:
                d[str[i-1] + str[i]] += 1
            else:
                d[str[i - 1] + str[i]] = 1
            if str[i] + str[i+1] in d:
                d[str[i] + str[i+1]] += 1
            else:
                d[str[i] + str[i + 1]] = 1

    return sorted(d.items(), key=lambda item:item[1], reverse=True)
def fuck(str):
    c = count(str)
    print(c)
    k1 = ord(c[0][0]) - 65
    for i in range(1, len(c)):
        k2 = ord(c[i][0]) - 65
        print(k1, k2)
        k = 0
        while ((k2-k1) + 26 * k)%15 != 0:
            k += 1
        a = ((k2-k1) + 26 * k)/15
        print(a, 'a=')
        if gcd(a, 26) == 1:
            b = k1-(4*a)
            print(a, b, 'yes')
            decipher(int(a), int(b), str)
    return str
def decipher(a, b, c):
    a_inv = get_inverse(a)
    print(a_inv)
    p=[]
    for i in c:
        temp=(((ord(i)-65)-b)*a_inv)%26+65
        p.append(chr(temp))
    print(''.join(p).lower())

if __name__ == '__main__':
    print(fuck('AOPC GUDE YKRO IFKG BEFM CPIY CRAR DEPBAQUF EPGH KJPK DDCJ GKPJ IEVC GEBE BAYCFAMC XCER IARE HAFF ERJG HCRA OKBB KYARRCED KFAI GHCP CDCK DFCB KKME FEMC GKXCOKRQ KYYE BKYC ERBH CCRJ KVEI BKPS AQKUFJRK BIDC EMEG HKFC ICRB CRQC ARQK YDERSERJ GEIQ KRIA JCPC JRKB BKKX PAOH B'.replace(' ','')))
    # print(fuck('FMXV EDKA PHFE RBND KRXR SREF MORU DSDK DVSH VUFE DKAP RKDL YEVL RHHR H'.replace(' ','')))

    # print(count('YIFQFMZRWQFYVECFMDZPCVMRZWNMDZVEJBTXCDDUMJNDIFEFMDZCDMQZKCEYFCJMYRNCWJCSZREXCHZUNMXZNZUCDRJXYYSMRTMEYIFZWDYVZVYFZUMRZCRWNZDZJJXZWGCHSMRNMDHNCMFQCHZJMXJZWIEJYUCFWDJNZDIR'))
    # print(doublecount('YIFQFMZRWQFYVECFMDZPCVMRZWNMDZVEJBTXCDDUMJNDIFEFMDZCDMQZKCEYFCJMYRNCWJCSZREXCHZUNMXZNZUCDRJXYYSMRTMEYIFZWDYVZVYFZUMRZCRWNZDZJJXZWGCHSMRNMDHNCMFQCHZJMXJZWIEJYUCFWDJNZDIR'))
    print(count('FSHF PMGH TFVM AZPP ZYUB MMGZ SOVI NFUMKCZM ZSOM GZVN FFWK IVAH YZAZ SOGF KTUYGTIM GHTI MZYI BNIY WOCF USAM FZSY BUAHYCDL MFOC ILGD ZVIN CFIA VUNQ HYMI SAZMCHRU ZCHV WSFK BHAO HFPV HEHC IBIC HIVFPTIM GHTI MZYV ZSYB UAZS OSUT NHCM GHFCDOCF ULVC ZSOV ISAP ZHBA VBZS HICI BOHNCILC FNIN ZBZM DISA ZSPF CTIM ZFSM GHFCDZGI EHMC ZHAS FMMF IVVU THMF FTUY GTIMGHTI MZYI BNIY WOCF USAI SAMG UVZA HEHBFLTI MGHT IMZY IBMF FBVI VMGH DICH SHHAHAPF CMGH TFVM LICM SFMH MGIM ZPDF UPZSZVGM GHIN FEHM KFHJ HCYZ VHVL BHIV HZTTHAZI MHBD VHSA THIS HTIZ BKZM GMGH VFBUMZFS VZPD FUYI SPFC MUSI MHBD CHYH ZEHIYFSP ZCTI MZFS HTIZ BKGZ YGZS PFCT VDFUMGIM DFUI CHMG HPZC VMFS HMFA FMGI MDFUKZBB NHIK ICAH AIUA ZVWF PPFU CON'.replace(' ','')))
    print(doublecount('FSHF PMGH TFVM AZPP ZYUB MMGZ SOVI NFUMKCZM ZSOM GZVN FFWK IVAH YZAZ SOGF KTUYGTIM GHTI MZYI BNIY WOCF USAM FZSY BUAHYCDL MFOC ILGD ZVIN CFIA VUNQ HYMI SAZMCHRU ZCHV WSFK BHAO HFPV HEHC IBIC HIVFPTIM GHTI MZYV ZSYB UAZS OSUT NHCM GHFCDOCF ULVC ZSOV ISAP ZHBA VBZS HICI BOHNCILC FNIN ZBZM DISA ZSPF CTIM ZFSM GHFCDZGI EHMC ZHAS FMMF IVVU THMF FTUY GTIMGHTI MZYI BNIY WOCF USAI SAMG UVZA HEHBFLTI MGHT IMZY IBMF FBVI VMGH DICH SHHAHAPF CMGH TFVM LICM SFMH MGIM ZPDF UPZSZVGM GHIN FEHM KFHJ HCYZ VHVL BHIV HZTTHAZI MHBD VHSA THIS HTIZ BKZM GMGH VFBUMZFS VZPD FUYI SPFC MUSI MHBD CHYH ZEHIYFSP ZCTI MZFS HTIZ BKGZ YGZS PFCT VDFUMGIM DFUI CHMG HPZC VMFS HMFA FMGI MDFUKZBB NHIK ICAH AIUA ZVWF PPFU CON'.replace(' ','')))
    print(aa('FSHF PMGH TFVM AZPP ZYUB MMGZ SOVI NFUMKCZM ZSOM GZVN FFWK IVAH YZAZ SOGF KTUYGTIM GHTI MZYI BNIY WOCF USAM FZSY BUAHYCDL MFOC ILGD ZVIN CFIA VUNQ HYMI SAZMCHRU ZCHV WSFK BHAO HFPV HEHC IBIC HIVFPTIM GHTI MZYV ZSYB UAZS OSUT NHCM GHFCDOCF ULVC ZSOV ISAP ZHBA VBZS HICI BOHNCILC FNIN ZBZM DISA ZSPF CTIM ZFSM GHFCDZGI EHMC ZHAS FMMF IVVU THMF FTUY GTIMGHTI MZYI BNIY WOCF USAI SAMG UVZA HEHBFLTI MGHT IMZY IBMF FBVI VMGH DICH SHHAHAPF CMGH TFVM LICM SFMH MGIM ZPDF UPZSZVGM GHIN FEHM KFHJ HCYZ VHVL BHIV HZTTHAZI MHBD VHSA THIS HTIZ BKZM GMGH VFBUMZFS VZPD FUYI SPFC MUSI MHBD CHYH ZEHIYFSP ZCTI MZFS HTIZ BKGZ YGZS PFCT VDFUMGIM DFUI CHMG HPZC VMFS HMFA FMGI MDFUKZBB NHIK ICAH AIUA ZVWF PPFU CON'.replace(' ','')))


    print(gcd(108, 126))
    print(gcd(18, 264))
    print(gcd(6, 318))
    print(gcd(6, 330))
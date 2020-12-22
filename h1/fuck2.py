def fuck(str, kstr):
    kl = []
    for ks in kstr:
        k = ord(ks) - 97
        # print(k)
        kl.append(k)
    lk = len(kl)
    r = ''
    for i in range(len(str)):
        if str[i].islower():
            r += chr((ord(str[i]) - 97 + kl[i%lk])%26 + 97)
        else:
            r += str[i]
    print(r)
    return r
def fucku(str, kstr):
    kl = []
    for ks in kstr:
        k = ord(ks) - 97
        # print(k)
        kl.append(k)
    lk = len(kl)
    r = ''
    for i in range(len(str)):
        if str[i].islower():
            r += chr((ord(str[i]) - 97 - kl[i%lk])%26 + 97)
        else:
            r += str[i]
    print(r)
    return r
if __name__ == '__main__':
    fuck('we are discovered, save yourself,', 'friday')
    fucku('bv drc uqvcmavzhd, jiye dfcuscqw,', 'friday')
    fuck('wearediscoveredsaveyourself', 'friday')
    fucku('bviuebnjkrvcwvlvatjpwxrqjcn', 'friday')

    fucku('KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUDDKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYCQKYVXCHKFTPONCQQRHJVAJUWETMCMSPKQDYHJVDAHCTRLSVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMVGKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTJRWXBAFSPEZQNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHIFFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIYCWHJVLNHIQIBTKHJVNPIST'.lower(), 'crypto')
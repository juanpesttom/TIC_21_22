def sustituye_vocales():
    x = raw_input()
    res = ''
    for c in x:
        if c.lower() in 'aeio':
            res += 'u'
        else:
            res += c
    print res
            
sustituye_vocales()

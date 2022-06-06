def remove(string):
    last_number = "!" * (len(string) - len(string.rstrip('!')))
    return string.replace("!", "") + last_number

remove('LCEMINUBMEANV!HXVVKG!!!')

def lmao(s):
    return print(s.replace('!', '') + '!' * (len(s) - len(s.rstrip('!'))))
lmao('LCEMINUBMEANV!HXVVKG!!!')

def lmaos(s):
    print(s.replace('!', ''))
    print((len(s)))
    print(len(s.rstrip('!')))

lmaos('LCEMINUBMEANV!HXVVKG!!!')
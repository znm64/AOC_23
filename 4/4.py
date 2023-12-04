raw = [i.strip() for i in open('data.txt', 'r').readlines()]

def getnums(raw):
    lines = []
    current = ''
    for i in raw:
        current = (i[i.index(':')+1:].strip())
        current.split('|')
    print(current)

getnums(raw)
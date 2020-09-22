def x(z):
    y = ['A', 'B', 'C', 'D']
    d = ''
    for u in z:
        for r in u:
            if r not in y and ord(r) < 87:
                d += r
    return d
print(x(['BED','FHY']))
print(x('CLOSET'))
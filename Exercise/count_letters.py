def count_letter(param_1):
    vagharlar = []
    new = ""
    d = {}
    para_1 = param_1.lower()
    for i in para_1:
        vagharlar.append(i)
    for s in vagharlar:
        if s.isalpha():
            d[s] = vagharlar.count(s)
    for k, v in d.items():
        w = str(v) + k
        new += w + ", "
    return new[:-2]

#print(count_letter("abbcc"))

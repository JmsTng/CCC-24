typed = input()
out = input()
quiet = '-'
silly = [list(set(typed).difference(set(out))), list(set(out).difference(set(typed)))[0]]

if len(silly[0]) == 1:
    print(silly[0][0], silly[1])
    print(quiet)
else:
    t1 = "".join([c for c in typed if c != silly[0][0]])
    t1 = t1.replace(silly[0][1], silly[1])

    if t1 == out:
        print(silly[0][1], silly[1])
        print(silly[0][0])
    else:
        print(silly[0][0], silly[1])
        print(silly[0][1])


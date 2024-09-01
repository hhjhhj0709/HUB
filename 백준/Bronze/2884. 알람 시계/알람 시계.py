ho,mi=map(int,input().split())

if mi>=45 and mi<=59 and ho<=24:
    mi=mi-45
elif mi<=45:
    if ho==0 :
        ho=23
        mi=mi+60
        mi=mi-45
    else:
        ho=ho-1
        mi=mi+60
        mi=mi-45

print(ho,mi)
from dish_count import *
from all_count import *


def f(brek, lun, din, sna):
    k = 1
    all = brek + lun + din + sna
    if q1 == 'gain' or 'dry':
        if f_kkal < all or bel < proteine:
            all *= k
            proteine *= k
            k += 0.1
        else:
            all /= 100
            fin = round(all, 0)
            fin *= 100
            brek = fin * 0.2
            lun = fin * 0.4
            din = fin * 0.4
            return(brek, lun, din, sna)
    else:
        if f_kkal < all:
            all *= k
            k += 0.1
        else:
            all /= 100
            fin = round(all, 0)
            fin *= 100
            brek = fin * 0.2
            lun = fin * 0.4
            din = fin * 0.4
            return(brek, lun, din, sna)
print(f(brek, lun, din, sna))

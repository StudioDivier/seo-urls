from functools import lru_cache


def dist(a, b):
    @lru_cache(maxsize=len(a) * len(b))
    def rec(i, j):
        if i == 0 or j == 0:
            return max(i, j)
        elif a[i-1] == b[j-1]:
            return rec(i-1, j-1)
        else:
            return 1 + min(
                rec(i, j-1),
                rec(i-1, j),
                rec(i-1, j-1),
            )
    return rec(len(a), len(b))


str1 = '/kraski_i_emali/obshchestroitelnye/khv_124'
str11 = '/kraski_i_emali/interernye/dlya-gipsokartona/tikkurila_harmony'
str2 = 'khv_124'

lev = dist(str11, str2)
bigger = max([len(str11), len(str2)])
pct = ((bigger - lev) / bigger) * 100
print("srt 1: {}\n str 2: {}\n===\n Сложность: {}%".format(str11, str2, pct))
print("levi: {}".format(lev))




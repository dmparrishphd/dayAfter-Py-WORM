def dayAfter(ymd):
    LAST_DAY_OF_MONTH = ( # FAQ: Q: WHY 29? A: SEE LOGIC OF dayAfter_.
        None, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    def isLeap(y):
        return \
            True  if not y % 400 else \
            False if not y % 100 else \
            True  if not y %   4 else \
            False
    def dayAfter_(ymd):
        y, m, d = ymd
        if m, d == 2, 28:
            return (y, m, 29) if isLeap(y) else (y, 3, 1)
        if d == LAST_DAY_OF_MONTH[m]:
            return (y + 1, 1, 1) if m == 12 else (y, m + 1 , 1)
        return y, m, d + 1
    return dayAfter_(ymd)

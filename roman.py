def roman(a):
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    inc = 0
    for i in range(len(a)):
        if i > 0 and val[a[i]] > val[a[i - 1]]:
                inc += val[a[i]] - 2 * val[a[i - 1]]
        else:
                inc += val[a[i]]
    return inc

str=raw_input()
print(roman(str))

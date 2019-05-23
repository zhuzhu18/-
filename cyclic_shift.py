'''
给定一个数组,循环右移位k位
'''
def cyclic_shift(a, k):

    n = len(a)
    start = 0

    for i in range(n-k, n):
        temp = a[i]
        for j in range(i, start, -1):
            a[j] = a[j-1]
        a[start] = temp
        start += 1

    return a


if __name__ == "__main__":

    given_array = list(eval(input('输入需要循环右移的数组(以逗号分隔)：')))
    k = eval(input('输入右移次数：'))
    print("\nbefore shift:", given_array)
    result = cyclic_shift(given_array, k)
    print("\nafter shift:", result)

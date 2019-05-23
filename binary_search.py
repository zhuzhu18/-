def bin_search(key,k,low=None,high=None):
    if low > high:
        print('查找失败')
    else:
        mid = (low+high) >> 1
        if k == key[mid]:
            return mid
        elif k > key[mid]:
            low = mid + 1
            return bin_search(key, k, low, high)
        else:
            high = mid - 1
            return bin_search(key, k, low, high)


if __name__ == '__main__':
    A = [2,3,5,7,8,10,12,15,19,21]
    loc = bin_search(A, 15, 0, len(A)-1)
    print(loc)

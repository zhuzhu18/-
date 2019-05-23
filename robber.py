#相邻两间房子有防盗连接，不能同时偷盗
# 前 i 间房子盗窃金额为 money[i] 元
def get_money(num):
    if len(num) == 0:
        return num(len(num)-1)
    elif len(num) == 1:
        return max(num[0],num[1])
    else:
        money = [0]*len(num)
        money[0] = num[0]
        money[1] = max(num[0],num[1])
        for index in range(2,len(num)):
            money[index] = max(money[index-1],money[index-2] + num[index])
        return money[len(num)-1]
profit = get_money([1,6,5,4,2,9,3,7,8])
print(profit)

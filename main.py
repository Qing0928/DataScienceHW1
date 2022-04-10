import matplotlib.pyplot as plt
import time

userBuyList = {}
productList = []
productSell = {}#dict

def UserProduct(line):
    if ('userId' not in line) and ('productId' not in line):
        return False
    elif 'userId' in line:
        if 'unknown' in line:
            return False
        else:
            userID = line.strip('review/userId: ')
            if userID in userBuyList:
                userBuyList[userID] = userBuyList[userID] + 1
                return True
            else:
                userBuyList[userID] = 1
                return True

    elif 'productId' in line:
        productID = line.strip('product/productId: ')
        if productID in productSell:
            productSell[productID] = productSell[productID] + 1
        else:
            productSell[productID] = 1
        return True

def Median(productSell):
    totalLen = len(productSell)
    if totalLen % 2 != 0:
        midPointNum = totalLen // 2
        midPoint = list(productSell.keys())[midPointNum]
        median = productSell[midPoint]

        return median
    else:
        midPointNum = totalLen // 2
        midPoint = list(productSell.keys())[midPointNum]
        midPointPre = list(productSell.keys())[midPointNum - 1]
        median = (productSell[midPointPre] + productSell[midPoint]) / 2

        return median

start = time.time()
with open('Music.txt', 'r') as file:
    for index, line in enumerate(file):
        if index%1000000 == 0:
            print(index)
        if UserProduct(line=line):
            pass
        else:
            continue

sortedproductSell = sorted(productSell.items(), reverse=True, key=lambda x:x[1])
userBuyList = dict(sorted(userBuyList.items(), key=lambda x:x[0]))

user = len(userBuyList.keys())
print(f'There are {user} unique users\n-------------------------')

product = len(productSell.keys())
print(f'There are {product} unique products\n-------------------------')

bsProduct = sortedproductSell[1]
print(f'The maximum number of products bought by a user is {bsProduct[1]}\n-------------------------')

medianValue = Median(productSell=dict(sortedproductSell))
print(f'Median is {medianValue}\n-------------------------')

print('First ten users who have median \n')
userBuyListKey = list(userBuyList.keys())
count = 0
for i in userBuyListKey:
    if count > 9:
        break
    elif userBuyList[i] == medianValue:
        print(i.strip('\n'))
        count += 1
    else:
        continue
end = time.time()
timeUse = end - start
print(f'Time use {timeUse}s')

pltxAxis = []
pltyAxis = []
pltData = dict(sortedproductSell)
pltDataKey = list(pltData.keys())
count = 0
for i in pltDataKey:
    if count > 9:
        break
    else:
        pltxAxis.append(i)
        pltyAxis.append(pltData[i])
    count+=1

plt.bar(pltxAxis, pltyAxis)
plt.ylabel('count')
plt.xlabel('productID')
plt.show()

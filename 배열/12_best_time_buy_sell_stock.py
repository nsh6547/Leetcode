import sys
input = [7,1,5,3,6,4]
output = 5
input2 = [7,6,5,4,3,1]
output = 0

profit = -sys.maxsize
min_price = sys.maxsize
for price in input:
    min_price = min(price, min_price)
    profit = max(profit,price-min_price)

print(min_price)

##########내 풀이 브루스포스계산 #1
#result=[]
#for i in range(0,len(input)):
#    for j in range(i+1,len(input)):
 #       if input[i]<input[j] :
  #          result.append(input[j]-input[i])
#print(max(result))
#print(result)


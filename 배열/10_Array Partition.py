input =[1,4,3,2]


#풀이3 파이썬다운 방식
# print( sum(sorted(input)[::2]))



#################풀이 2 (짝수 번째 값 )
# sum=0
# input.sort()
#
# for i, n in enumerate(input):
#     if i%2==0 :
#         sum += n
#
# print(sum)


## 풀이 1 오름차순
# sum =0
# pair = []
# input.sort()
# print(input)
#
# for n in input:
#     pair.append(n)
#     if len(pair) ==2:
#         sum += min(pair)
#         pair=[]
# print(sum)

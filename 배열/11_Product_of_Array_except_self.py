input = [1,2,3,4]
output= [24,12,8,6]
out =[]
p=1

### 퓰이 1
for i in range(0,len(input)):
    out.append(p)
    p *= input[i]
p=1
for i in range(len(input)-1,-1,-1):
    out[i] *= p
    p *= input[i]
    print(i)



#

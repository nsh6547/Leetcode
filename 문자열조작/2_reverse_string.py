s = ["h", "e", "l", "l", "o"]
print(s)
left,right =0, len(s)-1
print(left,right,end='')
print(s)
while left<right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1

print(s)
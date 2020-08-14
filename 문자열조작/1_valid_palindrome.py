import collections
from typing import Deque
import re

input= "A man, a plan, a canal: Panama"
input1= "race a car"

s = input.lower()
s = re.sub('[^a-z0-9]','',input)
print(s)

# class Solution: # 풀이 3 슬라이싱 사용 Runtime: 20ms
#     def isPalindrome(self, s: str) -> bool:
#         s= s.lower()
#         s= re.sub('[^a-z0-9]','', s)
#         return s == s[::-1]

# class Solution: 풀이 2 데크 자료형을 이용한 최적화 Runtime: 44ms
#     def isPalindrome(self, s: str) -> bool:
#
#         strs: Deque = collections.deque()
#
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())
#
#         while len(strs) > 1:
#             if strs.popleft() != strs.pop():
#                 return False
#
#         return True

#
# class Solution: # 풀이 1 리스트로 변환 Runtime: 288ms
#     def isPalindrome(self, s: str) -> bool:
#         strs = []
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())
#
#         while len(strs) > 1:
#             if strs.pop(0) != strs.pop:
#                 return False
#
#         return True

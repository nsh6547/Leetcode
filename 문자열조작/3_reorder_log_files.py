logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]


class Solution:
        letters,digits=[],[]

        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)

            else:
                letters.append(log)
        print(digits)
        print(letters)
        letters.sort(key=lambda x:(x.split()[1:], x.split()[0]))
        print(digits)
        print(letters)

        print(letters + digits)
#
# for l in logs:
#     print(l.split())
# letters, digits =[], []
#
# for log in logs:
#     if log.split()[1].isdigit():
#         digits.append(log)
#     else:
#         letters.append(log)
#
# letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
# print(letters + digits)
# a = [97, 8, 98, 89, 4, 5, 6, 646, 73, 9, 75, 46, 686, 78, 86, 5654, 57, 58]
#
# for i in range(len(a)):
#     for j in range(i, len(a) - 1):
#         j += 1
#         if a[i] > a[j]:
#             c = a[i]
#             a[i] = a[j]
#             a[j] = c
# print(a)
#

"""

冒泡

a = [97, 8, 98, 89, 4, 5]

for i in range(len(a)):
    for j in range(i, len(a) - 1):
        j += 1
        dd=a[j]
        if a[i] > a[j]:
            c = a[i]
            a[i] = a[j]
            a[j] = c

print(a)

"""

from multiprocessing import Pool, Manager
if __name__ == '__main__':


    que = Manager().Queue()
    headers = {"Content-Type": "application/json", "x-token": "",
               "x-countryCode": 'us'}
    url = 'https://api-t-9.azazie.com/1.0/user/register'
    data = [[url, "syt" + str(i)+'@tetx.com', '123456'] for i in range(20)]
    for i in data:
        que.put(i)
    print(que.qsize())


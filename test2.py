# aa= '1059311 1058823 1058823 1059313 1059313 1059313 1059302 1059301 1059312 1059326 1059314 1059324 1059307 1059303 1059320 1059318'
# print(aa.replace(' ',','))
#
# bb =[1059311,1058823,1058823,1059313,1059313,1059313,1059302,1059301,1059312,1059326,1059314,1059324,1059307,1059303,1059320,1059318
# ]
# print(set(bb))


import requests

ccc = [1006431, 1009633, 1051097, 1052924, 1006446, 1052846, 1051099, 1004452, 1052664]
for i in ccc:
    url = f'https://apix-p5.azazie.com/1.0/product/first-screen?goods_id={i}'

    headers = {"Content-Type": "application/json", "x-app": 'pc', "x-token": "",
               "x-project": "azazie", "x-countryCode": 'us', "languageCode": "en"}

    res = requests.get(url, headers=headers)
    dd = res.json()['data']['styleInfo']['color']
    li = []
    for k, v in dd.items():
        li.append(k)
    print(i)
    for j in li:
        print((0, i, 7, j, 0, 'us', '2023-04-26 23:41:18', '2023-04-26 23:41:18'))

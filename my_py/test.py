from multiprocessing import Pool, Manager
import requests
if __name__ == '__main__':

    que = Manager().Queue()
    headers = {"Content-Type": "application/json", "x-token": "",
               "x-countryCode": 'us'}
    url = 'https://api-t-9.azazie.com/1.0/user/register'
    data = [[url, "syt" + str(i) + '@tetx.com', '123456'] for i in range(20)]
    for i in data:
        que.put(i)
    print(que.qsize())

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

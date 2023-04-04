import requests

header = {"Content-Type": "application/json",
          "Accept": "application/json",
          "x-app": "pc",
          "x-token": "",
          "x-project": "azazie",
          "x-countryCode": "US",
          "authorization": "Basic bGViYmF5OnBhc3N3MHJk",
          "x-languagecode": "en"
          }

header2 = {"Content-Type": "application/json",
           "Accept": "application/json",
           "x-app": "pc",
           "x-token": "",
           "x-project": "azazie",
           "x-countryCode": "it",
           "authorization": "Basic bGViYmF5OnBhc3N3MHJk",
           "x-languagecode": "it"

           }
url = 'https://www.azazie.com/prod/1.0/list/content?cat_name=events-dresses&dress_type=dress&page=1&limit=60&in_stock=&sort_by=popularity&is_outlet=0&version=b&activityVerison=a&galleryVersion=A'


def func(url1):
    res = requests.post(url=url1, headers=header)
    goods_list = res.json()['data']['goodsIdList']
    print(goods_list)
    res2 = requests.post(url=url, headers=header2)
    goods_list2 = res2.json()['data']['goodsIdList']
    print(set(goods_list2)-set(goods_list))
    print(set(goods_list)-set(goods_list2))


func(url)
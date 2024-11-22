import requests
from handle_database import Database

headers = {"Content-Type": "application/json", "x-token": "",
           "x-countryCode": 'us'}

url = 'http://common-prod.opsfun.com/stock/v2/goodsId?warehouse=7&business_id=65582&goods_id=1000291'


def stock_v2():
    res = requests.get(url=url, headers=headers)
    list1 = res.json()['data']['1000291']
    for i in list1:
        if i['available_quantity'] == 0:
            print(i['sku'])


def get_color_name(db: Database, style_id):
    sql = f'SELECT * FROM `style` WHERE style_id ={style_id}'
    print(db.get_fetchall(sql))


if __name__ == '__main__':
    db = Database(
        user='azazie',
        password='azazie',
        host='db-zt.opsfun.com'
    )
    get_color_name(db, 1654)

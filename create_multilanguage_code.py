import requests

lego_url = ''
user = {}


def lego_login():
    url = 'https://api-t-1-lego.azazie.com/auth/login'
    data = {"username": "admin", "password": "lb123456"}
    res = requests.post(url, data)
    return res.json()['data']['token']


import requests

list_language = ['fr', 'de', 'es', 'it', ]


# return= {'fr': 'rouge', 'de': 'Rot', 'es': 'rojo', 'it': 'rosso'}
def google_translate(text, languages, src_lang='auto'):
    googleapis_url = 'https://translate.googleapis.com/translate_a/single'
    dict1 = {}
    for language in languages:
        url = '%s?client=gtx&sl=%s&tl=%s&dt=t&q=%s' % (googleapis_url, src_lang, language, text)
        data = requests.get(url).json()
        res = ''.join([s[0] for s in data[0]])
        dict1[language] = res
    return dict1


def create_codes(token, codes):
    url = 'https://api-t-1-lego.azazie.com/config/multilanguage/save'
    header = {"token": token}
    for i in codes:
        data = {"multilanguageId": 0,
                "code": "page_common_order_progress_order_placed_desc",
                "en": "We have received your order and a confirmation email was sent to {email}."}
        res = requests.post(url, data, headers=header)
        print(res.json())


if __name__ == '__main__':
    token = lego_login()
    # create_codes(token)
    # google_translate('red', list_language)

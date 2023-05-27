from selenium.webdriver.common.by import By

en_us = "- Shop 500+ bridesmaid dresses, from $69 to $169\n" \
        "- Shop 200+ wedding dresses, starting at $109\n" \
        "- Try on SAMPLE DRESSES for $10-$15\n" \
        "- Don't miss out the FLASH SALE!"

de_DE = "- Shoppen Sie 500+ Brautjungfernkleider, von 99€ bis 209€\n" \
        "- Shoppen Sie 200+ Brautkleider, ab 289€\n" \
        "- Verpassen Sie nicht den FLASH SALE!"

fr_FR = "- Acheter plus de 500 robes de demoiselle d'honneur, de €89 à €179\n" \
        "- Acheter plus de 250 robes de mariée, à partir de €259\n" \
        "- Ne manquez pas la VENTE FLASH !"

en_CA1 = "Shop 500+bridesmaid dresses, from CA$99 to CA$339\n" \
         "Shop 200+wedding dresses, starting at CA$323\n" \
         "Try on SAMPLE DRESSES for CA$15-CA$20\n" \
         "Don't miss out the FLASH SALE!"

es_MX = "- Compra más de 500 vestidos de dama de honor, desde MXN$2399 hasta MXN$4799\n" \
        "- Compra más de 250 vestidos de novia, desde MXN$6899\n" \
        "- ¡No te pierdas la VENTA FLASH!\n"

es_ES = "- Compre más de 500 vestidos de dama de honor, desde 99€ a 239€\n" \
        "- Compre más de 200 vestidos de novia, desde 259€\n" \
        "- ¡No te pierdas la OFERTA FLASH!"

it_IT = " - Acquista oltre 500 abiti da damigella, da 99€ a 239€\n" \
        " - Acquista oltre 200 abiti da sposa, a partire da 259€\n" \
        " - Prova campioni per 10€\n" \
        " - Non perdetevi la VENDITA FLASH"

en_AU = "- Shop 500+ bridesmaid dresses, from AU$129 to AU$259\n" \
        "- Shop 250+ wedding dresses, starting at AU$379\n" \
        "- Don't miss out the FLASH SALE!"

en_CA = " Shop 500+bridesmaid dresses, from CA$99 to CA$339\n" \
        " Shop 200+wedding dresses, starting at CA$323\n" \
        " Try on SAMPLE DRESSES for CA$15-CA$20\n" \
        " Don't miss out the FLASH SALE!"

en_GB = "- Shop 500+ bridesmaid dresses, from ￡79 to ￡159\n" \
        "- Shop 250+ wedding dresses, starting at ￡229\n" \
        "- Don't miss out the FLASH SALE!"

en_describe = ""
de_describe = ""
fr_describe = ""
it_describe = ""
es_describe = ""

save_button_loc = By.XPATH, '//button[text()="存储"]'
country_button_loc = By.XPATH, '//button[@role="button"]'
promotion_input_box_loc = By.XPATH, '//div[@name="promotionalText"]'
new_describe_loc = By.XPATH, '//div[@name="whatsNew"]'

country_en_US_loc = By.XPATH, '//DIV[text()="英文（美国）"]'
country_de_DE_loc = By.XPATH, '//DIV[text()="德文"]'
country_fr_FR_loc = By.XPATH, '//DIV[text()="法文"]'
country_en_CA1_loc = By.XPATH, '//DIV[text()="法文（加拿大）"]'
country_es_MX_loc = By.XPATH, '//DIV[text()="西班牙文（墨西哥）"]'
country_es_ES_loc = By.XPATH, '//DIV[text()="西班牙文（西班牙）"]'
country_it_IT_loc = By.XPATH, '//DIV[text()="意大利文"]'
country_en_AU_loc = By.XPATH, '//DIV[text()="英文（澳大利亚）"]'
country_en_CA_loc = By.XPATH, '//DIV[text()="英文（加拿大）"]'
country_en_GB_loc = By.XPATH, '//DIV[text()="英文（英国）"]'

country_list = [

    {"loc": country_en_US_loc, "v1": en_us, "v2": en_describe},
    {"loc": country_de_DE_loc, "v1": de_DE, "v2": de_describe},
    {"loc": country_fr_FR_loc, "v1": fr_FR, "v2": fr_describe},
    {"loc": country_en_CA1_loc, "v1": en_CA1, "v2": en_describe},
    {"loc": country_es_MX_loc, "v1": es_MX, "v2": es_describe},
    {"loc": country_es_ES_loc, "v1": es_ES, "v2": es_describe},
    {"loc": country_it_IT_loc, "v1": it_IT, "v2": it_describe},
    {"loc": country_en_AU_loc, "v1": en_AU, "v2": en_describe},
    {"loc": country_en_CA_loc, "v1": en_CA, "v2": en_describe},
    {"loc": country_en_GB_loc, "v1": en_GB, "v2": en_describe}
]

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Compose


def get_price(price):
    price = price.strip('$')
    price = float(price)
    return price

class AllforyouSgLoader(ItemLoader):
   
    title_in = MapCompose(unicode.strip)
    title_out = Join()

    description_in = MapCompose(unicode.strip)
    description_out = Join()

    retailer_sku_code_in = MapCompose(unicode.strip)
    retailer_sku_code_out = Join()

    url_in = MapCompose(unicode.strip)
    url_out = Join()

    promo_data_in = MapCompose(unicode.strip)
    promo_data_out = Join()

    #selqty_in = MapCompose(unicode.strip)
    #selqty_out = Join()

    price_in = MapCompose(unicode.strip, get_price)
    price_out = Compose()

    current_price_in = MapCompose(unicode.strip)
    current_price_out = Join()

    #add2cart_in = MapCompose(unicode.strip)
    #add2cart_out = Join()

    #add2list_in = MapCompose(unicode.strip)
    #add2list_out = Join()

    instock_in = MapCompose(unicode.strip)
    instock_out = Join()
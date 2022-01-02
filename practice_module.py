# import theater_module
# theater_module.price(3) # 3인의 영화표 가격
# theater_module.price_morning(4) # 4인의 조조할인 영화표 가격
# theater_module.price_soldier(5) # 5인(군인)의 영화표 가격

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(5)
# price_morning(6)

from theater_module import price_soldier as price
price(5)
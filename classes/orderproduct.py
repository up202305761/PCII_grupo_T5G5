# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2022)
#objective: class OrderProduct

"""""



from classes.customerorder import CustomerOrder
from classes.product import Product
# Import the generic class
from classes.gclass import Gclass



class OrderProduct(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 2

    # class attributes, identifier attribute must be the first one on the list
    att = ['_order_code','_product_code','_quantity','_price']
    # Class header title
    header = 'Escolha dos produtos'
    # field description for use in, for example, in input form
    des = ['Código da encomenda','Código do produto','Quantidade','Preço']
    # Constructor: Called when an object is instantiated
    def __init__(self, order_code, product_code, quantity, price):
        super().__init__()

        # self._quantity = float(quantity)
        # self._price = float(price)
        # Object attributes
        # Check the order and product referential integrity
        if order_code in CustomerOrder.lst:
            if product_code in Product.lst:
                product=Product.obj[product_code]
                if int(quantity) <= product.stock and float(price)>=product.price:
                    self._order_code = order_code
                    self._product_code = product_code
                    self._quantity = float(quantity)
                    self._price = float(price)
                    # Add the new object to the OrderProduct list
                    code = str(order_code) + str(product_code)
                    OrderProduct.obj[code] = self
                    OrderProduct.lst.append(code)
                    product.stock-=float(quantity)
                    Product.update(product_code) 
                elif int(quantity) > Product.obj[product_code].stock:
                    print('Não existe stock do produto ', product_code )
                else:
                    print ('O preço de venda deve ser superior a ', product.price )
            else:
                print('Produto ', product_code, ' não encontrado')
        else:
            print('Encomenda ', code, ' não encontrada')

    # Object properties
    # order property getter method
    @property
    def code(self):
        return self._code
    # product property getter method
    @property
    def product_code(self):
        return self._product_code
    # quantity property getter method
    @property
    def quantity(self):
        return self._quantity
    # quantity property setter method
    @quantity.setter
    def quantity(self, quantity):
        self._quantity = float(quantity)
    # price property getter method
    @property
    def price(self):
        return self._price
    # price property setter method
    @price.setter
    def price(self, price):
        self._price = float(price)



# class OrderProduct(Gclass):
#     obj = dict()
#     lst = list()
#     pos = 0
#     sortkey = ''
#     auto_number = 0
#     nkey = 2

#     # class attributes, identifier attribute must be the first one on the list
#     att = ['_order_code','_product_code','_quantity','_price']
#     # Class header title
#     header = 'Escolha dos produtos'
#     # field description for use in, for example, in input form
#     des = ['Código da encomenda','Código do produto','Quantidade','Preço']
#     # Constructor: Called when an object is instantiated
#     def __init__(self, order_code, product_code, quantity, price):
#         super().__init__()
#         # Object attributes
#         # Check the order and product referential integrity
#         if order_code in CustomerOrder.lst:
#             if product_code in Product.lst:
#                 product=Product.obj[product_code]
#                 if int(quantity) <= Product.obj[product_code].stock and float(price)<=Product.obj[product_code].price:
#                     self._order_code = order_code
#                     self._product_code = product_code
#                     self._quantity = float(quantity)
#                     self._price = float(price)
#                     # Add the new object to the OrderProduct list
#                     code = str(order_code) + str(product_code)
#                     OrderProduct.obj[code] = self
#                     OrderProduct.lst.append(code)
#                     product.stock-=quantity
#                 elif int(quantity) > Product.obj[product_code].stock:
#                     print('Não existe stock do produto ', product_code )
#                 else:
#                     print ('O preço de venda deve ser superior a ', product.price )
#             else:
#                 print('Produto ', product_code, ' não encontrado')
#         else:
#             print('Encomenda ', order_code, ' não encontrada')

#     # Object properties
#     # order property getter method
#     @property
#     def order_code(self):
#         return self._order_code
#     # product property getter method
#     @property
#     def product_code(self):
#         return self._product_code
#     # quantity property getter method
#     @property
#     def quantity(self):
#         return self._quantity
#     # quantity property setter method
#     @quantity.setter
#     def quantity(self, quantity):
#         self._quantity = float(quantity)
#     # price property getter method
#     @property
#     def price(self):
#         return self._price
#     # price property setter method
#     @price.setter
#     def price(self, price):
#         self._price = float(price)
   


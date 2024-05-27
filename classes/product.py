# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2022)
#objective: class Product

"""""
#%% Class Product
# Import the generic class
from classes.gclass import Gclass


class Product(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0 # = 1 in case of auto number on
    nkey = 1
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_name','_price','_stock']
    # Class header title
    header = 'Produtos'
    # field description for use in, for example, in input form
    des = ['Código','Nome','Preço','Stock']
    # Constructor: Called when an object is instantiated
    def __init__(self, code, name, price, stock):
        super().__init__()
        self._code = code
        self._name = name
        self._price = float(price)
        self._stock = int(stock)
        
        if code in Product.obj:
            existing_product = Product.obj[code]
            
            self._price = round(((self._price * self._stock) + (existing_product.price * existing_product.stock)) / (self._stock + existing_product.stock),2)
            self._stock += existing_product.stock
            # Product.remove(code)
            # Product.update(code)
        
        Product.obj[code] = self
        Product.lst.append(code)
        Product.update(code)
            
    # Object properties
    # code property getter method
    @property
    def code(self):
        return self._code
    # name property getter method
    @property
    def name(self):
        return self._name
    # price property getter method
    @property
    def price(self):
        return self._price
    
    # price property setter method
    @price.setter
    def price(self, price):
        self._price = price
    # stock property getter method
    @property
    def stock(self):
        return self._stock
    # stock property setter method
    @stock.setter
    def stock(self, stock):
        self._stock = stock


    # def __init__(self, code, name, price, stock):
    #     super().__init__()
    #     # Uncomment in case of auto number on
    #     # if code == 'None':
    #     #     codes = Product.getatlist('_code')
    #     #     if codes == []:
    #     #         code = str(1)
    #     #     else:
    #     #         code = str(max(map(int,Product.getatlist('_code'))) + 1)
    #     # Object attributes
    #     # if code not in Product.obj.code:
    #     # self._code = code
    #     # self._name = name
    #     # self._price = float(price)
    #     # self._stock = int(stock)
        
    #     # # Add the new object to the Product list
    #     # Product.obj[code] = self
    #     # Product.lst.append(code)
    #     if code in Product.obj:
    #         self._code = code 
    #         self._name=name 
    #         self._price= ((float(price)*int(stock))+(Product.obj[code].price*Product.obj[code].stock))/(Product.obj[code].stock+int(stock))
    #         self._stock= Product.obj[code].stock+int(stock) 
            
    #         Product.remove(code)
    #         Product.obj[code]=self 
    #         Product.lst.append(code)
            
    # Object properties
    # code property getter method
    @property
    def code(self):
        return self._code
    # name property getter method
    @property
    def name(self):
        return self._name
    # price property getter method
    @property
    def price(self):
        return self._price
    
    # price property setter method
    @price.setter
    def price(self, price):
        self._price = price
    # stock property getter method
    @property
    def stock(self):
        return self._stock
    # stock property setter method
    @stock.setter
    def stock(self, stock):
        self._stock = stock
    # foto property setter method
   

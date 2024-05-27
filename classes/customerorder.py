# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2022)
#objective: class Order

"""""
#%% Class Order
import datetime
from classes.customer import Customer
# Import the generic class
from classes.gclass import Gclass

class CustomerOrder(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 1 # = 1 in case of auto number on
    nkey = 1
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_customer_code']
    # Class header title
    header = 'Encomendas'
    # field description for use in, for example, in input form
    des = ['Código','Código do cliente']
    # Constructor: Called when an object is instantiated
    def __init__(self, code, customer_code):
        super().__init__()
        # Uncomment in case of auto number on
        if code == 'None':
            codes = CustomerOrder.getatlist('_code')
            if codes == []:
                code = str(1)
            else:
                code = str(max(map(int,CustomerOrder.getatlist('_code'))) + 1)
        # Object attributes
        # Check the customer referential integrity
        if customer_code in Customer.lst:
            self._code = code
            
            self._customer_code = customer_code
            # Add the new object to the Order list
            CustomerOrder.obj[code] = self
            CustomerOrder.lst.append(code)
        else:
            print('Cliente ', customer_code, ' não encontrado')
    # Object properties
    # code property getter method
    @property
    def code(self):
        return self._code

    # customer property getter method
    @property
    def customer_code(self):
        return self._customer_code
    # customer property setter method
    @customer_code.setter
    def customer_code(self, customer_code):
        if customer_code in Customer.lst:
            self._customer_code = customer_code
        else:
            print('Cliente ', customer_code, ' não encontrado')    
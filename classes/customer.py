# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2021)
#objective: class Customer_login

"""""
#%% Class Customer_login
# Import the generic class
from classes.gclass import Gclass

class Customer(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_name','_address','_email','_login']
    # Class header title
    header = 'Clientes'
    # field description for use in, for example, in input form
    des = ['Código','Nome','Morada','Email','Nome do utilizador']
    # Constructor: Called when an object is instantiated
    def __init__(self, code,name,address,email,login):
        super().__init__()
        # Object attributes
        self._code = code
        self._name = name
        self._address = address
        self._email = email
        self._login = login
        # Add the new object to the Customer_login list
        Customer.obj[code] = self
        Customer.lst.append(code)

    # Object properties
    # getter methodes
    # code property getter method
    @property
    def code(self):
        return self._code
    # name property getter method
    @property
    def name(self):
        return self._name
    # address property getter method
    @property
    def address(self):
        return self._address
    # email property getter method
    @property
    def email(self):
        return self._email
    # login property getter method
    @property
    def login(self):
        return self._login
    # name property setter method
    @name.setter
    def name(self, name):
        self._name = name
    # address property setter method
    @address.setter
    def address(self, address):
        self._address = address
    # email property setter method
    @email.setter
    def email(self, email):
        self._email = email
    # login property setter method
    @login.setter
    def login(self, login):
        self._login = login
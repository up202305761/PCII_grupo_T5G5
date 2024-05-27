from flask import Flask, render_template, request, session,flash, redirect, url_for
from datafile import filename

import os

from classes.customer import Customer
from classes.product import Product
from classes.customerorder import CustomerOrder
from classes.orderproduct import OrderProduct
from classes.userlogin import Userlogin

app = Flask(__name__)

Customer.read(filename + 'armazem.db')
Product.read(filename + 'armazem.db')
CustomerOrder.read(filename + 'armazem.db')
OrderProduct.read(filename + 'armazem.db')
Userlogin.read(filename + 'armazem.db')
prev_option = ""
submenu = ""
app.secret_key = 'BAD_SECRET_KEY'

upload_folder = os.path.join('static', 'ProductFotos')
app.config['UPLOAD'] = upload_folder


import subs_login as lsub
import subs_gform as gfsub
import subs_gformT as gfTsub
import subs_hform as gfhsub
import subs_subform as gfsubsub
import subs_productFoto as productFotosub



@app.route("/")         
def index():
    return render_template("index.html", ulogin=session.get("user"))
    
@app.route("/login")
def login():
    return lsub.login()

@app.route("/logoff")
def logoff():
    return lsub.logoff()

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    return lsub.chklogin()

@app.route("/submenu", methods=["post","get"])
def getsubm():
    global submenu
    submenu = request.args.get("subm")
    return render_template("index.html", ulogin=session.get("user"),submenu=submenu)

@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname=''):
    submenu = request.args.get("subm")
    return gfsub.gform(cname,submenu)



@app.route("/gformT/<cname>", methods=["post","get"])
def gformT(cname=''):
    submenu = request.args.get("subm")
    return gfTsub.gformT(cname,submenu)

@app.route("/hform/<cname>", methods=["post","get"])
def hform(cname=''):
    submenu = request.args.get("subm")
    return gfhsub.hform(cname,submenu)


@app.route("/calcula_lucro", methods=["post","get"])
def calcula_lucro():
           
#     # if request.form["produto"] != None: 
        # code = str(request.form["produto"]) 
           
        # price = Product.obj[code].price
        # price_order = OrderProduct.obj[code].price
        # quantidade = OrderProduct.obj[code].quantity
        # lucro = (price_order - price) * quantidade
           
        # return render_template("calcula_lucro.html", ulogin=session.get("user"),submenu=submenu,produtos=Product.obj, price=price, price_order=price_order, quantidade=quantidade, lucro=lucro)
    
    
    # # cname = 'Product'
    # else:
        return render_template("calcula_lucro.html", ulogin=session.get("user"),submenu=submenu,produtos=Product.obj, price="")

# @app.route("/lucro", methods=["post","get"])
# def calcula_lucro():
           
#     if request.form["produto"] != None: 
#         code = request.form["produto"] 
           
#         price = Product.obj[code].price
#         price_order = OrderProduct.obj[code].price
#         quantidade = OrderProduct.obj[code].quantity
#         lucro = (price_order - price) * quantidade
           
#         return render_template("lucro.html", ulogin=session.get("user"),submenu=submenu,produtos=Product.obj, price=price, price_order=price_order, quantidade=quantidade, lucro=lucro)
    
    
#     # # cname = 'Product'
#     else:
#         return render_template("lucro.html", ulogin=session.get("user"),submenu=submenu,produtos=Product.obj, price="")

# @app.route("/lucro", methods=["POST"])
# def calcula_lucro():
#     code = request.form.get("produto")
#     if code and code in Product.obj and code in OrderProduct.obj:
#         product = Product.obj[code]
#         order_product = OrderProduct.obj[code]

#         price = product.price
#         price_order = order_product.price
#         quantidade = order_product.quantity
#         lucro = (price_order - price) * quantidade

#         return jsonify({"lucro": lucro, "price": price, "price_order": price_order, "quantidade": quantidade})
#     else:
#         return jsonify({"error": "Produto não encontrado ou informações incompletas."}), 400






# @app.route("/lucro", methods=["POST","GET"])
# def calcula_lucro():
#     code = request.form.get("produto")
#     if code and code in Product.obj and code in OrderProduct.obj:
#         product = Product.obj[code]
#         order_product = OrderProduct.obj[code]

#         price = product.price
#         price_order = order_product.price
#         quantidade = order_product.quantity
#         lucro = (price_order - price) * quantidade

#         return {"lucro": lucro, "price": price, "price_order": price_order, "quantidade": quantidade}
#     else:
#         return {"error": "Produto não encontrado ou informações incompletas."}, 400

# @app.route("/lucro", methods=["POST", "GET"])
# def calcula_lucro():
#     if request.method == "POST":
#         code = request.form.get("produto")
#         if code and code in Product.obj and code in OrderProduct.obj:
#             product = Product.obj[code]
#             order_product = OrderProduct.obj[code]

#             price = product.price
#             price_order = order_product.price
#             quantidade = order_product.quantity
#             lucro = (price_order - price) * quantidade

#             return render_template(
#                 "lucro.html",
#                 ulogin=session.get("user"),
#                 submenu=submenu,
#                 produtos=Product.obj,
#                 price=price,
#                 price_order=price_order,
#                 quantidade=quantidade,
#                 lucro=lucro
#             )
#         else:
            
#             return render_template("lucro.html", ulogin=session.get("user"),submenu=submenu,produtos=Product.obj, price="")

#     else:
#         return render_template("lucro.html", ulogin=session.get("user"),submenu=submenu,produtos=Product.obj, price=price)

        
@app.route("/subform/<cname>", methods=["post","get"]) 
def subform(cname=""):
    submenu = request.args.get("subm")
    return gfsubsub.subform(cname,submenu)


@app.route("/productform", methods=["post","get"])
def productFoto():
    submenu = request.args.get("subm")
    cname = 'Product'
    return productFotosub.productFoto(app,cname,submenu)

# @app.route("/order/mapa", methods=["post","get"])
# def ordermapa():
#     submenu = request.args.get("subm")
#     cname = ''
#     return mapasub.mapaOrderform(app,cname,submenu)

@app.route("/uc", methods=["post","get"])
def uc():
    return render_template("uc.html", ulogin=session.get("user"),submenu=submenu)



    
if __name__ == '__main__':
    app.run(debug=True,port=6001)
    #app.run()
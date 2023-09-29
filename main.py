# Flask
from flask import Flask, jsonify, request
from functions import make_quotation_pdf
import pandas as pd
import uuid
port = 8080
#
#host = "0.0.0.0"



app = Flask(__name__)


@app.route('/delete-product-params', methods=['POST'])
def delete_product_parameters():
    json_response = {
        "sessionInfo": {
            "parameters": {
                "productName": None,
                "productQuantity": None,
                "isAvailable": None,
                "productPrice": None,
                "productTotalCost": None
            }
        }
    }
    return json_response

@app.route('/get-final-quotation', methods=['POST'])
def get_final_quotation():
    id_quotation = request.json['sessionInfo']['parameters']['idQuotation']
    data_base_items = pd.read_csv('data_base_quotation_items.csv')
    quotation_items = data_base_items[data_base_items['item_id_quote'] == id_quotation]
    make_quotation_pdf(quotation_items)
    json_response = {
        "sessionInfo": {
            "parameters": {
                "productName": None,
                "productQuantity": None,
                "isAvailable": None,
                "productPrice": None,
                "productTotalCost": None,
                "idQuotation": None
            }
        }
    }
    return json_response


@app.route('/find-product-by-name', methods=['POST'])
def find_product_by_name():
    data_base = pd.read_csv('data_base.csv', index_col=False)
    productToFind = request.json['sessionInfo']['parameters']['productname']
    products = data_base['Producto'].tolist()
    if productToFind in products:
        product_df = data_base[data_base['Producto'] == productToFind]
        price = product_df['Precio'].tolist()
        json_response = {
            "sessionInfo": {
                "parameters": {
                    "isAvailable": True,
                    "productPrice": round(price[0],2)
                }
            }
        }
        return json_response
    else:
        json_response = {
            "sessionInfo": {
                "parameters": {
                    "isAvailable": False
                }
            }
        }
        return json_response


@app.route('/get-product-total-cost', methods=['POST'])
def get_product_total_cost():
    id_quotation = request.json['sessionInfo']['parameters']['idQuotation']
    product_quantity = request.json['sessionInfo']['parameters']['productquantity']
    product_name = request.json['sessionInfo']['parameters']['productname']
    unit_cost = request.json['sessionInfo']['parameters']['productPrice']
    product_total_cost = round(product_quantity * unit_cost,2)
    json_response = {
        "sessionInfo": {
            "parameters": {
                "productTotalCost": product_total_cost
            }
        }
    }
    with open("data_base_quotation_items.csv","a",encoding="utf-8") as file:
        file.write(id_quotation + "," + product_name + "," + str(int(product_quantity)) + "," + str(unit_cost) + "," + "{:.2f}".format(product_total_cost) + "\n")

    return json_response

@app.route('/generate-id-for-quotation', methods=['POST'])
def generate_id_for_quotation():
    my_uuid = uuid.uuid4()
    json_response = {
        "sessionInfo": {
            "parameters": {
                "idQuotation": my_uuid
            }
        }
    }
    return json_response

if __name__ == '__main__':
    print(f"Initialized in :{port}")
    app.run(debug=True)

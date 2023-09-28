# Flask
from flask import Flask, jsonify, request
import functions_framework
import pandas as pd
import uuid
port = 8080
#
#host = "0.0.0.0"

data_base = pd.read_csv('data_base.csv', index_col=False)

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
    productToFind = request.json['sessionInfo']['parameters']['productname']
    products = data_base['Producto'].tolist()
    if productToFind in products:
        product_df = data_base[data_base['Producto'] == productToFind]
        price = product_df['Precio'].tolist()
        json_response = {
            "sessionInfo": {
                "parameters": {
                    "isAvailable": True,
                    "productPrice": price[0]
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
    product_quantity = request.json['sessionInfo']['parameters']['productquantity']
    total_cost = request.json['sessionInfo']['parameters']['productPrice']
    json_response = {
        "sessionInfo": {
            "parameters": {
                "productTotalCost": product_quantity * total_cost
            }
        }
    }
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

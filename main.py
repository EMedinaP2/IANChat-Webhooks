# Flask
from flask import Flask, request
from webhooks import Webhooks_functions


port = 8080
host = "0.0.0.0"


app = Flask(__name__)

webhook_functions = Webhooks_functions()
@app.route('/delete-product-params', methods=['POST'])
def delete_product_parameters():
    return webhook_functions.delete_product_parameters()

@app.route('/get-final-quotation', methods=['POST'])
def get_final_quotation():
    id_quotation = request.json['sessionInfo']['parameters']['idQuotation']
    return webhook_functions.get_final_quotation(id_quotation)


@app.route('/find-product-by-name', methods=['POST'])
def find_product_by_name():
    productToFind = request.json['sessionInfo']['parameters']['productname']
    return webhook_functions.find_product_by_name(productToFind)


@app.route('/get-product-total-cost', methods=['POST'])
def get_product_total_cost():
    id_quotation = request.json['sessionInfo']['parameters']['idQuotation']
    product_quantity = request.json['sessionInfo']['parameters']['productquantity']
    product_name = request.json['sessionInfo']['parameters']['productname']
    unit_cost = request.json['sessionInfo']['parameters']['productPrice']
    return webhook_functions.get_product_total_cost(id_quotation,product_quantity,unit_cost,product_name)

@app.route('/generate-id-for-quotation', methods=['POST'])
def generate_id_for_quotation():
    return webhook_functions.generate_id_for_quotation()

if __name__ == '__main__':
    print(f"Initialized in :{port}")
    app.run(debug=True)

# Flask
from flask import Flask, request, jsonify
from webhooks import Webhooks_functions
from waitress import serve

port = 8080
host = "0.0.0.0"


app = Flask(__name__)

webhook_functions = Webhooks_functions()
@app.route('/delete-product-params', methods=['POST'])
def delete_product_parameters():
    return jsonify(webhook_functions.delete_product_parameters())

@app.route('/get-final-quotation', methods=['POST'])
def get_final_quotation():
    id_quotation = request.json['sessionInfo']['parameters']['id_quotation']
    return jsonify(webhook_functions.get_final_quotation(id_quotation))


@app.route('/find-product-by-name', methods=['POST'])
def find_product_by_name():
    productToFind = request.json['sessionInfo']['parameters']['product_name']
    return jsonify(webhook_functions.find_product_by_name(productToFind))


@app.route('/get-product-total-cost', methods=['POST'])
def get_product_total_cost():
    id_quotation = request.json['sessionInfo']['parameters']['id_quotation']
    product_quantity = request.json['sessionInfo']['parameters']['product_quantity']
    product_name = request.json['sessionInfo']['parameters']['product_name']
    unit_cost = request.json['sessionInfo']['parameters']['product_price']
    return jsonify(webhook_functions.get_product_total_cost(id_quotation,product_quantity,unit_cost,product_name))

@app.route('/generate-id-for-quotation', methods=['POST'])
def generate_id_for_quotation():
    return jsonify(webhook_functions.generate_id_for_quotation())

@app.route('/update-product-entities', methods=['POST'])
def update_prodcut_entites():
    return webhook_functions.update_product_entities()

@app.route('/get-recommendations', methods=['POST'])
def get_recommendations():
    product_name = request.json['sessionInfo']['parameters']['product_name']
    return jsonify(webhook_functions.get_recommendations(product_name))

if __name__ == '__main__':
    print(f"Initialized in {host}:{port}")
    app.run(debug=True)
    #serve(app, host=host, port=port)

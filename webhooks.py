from pdf_manager import Pdf_manager
from entities_manager import sample_update_entity_type
import pandas as pd
import uuid
import difflib


class Webhooks_functions:

    def __init__(self) -> None:
        self.pdf_man = Pdf_manager()

    def delete_product_parameters(self):
        json_response = {
        "sessionInfo": {
            "parameters": {
                "product_name": None,
                "product_quantity": None,
                "is_available": None,
                "product_price": None,
                "product_total_cost": None
                }
            }
         }
        return json_response

    def get_final_quotation(self, id_quotation):
        data_base_items = pd.read_csv('data_base_quotation_items.csv')
        quotation_items = data_base_items[data_base_items['item_id_quote']
            == id_quotation]
        link = self.pdf_man.make_quotation_pdf(quotation_items)
        json_response = {
            "sessionInfo": {
                "parameters": {
                    "report_link": link,
                    "product_name": None,
                    "product_quantity": None,
                    "is_available": None,
                    "product_price": None,
                    "product_total_cost": None,
                    "id_quotation": None
                }
            }
        }
        return json_response

    def find_product_by_name(self, productToFind):
        data_base = pd.read_csv('data_base.csv', index_col=False)
        products = data_base['Producto'].tolist()
        if productToFind in products:
            product_df = data_base[data_base['Producto'] == productToFind]
            price = product_df['Precio'].tolist()
            json_response = {
                "sessionInfo": {
                    "parameters": {
                        "is_available": True,
                        "product_price": round(price[0], 2)
                    }
                }
            }
            return json_response
        else:
            json_response = {
                "sessionInfo": {
                    "parameters": {
                        "is_available": False
                    }
                }
            }
            return json_response

    def get_product_total_cost(self, id_quotation, product_quantity, unit_cost, product_name):
        product_total_cost = round(product_quantity * unit_cost, 2)
        json_response = {
            "sessionInfo": {
                "parameters": {
                    "product_total_cost": product_total_cost
                }
            }
        }
        with open("data_base_quotation_items.csv", "a", encoding="utf-8") as file:
            file.write(id_quotation + "," + product_name + "," + str(int(product_quantity)) +
                       "," + str(unit_cost) + "," + "{:.2f}".format(product_total_cost) + "\n")
        return json_response

    def generate_id_for_quotation(self):
        my_uuid = uuid.uuid4()
        json_response = {
            "sessionInfo": {
                "parameters": {
                    "id_quotation": my_uuid
                }
            }
        }
        return json_response
    
    def update_product_entities(self):
        products = pd.read_csv('data_base.csv')
        products = products['Producto'].to_list()    
        products_entities = [{"value": i,  "synonyms": [i] } for i in products]
        sample_update_entity_type("4364c715-73ad-469f-bad1-25a7f3828c08",products_entities)
        return "Product entities updated",200
    
    def get_recommendations(self, target_product):
        data_base = pd.read_csv('data_base.csv')
        sim_results = []
        for product in data_base['Producto']:
            sim = get_sim(product, target_product)
            if sim > 0.5:
                sim_results.append(product)
        print(sim_results)
        json_response = {
            "sessionInfo": {
                "parameters":{
                    "similar_results": sim_results
                    }
            }
        }
        return json_response

def get_sim(input_name,target_name):
    return difflib.SequenceMatcher(None, input_name.lower(), target_name.lower()).ratio()
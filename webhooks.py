from pdf_manager import Pdf_manager
import pandas as pd
import uuid

class Webhooks_functions:

    def __init__(self) -> None:
        self.pdf_man = Pdf_manager()

    def delete_product_parameters(self):
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

    def get_final_quotation(self, id_quotation):
        data_base_items = pd.read_csv('data_base_quotation_items.csv')
        quotation_items = data_base_items[data_base_items['item_id_quote'] == id_quotation]
        link= self.pdf_man.make_quotation_pdf(quotation_items)
        json_response = {
            "sessionInfo": {
                "parameters": {
                    "productName": None,
                    "productQuantity": None,
                    "isAvailable": None,
                    "productPrice": None,
                    "productTotalCost": None,
                    "idQuotation": None,
                    "reportLink": link
                }
            }
        }
        return json_response
    
    def find_product_by_name(self,productToFind):
        data_base = pd.read_csv('data_base.csv', index_col=False)
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

    def get_product_total_cost(self,id_quotation, product_quantity,unit_cost,product_name):
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
    
    def generate_id_for_quotation(self):
        my_uuid = uuid.uuid4()
        json_response = {
            "sessionInfo": {
                "parameters": {
                    "idQuotation": my_uuid
                }
            }
        }
        return json_response
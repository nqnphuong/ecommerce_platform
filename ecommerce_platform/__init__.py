from flask import Flask
import pymongo

# con_str = (f"mongodb://{setting.MONGOUSER}:{setting.MONGOPASS}"
#            f"@{setting.MONGOHOST}:{setting.MONGOPORT}/?authSource=admin")


client = pymongo.MongoClient("localhost", 27017)
db = client.ecommerce_website
print(db.list_collection_names())


def create_app():
    app = Flask(__name__)
    from ecommerce_platform.business_routes import customer
    app.register_blueprint(customer.customer)
    return app



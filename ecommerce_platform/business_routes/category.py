import uuid
from flask import Blueprint, request, jsonify
from passlib.hash import pbkdf2_sha256

from ecommerce_platform import db

category = Blueprint("category", __name__)


# create
@category.route("/category/add", methods=["POST"])
def category_register():
    try:
        categoryName = request.form.get("categoryName")
        description = request.form.get("description")
        category = {
            "_id": uuid.uuid4().hex,
            "categoryName": categoryName,
            "description": description,
        }

        db.category.insert_one(category)
        return jsonify({"success": "Done!"}), 200
    except:
        return jsonify({"error": "!!!!!!"}), 401


# hien thi mamber
@category.route("/category/show-all", methods=["GET"])
def category_show_all():
    try:
        category_list = db.category.find({})
        data = []
        for ca in category_list:
            data.append(ca)
        return jsonify({"customer": data})
    except:
        return jsonify({"error": "!!!!!!"}), 401


# update
@category.route("/category/update/<string:id>", methods=["PUT"])
def category_update(id):
    # try:
        categoryName = request.form.get("categoryName")
        description = request.form.get("description")
        myquery = {"_id": id}
        newvalues = {"$set": {
            "categoryName": categoryName,
            "description": description,
        }}
        db.category.update_one(myquery, newvalues)
        return jsonify({"success": "Done!"}), 200
    # except:
    #     return jsonify({"error": "!!!!!!"}), 401


# xoa member
@category.route("/category/delete/<string:id>", methods=["DELETE"])
def category_delete(id):
    try:
        db.category.delete_one({"_id": id})
        return jsonify({"success": "Done!"}), 200
    except:
        return jsonify({"error": "Cannot delete member"}), 401

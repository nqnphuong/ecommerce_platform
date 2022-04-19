import uuid
from flask import Blueprint, request, jsonify
from passlib.hash import pbkdf2_sha256

from ecommerce_platform import db

customer = Blueprint("customer", __name__)


# dang nhap
@customer.route("/customer/login", methods=["GET", "POST"])
def customer_login():
    if request.method == "POST":
        customerEmail = request.form.get("customerEmail")
        password = request.form.get("password")
        customer = db.member.find_one({
            "customerEmail": customerEmail,
        })
        if customer:
            if pbkdf2_sha256.verify(password, customer['password']):
                return jsonify({"success": "Done!"}), 200
            else:
                return jsonify({"error": "!!!!!!"}), 401
        else:
            return jsonify({"error": "!!!!!!"}), 401
    return jsonify({"error": "!!!!!!"}), 401


# dang ky - them member
@customer.route("/customer/add", methods=["POST"])
@customer.route("/customer/register", methods=["POST"])
def customer_register():
    try:
        customerEmail = request.form.get("customerEmail")
        customerName = request.form.get("customerName")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        contactName = request.form.get("contactName")
        address = request.form.get("address")
        city = request.form.get("city")
        postalCode = request.form.get("postalCode")
        if password == confirm_password:
            customer = {
                "_id": uuid.uuid4().hex,
                "customerEmail": customerEmail,
                "customerName": customerName,
                "password": pbkdf2_sha256.encrypt(password),
                "contactName": contactName,
                "address": address,
                "city": city,
                "postalCode": postalCode
            }
            if not db.customer.find_one({"customerEmail": f"{customerEmail}"}):
                db.customer.insert_one(customer)
                return jsonify({"success": "Done!"}), 200
            else:
                return jsonify({"error": "da ton tai email"}), 401
        else:
            return jsonify({"error": "mat khau sai"}), 401
    except:
        return jsonify({"error": "!!!!!!"}), 401


# hien thi mamber
@customer.route("/customer/show-all", methods=["GET"])
def customer_show_all():
    try:
        customer_list = db.customer.find({})
        data = []
        for cus in customer_list:
            data.append(cus)
        return jsonify({"customer": data})
    except:
        return jsonify({"error": "!!!!!!"}), 401


# update
@customer.route("/customer/update/<string:id>", methods=["PUT"])
def customer_update(id):
    # try:
        customerEmail = request.form.get("customerEmail")
        customerName = request.form.get("customerName")
        password = request.form.get("password")
        # confirm_password = request.form.get("confirm_password")
        contactName = request.form.get("contactName")
        address = request.form.get("address")
        city = request.form.get("city")
        postalCode = request.form.get("postalCode")
        myquery = {"_id": id}
        newvalues = {"$set": {
            "customerEmail": customerEmail,
            "customerName": customerName,
            "password": pbkdf2_sha256.encrypt(password),
            "contactName": contactName,
            "address": address,
            "city": city,
            "postalCode": postalCode
        }}
        db.customer.update_one(myquery, newvalues)
        return jsonify({"success": "Done!"}), 200
    # except:
    #     return jsonify({"error": "!!!!!!"}), 401


# xoa member
@customer.route("/customer/delete/<string:id>", methods=["DELETE"])
def customer_delete(id):
    try:
        db.customer.delete_one({"_id": id})
        return jsonify({"success": "Done!"}), 200
    except:
        return jsonify({"error": "Cannot delete member"}), 401

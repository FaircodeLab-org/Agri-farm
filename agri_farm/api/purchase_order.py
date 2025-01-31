import frappe,json


def sync_po(data):

    for x in data.get("purchase_orders"):
        po_check = frappe.db.sql(""" SELECT * FROM `tabPurchase Order` WHERE name=%s""", x.get("erpnext_purchase_order_id"),as_dict=1)
        if len(po_check) == 0:
            x['erpnext_supplier_id'] = x['supplier']
            generate_po(x)

def get_items(items):
    f_items = []
    for i in items:
        f_items.append({
            "item_code": i.get("erpnext_item_id"),
            "qty": i.get("qty"),
            "rate": i.get("rate"),
        })
    return f_items
@frappe.whitelist()
def add_po_items():
    data = json.loads(frappe.request.data)
    try:
        if data.get("erpnext_purchase_order_id"):
            po = frappe.get_doc("Purchase Order", data.get("erpnext_purchase_order_id"))
            po.append("items",  {
                "item_code": data.get("item_code"),
                "qty": data.get("qty"),
                "rate": data.get("item_price"),
                "uom": data.get("uom"),
            })
            po.save()
            return {"success": True, "message": "Item Added"}
    except:
        frappe.log_error("Adding Item to PO Failed", frappe.get_traceback())
        return {"success": False, "message": "Adding Item Failed"}


@frappe.whitelist()
def generate_po(po_data = None):
    try:
        if po_data:
            data = po_data
        else:
            data = json.loads(frappe.request.data)
        print(data)
        obj = {
            "doctype": "Purchase Order",
            "company": data.get("company"),
            "transaction_date": data.get("date"),
            "supplier": data.get("erpnext_supplier_id"),
            "schedule_date": data.get("schedule_date"),
            "items": get_items(data.get("items"))
        }

        farmer = frappe.get_doc(obj).insert()
        farmer.submit()
        frappe.db.commit()
        if farmer.name:
            return {"success": True, "message": "Purchase Order Creation Successful",
                    "data": {"erpnext_purchase_order_id": farmer.name}}
    except:
        frappe.log_error(frappe.get_traceback(), "Add Purchase Order Error")
        return {"success": False, "message": "Purchase Order Creation Failed"}


@frappe.whitelist()
def get_orders(company=None):
    if not company:
        data = json.loads(frappe.request.data)
        employee = frappe.db.sql(""" SELECT * FROM `tabEmployee` WHERE user_id=%s """, data.get("user_id"), as_dict=1)
        if len(employee) == 0:
            return {"message": "Fetching of Data Failed. User is not an Employee. Please contact ERPNext Administrator"}
        company = employee[0].company
    po = frappe.db.sql(""" SELECT name as erpnext_purchase_order_id, company, transaction_date as date, supplier, supplier_name, schedule_date, grand_total 
                          FROM `tabPurchase Order` WHERE docstatus=1 and company=%s""",company,as_dict=1)

    for x in po:
        x['items'] = frappe.db.sql(""" SELECT item_code, qty, rate, amount FROM `tabPurchase Order Item` WHERE parent=%s""", x.erpnext_purchase_order_id,as_dict=1)

    return {"success": True, "message": "Purchase Order Fetched",
            "data": {"purchase_orders": po}}

@frappe.whitelist()
def checkout():
    data = json.loads(frappe.request.data)
    try:
        if data.get("erpnext_purchase_order_id"):
            po = frappe.get_doc("Purchase Order", data.get("erpnext_purchase_order_id"))
            po.submit()
            return {"success": True, "message": "Purchase Order Fetched",
                "data": {"purchase_orders": po}}
    except:
        frappe.log_error("Checkout Failed", frappe.get_traceback())
        return {"success": False, "message": "Checkout Failed"}

@frappe.whitelist()
def create_cart():
    data = json.loads(frappe.request.data)
    try:
        obj = {
            "doctype": "Agri Farm Cart",
            "user_id": data.get("user_id"),
            "supplier_id": data.get("supplier_id"),
        }
        cart = frappe.get_doc(obj).insert()
        frappe.db.commit()
        return {"success": True, "message": "Cart Created",
            "data": {"erpnext_cart_id": cart.name}}
    except:
        frappe.log_error("Checkout Failed", frappe.get_traceback())
        return {"success": False, "message": "Crate Creation Failed"}
@frappe.whitelist()
def delete_cart():
    data = json.loads(frappe.request.data)
    try:
        cart = frappe.get_doc("Agri Farm Cart", data.get("erpnext_cart_id"))
        cart.delete()

        frappe.db.commit()
        return {"success": True, "message": "Cart Deleted"}
    except:
        frappe.log_error("Cart Deletion Failed", frappe.get_traceback())
        return {"success": False, "message": "Cart Deletion Failed"}
@frappe.whitelist()
def add_to_cart():
    data = json.loads(frappe.request.data)
    try:
        cart = frappe.get_doc("Agri Farm Cart", data.get("erpnext_cart_id"))
        cart.append("items", {
            "item_code": data.get("item_code"),
            "qty": data.get("qty"),
            "rate": data.get("item_price"),
            "uom": data.get("uom"),
        })
        cart.save()
        frappe.db.commit()
        return {"success": True, "message": "Item added to Cart"}
    except:
        frappe.log_error("Checkout Failed", frappe.get_traceback())
        return {"success": False, "message": "Adding Item to cart Failed"}

@frappe.whitelist()
def update_item_in_cart():
    data = json.loads(frappe.request.data)
    try:
        frappe.db.sql(""" UPDATE `tabAgri Farm Cart Items` SET qty=%s, uom=%s,rate=%s WHERE parent=%s and item_code=%s""", (data.get("qty"),data.get("uom"),data.get("item_price"),data.get("erpnext_cart_id"),data.get("item_code")))
        frappe.db.commit()
        return {"success": True, "message": "Item Updated in Cart"}
    except:
        frappe.log_error("Checkout Failed", frappe.get_traceback())
        return {"success": False, "message": "Updating Item Failed"}

@frappe.whitelist()
def remove_item_in_cart():
    data = json.loads(frappe.request.data)
    try:
        frappe.db.sql(""" DELETE FROM `tabAgri Farm Cart Items` WHERE parent=%s and item_code=%s""", (data.get("erpnext_cart_id"),data.get("item_code")))
        frappe.db.commit()
        return {"success": True, "message": "Item Removed from Cart"}
    except:
        frappe.log_error("Checkout Failed", frappe.get_traceback())
        return {"success": False, "message": "Removing Item Failed"}
@frappe.whitelist()
def get_cart():
    data = json.loads(frappe.request.data)
    try:
        cart = frappe.db.sql("""SELECT name as erpnext_cart_id, user_id 
                                FROm `tabAgri Farm Cart` 
                                WHERE user_id=%s and supplier_id=%s""",(data.get("user_id"),data.get("supplier_id")),as_dict=1)

        for i in cart:
            i["items"] = frappe.db.sql(""" SELECT item_code,qty,rate as item_price, uom FROm `tabAgri Farm Cart Items` WHERE parent=%s """, i.erpnext_cart_id,as_dict=1)
        return {"success": True, "message": "Cart fetched", "data": {"cart": cart}}
    except:
        frappe.log_error("Checkout Failed", frappe.get_traceback())
        return {"success": False, "message": "Fetching Cart Failed"}
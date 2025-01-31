import frappe


@frappe.whitelist()
def get_suppliers():

    items = frappe.db.sql("""SELECT name as erpnext_supplier_id, supplier_name FROm `tabSupplier` WHERE disabled=0 """,as_dict=1)

    return {"success": True, "message": "Fetched Suppliers", "data": {"suppliers": items}}
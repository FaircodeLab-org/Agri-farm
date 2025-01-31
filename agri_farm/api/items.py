import frappe
from erpnext.stock.stock_ledger import get_previous_sle


@frappe.whitelist()
def get_items():

    items = frappe.db.sql("""SELECT name as erpnext_item_id, item_name, item_code, stock_uom as unit_of_measurement 
                            FROm `tabItem` WHERE disabled=0 """,as_dict=1)

    for i in items:
        item_price = frappe.db.sql(""" SELECT * FROM `tabItem Price` WHERE item_code=%s and buying=1 ORDER BY valid_from DESC """, i.erpnext_item_id, as_dict=1)
        i['item_price'] = 0
        if len(item_price) > 0:
            i['item_price'] = item_price[0].price_list_rate
        i['stock'] = 0
        time = frappe.utils.now_datetime().time()
        date = frappe.utils.now_datetime().date()

        previous_sle = get_previous_sle({
            "item_code": i.erpnext_item_id,
            "warehouse": frappe.get_single('Agri Farm Settings').warehouse,
            "posting_date": date,
            "posting_time": time
        })
        # get actual stock at source warehouse
        i['stock'] = previous_sle.get("qty_after_transaction") or 0
    return {"success": True, "message": "Fetched Items", "data": {"items": items}}
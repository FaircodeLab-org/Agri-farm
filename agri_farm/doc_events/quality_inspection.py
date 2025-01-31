import frappe

@frappe.whitelist()
def status_set(jc_name,qt_status):
    frappe.db.set_value('Job Card',jc_name,'quality_inspection_status',qt_status)
    frappe.db.commit()

@frappe.whitelist()
def set_item_value(r_name):
    print(r_name)
    data=frappe.db.get_value('Job Card',r_name,'production_item')
    print(data)
    print('888888888888888888888888888888')
    if data:
        return data
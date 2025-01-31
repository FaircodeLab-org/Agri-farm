# import frappe
# def cancel(self,method):
#     d=frappe.db.sql("""update `tabTrace Net Entry` set deli_note=NULL where customer_name=%s""",(self.customer))
#     frappe.db.commit()
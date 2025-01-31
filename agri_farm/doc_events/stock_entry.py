import frappe
@frappe.whitelist()
def on_submit_se(self,method):
    print("ON SUBMIT")
    for i in self.items:
        if i.is_finished_item == 1:
            if i.batch_no:
                frappe.db.sql("""update `tabBatch` set work_order=%s where name=%s""",(self.name,i.batch_no))
                frappe.db.commit()



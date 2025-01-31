import frappe
def qly_ir_validation(self,method):
    print('KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK')
    if self.operation:
        qir = frappe.db.get_value('Operation',self.operation,'quality_inspection_required')
        print(qir)
        if qir == 1 and not self.quality_inspection:
            frappe.throw('Quality Inspection is required for {0} Job Card'.format(self.name)) 
        qlty_status = frappe.db.get_value('Quality Inspection',{"reference_name":self.name},'status')
        print(qlty_status)
        if qlty_status: 
            if qlty_status == "Accepted" or self.quality_inspection_status == "Accepted":
                self.status="Completed"
            elif qlty_status == "Rejected" or self.quality_inspection_status=="Rejected":
                self.status="Rejected"
                self.for_quantity =0
                self.total_completed_qty = 0
                frappe.db.sql("""UPDATE `tabJob Card` set status='Rejected', for_quantity = 0, total_completed_qty = 0 where name=%s""",self.name)
                frappe.db.commit()
                print('ffffffffffffffffffffffffffffffffffffffffff')
                frappe.db.sql("""UPDATE `tabWork Order Operation` SET status=%s, completed_qty = 0 where parent=%s AND operation=%s""",('Pending',self.work_order,self.operation))
                frappe.db.commit()

# @frappe.whitelist()
def refresh_set_qi(self,method):
    print("refreshed.......................................")
    data=frappe.db.sql("""SELECT name FROM `tabQuality Inspection` where item_code=%s and reference_name=%s """,(self.production_item,self.name),as_dict=1)
    if data:
        for i in data:
            self.quality_inspection=i.name

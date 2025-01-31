import frappe
@frappe.whitelist()
def include_asset_in_handover(self,method):
    print("----------------------yyyyyyyyy----------------------")
    if self.include_handover_asset==1:
        des=frappe.db.get_value('Item',self.item_code,'description')
        print(des)
        if frappe.db.exists("Asset Details",{'asset_name':self.asset_name}):
            frappe.msgprint("The item is already added in the Handover Asset Details of Employee {0} ".format(self.custodian))
        else:
            doc = frappe.get_doc('Employee', self.custodian)
            doc.append('handover_asset_details', {
                'asset_name': self.asset_name,
                'qty': 1,
                'remarks': des,
                
            })
            doc.save()
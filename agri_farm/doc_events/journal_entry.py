import frappe
def set_petty_cash_status(self,method):
    print("----------------------------------ffffffff------------------")
    if self.petty_cash_request:
        frappe.db.sql("""update `tabPetty Cash Request` set status='Paid', paid_amount=%s where name=%s""",(self.total_credit,self.petty_cash_request))
        frappe.db.commit()



def set_unpaid_petty_cash_status(self,method):
    print("----------------------------------ffffffff------------------")
    if self.petty_cash_request:
        frappe.db.sql("""update `tabPetty Cash Request` set status='Unpaid', paid_amount=%s where name=%s""",(self.total_credit,self.petty_cash_request))
        frappe.db.commit()
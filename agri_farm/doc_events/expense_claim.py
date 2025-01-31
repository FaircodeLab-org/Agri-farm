import frappe
@frappe.whitelist()
def create_journal(name,date,payable_account,total_amount,company,cost_center,other_party_name):
    print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
    data=frappe.db.sql("""select * from `tabOther Party` where name=%s """,other_party_name,as_dict=1)
    print (data) 
    if frappe.db.exists("Journal Entry Account",{'reference_name':name}):
        frappe.throw('Journal Entry is already exist') 
    else:
        je = frappe.new_doc("Journal Entry")
        je.posting_date = date
        # je.multi_currency=1
        je.company= company
        je.append(
            "accounts",
            {
            
                "account": payable_account,
                "debit_in_account_currency":total_amount,
                "cost_center":cost_center,
                
            },
        )
        for i in data:
            je.append(
                "accounts",
                {
                
                    "account":i.petty_cash_account ,
                    "credit_in_account_currency":total_amount,
                    "credit":total_amount,
                    "reference_type":"Expense Claim",
                    "reference_name":name,
                    "cost_center":cost_center,
                },
            )

        je.save()
        je.submit()
        frappe.db.sql("""update `tabExpense Claim` set status='Paid' where name=%s""",name)
        frappe.db.commit()
        return je
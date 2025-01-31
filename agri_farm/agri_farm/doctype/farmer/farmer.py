# Copyright (c) 2022, Momscode Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Farmer(Document):
   def validate(self):
     # Case 1: If the farmer is resigned, disable the user account
     if self.activity_status == "Resigned":
          if self.user:
               user = frappe.get_doc("User", self.user)
               
               if user:
                    # Disable the user account
                    user.enabled = 0
                    user.save()
                    frappe.msgprint(f"User {user.name} has been disabled as the farmer is resigned.")
     
     # Case 2: If the farmer is active, enable the user account (if previously disabled)
     elif self.activity_status == "Active":
          if self.user:
               user = frappe.get_doc("User", self.user)
               
               if user:
                    if user.enabled == 0:
                         # Enable the user account
                         user.enabled = 1
                         user.save()
                         frappe.msgprint("Farmer is now active.")

   @frappe.whitelist()
   def create_supplier(self):
      
      sg = frappe.get_doc('App Config')
      print("name-------------------------")
      print(sg)
      print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
      
      sp = frappe.db.sql("""select * from `tabFarmer` where name=%s """,(self.name), as_dict= 1)
     
     
      supplier = frappe.new_doc("Supplier")

      print(self.first_name)
      
    

      
      supplier.supplier_name = self.first_name
      supplier.custom_contact_number_ = self.phone_number
      supplier.custom_is_farmer = 1
      supplier.supplier_group = sg.supplier_group
      supplier.save()
      frappe.msgprint('Supplier created successfully.')
      

   

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_id_list(doctype, txt, searchfield, start, page_len, filters):
     print("working=====================")
     c=filters.get("country")
     print(c)
     return frappe.db.sql("""select id_card from `tabID Card List` where parent=%s """,c)
 
@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_id_lists(doctype, txt, searchfield, start, page_len, filters):
     print("working=====================")
     c=filters.get("country")
     print(c)
     return frappe.db.sql("""select id_card from `tabID Card List` where parent=%s """,c)


   
   
    
   
 
  
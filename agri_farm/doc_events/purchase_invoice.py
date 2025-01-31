import frappe
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def get_farmer(supplier):
    fm = frappe.db.sql("""select * from `tabFarmer` where first_name = %s""", (supplier), as_dict=1)

    return fm
# @frappe.whitelist()
# def create_gvr(driver,no,name):
#     print("hiiiiiiiiiiiiiii")
#     print (driver)
#     doc=frappe.new_doc("GOODS VEHICLE RECORD")
#     doc.registration_no_of_vehicle=no
#     doc.invoice_number=name
#     doc.append("period_of_work",{
#         'name_of_driver': driver

#     })
#     doc.save()
#     return doc.name

@frappe.whitelist()
def create_gvr(source_name, target_doc=None):
	doclist = get_mapped_doc(
		"Purchase Invoice",
		source_name,
		{
			"Purchase Invoice": 
			{"doctype": "GOODS VEHICLE RECORD",
	            "field_map": {
                        "name": "invoice_number",
                	},
	            },
			
			# 	"condition": lambda item: item.parent not in delivery_notes,
			# 	"postprocess": update_stop_details,
			# },
		},
		target_doc,
	)

	return doclist

     

    # try:
    #     # Save the document
    #     doc.save()
    #     return doc.name
    # except frappe.exceptions.ValidationError as e:
    #     # Handle validation errors
    #     frappe.throw(str(e))



    
   
  
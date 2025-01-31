import frappe
from frappe.model.mapper import get_mapped_doc
 
@frappe.whitelist()
def get_terms(s):
    print("terms and conditions")
    a=frappe.db.sql("""select terms from `tabTerms and Conditions` where name=%s""",s,as_dict=1)
    print(a)
    return a


@frappe.whitelist()
def make_export_packing_list(source_name, target_doc=None):
    return _make_export_packing_list(source_name,target_doc)

def _make_export_packing_list(source_name,target_doc=None):
    doclist = get_mapped_doc("Sales Invoice",source_name,{
        "Sales Invoice":{
            "doctype":"Export Packing List",
            "validation":{
                "docstatus":["=",0]
            },
            "field_map":{
                "name":"sales_invoice",
               
            }
        },
        "Sales Invoice Item":{
            "doctype":"Export Packing List Item",
            "field_map":{
                "item_code":"item_code",
                "uom":"uom",
                "qty":"quantity",
                "batch_no":"batch_no",
                "gst_hsn_code":"gst_hsn_code",
                "no_and_kind_of_pkgs":"no_and_kind_of_pkgs" ,
                
            }
        }
    },target_doc)
    return doclist



@frappe.whitelist()
def create_gvr(source_name, target_doc=None):
	doclist = get_mapped_doc(
		"Sales Invoice",
		source_name,
		{
			"Sales Invoice": 
			{"doctype": "GOODS VEHICLE RECORD",
	            "field_map": {"name": "invoice_number"},
	            },
			
			# 	"condition": lambda item: item.parent not in delivery_notes,
			# 	"postprocess": update_stop_details,
			# },
		},
		target_doc,
	)

	return doclist







# @frappe.whitelist()
# def create_gvr(name):
#     doc = get_mapped_doc("Sales Invoice", name, {
#       "Sales Invoice": {
#         "doctype": "GOODS VEHICLE RECORD",
        
#         "field_map": {
#             # doc.invoice_number:name
          
#         }
#       },
      
#     }, ignore_permissions=True)
#     mr = frappe.get_doc(doc).insert()

#     return mr.name
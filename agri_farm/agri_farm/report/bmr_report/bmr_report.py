# Copyright (c) 2022, sammish and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint
def execute(filters=None):
	columns, data = [], []
	columns=get_columns()
	conditions=get_conditions(filters)
	# c = get_fg_conditions(filters)
	lists=get_lists(filters)
	for li in lists:
		row=frappe._dict({
				'inward_date':li.inward_date,
				'pr_reference':li.pr_reference,
				'inward_qty':li.inward_qty,
				'rm_lot_no':li.rm_lot_no,
				'inward_tc_no':li.inward_tc_no,
	# 			'final_product_name':li.final_product_name,
	# 			'from_date':li.from_date,
	# 			'to_date':li.to_date,
	# 			'processing_qty':li.processing_qty,
	# 			'loss_qty':li.loss_qty,
	# 			'fg_qty':li.fg_qty,		
			})	
		data.append(row)
	return columns,data

def get_columns():
	return[
		{
			"fieldname": "inward_date",
   			"fieldtype": "Date",
   			"label": "Inward Date",	
				

		},
		{
			"fieldname": "pr_reference",
   			"fieldtype": "Link",
			"options":"Purchase Receipt",
   			"label": "Purchase Receipt Reference",	
				

		},
		{
   			"fieldname": "inward_qty",
   			"fieldtype": "Float",
   			"label": "Inward Qty",
			"width":170
			
 		},
		{
   			"fieldname": "rm_lot_no",
   			"fieldtype": "Data",
   			"label": "RM Lot No",
			"width":150
  		},
		{
   			"fieldname": "inward_tc_no",
   			"fieldtype": "Link",
			"options":"Trace Net Entry",
   			"label": "Inward tc No",
			"width":170
  		},
		{
   			"fieldname": "final_product_name",
   			"fieldtype": "Link",
   			"label": "Final Product Name",
			"options" : "Item",
			"width":120 
  		},
		{
   			"fieldname": "from_date",
   			"fieldtype": "Date",
   			"label": "From Date",
			"width":150
  		},
		{
   			"fieldname": "to_date",
   			"fieldtype": "Date",
   			"label": "To Date",
			"width":150
  		},
		{
   			"fieldname": "processing_qty",
   			"fieldtype": "Float",
   			"label": "Processing Qty",
			"width":150
  		},
		{
   			"fieldname": "loss_qty",
   			"fieldtype": "Float",
   			"label": "Loss Qty",
			"width":150
  		},
		{
   			"fieldname": "loss_per",
   			"fieldtype": "Data",
   			"label": "Loss %",
			"width":150
  		},
		{
   			"fieldname": "fg_qty",
   			"fieldtype": "Float",
   			"label": "FG Qty",
			"width":150
  		},
		
	]
def get_lists(filters):
	
	conditions=get_conditions(filters)
	# c=get_fg_conditions(filters)
	data=[]
	if filters.get("fg_lot_number"):
		batchs = filters.get("fg_lot_number")
		parent=frappe.db.sql("""SELECT p.posting_date as inward_date,p.name as pr_reference,pi.qty as inward_qty,t.lot_no as rm_lot_no,t.parent as inward_tc_no from 
		`tabPurchase Receipt` as p inner join `tabPurchase Receipt Item` as pi on p.name=pi.parent inner join `tabTrace Net Entry Item` as t 
		on p.name=t.purchase_receipt where {0}""".format(conditions),as_dict=1)
		print("parent")
		print(parent)
		for dic_p in parent:
			dic_p["indent"] = 0
			filters=conditions
			data.append(dic_p)
			if batchs:
				for i in batchs:
					fg_data = frappe.db.sql("""select item from `tabBatch` where name=%s""",i,as_dict=1)
					print("Item..........")
					print(fg_data)


	else:
		parent=frappe.db.sql("""SELECT p.posting_date as inward_date,p.name as pr_reference,pi.qty as inward_qty,t.lot_no as rm_lot_no,t.parent as inward_tc_no from 
		`tabPurchase Receipt` as p inner join `tabPurchase Receipt Item` as pi on p.name=pi.parent inner join `tabTrace Net Entry Item` as t 
		on p.name=t.purchase_receipt where {0}""".format(conditions),as_dict=1)
		print("parent")
		print(parent)
		for dic_p in parent:
			dic_p["indent"] = 0
			filters=conditions
			data.append(dic_p)
			
		
	return data

def get_conditions(filters):
	conditions=""
	if filters.get("company"):
		conditions += "p.company='{0}' ".format(filters.get("company"))
		if filters.get("warehouse"):
			conditions += "pi.warehouse='{0}' ".format(filters.get("warehouse"))
	if filters.get("item"):
		conditions += "and pi.item_code='{0}' ".format(filters.get("item"))
	if filters.get("from_date"):
		conditions += "and p.posting_date>='{0}'".format(filters.get("from_date"))
	
	return conditions

# def get_fg_conditions(filters):
# 	c=""
# 	if filters.get("fg_lot_number"):
# 		for i in filters.get("fg_lot_number"):
# 			print(type(i))
# 			print("IIIIIIIIIII")
# 			c += "name='{0}' ".format(i)
	
# 	return c



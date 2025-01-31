# Copyright (c) 2022, sammish and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint
def execute(filters=None):
	columns, data = [], []
	columns=get_columns()
	conditions=get_conditions(filters)
	lists=get_lists(filters)
	purchase_lists=get_purchase_lists(filters)
	sales_lists=get_sales_lists(filters)
	for li in lists:
		row=frappe._dict({
				'date':li.date,
				'voucher_type':li.voucher_type,
				'voucher_no':li.voucher_no,
				'item_code':li.item_code,
				'opening_qty':li.opening_qty,
				'inward_stock':li.inward_stock,
				'outward_qty':li.outward_qty,
				'closing_qty':li.closing_qty,
				'rate':li.rate,
				'amount':li.amount,
				'status':li.status,				
			})	
		data.append(row)
	for li in purchase_lists:
		row=frappe._dict({
			'date':li.date,
			'voucher_type':li.voucher_type,
			'voucher_no':li.voucher_no,
			'item_code':li.item_code,
			'opening_qty':li.opening_qty,
			'inward_qty':li.inward_qty,
			'outward_qty':li.outward_qty,
			'closing_qty':li.closing_qty,
			'rate':li.rate,
			'amount':li.amount,
			'status':li.status,

		})
		data.append(row)
	for li in sales_lists:
		row=frappe._dict({
			'date':li.date,
			'voucher_type':li.voucher_type,
			'voucher_no':li.voucher_no,
			'item_code':li.item_code,
			'opening_qty':li.opening_qty,
			'inward_qty':li.inward_qty,
			'outward_qty':li.outward_qty,
			'closing_qty':li.closing_qty,
			'rate':li.rate,
			'amount':li.amount,
			'status':li.status,

		})
		data.append(row)
	return columns,data

def get_columns():
	return[
		{
			"fieldname": "date",
   			"fieldtype": "Date",
   			"label": "Date",	
			"width":130
				

		},
		{
			"label": _("Voucher Type"), 
			"fieldname": "voucher_type", 
			"width": 120
		},
		{
			"label": _("Voucher No"),
			"fieldname": "voucher_no",
			"fieldtype": "Dynamic Link",
			"options": "voucher_type",
			"width": 180,
		},
		{
   			"fieldname": "item_code",
   			"fieldtype": "Link",
   			"label": "Item Code",
			"options":"Item",
			"width":210
			
 		},
		{
   			"fieldname": "opening_qty",
   			"fieldtype": "Float",
   			"label": "Opening Qty",
			"width":80
  		},
		{
   			"fieldname": "inward_qty",
   			"fieldtype": "Float",
   			"label": "Inward Qty",
			"width":80 
  		},
  		{
   			"fieldname": "outward_qty",
   			"fieldtype": "Float",
   			"label": "Outward Qty",
			"width":80 
  		},
		{
   			"fieldname": "closing_qty",
   			"fieldtype": "Float",
   			"label": "Closing Qty",
			"width":120 
  		},
		{
   			"fieldname": "rate",
   			"fieldtype": "Currency",
   			"label": "Rate",
			"width":120 
  		},	
		
		{
   			"fieldname": "amount",
   			"fieldtype": "Currency",
   			"label": "Amount",
			"width":100 
  		},
		{
   			"fieldname": "status",
   			"fieldtype": "Data",
   			"label": "Status",
			"width":130 
  		},
	]
def get_lists(filters):
	conditions=get_conditions(filters)
	data=[]
	if filters.get("from_date") and filters.get("to_date"):
		parent=frappe.db.sql("""SELECT
		sr.name as voucher_no,
		sr.docstatus,
		sr.posting_date as date,
		sri.item_code ,
		sri.qty as opening_qty,
		sri.valuation_rate as rate,
		sri.amount
		from `tabStock Reconciliation` as sr inner join `tabStock Reconciliation Item` as sri 
		on sr.name= sri.parent where sr.docstatus!=2 and {0}""".format(conditions),as_dict=1)
		for dic_p in parent:
			v_type = {"voucher_type":'Stock Reconciliation'}
			dic_p.update(v_type)

			if dic_p.docstatus==0:
				s = {'status':'Draft'}
				dic_p.update(s)
			if dic_p.docstatus==1:
				s = {'status':'Submitted'}
				dic_p.update(s)

			i_qty = {'inward_qty':0}
			dic_p.update(i_qty)

			o_qty = {'outward_qty':0}
			dic_p.update(o_qty)

			clo_qty = 0
			clo_qty = dic_p.opening_qty + dic_p.inward_qty - dic_p.outward_qty
			print("------------------------")
			print(dic_p.opening_qty)
			print(dic_p.inward_qty)
			print(dic_p.outward_qty)
			print(clo_qty)
			print("--------------------------")
			c_qty = {'closing_qty':clo_qty}
			print(c_qty)
			print("*********************")
			dic_p.update(c_qty)

			filters=conditions
			data.append(dic_p)
			
		return data

def get_purchase_lists(filters):
	conditions=get_conditions(filters)
	data=[]
	if filters.get("from_date") and filters.get("to_date"):
		parent=frappe.db.sql("""SELECT
		sr.name as voucher_no,
		sr.posting_date as date,
		sr.status,
		sri.item_code ,
		sri.qty as inward_qty,
		sri.rate,
		sri.amount
		from `tabPurchase Invoice` as sr inner join `tabPurchase Invoice Item` as sri 
		on sr.name= sri.parent where sr.docstatus!=2 and {0}""".format(conditions),as_dict=1)
		for dic_p in parent:
			v_type = {"voucher_type":'Purchase Invoice'}
			dic_p.update(v_type)
			
			op_qty = {'opening_qty':0}
			dic_p.update(op_qty)

			o_qty = {'outward_qty':0}
			dic_p.update(o_qty)

			clo_qty = 0
			clo_qty = dic_p.opening_qty + dic_p.inward_qty - dic_p.outward_qty
			c_qty = {'closing_qty':clo_qty}
			dic_p.update(c_qty)

			filters=conditions
			data.append(dic_p)
			
		return data
def get_sales_lists(filters):
	conditions=get_conditions(filters)
	data=[]
	if filters.get("from_date") and filters.get("to_date"):
		parent=frappe.db.sql("""SELECT
		sr.name as voucher_no,
		sr.posting_date as date,
		sr.status,
		sri.item_code,
		sri.qty as outward_qty,
		sri.rate,
		sri.amount
		from `tabSales Invoice` as sr inner join `tabSales Invoice Item` as sri 
		on sr.name= sri.parent where sr.docstatus!=2 and {0}""".format(conditions),as_dict=1)
		for dic_p in parent:
			v_type = {"voucher_type":'Sales Invoice'}
			dic_p.update(v_type)
			
			op_qty = {'opening_qty':0}
			dic_p.update(op_qty)

			i_qty = {'inward_qty':0}
			dic_p.update(i_qty)

			clo_qty = 0
			clo_qty = dic_p.opening_qty + dic_p.inward_qty - dic_p.outward_qty
			c_qty = {'closing_qty':clo_qty}
			dic_p.update(c_qty)

			filters=conditions
			data.append(dic_p)
			
		return data

def get_conditions(filters):
	conditions=""
	if filters.get("from_date") and filters.get("to_date"):
		conditions = "sr.posting_date BETWEEN '{0}' and '{1}' ".format(filters.get("from_date"),filters.get("to_date"))
		if filters.get("company"):
			conditions += "and sr.company='{0}'".format(filters.get("company"))
	if filters.get("item"):
		conditions += "and sri.item_code='{0}'".format(filters.get("item"))
	
	return conditions



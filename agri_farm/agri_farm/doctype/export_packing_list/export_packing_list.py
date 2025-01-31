# Copyright (c) 2022, Momscode Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
class ExportPackingList(Document):
	def validate(self):
		print("heyy")
		tab=self.get("items")
		total_pkg_weight=0
		g_weight=0
		for t in tab:
			total_pkg_weight+=t.quantity*t.net_weight
			g_weight+=t.quantity*t.net_weight
			if t.quantity and t.net_weight==" ":
				self.pkg_net_weight=" "
				self.gross_weight=" "
		# self.pkg_net_weight=total_pkg_weight
		# self.gross_weight=g_weight
		print(g_weight)
		


###########################################################################################################
			# self.gross_weight=table1[0].net_weight
			# if table1[0].quantity and table1[0].net_weight==" ":
			# 	self.pkg_net_weight=" "



	# @frappe.whitelist()
	# def fetch_items(self):
	# 	doc=frappe.get_doc("Sales Invoice",{"name":self.sales_invoice})
	# 	print(doc)
	# 	table=doc.items
	# 	print(table)
	# 	d=frappe.db.sql("""select name from `tabBatch` where item_name=%s""",table[0].item_name,as_dict=1)
	# 	print(d)
	# 	for j in d:
	# 		self.set("items",[])
	# 		for i in table:
	# 			self.append("items",{
	# 				"item_code":i.item_code,
	# 				"item_name":i.item_name,
	# 				"quantity":i.qty,
	# 				"description":i.description,
	# 				"batch_no":j.name
	# 			})

########################################################################################################
	 
	
	
	@frappe.whitelist()
	def fetch_items(self):
		doc=frappe.get_doc("Sales Invoice",{"name":self.sales_invoice})
		# print(doc)
		table=doc.items
		# print(table)
		self.set("items",[])
		for i in table:
			d=frappe.db.sql("""SELECT batch_no FROM `tabSales Invoice Item` WHERE parent=%s and item_name=%s""",(self.sales_invoice,i.item_name),as_dict=1)
			print(i.item_name)
			self.append("items",{
				"item_code":i.item_code,
				"item_name":i.item_name,
				"quantity":i.qty,
				"description":i.description,
				"batch_no":d[0].batch_no
			})



########################################################################
	# def validate(self):
	# 	print("heyy")
	# 	table1=self.get("items")
	# 	print(table1)
	# 	self.pkg_net_weight=table1[0].quantity*table1[0].net_weight
	# 	self.gross_weight=table1[0].net_weight
	# 	if table1[0].quantity and table1[0].net_weight==" ":
	# 		self.pkg_net_weight=" "
##########################################################################


		
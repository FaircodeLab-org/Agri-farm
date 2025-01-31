# Copyright (c) 2022, Momscode Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TraceNetEntry(Document):
	# def on_submit(self):
	# 	self.deli_note=self.delivery_note
	@frappe.whitelist()
	def get_supplier_items(self):
		print("welcome")
		self.set("trace_net_entry_item",[])
		for i in self.purchase_receipt:
			print(i.purchase_receipt)
			data = frappe.db.sql("""select * from `tabPurchase Receipt Item` where parent=%s""",i.purchase_receipt,as_dict=1)
			print("data--------------------")
			print(data)
			if data:
				for j in data:
					self.append("trace_net_entry_item",{
						"item_name":j.item_code,
						"qty":j.qty,
						"uom":j.uom,
						"batch_id":j.batch_no,
						"purchase_receipt":j.parent,
						"warehouse":j.warehouse,
						})

		# doc=frappe.get_doc("Purchase Receipt",{"supplier":self.supplier_name})
		# print(doc)
		# doc_table=doc.items
		# print(doc_table[0].rate)
		# table=self.get("trace_net_entry_item")
		# for i in doc_table:
		# 	self.set("trace_net_entry_item",[])
		# 	self.append("trace_net_entry_item",{
		# 		"item_name":doc_table[0].item_code,
		# 		"qty":doc_table[0].qty,
		# 		"uom":doc_table[0].uom,
		# 		"batch_id":doc_table[0].batch_no
		# 	})
		

	@frappe.whitelist()
	def get_customer_items(self):
		print("welcome")

		data=frappe.db.sql("""select delivery_note,customer_name from  `tabTrace Net Entry` where docstatus=%s""",1,as_dict=1)
		# print(data[0].delivery_note)
		# print(data[0].customer_name)
		
		doc1=frappe.get_doc("Delivery Note",{"customer":self.customer_name})
		print(doc1)
		doc1_table=doc1.items
		# self.deli_note=doc1.name
		table=self.get("trace_net_entry_item")
		if data:
			if self.delivery_note != data[0].delivery_note:
				for i in doc1_table:
						self.set("trace_net_entry_item",[])
						self.append("trace_net_entry_item",{
							"item_name":doc1_table[0].item_code,
							"qty":doc1_table[0].qty,
							"uom":doc1_table[0].uom,
							"batch_id":doc1_table[0].batch_no
						})
		else:
			for i in doc1_table:
					self.set("trace_net_entry_item",[])
					self.append("trace_net_entry_item",{
						"item_name":doc1_table[0].item_code,
						"qty":doc1_table[0].qty,
						"uom":doc1_table[0].uom,
						"batch_id":doc1_table[0].batch_no
					})


	



@frappe.whitelist()
def get_supplier(pur):
	# print("hiiiiiiiiii")
	a=frappe.db.sql("""select supplier from `tabPurchase Receipt` where name=%s""",pur,as_dict=1)
	# print(a)
	return a

@frappe.whitelist()
def get_customer(deli):
	# print("hiiiiiiiiii")
	a=frappe.db.sql("""select customer,name from `tabDelivery Note` where name=%s""",deli,as_dict=1)
	# print(a)
	return a


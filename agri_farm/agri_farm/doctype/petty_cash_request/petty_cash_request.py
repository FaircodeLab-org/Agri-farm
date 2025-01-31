# Copyright (c) 2023, Momscode and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class PettyCashRequest(Document):
	@frappe.whitelist()
	def set_other_party_approver_and_account(self):
		account=frappe.db.get_value("Other Party",self.other_party,"petty_cash_account")
		print(account)
		print("======================")
		self.employee_account=account
		app=frappe.db.get_value("Other Party",self.other_party,"petty_cash_approver")
		print(app)
		print("======================")
		self.petty_cash_approver=app
		company=frappe.db.get_value("Other Party",self.other_party,"company")
		self.company=company


		 
	@frappe.whitelist()
	def set_approver_and_account(self):
		account=frappe.db.get_value("Employee",self.employee,"petty_cash_account")
		print(account)
		print("======================")
		self.employee_account=account
		app=frappe.db.get_value("Employee",self.employee,"petty_cash_approver")
		print(app)
		print("======================")
		self.petty_cash_approver=app
		com=frappe.db.get_value("Employee",self.employee,"company")
		self.company=com


	@frappe.whitelist()
	def validate(self):
		e_account = frappe.db.get_value("Employee",self.employee,"petty_cash_account")
		if e_account:
			self.employee_account = e_account
		o_account = frappe.db.get_value("Other Party",self.other_party,"petty_cash_account")
		if o_account:
			self.other_party_account = o_account

		if self.type=="Employee":
			if not self.employee_account:
				frappe.throw(""" Please make sure you set Petty Cash Account in Employee Master """)
		if self.type=="Other Party":
			if not self.other_party_account:
				frappe.throw(""" Please make sure you set Petty Cash Account in Other Party""")


	@frappe.whitelist()
	def on_update_after_submit(self):
		if self.sanctioned_amount > self.request_amount:
			frappe.throw("Sanctioned Amount must not be greater than Request Amount")

	@frappe.whitelist()
	def on_submit(self):
		self.generate_journal_entry()

	@frappe.whitelist()
	def generate_journal_entry(self):
		if self.sanctioned_amount == 0:
			frappe.throw("Sanctioned Amount must not be 0")
		if not self.mode_of_payment :
			frappe.throw("Mode of Payment can not be Empty")
		doc_jv = {
			"doctype": "Journal Entry",
			"voucher_type": "Contra Entry",
			"posting_date": self.posting_date,
			"company":self.company,
			# "multi_currency":1,
			"accounts": self.jv_accounts(),
			"petty_cash_request": self.name,
			"user_remark": self.purpose,
		}

		jv = frappe.get_doc(doc_jv)
		jv.insert()
		jv.save()
		# frappe.db.sql("""update `tabPetty Cash Request` set status='Paid', paid_amount=%s where name=%s""",(self.sanctioned_amount,self.name))
		self.reload()
		return jv.name
		# frappe.db.sql("""update `tabPetty Cash Request` set status='Paid' where name=%s""",self.name,as_dict=1)
	@frappe.whitelist()
	def jv_accounts(self):
		accounts = []
		if self.type=='Employee':
			accounts.append({
				'account': self.employee_account,
				'debit_in_account_currency': self.sanctioned_amount,
				'credit_in_account_currency': 0,
				'party_type': "Employee",
				'party': self.employee,
				'cost_center': self.cost_center,
			})
		if self.type=='Other Party':
			accounts.append({
				'account': self.other_party_account,
				'debit_in_account_currency': self.sanctioned_amount,
				'credit_in_account_currency': 0,
				'cost_center': self.cost_center,
			})

		credit_acount = frappe.db.sql(""" SELECT * FROM `tabMode of Payment Account` WHERE parent=%s and company=%s""", (self.mode_of_payment,self.company),as_dict=1)

		if len(credit_acount) > 0:
			accounts.append({
				'account': credit_acount[0].default_account,
				'debit_in_account_currency': 0,
				'credit_in_account_currency': self.sanctioned_amount,
				'cost_center': self.cost_center,
			})
		else:
			frappe.throw("Please set Default Account for the company '{0}' in Mode of Payment '{1}'".format(self.company,self.mode_of_payment))
		return accounts

@frappe.whitelist()
def get_jv(name):
	jv = frappe.db.sql(""" SELECT * FROM `tabJournal Entry` WHERE petty_cash_request=%s and docstatus < 2""",name, as_dict=1)
	if len(jv) > 0:
		return True
	return False

@frappe.whitelist()
def get_approvers(employee):
	employee_record = frappe.db.sql(""" SELECT department FROM `tabEmployee` WHERE name=%s""", employee,as_dict=1)
	print(employee)
	print(employee_record)
	dp = []
	if employee_record[0].department:
		dp = frappe.db.sql(""" SELECT * FROm `tabDepartment Approver` WHERE parent=%s """, employee_record[0].department,as_dict=1)

	return [i.approver for i in dp]

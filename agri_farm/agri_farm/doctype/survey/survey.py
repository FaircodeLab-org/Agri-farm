# Copyright (c) 2023, Momscode Technologies and contributors
# For license information, please see license.txt 
 
import frappe
from frappe.model.document import Document

class Survey(Document):
	def validate(self):
		print("validated")
		for i in self.crop:
			d = i.yielding_count * i.estimated_yield_count_in_kg_per_plant
			i.yield_qty_in_kg =d
			i.available_qty_kg = i.yield_qty_in_kg

			if i.total_other_sale_qty_kg:
				i.available_qty_kg = i.yield_qty_in_kg - i.total_other_sale_qty_kg
			else:
				i.available_qty_kg = i.yield_qty_in_kg

		for j in self.animal_husbandry:
			d = j.yielding_count * j.estimated_yield_count
			j.total_yield_count =d
			j.available_qty_kg = j.total_yield_count

			if j.total_other_sale_qty_kg:
				j.available_qty_kg = j.total_yield_count - j.total_other_sale_qty_kg
			else:
				j.available_qty_kg = j.total_yield_count



    
	@frappe.whitelist()
	def get_performa(self):

		
		c = frappe.db.sql("""select * from `tabFarm Details Questions` order by idx """,as_dict=1)

		
		if c:
			for idx,i in enumerate(c, start=1):
				self.append("farm_details_questions", {
					'questions': i.questions,
					'idx':idx
				
				})

# /////////////////////////////////////////////////////////////////////////////////////////////

		d = frappe.db.sql("""select * from `tabLabour Questions` order by idx """,as_dict=1)

		
		if d:
			for idx,i in enumerate(d, start=1):
				self.append("labour_questions", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////			

		e = frappe.db.sql("""select * from `tabFertigation Questions` order by idx """,as_dict=1)

		
		if e:
			for idx,i in enumerate(e, start=1):
				self.append("fertigation_questions", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////

		f = frappe.db.sql("""select * from `tabMulching Questions` order by idx """,as_dict=1)

		
		if f:
			for idx,i in enumerate(f, start=1):
				self.append("mulching_questions", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////

		g = frappe.db.sql("""select * from `tabIrrigation Questions` order by idx """,as_dict=1)

		
		if g:
			for idx,i in enumerate(g, start=1):
				self.append("irrigation_questions", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////	

		k = frappe.db.sql("""select * from `tabWeed control Questions` order by idx """,as_dict=1)

		
		if k:
			for idx,i in enumerate(k, start=1):
				self.append("weed_control_questions", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////				

		j = frappe.db.sql("""select * from `tabCrop Questions` order by idx """,as_dict=1)

		
		if j:
			for idx,i in enumerate(j, start=1):
				self.append("crop_questions", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////				

		l = frappe.db.sql("""select * from `tabBiodiversity Questions` order by idx """,as_dict=1)

		
		if l:
			for idx, i in enumerate(l, start=1):
				self.append("biodiversity_questions", {
					'questions': i.questions,
					'idx': idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////
				

		# m = frappe.db.sql("""select * from `tabRisk Questions` """,as_dict=1)

		
		# if m:
		# 	for i in m:
		# 		self.append("risk_questions", {
		# 			'questions': i.questions
		# 		})



		m = frappe.db.sql("""select * from `tabRisk Questions` order by idx""", as_dict=1)

		if m:
			for idx, i in enumerate(m, start=1):
				self.append("risk_questions", {
					'questions': i.questions,
					'idx': idx
				})





# /////////////////////////////////////////////////////////////////////////////////////////////

		n = frappe.db.sql("""select * from `tabProcessing Questions` order by idx """,as_dict=1)

		
		if n:
			for idx,i in enumerate(n, start=1):
				self.append("processing_questions", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////

		o = frappe.db.sql("""select * from `tabStorage Questions` order by idx """,as_dict=1)

		
		if o:
			for idx,i in enumerate(o, start=1):
				self.append("storage_questions", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////				

		p = frappe.db.sql("""select * from `tabTraining Questions` order by idx """,as_dict=1)

		
		if p:
			for idx,i in enumerate(p, start=1):
				self.append("training_questions", {
					'questions': i.questions,
					'idx':idx
				})

# /////////////////////////////////////////////////////////////////////////////////////////////				

		q = frappe.db.sql("""select * from `tabOthers Questions` order by idx """,as_dict=1)

		
		if q:
			for idx,i in enumerate(q, start=1):
				self.append("others_questions", {
					'questions': i.questions,
					'idx':idx
				}) 

# ////////////////////////////////////////////////////////////////////////////////////////////////
				
		inspection = frappe.db.sql("""select * from `tabInspection Records` order by idx """,as_dict=1)

		
		if inspection:
			for idx,i in enumerate(inspection, start=1):
				self.append("inspection_records", {
					'questions': i.questions,
					'idx':idx
				}) 
# Copyright (c) 2022, Momscode Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Plot(Document):
	# def validate(self):
	# 	# total = 0
	# 	# if "crop_list" in self.__dict__:
	# 	# 	for i in self.crop_list:
	# 	# 		try:
	# 	# 			total += i.plot_area
	# 	# 		except:
	# 	# 			total += i['plot_area']
	# 	# 	self.total_crop_list_plot_area = total
	# 	# 	if self.total_crop_list_plot_area != self.total_plot_area:
	# 	# 		frappe.throw("Total Crop List Plot Area must be equal to Total Plot Area")
	# 	pass
	def validate(self):
		if self.farmer:
			farmer = frappe.get_doc("Farmer", self.farmer)
			self.farmer_name = farmer.first_name
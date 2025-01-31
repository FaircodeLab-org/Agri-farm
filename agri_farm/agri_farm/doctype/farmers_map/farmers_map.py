# Copyright (c) 2022, Momscode Technologies and contributors
# For license information, please see license.txt

import frappe,json
from frappe.model.document import Document
 
class FarmersMap(Document):

	@frappe.whitelist()
	def get_plots(self):
		for_clicks = []
		conditions = ""
		if self.farmer:
			conditions += " WHERE farmer='{0}'".format(self.farmer)
		plots = frappe.db.sql(""" SELECT * FROM `tabPlot` {0} """.format(conditions),as_dict=1)

		locations = []

		for i in plots:
			i['crops'] = frappe.db.sql(""" SELECT crop, plot_name, plot_area, number_of_plants, start_date 
 					FROM `tabPlot Crops` WHERE parent=%s""", i.name,as_dict=1)
			for_clicks.append(i)
			if i.longitude and i.latitude:
				locations.append({
					"type":"Feature",
					"properties":{},
					"geometry":{
						"type":"Point",
						"coordinates":[
							i.longitude,
							i.latitude
						]
					}
				})
			if self.farmer and i.perimeter_mapping:
				locations.append({
					"type": "Feature",
					"properties": {},
					"geometry": {
						"type": "Polygon",
						"coordinates": [
							eval(i.perimeter_mapping)
						]
					}
				})

		print(locations)
		self.location = json.dumps({
			"type":"FeatureCollection",
			"features":locations
		})

		return for_clicks


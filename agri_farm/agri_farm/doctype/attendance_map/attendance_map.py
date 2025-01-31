# Copyright (c) 2022, Momscode Technologies and contributors
# For license information, please see license.txt

import frappe, json
from frappe.model.document import Document
 
class AttendanceMap(Document):
	@frappe.whitelist()
	def get_attendance(self):
		if self.employee:

			plots = frappe.db.sql(""" SELECT * FROM `tabAgri Farm Attendance` WHERE employee='{0}' and attendance_date='{1}' and docstatus=1""".format(self.employee,self.attendance_date), as_dict=1)

			locations = []
			line_strings = []

			for i in plots:

				times = frappe.db.sql(""" SELECT longitude,latitude
							FROM `tabAgri Farm Attendance Details` WHERE parent=%s ORDER BY time_type ASC,time ASC""", i.name, as_dict=1)

				for x in times:
					if x.longitude and x.latitude:
						line_strings.append([float(x.longitude),float(x.latitude)])
				locations.append({
					"type": "Feature",
					"properties": {},
					"geometry": {
						"type": "Point",
						"coordinates": [
							line_strings[0][0],
							line_strings[0][1]
						]
					}
				})
				locations.append({
					"type": "Feature",
					"properties": {},
					"geometry": {
						"type": "LineString",
						"coordinates": line_strings

					}
				})
				locations.append({
					"type": "Feature",
					"properties": {},
					"geometry": {
						"type": "Point",
						"coordinates": [
							line_strings[-1][0],
							line_strings[-1][1]
						]
					}
				})
			print("=========================")
			print(locations)
			if not line_strings:
				frappe.throw("No Attendance on the particular date")
			self.location = json.dumps({
				"type": "FeatureCollection",
				"features": locations
			})


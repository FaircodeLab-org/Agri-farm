// Copyright (c) 2023, Momscode Technologies and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Bank Stock Summary"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"fieldtype": "Date",
			"label": "From Date",
			"reqd":1,
		
		},
		{			
			"fieldname": "to_date",
			"fieldtype": "Date",
			"label": "To Date",
			"reqd":1,		
		},
		{			
			"fieldname": "company",
			"fieldtype": "Link",
			"options":"Company",
			"label": "Company",
		},
		{
			"fieldname": "item",
			"fieldtype": "Link",
			"label": "Item",
			"options":"Item"
			// "reqd":1,		
		},

	]
}


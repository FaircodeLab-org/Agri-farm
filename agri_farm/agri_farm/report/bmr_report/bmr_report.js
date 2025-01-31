// Copyright (c) 2023, Momscode Technologies and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["BMR Report"] = {
	"filters": [
		{			
			"fieldname": "company",
			"fieldtype": "Link",
			"options":"Company",
			"label": "Company",	
			"reqd":1,	
			
		},
		
		{			
			"fieldname": "item",
			"fieldtype": "Link",
			"label": "Name of Commodity",
			"options": "Item",
			"reqd":1,		
		},
		{			
			"fieldname": "from_date",
			"fieldtype": "Date",
			"label": "From Date",	
			// "reqd":1,	
			
		},
		{
			
			"fieldname": "fg_lot_number",
			"fieldtype": "MultiSelectList",
			"label": "FG Lot Number",
			"options":"Batch",
			get_data: function(txt) {
				return frappe.db.get_link_options('Batch', txt, {
					// company: frappe.query_report.get_filter_value("company")
				});
			}
			
		},
		{
			"fieldname": "warehouse",
			"fieldtype": "Link",
			"label": "Process Center",
			"options": "Warehouse",
			// "reqd":1,
			"get_query": function() {
				const company = frappe.query_report.get_filter_value('company');
				return {
					filters: { 'company': company }
				}
			}
			
		
		},

	]
};

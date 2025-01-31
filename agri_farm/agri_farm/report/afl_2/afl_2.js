// Copyright (c) 2024, Momscode Technologies and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["AFL 2"] = {
	"filters": [
		{
			"fieldname": "user",
			"fieldtype": "Link",
			"label": "User",
			"options": "User", 
			// "reqd":1,
		
		}, 
		{			 
			"fieldname": "company",
			"fieldtype": "Link",
			"label": "Company",
			"options": "Company",
			"reqd":1,		
		},
		{
			
			"fieldname": "farmer",
			"fieldtype": "Link",
			"label": "Farmer",
			"options": "Farmer",
			// "reqd":1,
		},
	
		{
			
			"fieldname": "cluster",
			"fieldtype": "Link",
			"label": "Cluster",
			"options": "Clusters",
			// "reqd":1,
		},
		{
			
			"fieldname": "village",
			"fieldtype": "Link",
			"label": "Village",
			"options": "Village",
			// "reqd":1,
		},
		{
			
			"fieldname": "survey",
			"fieldtype": "Link",
			"label": "Survey",
			"options": "Survey",
			// "reqd":1,
		},

	]
};
 
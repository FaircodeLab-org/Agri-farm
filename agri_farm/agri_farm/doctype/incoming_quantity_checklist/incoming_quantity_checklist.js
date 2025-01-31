// Copyright (c) 2023, Momscode Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Incoming Quantity Checklist', {
	// refresh: function(frm) {

	// }
});
frappe.ui.form.on('Incoming Quantity Checklist Item',{
	type:function(frm,cdt,cdn){
		var d=locals[cdt][cdn]
		console.log("************************")
		d.count = d.idx
		frm.refresh_field("incoming_quantity_checklist")
	}

})

 
// Copyright (c) 2022, Momscode Technologies and contributors
// For license information, please see license.txt


frappe.ui.form.on('Export Packing List', {
	get_items: function(frm) {
		frm.call({
			doc:cur_frm.doc,
			method:'fetch_items',
			args:{}
		})

	},
});
// frappe.ui.form.on("Export Packing List Item","quantity",function(frm,cdt,cdn){
// 	var d=local[cdt][cdn];
// 	if(d.quantity){
// 		frm.call({
// 			doc:cur_frm.doc,
// 			method:'get_weight',
// 			args:{}
// 		})
// 	}
// }) 
// Copyright (c) 2023, Momscode Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Farm Minimal', {
	refresh: function(frm) {
		// for(var i=0;i<cur_frm.doc.area_updates.length;i++){

		// }
		// var b=cur_frm.doc.area_updates.length
		// console.log("length",b)

	}
});

frappe.ui.form.on('Total Area Updates', {
	total_area_in_acres:function(frm,cdt,cdn){
		var row=locals[cdt][cdn];
		if(row.total_area_in_acres){
			for(var i=0;i<cur_frm.doc.area_updates.length;i++){

			}
			var b=cur_frm.doc.area_updates.length


			console.log("length",b)
			console.log("value",cur_frm.doc.area_updates[b-1].total_area_in_acres)
			cur_frm.set_value('total_area',cur_frm.doc.area_updates[b-1].total_area_in_acres)

		}
	}
	
});
 
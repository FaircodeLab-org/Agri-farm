// Copyright (c) 2022, Momscode Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Plot', {
	// refresh: function(frm) {

	// }
});


frappe.ui.form.on('Plot Crops', {
	plot_area: function(frm) {
        compute_plot_area(cur_frm)
	},
    crop_list_remove: function () {
        compute_plot_area(cur_frm)
    }
});

function compute_plot_area(cur_frm) {
    var total = 0
    if(cur_frm.doc.crop_list){
        for(var x=0;x<cur_frm.doc.crop_list.length;x+=1){
            total += cur_frm.doc.crop_list[x].plot_area
        }
    }
    cur_frm.doc.total_crop_list_plot_area = total
    cur_frm.refresh_field("total_crop_list_plot_area")
    if(cur_frm.doc.total_crop_list_plot_area !== cur_frm.doc.total_plot_area){
        frappe.throw("Total Crop List Plot Area must be equal to Total Plot Area")
    }
}
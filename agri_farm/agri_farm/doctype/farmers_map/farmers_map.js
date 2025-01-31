// Copyright (c) 2022, Momscode Technologies and contributors
// For license information, please see license.txt
var done_reloading = false 
frappe.ui.form.on('Farmers Map', {
	farmer: function () {
		done_reloading = true
		cur_frm.call({
			doc: cur_frm.doc,
			method: "get_plots",
			async:false,
			callback: function (r) {
					if(!done_reloading){
						cur_frm.reload_doc()
						done_reloading = true
					}
for(var x=0;x<r.message.length;x+=1){
						 (function(e) {
        					document.getElementsByClassName("leaflet-marker-icon")[e].onclick = function() {
        						console.log("tetst")
								var table_fields = [
									{
										fieldname: "crop", fieldtype: "Link",
										in_list_view: 1, label: "Crop",
										options: "Crop Parent", read_only:1
									},
									{
										fieldname: "plot_name", fieldtype: "Data",
										in_list_view: 1, label: "Plot Name", read_only:1
									},
									{
										fieldname: "number_of_plants", fieldtype: "Float",
										in_list_view: 1, label: "Number of Plants", read_only:1
									},
									{
										fieldname: "plot_area", fieldtype: "Float",
										in_list_view: 1, label: "Plot Area", read_only:1
									},
									{
										fieldname: "start_date", fieldtype: "Date",
										in_list_view: 1, label: "Start date", read_only:1
									}
								];
								let d = new frappe.ui.Dialog({
									title: r.message[e].farmer_name,
									fields: [
										{
											label: 'Total Plot Area',
											fieldname: 'total_plot_area',
											fieldtype: 'Data',
											read_only:1
										},
										{
											label: 'Crop Unit',
											fieldname: 'crop_unit',
											fieldtype: 'Data',
											read_only:1
										},
										{
											fieldname: "crops",
											fieldtype: "Table",
											label: "Crops",
											cannot_add_rows: true,
											in_place_edit: true,
											fields: table_fields
										}
									],
									primary_action_label: 'Close',
									primary_action(values) {
										d.hide();
									}
								});
								console.log(d)
								d.fields_dict.total_plot_area.set_value(r.message[e].total_plot_area);
								d.fields_dict.crop_unit.set_value(r.message[e].crop_unit);
								console.log(r.message[e].crops)
								d.fields_dict.crops.df.data = r.message[e].crops;
								d.fields_dict.crops.grid.refresh();
								d.show();
							};
    					})(x);

					}
			}
		})
    },
	onload_post_render: function(frm) {

		// document.getElementById("unique-0").style['min-height'] = "650px"
		// console.log(document.getElementById("unique-0"))
		cur_frm.call({
			doc: cur_frm.doc,
			method: "get_plots",
			async:false,
			callback: function (r) {
				console.log(r.message)
					if(!done_reloading){
						cur_frm.reload_doc()
						done_reloading = true
					}
					if(r.message.length > 0){

for(var x=0;x<r.message.length;x+=1){
						console.log("HERE")
						 (function(e) {
        					document.getElementsByClassName("leaflet-marker-icon")[e].onclick = function() {
        						console.log("tetst")
								var table_fields = [
									{
										fieldname: "crop", fieldtype: "Link",
										in_list_view: 1, label: "Crop",
										options: "Crop Parent", read_only:1
									},
									{
										fieldname: "plot_name", fieldtype: "Data",
										in_list_view: 1, label: "Plot Name", read_only:1
									},
									{
										fieldname: "number_of_plants", fieldtype: "Float",
										in_list_view: 1, label: "Number of Plants", read_only:1
									},
									{
										fieldname: "plot_area", fieldtype: "Float",
										in_list_view: 1, label: "Plot Area", read_only:1
									},
									{
										fieldname: "start_date", fieldtype: "Date",
										in_list_view: 1, label: "Start date", read_only:1
									}
								];
								let d = new frappe.ui.Dialog({
									title: r.message[e].farmer_name,
									fields: [
										{
											label: 'Total Plot Area',
											fieldname: 'total_plot_area',
											fieldtype: 'Data',
											read_only:1
										},
										{
											label: 'Crop Unit',
											fieldname: 'crop_unit',
											fieldtype: 'Data',
											read_only:1
										},
										{
											fieldname: "crops",
											fieldtype: "Table",
											label: "Crops",
											cannot_add_rows: true,
											in_place_edit: true,
											fields: table_fields
										}
									],
									primary_action_label: 'Close',
									primary_action(values) {
										d.hide();
									}
								});
								console.log(d)
								d.fields_dict.total_plot_area.set_value(r.message[e].total_plot_area);
								d.fields_dict.crop_unit.set_value(r.message[e].crop_unit);
								console.log(r.message[e].crops)
								d.fields_dict.crops.df.data = r.message[e].crops;
								d.fields_dict.crops.grid.refresh();
								d.show();
							};
    					})(x);

					}
										cur_frm.trigger("farmer")
					}

			}
		})

	}
});

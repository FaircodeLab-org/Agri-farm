// Copyright (c) 2022, Momscode Technologies and contributors
// For license information, please see license.txt




frappe.ui.form.on('Farmer', {

    refresh: function(frm) {



		if (cur_frm.doc.docstatus == 0 && cur_frm.doc.first_name){
			frm.add_custom_button(__('Create Supplier'), function() {
				console.log("kkkk")
				cur_frm.call({
					doc: cur_frm.doc,
					method: 'create_supplier',
					args: {},
					callback: function(a) {
						console.log("test supplier")
						console.log(a)
						
						
					}	
				});
			   
			});


		}
	}
});
		

cur_frm.set_query("id_card", (frm) => {
    return {
        query: "agri_farm.agri_farm.doctype.farmer.farmer.get_id_list",
        filters: {
            country: cur_frm.doc.country
        }
    };
});

cur_frm.set_query("id_card_2", (frm) => {
    return {
        query: "agri_farm.agri_farm.doctype.farmer.farmer.get_id_lists",
        filters: {
            country: cur_frm.doc.country
        }
    };
});
 
 
  
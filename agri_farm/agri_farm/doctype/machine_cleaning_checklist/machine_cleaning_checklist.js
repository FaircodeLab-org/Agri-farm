// Copyright (c) 2023, Momscode Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Machine Cleaning Checklist', {
	refresh: function(frm) {
		cur_frm.set_query("parts_of_equipment", "machine_cleaning_checklist", (frm, cdt, cdn) => {
			let d = locals[cdt][cdn];
            return {
                "filters": {
					"equipment": d.equipment
				}
			}
        })


	}
});

	


 

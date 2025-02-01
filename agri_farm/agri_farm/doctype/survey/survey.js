// Copyright (c) 2023, Momscode Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Survey', {

	refresh: function(frm) {
		cur_frm.set_query("farm_id",()=>{
			return{
				filters:{
					farmer_id:cur_frm.doc.farmer_id,
					
				}
			}
		})
	
	},
	view_map: function(frm) {
        if (!frm.doc.farm_boundary || frm.doc.farm_boundary.length === 0) {
            frappe.msgprint(__('Please add latitude and longitude values in the child table.'));
            return;
        }

        let coordinates = frm.doc.farm_boundary.map(row => [parseFloat(row.longitude), parseFloat(row.latitude)]);

        if (coordinates.length < 3) {
            frappe.msgprint(__('A polygon requires at least three coordinates.'));
            return;
        }

        coordinates.push(coordinates[0]);

        let polygon = JSON.stringify({
            type: "Feature",
            properties: { name: "Custom Polygon" },
            geometry: { type: "Polygon", coordinates: [coordinates] }
        });

        let base_url = "https://earthmap.org/?";
		let gfc_loss_year = {
				opacity: 1
			};

        let params = {
            aoi: "global",
            boundary: "Custom_Polygon",
            embed: "true",
            layers: JSON.stringify({
				"Hansen": gfc_loss_year,
			}),

            map: JSON.stringify({
                center: { lat: coordinates[0][1], lng: coordinates[0][0] },
                zoom: 18,
                mapType: "roadmap"
            }),

            polygon: polygon,
            statisticsOpen: "true",
			mainmenu: "true"
        };

        let map_url = base_url + new URLSearchParams(params).toString();
        console.log('Generated Map URL:', map_url);

        frm.set_value('map_url', map_url);
        frm.save();

        if (frm.fields_dict.map_html) {
            frm.fields_dict.map_html.$wrapper.html(`
                <iframe src="${map_url}" width="100%" height="600px" frameborder="0"></iframe>
            `);
        }

    },

	onload: function(frm) {
		
		if (!frm.doc.map_url) {
            if (frm.fields_dict.map_html) {
                frm.fields_dict.map_html.$wrapper.html('');
            }
        }

		cur_frm.get_field("farm_details_questions").grid.cannot_add_rows = true;
		refresh_field("farm_details_questions");

		cur_frm.get_field("labour_questions").grid.cannot_add_rows = true;
		refresh_field("labour_questions");

		cur_frm.get_field("fertigation_questions").grid.cannot_add_rows = true;
		refresh_field("fertigation_questions");

		cur_frm.get_field("mulching_questions").grid.cannot_add_rows = true;
		refresh_field("mulching_questions");

		cur_frm.get_field("irrigation_questions").grid.cannot_add_rows = true;
		refresh_field("irrigation_questions");

		cur_frm.get_field("weed_control_questions").grid.cannot_add_rows = true;
		refresh_field("weed_control_questions");

		cur_frm.get_field("crop_questions").grid.cannot_add_rows = true;
		refresh_field("crop_questions");

		cur_frm.get_field("biodiversity_questions").grid.cannot_add_rows = true;
		refresh_field("biodiversity_questions");

		cur_frm.get_field("risk_questions").grid.cannot_add_rows = true;
		refresh_field("risk_questions");

		cur_frm.get_field("processing_questions").grid.cannot_add_rows = true;
		refresh_field("processing_questions");

		cur_frm.get_field("storage_questions").grid.cannot_add_rows = true;
		refresh_field("storage_questions");

		cur_frm.get_field("training_questions").grid.cannot_add_rows = true;
		refresh_field("training_questions");

		cur_frm.get_field("others_questions").grid.cannot_add_rows = true;
		refresh_field("others_questions");

		cur_frm.get_field("inspection_records").grid.cannot_add_rows=true;
		refresh_field("inspection_records")


	},


	fetch_survey_questions:function(cur_frm){
		cur_frm.call({
			doc:cur_frm.doc,
			method:'get_performa',
			args:{},
			callback:function(a){
				console.log("test java ")
				console.log(a);
			}
	});
	
	}
	




}); 


	function update_available_qty(frm) {
		console.log("Updating available qty...");
		frm.doc.crop.forEach(function(row) {
			row.available_qty_kg = row.available_qty_kg - row.other_sale_qty_kg;
		});
	
		frm.refresh_field('crop');
	
		console.log("Update complete");
	}

	frappe.ui.form.on('Survey Crop Qty Table', {
		update_available_qty: function(frm,cdt,cdn) {
			var d = locals[cdt][cdn];
			if (d.other_sale_qty_kg){
				d.available_qty_kg = d.available_qty_kg - d.other_sale_qty_kg
				d.total_other_sale_qty_kg += d.other_sale_qty_kg
				d.other_sale_qty_kg = 0
				
			}
			frm.refresh_field("crop")
		}
});



	function update_available_qty(frm) {
		console.log("Updating available qty...");
		frm.doc.crop.forEach(function(row) {
			row.available_qty_kg = row.available_qty_kg - row.other_sale_qty_kg;
		});
		
		frm.refresh_field('animal_husbandry');
}

	frappe.ui.form.on('Survey Animal  Husbandry Table', {
		update_available_qty: function(frm,cdt,cdn) {
			var d = locals[cdt][cdn];
			if (d.other_sale_qty_kg){
				d.available_qty_kg = d.available_qty_kg - d.other_sale_qty_kg
				d.total_other_sale_qty_kg += d.other_sale_qty_kg
				d.other_sale_qty_kg = 0
			}
			frm.refresh_field("animal_husbandry")
		}
	});



	



	
	




	
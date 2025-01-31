// Copyright (c) 2022, Momscode Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Trace Net Entry', {

	// purchase_receipt:function(frm){
		// if(cur_frm.doc.purchase_receipt){
		// 	frappe.call({
		// 		method:"agri_farm.agri_farm.doctype.trace_net_entry.trace_net_entry.get_supplier",
		// 		args:{
		// 			pur:cur_frm.doc.purchase_receipt
		// 		},
		// 		callback:function(r){
		// 			console.log(r)
		// 			cur_frm.set_value("supplier_name",r.message[0].supplier)
		// 		}
		// 	})
		// }
		// else{
		// 	cur_frm.clear_table("trace_net_entry_item")
		// 	cur_frm.refresh_fields()
		// }
	// },

	delivery_note:function(frm){
		if(cur_frm.doc.delivery_note){
			frappe.call({
				method:"agri_farm.agri_farm.doctype.trace_net_entry.trace_net_entry.get_customer",
				args:{
					deli:cur_frm.doc.delivery_note
				},
				callback:function(r){
					console.log(r)
					cur_frm.set_value("customer_name",r.message[0].customer)
				}
			})
		
		}
	},
	get_invoice:function(frm){
		if(cur_frm.doc.entry_type=="Inward"){
			frm.call({
				doc:cur_frm.doc,
				method:'get_supplier_items',
				args:{}
			})
		}
		if(cur_frm.doc.entry_type=="Outward"){
			frm.call({
				doc:cur_frm.doc,
				method:'get_customer_items',
				args:{}
			})
		}
		// if(cur_frm.doc.entry_type=" "){
		// 	frm.clear_table("trace_net_entry_item")
		// 	frm.refresh_fields()
		// }
		
		
	},
	entry_type:function(frm){
		if(cur_frm.doc.entry_type=='Outward'){
			frm.set_value("purchase_receipt",[])
		}
		if(cur_frm.doc.entry_type=='Inward'){
			frm.set_value("delivery_note",'')
		}
	}
	
	
});

// Copyright (c) 2023, Momscode and contributors
// For license information, please see license.txt

frappe.ui.form.on('Petty Cash Request', {
	sanctioned_amount: function(frm) {
		if(cur_frm.doc.sanctioned_amount > cur_frm.doc.request_amount){
			cur_frm.doc.sanctioned_amount = cur_frm.doc.request_amount
			cur_frm.refresh_field("sanctioned_amount")
			frappe.throw("Sanctioned Amount must not be greater than Request Amount")
		}
	},
	type:function(frm){
		if (cur_frm.doc.type=="Other Party"){
			frm.set_value("employee","")
			frm.set_value("employee_name","")
			frm.set_value("petty_cash_approver","")
		}
		if (cur_frm.doc.type=="Employee"){
			frm.set_value("other_party","")
			// frm.set_value("employee_account","")
			frm.set_value("petty_cash_approver","")
		}
		// if(cur_frm.doc.employee){
		// 	frappe.db.get_value("Employee",cur_frm.doc.employee,"petty_cash_account")
		// 	.then(account =>{
		// 		cur_frm.doc.employee_account=account
		// 		cur_frm.refresh_field("employee_account")
		// 	})
	
		// } 
	},
   employee: function(frm) {
	cur_frm.call({
		doc:cur_frm.doc,
		method:'set_approver_and_account',
		args:{
			
			
		}

	})	
	
	//    if(cur_frm.doc.employee){
	// 	   frappe.call({
	// 		   method: "agri_farm.agri_farm.doctype.petty_cash_request.petty_cash_request.get_approvers",
	// 		   args:{
	// 			   employee: cur_frm.doc.employee
	// 		   },
	// 		   async: false,
	// 		   callback: function (r) {
	// 			   console.log(r.message)
	// 			   cur_frm.set_query("petty_cash_approver", () => {
	// 				   return {
	// 					   filters: {
	// 						   name: ['in', r.message]
	// 					   }
	// 				   }
	// 			   })
	// 		   }
	// 	   })
	//    }

   },
   other_party: function(frm) {
	cur_frm.call({
		doc:cur_frm.doc,
		method:'set_other_party_approver_and_account',
		args:{
			
			
		}

	})	
	},
   company:function(frm){
		frm.set_query('cost_center', function(doc) {
			return {
				filters: {
					
					"company": cur_frm.doc.company,
					"is_group":0,
				}
			};
		});

   },
   refresh: function(frm) {
	// if(cur_frm.doc.employee){
	// 	frappe.db.get_value("Employee",cur_frm.doc.employee,"petty_cash_account")
	// 	.then(account =>{
	// 		cur_frm.doc.employee_account=account
	// 		cur_frm.refresh_field("employee_account")
	// 	})

	// }
	   // document.querySelectorAll("[data-doctype='Journal Entry']")[1].style.display ="none";
	   frm.set_query('cost_center', function(doc) {
		return {
			filters: {
				
				"company": cur_frm.doc.company,
				"is_group":0,
			}
		};
		});
	   var show = false
	   frappe.call({
		   method: "agri_farm.agri_farm.doctype.petty_cash_request.petty_cash_request.get_jv",
		   args:{
			   name: cur_frm.doc.name
		   },
		   async: false,
		   callback: function (r) {
			   show = r.message
			   console.log(r.message)
		   }
	   })
	   if(cur_frm.doc.docstatus && cur_frm.doc.approval_status === 'Approved' && !cur_frm.doc.journal_entry_date && !show){
			frm.add_custom_button(__("Journal Entry"), () => {
				   cur_frm.call({
					   doc: cur_frm.doc,
					   method: 'generate_journal_entry',
					   args: {},
					   freeze: true,
					   freeze_message: "Generating Journal Entry...",
					   callback: (r) => {
						   cur_frm.reload_doc()
							   frappe.set_route("Form", "Journal Entry", r.message);
					   }
			   })
		   }, "Create")
	   }


   },
});


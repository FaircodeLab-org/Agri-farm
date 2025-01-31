// Copyright (c) 2023, Momscode Technologies and contributors
// For license information, please see license.txt
 
frappe.ui.form.on('Other Party', {
	company: function(frm) {
		cur_frm.set_query("payable_account",()=>{
			return{
				filters:{
					company:cur_frm.doc.company,
					root_type:"Liability",
					is_group:0
				}
			}
		})
		cur_frm.set_query("petty_cash_account",()=>{
			return{
				filters:{
					company:cur_frm.doc.company,
					root_type:"Asset",
					is_group:0
				}
			}
		})


	},
	petty_cash_account: function(frm) {
		cur_frm.set_query("payable_account",()=>{
			return{
				filters:{
					company:cur_frm.doc.company,
					root_type:"Liability",
					is_group:0
				}
			}
		})
		cur_frm.set_query("petty_cash_account",()=>{
			return{
				filters:{
					company:cur_frm.doc.company,
					root_type:"Asset",
					is_group:0
				}
			}
		})


	}
});

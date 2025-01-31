// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt



frappe.ui.form.on("Expense Claim", {
    refresh:function(frm){
        console.log("kkkkkkkkkkkkkk")
        if(cur_frm.doc.docstatus==1 && cur_frm.doc.type=="Other Party"){
            setTimeout(() => {
                frm.remove_custom_button('Payment', 'Create');
            }, 10);
            frm.add_custom_button('Journal Entry',()=>{
                frappe.call({
                    'method' : 'agri_farm.doc_events.expense_claim.create_journal',
                    'args' : {
                        name:cur_frm.doc.name,
                        date:cur_frm.doc.posting_date,
                        payable_account:cur_frm.doc.payable_account,
                        total_amount:cur_frm.doc.total_sanctioned_amount,
                        company:cur_frm.doc.company,
                        cost_center:cur_frm.doc.cost_center,
                        other_party_name:cur_frm.doc.other_party,

                    },
                    callback:function(r){
                        frm.refresh()
                        frappe.show_alert({
                            message: __('Journal Entry Created'),
                            indicator: 'green'
                        }, 3);
                    }
    
                })			
                
            }, 'Create')
        }

    },
    type:function(frm){
		if (cur_frm.doc.type=="Other Party"){
			frm.set_value("employee","")
			frm.set_value("employee_name","")
			
		}
		if (cur_frm.doc.type=="Employee"){
			frm.set_value("other_party","")
			
		}
		
	},
    other_party:function(frm){
        if(cur_frm.doc.other_party){
            frappe.db.get_value("Other Party",cur_frm.doc.other_party,"petty_cash_approver")
            .then(approver => {
                console.log("GGGGGGGGGGGGG")
                console.log(approver.message["petty_cash_approver"])
            frm.set_value("expense_approver",approver.message["petty_cash_approver"])
            })
            frappe.db.get_value("Other Party",cur_frm.doc.other_party,"company")
            .then(com => {
            frm.set_value("company",com.message["company"])
            })
            frappe.db.get_value("Other Party",cur_frm.doc.other_party,"payable_account")
            .then(pay_account=> {
                console.log(pay_account.message["payable_account"])
                console.log("*************************")
                setTimeout(() => {
            frm.set_value("payable_account",pay_account.message["payable_account"])
                }, 1002);
            
            })
            
   
        }
    }
    

    
})
// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt



frappe.ui.form.on("Employee", {
    refresh:function(frm){

        frm.set_query('petty_cash_account', function(doc) {
            return {
                filters: {
                    
                    "company": cur_frm.doc.company,
                    "is_group":0,
                }
            };
        });
    },
    company:function(frm){
        frm.set_query('petty_cash_account', function(doc) {
            return {
                filters: {
                    
                    "company": cur_frm.doc.company,
                    "is_group":0,
                }
            };
        });
    },
    petty_cash_account:function(frm){
        frm.set_query('petty_cash_account', function(doc) {
            return {
                filters: {
                    
                    "company": cur_frm.doc.company,
                    "is_group":0,
                }
            };
        });

    }

})
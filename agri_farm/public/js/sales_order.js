// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt


frappe.ui.form.on("Sales Order", {
    is_export_invoice:function(frm){
        if(cur_frm.doc.is_export_invoice){
            cur_frm.set_value("is_export_with_gst",1)

        }
        else{
            cur_frm.set_value("is_export_with_gst",0)
        }

    },
})
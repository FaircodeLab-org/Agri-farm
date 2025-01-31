// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt


frappe.ui.form.on("Sales Invoice", {
    statement_of_origin:function(frm){
        if(cur_frm.doc.statement_of_origin){
            frappe.call({
                method:"agri_farm.doc_events.sales_invoice.get_terms",
                args:{
                    s:cur_frm.doc.statement_of_origin
                },
                callback:function(r){
                    console.log(r)
                    cur_frm.set_value("statement",r.message[0].terms)
                }
            })
        }
        
    }, 
    is_export_invoice:function(frm){
        if(cur_frm.doc.is_export_invoice){
            cur_frm.set_value("is_export_with_gst",1)

        }
        else{
            cur_frm.set_value("is_export_with_gst",0)
        }

    },
    refresh:function(frm){


        if(!frm.is_new()){
            frm.add_custom_button(__('GVR'), function(){
                console.log(frm.doc.driver_name)
                console.log(frm.doc.vehicle_no)
                frappe.model.open_mapped_doc({
                    method:"agri_farm.doc_events.sales_invoice.create_gvr",
                    frm: cur_frm
                })
                // frappe.call({
                //     method:"agri_farm.doc_events.purchase_invoice.create_gvr",
                //     args:{

                //         driver:frm.doc.driver_name,
                //         no:frm.doc.vehicle_no,
                //         name:frm.doc.name
                //     },
                //     callback:function(r){
                //         frappe.set_route("Form", "GOODS VEHICLE RECORD",r.message)

                //     }
                   
                    
                // })
                // frappe.set_route("List", "GOODS VEHICLE RECORD")

                
                 console.log("GVR");
             }, __("Create"));
             

        }

        // if(!frm.is_new()){
        //     frm.add_custom_button(__('GVR'), function(){
        //         frappe.call({
        //             method:"agri_farm.doc_events.sales_invoice.create_gvr",
        //             args:{

        //                 name:cur_frm.doc.name
        //             },
        //             callback:function(r){
        //                 frappe.set_route("Form", "GOODS VEHICLE RECORD",r.message)

        //             }
                   
                    
        //         })
                
        //          console.log("GVR");
        //      }, __("Create"));
             

        // }
        if(cur_frm.doc.docstatus==0 && cur_frm.doc.is_export_invoice){
            cur_frm.add_custom_button(__("Export Packing List"),function(){
                frappe.model.open_mapped_doc({
                    method:"agri_farm.doc_events.sales_invoice.make_export_packing_list",
                    frm:cur_frm
                })
            },__('Create'));
            
        }
    },
  
})
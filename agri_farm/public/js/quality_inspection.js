// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.ui.form.on("Quality Inspection", {
    reference_type:function(frm){
        console.log('gggggg')
        if(cur_frm.doc.reference_type =='Job Card'){
            console.log('kkkkkk')
            cur_frm.set_query("reference_name", (frm) => {
                if(cur_frm.doc.reference_type =='Job Card'){
                    return {
                        filters:[
                            ["status", "in", ["Open", "Work In Progress"]],

                        ]
                        // filters: {
                        //     status: ["in", "Open", "Work In Progress"] , //apply filter to child table of quotation only vacant status record can be visible in holding name 
                        // }
                    }
                }
                else{
                    console.log('condition not worked')
                }
            })
        }
        else{
            console.log('job not job card')
        }
    },
    reference_name:function(frm){
        if(cur_frm.doc.reference_name){
            frappe.call({
                'method':'agri_farm.doc_events.quality_inspection.set_item_value',
                'args':{
                    r_name:cur_frm.doc.reference_name,

                },
                callback:function(r){
                    cur_frm.set_value('item_code',r.message)
                    console.log("eeeeeeeeeeeee")
                }
            })
        }
    },
    validate:function(frm){
        console.log('hiiii')
        if(cur_frm.doc.reference_type=='Job Card'){
            console.log('hellooo')
            frappe.call({
                'method' : 'agri_farm.doc_events.quality_inspection.status_set',
                'args' : {
                    jc_name:cur_frm.doc.reference_name,
                    qt_status : cur_frm.doc.status,
                },

            })
        }
    }
})
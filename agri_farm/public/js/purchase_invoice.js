frappe.ui.form.on('Purchase Invoice', {
    refresh: function(frm) {

        if(!frm.is_new()){
            frm.add_custom_button(__('GVR'), function(){
                console.log(frm.doc.driver_name)
                console.log(frm.doc.vehicle_no)
                frappe.model.open_mapped_doc({
                    method:"agri_farm.doc_events.purchase_invoice.create_gvr",
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

        


       
         



         





        cur_frm.set_query("custom_farm_id",()=>{
            return{
                filters:{
                    farmer_id:cur_frm.doc.custom_farmer_id
                }
            }
        })
        cur_frm.set_query("custom_survey",()=>{
            return{
                   filters:{
                farm_id:cur_frm.doc.custom_farm_id,
                   }
            }
        }) 
       
       
    },
    supplier: function(frm) {
        console.log('testing farmer')
        frappe.call({
            method: "agri_farm.doc_events.purchase_order.get_farmer",
            args: {
                supplier: frm.doc.supplier
            },
            callback: function(r) {
                if (r.message) {
                    frm.set_value('custom_farmer_id', r.message[0].name);
                    console.log(r)
                }
            }
        
        });
    }

    

}); 
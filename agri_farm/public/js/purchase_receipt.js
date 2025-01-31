frappe.ui.form.on('Purchase Receipt', {
    refresh: function(frm) {
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
// bind events

frappe.ui.form.on("ToDo", {
    refresh:function(frm){
        console.log("hiiiiiii")
        console.log(frm.doc.check_list_1_details)
        // cur_frm.set_df_property('status','options', 'Open\nWorking\nClosed\nCancelled');
    },
    before_save:function(frm){
        console.log('on_save')
        if(cur_frm.doc.check_list_1==0){
            frm.set_value('check_list_1_details',"")
            frm.set_value('attach_image_1',"")
        }
        if(cur_frm.doc.check_list_2==0){
            frm.set_value('check_list_2_details',"")
            frm.set_value('attach_image_2',"")
        }
        if(cur_frm.doc.check_list_3==0){
            frm.set_value('check_list_3_details',"")
            frm.set_value('attach_image_3',"")
        }
        if(cur_frm.doc.check_list_4==0){
            frm.set_value('check_list_4_details',"")
            frm.set_value('attach_image_4',"")
        }
        if(cur_frm.doc.check_list_5==0){
            frm.set_value('check_list_5_details',"")
            frm.set_value('attach_image_5',"")
        }
    }

})
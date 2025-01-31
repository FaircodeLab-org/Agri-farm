// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt


frappe.ui.form.on("Task", {
    company_name:function(frm){
        if(cur_frm.doc.company_name){
            cur_frm.set_value("company",cur_frm.doc.company_name)
            cur_frm.refresh_field("company")

        }

    },
    project:function(frm){
        if(cur_frm.doc.project){
            console.log("byeeee")
            console.log(cur_frm.doc.project_name)
            frappe.call({
                method:"agri_farm.doc_events.task.fetch_company",
                args:{
                    pro_name:cur_frm.doc.project_name
                },
                callback:function(r){
                    cur_frm.set_value("company_name",r.message[0].company)
                    console.log(r.message[0].company)
                    cur_frm.refresh_field("company_name")
                    cur_frm.set_value("company",r.message[0].company)
                    cur_frm.refresh_field("company")

                }
            })
        }

    },
	// onload:function(frm){
        
     //    // cur_frm.set_df_property("frequency","hidden",1)
     //    // cur_frm.set_df_property("start_date","hidden",1)
     //    // cur_frm.set_df_property("end_date","hidden",1)
     //    // cur_frm.set_df_property("repeat_on_day","hidden",1)
	// },
    onload_post_render(frm) {
            cur_frm.set_df_property("is_template","hidden",1)
            


        // if(!window.location.hash) {
        //     window.location = window.location + '#';
        //     window.location.reload();
        // }
        // intro(frm)
        set_status(frm)
    },
    // before_save:function(frm){
    //     if(cur_frm.doc.status=='Completed'){
    //         frappe.call({
    //             method:"agri_farm.doc_events.task.completed_validation",
    //             args:{
    //                 task_name:cur_frm.doc.name,  
    //             },
    //             callback:function(r){
    //                 console.log("function executed")
    //             }
    //         })

    //     }
    // },

    
   
    
    // repeat_task:function(frm){
    //     if(cur_frm.doc.repeat_task){
    //         frm.set_df_property("frequency","hidden",0)
    //         frm.set_df_property("start_date","hidden",0)
    //         frm.set_df_property("end_date","hidden",0)
    //         frm.set_df_property("repeat_on_day","hidden",0)
    //         frm.set_df_property("frequency","reqd",1)
    //         frm.set_df_property("start_date","reqd",1)
    //         frm.set_df_property("end_date","reqd",1)
    //         frm.set_df_property("repeat_on_day","reqd",1)
            
    //     }
    //     else{
    //         cur_frm.set_df_property("frequency","hidden",1)
    //         cur_frm.set_df_property("start_date","hidden",1)
    //         cur_frm.set_df_property("end_date","hidden",1)
    //         cur_frm.set_df_property("repeat_on_day","hidden",1)
    //         frm.set_df_property("frequency","reqd",0)
    //         frm.set_df_property("start_date","reqd",0)
    //         frm.set_df_property("end_date","reqd",0)
    //         frm.set_df_property("repeat_on_day","reqd",0)
    //     }
    // },
    after_save:function(frm){
        var rr=cur_frm.doc.repeat_task
        if(rr){
            frappe.call({
                method:"agri_farm.doc_events.task.save_task",
                args:{
                    fr:cur_frm.doc.frequency,
                    date:cur_frm.doc.start_date,
                    doc:cur_frm.doc.doctype,
                    doc_name:cur_frm.doc.name,
                    end_date:cur_frm.doc.end_date,
                    r:cur_frm.doc.repeat_on_day
                },
                async: false,
                callback:function(r){
                    console.log("function executed. AFTER SAVE. REPEAT TASK")
                }
            })
        }
       
        if(cur_frm.doc.status==='Open'){
            console.log("joooo")
            if(cur_frm.doc.responsible_person){
                var rp=frm.doc.responsible_person
                // for(var i=0;i<rp.length;i++){
                    frappe.call({
                        method:"agri_farm.doc_events.task.create_todo",
                        args:{
                            responsible_person:cur_frm.doc.responsible_person.concat(cur_frm.doc.participants),
                            task_name:cur_frm.doc.name,
                            status:cur_frm.doc.status,
                            priority:cur_frm.doc.priority,
                            description:cur_frm.doc.subject,
                            created_by: cur_frm.doc.created_by,
                            observer: cur_frm.doc.observer,
                        },
                        async: false,
                        callback:function(r){
                        set_status(frm)
                            set_status(frm)
                            cur_frm.reload_doc()
                            console.log("function executed. CREATE TODO")
                        }
                    })
            
                // }
            }
            // if(cur_frm.doc.participants){
            //     var p=frm.doc.participants
            //     // for(var i=0;i<p.length;i++){
            //     //     console.log(cur_frm.doc.participants[i].user)
            //         frappe.call({
            //             method:"agri_farm.doc_events.task.create_todo",
            //             args:{
            //                 responsible_person:cur_frm.doc.participants,
            //                 task_name:cur_frm.doc.name,
            //                 status:cur_frm.doc.status,
            //                 priority:cur_frm.doc.priority,
            //                 description:cur_frm.doc.subject,
            //
            //
            //             },
            //             async:false,
            //             callback:function(r){
            //                 // set_status(frm)
            //                 cur_frm.reload_doc()
            //                 console.log("function executed. PARTICIPANTS")
            //             }
            //         })
            //
            //     // }
            //
            // }
            
        }
        // cur_frm.reload_doc()
        // intro(frm)
        // set_status(frm)
    }

   


})
function set_status(frm){
   // if(!frm.is_new())
   //  {
   //      frm.set_intro(('{0}',
   //      [
   //          '<h3>ToDo for this Task</h3>'
   //          ]
   //      )
   //          )
   //      // return true
   //  }
    var params = {
        'task': frm.doc.name
    }
    frappe.call('agri_farm.task_api.get_todo', params).then((r) => {
        let total = r.message;
        var name = total.name;
        var status = total.status1;
        var reference_name = total.reference_name;
        var size = name.length;

        var todos = cur_frm.is_new() ? "":"<h3>ToDo for this Task</h3>"
        for(var i = 0; i< size; i++){
            todos += `<a href="/app/todo/${name[i]}">${i+1}: ${name[i]} -${reference_name[i]} </a>`
            todos += `<p>${status[i]}</p>`
        }
        frm.set_intro(('',todos), 'red');

    })
    
}
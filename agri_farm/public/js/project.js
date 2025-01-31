frappe.ui.form.on('Project', {
	refresh(frm) {
        console.log("Bhai ka app")
        intro(frm)
		set_status(frm)
	},
    company_name:function(frm){
        if(cur_frm.doc.company_name){
            cur_frm.set_value("company",cur_frm.doc.company_name)
            cur_frm.refresh_field("company")

        }

    }
})

function intro(frm)
{
    if(!frm.is_new())
    {
        frm.set_intro(('{0}',
        [
            '<h3>Tasks for this Project</h3>'
            ]
        )
            )
    }
}

function set_status(frm)
{
    let params = {
        'project': frm.doc.name
    }
    frappe.call('agri_farm.project_api.get_t', params).then((r) => {
        let total = r.message;
        let name = total.name;
        let status = total.status1;
        let subject = total.subject;
        let size = name.length;
        console.log(name)
        console.log(status)
        console.log(subject)
        console.log(size)
        for(let i = 0; i< size; i++)
        {
            if (!frm.doc.description && !frm.is_new()) {
                frm.set_intro(('',
                      [
                        `<a href="/app/task/${name[i]}">${i+1}:${subject[i]} - ${name[i]}</a>`,
                        `<p>${status[i]}</p>`,
                      ]), 'red');
            }
        }
    })
    
}
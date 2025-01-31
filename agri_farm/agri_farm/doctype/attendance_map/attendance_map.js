var done_reloading = false
frappe.ui.form.on('Attendance Map', {
	employee: function () {
		done_reloading = true
		cur_frm.call({
			doc: cur_frm.doc,
			method: "get_attendance",
			async:false,
			callback: function (r) {
					if(!done_reloading){
						cur_frm.reload_doc()
						done_reloading = true
					}

			}
		})
    },
	attendance_date: function () {
		done_reloading = true
		cur_frm.call({
			doc: cur_frm.doc,
			method: "get_attendance",
			async:false,
			callback: function (r) {
					if(!done_reloading){
						cur_frm.reload_doc()
						done_reloading = true
					}

			}
		})
    },
	onload_post_render: function () {
		cur_frm.doc.employee = ""
		cur_frm.refresh_field("employee")
		cur_frm.disable_save()
    }
});
 
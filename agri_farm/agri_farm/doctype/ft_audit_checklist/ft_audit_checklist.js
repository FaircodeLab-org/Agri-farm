// Copyright (c) 2023, Momscode Technologies and contributors
// For license information, please see license.txt
 
frappe.ui.form.on('FT audit Checklist', {
	// refresh: function(frm) {
 
	// }
	notify1:function(frm){
		console.log("aaaaaaaaaaaaaaaaaa")
		sent_email(cur_frm,cur_frm.doc.approver1)
		
	},
	notify2:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver2)
		
	},
	notify3:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver3)
		
	},
	notify4:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver4)
		
	},
	notify5:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver5)
		
	},
	notify6:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver6)
		
	},
	notify7:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver7)
		
	},
	notify8:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver8)
		
	},
	notify9:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver9)
		
	},
	notify10:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver10)
		
	},
	notify11:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver11)
		
	},
	notify12:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver12)
		
	},
	notify13:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver13)
		
	},
	notify14:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver14)
		
	},
	notify15:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver15)
		
	},
	notify16:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver16)
		
	},
	notify17:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver17)
		
	},
	
	notify18:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver18)
		
	},
	notify19:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver19)
		
	},
	notify20:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver20)
		
	},
	notify21:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver21)
		
	},
	notify22:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver22)
		
	},
	notify23:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver23)
		
	},
	notify24:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver24)
		
	},
	notify25:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver25)
		
	},
	notify26:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver26)
		
	},
	notify27:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver27)
		
	},
	notify28:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver28)
		
	},
	notify29:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver29)
		
	},
	notify30:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver30)
		
	},
	notify31:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver31)
		
	},
	notify32:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver32)
		
	},
	notify33:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver33)
		
	},
	notify34:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver34)
		
	},
	notify35:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver35)
		
	},
	notify36:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver36)
		
	},
	notify37:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver37)
		
	},
	notify38:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver38)
		
	},
	notify39:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver39)
		
	},
	notify40:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver40)
		
	},
	notify41:function(frm){
		sent_email(cur_frm,cur_frm.doc.approver41)
		
	},
	

	
});

function sent_email(cur_frm,approver){
	console.log("xxxxxxxxxxxxxxxxx")
	
	if(approver){
		console.log(approver)
		cur_frm.call({
			doc: cur_frm.doc,
			method: 'send_email_on_notify',
			args: {
				approver_email:approver,
			},
			callback: (r) => {
	 
			
					
			}
		})
	}

}

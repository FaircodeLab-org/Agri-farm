# # Copyright (c) 2023, Momscode Technologies and contributors
# # For license information, please see license.txt

# import frappe
# from frappe.model.document import Document

# class FTauditChecklist(Document):
		
# 	@frappe.whitelist()
# 	def send_email_on_notify(self):
# 		# Get the document
		

# 		# Get the email address of the 'aprover' (User)
# 		approver_email = self.approver1
# 		name=frappe.db.get_value("User",self.email_id,"full_name")
		
		

# 		# Compose the email message
# 		subject = "Notification: Action Required"
# 		message = f"Dear {self.name},\n\n" \
# 				f"You are notified regarding document .\n" \
# 				f"Please take the necessary action."

# 		# Send the email
# 		frappe.sendmail(
# 			recipients=approver_email,
# 			subject=subject,
# 			message=message
# 		)

# 		# Optionally, you can log the email in the Communication section of the document
# 		self.add_comment('Comment', _(f"Notification email sent to {approver_email}"))

# 		# Return a response (if needed)
# 		return "Email sent successfully"




 

# # custom_script.py





import frappe
from frappe.model.document import Document

class FTauditChecklist(Document):
		
    @frappe.whitelist()
    def send_email_on_notify(self,approver_email):
        print("sssssssssss")
        # Get the email address of the 'approver' (User)
        
        name = frappe.db.get_value("User", approver_email, "full_name")
        # name = self.approver1

        # Compose the email message
        subject = "Notification: Action Required"
        message = f"Dear {name},\n\n" \
                  f"You are notified regarding document {self.name}.\n" \
                  f"Please take the necessary action."

        # Send the email
        frappe.sendmail(
            recipients=approver_email,
            subject=subject,
            message=message
        )
        frappe.msgprint("email sent successfully")
       
  
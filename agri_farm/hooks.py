from . import __version__ as app_version

app_name = "agri_farm"
app_title = "Agri Farm"
app_publisher = "Momscode Technologies"
app_description = "Agri Farm"
app_email = "info@momscode.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/agri_farm/css/agri_farm.css"
# app_include_js = "/assets/agri_farm/js/agri_farm.js"

# include js, css files in header of web template
# web_include_css = "/assets/agri_farm/css/agri_farm.css"
# web_include_js = "/assets/agri_farm/js/agri_farm.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "agri_farm/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {
#     "leaderboard" : "public/js/leaderboard.js"
# }

# include js in doctype views
doctype_js = {"Task" : "public/js/task.js",
              "Sales Invoice":"public/js/sales_invoice.js",
              "Quality Inspection" : "public/js/quality_inspection.js",
              "Project" : "public/js/project.js",
              "ToDo" : "public/js/todo.js",
              "Employee": "public/js/employee.js",
              "Expense Claim":"public/js/expense_claim.js",
               "Sales Order":"public/js/sales_order.js",
               "Purchase Order":"public/js/purchase_order.js",
               "Purchase Receipt":"public/js/purchase_receipt.js",
               "Purchase Invoice":"public/js/purchase_invoice.js"
}
doctype_list_js = {
    "Job Card" : "public/js/job_card_list.js",
    
}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "agri_farm.utils.jinja_methods",
#	"filters": "agri_farm.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "agri_farm.install.before_install"
# after_install = "agri_farm.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "agri_farm.uninstall.before_uninstall"
# after_uninstall = "agri_farm.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "agri_farm.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Job Card":{
        "on_submit":"agri_farm.doc_events.job_card.qly_ir_validation",
        "onload":"agri_farm.doc_events.job_card.refresh_set_qi",
    },
    "Asset":{
        "validate":"agri_farm.doc_events.asset.include_asset_in_handover"
    },
    "Journal Entry":{
        "on_submit":"agri_farm.doc_events.journal_entry.set_petty_cash_status",
        "on_cancel":"agri_farm.doc_events.journal_entry.set_unpaid_petty_cash_status"
    },
    "Stock Entry":{
        "on_submit":"agri_farm.doc_events.stock_entry.on_submit_se",
    },
    "Purchase Receipt":{
        "on_submit":"agri_farm.doc_events.purchase_receipt.update_qty",
        "on_cancel":"agri_farm.doc_events.purchase_receipt.cancel_update_qty"
    },
    "Purchase Order":{
        "on_submit":"agri_farm.doc_events.purchase_order.validate_qty"
    }
   
    
    # "Delivery Note":{
	# 	"on_cancel":"agri_farm.doc_events.delivery_note.cancel"
	# }

#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"agri_farm.tasks.all"
#	],
#	"daily": [
#		"agri_farm.tasks.daily"
#	],
#	"hourly": [
#		"agri_farm.tasks.hourly"
#	],
#	"weekly": [
#		"agri_farm.tasks.weekly"
#	],
#	"monthly": [
#		"agri_farm.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "agri_farm.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "agri_farm.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
override_doctype_dashboards = {
	"Sales Invoice":"agri_farm.doc_events.override_sales_invoice_dashboard.get_data"
}

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"agri_farm.auth.validate"
# ]
fixtures =[{
	"dt":"Custom Field",
	"filters":[
		["name","in",[
			"Task-task_members",
            "Task-responsible_person",
            "Task-created_by",
            "Task-participants",
            "Task-column_break_25",
            "Task-observer",
            "Task-quantity",
            "Task-repeat_task",
            "Task-frequency",
            "Task-start_date",
            "Task-section_break_16",
            "Task-end_date",
            "Task-column_break_19",
            "Task-repeat_on_day",
            "Task-auto_repeat",
            "Task-company_name",
            "Project-company_name",

            "Sales Invoice-export",
            "Sales Invoice-state",
            "Sales Invoice-vehicle_no",
            "Sales Invoice-date_of_supply",
            "Sales Invoice-place_of_supply",
            "Sales Invoice-consignee",
            "Sales Invoice-notify",
            "Sales Invoice-notify2",
            "Sales Invoice-pre_carriage_by",
            "Sales Invoice-place_of_receipt_by_pre_carrier",
            "Sales Invoice-final_destination",
            "Sales Invoice-country_of_origin_of_goods",
            "Sales Invoice-flight_no",
            "Sales Invoice-port_of_loading",
            "Sales Invoice-port_of_discharge",
            "Sales Invoice-country_of_final_destination",
            "Sales Invoice-mode_of_transport",
            "Sales Invoice-column_break_250",
            "Sales Invoice-vehicle_number",
            "Sales Invoice-mode_of_transportation",
            "Sales Invoice-other_information",
            "Sales Invoice-column_break_244",
            "Sales Invoice-receiver_details",
            "Sales Invoice-column_break_237",
            "Sales Invoice-export_details",
            "Sales Invoice-distance",
            "Sales Invoice-driver_name",
            "Sales Invoice-lr_date",
            "Sales Invoice-transporter",
            "Sales Invoice-gst_transporter_id",
            "Sales Invoice-driver",
            "Sales Invoice-lr_no",
            "Sales Invoice-transporter_info",
            "Sales Invoice-transporter_col_break",
            "Sales Invoice-gst_vehicle_type",
            "Sales Invoice-transporter_name",
            "Sales Invoice-vessel_no",
            "Sales Invoice-container_no",
            "Sales Invoice-seal_no",
            "Sales Invoice-ico_lot_no",
            "Sales Invoice-coffee_board_permit_no",
            "Sales Invoice-harvest_year",
            "Sales Invoice-certification_details",
            "Sales Invoice-statement_of_origin",
            "Sales Invoice-statement",
            "Sales Invoice-is_online_invoice",
            "Sales Invoice-online_invoice_reference",
            "Sales Invoice-online_platform",
            "Sales Invoice-is_export_invoice",
            "Company-export",
            "Company-oc_no",
            "Company-rex_no",
            "Company-certification_body_code_no",
            "Company-fssai_license_no",
            "Company-ie_code_no",
            "Sales Invoice Item-no_and_kind_of_pkgs",
            "Sales Invoice Item-marks_and_numbers",
            "Sales Invoice Item-cn_code",
            "Sales Invoice Item-export_details",
            "Operation-quality_inspection_required",
            "Job Card-quality_inspection_status",
            "Employee-other_details",
            "Employee-aadhar_number",
            "Employee-voter_id_card_number",
            "Employee-column_break_84",
            "Employee-driving_licence_number",
            "Employee-uan_no",
            "Employee-pf_member_id",            
            "ToDo-check_list",
            "ToDo-check_list_1",
            "ToDo-attach_image_1",
            "ToDo-check_list_2",
            "ToDo-attach_image_2",
            "ToDo-check_list_3",
            "ToDo-attach_image_3",
            "ToDo-check_list_4",
            "ToDo-attach_image_4",
            "ToDo-check_list_5",
            "ToDo-attach_image_5",
            "ToDo-check_list_1_details",
            "ToDo-check_list_2_details",
            "ToDo-check_list_3_details",
            "ToDo-check_list_4_details",
            "ToDo-check_list_5_details",
            "ToDo-naming_series",
            "ToDo-column_break_11",
            "Task-project_name",
            "Employee-asset_details",
            "Employee-handover_asset_details",
            "Employee-handover_date",
            "Employee-petty_cash_account",
            "Journal Entry-petty_cash_request",
            "Employee-petty_cash_approver",
            "Expense Claim-type",
            "Expense Claim-other_party",
            "Company-bank_account_details",
            "Company-bank_details",
            "Expense Claim-other_party_name",
            "Sales Invoice-place_of_supply_",

            "Sales Order-is_export_invoice",
            "Sales Order-export",
            "Sales Order-export_details",
            "Sales Order-state",
            "Sales Order-country_of_origin_of_goods",
            "Sales Order-country_of_final_destination",
            "Sales Order-port_of_loading",
            "Sales Order-column_break_177",
            "Sales Order-port_of_discharge",
            "Sales Order-final_destination",
            "Sales Order-date_of_supply",
            "Sales Order-place_of_supply_",
            "Sales Order-receiver_details",
            "Sales Order-consignee",
            "Sales Order-notify",
            "Sales Order-column_break_185",
            "Sales Order-notify2",
            "Sales Order-other_information",
            "Sales Order-mode_of_transportation",
            "Sales Order-vessel_no",
            "Sales Order-flight_no",
            "Sales Order-place_of_receipt_by_pre_carrier",
            "Sales Order-vehicle_number",
            "Sales Order-container_no",
            "Sales Order-seal_no",
            "Sales Order-ico_lot_no",
            "Sales Order-coffee_board_permit_no",
            "Sales Order-column_break_197",
            "Sales Order-pre_carriage_by",
            "Sales Order-harvest_year",
            "Sales Order-certification_details",
            "Sales Order-statement_of_origin",
            "Sales Order-statement",
            "Company-column_break_111",
            "Company-address_details",
            "Sales Order Item-export_details",
            "Sales Order Item-marks_and_numbers",
            "Sales Order Item-no_and_kind_of_pkgs",
            "Sales Order Item-cn_code",
            "ToDo-company",
            "Sales Invoice-notify_3",
            "Sales Invoice-flo_id",
            "Sales Invoice-eori",
            "Batch-work_order",
            "Sales Invoice-export_remarks",
            
            "User-custom_country_code",
            "User-custom_fcm_token",
            "User-custom_type",
            "User-custom_comments",


            "Purchase Order-custom_farm_id",
            "Purchase Order-custom_farmer_id",
            "Purchase Order-custom_crops",
            "Purchase Order-custom_animal_husbandry",
            "Purchase Order-custom_vehicle_number",
            "Purchase Order-custom_notes",
            "Purchase Order-custom_section_break_mdudx",
            "Country-custom_id_card_list",
            "Purchase Order-custom_farmer_name",
            "Purchase Order-custom_custom_farm_name",
            "Purchase Receipt-custom_farm_id",
            "Purchase Receipt-custom_farm_name",
            "Purchase Receipt-custom_farmer_id",
            "Purchase Receipt-custom_farmer_name",
            "Supplier-custom_is_farmer",
            "Purchase Order-custom_is_farmer",
            "Purchase Receipt-custom_is_farmer",
            "Purchase Invoice-custom_farm_id",
            "Purchase Invoice-custom_farm_name",
            "Purchase Invoice-custom_farmer_id",
            "Purchase Invoice-custom_farmer_name",
            "Purchase Invoice-custom_is_farmer",
            "Purchase Order-custom_survey",
            "Purchase Receipt-custom_survey",
            "Purchase Invoice-custom_survey",
            "Country-country_base_item_group",
            "Item-item_type",
            "Purchase Order Item-item_type",
            "Purchase Order-place",
            "Purchase Receipt Item-item_type",
            "Purchase Receipt-place",
            "Job Offer-description",
            "Job Offer-job_description",
            "Job Applicant-previous_company_name_",
            "Job Applicant-reference_person_name_",
            "Supplier-custom_contact_number_"

		]]
	]
},
{
		"doctype":"Property Setter",
		"filters": [
			[
				"name",
				"in",
				[
                    "Expense Claim-employee-reqd",
                    "Expense Claim-employee-depends_on",
                    "Expense Claim-employee_name-depends_on",
                    "Expense Claim-Employee-mandatory_depends_on",

                ]
			]
		]
	},
]
 
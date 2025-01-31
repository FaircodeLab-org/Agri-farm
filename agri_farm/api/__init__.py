import frappe, json, requests
from frappe.utils.password import get_decrypted_password
from agri_farm.api.sync_data import sync_farmers
from agri_farm.api.farmer import get_farmers
from agri_farm.api.items import get_items
from agri_farm.api.purchase_order import get_orders
from agri_farm.api.visit_report import get_visit_reports
from agri_farm.api.attendance import sync_attendance
from agri_farm.api.purchase_order import sync_po
# {
#     'farmer': [
#         '{
#            "company":"Plantrich Agritech Private Limited",
#             "first_name":"12",
#             "last_name":"12",
#             "father_name":"12",
#             "project":"Project 4",
#             "families_members":"21",
#             "gender":"Male",
#             "date_of_birth":"2022-12-15",
#             "state":"State 2",
#             "society":"Society 4",
#             "phone_number":"345435",
#             "country":"Argentina",
#             "district":"District 5",
#             "village":"Village 1",
#             "inspector":"Inspector 1",
#             "season":"2022-2023",
#             "bank_name":"23423",
#             "bank_ifsc":"345345",
#             "bank_acc_no":"456546",
#             "bank_branch":"35435",
#             "pin_code":"546456",
#             "aadhar_number":"45645",
#             "total_farmland":"345345",
#             "inspection_date":"2022-12-15",
#             "local_Id":"1671097913695"}'], 'plots': ['{"company":"Plantrich Agritech Private Limited","erpnext_farmer_id":"1671097913695","farmer_name":"12","plot_name":"234","total_plot_area":"23","crop_unit":"Acre","fallow_land":"12","latitude":"11.29207","longitude":"75.82582","local_plot_id":"1671097913695"}'], 'crops': ['{"crop":"Test Crop","plot_name":"12","number_of_plants":"12","starting_date":"2022-12-15","plot_area":"12","mature_plant":"12","non_mature_plant":"12","erpnext_plot_id":"1671097913695"}']}
@frappe.whitelist()
def sync_data():
    data = json.loads(frappe.request.data)
    frappe.log_error("Sync Data",str(data))
    sync_farmers(data)
    sync_attendance(data)
    sync_po(data)

    return {"success": True, "message": "Synced Data"}



@frappe.whitelist(allow_guest=True)
def login():
    frappe.log_error("INSIDE LOGIN", "INSIDE LOGIN")
    try:
        data = json.loads(frappe.request.data)
        email = data.get('user')
        password = data.get('password')
        protocol = data.get('protocol')
        site = data.get('site')

        if not email:
            return {"success": False, "message": "Invalid Email"}
        if not password:
            return {"success": False, "message": "Invalid Password"}
        if not protocol:
            return {"success": False, "message": "Invalid Protocol"}
        if not site:
            return {"success": False, "message": "Invalid Site Name"}
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        credentials = {
            "usr": email,
            "pwd": password
        }
        data = requests.get(
            protocol + "://" + site + "/api/method/login",
            headers=headers,
            json=credentials).json()

        if data['message'] == 'Logged In':
            user = frappe.db.sql(""" SELECT * FROM `tabUser` where email=%s """, email, as_dict=1)
            pwrd = get_decrypted_password("User", user[0].name, "api_secret")
            data = get_data(email)
            return {
                "success": True,
                "message": "Login Successful",
                "data": {
                    "api_key": user[0].api_key,
                    "api_secret": pwrd,
                    "data": data
                }
            }
        else:
            return {"success": False, "message": "Login Failed"}
    except:
        frappe.log_error(frappe.get_traceback(), "ERROR LOGIN")
    return {"success": False, "message": "Login Failed"}

@frappe.whitelist()
def get_data(email):
    employee = frappe.db.sql(""" SELECT * FROM `tabEmployee` WHERE user_id=%s """, email,as_dict=1)
    if len(employee) == 0:
        return {"message": "Fetching of Data Failed. User is not an Employee. Please contact ERPNext Administrator"}

    companies = frappe.db.sql(""" SELECT name FROM `tabCompany` WHERE name=%s""",employee[0].company, as_dict=1)
    villages = frappe.db.sql(""" SELECT village FROM `tabVillage`""", as_dict=1)
    districts = frappe.db.sql(""" SELECT district FROM `tabDistrict`""", as_dict=1)
    seasons = frappe.db.sql(""" SELECT name FROM `tabFiscal Year`""", as_dict=1)
    inspectors = frappe.db.sql(""" SELECT inspector FROM `tabInspector`""", as_dict=1)
    farmers_ = get_farmers(employee[0].company)
    farmers = farmers_.get("data").get("farmers")
    states = frappe.db.sql(""" SELECT state FROM `tabState`""", as_dict=1)
    societies = frappe.db.sql(""" SELECT society FROM `tabSociety`""", as_dict=1)
    crops = frappe.db.sql(""" SELECT crop FROM `tabCrop Parent`""", as_dict=1)
    crop_units = frappe.db.sql(""" SELECT name as crop_unit FROM `tabCrop Unit`""", as_dict=1)
    projects = frappe.db.sql(""" SELECT name as project FROM `tabAgri Project`""", as_dict=1)
    countries = frappe.db.sql(""" SELECT name as country FROM `tabCountry`""", as_dict=1)
    suppliers = frappe.db.sql(""" SELECT name as supplier, supplier_name FROM `tabSupplier`""", as_dict=1)
    certification_types = frappe.db.sql(""" SELECT name as certification FROM `tabCertification`""", as_dict=1)
    orders_ = get_orders(employee[0].company)
    items1 = get_items()
    visit_reports = get_visit_reports(employee[0].company)
    items_ = items1.get("data").get("items")
    orders = orders_.get("data").get("purchase_orders")
    visit_reports_ = visit_reports.get("data").get("visit_reports")

    obj = {
        "visit_reports_": visit_reports_,
        "suppliers": suppliers,
        "items": items_,
        "orders": orders,
        "villages": villages,
        "districts": districts,
        "seasons": seasons,
        "inspectors": inspectors,
        "farmers": farmers,
        "states": states,
        "societies": societies,
        "companies": companies,
        "crops": crops,
        "crop_units": crop_units,
        "projects": projects,
        "countries": countries,
        "certification_types": certification_types,
    }

    return obj
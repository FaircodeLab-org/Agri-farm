import frappe,json,requests
from frappe.utils.password import get_decrypted_password
from agri_farm.api.plot import fetch_plots_based_on_farmer
# data =  {
#         "company": "Plantrich Agritech Private Limited",
#         "first_name": "TEST FARMER 2222",
#         "last_name": "LAST NAME",
#         "families_members": "6",
#         "gender": "Male",
#         "state": "State 1",
#         "society": "Society 1",
#         "vendor_code": "123456",
#         "phone_number": "12345567",
#         "country": "India",
#         "district": "District 1",
#         "village": "Village 1",
#         "season": "2022-2023",
#         "inspector": "Inspector 1",
#         "bank_name": "Bank Name 1",
#         "bank_ifsc": "Bank IFSC 1",
#         "bank_acc_no": "Bank Acc No 1",
#         "bank_branch": "Bank Branch 1s",
#         "pin_code": "1234",
#         "aadhar_number": "Aadhar Number 1",
#         "total_farmland": "700",
#         "inspection_date": "2022-11-30",
#         "date_of_birth": "2022-11-30",
#         "project":"Project 1"
#
#     }
def get_certifications(data):
    certifications = []
    if data:
        for i in data:
            certifications.append({
                "certification_type": i
            })
    return certifications
@frappe.whitelist()
def add_farmer(farmer_data=None):
    print("ADD FARMER")
    if farmer_data:
        data = farmer_data
    else:
        data = json.loads(frappe.request.data)
    frappe.log_error("Add Farmer Method Executed", "Add Farmer Method NOT AN ERROR")
    frappe.log_error("Add Farmer Method Executed", str(data))
    company_check = frappe.db.sql(""" SELECT * FROm `tabCompany` WHERE name=%s """, data.get("company"),as_dict=1)
    frappe.log_error("Company does not exist", str(company_check))

    if len(company_check) == 0:
        frappe.log_error("Company does not exist","Company does not exist")
        return {"success": False, "message": "Company Does Not Exist"}
    try:
        obj = {
            "doctype": "Farmer",
            "company": data.get('company'),
            "first_name": data.get('first_name'),
            "last_name": data.get('last_name'),
            "father_name": data.get('father_name'),
            "project": data.get('project') if data.get("project") else [],
            "families_members": data.get('families_members'),
            "gender": data.get('gender'),
            "state": data.get('state') if data.get("state") else [],
            "society": data.get('society') if data.get("society") else [],
            "vendor_code": data.get('vendor_code'),
            "phone_number": data.get('phone_number'),
            "country": data.get('country'),
            "district": data.get('district') if data.get("district") else [],
            "village": data.get('village') if data.get("village") else [],
            "season": data.get('season'),
            "inspector": data.get('inspector') if data.get("inspector") else [],
            "bank_name": data.get('bank_name'),
            "bank_ifsc": data.get('bank_ifsc'),
            "bank_acc_no": data.get('bank_acc_no'),
            "bank_branch": data.get('bank_branch'),
            "pin_code": data.get('pin_code'),
            "aadhar_number": data.get('aadhar_number'),
            "total_farmland": data.get('total_farmland'),
            "inspection_date": data.get('inspection_date'),
            "date_of_birth": data.get('date_of_birth'),
            "member_since": data.get('member_since'),
            "organic_farm_land": data.get('organic_farm_land'),
            "farmer_code": data.get('farmer_code'),
            "address": data.get('address'),
            "organically_certified": data.get('organically_certified'),
            "certification_type":get_certifications(data.get("certifications"))
        }


        farmer = frappe.get_doc(obj).insert()
        frappe.db.commit()
        auto_create_supplier = frappe.db.get_single_value("Agri Farm Settings", "auto_create_supplier")
        if auto_create_supplier:
            create_supplier(farmer,data)
        if farmer.name:
            return { "success": True,"message": "Farmer Creation Successful", "data": {"erpnext_farmer_id": farmer.name}}
    except:
        frappe.log_error(frappe.get_traceback(),"Add Farmer Error")
        return {"success": False, "message": "Farmer Creation Failed"}
def create_supplier(farmer,data):
    supplier_group = frappe.db.get_single_value("Agri Farm Settings", "supplier_group")
    auto_link_supplier = frappe.db.get_single_value("Agri Farm Settings", "auto_link_supplier")

    obj = {
        "doctype": "Supplier",
        "supplier_name": farmer.first_name + " " + farmer.last_name,
        "supplier_group": supplier_group,
        "certification_type": data.get("certification_types") if data.get("certification_types") else []
    }
    supplier = frappe.get_doc(obj).insert()
    if auto_link_supplier:
        farmer = frappe.get_doc("Farmer", farmer.name)
        farmer.supplier = supplier.name
        farmer.save()

@frappe.whitelist()
def update_farmer(farmer_data=None):
    if farmer_data:
        data = farmer_data
    else:
        data = json.loads(frappe.request.data)

    # frappe.log_error("UPDATE Farmer Method Executed", data.get('gender') + " " + str(data.get('families_members')) + " " +  data.get('country'))
    try:
        farmer_based_on_id = frappe.db.sql("""SELECT * FROM `tabFarmer` WHERE name=%s """, data.get('erpnext_farmer_id'), as_dict=1)
        if len(farmer_based_on_id) == 0:
            return {"success": False, "message": "Farmer does not exists"}
        frappe.db.sql(""" UPDATE `tabFarmer` 
                          SET 
                          country=%s,
                          families_members=%s, 
                          gender=%s,
                          company=%s,
                          first_name=%s,
                          last_name=%s,
                          father_name=%s,
                          date_of_birth=%s,
                          state=%s,
                          society=%s,
                          vendor_code=%s,
                          phone_number=%s,
                          district=%s,
                          village=%s,
                          project=%s,
                          season=%s,
                          inspector=%s,
                          bank_name=%s,
                          bank_ifsc=%s,
                          bank_acc_no=%s,
                          bank_branch=%s,
                          pin_code=%s,
                          aadhar_number=%s,
                          total_farmland=%s,
                          inspection_date=%s,
                          organic_farm_land=%s,
                          member_since=%s,
                          farmer_code=%s,
                          address=%s,
                          organically_certified=%s
                          WHERE name=%s
                          """, (data.get('country') if data.get('country') else None,
                                data.get('families_members') if data.get('families_members') else None,
                                data.get('gender') if data.get('gender') else None,
                                data.get('company') if data.get('company') else None,
                                data.get('first_name') if data.get('first_name') else None,
                                data.get('last_name') if data.get('last_name') else None,
                                data.get('father_name') if data.get('father_name') else None,
                                data.get('date_of_birth') if data.get('date_of_birth') else None,
                                data.get('state') if data.get('state') else None,
                                data.get('society') if data.get('society') else None,
                                data.get('vendor_code') if data.get('vendor_code') else None,
                                data.get('phone_number') if data.get('phone_number') else None,
                                data.get('district') if data.get('district') else None,
                                data.get('village') if data.get('village') else None,
                                data.get('project') if data.get('project') else None,
                                data.get('season') if data.get('season') else None,
                                data.get('inspector') if data.get('inspector') else None,
                                data.get('bank_name') if data.get('bank_name') else None,
                                data.get('bank_ifsc') if data.get('bank_ifsc') else None,
                                data.get('bank_acc_no') if data.get('bank_acc_no') else None,
                                data.get('bank_branch') if data.get('bank_branch') else None,
                                data.get('pin_code') if data.get('pin_code') else None,
                                data.get('aadhar_number') if data.get('aadhar_number') else None,
                                data.get('total_farmland') if data.get('total_farmland') else None,
                                data.get('inspection_date') if data.get('inspection_date') else None,
                                data.get('organic_farm_land') if data.get('organic_farm_land') else None,
                                data.get('member_since') if data.get('member_since') else None,
                                data.get('farmer_code') if data.get('farmer_code') else None,
                                data.get('address') if data.get('address') else None,
                                data.get('organically_certified') if data.get('organically_certified') else None,
                                data.get('erpnext_farmer_id')
                                ))
        frappe.db.commit()

        if data.get("certifications"):
            for x in data.get("certifications"):
                frappe.db.sql(""" UPDATE `tabCertification Type`  SET certification_type=%s WHERE name=%s""", (x,x.get("certification_type_id")))
                frappe.db.commit()

        return { "success": True,"message": "Farmer Updated Successful"}
    except:
        frappe.log_error(frappe.get_traceback(),"Update Farmer Error")
        return {"success": False, "message": "Updating Farmer Failed"}

@frappe.whitelist()
def delete_certification_type():
    data = json.loads(frappe.request.data)
    frappe.db.sql(""" DELETE FROM `tabCertification Type`  WHERE name=%s""",data.get("erpnext_certification_type_id"))
    frappe.db.commit()
def get_condition(x):
    condition = ''
    if x == 'state':
        condition += "state = '{0}'".format(x)
    elif x == 'society':
        condition += "society = '{0}'".format(x)
    elif x == 'inspector':
        condition += "inspector = '{0}'".format(x)
    elif x == 'village':
        condition += "village = '{0}'".format(x)
    elif x == 'district':
        condition += "district = '{0}'".format(x)
    return condition
@frappe.whitelist()
def delete_farmer():
    data = json.loads(frappe.request.data)
    farmer_id = data.get('erpnext_farmer_id')

    try:
        frappe.log_error("DELETE Farmer Method Executed", "DELETE Farmer Method NOT AN ERROR")
        farmer_based_on_id = frappe.db.sql("""SELECT * FROM `tabFarmer` WHERE name=%s """, farmer_id,as_dict=1)
        if len(farmer_based_on_id) == 0:
            return {"success": False, "message": "Farmer does not exists"}
        farmer = frappe.get_doc("Farmer", farmer_id)
        farmer.delete()
        return {"success": True, "message": "Farmer Deleted"}
    except:
        frappe.log_error(frappe.get_traceback(), "Delete Farmer Error")
        return {"success": False, "message": "Farmer deletion failed"}

@frappe.whitelist()
def get_farmers(company=None):
    if not company:
        data = json.loads(frappe.request.data)
        employee = frappe.db.sql(""" SELECT * FROM `tabEmployee` WHERE user_id=%s """, data.get("user_id"), as_dict=1)
        if len(employee) == 0:
            return {"message": "Fetching of Data Failed. User is not an Employee. Please contact ERPNext Administrator"}
        company = employee[0].company

    frappe.log_error("GET Farmer Method Executed", "GET Farmer Method NOT AN ERROR")
    try:
        farmers = frappe.db.sql(""" SELECT 
                                         company, 
                                         name as erpnext_farmer_id, 
                                         first_name,
                                         last_name,
                                         father_name,
                                         project,
                                         families_members,
                                         gender, 
                                         date_of_birth,
                                         state,
                                         society,
                                         vendor_code,
                                         phone_number,
                                         country,
                                         district,
                                         village,
                                         inspector,
                                         season,
                                         bank_name,
                                         bank_ifsc,
                                         bank_acc_no,
                                         bank_branch,
                                         pin_code,
                                         aadhar_number,
                                         total_farmland,
                                         inspection_date,
                                          organic_farm_land,
                                          member_since,
                                          farmer_code,
                                          address
                                       FROM `tabFarmer` WHERE company=%s""",company, as_dict=1)
        for x in farmers:
            x['plots'] = fetch_plots_based_on_farmer(x.erpnext_farmer_id)
            x['certifications'] = get_certifications_farmer(x.erpnext_farmer_id)
        return { "success": True,"message": "Fetched Farmers", "data": {"farmers": farmers}}
    except:
        frappe.log_error(frappe.get_traceback(),"Add Farmer Error")
        return {"success": False, "message": "Fetching Farmers Failed"}

def get_certifications_farmer(erpnext_farmer_id):

    return frappe.db.sql(""" SELECT name as erpnext_certification_type_id, certification_type FROM `tabCertification Type` WHERE parent=%s""",(erpnext_farmer_id),as_dict=1)

@frappe.whitelist()
def get_projects():
    projects = frappe.db.sql(""" SELECT name as project FROM `tabAgri Project` """, as_dict=1)
    return {"success": True, "message": "Fetched Projects", "data": {"projects": projects}}

@frappe.whitelist()
def get_countries():
    projects = frappe.db.sql(""" SELECT name as country FROM `tabCountry` """, as_dict=1)
    return {"success": True, "message": "Fetched Countries", "data": {"countries": projects}}
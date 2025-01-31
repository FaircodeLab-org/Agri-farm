import frappe,json
done = False
def create_update_attendance(data, type):
    frappe.log_error(type, str(data))
    get_employee = frappe.db.sql(""" SELECT * FROM `tabEmployee` WHERE user_id=%s """, data.get("user_id"), as_dict=1)
    if len(get_employee) == 0:
        return {"success": False,"message": "Punched In Failed. User must be set to an employee. Please contact Administrator"}

    check_attendance = frappe.db.sql(
        """ SELECT * FROM `tabAgri Farm Attendance` WHERE posting_date=%s and employee=%s and docstatus<2""", (data.get("date"),get_employee[0].name),
        as_dict=1)
    frappe.log_error("CHECK ATTENDANCE",str(check_attendance))

    if len(check_attendance) == 0:
        obj = {
            "doctype": "Agri Farm Attendance",
            "posting_date": data.get("date"),
            "attendance_date": data.get("date"),
            "employee": get_employee[0].name,
            "attendance": [{
                "type": type,
                "longitude": data.get("longitude"),
                "latitude": data.get("latitude"),
                "time": data.get("time").split(" ")[0],
                "time_type": data.get("time").split(" ")[1],
            }]
        }

        agri_farm_att = frappe.get_doc(obj).insert()
        agri_farm_att.submit()
        frappe.db.commit()
        return {"success": True, "message": type}
    else:
        obj = {
            "doctype": "Agri Farm Attendance Details",
            "parent": check_attendance[0].name,
            "parenttype": "Agri Farm Attendance",
            "parentfield": "attendance",
            "type": type,
            "longitude": data.get("longitude"),
            "latitude": data.get("latitude"),
            "time": data.get("time").split(" ")[0],
            "time_type": data.get("time").split(" ")[1],
        }

        agri_farm_att1 = frappe.get_doc(obj).insert()
        agri_farm_att1.submit()
        frappe.db.commit()
        return {"success": True, "message": type}
@frappe.whitelist()
def punch_in():
    data = json.loads(frappe.request.data)
    try:
        return create_update_attendance(data, "Punch In")
    except:
        frappe.log_error("Punch In", frappe.get_traceback())

@frappe.whitelist()
def punch_out():
    data = json.loads(frappe.request.data)
    try:
        return create_update_attendance(data, "Punch Out")
    except:
        frappe.log_error("Punch Out", frappe.get_traceback())
@frappe.whitelist()
def travelling():
    data = json.loads(frappe.request.data)
    try:
        return create_update_attendance(data, "Travel")
    except:
        frappe.log_error("Travel", frappe.get_traceback())
@frappe.whitelist()
def stoppage():
    data = json.loads(frappe.request.data)
    try:
        return create_update_attendance(data, "Stoppage")
    except:
        frappe.log_error("Stoppage", frappe.get_traceback())


def sync_attendance(data):

    for i in data.get("attendance"):
        a = json.loads(i)
        for x in a:
            f_type = get_type(x)
            create_update_attendance(a[x], f_type)

def get_type(x):
    if "-" in x:
        type_split = x.split("-")
        return type_split[0].capitalize() + " " + type_split[1].capitalize()
    else:
        return x.capitalize()
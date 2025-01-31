import frappe,json,requests
from frappe.utils.password import get_decrypted_password
from frappe.utils.file_manager import save_file
import base64
import os

def get_questions(questions):
    q = []

    for i in questions:
        q.append({
            "question": i.get("question"),
            "answer": i.get("answer"),
            "explanation":i.get("explanation")
        })
    return q

@frappe.whitelist()
def add_visit_report_crops(crops, erpnext_visit_report_id):

    for i in crops:
        obj = {
            "doctype": "Plot Crops",
            "parenttype": "Visit Report",
            "parentfield": "crops",
            "parent": erpnext_visit_report_id,
            "crop": i.get("crop"),
            "plot_name": i.get("plot_name"),
            "number_of_plants": i.get("number_of_plants"),
            "plot_area": i.get("plot_area"),
            "start_date": i.get("starting_date"),
        }
        frappe.get_doc(obj).insert(ignore_permissions=1)
        frappe.db.commit()

@frappe.whitelist()
def add_visit_report(visit_report_data=None):
    if visit_report_data:
        data = visit_report_data
    else:
        data = json.loads(frappe.request.data)
    frappe.log_error("Add Visit Report Method Executed", "Add Visit Report Method NOT AN ERROR")
    frappe.log_error("image", data.get("image"))


    frappe.log_error("audio",data.get("audio"))
    frappe.log_error("data",str(data))
    time_format = data.get('time').split(" ")
    try:
        obj = {
            "doctype": "Visit Report",
            "company": data.get('company'),
            "posting_date": data.get('date'),
            "time_format": time_format[1],
            "posting_time": time_format[0],
            "farmer": data.get('erpnext_farmer_id'),
            "farmer_name": data.get('farmer_name'),
            "longitude": data.get("longitude"),
            "latitude": data.get("latitude"),
            "visit_type": data.get("visit_type"),
            "remarks": data.get("remarks"),

            "quantity_own_consumptionT": data.get("quantity_own_consumptionT"),
            "quantity_sale_consumption": data.get("quantity_sale_consumption"),
            "quantity_left_seed": data.get("quantity_left_seed"),
            "employee_below_30": data.get("employee_below_30"),
            "permenent_workers": data.get("permenent_workers"),
            "faritrade_member": data.get("faritrade_member"),

            "visit_report_questions": get_questions(data.get("questions")),

        }
        plot = frappe.get_doc(obj).insert()
        frappe.db.commit()
        if data.get("crops"):
            add_visit_report_crops(data.get("crops"), plot.name)
        if data.get("audio"):
            add_visit_report_audio(data.get("audio"), plot.name)

        # sf = save_file("test.jpeg", data.get("image"), "Visit Report", plot.name)
        if data.get("image"):
            upload_image(data,plot)
        if plot.name:
            return { "success": True,"message": "Visit Report Creation Successful", "data": {"erpnext_visit_report_id": plot.name}}
    except:
        frappe.log_error(frappe.get_traceback(),"Add Visit Report Error")
        return {"success": False, "message": "Plot Creation Failed"}
def upload_image(data,plot):

    path = os.path.abspath(__file__)
    path = path.rsplit('/apps/', 1)[0]

    import base64
    from io import BytesIO
    from PIL import Image
    file = ""
    with open("imageToSave.png", "wb") as fh:
        byte_file = data.get("image")
        file = base64.b64decode(byte_file)
    frappe.log_error("encode result", str(file))
    actual_file = Image.open(BytesIO(file))
    file_name = plot.name.replace("-","_")
    actual_file.save(frappe.get_site_path() + "/public" + "/files/" + file_name +".jpeg", quality=95)
    frappe.db.sql(""" UPDATE `tabVisit Report` SET attach_image=%s, image_base_64=%s WHERE name=%s""", ("/files/" + file_name +".jpeg",data.get("image"),plot.name))
    frappe.db.commit()

@frappe.whitelist()
def update_visit_report(visit_report_data=None):

    if visit_report_data:
        data = visit_report_data
    else:
        data = json.loads(frappe.request.data)
    frappe.log_error("UPDATE Visit Report Method Executed", "UPDATE Visit Report NOT AN ERROR")
    frappe.log_error("visit report data", str(data))
    time_format = data.get('time').split(" ")
    try:
        plot_based_on_id = frappe.db.sql("""SELECT * FROM `tabVisit Report` WHERE name=%s """, data.get('erpnext_visit_report_id'), as_dict=1)
        if len(plot_based_on_id) == 0:
            return {"success": False, "message": "Visit Report does not exists"}
        frappe.db.sql(""" UPDATE `tabVisit Report` SET 
                          company=%s,
                          farmer=%s, 
                          posting_date=%s,
                          posting_time=%s,
                          time_format=%s,
                          longitude=%s,
                          latitude=%s,
                          visit_type=%s,
                          remarks=%s,
                          
                          quantity_own_consumptionT=%s,
                          quantity_sale_consumption=%s,
                          quantity_left_seed=%s,
                          employee_below_30=%s,
                          permenent_workers=%s,
                          faritrade_member=%s,
                          
                          farmer_name=%s WHERE name=%s""",
                      (data.get('company'),data.get('erpnext_farmer_id'),data.get('date'),
                       time_format[0],time_format[1],data.get('longitude'),data.get('latitude'),
                       data.get('visit_type'),data.get('remarks'),

                       data.get('quantity_own_consumptionT'),data.get('quantity_sale_consumption'),
                       data.get('quantity_left_seed'),data.get('employee_below_30'),
                       data.get('permenent_workers'),data.get('faritrade_member'),

                       data.get('farmer_name'),data.get('erpnext_visit_report_id')
                       ))
        frappe.db.commit()
        plot = frappe.get_doc("Visit Report", data.get('erpnext_visit_report_id'))

        if data.get("image"):
            upload_image(data,plot)
        if data.get("audio"):
            add_visit_report_audio(data.get("audio"), data.get('erpnext_visit_report_id'))

        update_questions(data.get("questions"),data.get('erpnext_visit_report_id'))
        return { "success": True,"message": "Visit Report Updated Successful"}
    except:
        frappe.log_error(frappe.get_traceback(),"Update Visit Report Error")
        return {"success": False, "message": "Updating Visit Report Failed"}
def update_questions(questions, visit_report_id):
    for i in questions:
        frappe.db.sql(""" UPDATE `tabVisit Report Questions` 
                          SET question=%s, answer=%s,explanation=%s  
                          WHERE question=%s and parent=%s""", (i.get("question"),i.get("answer"),i.get("explanation"),i.get("question"),visit_report_id))
        frappe.db.commit()
@frappe.whitelist()
def delete_visit_report():
    data = json.loads(frappe.request.data)
    plot_id = data.get('erpnext_visit_report_id')

    try:
        frappe.log_error("DELETE Visit Report Method Executed", "DELETE Visit Report Method NOT AN ERROR")
        plot_based_on_id = frappe.db.sql("""SELECT * FROM `tabVisit Report` WHERE name=%s """, plot_id,as_dict=1)
        if len(plot_based_on_id) == 0:
            return {"success": False, "message": "Visit Report does not exists"}
        plot = frappe.get_doc("Visit Report", plot_id)
        plot.delete()
        return {"success": True, "message": "Visit Report Deleted"}
    except:
        frappe.log_error(frappe.get_traceback(), "Delete Visit Report Error")
        return {"success": False, "message": "Visit Report deletion failed"}

@frappe.whitelist()
def get_visit_reports(company = None):
    if not company:
        data = json.loads(frappe.request.data)
        employee = frappe.db.sql(""" SELECT * FROM `tabEmployee` WHERE user_id=%s """, data.get("user_id"), as_dict=1)
        if len(employee) == 0:
            return {"message": "Fetching of Data Failed. User is not an Employee. Please contact ERPNext Administrator"}
        company = employee[0].company
    frappe.log_error("GET Visit Report Method Executed", "GET Visit Report Method NOT AN ERROR")
    try:
        plots = frappe.db.sql(""" SELECT 
                                     name as erpnext_visit_report_id,
                                      company,
                                      visit_type,
                                      farmer as erpnext_farmer_id,
                                      farmer_name,
                                      posting_date,
                                      posting_time,
                                      time_format,
                                      remarks,
                                      longitude,
                                      quantity_own_consumptionT,
                                      quantity_sale_consumption,
                                      quantity_left_seed,
                                      employee_below_30,
                                      permenent_workers,
                                      faritrade_member,
                                      image_base_64 as image, 
                                      latitude
                                   FROM `tabVisit Report` WHERE company=%s """,company, as_dict=1)
        for i in plots:
            c_posting_time = str(i.posting_time).split(":") if i.posting_time else ""
            f_posting_time = c_posting_time[0] + ":" + c_posting_time[1] if i.posting_time else ""
            i['posting_time'] = f_posting_time
            i['questions'] = get_questions_for_visit_report(i.erpnext_visit_report_id)
            i['crops'] = get_crops_for_vr(i.erpnext_visit_report_id)
        return { "success": True,"message": "Fetched Reports", "data": {"visit_reports": plots}}
    except:
        frappe.log_error(frappe.get_traceback(),"Get Visit Report Error")
        return {"success": False, "message": "Fetching Visit Report Failed"}

def get_questions_for_visit_report(erpnext_visit_report_id):
        return frappe.db.sql(
            """ SELECT question, answer, explanation FROM `tabVisit Report Questions` WHERE parent=%s """,
            erpnext_visit_report_id, as_dict=1)

@frappe.whitelist()
def get_crops_for_vr(erpnext_plot_id):
    return frappe.db.sql(""" SELECT name as plot_crop_id, crop, plot_name, number_of_plants, plot_area, start_date FROM `tabPlot Crops` WHERE parent=%s """, erpnext_plot_id,as_dict=1)


def add_visit_report_audio(audio, visit_report):
    import base64
    file_name = frappe.get_site_path() + "/public" + "/files/" + visit_report.replace("-","_")+ ".wav"
    wav_file = open(file_name, "wb")
    decode_string = base64.b64decode(audio)
    wav_file.write(decode_string)

    obj = {
        "doctype": "File",
        "file_url":"/files/" + visit_report.replace("-","_")+ ".wav",
        "attached_to_doctype": "Visit Report",
        "attached_to_name": visit_report
    }

    frappe.get_doc(obj).insert()
    frappe.db.commit()
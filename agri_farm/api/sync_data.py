import frappe,json
from agri_farm.api.farmer import add_farmer,update_farmer
from agri_farm.api.plot import add_plot,update_plot
from agri_farm.api.plot import add_crops
from agri_farm.api.visit_report import add_visit_report,update_visit_report
def sync_farmers(data):
    farmers = []
    for i in data.get("farmer"):
        a = json.loads(i)
        if a.get("erpnext_farmer_id") == "null":
            farmer_ = add_farmer(a)
            data_farmer = farmer_.get("data")
            a['erpnext_farmer_id'] = data_farmer.get('erpnext_farmer_id')
            farmers.append(a)
            sync_plot(data, data_farmer.get("erpnext_farmer_id"),a.get("local_Id"))
            frappe.log_error("SYNC PLOT", "SYNC PLOT")
        elif a.get("erpnext_farmer_id") != "null":
            update_farmer(a)
    other_plots = []
    other_crops = []
    for i in data.get("plots"):
        a = json.loads(i)
        farmer_check = frappe.db.sql(""" SELECT * FROM `tabFarmer` WHERE name=%s """, a.get("erpnext_farmer_id"),
                                     as_dict=1)
        if len(farmer_check) > 0:
            other_plots.append(json.dumps(a))
    for i in data.get("crops"):
        a = json.loads(i)
        plot_check = frappe.db.sql(""" SELECT * FROM `tabPlot` WHERE name=%s """, a.get("erpnext_plot_id"),
                                     as_dict=1)
        if len(plot_check) > 0:
            other_crops.append(json.dumps(a))
    sync_plot({"plots": other_plots, "crops": data.get("crops")},"", "")
    sync_crops({"crops": other_crops},"", "")
    sync_visit_report(farmers,data)
def sync_plot(data, erpnext_farmer_id, local_id):
    plots = []
    for i in data.get("plots"):
        a = json.loads(i)
        if not erpnext_farmer_id and not local_id:
            plot_record = add_plot(a)
            plot_ = plot_record.get("data")
            sync_crops(data, plot_.get("erpnext_plot_id"), a.get("local_plot_id"))
        elif not a.get("erpnext_plot_id") and a.get("erpnext_farmer_id") == local_id:
            a['erpnext_farmer_id'] = erpnext_farmer_id
            plot_record = add_plot(a)
            plot_ = plot_record.get("data")
            sync_crops(data,plot_.get("erpnext_plot_id"),a.get("local_plot_id"))
        elif a.get("erpnext_plot_id"):
            update_plot(a)
    return plots

def sync_crops(data,erpnext_plot_id,local_plot_id):
    frappe.log_error("SYYNC CROOPS")
    crops = []
    for i in data.get("crops"):
        a = json.loads(i)
        # frappe.log_error(a.get("erpnext_plot_id") + "   " + local_plot_id)
        if not erpnext_plot_id and not local_plot_id:
            add_crops({"crops": [a], "erpnext_plot_id": a.get("erpnext_plot_id")})
        elif a.get("erpnext_plot_id") == local_plot_id:
            a['erpnext_plot_id'] = erpnext_plot_id
            crops.append(a)
    if erpnext_plot_id and local_plot_id:
        add_crops({"crops": crops, "erpnext_plot_id":erpnext_plot_id})
    return True

def sync_visit_report(farmers,data):
    frappe.log_error("SYYNC VISIT REPORT")


    for i in data.get("visitreport"):
        a = json.loads(i)
        # frappe.log_error(a.get("erpnext_plot_id") + "   " + local_plot_id)
        farmer_check = frappe.db.sql(""" SELECT * FROM `tabFarmer` WHERE name=%s """,a.get("erpnext_farmer_id"),as_dict=1)
        erpnext_farmer_id = a.get("erpnext_farmer_id") if len(farmer_check) > 0 else get_farmer_id(farmers,a.get("erpnext_farmer_id"))

        if erpnext_farmer_id and a.get("erpnext_visit_report_id") == 'null':
            a['erpnext_farmer_id'] = erpnext_farmer_id
            a['time'] = a.get("posting_time") + " " + a.get("time_Format")
            add_visit_report(a)
        elif a.get("erpnext_visit_report_id") != 'null':
            a['time'] = a.get("posting_time") + " " + a.get("time_Format")
            update_visit_report(a)
    return True

def get_farmer_id(farmers, farmer_id):

    for i in farmers:
        if i.get("local_Id") == farmer_id:
            return i.get("erpnext_farmer_id")
    return ""

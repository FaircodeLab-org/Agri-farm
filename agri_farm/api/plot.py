import frappe,json,requests
from frappe.utils.password import get_decrypted_password


@frappe.whitelist()
def add_crops(crop_data = None):
    if crop_data:
        data = crop_data
    else:
        data = json.loads(frappe.request.data)

    frappe.log_error("UPDATE PLOT Method Executed", "UPDATE PLOT NOT AN ERROR")
    frappe.log_error("DATAAA", str(data))
    try:
        plot_based_on_id = frappe.db.sql("""SELECT * FROM `tabPlot` WHERE name=%s """, data.get('erpnext_plot_id'),
                                         as_dict=1)
        if len(plot_based_on_id) == 0:
            return {"success": False, "message": "Plot does not exists"}
        for i in data.get("crops"):
            obj = {
                "doctype": "Plot Crops",
                "parenttype": "Plot",
                "parentfield": "crop_list",
                "parent": data.get('erpnext_plot_id'),
                "crop": i.get("crop"),
                "plot_name": i.get("plot_name"),
                "number_of_plants": i.get("number_of_plants"),
                "plot_area": i.get("plot_area"),
                "start_date": i.get("starting_date"),
                "mature_plant": i.get("mature_plant"),
                "non_mature_plant": i.get("non_mature_plant"),

                "harvest_type": i.get("harvest_type"),
                "estimated_yield_mt_fresh": i.get("yield_fresh"),
                "estimated_yield_mt_dired": i.get("yield_dried"),
                "previous_year_stock": i.get("previous_stock"),
            }
            frappe.get_doc(obj).insert(ignore_permissions=1)
            frappe.db.commit()
        return {"success": True, "message": "Plot Updated Successful"}
    except:
        frappe.log_error(frappe.get_traceback(), "Update PlotError")
        return {"success": False, "message": "Updating Plot Failed"}
@frappe.whitelist()
def add_plot(plot_data=None):
    if plot_data:
        data = plot_data
    else:
        data = json.loads(frappe.request.data)
    frappe.log_error("Add Plot Method Executed", "Add Plot Method NOT AN ERROR")
    frappe.log_error("Add Plot Method Executed", str(data))
    try:


        obj = {
            "doctype": "Plot",
            "company": data.get('company'),
            "farmer": data.get('erpnext_farmer_id'),
            "farmer_name": data.get('farmer_name'),
            "plot_name": data.get('plot_name'),
            "total_plot_area": data.get('total_plot_area'),
            "crop_unit": data.get('crop_unit'),
            "fallow_land": data.get('fallow_land'),
            "longitude": data.get("longitude"),
            "latitude": data.get("latitude"),
            "perimeter_mapping": str(data.get("perimeter_mapping")).replace("LatLng"," ").replace("(", "[").replace(")", "]") if data.get("perimeter_mapping") else "",
            "perimeter_mapping_from_ma": str(data.get("perimeter_mapping")) if data.get("perimeter_mapping") else "",
        }

        plot = frappe.get_doc(obj).insert()
        frappe.db.commit()
        if plot.name:
            return { "success": True,"message": "Plot Creation Successful", "data": {"erpnext_plot_id": plot.name}}
    except:
        frappe.log_error(frappe.get_traceback(),"Add Plot Error")
        return {"success": False, "message": "Plot Creation Failed"}

def get_crops(crops):
    f_crops = []
    for i in crops:
        f_crops.append({
            "crop": i.get("crop"),
            "plot_name": i.get("plot_name"),
            "number_of_plants": i.get("number_of_plants"),
            "plot_area": i.get("plot_area"),
        })
    return f_crops
# def update_crops(crops, plot):
#     for i in crops:
#         plot.append("crop_list",{
#             "crop": i.get("crop"),
#             "plot_name": i.get("plot_name"),
#             "number_of_plants": i.get("number_of_plants"),
#             "plot_area": i.get("plot_area"),
#             "start_date": i.get("start_date"),
#             "mature_plant": i.get("mature_plant"),
#             "non_mature_plant": i.get("non_mature_plant"),
#         })
@frappe.whitelist()
def update_plot(plot_data=None):
    if plot_data:
        data = plot_data
    else:
        data = json.loads(frappe.request.data)

    frappe.log_error("UPDATE PLOT Method Executed", "UPDATE PLOT NOT AN ERROR")
    try:
        plot_based_on_id = frappe.db.sql("""SELECT * FROM `tabPlot` WHERE name=%s """, data.get('erpnext_plot_id'), as_dict=1)
        if len(plot_based_on_id) == 0:
            return {"success": False, "message": "Plot does not exists"}
        # frappe.db.sql(""" DELETE FROM `tabPlot Crops` WHERE parent=%s""", data.get('erpnext_plot_id'))
        # frappe.db.commit()
        frappe.db.sql(""" UPDATE `tabPlot` 
                          SET 
                          company=%s,farmer=%s,
                          plot_name=%s,total_plot_area=%s,
                          crop_unit=%s,fallow_land=%s,
                          farmer_name=%s, longitude=%s,latitude=%s,
                          perimeter_mapping=%s, perimeter_mapping_from_ma=%s WHERE name=%s""",
                      (data.get('company'),data.get('erpnext_farmer_id'),data.get('plot_name'),
                       data.get('total_plot_area'),data.get('crop_unit'),data.get('fallow_land'),
                       data.get('farmer_name'),data.get('longitude'),data.get('latitude'),
                       str(data.get("perimeter_mapping")).replace("LatLng", " ").replace("(", "[").replace(")","]") if data.get("perimeter_mapping") else "",
                       str(data.get("perimeter_mapping")) if data.get("perimeter_mapping") else "",data.get('erpnext_plot_id')))
        frappe.db.commit()
        return { "success": True,"message": "Plot Updated Successful"}
    except:
        frappe.log_error(frappe.get_traceback(),"Update PlotError")
        return {"success": False, "message": "Updating Plot Failed"}
@frappe.whitelist()
def delete_plot():
    data = json.loads(frappe.request.data)
    plot_id = data.get('erpnext_plot_id')

    try:
        frappe.log_error("DELETE Plot Method Executed", "DELETE Plot Method NOT AN ERROR")
        plot_based_on_id = frappe.db.sql("""SELECT * FROM `tabPlot` WHERE name=%s """, plot_id,as_dict=1)
        if len(plot_based_on_id) == 0:
            return {"success": False, "message": "Plot does not exists"}
        plot = frappe.get_doc("Plot", plot_id)
        plot.delete()
        return {"success": True, "message": "Plot Deleted"}
    except:
        frappe.log_error(frappe.get_traceback(), "Delete Plot Error")
        return {"success": False, "message": "Plot deletion failed"}

@frappe.whitelist()
def get_plots():
    # data = json.loads(frappe.request.data)

    frappe.log_error("GET Plot Method Executed", "GET Plot Method NOT AN ERROR")
    try:
        plots = frappe.db.sql(""" SELECT 
                                     name as erpnext_plot_id,
                                      company,
                                      plot_name,
                                      farmer as erpnext_farmer_id,
                                      farmer_name,
                                      fallow_land,
                                      total_plot_area,
                                      crop_unit,
                                      latitude,
                                      longitude,
                                      perimeter_mapping_from_ma as perimeter_mapping,
                                      total_crop_list_plot_area
                                   FROM `tabPlot` """, as_dict=1)
        for i in plots:
            # if i.perimeter_mapping:
            #     i.perimeter_mapping = get_final_perimeter_mapping(i.perimeter_mapping)
            i['crops'] = get_crops_for_plot(i.erpnext_plot_id)
        return { "success": True,"message": "Fetched Plots", "data": {"plots": plots}}
    except:
        frappe.log_error(frappe.get_traceback(),"Get Plots Error")
        return {"success": False, "message": "Fetching Plot Failed"}
def get_final_perimeter_mapping(perimeter_mapping):
    fpm = []
    for i in eval(perimeter_mapping):
        fpm.append(eval("LatLng" + str(tuple(i))))
    return fpm
@frappe.whitelist()
def get_crops_for_plot(erpnext_plot_id):
    return frappe.db.sql(""" SELECT name as plot_crop_id, crop, plot_name, number_of_plants, plot_area, start_date, mature_plant, non_mature_plant, harvest_type, estimated_yield_mt_fresh,estimated_yield_mt_dired,previous_year_stock FROM `tabPlot Crops` WHERE parent=%s """, erpnext_plot_id,as_dict=1)

@frappe.whitelist()
def get_crops_for_plot_farmer(erpnext_plot_id):
    crops = frappe.db.sql(""" SELECT name as plot_crop_id, crop, plot_name, number_of_plants, plot_area, start_date, mature_plant, non_mature_plant, harvest_type, estimated_yield_mt_fresh,estimated_yield_mt_dired,previous_year_stock FROM `tabPlot Crops` WHERE parent=%s """, erpnext_plot_id,as_dict=1)

    return [i.crop for i in crops]
@frappe.whitelist()
def get_all_crops():
    data = json.loads(frappe.request.data)

    return frappe.db.sql(""" SELECT name as plot_crop_id, crop, plot_name, number_of_plants, plot_area, start_date, mature_plant, non_mature_plant, harvest_type, estimated_yield_mt_fresh,estimated_yield_mt_dired,previous_year_stock FROM `tabPlot Crops` WHERE parent=%s """, data.get("erpnext_plot_id"),as_dict=1)

@frappe.whitelist()
def fetch_all_crops():
    return frappe.db.sql(""" SELECT name as plot_crop_id, crop, plot_name, number_of_plants, plot_area, start_date, mature_plant, non_mature_plant, parent as erpnext_plot_id, harvest_type, estimated_yield_mt_fresh,estimated_yield_mt_dired,previous_year_stock FROM `tabPlot Crops` """,as_dict=1)

@frappe.whitelist()
def get_crops_based_on_farmer():
    data = json.loads(frappe.request.data)

    frappe.log_error("GET Crops Method Executed", "GET Crops Method NOT AN ERROR")
    try:
        crops = []
        plots = frappe.db.sql(""" SELECT * FROM `tabPlot`  WHERE farmer=%s""", (data.get("erpnext_farmer_id")), as_dict=1)
        for i in plots:
            crops += get_crops_for_plot_farmer(i.name)
        return {"success": True, "message": "Fetched Crops", "data": {"plots": crops}}
    except:
        frappe.log_error(frappe.get_traceback(), "Get Crops Error")
        return {"success": False, "message": "Fetching Crops Failed"}
@frappe.whitelist()
def get_plots_based_on_farmer():
    data = json.loads(frappe.request.data)

    frappe.log_error("GET Plot Method Executed", "GET Plot Method NOT AN ERROR")
    try:
        plots = frappe.db.sql(""" SELECT 
                                     name as erpnext_plot_id,
                                      company,
                                      plot_name,
                                      farmer as erpnext_farmer_id,
                                      farmer_name,
                                      fallow_land,
                                      total_plot_area,
                                      crop_unit, latitude,
                                      longitude,
                                      perimeter_mapping_from_ma as perimeter_mapping,
                                      total_crop_list_plot_area
                                   FROM `tabPlot` WHERE farmer=%s""",(data.get("erpnext_farmer_id")), as_dict=1)
        for i in plots:
            # if i.perimeter_mapping:
            #     i.perimeter_mapping = get_final_perimeter_mapping(i.perimeter_mapping)
            i['crops'] = get_crops_for_plot(i.erpnext_plot_id)
        return { "success": True,"message": "Fetched Plots", "data": {"plots": plots}}
    except:
        frappe.log_error(frappe.get_traceback(),"Get Plots Error")
        return {"success": False, "message": "Fetching Plot Failed"}
@frappe.whitelist()
def fetch_plots_based_on_farmer(farmer_id):

    plots = frappe.db.sql(""" SELECT 
                                 name as erpnext_plot_id,
                                  company,
                                  plot_name,
                                  farmer as erpnext_farmer_id,
                                  farmer_name,
                                  fallow_land,
                                  total_plot_area,
                                  crop_unit, latitude,
                                  longitude,
                                  perimeter_mapping_from_ma as perimeter_mapping,
                                  total_crop_list_plot_area
                               FROM `tabPlot` WHERE farmer=%s""",farmer_id, as_dict=1)
    for i in plots:
        i['crops'] = get_crops_for_plot(i.erpnext_plot_id)
    return  plots
@frappe.whitelist()
def delete_crops():

    data = json.loads(frappe.request.data)
    try:
        frappe.db.sql(""" DELETE FROM `tabPlot Crops` WHERE name=%s """, data.get("plot_crop_id"),as_dict=1)
        return {"success": True, "message": "Plot Crop Deleted"}
    except:
        frappe.log_error(frappe.get_traceback(), "Delete Plot Crop Error")
        return {"success": False, "message": "Plot Crop Deletion Failed"}


@frappe.whitelist()
def update_crops():

    data = json.loads(frappe.request.data)
    try:
        frappe.db.sql(""" UPDATE `tabPlot Crops` 
                          SET crop=%s, plot_name=%s, 
                              number_of_plants=%s, plot_area=%s, 
                              mature_plant=%s, non_mature_plant=%s, 
                              start_date=%s , harvest_type=%s, estimated_yield_mt_fresh=%s,
                              estimated_yield_mt_dired=%s,previous_year_stock=%s
                          WHERE name=%s """, (data.get("crop"),data.get("plot_name"),
                                              data.get("number_of_plants"),data.get("plot_area"),
                                              data.get("mature_plant"),data.get("non_mature_plant"),
                                              data.get("starting_date"),data.get("plot_crop_id"),
                                              data.get("harvest_type"),data.get("yield_fresh"),
                                              data.get("yield_dried"),data.get("previous_stock")
                                              ),as_dict=1)
        frappe.db.commit()
        return {"success": True, "message": "Plot Crop Updated"}
    except:
        frappe.log_error(frappe.get_traceback(), "Update Plot Crop Error")
        return {"success": False, "message": "Updating Plot Crop Failed"}
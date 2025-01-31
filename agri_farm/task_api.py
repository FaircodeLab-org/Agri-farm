import frappe
@frappe.whitelist()
def get_todo():
    print("-----------------------todo-------------------------------------")
    task = frappe.form_dict.get('task')
    print(task)
    global a,b,c
    a = []
    b,c = [],[]
    all_todos = frappe.get_all('ToDo', filters ={'reference_name':task})
    for i in all_todos:
        a.append((frappe.get_doc('ToDo',i)).name)
        b.append((frappe.get_doc('ToDo',i)).reference_name)
        c.append((frappe.get_doc('ToDo',i)).status)
    print(a,b,c)
    d = {
        "name":a,
        "reference_name":b,
        "status1":c
    }
    print(d)
    frappe.response.message = d






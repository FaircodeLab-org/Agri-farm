import frappe,json
@frappe.whitelist()
def save_task(fr,date,doc,doc_name,end_date,r):

    doc=frappe.get_doc({
        "doctype":"Auto Repeat",
        "reference_doctype":doc,
        "reference_document":doc_name,
        "frequency":fr,
        "start_date":date,
        "end_date":end_date,
        "repeat_on_day":r
    })
    doc.insert()
    frappe.db.commit()

@frappe.whitelist()
def create_todo(responsible_person,task_name,status,priority,description, created_by=None,observer=None):
    count=0
    observers = json.loads(observer)
    f_observers = [i['user'] for i in observers]
    responsible_person = json.loads(responsible_person)
    assign_to = [i['user'] for i in responsible_person if not frappe.db.exists("ToDo", {'reference_name': task_name, 'allocated_to': i['user']})]
    print("ASIGN TOOO")
    print(json.dumps(assign_to))
    # data=frappe.db.sql(""" select name from `tabToDo` where reference_name=%s and allocated_to=%s and (status='Open' or status='Closed')""",(task_name,responsible_person),as_dict=1)
    # if data:

    # {
    #   'assign_to_me': '0',
    #   'assign_to': '["accounts@onlyorganic.co.in"]',
    #   'doctype': 'Task',
    #   'name': 'TASK-2022-00008',
    #   'bulk_assign': 'false',
    #   're_assign': 'false',
    #   'cmd': 'frappe.desk.form.assign_to.add'
    # }
    from frappe.desk.form.assign_to import add
    from frappe.share import add as share_add
    if len(assign_to) > 0:
        add({
            'assign_to_me': '0',
            'assign_to': json.dumps(assign_to),
            'doctype': 'Task',
            'name': task_name,
            'bulk_assign': 'false',
            're_assign': 'false',
        })
        if created_by:
            share_add("Task", task_name, created_by, write=1)
        if observer:
            for y in f_observers:
                share_add("Task", task_name, y, write=1)
        for x in assign_to:
            share_add("Task", task_name,x, write=1)

    todos = frappe.db.sql(""" SELECT * FROM `tabToDo` WHERE reference_name=%s """, task_name,as_dict=1)

    for t in todos:
        share_add("ToDo", t.name, t.allocated_to, write=1)
        # if observer:
        #     for y in f_observers:
        #         share_add("ToDo",  t.name, y)
        # for x in assign_to:
        #     share_add("ToDo",  t.name, x)
    # if frappe.db.exists("ToDo",{'reference_name':task_name,'allocated_to':responsible_person}):
    #     print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! already created')
    # else:
    #     if priority=='Urgent':
    #         priority='High'
    #     new_todo =frappe.get_doc({"doctype":"ToDo",
    #     "reference_type":'Task',
    #     "reference_name" : task_name,
    #     "allocated_to" : responsible_person,
    #     "status" : status,
    #     "priority" : priority,
    #     "description" : description,
    #     })
    #     new_todo.insert()
    #     frappe.db.commit()





#  ----------------------------------------------------------------------------------------------------------  
# @frappe.whitelist()
# def completed_validation(task_name):
#     data=frappe.db.sql(""" select name,status from `tabToDo` where reference_name=%s""",task_name,as_dict=1)
#     for i in data:
#         if i.status=='Open':
#             frappe.throw('ToDo {0} is not Completed'.format(i.name))


# @frappe.whitelist()
# def completed_val(doc,method):
#     print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
#     if doc.status =='Completed':
#         print('ffffff')
#         data=frappe.db.sql(""" select name,status from `tabToDo` where reference_name=%s""",doc.name,as_dict=1)
#         if data:
#             for i in data:
#                 if i.status=='Open':
#                     frappe.throw('ToDo {0} is not Completed'.format(i.name))
# ---------------------------------------------------------------------------------------------------------------
# def save_task(fr,date,doc,doc_name,end_date,r):
#     if fr or date: 
#         print("Taaaaaaaaaaaaaaaaaaaaaaaaadsfsdgdfhgfjhg")

#         doc=frappe.get_doc({"doctype":"Auto Repeat",
#             "reference_doctype":doc,
#             "reference_document":doc_name,
#             "frequency":fr,
#             "start_date":date,
#             "end_date":end_date,
#             "repeat_on_day":r

#         })
#         doc.insert()
#         frappe.db.commit()
@frappe.whitelist()
def fetch_company(pro_name):
    data=frappe.db.sql("""select company from `tabProject` where project_name=%s""",pro_name,as_dict=1)
    print("company")
    print(data)
    return data


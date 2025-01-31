# Copyright (c) 2023, Momscode Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe import _


 
def execute(filters=None):

	columns, data = [], []
	columns = get_columns()
	conditions = get_conditions(filters)
	lists = get_lists(filters)
	print("lists------") 
	print(lists)

	for li in lists:
		row = frappe._dict({
			'name':li.name,
			'first_name': li.first_name,
			'gender': li.gender,
			'phone_number': li.phone_number,
			'country': li.country,
			'state': li.state,
			'district': li.district,
			'society': li.society,
			'village': li.village,
			'address': li.address,
			'pin_code': li.pin_code,
			'total_farmland': li.total_farmland,
			'id_card_number': li.id_card_number,
			'id_card': li.id_card,
			'families_members': li.families_members,
			'status': li.status,
			'organically_certified': li.organically_certified,
			'season': li.season,
			'field_staff_name': li.field_staff_name,
			'bank_name': li.bank_name,
			'ac_holder_name': li.ac_holder_name,
			'bank_acc_no': li.bank_acc_no,
			'bank_ifsc': li.bank_ifsc,
			'bank_branch': li.bank_branch,
			'email_id': li.email_id,
			'date_of_birth': li.date_of_birth,
			'father_name': li.father_name,
			'member_since': li.member_since,
			'project': li.project,
			'created_by_field_staff':li.created_by_field_staff

			
		})
		data.append(row)
		if li.name:
			print(li.name)
			name = li.name
			v_list = get_v_lists(filters,li.name)


			for l in v_list:
				row = frappe._dict({
					'survey':l.survey,
					'date': l.date,
					'farm_name':l.farm_name,
					'variant': l.variant,
					'yield_qty_in_kg': l.yield_qty_in_kg,
					'questions': l.questions,
            		'remark': l.remark
				})
				data.append(row)

 

	return columns, data

def get_columns():
    return [

		 {
   			"fieldname": "name",
   			"fieldtype": "Link",
   			"label": "Farmer ID",
			"options":"Farmer",
			"width":100
			
 		},
        {
            "fieldname": "first_name",
            "fieldtype": "Data",
            "label": "Farmer Name",
            "width": 170
        },
        {
   			"fieldname": "gender",
   			"fieldtype": "Data",
   			"label": "Gender",
			# "options":"Gender",
			"width":170
			
 		},
		{
   			"fieldname": "phone_number",
   			"fieldtype": "Data",
   			"label": "Phone Number",
			"width":170
  		},
		{
   			"fieldname": "country",
   			"fieldtype": "Data",
   			"label": "Country",
			# "options":"Country",
			"width":150
  		},
		{
   			"fieldname": "state",
   			"fieldtype": "Data",
   			"label": "State",
			# "options":"State",
			"width":120 
  		},
  		{
   			"fieldname": "district",
   			"fieldtype": "Data",
   			"label": "District",
			# "options":"District",
			"width":120 
  		},
		{
   			"fieldname": "society",
   			"fieldtype": "Data",
   			"label": "Society",
			# "options":"Society",
			"width":120 
  		},
		{
   			"fieldname": "village",
   			"fieldtype": "Data",
   			"label": "Village",
			# "options":"Village",
			"width":120 
  		},
		    {
   			"fieldname": "address",
   			"fieldtype": "Small Text",
   			"label": "Address",
			"width":120 
  		},
		  {
   			"fieldname": "pin_code",
   			"fieldtype": "Data",
   			"label": "Pin Code",
			"width":120 
  		},
		  {
   			"fieldname": "total_farmland",
   			"fieldtype": "Data",
   			"label": "Total Farmland",
			"width":120 
  		},
		{
   			"fieldname": "id_card",
   			"fieldtype": "Data",
   			"label": "ID card",
			# "options":"ID Cards",
			"width":120 
  		},
		  {
   			"fieldname": "id_card_number",
   			"fieldtype": "Data",
   			"label": "ID Card Number",
			"width":170 
  		},
		  {
   			"fieldname": "families_members",
   			"fieldtype": "Int",
   			"label": "Families Members",
			"width":170 
  		},
		    {
   			"fieldname": "status",
   			"fieldtype": "Select",
   			"label": "Status",
			"options":"\nCertified",
			"width":120 
  		},
		
		  {
   			"fieldname": "organically_certified",
   			"fieldtype": "Select",
   			"label": "Organically Certified",
			"options": "Yes\nNo",
			"width":100 
  		},
		  {
   			"fieldname": "season",
   			"fieldtype": "Data",
   			"label": "Season",
			# "options":"Fiscal Year",
			"width":120 
  		},
		   {
   			"fieldname": "created_by_field_staff",
   			"fieldtype": "Link",
   			"label": "Created By",
			"options":"Employee",
			"width":170 
  		},
		  {
   			"fieldname": "bank_name",
   			"fieldtype": "Data",
   			"label": "Bank Name",
			"width":170 
  		},
		  {
   			"fieldname": "ac_holder_name",
   			"fieldtype": "Data",
   			"label": "A/C Holder Name",
			"width":170 
  		},
		  {
   			"fieldname": "bank_acc_no",
   			"fieldtype": "Data",
   			"label": "Bank Account No",
			"width":170 
  		},
		  {
   			"fieldname": "bank_ifsc",
   			"fieldtype": "Data",
   			"label": "Bank IFSC Code",
			"width":170 
  		},
		  {
   			"fieldname": "bank_branch",
   			"fieldtype": "Data",
   			"label": "Bank Branch",
			"width":170 
  		},
		  {
   			"fieldname": "email_id",
   			"fieldtype": "Data",
   			"label": "Email ID",
			"width":120 
  		},
		  {
   			"fieldname": "date_of_birth",
   			"fieldtype": "Data",
   			"label": "Date of Birth",
			"width":120 
  		},
		  {
   			"fieldname": "father_name",
   			"fieldtype": "Data",
   			"label": "Father Name",
			"width":120 
  		},
		  {
   			"fieldname": "member_since",
   			"fieldtype": "Data",
   			"label": "Member Since",
			"width":120 
  		},
		  {
   			"fieldname": "project",
   			"fieldtype": "Data",
   			"label": "Project",
			# "options":"Agri Project",
			"width":120 
  		},
		  {
			"fieldname": "survey",
			"fieldtype": "Link",
			"label": "Survey",
			"options":"Survey",
			"width":100
			
		},  
		  



		{
			"fieldname": "date",
			"fieldtype": "Date",
			"label": "Survey Date",
			"width": 100
		},
				{
			"fieldname": "farm_name",
			"fieldtype": "Data",
			"label": "Farm Name",
			"width":100
			
		},  
		
		{
			"fieldname": "variant",
			"fieldtype": "Link",
			"label": "Variant",
			"options": "Item",
			"width": 150
		},
		
		{
			"fieldname": "yield_qty_in_kg",
			"fieldtype": "Float",
			"label": "Estimated Yield Count",
			"width": 150
		},
		
			{
			"fieldname": "questions",
			"fieldtype": "Data",
			"label": "Questions",
			"width": 200
		},
			{
			"fieldname": "remark",
			"fieldtype": "Data",
			"label": "Remark",
			"width": 200
		}
	
    ]



def get_lists(filters):
	
	conditions=get_conditions(filters)

	data=[]
	parent = frappe.db.sql("""select name,first_name,state,country,phone_number,gender, district,society,village,address,pin_code,total_farmland,id_card,id_card_number,
						families_members,status,organically_certified,season,bank_name,ac_holder_name,bank_acc_no,bank_ifsc,bank_branch,
						email_id,date_of_birth,father_name,member_since,project,created_by_field_staff from `tabFarmer` where docstatus=0 {0}""".format(conditions),as_dict=1)
	print(parent)
	for dic_p in parent:
		dic_p["indent"] = 0
		filters=conditions
		data.append(dic_p)

	print("data")	
	print(data)	
	
	return data


def get_v_lists(filters,name):
	print("v list")
	print(name)
	conditions = get_survey_conditions(filters)
	data = []
	
	surveys = frappe.db.sql("""
        SELECT
            c.crop_variant as variant,
            c.yield_qty_in_kg,
            s.name as survey,
            s.date,
            s.farm_name	
        FROM
            `tabSurvey` as s
            INNER JOIN `tabSurvey Crop Qty Table` as c ON s.name = c.parent
        WHERE
            s.docstatus = 1 AND
            s.farmer_id = %s {0}
    """.format(conditions), name, as_dict=True)

	
	asurveys = frappe.db.sql("""
        SELECT
            a.animal_variant as variant,
            a.yielding_count as yield_qty_in_kg,
            s.name as survey,
            s.date,
            s.farm_name
        FROM
            `tabSurvey Animal  Husbandry Table` as a
            INNER JOIN `tabSurvey` as s ON s.name = a.parent
        WHERE
            s.docstatus = 1 AND
            s.farmer_id = %s {0}
    """.format(conditions), name, as_dict=True)

	
	for survey in surveys:
		survey["indent"] = 0
		data.append(survey)


	for a_survey in asurveys:
		a_survey["indent"] = 0
		data.append(a_survey)

	for i in data:
		riskq = frappe.db.sql(""" 
		SELECT 
			rq.questions,
			rq.remark 
		FROM
			`tabSurvey Risk Questions` as rq
			INNER JOIN `tabSurvey` as s ON rq.parent = s.name
		WHERE
			rq.idx = 3 AND
			s.docstatus = 1 AND 
			s.farmer_id = %s and
			s.name = %s
		""",(name,i.survey), as_dict=True)

		print("8888888888888888888")
		print(riskq)
		question=''
		answer =''
		if riskq:
			if riskq[0].questions:
				question = {"questions":riskq[0].questions}
			if riskq[0].remark:
				answer = {"remark":riskq[0].remark}
		i.update(question)
		i.update(answer)
	return data


	








def get_conditions(filters):
	conditions=''
	if filters.get("company"):
		conditions += "and company='{0}' ".format(filters.get("company"))
	if filters.get("farmer"):
		conditions += "and name='{0}' ".format(filters.get("farmer"))
	if filters.get("user"):
		conditions += "and user='{0}' ".format(filters.get("user"))
	if filters.get("cluster"):
		conditions += "and cluster='{0}' ".format(filters.get("cluster"))		

	return conditions


def get_survey_conditions(filters):
	conditions=''
	if filters.get("survey"):
		conditions += "and s.name='{0}' ".format(filters.get("survey"))


	return conditions















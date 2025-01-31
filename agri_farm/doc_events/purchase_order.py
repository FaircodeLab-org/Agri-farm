import frappe

@frappe.whitelist()
def get_farmer(supplier):
    fm = frappe.db.sql("""select * from `tabFarmer` where first_name = %s""", (supplier), as_dict=1)

    return fm


@frappe.whitelist()
def validate_qty(self, method):
    print("submit ok")

    if self.custom_is_farmer:
        doc = frappe.get_doc("Survey", self.custom_survey)
        
        for item in self.items:
            purchased_qty = item.qty 

            for crop in doc.crop:
                if crop.crop_variant == item.item_code:
                    print(crop.crop_variant)
                    estimated_yield = crop.yield_qty_in_kg
                    
                    if purchased_qty > crop.available_qty_kg:
                        frappe.throw("Purchased quantity exceeds the Total yield count for crop {0}".format(crop.crop_variant))
    
            for k in doc.animal_husbandry:
                if k.animal_variant == item.item_code:
                    print(k.animal_variant)
                    yielding_count = k.total_yield_count
                                    
                    if purchased_qty > k.available_qty_kg:
                        frappe.throw("Purchased quantity exceeds the Total yield count for animal {0}".format(k.animal_variant))


    else:
        pass 
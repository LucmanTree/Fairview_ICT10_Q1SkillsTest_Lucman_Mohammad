from pyscript import document, display


restaurant_name = ['Gnarly Dog Food']
owner_name = "The Man who forgot his name"
year_established = 1872
popular_item_price = 45.00
has_delivery = False
product_names = ['The Doggy Bone','The Wagging Tail','Fluffy Fur']
business_hours = "7am-8pm"
menu_prices = {'20':'The Doggy Bone','24':'The Wagging Tail','40':'The Dog Collar','36':'The Pink Water Bowl','45':'Fluffy Fur'}
common_allergens = ('Egg','Meat','Gluten')
tax_rate = 0.1

def submit_order():
    name = document.querySelector("#name").value
    address = document.querySelector("#address").value
    contact = document.querySelector("#contact").value
    items = [c.value for c in document.querySelectorAll("input.form-check-input:checked")]

    summary = f"""
    <strong>Name:</strong> {name}<br>
    <strong>Address:</strong> {address}<br>
    <strong>Contact:</strong> {contact}<br>
    <strong>Items:</strong> {", ".join(items) if items else "None"}<br>
    <strong>Note:</strong> Allergen risk – {", ".join(common_allergens)}
    """
    document.querySelector("#order-summary").innerHTML = summary


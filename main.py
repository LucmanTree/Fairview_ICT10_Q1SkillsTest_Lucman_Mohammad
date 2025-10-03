from pyscript import document, display

# Item prices
TDG = ("The Doggy Bone", 20)
TWT = ("The Wagging Tail", 24)
TDC = ("The Dog Collar", 40)
TPWB = ("The Pink Water Bowl", 36)
FF = ("Fluffy Fur", 45)

def submit_order():
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    contact = document.getElementById("contact").value

   
    items_selected = []
    total_price = 0

    for item_id, item in [("TDG", TDG), ("TWT", TWT), ("TDC", TDC), ("TPWB", TPWB), ("FF", FF)]:
        if document.getElementById(item_id).checked:
            items_selected.append(item[0])
            total_price += item[1]

    if not items_selected:
        display("Please select at least one item.", target="order-summary")
        return

    subtotal = total_price
    tax = subtotal * 0.1
    total = subtotal + tax

    message = f'''Thank you, {name}, for ordering at Gnarly Dog Food!
Take note that we can't deliver to {address}, so you must pick it up at our store.
Items ordered: {', '.join(items_selected)}
Subtotal: ₱{subtotal} + Tax: ₱{tax:.2f} = Total: ₱{total:.2f}'''

    display(message)

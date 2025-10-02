prices = { "The Doggy Bone": 20, "The Wagging Tail": 24, "The Dog Collar": 40, "The Pink Water Bowl": 36, "Fluffy Fur": 45 }
form = cgi.FieldStorage() 
name = form.getvalue("name") 
address = form.getvalue("address") 
contact = form.getvalue("contact") 
items = form.getlist("item") 
total = sum(prices[i] for i in items) 

list_fruits = ["apple", "bannnnaa"]
list_quant = ["5kg", "14pcs"]

total_list = zip(list_fruits,list_quant)
list_for_Console = list(total_list)
print(list_for_Console)

list_fruits.append("mango")
list_quant.append("10kg")
total_list = zip(list_fruits,list_quant)
list_for_Console = list(total_list)
print(list_for_Console)


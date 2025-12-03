#Faleev kirill вариант 1 
import json

print("start code")

with open("task_2\\text_1_files", 'r', encoding='utf-8') as file:
    data = json.load(file)
    
input_pk = input("введите номер квалификации: ")   

def search_in_data(data,s):
    if isinstance(data, list):
        for item in data:
            result = s(item)
            if result:
                return result
                
object = search_in_data(data,input_pk)

if object:
    print("="*10)
    print("Найдено")
    print("="*10) 
    print(f"{"code"} >> специальность {"title"},")


print("end code")

#{       "model": "data.skill",
#        "pk": 58,
#        "fields": {
#           "code": "4-02-0413-01-03",
#          "title": "Продавец (4-5 разряд)",
#         "searchtag": null,
#        "specialty": 25,
#       "desc": null
#  }
#    },
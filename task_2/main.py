#Faleev kirill вариант 1 
import json

print("start code")

with open("doc.json", 'r', encoding='utf-8') as file:
    data = json.load(file)
    
input_pk = int(input("введите номер квалификации(1 - 733): "))   
if input_pk < 734 and input_pk > 0:
    for object1 in data:
        if object1["pk"] == input_pk and object1["model"] == "data.skill":
            obj_1 = object1["fields"]["title"]
            obj_2 = object1["fields"]["code"]
            obj_3 = object1["fields"]["specialty"]
            break
        if object1["pk"] == input_pk and object1["model"] == "data.specialty":
            spec = object1["fields"]["title"]
            spec_code = object1["fields"]["code"]
            c_type = object1["fields"]["c_type"]

 
    print(" Найдено ".center(50, "="))
    print(f"{obj_2} >> Специальность \"{spec}\", {c_type}" )
    print(f"{spec_code} >> Квалификация \"{obj_1}\"")
else:
    print(" Не найдено ".center(50, "="))
    file.close()


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
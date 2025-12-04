#Faleev kirill вариант 1 

import json

print("start code")

filename = r"task_3(2)\fishes.json"
while True:
    
    print("""
-1.вывести все записи
-2.вывести все записи по полю
-3.добавить запись 
-4.удалить записи по полю
-5.выйти из программы  
""")

    user_number = int(input("введите число от 1-5: "))



    with open(filename,'r',encoding='UTF-8') as file:
        database=json.load(file)
    #первая функция меню
    if user_number == 1:
     print("все записи: ")
     for record in database:
                print(f"\n{'━'*40}")
                print(f"ID: {record['id']}")
                print(f"Название: {record['name']}")
                print(f"Латинское название: {record['latin_name']}") 
                water_type = "морская" if record['is_salt_water_fish'] else "пресноводная"
                print(f"Тип: {water_type}")
                print(f"Количество подвидов: {record['sub_type_count']}")
                print(f"{'━'*40}")
    elif user_number == 2:
       print("вывести по полю: ")
       input_id = int(input("введите номер ID: "))
       for i, record in enumerate(database):
            if record['id'] == input_id:
                position = i
                found = True
                print(f"\n✅ Найдена рыба с ID {input_id}:")
                print(f"   Позиция в базе: {position + 1}")
                print(f"   Название: {record['name']}")
                print(f"   Латинское название: {record['latin_name']}")
                water_type = "морская" if record['is_salt_water_fish'] else "пресноводная"
                print(f"   Тип: {water_type}")
                print(f"   Количество подвидов: {record['sub_type_count']}")
                break
       input("введите Enter для выхода в меню")

    elif user_number == 3:
      print("добавить запись: ")
      name = input("введите название рыбы: ")
      latin_name = input("введите латинское название рыбы: ")
      print("введите 1 если рыба морская: ")
      print("введите 2 если рыба пресноводная: ")
      water = int(input())
      if water == 1:
        is_salt_water_fish = True
      elif water == 2:
            is_salt_water_fish = False
      input("введите кол-во видов: ") 
      sub_type_count = int(input())
      print("придумайте ID: ")
      id = int(input())

      new_record = {
            "id": id,
            "name": name,
            "latin_name": latin_name,
            "is_salt_water_fish": is_salt_water_fish,
            "sub_type_count": sub_type_count
        }
#добавляем в базу
      database.append(new_record)
    elif user_number == 4:
      id = int(input("введите ID для удаления: "))
      for record in file:
            if record["id"] == id:
                  print(f"{record}эта запись была удалена")
                  database.delate(record)
                  json.dump(database,file,ensure_ascii=False,indent=4)
                  file.close()
    elif user_number == 5:
          
        break




        
          




print("end code")

#Faleev kirill вариант 1 

import json

print("start code")

filename = r"task_3\fishes.json"

def display_menu():
  print("""
  -1.вывести все записи
  -2.вывести все записи по полю
  -3.добавить запись 
  -4.удалить записи по полю
  -5.выйти из программы  
  """)






def load_database():
  with open(filename,'r',encoding='UTF-8') as file:
    return json.load(file)
  

def dump_position(database):  
  with open(filename,'r',encoding='UTF-8') as file:
   json.dump(database,file,ensure_ascii=False,indent=4)

  #первая функция меню
def position_1(database):
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

  #вторая функция меню   
def position_2(database):
  print("вывести по полю: ")
  input_id = int(input("введите номер ID: "))
  for i, record in enumerate(database):
    if record['id'] == input_id:
      position = i
      found = True
      print(f"\n Найдена рыба с ID {input_id}:")
      print(f"   Позиция в базе: {position + 1}")
      print(f"   Название: {record['name']}")
      print(f"   Латинское название: {record['latin_name']}")
      water_type = "морская" if record['is_salt_water_fish'] else "пресноводная"
      print(f"   Тип: {water_type}")
      print(f"   Количество подвидов: {record['sub_type_count']}")
      break
  input("введите Enter для выхода в меню")


#третья функция меню
def position_3(database):
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
  dump_position(database)
  print("введите enter для выхода в меню...1")

#четвертая функция меню  
def position_4(database):
  delete_id = int(input("введите ID для удаления: "))
  for i,record in enumerate(database):
    if record["id"] == delete_id:
      delete_index = i
      deleted_record = database.pop(delete_index)
      print(f"{record}эта запись была удалена")
      dump_position(database)

  
        
          
def main():
  while True:
    display_menu()

    try:
      user_number = int(input("введите число от 1-5: "))
      
      if user_number not in [1,2,3,4,5]:
        print("введите число от 1 до 5: ")
        continue

      database = load_database()


      if user_number == 1:
        position_1(database)

      elif user_number == 2:
        position_2(database)

      elif user_number == 3:
        position_3(database)

      elif user_number == 4:
        position_4(database)

      elif user_number == 5:
        print("выход из базы данных...")
        break








    except ValueError:
      print("Пожалуйста, введите число от 1 до 5")

if __name__ == "__main__":
  main()




print("end code")

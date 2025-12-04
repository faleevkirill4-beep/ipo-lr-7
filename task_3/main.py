#Faleev kirill вариант 1 
import json
import os
print("start code")


# Настройки
FILENAME = "fishes_database.json"

# Счетчик операций
operations_count = 0

# Инициализация базы данных с 5 записями
initial_data = [
    {
        "id": 1,
        "name": "Щука обыкновенная",
        "latin_name": "Esox lucius",
        "is_salt_water_fish": False,
        "sub_type_count": 5
    },
    {
        "id": 2,
        "name": "Сёмга",
        "latin_name": "Salmo salar",
        "is_salt_water_fish": True,
        "sub_type_count": 3
    },
    {
        "id": 3,
        "name": "Карп",
        "latin_name": "Cyprinus carpio",
        "is_salt_water_fish": False,
        "sub_type_count": 12
    },
    {
        "id": 4,
        "name": "Тунец синий",
        "latin_name": "Thunnus thynnus",
        "is_salt_water_fish": True,
        "sub_type_count": 8
    },
    {
        "id": 5,
        "name": "Окунь речной",
        "latin_name": "Perca fluviatilis",
        "is_salt_water_fish": False,
        "sub_type_count": 6
    }
]

# Проверяем существует ли файл, если нет - создаем с начальными данными
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(initial_data, file, ensure_ascii=False, indent=2)
    print(f"📁 Создан новый файл базы данных: {FILENAME}")
    print(f"✅ Добавлено {len(initial_data)} начальных записей")
    operations_count += 1  # Операция создания файла
else:
    print(f"📁 Загружена существующая база данных: {FILENAME}")

# Загрузка данных
with open(FILENAME, "r", encoding="utf-8") as file:
    database = json.load(file)

print(f"📊 Загружено записей: {len(database)}")

# Основной цикл программы
while True:
    print("\n" + "="*60)
    print("           БАЗА ДАННЫХ 'МОРСКИЕ И РЕЧНЫЕ РЫБЫ'")
    print("="*60)
    print("1. 🐟 Вывести все записи о рыбах")
    print("2. 🔍 Найти рыбу по ID")
    print("3. ➕ Добавить новую рыбу")
    print("4. ❌ Удалить рыбу по ID")
    print("5. 🚪 Выйти из программы")
    print("="*60)
    
    choice = input("\nВыберите действие (1-5): ").strip()
    
    # 1. Вывести все записи
    if choice == "1":
        print("\n" + "="*60)
        print("СПИСОК ВСЕХ РЫБ В БАЗЕ ДАННЫХ:")
        print("="*60)
        
        if not database:
            print("\nБаза данных пуста.")
        else:
            for record in database:
                print(f"\n{'━'*40}")
                print(f"ID: {record['id']}")
                print(f"Название: {record['name']}")
                print(f"Латинское название: {record['latin_name']}")
                water_type = "морская" if record['is_salt_water_fish'] else "пресноводная"
                print(f"Тип: {water_type}")
                print(f"Количество подвидов: {record['sub_type_count']}")
                print(f"{'━'*40}")
        
        operations_count += 1
        input("\nНажмите Enter для возврата в меню...")
    
    # 2. Найти рыбу по ID
    elif choice == "2":
        print("\n" + "="*60)
        print("ПОИСК РЫБЫ ПО ID")
        print("="*60)
        
        try:
            search_id = int(input("Введите ID рыбы для поиска: "))
        except ValueError:
            print("\n❌ Ошибка! ID должен быть числом.")
            input("\nНажмите Enter для возврата в меню...")
            continue
        
        found = False
        position = -1
        
        for i, record in enumerate(database):
            if record['id'] == search_id:
                position = i
                found = True
                print(f"\n✅ Найдена рыба с ID {search_id}:")
                print(f"   Позиция в базе: {position + 1}")
                print(f"   Название: {record['name']}")
                print(f"   Латинское название: {record['latin_name']}")
                water_type = "морская" if record['is_salt_water_fish'] else "пресноводная"
                print(f"   Тип: {water_type}")
                print(f"   Количество подвидов: {record['sub_type_count']}")
                break
        
        if not found:
            print(f"\n⚠️  Предупреждение: Рыба с ID {search_id} не найдена!")
        
        operations_count += 1
        input("\nНажмите Enter для возврата в меню...")
    
    # 3. Добавить новую рыбу
    elif choice == "3":
        print("\n" + "="*60)
        print("ДОБАВЛЕНИЕ НОВОЙ РЫБЫ")
        print("="*60)
        
        # Находим максимальный ID для генерации нового
        max_id = 0
        for record in database:
            if record['id'] > max_id:
                max_id = record['id']
        new_id = max_id + 1
        
        print(f"Будет присвоен ID: {new_id}")
        
        # Ввод данных
        name = input("Введите общее название рыбы: ").strip()
        while not name:
            print("❌ Название не может быть пустым!")
            name = input("Введите общее название рыбы: ").strip()
        
        latin_name = input("Введите латинское название рыбы: ").strip()
        while not latin_name:
            print("❌ Латинское название не может быть пустым!")
            latin_name = input("Введите латинское название рыбы: ").strip()
        
        # Ввод типа воды
        while True:
            water_input = input("Это морская рыба? (да/нет): ").strip().lower()
            if water_input == 'да':
                is_salt_water_fish = True
                break
            elif water_input == 'нет':
                is_salt_water_fish = False
                break
            else:
                print("❌ Пожалуйста, введите 'да' или 'нет'")
        
        # Ввод количества подвидов
        while True:
            try:
                sub_type_count = int(input("Введите количество подвидов: "))
                if sub_type_count < 0:
                    print("❌ Количество не может быть отрицательным!")
                    continue
                break
            except ValueError:
                print("❌ Пожалуйста, введите число!")
        
        # Создание новой записи
        new_record = {
            "id": new_id,
            "name": name,
            "latin_name": latin_name,
            "is_salt_water_fish": is_salt_water_fish,
            "sub_type_count": sub_type_count
        }
        
        # Добавление в базу
        database.append(new_record)
        
        # Сохранение в файл
        with open(FILENAME, "w", encoding="utf-8") as file:
            json.dump(database, file, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Рыба '{name}' успешно добавлена с ID {new_id}")
        
        operations_count += 1
        input("\nНажмите Enter для возврата в меню...")
    
    # 4. Удалить рыбу по ID
    elif choice == "4":
        print("\n" + "="*60)
        print("УДАЛЕНИЕ РЫБЫ")
        print("="*60)
        
        try:
            delete_id = int(input("Введите ID рыбы для удаления: "))
        except ValueError:
            print("\n❌ Ошибка! ID должен быть числом.")
            input("\nНажмите Enter для возврата в меню...")
            continue
        
        found = False
        delete_index = -1
        fish_name = ""
        
        # Поиск рыбы
        for i, record in enumerate(database):
            if record['id'] == delete_id:
                delete_index = i
                fish_name = record['name']
                found = True
                break
        
        if not found:
            print(f"\n⚠️  Предупреждение: Рыба с ID {delete_id} не найдена!")
            input("\nНажмите Enter для возврата в меню...")
            continue
        
        # Подтверждение удаления
        print(f"\nНайдена рыба для удаления:")
        print(f"ID: {delete_id}")
        print(f"Название: {fish_name}")
        
        confirm = input(f"\nВы уверены, что хотите удалить эту рыбу? (да/нет): ").strip().lower()
        
        if confirm == 'да':
            # Удаление из базы
            deleted_record = database.pop(delete_index)
            
            # Сохранение в файл
            with open(FILENAME, "w", encoding="utf-8") as file:
                json.dump(database, file, ensure_ascii=False, indent=2)
            
            print(f"\n✅ Рыба '{fish_name}' (ID: {delete_id}) успешно удалена")
            operations_count += 1
        else:
            print("\n❌ Удаление отменено")
        
        input("\nНажмите Enter для возврата в меню...")
    
    # 5. Выйти из программы
    elif choice == "5":
        print("\n" + "="*60)
        print("ЗАВЕРШЕНИЕ РАБОТЫ ПРОГРАММЫ")
        print("="*60)
        print(f"📊 СТАТИСТИКА ВЫПОЛНЕННЫХ ОПЕРАЦИЙ:")
        print(f"   Всего операций с записями: {operations_count}")
        print(f"   Всего записей в базе: {len(database)}")
        print(f"   Файл базы данных: {FILENAME}")
        
        # Показываем текущие записи перед выходом
        if database:
            print(f"\nТекущие записи в базе:")
            for record in database:
                water_type = "морская" if record['is_salt_water_fish'] else "пресноводная"
                print(f"  ID {record['id']}: {record['name']} ({water_type})")
        
        print("\n👋 До свидания!")
        print("="*60)
        break
    
    # Неверный выбор
    else:
        print("\n❌ Неверный выбор! Пожалуйста, введите число от 1 до 5.")
        input("Нажмите Enter для продолжения...")

# Финальная информация о состоянии базы
print(f"\n📁 Файл {FILENAME} сохранен с {len(database)} записями")
if os.path.exists(FILENAME):
    print(f"📏 Размер файла: {os.path.getsize(FILENAME)} байт")

    
print("end code")
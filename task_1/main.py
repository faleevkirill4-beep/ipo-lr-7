#Faleev kirill вариант 1 
print("start code")

books = [  
{"title": "Война и мир","autor": "Лев Толстой ","year": 1869},
{"title": "Улисс","autor": "Джеймс Джойс","year": 1922},
{"title": "Сто лет одиночества","autor": "Габриэль Гарсиа Маркес","year": 1967},
{"title": "Над пропастью во ржи","autor": "Джером Д. Сэлинджер","year": 1951},
{"title": "Анна Каренина","autor": "Лев Толстой","year": 1877}]

for i,book in enumerate(books,1):
    print(f"------------- Книга {i} -------------")
    print(f"Название: {book["title"]} , Автор: {book["autor"]} ,")
    print(f"---------{book["year"]} ---------")






print("end code")
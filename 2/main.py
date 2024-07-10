from pymongo import MongoClient
from bson.objectid import ObjectId

# Підключення до хмарни MongoDB
# для поступу ввести свій user та password
uri = "mongodb+srv://user:pass@cluster0.wkl8bnj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client['test']
collection = db['cats']

# Функція для виведення всіх записів із колекції
def read_all_cats():
    try:
        print("\nAll cats:")
        cats = collection.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        print(f"An error occurred: {e}")

# Функція для виведення інформації про кота за ім'ям
def read_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"No cat found with name: {name}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Функція для оновлення віку кота за ім'ям
def update_cat_age(name, age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": age}})
        if result.matched_count > 0:
            print(f"Cat's age updated to {age} for {name}")
        else:
            print(f"No cat found with name: {name}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Функція для додавання нової характеристики до списку features кота за ім'ям
def add_cat_feature(name, feature):
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": feature}})
        if result.matched_count > 0:
            print(f"Feature '{feature}' added to {name}")
        else:
            print(f"No cat found with name: {name}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Функція для видалення запису з колекції за ім'ям
def delete_cat_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Cat with name {name} deleted")
        else:
            print(f"No cat found with name: {name}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Функція для видалення всіх записів із колекції
def delete_all_cats():
    try:
        result = collection.delete_many({})
        print(f"All cats deleted, count: {result.deleted_count}")
    except Exception as e:
        print(f"An error occurred: {e}")



# Приклади використання функцій
if __name__ == "__main__":
    # Додавання тестових даних
    try:
        collection.insert_many([
            {
                "name": "barsik",
                "age": 3,
                "features": ["ходить в капці", "дає себе гладити", "рудий"]
            },
            {
                "name": 'Lama',
                "age": 2,
                "features": ['ходить в лоток', 'не дає себе гладити', 'сірий'],
            },
            {
                "name": 'Liza',
                "age": 4,
                "features": ['ходить в лоток', 'дає себе гладити', 'білий'],
            },
            {
                "name": 'Boris',
                "age": 12,
                "features": ['ходить в лоток', 'не дає себе гладити', 'сірий'],
            },
            {
                "name": 'Murzik',
                "age": 1,
                "features": ['ходить в лоток', 'дає себе гладити', 'чорний'],
            },
        ])
        print("Test data inserted successfully.")
    except Exception as e:
        print(f"An error occurred while inserting test data: {e}")

    # Читання всіх котів
    # read_all_cats()

    # Читання кота за ім'ям, наприклад 'barsik'
    # print("\nCat named 'barsik':")
    # read_cat_by_name("barsik")

    # Оновлення віку кота за ім'ям
    # update_cat_age("barsik", 4)

    # Додавання нової характеристики
    # add_cat_feature("barsik", "любитиме гратися")

    # Видалення кота за ім'ям
    # delete_cat_by_name("barsik")

    # Видалення всіх котів
    # delete_all_cats()

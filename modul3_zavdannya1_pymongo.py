from pymongo import MongoClient
from bson.objectid import ObjectId

# Підключення до MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['cats_database']
collection = db['cats_collection']


def create_cat(name, age, features):
    # Створення документа
    cat = {"name": name, "age": age, "features": features}
    # Вставка документа в колекцію
    collection.insert_one(cat)
    print("Cat created successfully!")


def read_all_cats():
    # Виведення всіх записів із колекції
    cats = collection.find()
    for cat in cats:
        print(cat)


def read_cat_by_name(name):
    # Знайти та вивести інформацію про кота за ім'ям
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print("Cat not found!")


def update_cat_age_by_name(name, new_age):
    # Оновлення віку кота за ім'ям
    collection.update_one({"name": name}, {"$set": {"age": new_age}})
    print("Cat age updated successfully!")


def add_feature_to_cat(name, new_feature):
    # Додавання нової характеристики до списку features кота за ім'ям
    collection.update_one({"name": name}, {"$push": {"features": new_feature}})
    print("Feature added to cat successfully!")


def delete_cat_by_name(name):
    # Видалення запису з колекції за ім'ям тварини
    collection.delete_one({"name": name})
    print("Cat deleted successfully!")


def delete_all_cats():
    # Видалення всіх записів із колекції
    collection.delete_many({})
    print("All cats deleted successfully!")


# Приклад використання функцій
create_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
read_all_cats()
read_cat_by_name("barsik")
update_cat_age_by_name("barsik", 4)
add_feature_to_cat("barsik", "любить спати на подушці")
delete_cat_by_name("barsik")
delete_all_cats()

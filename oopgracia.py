'''
Assignment: Create 10 classes with 5 corresponding objects.
Print out atleast one piece of information for each object.
Submission: oopgracia.py on github before midnight today.
'''
# A class of laptops.
class Laptop:
    brand = "Apple"
    color = "black"
    screen_size = "11 inches"
print(Laptop.brand)

laptop2 = Laptop()
laptop2.brand = "Dell"
laptop2.color = "white"
laptop2.screen_size = "12 inches"
print(f"This laptop is {laptop2.color}.")

laptop3 = Laptop()
laptop3.brand = "Lenovo"
laptop3.color = "red"
laptop3.screen_size = "13 inches"
print(laptop3.screen_size)

laptop4 = Laptop()
laptop4.brand = "HP"
laptop4.color = "blue"
laptop4.screen_size = "14 inches"
print(f"My laptop is an {laptop4.brand}.")

laptop5 = Laptop()
laptop5.brand = "Microsoft"
laptop5.color = "grey"
laptop5.screen_size = "15 inches"
print(laptop5.color)


# A class of pieces of furniture.
class Furniture:
    type = "shelf"
    material = "wooden"
    color = "brown"
print(f"I love my {Furniture.type}.")

furniture2 = Furniture()
furniture2.type = "chair"
furniture2.material = "metallic"
furniture2.color = "green"
print(furniture2.material)

furniture3 = Furniture()
furniture3.type = "stool"
furniture3.material = "plastic"
furniture3.color = "black"
print(f"Its color is {furniture3.color}.")

furniture4 = Furniture()
furniture4.type = "table"
furniture4.material = "glass"
furniture4.color = "transparent"
print(furniture4.type)

furniture5 = Furniture()
furniture5.type = "bed"
furniture5.material = "wooden"
furniture5.color = "grey"
print(f"This bed is {furniture5.material}.")

# A class of clothes.
class Cloth():
    category = "blouse"
    material = "cotton"
    color = "red"
print(Cloth.category)

cloth2 = Cloth()
cloth2.category = "trouser"
cloth2.material = "leather"
cloth2.color = "black"
print(f"This {cloth2.material} is uncomfortable.")

cloth3 = Cloth()
cloth3.category = "jacket"
cloth3.material = "velvet"
cloth3.color = "blue"
print(cloth3.color)

cloth4 = Cloth()
cloth4.category = "skirt"
cloth4.material = "chiffon"
cloth4.color = "purple"
print(f"This {cloth4.category} is nice.")

cloth5 = Cloth()
cloth5.category = "scarf"
cloth5.material = "flannel"
cloth5.color = "yellow"
print(cloth5.material)

# A class of foods.
class Food():
    name = "rice"
    nutrient = "carbohydrates"
    color = "white"
print(f"I love {Food.name}.")

food2 = Food()
food2.name = "meat"
food2.nutrient = "proteins"
food2.color = "brown"
print(food2.nutrient)

food3 = Food()
food3.name = "avocado"
food3.nutrient = "fats"
food3.color = "yellow/green"
print(f"The {food3.color} color is a good sign.")

food4 = Food()
food4.name = "chia"
food4.nutrient = "fibre"
food4.color = "black"
print(food4.name)

food5 = Food()
food5.name = "carrot"
food5.nutrient = "vitamins"
food5.color = "orange"
print(f"They are rich in {food5.nutrient}.")

# A class of tv series.
class Serie():
    name = "Suits"
    seasons = 9
    genre = "legal drama"
print(Serie.name)

serie2 = Serie()
serie2.name = "The Office"
serie2.seasons = 9
serie2.genre = "mockumentary"
print(f"I watched all {serie2.seasons} seasons.")

serie3 = Serie()
serie3.name = "Modern Family"
serie3.seasons = 11
serie3.genre = "sitcom"
print(serie3.genre)

serie4 = Serie()
serie4.name = "The Originals"
serie4.seasons = 5
serie4.genre = "supernatural"
print(f"I finished {serie4.name}.")

serie5 = Serie()
serie5.name = "Rosewood"
serie5.seasons = 2
serie5.genre = "police procedural"
print(serie5.seasons)

# A class of speaking languages.
class Language():
    name = "English"
    writing = "Latin script"
    family = "Indo-European"
print(f"I speak {Language.name}.")

language2 = Language()
language2.name = "Spanish"
language2.writing = "Latin script"
language2.family = "Indo-European"
print(language2.writing)

language3 = Language()
language3.name = "Arabic"
language3.writing = "Arabic alphabet"
language3.family = "Afro-Asiatic"
print(f"I want to learn {language3.family} languages.")

language4 = Language()
language4.name = "Russian"
language4.writing = "Cyrillic script"
language4.family = "Indo-European"
print(language4.name)

language5 = Language()
language5.name = "Mandarin"
language5.writing = "Chinese characters"
language5.family = "Sino-Tibetan"
print(f"We use {language5.writing} in this language.")

# A class of continents.
class Continent():
    name = "Africa"
    denonym = "African"
    religion = "Christianity"
print(Continent.name)

continent2 = Continent()
continent2.name = "Asia"
continent2.denonym = "Asian"
continent2.religion = "Hinduism"
print(f"I met an {continent2.denonym}.")

continent3 = Continent()
continent3.name = "Europe"
continent3.denonym = "European"
continent3.religion = "Christianity"
print(continent3.religion)

continent4 = Continent()
continent4.name = "Australia"
continent4.denonym = "Australian"
continent4.religion = "Christianity"
print(f"They went to {continent4.name}.")

continent5 = Continent()
continent5.name = "South America"
continent5.denonym = "South American"
continent5.religion = "Christianity"
print(continent5.denonym)

# A class of animals.
class Animal():
    name = "lion"
    bclass = "mammalia"
    order = "canivora"
print(f"The {Animal.name} is the king of jungle.")

animal2 = Animal()
animal2.name = "elephant"
animal2.bclass = "mammalia"
animal2.order = "proboscidea"
print(animal2.bclass)

animal3 = Animal()
animal3.name = "snake"
animal3.bclass = "reptilia"
animal3.order = "squamata"
print(f"Its order is {animal3.order}.")

animal4 = Animal()
animal4.name = "frog"
animal4.bclass = "amphibia"
animal4.order = "anura"
print(animal4.name)

animal5 = Animal()
animal5.name = "deer"
animal5.bclass = "mammalia"
animal5.order = "Artiodactyla"
print(f"A deer belongs to {animal5.bclass}.")

# A class of movies.
class Movie():
    name = "Mission Impossible"
    parts = 6
    first = 1996
print(Movie.name)

movie2 = Movie()
movie2.name = "Fast & Furious"
movie2.parts = 10
movie2.first = 2001
print(f"I think it has {movie2.parts} films.")

movie3 = Movie()
movie3.name = "Pirates of the Carribean"
movie3.parts = 5
movie3.first = 2003
print(movie3.first)

movie4 = Movie()
movie4.name = "Jurassic Park"
movie4.parts = 6
movie4.first = 1993
print(f"{movie4.name} is fun.")

movie5 = Movie()
movie5.name = "Harry Potter"
movie5.parts = 8
movie5.first = 2001
print(movie5.parts)

# A class of musicians.
class Musician():
    name = "Adele"
    genre = "pop & soul"
    label = "XL"
print(f"{Musician.name} has a great voice.")

musician2 = Musician()
musician2.name = "Kelly Clarkson"
musician2.genre = "pop & pop rock"
musician2.label = "RCA"
print(musician2.genre)

musician3 = Musician()
musician3.name = "Tori Kelly"
musician3.genre = "R&B, pop, soul & gospel"
musician3.label = "Epic"
print(f"{musician3.label} is her label.")

musician4 = Musician()
musician4.name = "Alessia Cara"
musician4.genre = "pop & R&B"
musician4.label = "EP"
print(musician4.name)

musician5 = Musician()
musician5.name = "Lorde"
musician5.genre = "pop"
musician5.label = "UMG"
print(f"Her music is a variety of {musician5.genre}.")
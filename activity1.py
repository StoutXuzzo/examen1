import foodapi

cookbook = {}

def addRecipe(cookbook, recipe, ingredients):
    cookbook[recipe] = ingredients
    return len(cookbook)

def getIngredients(cookbook, recipe):
    if recipe in cookbook:
        return cookbook[recipe]
    else:
        return None

def findRecipe(cookbook, ingredient):
    #recipies = []
    #for elem in cookbook.keys():
    #    for ing in cookbook[elem]:
    #        if ing.upper() == ingredient.upper():
    #            recipies.append(elem)
    #            break
    #return recipies

    recipes = []
    for elem in cookbook.keys():
        for ing in cookbook[elem]:
            if str(ing).upper().count(ingredient.upper()):
                recipes.append(elem)
                break
    return recipes

def listRecipes(cookbook):
    text = ""
    for elem in cookbook.keys():
        text += elem + "\n"
        for ing in cookbook[elem]:
            text += "   " + ing + "\n"
    return text

def importJson(num):
    return foodapi.getRecipe(num)

while True:
    print("Recipe Cookbook")
    print("There are currently", len(cookbook), "recipes")
    print("1.- Add recipe\n2.- Get ingredients\n3.- Search recipes by ingredient\n4.- List cookbook\n5.- Import JSON recipe\n6.- Exit")
    user = input("Select option: ")
    print("")

    if user == "1":

        recipe = input("Enter recipe name:")
        ingredients = []
        while True:
            ingredient = input("Enter ingredient (END to finish):")
            if ingredient == "END":
                break
            ingredients.append(input)
        addRecipe(cookbook, recipe, ingredients)
        print("")

    elif user == "2":

        recipe = input("Enter recipe name:")
        print("Ingredients needed: ")
        tempList = getIngredients(cookbook, recipe)
        if tempList != None:
            for elem in getIngredients(cookbook, recipe):
               print("  " ,elem)
        else:
            print("The recipe dosn't exist")
        print("")

    elif user == "3":

        ingredient = input("Enter ingredient:")
        tempList = findRecipe(cookbook, ingredient)
        if len(tempList) > 0:
            for elem in tempList:
                print(elem)
        else:
            print("There is no recipe with that ingredient.")
        print("")

    elif user == "4":

        print(listRecipes(cookbook))
        print("")

    elif user == "5":

        num = int(input("Enter the recipe number: "))
        temp = importJson(num)

        recipe = temp["name"]
        ingredients = []

        for elem in temp["sections"][0]["components"]:
            ingredients.append(elem["raw_text"])
        addRecipe(cookbook, recipe, ingredients)


    elif user == "0":

        print("That's all folks!")
        break

    else:

        print("You have to enter one of the existent options.")
        print("")


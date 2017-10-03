""" Contains the various object models used by the recipe app """


class User:
    """ Describes the user model """

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.recipe_categories = {}

    def add_recipe_category(self, recipe_category_title):
        """ Adds a new recipe category to the user's recipe categorie """
        if recipe_category_title:
            if not recipe_category_title in self.recipe_categories:
                self.recipe_categories[recipe_category_title] = Recipe_category(
                    recipe_category_title)
                return "recipe category added"
            return "A recipe category with this name already exists"
        return "None input"

    def edit_recipe_category(self, title, new_title):
        """ Adds a new recipe_category to the user's recipe category """
        if title and new_title:
            if not title == new_title:
                if title in self.recipe_categories:
                    if not new_title in self.recipe_categories:
                        self.recipe_categories[new_title] = self.recipe_categories.pop(
                            title)
                        return "recipe category updated"
                    return "No change, new name already in recipe categories"
                return "recipe category not found "
            return "No change, same name"
        return "None input"

    def delete_recipe_category(self, recipe_category_title):
        """ Deletes a recipe_category whose name is provided from a user's category """
        if recipe_category_title:
            if recipe_category_title in self.recipe_categories:
                self.recipe_categories.pop(recipe_category_title)
                return "recipe category deleted"
            return "recipe category not found"
        return "None input"


class Recipe_category:
    """ Describes the recipe_category model """

    def __init__(self, title):
        self.title = title
        self.recipes = {}

    def add_recipe(self, description):
        """ Adds an recipe to a recipe_category """
        if description:
            if not description in self.recipes:
                self.recipes[description] = Recipe(description)
                return "recipe added"
            return "recipe already exists"
        return "None input"

    def edit_description(self, description, new_description):
        """ Updates a recipe's description in a recipe_category """
        if description and new_description:
            if not new_description == description:
                if not new_description in self.recipes:
                    if description in self.recipes:
                        self.recipes[new_description] = self.recipes.pop(
                            description)
                        return "recipe updated"
                    return "recipe not found"
                return "New description already in recipe_category"
            return "No changes"
        return "None input"

    def update_status(self, description, status):
        """ Updates an recipe's status in a recipe_category """
        if description and status:
            if description in self.recipes:
                if status == "private" or status == "public":
                    if not self.recipes[description].status == status:
                        self.recipes[description].status = status
                        return "recipe updated"
                    return "No changes"
                return "Invalid status"
            return "recipe not found"
        return "None input"

    def delete_recipe(self, description):
        """ Deletes an recipe from a recipe_category """
        if description:
            if description in self.recipes:
                self.recipes.pop(description)
                return "recipe deleted"
            return "recipe not found"
        return "None input"

    def get_recipes_count(self):
        """ Counts recipes in a recipe_category """
        return len(self.recipes)


class Recipe:
    """ Describes the recipe model """

    def __init__(self, description, title =None):
        self.description = description
        self.title= title

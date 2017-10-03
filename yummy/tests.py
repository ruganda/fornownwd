import unittest
from models import User, Recipe_category, Recipe
from app import register, login, USERS


class TestappMethods(unittest.TestCase):
    """ This class tests methods of the app module """

    def setUp(self):
        self.name = "ruganda mubarak"
        self.correct_username = "ruganda"
        self.short_username = "mub"
        self.long_username = "rugandamubarak"
        self.correct_password = "password"
        self.short_pass = "pass"
        self.long_pass = "passwordpassword"

    def test_setup_name(self):
        self.assertEqual(self.name, "ruganda mubarak")

    def test_setup_username(self):
        self.assertEqual(self.correct_username, "ruganda")

    def test_setup_short_username(self):
        self.assertEqual(self.short_username, "mub")

    def test_setup_long_username(self):
        self.assertEqual(self.long_username, "rugandamubarak")

    def test_setup_correct_password(self):
        self.assertEqual(self.correct_password, "password")

    def test_setup_shortpass(self):
        self.assertEqual(self.short_pass, "pass")

    def test_setup_longpass(self):
        self.assertEqual(self.long_pass, "passwordpassword")
    """ Tests the register method of the views class against various inputs """

    def test_register_None(self):

        self.assertEqual(register(None, None, None, None), "None input")

    def test_register_blank_input(self):
        self.assertEqual(register("  ", " ", "  ", " "), 'Username should be 4 to 10 characters')

    def test_register_short_username(self):
        self.assertEqual(register(self.name, self.short_username,
                                  self.correct_password, self.correct_password),
                         "Username should be 4 to 10 characters")

    def test_register_correctpass(self):
        self.assertEqual(register(self.name, self.long_username, self.correct_password,
                                  self.correct_password),
                         "Username should be 4 to 10 characters")

    def test_register_short_pass(self):
        self.assertEqual(register(self.name, self.correct_username, self.short_pass,
                                  self.short_pass),
                         "Registration successful")

    def test_registerpassword_range(self):
        self.assertEqual(register(self.name, self.correct_username, self.long_pass,
                                  self.long_pass),
                         "Password should be 2 to 10 characters")

    def test_register_passwords_dont_match(self):
        self.assertEqual(register(self.name, self.correct_username, self.correct_password,
                                  self.long_pass),
                         "Passwords don't match")

    def test_register_RegistrationSucessful(self):
        self.assertEqual(register(self.name, self.correct_username, self.correct_password,
                                  self.correct_password),
                         "Registration successful")


class UserTest(unittest.TestCase):
    """ self set up """

    def setUp(self):
        self.user = User("ruganda", "mubaruganda@gmail.com", "password")

    def test_created_user(self):
        self.assertIsInstance(self.user, User, 'User not created')

    def test_add_recipe_category_category_added(self):
        self.assertEqual(self.user.add_recipe_category("dinner"),
                         "recipe category added")

    def test_add_recipe_category_name_already_exists(self):
        self.user.add_recipe_category("dinner")
        self.assertEqual(self.user.add_recipe_category
                         ("dinner"),
                         "A recipe category with this name already exists")

    def test_edit_recipe_category_not_found(self):
        self.assertEqual(self.user.edit_recipe_category("absent", "newtype"),
                         "recipe category not found ")

    def test_edit_recipe_category_successful(self):
        self.user.add_recipe_category("Snacks")
        self.assertEqual(self.user.edit_recipe_category(
            "Snacks", "local foods"), "recipe category updated")

    def test_delete_recipe_category_not_found(self):
        self.assertEqual(self.user.delete_recipe_category(
            "not exist"), "recipe category not found"
        )

    def test_delete_recipe_category_deleted(self):
        self.user.add_recipe_category("lunch recipes")
        self.assertEqual(self.user.delete_recipe_category("lunch recipes"),
                         "recipe category deleted")

    def test_view_recipe_category(self):
        pass
        # self.assertEqual(self.user.view_recipe_category(" "),
        #                 "recipe_categories is empty")


class Recipe_categoryTest(unittest.TestCase):

    def setUp(self):
        self.recipes = Recipe_category("")

    def test_recipe_instantiation(self):
        self.assertIsInstance(self.recipes, Recipe_category,
                              "Failed to instantiate")

    def test_add_recipe_added(self):
        self.assertEqual(self.recipes.add_recipe(
            "pillawo"), "recipe added")

    def test_add_recipe_exists(self):
        self.recipes.add_recipe("pizza")
        self.assertEqual(self.recipes.add_recipe(
            "pizza"), "recipe already exists")

    def test_edit_description_not_found(self):
        self.assertEqual(self.recipes.edit_description(
            "chicken recipe", "beef recipe"), "recipe not found")

    def test_edit_description_edited_succesfully(self):
        self.recipes.add_recipe("pizza")
        self.assertEqual(self.recipes.edit_description(
            "chicken", "pizza"), "New description already in recipe_category")

    def test_delete_recipe_not_found(self):
        self.assertEqual(self.recipes.delete_recipe(
            "katogo"), "recipe not found")

    def test_recipe_item(self):
        self.recipes.add_recipe("katogo")
        self.assertEqual(self.recipes.delete_recipe(
            "katogo"), "recipe deleted")

    def test_view_recipe(self):
        pass
        #self.assertEqual(self.recipes.view_recipe(" "), "no recipe found")


class RecipeTest(unittest.TestCase):
    def setUp(self):
        self.recipe = Recipe("")

    def test_create_item_instance(self):
        self.assertIsInstance(self.recipe, Recipe, "Failed to create instance")


class RepositoryTest(unittest.TestCase):
    def setUp(self):
        self.users = {}
        self.recipe_categories = {}

    def test_repository_instantiation(self):
        pass

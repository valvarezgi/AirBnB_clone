#!/usr/bin/python3
"""Model Unittest → BaseModel
"""


import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Class test
    """

    def setUp(self):
        self.my_model = BaseModel()
        self.my_model2 = BaseModel()
        self.my_model.name = "Vale"
        self.my_model.age = 28

    def test_base(self):
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertEqual(self.my_model.name, "Vale")
        self.assertEqual(self.my_model.age, 28)
        self.assertTrue(hasattr(self.my_model, "id"))
        self.assertTrue(hasattr(self.my_model, "created_at"))
        self.assertTrue(hasattr(self.my_model, "updated_at"))
        self.assertTrue(hasattr(self.my_model, "__class__"))
        model1 = self.my_model.created_at
        model2 = self.my_model2.created_at
        self.assertTrue(model1 != model2)
        model1 = self.my_model.id
        model2 = self.my_model2.id
        self.assertNotEqual(model1, model2)

    def test_to_dict(self):

        dict_json = self.my_model.to_dict()
        self.assertEqual(type(dict_json), dict)
        self.assertTrue(type(dict_json['created_at']) is str)
        self.assertTrue(type(dict_json['updated_at']) is str)

    def test_save(self):
        previous_update = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(previous_update, self.my_model.updated_at)

    def test_str(self):
        self.assertEqual(str(self.my_model), "[BaseModel] ({}) {}".
                         format(self.my_model.id, self.my_model.__dict__))
        self.assertEqual(self.my_model.__str__(), "[BaseModel] ({}) {}".
                         format(self.my_model.id, self.my_model.__dict__))

    def test_kwargs(self):
        dict_json = self.my_model.to_dict()
        my_model2 = BaseModel(**dict_json)
        self.assertFalse(my_model2 is self.my_model)
        self.assertEqual(self.my_model.id, my_model2.id)
        self.assertEqual(self.my_model.created_at, my_model2.created_at)
        self.assertEqual(self.my_model.updated_at, my_model2.updated_at)

if __name__ == '__main__':
    unittest.main()

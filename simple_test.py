import pytest
from main import *
# def test_constructor():
#    with pytest.raises(CustomException):
#       input_data(5)

# Success
def test_constructor():
   test_object = Multitool("Signal", 19, 100, "Black oxide")
   assert test_object.title == "Signal"
   assert test_object.number_of_functions == 19
   assert test_object.price == 100
   assert test_object.color == "Black oxide"

# Failure 
def test_title_validation():
   with pytest.raises(ValueError):
      test_object = Multitool(0, 19, 100, "Black oxide")

# Failure 
def test_number_of_functions_validation():
   with pytest.raises(ValueError):
      test_object = Multitool("Signal", "string", 100, "Black oxide")

   with pytest.raises(ValueError):
      test_object = Multitool("Signal", -1, 100, "Black oxide")

# Failure 
def test_price_validation():
   with pytest.raises(ValueError):
      test_object = Multitool("Signal", 19, -1, "Black oxide")

   with pytest.raises(ValueError):
      test_object = Multitool("Signal", 19, "string", "Black oxide")

# Failure 
def test_color_validation():
   with pytest.raises(ValueError):
      test_object = Multitool("Signal", 19, 100, "oxide")

# Failure 
def test_empty_constructor():
   with pytest.raises(TypeError):
      test_object = Multitool()

# Success
def test_setters():
   test_object = Multitool("Signal", 19, 100, "Black oxide")
   test_object.title = "Surge"
   assert test_object.title == "Surge"
   test_object.number_of_functions = 21
   assert test_object.number_of_functions == 21
   test_object.price = 140
   assert test_object.price == 140
   test_object.color = "Silver"
   assert test_object.color == "Silver"

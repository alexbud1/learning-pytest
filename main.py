COLOR_CHOICES = [
    'Silver',
    'Black oxide',
]

def validate_title(title : str) -> None:
    if not isinstance(title, str): 
        raise ValueError('title must be a string') 

def validate_number_of_functions(number_of_functions : int) -> None:
    if not isinstance(number_of_functions, int):
        raise ValueError('number_of_functions must be an integer')
    if number_of_functions < 0:
        raise ValueError('number_of_functions must be positive integer')

def validate_price(price : int) -> None:
    if not isinstance(price, int):
        raise ValueError('price must be an integer')
    if price < 0:
        raise ValueError('price must be positive integer')

def validate_color(color : str) -> None:
    if color not in COLOR_CHOICES:
        raise ValueError('color must be one of the following:'+ ', '.join(COLOR_CHOICES))



class Multitool:
    def __init__(self, title : str, number_of_functions : int, price : int, color : str) -> None:
        validate_title(title)           
        self._title = title
        
        validate_number_of_functions(number_of_functions)
        self.number_of_functions = number_of_functions

        validate_price(price)
        self.price = price

        validate_color(color)
        self.color = color
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title : str) -> None:
        validate_title(title)            
        self._title = title

    @property
    def number_of_functions(self) -> int:
        return self._number_of_functions

    @number_of_functions.setter
    def number_of_functions(self, number_of_functions : int) -> None:
        validate_number_of_functions(number_of_functions)
        self._number_of_functions = number_of_functions

    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def price(self, price : int) -> None:
        validate_price(price)
        self._price = price

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, color : str) -> None:
        validate_color(color)
        self._color = color

    def __repr__(self) -> str:
        return f'Multitool({self._title!r}, {self.number_of_functions!r}, {self.price!r}, {self.color!r})'

object = Multitool("Signal", 19, 100, "Silver")
print(object)

# object.number_of_functions = "dcsdc"
# # object.title = 0
# print(object)

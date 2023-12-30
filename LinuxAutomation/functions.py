# def <FUNCTION NAME>(<PARAMETERS>):
#     <FUNCTION BODY or CODE BLOCK>

def my_shiny_new_function():
    '''This is a doc string.
    It should describe what the function does,
    what parameters work, and what the function returns.
    '''
    pass

def example_docstring(param1, param2):
    """
    Description of the function.

    Parameters:
    param1 (type): Description of param1.
    param2 (type): Description of param2.

    Returns:
    type: Description of return value.
    """
    pass

def filter_and_order_dicts(listOfdict):
    """
    Current function filters list of dictionaries by condition age > 25 and order it by age.

    Parameters:
    listOfdict (list of dict): Dictionary.

    Returns:
    list of dict: Filtered and sorted persons - list of dictionaries.
    """

    return sorted((person for person in listOfdict if person["age"] > 25), \
                  key=lambda person: person["age"])

def default_params(first=1, second=2):
    '''Function with assigned default values'''
    print(f"first:{first}")
    print(f"second:{second}")

def no_return():
    '''No return defined'''
    pass

def double(input):
     '''double input'''
     return input*2

def triple(input):
     '''Triple input'''
     return input*3




# TODO: lambda functions - Anonymous functions

def main():
    print(no_return())

    double
type(double)
#<class 'function'>

functions = [double, triple]
for function in functions:
    print(function(3))

    people = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 35},
        {"name": "Charlie", "age": 30}
    ]
    # type(people)
    print(filter_and_order_dicts(people))

    default_params()

if __name__ == '__main__':
    main()
'''
### kyu 6 ###
Lately you've fallen in love with JSON, and have used it to template different
classes.

However you feel that doing it by hand is too slow, so you wanted to create a
decorator that would do it auto-magically!

Explanation
Your task is to write a decorator that loads a given JSON file object and makes
each key-value pair an attribute of the given class.

Example
Given the following data is written in the /tmp/myClass.json file:

{
  "foo": "bar",
  "an_int": 5,
  "this_kata_is_awesome": true
}
Here's how you would use the decorator:

@jsonattr("/tmp/myClass.json")
class MyClass:
    pass


MyClass.foo == "bar"
MyClass.an_int == 5
MyClass.this_kata_is_awesome == True
'''

def jsonattr(filepath):
    def wrapper(cls):
        def inner_wrapper(cls):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self._file_path = file_path
                    self._load_state()

                def _load_state(self):
                    try:
                        with open(self._file_path, 'r') as file:
                            state = json.load(file)
                            self.__dict__.update(state)
                    except (FileNotFoundError, json.JSONDecodeError):
                        pass
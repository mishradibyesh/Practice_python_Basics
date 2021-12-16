"""
implementing basic data type problems
learning Dictionary and set  data type
"""
""" dictionary: Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates. """
my_dictionary = {
"brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
value = my_dictionary.get("model")
print(value)
my_dictionary.update({'price' : "1000000000"})
print(my_dictionary)
my_dictionary.pop('price')
print(my_dictionary)
print(my_dictionary.values())
print(my_dictionary.keys())
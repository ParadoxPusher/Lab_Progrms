def add_entry(d):
    d["new_key"] = "new_value"
    print("Inside add_entry: ", d)

def reassign_dict(d):
    d = {"brand_new": "dict"}
    print("Inside reassign_dict: ", d)

my_dict = {"a": 1, "b": 2}
print("Before: ", my_dict)

add_entry(my_dict)
print("After add_entry: ", my_dict)

reassign_dict(my_dict)
print("After reassign_dict: ", my_dict)
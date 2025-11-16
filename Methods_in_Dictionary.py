info = {"name":"Omkar",
        "from":"India",
        "marks":[80,90,78]}
print(info)

# Item method to return the list of key,values
print(info.items())

# key method to return the list of keys
print(info.keys())

# Update method to update the dictionary
info.update({"name":"Omii"})
print(info)

# Get method to get the specific value
print(info.get("marks"))
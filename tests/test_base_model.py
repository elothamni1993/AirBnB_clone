# tests/test_base_model.py
#!/usr/bin/python3
from models.base_model import BaseModel

# Test instance creation
my_model = BaseModel()
print(my_model)

# Test id type
print(f"id type: {type(my_model.id)}")

# Test created_at type
print(f"created_at type: {type(my_model.created_at)}")

# Test 2 instances creation with different ids
another_model = BaseModel()
print(f"Another model id: {another_model.id}")

# Test __str__ implementation
print(my_model.__str__())

# Test to_dict()
my_model_dict = my_model.to_dict()
print(my_model_dict)

# Test save() and updated_at type
my_model.save()
print(f"updated_at type: {type(my_model.updated_at)}")


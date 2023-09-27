person = {
    'name': 'Vũ Thanh Tài',
    'age': 22,
    'male': True,
    'status': 'single'        
    }
print(person)
print(person['name']) # Vũ Thanh Tài
print(person['status'])
person['status'] = "married"
print("Update person[status]: ", person)
del person['status']
print("delete person[status]: ", person)
person.clear()
print("clear person: ", person)
person['name'] = 'Vũ Thanh Tài'
person['option'] = { 
    'age': 22,
    'male': True,
    'status': 'single'        
    }
print('New person: ', person)
print("get person option: ", person.get("option", "Not found option"))
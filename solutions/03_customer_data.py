new_data = {
        'customer_id': 23,
        'first_name': 'Joseph',
        'last_name': 'Smith',
        'city': 'London',
        'country': 'UK'
}
table.insert(new_data)
result = table.find_one(first_name='Joseph', country='UK')
print(result)

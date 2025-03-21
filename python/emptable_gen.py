import random
from faker import Faker

# Initialize the Faker library to generate names
fake = Faker()

# Define the country codes and their distribution
country_codes = ['US', 'MX', 'CA']
distribution = {'US': 0.62, 'MX': 0.34, 'CA': 0.04}

# To store the generated employee IDs and avoid duplicates
generated_ids = set()

def generate_employee_id():
    while True:
        # Select the country code based on the distribution
        country = random.choices(country_codes, weights=[distribution['US'], distribution['MX'], distribution['CA']], k=1)[0]
        
        # Generate a random 6-digit number
        random_number = random.randint(100000, 999999)
        
        # Create the employee ID
        employee_id = f"{country}{random_number}"
        
        # Ensure the ID is unique
        if employee_id not in generated_ids:
            generated_ids.add(employee_id)
            return employee_id

def generate_employee_data():
    employee_id = generate_employee_id()
    name = fake.name()  # Generate a random name
    return employee_id, name

# Test the generation and output some results
for _ in range(10):
    emp_id, emp_name = generate_employee_data()
    print(f"Employee ID: {emp_id}, Name: {emp_name}")

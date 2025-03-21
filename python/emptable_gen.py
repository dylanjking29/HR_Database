from faker import Faker
import random

fake = Faker()

def generate_employee():
    return {
        "employee_id": random.randint(1000, 9999),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone_number": fake.phone_number(),
        "address": fake.address(),
        "hire_date": fake.date_this_decade(),
        "job_title": fake.job(),
        "department": random.choice(["HR", "Sales", "Engineering", "Finance", "Marketing"]),
        "salary": random.randint(40000, 120000),
    }

# Generate 10 synthetic employees
employees = [generate_employee() for _ in range(10)]

for employee in employees:
    print(employee)

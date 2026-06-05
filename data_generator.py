from faker import Faker
import pandas as pd
import random

fake = Faker()


def generate_column_data(column_name):

    col = column_name.lower()

    if "name" in col:
        return fake.name()

    elif "email" in col:
        return fake.email()

    elif "phone" in col:
        return fake.phone_number()

    elif "address" in col:
        return fake.address()

    elif "city" in col:
        return fake.city()

    elif "country" in col:
        return fake.country()

    elif "date" in col:
        return fake.date()

    elif "marks" in col:
        return random.randint(0, 100)

    elif "salary" in col:
        return random.randint(20000, 150000)

    elif "age" in col:
        return random.randint(18, 60)

    elif "department" in col:
        return random.choice(
            ["IT", "HR", "Finance", "Sales"]
        )

    elif "division" in col:
        return random.choice(
            ["A", "B", "C"]
        )

    else:
        return fake.word()


def generate_dataset(columns, rows):

    columns = [c.strip() for c in columns.split(",")]

    data = {}

    for col in columns:

        data[col] = [
            generate_column_data(col)
            for _ in range(rows)
        ]

    return pd.DataFrame(data)
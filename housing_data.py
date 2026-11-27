import pandas as pd
import numpy as np


def load_data():


    np.random.seed(42)


    area = np.random.randint(600, 3000, 100)
    bedrooms = np.random.randint(1, 6, 100)
    age = np.random.randint(1, 30, 100)


    price = (
        2000 * area
        + 50000 * bedrooms
        - 10000 * age
        + np.random.randint(-20000, 20000, 100)
    )


    df = pd.DataFrame({
        "area": area,
        "bedrooms": bedrooms,
        "age": age,
        "price": price
    })


    return df

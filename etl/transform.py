import pandas as pd
from extract import load_planet_data, load_star_data

def load_data():
    planet_data = load_planet_data()
    star_data = load_star_data()

    return planet_data, star_data

load_data()
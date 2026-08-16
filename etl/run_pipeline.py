from etl.nasa_data import fetch_exoplanet_data
from etl.extract import load_planet_data, load_star_data
from etl.transform import clean_data
from src.config import ENGINE
from etl.load import load_data

def run_pipeline():
    # Fetch data from NASA Exoplanet Archive
    nasa_data = fetch_exoplanet_data()

    # Load planet and star data
    planet_data = load_planet_data(nasa_data)
    star_data = load_star_data(nasa_data)

    # Clean the data
    clean_planet_data, clean_star_data = clean_data(planet_data, star_data)

    # Load the cleaned data into the database
    load_data(ENGINE, clean_star_data, clean_planet_data)

if __name__ == "__main__":
    run_pipeline()
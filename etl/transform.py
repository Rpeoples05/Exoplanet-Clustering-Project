from src.config import CLEAN_PLANET_PATH, CLEAN_STAR_PATH
import pandas as pd

def clean_data(planet_data, star_data):
    # Clean planet data
    planet_data = planet_data.drop(columns=['eccentricity'])
    planet_data = planet_data[planet_data.notna().all(axis=1)]
    planet_data = planet_data.rename(columns={"dec": "dec_"})

    #Clean star data
    star_data = star_data[star_data['star_name'].isin(planet_data['star_name'])]
    star_data = star_data.drop(columns=['star_type','star_age','star_metallicity'])
    star_data = star_data[star_data.notna().all(axis=1)]

    # Filter Planet Data
    planet_data = planet_data[planet_data['star_name'].isin(star_data['star_name'])]

    # Save cleaned data to CSV
    planet_data.to_csv(CLEAN_PLANET_PATH, index=False)
    star_data.to_csv(CLEAN_STAR_PATH, index=False)
    
    return planet_data, star_data
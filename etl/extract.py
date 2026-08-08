import pandas as pd
from etl.nasa_data import fetch_exoplanet_data
from pathlib import Path
from src.config import RAW_PLANET_PATH, RAW_STAR_PATH

DATA = fetch_exoplanet_data()

def load_planet_data():
    planet_data = DATA[[
        'pl_name',
        'hostname',
        'sy_pnum',
        'pl_orbper',
        'pl_orbsmax',
        'pl_rade',
        'pl_bmasse',
        'pl_radj',
        'pl_bmassj',
        'pl_dens',
        'pl_eqt',
        'pl_orbeccen',
        'ra',
        'dec'
    ]].copy()

    planet_data.columns = [
        'planet_name',
        'star_name',
        'planets_in_system',
        'orbital_period',
        'semi_major_axis',
        'radius_earths',
        'mass_earths',
        'radius_jupiters',
        'mass_jupiters',
        'density',
        'equilibrium_temperature',
        'eccentricity',
        'ra',
        'dec'
    ]

    planet_data.to_csv(RAW_PLANET_PATH, index=False)
    
    return planet_data

def load_star_data():
    star_data = DATA[[
        'hostname',
        'st_spectype',
        'st_teff',
        'st_rad',
        'st_mass',
        'st_met',
        'st_logg',
        'st_age'
    ]].copy()

    star_data.columns = [
        'star_name',
        'star_type',
        'star_temperature',
        'star_radius',
        'star_mass',
        'star_metallicity',
        'star_surface_gravity',
        'star_age'
    ]

    star_data.to_csv(RAW_STAR_PATH, index=False)

    return star_data
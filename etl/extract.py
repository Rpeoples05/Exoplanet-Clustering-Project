import pandas as pd
from etl.nasa_data import fetch_exoplanet_data

DATA = fetch_exoplanet_data()

def save_raw_data():
    DATA.to_csv('../data/raw_exoplanet_data.csv', index=False)

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

    return star_data
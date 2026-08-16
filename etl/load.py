import os
import sqlalchemy as db
from src.config import ENGINE

def upsert_stars(engine, df):
    with engine.begin() as connection:
        for index, row in df.iterrows():
            insert_stmt = db.text("""
                INSERT INTO stars (star_name, star_temperature, star_mass, star_radius, star_surface_gravity)
                VALUES (:star_name, :star_temperature, :star_mass, :star_radius, :star_surface_gravity)
                ON DUPLICATE KEY UPDATE
                    star_temperature = VALUES(star_temperature),
                    star_mass = VALUES(star_mass),
                    star_radius = VALUES(star_radius),
                    star_surface_gravity = VALUES(star_surface_gravity);
            """)
            connection.execute(insert_stmt, row.to_dict())

def upsert_planets(engine, df):
    with engine.begin() as connection:
        for index, row in df.iterrows():
            insert_stmt = db.text("""
                INSERT INTO exoplanets (planet_name, star_name, planets_in_system, mass_earths, radius_earths, mass_jupiters, radius_jupiters, density, equilibrium_temperature, orbital_period, semi_major_axis, ra, dec_)
                VALUES (:planet_name, :star_name, :planets_in_system, :mass_earths, :radius_earths, :mass_jupiters, :radius_jupiters, :density, :equilibrium_temperature, :orbital_period, :semi_major_axis, :ra, :dec_)
                ON DUPLICATE KEY UPDATE
                    star_name = VALUES(star_name),
                    planets_in_system = VALUES(planets_in_system),
                    orbital_period = VALUES(orbital_period),
                    semi_major_axis = VALUES(semi_major_axis),
                    radius_earths = VALUES(radius_earths),
                    mass_earths = VALUES(mass_earths),
                    radius_jupiters = VALUES(radius_jupiters),
                    mass_jupiters = VALUES(mass_jupiters),
                    density = VALUES(density),
                    equilibrium_temperature = VALUES(equilibrium_temperature),
                    ra = VALUES(ra),
                    dec_ = VALUES(dec_);
            """)
            connection.execute(insert_stmt, row.to_dict())

def load_data(engine, star_df, planet_df):
    upsert_stars(engine, star_df)
    upsert_planets(engine, planet_df)
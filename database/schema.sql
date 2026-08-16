CREATE DATABASE IF NOT EXISTS exoclusters;

USE exoclusters;

DROP TABLE IF EXISTS stars;
DROP TABLE IF EXISTS exoplanets;

CREATE TABLE IF NOT EXISTS stars (
    star_name VARCHAR(255) NOT NULL PRIMARY KEY,
    star_temperature DECIMAL(10, 2),
    star_mass DECIMAL(10, 2),
    star_radius DECIMAL(10, 2),
    star_surface_gravity DECIMAL(10, 2)
);

CREATE TABLE IF NOT EXISTS exoplanets (
    planet_name VARCHAR(255) NOT NULL PRIMARY KEY,
    star_name VARCHAR(255),
    planets_in_system INT,
    mass_earths DECIMAL(10, 2),
    radius_earths DECIMAL(10, 2),
    mass_jupiters DECIMAL(10, 2),
    radius_jupiters DECIMAL(10, 2),
    density DECIMAL(10, 2),
    equilibrium_temperature DECIMAL(10, 2),
    orbital_period DOUBLE,
    semi_major_axis DECIMAL(10, 2),
    ra DECIMAL(10, 6),
    dec_ DECIMAL(10, 6),
    FOREIGN KEY (star_name) REFERENCES stars(star_name)
);



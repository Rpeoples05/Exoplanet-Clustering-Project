CREATE DATABASE IF NOT EXISTS exoclusters;

USE exoclusters;

CREATE TABLE IF NOT EXISTS stars (
    star_id INT AUTO_INCREMENT PRIMARY KEY,
    star_name VARCHAR(255) NOT NULL,
    star_temperature DECIMAL(10, 2),
    star_mass DECIMAL(10, 2),
    star_radius DECIMAL(10, 2),
    star_metallicity DECIMAL(10, 2),
    star_surface_gravity DECIMAL(10, 2)
);

CREATE TABLE IF NOT EXISTS exoplanets (
    planet_id INT AUTO_INCREMENT PRIMARY KEY,
    planet_name VARCHAR(255) NOT NULL,
    star_id INT,
    mass_earths DECIMAL(10, 2),
    radius_earths DECIMAL(10, 2),
    mass_jupiters DECIMAL(10, 2),
    radius_jupiters DECIMAL(10, 2),
    orbital_period DECIMAL(10, 2),
    semi_major_axis DECIMAL(10, 2),
    eccentricity DECIMAL(10, 2),
    FOREIGN KEY (star_id) REFERENCES stars(star_id)
);



CREATE INDEX idx_exoplanet_star
ON exoplanets(star_id);

CREATE INDEX idx_star_name
ON stars(star_name);

CREATE INDEX idx_exoplanet_name
ON exoplanets(planet_name);
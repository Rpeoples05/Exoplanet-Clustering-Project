import requests
import pandas as pd
from io import StringIO

TAP_URL = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"


def fetch_exoplanet_data():

    query = """
    SELECT
        pl_name,
        hostname,
        sy_pnum,
        pl_orbper,
        pl_orbsmax,
        pl_rade,
        pl_bmasse,
        pl_radj,
        pl_bmassj,
        pl_dens,
        pl_eqt,
        pl_orbeccen,
        st_spectype,
        st_teff,
        st_rad,
        st_mass,
        st_met,
        st_logg,
        st_age,
        ra,
        dec
    FROM pscomppars
    """

    params = {
        "query": query,
        "format": "csv"
    }

    response = requests.get(TAP_URL, params=params)
    response.raise_for_status()

    return pd.read_csv(StringIO(response.text))
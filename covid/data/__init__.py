"""
Import data sets from various sources.
"""
from .cia_factbook import cia_factbook, age_distribution, hospital_bed_density
from .data import contact_matrix, CONTACT_MATRIX_COUNTRIES, CONTACT_MATRIX_IDS, COUNTRIES
from .ibge import brazil_healthcare_capacity, city_id_from_name
from .mortality import covid_mortality, covid_mean_mortality
from .ibge_demographic import brazil_city_demography

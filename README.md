# Visualization of the annual EU energy data #

    Demo at: https://envis.ankaa.uberspace.de/

The visualization is based on the annual energy data from
Eurostat, the Statistical Office of the European Union. The data can be found
[here](http://ec.europa.eu/eurostat/web/energy/data/database).

The backend is developed with [python 3](https://www.python.org/downloads/release/python-360/)
using the [flask](http://flask-sqlalchemy.pocoo.org/2.1/) microframework.
The frontend mainly uses [D3](https://d3js.org/) as well as the
[jinja2](http://jinja.pocoo.org/) templating engine.


### Install ##
* Clone the repository
* Create a virtual environment with python 3
* Activate the virtual environment and install requirements:
  pip install -r requirements.txt


### Run ##
* Activate the virtual environment
* Make sure run.py has execution rights (chmod u+x run.py)
* In a terminal run: python run.py
* Open your browser on [127.0.0.1:8000](127.0.0.1:8000)


### Sankey diagram ###
The energy flow is represented as [sankey diagram](https://en.wikipedia.org/wiki/Sankey_diagram).
A sankey diagram consists of nodes and links. In this case the nodes represent
indicators of a country.
Examples for nodes are the primary energy production of a country,
imports and exports as well as energy transformation and consumption.

The links between the nodes represent the flow of energy. The width of the links
show the quantity which is expressed in
[kilotons of oil equivalent](https://en.wikipedia.org/wiki/Tonne_of_oil_equivalent).


### API ###
A API was developed to get the energy data for a specific country and year.
For example to get the energy data for the 28 member states of the EU for
the year 2015 the query string [?geo=EU28&year=2015]() can be used on the
API:
[http://127.0.0.1:8000/api/v1.0/json?geo=EU28&year=2015](http://127.0.0.1:8000/api/v1.0/json?geo=EU28&year=2015)

    Demo: https://envis.ankaa.uberspace.de/api/v1.0/json?geo=EU28&year=2015

The following list contains all possible countries usable for the geo query string:
* EU28 = European Union (28 countries)
* EA19 = Euro area (19 countries)
* BE   = Belgium
* BG = Bulgaria
* CZ = Czech Republic
* DK = Denmark
* DE = Germany (until 1990 former territory of the FRG)
* EE = Estonia
* IE = Ireland
* EL = Greece
* ES = Spain
* FR = France
* HR = Croatia
* IT = Italy
* CY = Cyprus
* LV = Latvia
* LT = Lithuania
* LU = Luxembourg
* HU = Hungary
* MT = Malta
* NL = Netherlands
* AT = Austria
* PL = Poland
* PT = Portugal
* RO = Romania
* SI = Slovenia
* SK = Slovakia
* FI = Finland
* SE = Sweden
* UK = United Kingdom
* IS = Iceland
* NO = Norway
* ME = Montenegro
* MK = Former Yugoslav Republic of Macedonia, the
* AL = Albania
* RS = Serbia
* TR = Turkey
* XK = Kosovo (under United Nations Security Council Resolution 1244/99)
* UA = Ukraine


### Project structure ###
The project structure looks like the following tree:

energyvis/ (root directory) <br>
|--app/ <br>
|--app/static/ <br>
|--app/templates/ <br>
|--data/ <br>
|--instance/ <br>
|--tests/ <br>
|--config.py <br>
|--config_example.cmd <br>
|--manage.py <br>
|--run.py <br>
|--utils.py <br>

__app/__ <br>
Contains the main files for the visualization like database models, views, the
API as well as html templates and static files.

__data/__ <br>
Contains the database and additional data necessary to create the nodes and links
for the visualization. 
* energy.db: Database with energy data. Imported from nrg_sankey.csv
* nrg_sankey.csv: Contains the energy data from eurostat for the years 1990 to 2015
* nodes_default.csv: Contains the nodes used for the visualization
* links_default.csv: Maps the link between the nodes from source node to target node.
 Value represents the indicator ID to retrieve the flow value in KTOE from the database.
* geo.txt: Contains a list of all the countries
* product.txt: Contains the energy products like natural gas, wind power, etc.
* year.txt: Contains the years from 1990 until 2015 to map the energy data to

__instance/__ <br>
The instance folder contains additional settings for the app (like secret keys)
which should be excluded from version control.

__tests/__ <br>
The tests folder contains unit tests for the app.

__config.py__ <br>
Main project configuration files. You can choose between the three configurations:
Development, Testing and Production.

__config_example.cmd__ <br>
Example windows shell script to set environment variables for configuration.

__manage.py__ <br>
Contains functions for managing the project like database initialization and
database imports.

__run.py__ <br>
Module to run the app: python run.py

__utils.py__ <br>
Utility functions for the app.


### Background ###
An energy balance is an accounting framework for the compilation and
understanding of data on all energy products for a country.
The energy balance is represented as a table matrix and shows the statistical
balancing of energy products and their flow in the economy.

An energy balance includes energy production and energy consumption
in energy units (terajoule or kilotons of oil equivalent) over a period of one
year. The results show the connections between the supply, the inputs into the
energy transformation processes and their outputs as well as the actual energy
consumption in different areas of the end use.

One tonne of oil equivalent is a standardized unit of energy,
defined as net heating value of 107 kilocalories (41,868 MJ),
which is roughly equal to the net energy equivalent of one tonne of crude oil.

Eurostat's energy statistics cover energy balances between 1990 and 2015 for
the 28 member states of the European Union as well as candidates for accession
and potential candidates for accession, as well as states of the European Free
Trade Association. The data are published by the Statistical Office of the
European Union (Eurostat). Eurostat is the administrative unit of the
European Union (EU) for the production of official European statistics based
in Luxembourg.
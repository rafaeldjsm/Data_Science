# Where to open a new coffee shop?

![](https://raw.githubusercontent.com/rafaeldjsm/Data_Science/master/Imagens/webp-net-resizeimage-6-1.webp)

## 📖 Background
You are helping a client who owns coffee shops in Colorado. The company's coffee shops serve high-quality and responsibly sourced coffee,  pastries, and sandwiches. They operate three locations in Fort Collins and want to expand into Denver. 

Your client believes that the ideal location for a new store is close to affluent households, and the store appeals to the 20-35 year old demographic.
 
Your team collected geographical and demographic information about Denver's neighborhoods to assist the search. They also collected data for Starbucks stores in Denver. Starbucks and the new coffee shops do not compete for the same clients; the team included their location as a reference.

## 💾 The data
You have assembled information from three different sources ([locations](https://github.com/chrismeller/), [neighborhoods](http://data.denvergov.org), [demographics](https://www.census.gov/)):

#### Starbucks locations in Denver, Colorado
- "StoreNumber" - Store Number as assigned by Starbucks
- "Name" - Name identifier for the store
- "PhoneNumber" - Phone number for the store
- "Street 1, 2, and 3" - Address for the store
- "PostalCode" - Zip code of the store
- "Longitude, Latitude" - Coordinates of the store

#### Neighborhoods' geographical information
- "NBHD_ID" - Neighborhood ID (matches the census information)
- "NBHD_NAME" - Name of the statistical neighborhood
- "Geometry" - Polygon that defines the neighborhood

#### Demographic information
- "NBHD_ID" - Neighborhood ID (matches the geographical information)
- "NBHD_NAME' - Nieghborhood name
- "POPULATION_2010' - Population in 2010
- "AGE_ " - Number of people in each age bracket (< 18, 18-34, 35-65, and > 65)
- "NUM_HOUSEHOLDS" - Number of households in the neighborhood
- "FAMILIES" - Number of families in the neighborhood
- "NUM_HHLD_100K+" - Number of households with income above 100 thousand USD per year

_Starbucks locations were scrapped from the Starbucks store locator webpage by [Chris Meller](https://github.com/chrismeller/)._  
_Statistical Neighborhood information from the [City of Denver Open Data Catalog](http://data.denvergov.org), [CC BY 3.0](http://creativecommons.org/licenses/by/3.0/) license._      
_Census information from the [United States Census Bureau](https://www.census.gov/). Publicly available information._


# 3 Final Considerations

<p align="center">
  <img src="https://github.com/rafaeldjsm/Data_Science/blob/master/Geospatial_Intelligence_for_the_best_Coffee_Shop_location/data/density_100k.png" alt="Sublime's custom image"/>
</p>


<p align="center">
  <img src="https://github.com/rafaeldjsm/Data_Science/blob/master/Geospatial_Intelligence_for_the_best_Coffee_Shop_location/data/kde_geoplot.png" alt="Sublime's custom image"/>
</p>


## First, let's check the neighborhoods in common among the top nine in each income and age criteria.

> Note that there are only three out of the 9 best neighborhoods in common when considering the two main criteria, in these neighborhoods 2 have a good density of starbusks stores and only one with a low density, as the amount of starbucks is given only as a reference, we will adopt the three neighborhoods found above.

<table border="1" class="marginStyle" align="center">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>NBHD_NAME</th>\n      <th>AREA</th>\n      <th>Count_Starbucks</th>\n      <th>Starbucks_density</th>\n      <th>AGE_18_TO_34</th>\n      <th>NUM_HHLD_100K+</th>\n      <th>AGE_18_TO_34_density</th>\n      <th>NUM_HHLD_100K+_density</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Civic Center</td>\n      <td>0.791594</td>\n      <td>5.0</td>\n      <td>6.316370</td>\n      <td>2012.0</td>\n      <td>1519.0</td>\n      <td>2541.707311</td>\n      <td>1918.913223</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Cheesman Park</td>\n      <td>1.371804</td>\n      <td>3.0</td>\n      <td>2.186902</td>\n      <td>5961.0</td>\n      <td>1680.0</td>\n      <td>4345.373953</td>\n      <td>1224.665029</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>North Capitol Hill</td>\n      <td>0.918346</td>\n      <td>0.0</td>\n      <td>0.000000</td>\n      <td>3238.0</td>\n      <td>1010.0</td>\n      <td>3525.905913</td>\n      <td>1099.803883</td>\n    </tr>\n  </tbody>\n</table>

- Civic Center
- Cheesman Park
- North Capitol Hill

>> This strategy also focuses on downtown Denver, as seen in the Starbucks Store Distribution Kernel Density Estimate and Income and Age Kernel Density Estimate.


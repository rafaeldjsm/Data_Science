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

<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>NBHD_ID</th>\n      <th>NBHD_NAME</th>\n      <th>geometry</th>\n      <th>AREA</th>\n      <th>Count_Starbucks</th>\n      <th>Starbucks_density</th>\n      <th>AGE_18_TO_34</th>\n      <th>NUM_HHLD_100K+</th>\n      <th>AGE_18_TO_34_density</th>\n      <th>NUM_HHLD_100K+_density</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>16</td>\n      <td>Civic Center</td>\n      <td>POLYGON ((-104.98739 39.74011, -104.98739 39.74001, -104.98739 39.73961, -104.98741 39.73843, -104.98739 39.73685, -104.98740 39.73526, -104.98742 39.73386, -104.98740 39.73204, -104.98740 39.73045, -104.98740 39.72909, -104.98742 39.72728, -104.98742 39.72694, -104.98753 39.72700, -104.98777 39.72714, -104.98808 39.72729, -104.98831 39.72742, -104.98854 39.72756, -104.98869 39.72767, -104.98874 39.72769, -104.98879 39.72770, -104.98889 39.72774, -104.98895 39.72777, -104.98906 39.72787, -104.98925 39.72802, -104.98937 39.72809, -104.98947 39.72816, -104.98955 39.72822, -104.98960 39.72826, -104.98965 39.72831, -104.98971 39.72835, -104.98980 39.72843, -104.98986 39.72850, -104.98993 39.72859, -104.98999 39.72866, -104.99004 39.72871, -104.99011 39.72877, -104.99017 39.72884, -104.99022 39.72889, -104.99041 39.72909, -104.99046 39.72915, -104.99053 39.72923, -104.99059 39.72932, -104.99068 39.72945, -104.99075 39.72955, -104.99085 39.72967, -104.99092 39.72977, -104.99104 39.72992, -104.99112 39.73003, -104.99125 39.73018, -104.99132 39.73028, -104.99140 39.73038, -104.99154 39.73056, -104.99163 39.73067, -104.99173 39.73082, -104.99181 39.73092, -104.99186 39.73099, -104.99194 39.73111, -104.99201 39.73123, -104.99208 39.73133, -104.99213 39.73140, -104.99221 39.73150, -104.99234 39.73166, -104.99246 39.73183, -104.99258 39.73201, -104.99267 39.73213, -104.99283 39.73234, -104.99295 39.73250, -104.99303 39.73262, -104.99312 39.73274, -104.99325 39.73291, -104.99325 39.73291, -104.99333 39.73302, -104.99343 39.73316, -104.99350 39.73326, -104.99354 39.73332, -104.99360 39.73341, -104.99373 39.73357, -104.99379 39.73364, -104.99392 39.73386, -104.99398 39.73393, -104.99404 39.73402, -104.99412 39.73415, -104.99422 39.73427, -104.99431 39.73438, -104.99441 39.73449, -104.99445 39.73455, -104.99449 39.73462, -104.99455 39.73470, -104.99472 39.73492, -104.99480 39.73503, -104.99489 39.73515, -104.99498 39.73527, -104.99505 39.73536, -104.99518 39.73553, -104.99530 39.73570, -104.99541 39.73585, -104.99550 39.73597, -104.99560 39.73610, -104.99565 39.73618, -104.99573 39.73631, -104.99581 39.73644, -104.99588 39.73653, -104.99595 39.73660, -104.99630 39.73709, -104.99639 39.73722, -104.99648 39.73735, -104.99668 39.73762, -104.99686 39.73786, -104.99698 39.73802, -104.99704 39.73809, -104.99706 39.73811, -104.99716 39.73824, -104.99722 39.73838, -104.99740 39.73854, -104.99746 39.73860, -104.99749 39.73864, -104.99755 39.73870, -104.99759 39.73875, -104.99764 39.73882, -104.99766 39.73887, -104.99771 39.73896, -104.99776 39.73904, -104.99780 39.73910, -104.99787 39.73917, -104.99791 39.73921, -104.99794 39.73926, -104.99797 39.73932, -104.99800 39.73940, -104.99802 39.73943, -104.99807 39.73950, -104.99812 39.73957, -104.99815 39.73961, -104.99820 39.73964, -104.99826 39.73970, -104.99831 39.73976, -104.99835 39.73981, -104.99838 39.73986, -104.99841 39.73992, -104.99857 39.74019, -104.99825 39.74018, -104.99813 39.74018, -104.99694 39.74016, -104.99651 39.74016, -104.99644 39.74016, -104.99527 39.74015, -104.99436 39.74014, -104.99353 39.74014, -104.99292 39.74013, -104.99250 39.74013, -104.99166 39.74013, -104.99042 39.74012, -104.99008 39.74011, -104.98994 39.74012, -104.98982 39.74016, -104.98968 39.74024, -104.98955 39.74037, -104.98943 39.74047, -104.98931 39.74055, -104.98911 39.74061, -104.98894 39.74064, -104.98875 39.74064, -104.98853 39.74057, -104.98853 39.74056, -104.98840 39.74049, -104.98828 39.74039, -104.98812 39.74029, -104.98810 39.74027, -104.98797 39.74019, -104.98792 39.74017, -104.98785 39.74015, -104.98777 39.74013, -104.98751 39.74011, -104.98739 39.74011))</td>\n      <td>0.791594</td>\n      <td>5.0</td>\n      <td>6.316370</td>\n      <td>2012.0</td>\n      <td>1519.0</td>\n      <td>2541.707311</td>\n      <td>1918.913223</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>12</td>\n      <td>Cheesman Park</td>\n      <td>POLYGON ((-104.96019 39.72911, -104.96077 39.72911, -104.96135 39.72911, -104.96193 39.72911, -104.96251 39.72911, -104.96309 39.72911, -104.96366 39.72911, -104.96424 39.72910, -104.96482 39.72910, -104.96588 39.72909, -104.96656 39.72909, -104.96714 39.72909, -104.96773 39.72909, -104.96831 39.72909, -104.96889 39.72909, -104.96946 39.72909, -104.97062 39.72909, -104.97178 39.72908, -104.97294 39.72908, -104.97295 39.73045, -104.97298 39.73205, -104.97298 39.73371, -104.97300 39.73516, -104.97301 39.73688, -104.97302 39.73840, -104.97300 39.73955, -104.97299 39.74004, -104.97276 39.74004, -104.97214 39.74003, -104.97188 39.74003, -104.97129 39.74003, -104.97079 39.74003, -104.97031 39.74003, -104.97014 39.74003, -104.96969 39.74003, -104.96846 39.74001, -104.96785 39.74001, -104.96723 39.74001, -104.96661 39.74001, -104.96599 39.74001, -104.96538 39.74000, -104.96477 39.74000, -104.96412 39.74000, -104.96347 39.73999, -104.96285 39.73999, -104.96224 39.73999, -104.96163 39.73999, -104.96101 39.73999, -104.96040 39.73999, -104.95978 39.73999, -104.95978 39.73972, -104.95978 39.73839, -104.95978 39.73681, -104.95979 39.73504, -104.95980 39.73345, -104.95980 39.73228, -104.95983 39.73195, -104.95984 39.73148, -104.95984 39.73108, -104.95990 39.73093, -104.96009 39.73068, -104.96017 39.73049, -104.96019 39.72911))</td>\n      <td>1.371804</td>\n      <td>3.0</td>\n      <td>2.186902</td>\n      <td>5961.0</td>\n      <td>1680.0</td>\n      <td>4345.373953</td>\n      <td>1224.665029</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>47</td>\n      <td>North Capitol Hill</td>\n      <td>POLYGON ((-104.97338 39.74378, -104.97339 39.74325, -104.97339 39.74268, -104.97339 39.74165, -104.97341 39.74003, -104.97415 39.74002, -104.97479 39.74002, -104.97532 39.74002, -104.97544 39.74002, -104.97610 39.74001, -104.97648 39.74001, -104.97764 39.74001, -104.97821 39.74001, -104.97874 39.74002, -104.97933 39.74002, -104.97991 39.74002, -104.98050 39.74002, -104.98110 39.74003, -104.98173 39.74003, -104.98233 39.74003, -104.98296 39.74003, -104.98358 39.74005, -104.98422 39.74005, -104.98486 39.74006, -104.98548 39.74006, -104.98614 39.74006, -104.98626 39.74011, -104.98739 39.74011, -104.98738 39.74085, -104.98740 39.74147, -104.98741 39.74169, -104.98741 39.74195, -104.98742 39.74221, -104.98739 39.74306, -104.98738 39.74336, -104.98742 39.74483, -104.98741 39.74506, -104.98741 39.74547, -104.98741 39.74593, -104.98741 39.74619, -104.98740 39.74668, -104.98740 39.74697, -104.98740 39.74736, -104.98731 39.74742, -104.98720 39.74752, -104.98611 39.74753, -104.98568 39.74753, -104.98557 39.74760, -104.98548 39.74758, -104.98538 39.74757, -104.98522 39.74756, -104.98509 39.74755, -104.98494 39.74755, -104.98485 39.74755, -104.98476 39.74755, -104.98422 39.74756, -104.98394 39.74756, -104.98359 39.74755, -104.98312 39.74755, -104.98295 39.74755, -104.98231 39.74755, -104.98169 39.74755, -104.98107 39.74755, -104.97989 39.74754, -104.97872 39.74753, -104.97836 39.74753, -104.97821 39.74751, -104.97818 39.74750, -104.97754 39.74696, -104.97699 39.74656, -104.97649 39.74618, -104.97614 39.74591, -104.97478 39.74484, -104.97398 39.74423, -104.97338 39.74378))</td>\n      <td>0.918346</td>\n      <td>0.0</td>\n      <td>0.000000</td>\n      <td>3238.0</td>\n      <td>1010.0</td>\n      <td>3525.905913</td>\n      <td>1099.803883</td>\n    </tr>\n  </tbody>\n</table>

- Civic Center
- Cheesman Park
- North Capitol Hill

>> This strategy also focuses on downtown Denver, as seen in the Starbucks Store Distribution Kernel Density Estimate and Income and Age Kernel Density Estimate.


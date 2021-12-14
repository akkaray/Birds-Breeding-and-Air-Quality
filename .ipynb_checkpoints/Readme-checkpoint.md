# Final-Project
Readme file for Final project
.I have the data of Breeding birds from 2000-2005 distributed according to the county and 5 datasets of air quality index for each year from 2000 to 2005 distributed by county
Firstly i merged the 5 datasets,opened a new csv file and wrote the first dataset to the newfile,i wanted to check the data only for newyork city so filtered newyork's data.
The newcsv didnot have the header so i added the values of header to a list and added it to the csv
following is the script:
```python
import csv
f=open('C:/Users/yasha/OneDrive/Documents/Yahsaswini/Big data procs/Final Project/daily_aqi_by_county_2000.csv','r')
reader = csv.reader(f)
f2 = open('Daily_aqi_data.csv','w')
writer = csv.writer(f2,delimiter=',',lineterminator='\n')
n=0
l=["State Name","county Name","State Code","County Code","Date","AQI","Category","Defining Parameter","Defining Site","Number of Sites Reporting"]
writer.writerow(l)
for row in reader:
    if row[0] == 'New York':
        writer.writerow(row)
n+= 1

f.close
f2.close()
```

-Opened the remaininng datasets and wrote the columns to the new csv
following is the script:

```python
import csv 

f1=open('C:/Users/yasha/OneDrive/Documents/Yahsaswini/Big data procs/Final Project/daily_aqi_by_county_2001.csv','r')
reader1 = csv.reader(f1)
f2=open('Daily_aqi_data.csv','a') 
writer = csv.writer(f2)
n=0
for row in reader1:
    if row[0] == 'New York':
        writer.writerow(row)
n+=1
    
f1.close
f2.close()
```


.I have opened the final merged file of the Airquality and the Birds breeding data where i wanted to lookup the values of "Category" which had list of Good,moderate,unhealthy and veryunhealthy
values to the breeding status column in Birds data where the granularity of date and County are matched in both the datasets.
.I created a lookup by first filtering just the categories of good and veryunhealthy airquality as i wanted to see if the airquality affected the breeding status of birds.
.Defined the names of the columns and formated the county names by using "lower()"and ".replace()" as they were represented differently in each dataset
-defined the key which was derived by merging the columns of Date and County using the string concatenation operator "+" and the lookup value for key was the category of airquality.
following is the code for data
```python
import csv

Bird_data = open('C:/Users/yasha/OneDrive/Documents/Yahsaswini/Big data procs/Final Project/Breeding_Bird_Atlas__Second_Edition__2000-2005.csv', 'r')
reader6 = csv.reader(Bird_data)

AQI = open('Daily_aqi_data.csv','r')
reader7 =csv.reader(AQI)

AQI_lookup={}
n=0
for row2 in reader7:
    if len(row2)>=6:
        
        if row2[6] == "Good" or row2[6] == "Very Unhealthy":
            
            Date_AQI=row2[4]
            County_AQI=row2[1].lower().replace(".","")
            Air_Quality=row2[6]
            k=Date_AQI+'_'+County_AQI
            AQI_lookup[k]=Air_Quality
            
        n+=1
    
print(AQI_lookup['2000-04-18_st lawrence'])
```

-I had the lookup values from AQI dataset,needed to work on the cleansing of Birds dataset 
-Started by opening a csv so as to write the resultant output data into a new csv file,created an empty list called "Birds_behavior"and then applied filters as i wanted to observe the behaviour of the birds that were threatened species
-to match the granularity the date in birds dataset had a different format,so changed it using the datetime functions,
-passed the date to datetimeobject and filled in '0'before the month,date to match format using "zfill()"
-converted it to the format needed and converted it back to string
-defined the name of the rows i needed to print in output and converted the county names using "lower()"
-defined the keyvalue in Birds dataset as a concatenated string of date and county columns in AQI dataset
-Then using the "if" statement if the keys in both the datasets matched then i appended the values of Date,County,Name of Bird,Breeding status,Breeding behavior of birds,Status of Airquality
-I had an issue here cause the Date and county were joined strings so i went back to the key values and added a character of "_" so later i could split them while writing it to the csv file
-following is the script:
```python
import datetime,csv

header=["Date","County","Name of Bird","Breeding_Behavior","Breeding_Status","AirQuality"]
f3=open('Birds_behaviour.csv', 'w',newline='') 
writer = csv.writer(f3)
writer.writerow(header)
n=0
for row1 in reader6:
    Birds_behaviour=[]
    #print(row1)
    if row1[6] == "Threatened":
        if "//" not in row1[10]:
            Date_Bird=row1[10].split('/')
            dto=datetime.datetime.strptime(Date_Bird[0].zfill(2)+Date_Bird[1].zfill(2)+Date_Bird[2],'%m%d%Y')
            dts=datetime.datetime.strftime(dto,'%Y-%m-%d')
            County_Bird=row1[3].lower()
            Name_Bird=row1[4]
            Breeding_Behavior=row1[9]
            Breeding_Status=row1[11]
            k=dts+'_'+County_Bird
            #print(k)
        
        if k in AQI_lookup:
            n+=1
            Birds_behaviour.append(k.split('_')[0])
            Birds_behaviour.append(k.split('_')[1])
            Birds_behaviour.append(Name_Bird)
            Birds_behaviour.append(Breeding_Behavior)#Breeding_Behavior
            Birds_behaviour.append(Breeding_Status)
            Birds_behaviour.append(AQI_lookup[k])#AQI_lookup[k]
            
            #print(Birds_behaviour)
            writer.writerow(Birds_behaviour)
```
-Finally i had a csv which looked like this called BirdsBehaviour:


![Image of csv](Images/Final_Excel_output.png)


-Loaded the shapefile of Newyork state and the BirdsBehaviour csv into the Rstudio
-Loaded bunch of libraries and started mapping the columns i wanted to check and had the first map showing the Airquality data





![Image of Newyork Airquality Map](Images/Newyork_Airquality_Data.png)

-Map displaying the Name of the birds accordig to the counties and their Breeding Status

![Image of Newyork Birds and their breeding status Map](Images/Birds_and_Breeding_status_of_the_birds.png)


-my final goal was to create an interactive map which could display the Bird's name,breedingstatus and quality of air for each county.

-Used leaflet in R to create a basic interactive map
following is the code:
```r
library(leaflet)
m <- leaflet(map_and_data1_as_sp) %>% 
  addTiles()  %>% 
  setView( lat=64.2008, lng=-149.4937 , zoom=2) %>%
  addPolygons(stroke=FALSE )

m
```

![Image of Basic Interactive Map](Images/Basic_interactive_Map.png)

-Added the polygons,Popups,borders,labels and finally tiles to the map and following is the code:

```r
mytext <- paste(
    "<strong>County:<strong> ", map_and_data1_as_sp@data$NAME,"<br/>", 
    "<strong>Bird<strong>: ", map_and_data1_as_sp@data$Name.of.Bird, "<br/>",
    "<strong>Breeding_Status<strong>: ", map_and_data1_as_sp@data$Breeding_Status, "<br/>",
    "<strong>AirQuality<strong>: ", map_and_data1_as_sp@data$AirQuality, "<br/>",
        sep="") %>%
  lapply(htmltools::HTML)

#bins <- c(0, 10, 20, 50, 100, 200, 500, 1000)
#mybins<-colorNumeric(c("red", "green", "blue"), 1:10)
pal <- colorBin("YlOrBr", domain = map_and_data1_as_sp$ALAND, bins = bins)
pal2 <- colorNumeric(
  palette = "BuPu",
  domain = map_and_data_as_sp$ALAND)
pal3 <- colorNumeric(
    c("Yellow", "Purple"),domain = map_and_data1_as_sp$ALAND)
pal4<-colorNumeric(
  palette = "viridis",
  domain = map_and_data_as_sp$ALAND)
```
```r
m %>% addPolygons(
  fillColor = ~pal2(ALAND),
  weight = 2,
  opacity = 0.01,
  color = "White",
  smoothFactor = 0.5,
  dashArray = "",
  fillOpacity = 0.7, highlightOptions = highlightOptions(
    weight = 5,
    color = "white",
    dashArray = "",
    fillOpacity = 1,
    bringToFront = TRUE),
  label = mytext,
    labelOptions = labelOptions( 
      style = list("color" = "grey","font-weight" = "normal","font-style" = "italic", padding = "3px 8px","box-shadow" = "3px 3px rgba(0,0,0,0.25)", 
      textsize = "13px", 
      direction = "auto")))  %>%
  addTiles(group = "OSM") %>%
  addProviderTiles("CartoDB.DarkMatter", group = "Carto") %>%
  addProviderTiles("Esri.WorldImagery", group = "Sat") %>%
  addLayersControl(baseGroups = c("OSM", "Carto","Sat"), 
                   overlayGroups = c("map_and_data_as_sp"))

```

Image if the map:

![Image of Interactive Map](Images/Interactive_Map.png)




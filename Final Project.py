{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "c094d0d4-8b14-46c4-a9e7-a53621162050",
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "f=open('C:/Users/yasha/OneDrive/Documents/Yahsaswini/Big data procs/Final Project/daily_aqi_by_county_2000.csv','r')\n",
    "reader = csv.reader(f)\n",
    "f2 = open('Daily_aqi_data.csv','w')\n",
    "writer = csv.writer(f2,delimiter=',',lineterminator='\\n')\n",
    "n=0\n",
    "l=[\"State Name\",\"county Name\",\"State Code\",\"County Code\",\"Date\",\"AQI\",\"Category\",\"Defining Parameter\",\"Defining Site\",\"Number of Sites Reporting\"]\n",
    "writer.writerow(l)\n",
    "for row in reader:\n",
    "    if row[0] == 'New York':\n",
    "        writer.writerow(row)\n",
    "n+= 1\n",
    "\n",
    "f.close\n",
    "f2.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "bff0d66d-5c3f-430f-b192-1b637c108632",
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv \n",
    "\n",
    "f1=open('C:/Users/yasha/OneDrive/Documents/Yahsaswini/Big data procs/Final Project/daily_aqi_by_county_2001.csv','r')\n",
    "reader1 = csv.reader(f1)\n",
    "f2=open('Daily_aqi_data.csv','a') \n",
    "writer = csv.writer(f2)\n",
    "n=0\n",
    "for row in reader1:\n",
    "    if row[0] == 'New York':\n",
    "        writer.writerow(row)\n",
    "n+=1\n",
    "    \n",
    "f1.close\n",
    "f2.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "757f8adb-fe13-49c3-a755-6531d0f5ff05",
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv \n",
    "\n",
    "f3=open('C:/Users/yasha/OneDrive/Documents/Yahsaswini/Big data procs/Final Project/daily_aqi_by_county_2002.csv','r')\n",
    "reader2= csv.reader(f3)\n",
    "f2=open('Daily_aqi_data.csv','a') \n",
    "writer = csv.writer(f2)\n",
    "n=0\n",
    "for row in reader2:\n",
    "    if row[0] == 'New York':\n",
    "        writer.writerow(row)\n",
    "n+=1\n",
    "    \n",
    "f3.close\n",
    "f2.close()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "35a4d8d3-7a01-4aa6-ae1e-29377700cdd4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv \n",
    "\n",
    "\n",
    "f4=open('C:/Users/yasha/OneDrive/Documents/Yahsaswini/Big data procs/Final Project/daily_aqi_by_county_2003.csv','r')\n",
    "reader3 = csv.reader(f4)\n",
    "f2=open('Daily_aqi_data.csv','a') \n",
    "writer = csv.writer(f2)\n",
    "n=0\n",
    "for row in reader3:\n",
    "    if row[0] == 'New York':\n",
    "        writer.writerow(row)\n",
    "n+=1\n",
    "    \n",
    "f4.close\n",
    "f2.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f72a9714-dbf6-4648-8199-05669e2aa929",
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv \n",
    "\n",
    "f5=open('C:/Users/yasha/OneDrive/Documents/Yahsaswini/Big data procs/Final Project/daily_aqi_by_county_2004.csv','r')\n",
    "reader4 = csv.reader(f5)\n",
    "f2=open('Daily_aqi_data.csv','a') \n",
    "writer = csv.writer(f2)\n",
    "n=0\n",
    "for row in reader4:\n",
    "    if row[0] == 'New York':\n",
    "        writer.writerow(row)\n",
    "n+=1\n",
    "    \n",
    "f5.close\n",
    "f2.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "8f631b87-a903-48c3-ad27-88e977f45626",
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv \n",
    "\n",
    "f6=open('C:/Users/yasha/OneDrive/Documents/Yahsaswini/Big data procs/Final Project/daily_aqi_by_county_2005.csv','r')\n",
    "reader5 = csv.reader(f6)\n",
    "f2=open('Daily_aqi_data.csv','a') \n",
    "writer = csv.writer(f2)\n",
    "n=0\n",
    "for row in reader5:\n",
    "    if row[0] == 'New York':\n",
    "        writer.writerow(row)\n",
    "n+=1\n",
    "    \n",
    "f6.close\n",
    "f2.close()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "8a126277-11f0-4b62-9f85-189ec6f71025",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Good\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "\n",
    "Bird_data = open('C:/Users/yasha/OneDrive/Documents/Yahsaswini/Big data procs/Final Project/Breeding_Bird_Atlas__Second_Edition__2000-2005.csv', 'r')\n",
    "reader6 = csv.reader(Bird_data)\n",
    "\n",
    "AQI = open('Daily_aqi_data.csv','r')\n",
    "reader7 =csv.reader(AQI)\n",
    "\n",
    "AQI_lookup={}\n",
    "n=0\n",
    "for row2 in reader7:\n",
    "    if len(row2)>=6:\n",
    "        \n",
    "        if row2[6] == \"Good\" or row2[6] == \"Very Unhealthy\":\n",
    "            \n",
    "            Date_AQI=row2[4]\n",
    "            County_AQI=row2[1].lower().replace(\".\",\"\")\n",
    "            Air_Quality=row2[6]\n",
    "            k=Date_AQI+'_'+County_AQI\n",
    "            AQI_lookup[k]=Air_Quality\n",
    "            \n",
    "        n+=1\n",
    "    \n",
    "print(AQI_lookup['2000-04-18_st lawrence'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "382083b2-a502-4fe1-b953-79acda874263",
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime,csv\n",
    "\n",
    "header=[\"Date\",\"County\",\"Name of Bird\",\"Breeding_Behavior\",\"Breeding_Status\",\"AirQuality\"]\n",
    "f3=open('Birds_behaviour.csv', 'w',newline='') \n",
    "writer = csv.writer(f3)\n",
    "writer.writerow(header)\n",
    "n=0\n",
    "for row1 in reader6:\n",
    "    Birds_behaviour=[]\n",
    "    #print(row1)\n",
    "    if row1[6] == \"Threatened\":\n",
    "        if \"//\" not in row1[10]:\n",
    "            Date_Bird=row1[10].split('/')\n",
    "            dto=datetime.datetime.strptime(Date_Bird[0].zfill(2)+Date_Bird[1].zfill(2)+Date_Bird[2],'%m%d%Y')\n",
    "            dts=datetime.datetime.strftime(dto,'%Y-%m-%d')\n",
    "            County_Bird=row1[3].lower()\n",
    "            Name_Bird=row1[4]\n",
    "            Breeding_Behavior=row1[9]\n",
    "            Breeding_Status=row1[11]\n",
    "            k=dts+'_'+County_Bird\n",
    "            #print(k)\n",
    "        \n",
    "        if k in AQI_lookup:\n",
    "            n+=1\n",
    "            Birds_behaviour.append(k.split('_')[0])\n",
    "            Birds_behaviour.append(k.split('_')[1])\n",
    "            Birds_behaviour.append(Name_Bird)\n",
    "            Birds_behaviour.append(Breeding_Behavior)#Breeding_Behavior\n",
    "            Birds_behaviour.append(Breeding_Status)\n",
    "            Birds_behaviour.append(AQI_lookup[k])#AQI_lookup[k]\n",
    "            \n",
    "            #print(Birds_behaviour)\n",
    "            writer.writerow(Birds_behaviour)\n",
    "               \n",
    "                \n",
    "                      \n",
    "            \n",
    "                \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3bbe26ea-a4d2-493c-bcbe-5cca58a01c0c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f027ba57-6ca6-4480-9314-cf5fe75b8f2f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

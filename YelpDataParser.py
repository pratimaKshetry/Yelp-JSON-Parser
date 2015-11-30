/************************
Original Author: Pratima Kshetry
This code parses the yelp available in json format to a regular csv format. 
The dataset is available at: https://www.yelp.com/dataset_challenge/dataset 
************************************************************************************************/

import json

''' Yelp tip dataset '''
json_data=open('yelp_tip.txt')
data = json.load(json_data)
count = 0
fcsv=open('yelp_tips.csv','w')
str1='user_id,text,business_id,likes,date,type\n'

fcsv.write(str1)
while (count < 475):
   str1=data["tip"][count]["user_id"]
   str1=str1.replace(",","")
   
   str2=data["tip"][count]["text"]
   str2=str2.replace(",","")
   str1=str1+','+ str(str2)

      
   str2=data["tip"][count]["business_id"]
   str1=str1+','+ str2

   str2=data["tip"][count]["likes"]
   str1=str1+','+ str(str2) 

   str2=data["tip"][count]["date"]
   str1=str1+','+ str(str2)

   str2=data["tip"][count]["type"]
   str2=str2.replace(",","")
   str1=str1+','+(str2)

    
   
   newstr =str1.replace("\n", "")
   str2=newstr+'\n'
   print(str2) 

      
   fcsv.write(str2)
   count = count + 1
json_data.close()
fcsv.close()


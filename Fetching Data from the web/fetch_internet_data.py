import urllib.request as url
import json
from html.parser import HTMLParser
import xml.dom.minidom

#Example
def read_data():
    wUrl=url.urlopen('https://www.google.com')
    print('you can read from this website') if wUrl.getcode()==200 else print('you cannot read from this website') #200 is a http code
    htmldata=wUrl.read()
    print(htmldata)
#read_data()

#############################################
#############################################
#############################################
#############################################

#FETCHING FROM JSON
def use_json(data):
    JSon=json.loads(data)
    #get the title
    if 'title' in JSon['metadata']:
        print(JSon['metadata']['title'])
    c = JSon['metadata']['count']
    print(c,'earthquakes was found')
    #print in which place the events was occured
    for i in JSon['features']:
        print(i['properties']['place'])
            
    #print out all the mag greater or equal to 4
    for i in JSon['features']:
        if(i['properties']['mag']>=4.0):
            print('{0:.2f}'.format(i['properties']['mag']))

    #print all the events where at least 1 person reported feeling something
    for i in JSon['features']:
        felt=i['properties']['felt']
        if felt!=None:
            if(felt>=1):
                print('Event felt: ',i['properties']['place'])
                print('Was felt by :',i['properties']['felt'],' Persons')

    #print the point longitude, latitude and the depth and its ID
    for i in JSon['features']:
        x,y,z=i['geometry']['coordinates']
        id=i['id']
        print(id,x,y,z)

    #print all the events place where the latitude greater than 35.0
    for i in JSon['features']:
        x,y,z=i['geometry']['coordinates']
        if y>35.0:
            print(i['properties']['place'])
def usgs():
    wUrl=url.urlopen('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson')
    if(wUrl.getcode()==200):
        htmlData=wUrl.read()
        use_json(htmlData)
    else:
        raise TypeError('You cannot acces the website')

#usgs()

####################################
####################################
####################################
#USING XML

def use_xml():
    #load the xml file and parse it ==> creating an object we can manipulate
    my_data=xml.dom.minidom.parse('myXML.xml')
    #print out the node and the name of the first child tag
    print(my_data.nodeName)
    print(my_data.firstChild.tagName)
    #get the skill tag name
    skill=my_data.getElementsByTagName('skill')
    print('%d skills'%skill.length)
    for i in skill:
        print(i.getAttribute('name'))
    #get the name and last name
    name=my_data.getElementsByTagName('firstname')[0].childNodes[0].nodeValue
    lname=my_data.getElementsByTagName('lastname')[0].childNodes[0].nodeValue
    print(name,lname)
    #get the phone numbers
    phonenbr=my_data.getElementsByTagName('phonenbr')
    for i in phonenbr:
        print(i.getAttribute('name'))
    #add a new skill into the xml doc
    newSkill=my_data.createElement('skill')
    newSkill.setAttribute('name','C#')
    my_data.firstChild.appendChild(newSkill)
    skill=my_data.getElementsByTagName('skill')
    print('%d skills'%skill.length)
    for i in skill:
        print(i.getAttribute('name'))
use_xml()
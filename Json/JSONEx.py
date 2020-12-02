import json
from json import JSONEncoder

#Part 1
my_data={'name':'Max','age':15,'hasChildren':True,'job':['Writer','Programmer']}
encodeJSON=json.dumps(my_data,indent=4) #encode from dict to json
print(encodeJSON)
#with open('info.json','w') as file: #write (fill) to info.json some data
    #json.dump(my_data,file,indent=4)

#    file.close()


decodeJSON=json.loads(encodeJSON) #decode from json to dict

with open('info.json','r') as f: #load from info.json some data
    dJson = json.load(f)
    print(dJson)
    f.close()


#manipulate custom objects
#Part 2
class Music:
    def __init__(self,title,singer,genre,appearance):
        self.title=title
        self.singer=singer
        self.genre=genre
        self.appearance=appearance

def encode_Music(obj):
    if isinstance(obj,Music):
        return {'Singer':obj.singer, 'Title':obj.title, 'Genre':obj.genre, 'Date Of Appearance':obj.appearance,obj.__class__.__name__:True}
    return TypeError('Object of type Music is not JSON serializable')
music=Music('Mi gente','J Balvin','Dance',2017)
musicJson = json.dumps(music,indent=4,separators=(', ','= '),default=encode_Music)
mJson=json.dumps(music,default=encode_Music)
ToJson=json.loads(mJson) #you have to convert to a JSON format because the class returns a string
with open('music.json','w') as file:
    json.dump(ToJson,file,indent=4,separators=(', ','= '))
    file.close()
print(musicJson)

# we can now use the default class provided by JSON to encode the our data
class Music_encoder(JSONEncoder): #we've overrided the default method
    def default(self,obj):
        if isinstance(obj,Music):
            return {'Singer':obj.singer, 'Title':obj.title, 'Genre':obj.genre, 'Date Of Appearance':obj.appearance,obj.__class__.__name__:True}
        return JSONEncoder.default(self,obj)
mJson1=json.dumps(music,cls=Music_encoder)
ToJson1=json.loads(mJson1)
with open('music.json','a') as f:
    json.dump(ToJson1,f,indent=4)
    f.close()

###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################

#Access the nested key ‘salary’ from the company.json file
with open('company.json')as f:
    data=json.load(f) #the type of data is a dictionary
    print(data['company']['employee']['payble']['salary'])
    f.close()

#Convert the following Vehicle Object into JSON
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

veh = Vehicle("Toyota Rav4", "2.5L", 32000)
def convert_vehicle(obj):
    if isinstance(obj,Vehicle):
        return {'Mark':obj.name,'Engine':obj.engine,'Price':obj.price,obj.__class__.__name__ : True}
    return TypeError('Object of type Music is not JSON serializable')
my_str=json.dumps(veh,default=convert_vehicle)
TJson = json.loads(my_str)
with open('Vehicle.json','w') as f:
    json.dump(TJson,f,indent=4)
    f.close()
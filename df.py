from webbrowser import get
import pymongo
from pymongo import MongoClient

class ReprDict(dict):
    def __repr__(self):
        return "\n".join(f"{k}: {v}" for k, v in self.items())
client = MongoClient("mongodb+srv://noema:658Vobisi@check.8n3yvam.mongodb.net/?retryWrites=true&w=majority")
db=client["Check"]
manhwa_data = db['manhwa']
manhwa_chapters = db['ex']



def register_user(user_id):
    new = db["users"]
    if  new.count_documents({'user_id': f"{user_id}"}) == 0:
       a = new.insert_one({"user_id" : f"{user_id}", 'selected_manhwa': 'zero', 'selected_chapter':1})


def selected_manhwa(manhwa_name, user_id):
    new = db["users"]
    print(user_id)
    new.update_one({"user_id" : f"{user_id}"}, {"$set":{"selected_manhwa":manhwa_name}})
    #new.update({'user_id': user_id}, {"$set": { "selected_manhwa": manhwa_name }} )

def selected_chapter(user_id):
    new = db['users']
    users = list(new.find({"user_id" : f"{user_id}"})) 
    
    return [user['selected_chapter'] for user in users]


# find по всем манхвам -> берем список жанров у манхвы и делаеим сравнение -> если совпадает добавляем.
def available_genres():
    new = db['genres']
    genres = list(new.find({}))
    return [user['genre'] for user in genres]

def available_manhwa():
    new = db['manhwa']
    manhwa = list(new.find({}))
    return [user['name'] for user in manhwa]

print(available_genres())

def add_genre(genres):
    new = db['genres']
    genre_list = genres.split(', ')
    i=0
    while i<len(genre_list):
        genre = genre_list[i]
        if  new.count_documents({'genre': genre}) == 0:
            new.insert_one({'genre': genre})
        i+=1

def find_manhwa_genre(genre_name):
    genre_db = db['genres']
    manhwa_db = db['manhwa']
    genres = list(genre_db.find({}))
    accepted_manhwa = []
    manhwa_genres = list(manhwa_db.find({})) # передавать в какой то последовательности список манхв
    #print('\n\n\n\n\n\n\n\n\n\n\n',  manhwa_genres)
    genre_list = [user['genre'] for user in genres]
    #manhwa_genre_list = [(manhwa_genres['genres'])]
    manhwa_genre_list = [user['genres'] for user in manhwa_genres]
    all_manhwa =  [user['name'] for user in manhwa_genres]
    
    k=0
    print(all_manhwa)
    while k<len(all_manhwa):
        manhwa_genres = list(manhwa_db.find({'name':all_manhwa[k]}))
        
        manhwa_name = []
        for user in manhwa_genres:
            manhwa_name.append(user['name'])

        #print('\n\n\n\n\n\n,dmthrsngtbfs',manhwa_name)
        #manhwa_name = [user['name'] for user in manhwa_genres]
        #manhwa_genre_list = manhwa_genres[0]
        nwe = []
        for user in manhwa_genres:
            nwe.append(user['genres'])
        ab = (str(nwe).replace('[', '').replace(']', '').replace(', ', ' ').replace("'", ''))
        nwe = ab.split()
       #print(ab[0])
        print('\n\n\n\n\n\n,fvdfsdfdfvdf', nwe)
        print(nwe[0])
        #print(len(list(ab)))
        #manhwa_genr)e_list = user['genres'] for user in manhwa_genres]
        #manhwa_genre_list = str(manhwa_genre_list).split(', ')
        #print('\n\n\n\n\n\n\n\n\n\n\n',  manhwa_genre_list, manhwa_name)
        k+=1
        i=0
        #print('\n\n\n', manhwa_genre_list) 
        while i<len(nwe):
            print('\n\n\n', nwe[i]) 
            if nwe[i] == genre_name:
                print('1111')
                manhwa_name = str(manhwa_name).replace("['", "").replace("']", "")
                accepted_manhwa.append((manhwa_name))
            i+=1
        

    return accepted_manhwa

            #if manhwa_genre_list[i] == genre_name:
               # accepted_manhwa.append()
    
    #print('\n\n\n\n\n\n\n\n\n\n\n', genre_list, manhwa_genre_list)
    
    
# сравниваю жанр манхвы со всеми жанрами.
ik = find_manhwa_genre('один')
print(ik)
#print('\n\n\n\n\n\n\n\n\n\n\n',find_manhwa_genre('один'))








def update_selected_chapter(user_id, selected_chapter):
    new = db['users']
    new.update_one({"user_id" : f"{user_id}"}, {"$set":{"selected_chapter":selected_chapter}})
    

def get_chapters(manhwa_name, chapter_number): # сбитая нумерация глав + manhwa_name не используется. по manhwa_name найти object id и по нему идти в таблицу.
    manhwa_data = db['manhwa']
    manhwa_id = manhwa_data.find_one({"name": manhwa_name[0]},{'_id':1})
   
    manhwa_id = str(manhwa_id).replace("'", '').replace("{", '').replace("}", '').replace("_id: ", '') # по manhwa_name
    print(manhwa_name)
    print(manhwa_id)
    buffer_data = db[manhwa_id]
    chapter_id = buffer_data.find({'chapter_number': chapter_number})
    chapter_id = [user['chapter_id'] for user in chapter_id]
    print(chapter_id)
    return chapter_id






'''




    manhwa_data = db['manhwa']
    
    photo =  manhwa_data.find_one({'name': manhwa_name }, { '_id':1})
    photo_new = str(photo).replace('{', '').replace('}', '').replace("'", '').replace(":", '').replace("_id", '').replace(" ", '')
    
    buffer_data = db[photo_new]
    photo =  list(buffer_data.find({'chapter_number': chapter_number}))
    #print([user['chapter_id'] for user in photo])
    #return [user['chapter_id'] for user in photo]
    chapter_id = buffer_data.find_one({'chapter_number': chapter_number}, {'chapter_id':1, '_id':0})

    photo_new = str(chapter_id).replace('{', '').replace('}', '').replace("'", '').replace(":", '').replace("chapter_id", '').replace(" ", '')
    return photo_new
    '''





def get_all_users_identificators(): 
        new = db['manhwa']
        users = list(new.find())
        return [user['_id'] for user in users]



def get_selected_manhwa(user_id):
    new = db['users']
    photo =  list(new.find({'user_id': f"{user_id}" }))
    return [user['selected_manhwa'] for user in photo]
    photo = new.find_one({'user_id': f"{user_id}" }, {'selected_manhwa':1, '_id':0})
    photo_new = str(photo).replace('{', '').replace('}', '').replace("'", '').replace(":", '').replace("selected_manhwa", '').replace(" ", '')
    return photo_new

def add_chapters_to_storage(name, chapter_number, chapter_id): #либо хреначить по манхва ид либо по нейму  
    manhwa_chapters = db[f"{name}"]
    manhwa_chapters.insert_one({
        'chapter_number': chapter_number,
        'chapter_id': chapter_id
    })

def add_to_storage( name, picture,description, number_of_chapters,release_year,genres,manhwa_state):
        manhwa_data.insert_one({
            'name': name,
            'picture': picture,
            'description': description,
            'number_of_chapters': number_of_chapters,
            'release_year': release_year,
            'genres': genres,
            'manhwa_state': manhwa_state,
        })


def find_document(collection, elements):
        users = collection.find(elements)
        return [user['name'] for user in users]
    
def manhwa_id(collection, elements):
        users = collection.find(elements)
        return [user['_id'] for user in users]

def find_document_id(collection, elements, elements_2, multiple=True):
    """ Function to retrieve single or multiple documents from a provided
    Collection using a dictionary containing a document's elements.
    """
    if multiple:
        results = collection.find(elements, elements_2)
        print(results)
        return [r for r in results]
        
    else:
            return collection.find_one(elements, elements_2)
            #return collection.find_one(elements)




def get_photo(manhwa_name):
    manhwa_data = db['manhwa']
    #photo =  manhwa_data.find_one({'name': manhwa_name }, {'picture':1, '_id':0})
    users = list(manhwa_data.find({"name" : manhwa_name })) 
    print([user['picture'] for user in users])
    return [user['picture'] for user in users]

    photo_new = str(photo).replace('{', '').replace('}', '').replace("'", '').replace(":", '').replace("picture", '').replace(" ", '')
    #return photo_new
def get_description(manhwa_name):
    manhwa_data = db['manhwa']
    photo =  list(manhwa_data.find({'name': manhwa_name }))
    return [user['description'] for user in photo]
    #return photo_new

def get_number_of_chap(manhwa_name):
    manhwa_data = db['manhwa']
    photo =  list(manhwa_data.find({'name': manhwa_name }))
    return [user['number_of_chapters'] for user in photo]
    photo =  manhwa_data.find_one({'name': manhwa_name }, {'number_of_chapters':1, '_id':0})
    photo_new = str(photo).replace('{', '').replace('}', '').replace("'", '').replace(":", '').replace("number_of_chapters", '').replace(" ", '')
    return photo_new

def get_release_year(manhwa_name):
    manhwa_data = db['manhwa']
    photo =  list(manhwa_data.find({'name': manhwa_name }))
    return [user['release_year'] for user in photo]
    photo =  manhwa_data.find_one({'name': manhwa_name }, {'release_year':1, '_id':0})
    photo_new = str(photo).replace('{', '').replace('}', '').replace("'", '').replace(":", '').replace("release_year", '').replace(" ", '')
    return photo_new


def get_manhwa_state(manhwa_name):
    manhwa_data = db['manhwa']
    photo =  list(manhwa_data.find({'name': manhwa_name }))
    return [user['manhwa_state'] for user in photo]
    photo =  manhwa_data.find_one({'name': manhwa_name }, {'manhwa_state':1, '_id':0})
    photo_new = str(photo).replace('{', '').replace('}', '').replace("'", '').replace(":", '').replace("manhwa_state", '').replace(" ", '')
    return photo_new

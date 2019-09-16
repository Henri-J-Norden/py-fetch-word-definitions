import requests, json

class Word_DB:
    from oxford_dicts_config import Config
    
    # config
    c = Config()

    # oxford dictionary api values
    url_base = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/'  + c.language + '/'
    
    # value initialization (do not change)
    db_filename = None
    db = None
    changed = False
    

    def __init__(self, db_filename):
        self.db_filename = db_filename
        if self.c.debug: print("Reading DB from file '" + self.db_filename + "'...")

        try:
            with open(self.db_filename) as f:
                self.db = json.load(f)
        except:
            print("DB file not found. Continuing with blank DB...")
            self.db = {}


    def get(self, word):
        if self.db is None: raise ValueError("DB not initialized")

        if word in self.db:
            if self.c.debug: print("Accessing word '{}'...".format(word))
            return self.db[word]
        else:
            return self.__get_request(word)


    def __get_request(self, word):
        url = self.url_base + word.lower()
        if self.c.debug: print("GET Request to '" + url + "'...")

        r = requests.get(url, headers = {'app_id' : self.c.app_id, 'app_key' : self.c.app_key})
        data = r.json()
        if "error" in data:
            print("No results found for '{}'! Check the spelling.".format(word))
        else:
            self.db[word] = data

            if self.c.save_after_every_req: self.save()
            else: self.changed = True

        return data
    

    def save(self):
        if self.c.app_caching:
            if self.c.debug: print("Saving DB...")
            if self.db is None: raise ValueError("DB not initialized")
            
            with open(self.db_filename, "w") as f:
                f.write(json.dumps(self.db, sort_keys=True, indent=4))
                
        else:
            if self.c.debug: print("DB saving disabled (see config value 'app_caching')!")

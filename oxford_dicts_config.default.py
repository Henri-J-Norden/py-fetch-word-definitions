
class Config:
    app_id = '<your app id here>' 
    app_key = '<your app key here>'
    # Caching can be enabled to create a local DB to avoid re-fetching the same words when a new output is required
    # [!!!] Caching may only be enabled in compliance with Oxford Dictionaries' API TOS (https://developer.oxforddictionaries.com/api-terms-and-conditions)
    # [!!!]     Please note that at time of writing (2019-09-16) the TOS only allows caching for Enterprise licenses (see TOS 6. Usage Requirements and Restrictions)
    app_caching = False 
    
    # languages other than 'en' have not been tested
    language = 'en'
    
    # if caching is allowed (app_caching = True):
    #    if save_after_every_req is True, the DB is saved after every new word is fetched
    #     if save_after_every_req is False, the DB is saved when all words have been parsed and new words were fetched during the operation
    #        (meaning that if no new words were fetched and there is nothing to save, the DB file does not get written to)
    save_after_every_req = True
    # print info about the process
    debug = True

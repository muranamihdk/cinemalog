import requests

# URL for debugging
# - https://itunes.apple.com/search?country=jp&media=movie&term=world
# - https://itunes.apple.com/lookup?country=jp&id=399966400

## iTunes Store Search API Class
class iTunesStoreAPI():
    def __init__(self):
        self.host = 'itunes.apple.com'
        self.search_path = '/search'    
        self.lookup_path = '/lookup'
        
    def request(self, opt, path):
        url = "https://{}{}".format(self.host, path)
        r = requests.get(url, opt)
        return r.json()


    def search(self, media, entity, keyword):
        # Parameter
        opt = {}
        opt['term'] = keyword
        opt['country'] = 'JP'
        opt['media'] = media
        opt['entity'] = entity
        opt['lang'] = 'ja_jp'
        return self.request(opt, self.search_path)

    def lookup(self, item_id):
        opt = {}
        opt['id'] = item_id
        opt['country'] = 'JP'
        return self.request(opt, self.lookup_path)


def search_sample_movie():
    import pprint
    itunes = iTunesStoreAPI()
    keyword = 'エデンの東'
    media = 'movie'
    entity = 'movie'  #movieArtist, movie
    results = itunes.search(media, entity, keyword)
    pprint.pprint(results)

def search_sample_music():
    import pprint
    itunes = iTunesStoreAPI()
    keyword = '未来のミュージアム'
    media = 'music'
    entity = 'song'  #musicArtist, musicTrack, album, musicVideo, mix, song
    results = itunes.search(media, entity, keyword)
    pprint.pprint(results)

if __name__ == '__main__':
    search_sample_movie()
    #search_sample_music()

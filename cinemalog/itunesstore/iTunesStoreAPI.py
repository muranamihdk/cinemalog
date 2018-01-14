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
        r = requests.get(url, opt, verify=False)
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



def search_movie(keyword):
    itunes = iTunesStoreAPI()
    media = 'movie'
    entity = 'movie'  #movieArtist, movie
    results = itunes.search(media, entity, keyword)
    result_count = results['resultCount']
    movies = results['results']
    return movies


def search_music(keyword):
    itunes = iTunesStoreAPI()
    media = 'music'
    entity = 'song'  #musicArtist, musicTrack, album, musicVideo, mix, song
    results = itunes.search(media, entity, keyword)
    result_count = results['resultCount']
    musics = results['results']
    return musics

def lookup(item_id):
    itunes = iTunesStoreAPI()
    results = itunes.lookup(item_id)
    result_count = results['resultCount']
    result = results['results'][0]
    return result



if __name__ == '__main__':
    import pprint
    keyword = 'エデンの東'
    results = search_movie(keyword)
    #keyword = '未来のミュージアム'
    #results = search_music(keyword)
    pprint.pprint(results)


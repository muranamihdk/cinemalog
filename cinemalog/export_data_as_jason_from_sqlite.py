import os
import json
import sqlite3


class SQLite(object):
    def __init__(self, db_path):
        self.db_path = db_path
    
    def fetch_all(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT id, date, track_id, itunes_url, img_url30, img_url60, img_url100, title, director, genre, release, runtime, score, review FROM cinemalog ORDER BY date ASC, id ASC")
        result = []
        for item in c:
            movie_info = {}
            #movie_info['id'] = item[0]
            movie_info['date'] = item[1]
            movie_info['track_id'] = item[2]
            movie_info['itunes_url'] = item[3]
            movie_info['img_url30'] = item[4]
            movie_info['img_url60'] = item[5]
            movie_info['img_url100'] = item[6]
            movie_info['title'] = item[7]
            movie_info['director'] = item[8]
            movie_info['genre'] = item[9]
            movie_info['release'] = item[10]
            movie_info['runtime'] = item[11]
            movie_info['score'] = item[12]
            movie_info['review'] = item[13]
            result.append({'model':'logbook.Movie', 'fields':movie_info})
        c.close()
        conn.close()
        return result


db_path = os.path.join(os.path.dirname(__file__), 'cinemalog.db')
sqlite = SQLite(db_path)
movies = sqlite.fetch_all()

with open('cinemalog.json', mode='wt', encoding='utf-8', errors='strict') as f:
    f.write(json.dumps(movies, ensure_ascii=False))


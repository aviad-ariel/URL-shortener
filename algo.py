from datetime import date

BASE = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
BASE_SIZE = 62
EXPIRATION_LENGTH = 2

def url_shorter(url, db):
    creation = date.today()
    expiration = add_years_to_date(creation, EXPIRATION_LENGTH)
    db.execute("""INSERT INTO urls(hash_id, url, creation, expiration) VALUES(?,?,?,?)""", ("", url['url'], creation, expiration))
    db.execute("""SELECT last_insert_rowid()""")
    id_ = db.fetchone()[0]
    hash_id = convert_base10_to_base62(id_)
    db.execute("""UPDATE urls SET hash_id = ? WHERE id = ?""", (hash_id, id_))
    return hash_id

def decode_url(hash_id, db):
    db.execute("""SELECT * FROM urls WHERE hash_id = ?""", (hash_id,))
    url = db.fetchone()
    if url:
        return url[2]
    else:
        return None 

def convert_base10_to_base62(num):
    res = [] 
    while(num):
        num, reminder = divmod(num, BASE_SIZE)
        res.append(BASE[reminder])
    res.reverse()
    return ''.join(res)

def add_years_to_date(date_object, years_to_add):
    return date_object.replace(year = date_object.year + years_to_add)

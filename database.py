import sqlite3

connection = sqlite3.connect("songs.db")

cursor = connection.cursor()

cursor.execute("create table songs (song text, artist text, album text)")

song_list = [
    ("Ne Var Ne Yok",	"Büyük Ev Ablukada",	"Full Faça"),
    ("Wake Me Up When September Ends",	"Green Day",	"American Idiot"),
    ("The Adults Are Talking",	"The Strokes",	"The New Abnormal"),
    ("Veridis Quo",	"Daft Punk",	"Discovery"),
    ("Estranged",	"Guns N Roses",	"Use Your Illusion II"),
    ("Supermassive Black Hole",	"Muse",	"Black Holes and Revelations"),
    ("One More Light",	"Linkin Park",	"One More Light"),
    ("Düşünme Kaybolursun",	"No Land",	"Aramızda"),
    ("Ali Desidero",	"MFÖ",	"Geldiler"),
    ("Toz",	"Jakuzi",	"Hata Payı")
]



cursor.executemany("insert into songs values(?,?,?)", song_list)
connection.commit()
connection.close()
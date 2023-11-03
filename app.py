from flask import Flask, render_template, request, url_for, redirect, g,session
import sqlite3

app = Flask(__name__)
app.secret_key = "Breakfast_In_Pharmacy51"

@app.route('/',methods=["POST", "GET"])
def index():
    session["all_songs"], session["playlist"]  = get_db()
    return render_template("index.html", all_songs = session["all_songs"],
                                        my_playlist = session["playlist"])

@app.route('/add_song',methods=["post"])
def add_songs():
    session["playlist"].append(request.form["select_song"])
    session.modified = True
    return render_template("index.html", all_songs = session["all_songs"],
                                        my_playlist = session["playlist"])
#404 error                                        
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 405
#505 error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("505.html"), 500

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('songs.db')
        cursor = db.cursor()
        cursor.execute("select * from songs")
        all_songs = cursor.fetchall()
        
        playlist = []
    return all_songs, playlist
    
if __name__ == '__main__':
    app.run()
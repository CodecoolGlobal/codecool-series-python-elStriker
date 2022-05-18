from flask import Flask, render_template, url_for, request, redirect, session, jsonify
from data import queries
import math
from dotenv import load_dotenv

load_dotenv()
app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/api/get-most-rated-shows')
def most_rated_shows():
    return jsonify(queries.get_fifteen_most_rated_shows())


@app.route('/api/get-actors-detail')
def get_actors_detail():
    return jsonify(queries.get_actor_detail())


@app.route('/api/get-genres')
def get_genres():
    return jsonify(queries.get_genres_by_limit())


@app.route('/api/get-ordered-shows/<order>')
def get_shows_by_order(order):
    return jsonify(queries.get_shows_by_episode_count(order))


@app.route('/api/get-genres-detail/<int:genre_id>')
def get_genre_details(genre_id):
    return jsonify(queries.get_genre_by_limit(genre_id))


@app.route('/actors')
@app.route('/actors/<name>')
def display_hundred_actor():
    return render_template('list-actors.html')


@app.route('/shows/genres')
def genre():
    return render_template('genres.html')


@app.route('/shows/most-rated')
def shows():
    return render_template('most-rated-shows.html')


@app.route('/show/<int:id>')
def show_detail(id):
    show_details = queries.get_show(id)
    seasons = queries.get_seasons_by_show_id(id)
    return render_template('show-details.html', details=show_details, seasons=seasons)


@app.route('/ordered-shows')
def render_ordered_shows():
    return render_template('ordered_shows.html')


@app.route('/birthday-actors')
def display_birthday_actors():
    return render_template('birthday-actors.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    pass


def main():
    app.run(debug=True, port=5001)


if __name__ == '__main__':
    main()

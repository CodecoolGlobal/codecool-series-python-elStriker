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


@app.route('/shows/most-rated')
def shows():
    return render_template('most-rated-shows.html')


@app.route('/show/<int:id>')
def show_detail(id):
    show_details = queries.get_show(id)
    seasons = queries.get_seasons_by_show_id(id)
    return render_template('show-details.html', details=show_details, seasons=seasons)


def main():
    app.run(debug=True, port=5001)


if __name__ == '__main__':
    main()

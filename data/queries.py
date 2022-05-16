from data import data_manager as dm
from psycopg import sql

def get_shows():
    return dm.execute_select('SELECT id, title FROM shows;')


def get_fifteen_most_rated_shows():
    return dm.execute_select(sql.SQL("""
        SELECT shows.id,
    shows.title,
    DATE_PART('year', shows.year::date) as year,
    shows.runtime,
    ROUND(shows.rating::numeric, 1) as rating,
    string_agg(genres.name, ','
        ORDER BY genres.name ASC) genres,
    shows.trailer,
    shows.homepage
    FROM shows
         JOIN show_genres on shows.id = show_genres.show_id
         JOIN genres on genres.id = show_genres.genre_id
    GROUP BY shows.id
    ORDER BY rating DESC
    """))


def get_show(show_id):
    return dm.execute_select(sql.SQL(
        """
        SELECT shows.id,
        shows.title,
       shows.runtime,
       shows.trailer,
       ROUND(shows.rating::numeric, 1) rating,
       string_agg(DISTINCT genres.name, ','
                  ORDER BY genres.name ASC) genres,
       shows.overview,
       array_to_string((array_agg(DISTINCT actors.name))[1:3], ', ') Actors
        FROM shows
         JOIN show_characters on shows.id = show_characters.show_id
         JOIN show_genres on shows.id = show_genres.show_id
         JOIN genres on genres.id = show_genres.genre_id
         JOIN actors on actors.id = show_characters.actor_id
        WHERE shows.id = {show_id}
        GROUP BY shows.id
    """).format(show_id=sql.Literal(show_id)))


def get_seasons_by_show_id(show_id):
    return dm.execute_select(sql.SQL("""
    SELECT seasons.season_number, seasons.title, COALESCE(seasons.overview, '') as overview
    FROM seasons
    JOIN shows on shows.id = seasons.show_id
    WHERE shows.id = {show_id}
    GROUP BY shows.id, seasons.id;
    """).format(show_id=sql.Literal(show_id)))

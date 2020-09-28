
from api import db
from api.resources.movie_model import Movie, Comments


def add_movie(title, url):
    movie = Movie(
        title=title,
        url=url
    )
    db.session.add(movie)
    db.session.commit()
    return movie

from datetime import datetime

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
):
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: datetime = None):
    session_queryset = MovieSession.objects.all()
    if session_date:
        session_queryset = session_queryset.filter(
            show_time__date=session_date
        )

    return session_queryset


def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
):
    session_queryset = MovieSession.objects.filter(id=session_id)

    if show_time:
        session_queryset.update(show_time=show_time)

    if movie_id:
        session_queryset.update(movie_id=movie_id)

    if cinema_hall_id:
        session_queryset.update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int):
    MovieSession.objects.get(id=session_id).delete()

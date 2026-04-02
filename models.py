from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Benutzer(db.Model):
    __tablename__ = "benutzer"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)

    filme = db.relationship(
        "Film",
        backref="benutzer",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Benutzer {self.name}>"


class Film(db.Model):
    __tablename__ = "film"

    id = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.String(255), nullable=False)
    director = db.Column(db.String(255))
    jahr = db.Column(db.String(10))
    imdb_id = db.Column(db.String(20))
    poster_url = db.Column(db.String(500))

    benutzer_id = db.Column(
        db.Integer,
        db.ForeignKey("benutzer.id"),
        nullable=False
    )

    def __repr__(self) -> str:
        return f"<Film {self.titel}>"

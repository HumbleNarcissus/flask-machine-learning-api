from api import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(250), nullable=True)
    comments = db.relationship('Comments', backref='comment', lazy=True)

    def __init__(self, title):
        self.title = title

    def json(self):
        # return object in json format
        return {
            'id': self.id,
            'title': self.title,
            'comments': [comment.json() for comment in self.comments]
        }
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(100), nullable=True)
    positive = db.Column(db.String(10), nullable=False)
    prob = db.Column(db.Float, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'),
        nullable=False) 
    
    def __init__(self, text, positive, prob, movie_id):
        self.text = text
        self.positive = positive
        self.movie_id = movie_id
        self.prob = prob
    
    def json(self):
        # Return object in json format
        return {
            'id': self.id,
            'text': self.text,
            'prob': self.prob,
            'positive': self.positive
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import numpy as np
import pickle
from .model import NLPModel
from .movie_model import Movie, Comments

model = NLPModel()

clf_path = 'api/lib/models/SentimentClassifier.pkl'
with open(clf_path, 'rb') as f:
    model.clf = pickle.load(f)

vec_path = 'api/lib/models/TFIDFVectorizer.pkl'
with open(vec_path, 'rb') as f:
    model.vectorizer = pickle.load(f)

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument(
    'title',
    type=str,
    required=True,
    help="This field cannot be blank!"
)

parser.add_argument(
    'comments',
    required=False,
    action="append",
    help="This field cannot be blank!"
)

class PredictSentiment(Resource):
    def post(self):
        args = parser.parse_args()
        title = args['title']
        comments = args['comments']
        
        movie = Movie(title)
        movie.save_to_db()

        # check if movie exists
        result = Movie.query.filter_by(
            title=args['title']
        ).first()

        if result is not None:
            return {"message": "Movie already exists"}, 409


        for comment in comments:
            # vectorize the user's query and make a prediction
            uq_vectorized = model.vectorizer_transform(np.array([comment]))
            prediction = model.predict(uq_vectorized)
            pred_proba = model.predict_proba(uq_vectorized)

            # Output either 'Negative' or 'Positive' along with the score
            if prediction == 0:
                pred_text = 'Negative'
            else:
                pred_text = 'Positive'
            
            # round the predict proba value
            confidence = round(pred_proba[0], 3)

            comment = Comments(comment, pred_text, pred_proba[0], movie.id)
            comment.save_to_db()

        # create JSON object
        return { 'info': 'Ok' }, 200
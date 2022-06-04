from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

#single database using the SQLAlchemy.Model() class
class UploadDocumentFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    process_name = db.Column(db.String(30), unique=True)
    director = db.Column(db.String(30), unique=False, nullable=False)
    genre = db.Column(db.String(30), unique=False, nullable=False)
    collection = db.Column(db.Integer, unique=False, nullable=False)
    data = db.Column(db.LargeBinary, unique=False, nullable=False)

    def __init__(self, process_name, director, genre, collection):
        self.process_name = process_name
        self.director = director
        self.genre = genre
        self.collection = collection
        
    def json(self):
        #format the data as a dictionary object
        return {'Title': self.title, 'Director': self.director, 'Genre': self.genre, 'Collection': self.collection}
    
    #classmethod is a helper function is implemented to check a given is existing in the database or not.
    @classmethod
    def find_by_title(cls, process_name):
        #FILTER RECORD by "title"
        return cls.query.filter_by(process_name=process_name).first()
    
    #SAVE & DELETE
    def save_to(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_(self):
        db.session.delete(self)
        db.session.commit()
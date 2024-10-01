from App.database import db

class Student (db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(120), nullable=False)

     def __repr__(self):
          return f'<Publisher{self.name}>'
    



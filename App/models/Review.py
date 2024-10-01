from App.database import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    comment = db.Column(db.String(350), nullable=False)
    students = db.relationship('Review',  secondary='student', backref='reviews')



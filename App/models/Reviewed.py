from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Reviewed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    review_id = db.Column(db.Integer, db.ForeignKey('review.id'), nullable=False)
    position = db.Column(db.Integer, nullable=False)

from applications import db


class Task(db.Model):
    db.create_all()
    id = db.Column(db.Integer, primary_key =True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable = False)

    def __repr__(self):
        return f'{self.title} created on {self.date}'
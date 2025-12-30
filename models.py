from db import db

class Detail(db.Model):
    __tablename__ = "details"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    category = db.Column(db.Text)
    tags = db.Column(db.Text)
    description = db.Column(db.Text)

class DetailUsageRule(db.Model):
    __tablename__ = "detail_usage_rules"

    id = db.Column(db.Integer, primary_key=True)
    detail_id = db.Column(db.Integer, db.ForeignKey("details.id"))
    host_element = db.Column(db.Text)
    adjacent_element = db.Column(db.Text)
    exposure = db.Column(db.Text)

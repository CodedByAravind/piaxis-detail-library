from flask import Flask, jsonify, request
from db import db
import models
from models import Detail, DetailUsageRule
from sqlalchemy import or_


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:aravind@localhost:5432/piaxis_local"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)

@app.route("/")
def home():
    return "Hai"

#API 1
@app.route("/details", methods=["GET"])
def get_details():
    details = Detail.query.all()

    result = []
    for d in details:
        result.append({
            "id": d.id,
            "title": d.title,
            "category": d.category,
            "tags": d.tags,
            "description": d.description
        })

    return jsonify(result)
         
#API 2
@app.route("/details/search", methods=["GET"])
def search_details():
    query = request.args.get("q")

    if not query:
        return jsonify([])

    results = Detail.query.filter(
        or_(
            Detail.title.ilike(f"%{query}%"),
            Detail.tags.ilike(f"%{query}%"),
            Detail.description.ilike(f"%{query}%")
        )
    ).all()

    data = []
    for d in results:
        data.append({
            "id": d.id,
            "title": d.title,
            "category": d.category,
            "tags": d.tags,
            "description": d.description
        })

    return jsonify(data)

#API 3
@app.route("/suggest-detail", methods=["POST"])
def suggest_detail():
    data = request.get_json()

    host = data.get("host_element")
    adjacent = data.get("adjacent_element")
    exposure = data.get("exposure")

    rule = DetailUsageRule.query.filter_by(
        host_element=host,
        adjacent_element=adjacent,
        exposure=exposure
    ).first()

    if not rule:
        return jsonify({
            "message": "No suitable detail found for the given context"
        }), 404

    detail = Detail.query.get(rule.detail_id)

    explanation = (
        f"This detail is suggested because it is used when "
        f"{host} connects with {adjacent} under {exposure} conditions."
    )

    return jsonify({
        "detail": {
            "id": detail.id,
            "title": detail.title,
            "category": detail.category,
            "tags": detail.tags,
            "description": detail.description
        },
        "explanation": explanation
    })


if __name__ == "__main__":
    app.run(debug=True)
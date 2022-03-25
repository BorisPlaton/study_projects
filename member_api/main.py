from flask import Flask, jsonify, g, request
import sqlite3

app = Flask(__name__)


def connect_db():
    sql = sqlite3.connect("member.db")
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    if not hasattr(g, "sqlite_db"):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "sqlite_db"):
        g.sqlite_db.close()


@app.route("/member", methods=["GET"])
def get_members():
    db = get_db()
    cur = db.execute("""
        SELECT * FROM member;
    """)
    res = cur.fetchall()

    members = []
    for i in res:
        member = {}
        member["id"] = i["id"]
        member["name"] = i["name"]
        member["email"] = i["email"]
        member["rank"] = i["rank"]
        members.append(member)

    return jsonify({"members": members})


@app.route("/member/<int:member_id>", methods=["GET"])
def get_member(member_id):
    db = get_db()
    cur = db.execute("""
            SELECT * FROM member
            WHERE id = ?;
        """, [member_id])
    res = cur.fetchone()

    member = {}
    member["id"] = res["id"]
    member["name"] = res["name"]
    member["email"] = res["email"]
    member["rank"] = res["rank"]

    return jsonify({"member": member})


@app.route("/member", methods=["POST"])
def add_member():
    member = request.get_json()
    db = get_db()
    cur = db.execute("""
        INSERT INTO member (name, email, rank)
        VALUES
            (?, ?, ?);
    """, [member["name"], member["email"], member["rank"]])
    db.commit()
    return jsonify(member)


@app.route("/member/<int:member_id>", methods=["PUT", "PATCH"])
def update_member(member_id):
    member = request.get_json()
    db = get_db()
    db.execute("""
            UPDATE member 
            SET
                name = ?,
                email = ?,
                rank = ?
            WHERE id = ?;
        """, [member["name"], member["email"], member["rank"], member_id])
    db.commit()

    cur = db.execute("""
            SELECT * FROM member;
        """)
    res = cur.fetchall()

    members = []
    for i in res:
        member = {}
        member["id"] = i["id"]
        member["name"] = i["name"]
        member["email"] = i["email"]
        member["rank"] = i["rank"]
        members.append(member)

    return jsonify({"members": members})


@app.route("/member/<int:member_id>", methods=["DELETE"])
def delete_members(member_id):
    db = get_db()
    db.execute("""
        DELETE FROM member
        WHERE id = ?;
    """, [member_id])
    db.commit()
    cur = db.execute("""
            SELECT * FROM member;
        """)
    res = cur.fetchall()

    members = []
    for i in res:
        member = {}
        member["id"] = i["id"]
        member["name"] = i["name"]
        member["email"] = i["email"]
        member["rank"] = i["rank"]
        members.append(member)

    return jsonify({"members": members})


if __name__ == "__main__":
    app.run(debug=True)

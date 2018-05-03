import sqlite3
from flask_restful import Resource, reqparse
from models import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username",
                        type=str,
                        required=True,
                        help="username for registration"
                        )
    parser.add_argument("password",
                        type=str,
                        required=True,
                        help="password for registration"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.get_by_name(data["username"]):
            return {"message": "User: {}, already exists".format(data["username"])}, 400

        conn = sqlite3.Connection("data.db")
        cursor = conn.cursor()
        query = "INSERT INTO users VALUES(NULL, ?, ?)"
        cursor.execute(query, (data["username"], data["password"]))
        conn.commit()
        conn.close()
        return "User created successfully"

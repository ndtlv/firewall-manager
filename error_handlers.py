from flask import jsonify, Flask

from peewee import DoesNotExist


def error_handlers(app: Flask):
    @app.errorhandler(ValueError)
    def handle_value_error(err):
        return jsonify({
            "error": "value_error",
            "messages": err.args
        }), 400

    @app.errorhandler(DoesNotExist)
    def handle_value_error(err):
        return jsonify({
            "error": "not_found",
            "messages": "Object with given id does not exist"
        }), 404
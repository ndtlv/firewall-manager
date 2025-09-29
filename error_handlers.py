from flask import jsonify, Flask

from peewee import DoesNotExist


class ObjectLinkedError(Exception):
    def __init__(self, object_id):
        self.message = f'Object with id {object_id} is linked to an existing Filtering Policy'
        self.error_code = 409

    def __str__(self):
        return f'{self.message} (Error Code {self.error_code})'


def error_handlers(app: Flask):
    @app.errorhandler(ValueError)
    def handle_value_error(err):
        return jsonify({
            'error': 'value_error',
            'messages': err.args
        }), 400

    @app.errorhandler(DoesNotExist)
    def handle_value_error(err):
        return jsonify({
            'error': 'not_found',
            'messages': 'Object with given id does not exist'
        }), 404

    @app.errorhandler(ObjectLinkedError)
    def handle_object_linked_error(err):
        return jsonify({
            'error': 'conflict',
            'messages': 'Object with given id is linked to a Filtering Policy'
        }), 409
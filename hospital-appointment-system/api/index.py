


# from app import create_app

# app = create_app()



import traceback

try:
    from app import create_app
    app = create_app()
except Exception as e:
    import flask
    app = flask.Flask(__name__)

    @app.route("/")
    @app.route("/<path:path>")
    def error_handler(path=""):
        return flask.jsonify({
            "error": str(e),
            "trace": traceback.format_exc()
        }), 500
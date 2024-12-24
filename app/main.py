from flask import Flask
from app.controllers.analysis_graphs_controller import analysis_graphs_blueprint
from app.controllers.analysis_maps_controller import analysis_blueprint

app = Flask(__name__)
app.register_blueprint(analysis_blueprint, url_prefix="/")
app.register_blueprint(analysis_graphs_blueprint, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True)

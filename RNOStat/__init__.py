from .webdriver import FlaskApp
from .routes import RS_API


App = FlaskApp(name="RNOSatistics")
App.register_mass_blueprints(
    [
        RS_API
    ]
)
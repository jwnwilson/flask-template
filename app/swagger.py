from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec


def setup_swagger(app):
    spec = APISpec(
        title="Flask Template",
        version="v1",
        plugins=[MarshmallowPlugin()],
        openapi_version="2.0.0",
    )
    api_key_scheme = {"type": "apiKey", "in": "header", "name": "Auhtorization"}
    spec.components.security_scheme("jwt", api_key_scheme)

    app.config.update(
        {
            "APISPEC_SPEC": spec,
            "APISPEC_SWAGGER_URL": "/swagger/",  # URI to access API Doc JSON
            "APISPEC_SWAGGER_UI_URL": "/",  # URI to access UI of API Doc
        }
    )
    swagger = FlaskApiSpec(app)
    return swagger

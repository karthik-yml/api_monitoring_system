# swagger_docs.py
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from appauth.serializers import CustomUserSerializer


class AppAuthSwaggerDocs:
    # Swagger documentation for RegisterView
    register_view_docs = swagger_auto_schema(
        operation_description="Register a new user.",
        request_body=CustomUserSerializer,
        responses={
            201: openapi.Response("User registered successfully"),
            400: openapi.Response("Bad request"),
        },
    )

    # Swagger documentation for LoginView
    login_view_docs = swagger_auto_schema(
        operation_description="Log in an existing user.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING, description="User email"),
                "password": openapi.Schema(type=openapi.TYPE_STRING, description="User password"),
            },
            required=["email", "password"],
        ),
        responses={
            200: openapi.Response(
                description="Successful login",
                examples={
                    "application/json": {
                        "access": "access_token_example",
                        "refresh": "refresh_token_example",
                    }
                },
            ),
            401: openapi.Response("Invalid credentials"),
            404: openapi.Response("User does not exist"),
        },
    )

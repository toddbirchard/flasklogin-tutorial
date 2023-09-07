"""Create and bundle CSS and JS files."""
from flask import Flask
from flask_assets import Bundle, Environment


def compile_static_assets(app: Flask):
    """
    Configure static asset bundles.

    :param Flask assets_env: Flask application environment for containing assets.

    :return: None
    """
    assets_env = Environment(app)
    Environment.auto_build = True
    Environment.debug = False
    compile_javascript(assets_env)
    compile_stylesheets(assets_env)


def compile_javascript(assets_env: Environment):
    """
    Configure static asset bundles.

    :param Environment assets_env: Flask application environment.

    :return: None
    """
    # JavaScript Bundle
    js_bundle = Bundle("src/js/main.js", filters="jsmin", output="dist/js/main.min.js")
    # Register JS assets
    assets_env.register("js_all", js_bundle)
    # Build assets
    js_bundle.build()


def compile_stylesheets(assets_env: Environment):
    """
    Configure static asset bundles.

    :param Environment assets_env: Flask application environment.

    :return: None
    """
    # Stylesheets Bundles
    account_less_bundle = Bundle(
        "src/less/account.less",
        filters="less,cssmin",
        output="dist/css/account.css",
        extra={"rel": "stylesheet/less"},
    )
    dashboard_less_bundle = Bundle(
        "src/less/dashboard.less",
        filters="less,cssmin",
        output="dist/css/dashboard.css",
        extra={"rel": "stylesheet/less"},
    )
    # Register CSS assets
    assets_env.register("account_less_bundle", account_less_bundle)
    assets_env.register("dashboard_less_bundle", dashboard_less_bundle)
    # Build Stylesheets from `.less` files.
    account_less_bundle.build()
    dashboard_less_bundle.build()

"""Create and bundle CSS and JS files."""
from flask_assets import Bundle, Environment


def compile_static_assets(app):
    """Configure static asset bundles."""
    assets = Environment(app)
    Environment.auto_build = True
    Environment.debug = False
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
    # JavaScript Bundle
    js_bundle = Bundle("src/js/main.js", filters="jsmin", output="dist/js/main.min.js")
    # Register assets
    assets.register("account_less_bundle", account_less_bundle)
    assets.register("dashboard_less_bundle", dashboard_less_bundle)
    assets.register("js_all", js_bundle)
    # Build assets
    account_less_bundle.build()
    dashboard_less_bundle.build()
    js_bundle.build()

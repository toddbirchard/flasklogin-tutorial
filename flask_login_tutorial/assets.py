from flask_assets import Environment, Bundle


def compile_assets(blueprint):
    """Configure authorization asset bundles."""
    assets = Environment(blueprint)
    Environment.auto_build = True
    Environment.debug = False
    # Stylesheets Bundle
    account_less_bundle = Bundle('src/less/account.less',
                         filters='less,cssmin',
                         output=f'dist/css/account.css',
                         extra={'rel': 'stylesheet/less'})
    dashboard_less_bundle = Bundle('src/less/dashboard.less',
                         filters='less,cssmin',
                         output=f'dist/css/dashboard.css',
                         extra={'rel': 'stylesheet/less'})
    # JavaScript Bundle
    js_bundle = Bundle('src/js/main.js',
                       filters='jsmin',
                       output='dist/js/main.min.js')
    # Register assets
    assets.register('account_less_bundle', account_less_bundle)
    assets.register('dashboard_less_bundle', dashboard_less_bundle)
    assets.register('js_all', js_bundle)
    # Build assets
    account_less_bundle.build()
    dashboard_less_bundle.build()
    js_bundle.build()

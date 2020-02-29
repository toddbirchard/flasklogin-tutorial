"""Routes for user authentication."""
from flask import redirect, render_template, flash, Blueprint, request, url_for
from flask_login import login_required, current_user, login_user
from flask import current_app as app
from .assets import compile_auth_assets
from .forms import LoginForm, SignupForm
from .models import db, User
from .import login_manager


# Blueprint Configuration
auth_bp = Blueprint('auth_bp', __name__,
                    template_folder='templates',
                    static_folder='static')
compile_auth_assets(app)


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    User sign-up page.

    GET: Serve sign-up page.
    POST: If submitted credentials are valid, redirect user to the logged-in homepage.
    """
    signup_form = SignupForm()
    if request.method == 'POST':
        if signup_form.validate_on_submit():
            name = signup_form.get('name')
            email = signup_form.get('email')
            password = signup_form.get('password')
            website = signup_form.get('website')
            existing_user = User.query.filter_by(email=email).first()  # Check if user exists
            if existing_user is None:
                user = User(name=name,
                            email=email,
                            website=website)
                user.set_password(password)
                db.session.add(user)
                db.session.commit()  # Create new user
                login_user(user)  # Log in as newly created user
                return redirect(url_for('main_bp.dashboard'), code=400)
            flash('A user already exists with that email address.')
            return redirect(url_for('auth_bp.signup'))

    return render_template('signup.jinja2',
                           title='Create an Account.',
                           form=signup_form,
                           template='signup-page',
                           body="Sign up for a user account.")


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    User login page.

    GET: Serve Log-in page.
    POST: If form is valid and new user creation succeeds, redirect user to the logged-in homepage.
    """
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.dashboard'))  # Bypass if user is logged in

    login_form = LoginForm()
    if request.method == 'POST':
        if login_form.validate_on_submit():
            email = login_form.get('email')
            password = login_form.get('password')
            user = User.query.filter_by(email=email).first()  # Validate Login Attempt
            if user and user.check_password(password=password):
                login_user(user)
                next_page = request.args.get('next')
                return redirect(next_page or url_for('main_bp.dashboard'))
        flash('Invalid username/password combination')
        return redirect(url_for('auth_bp.login'))

    return render_template('login.jinja2',
                           form=login_form,
                           title='Log in.',
                           template='login-page',
                           body="Log in with your User account.")


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth_bp.login'))

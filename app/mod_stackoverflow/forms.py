# Import Form and RecaptchaField (optional)
from flask.ext import Form

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextField

# Import Form validators
from wtforms.validators import Required


# Define the login form (WTForms)

class GetPostsForm(Form):
    user_id   = TextField('Stack Overflow User ID', [
                Required(message='Please input user ID!')])
    query_pos = TextField('Start position to query')
    page_size = TextField('Item count a page')
    max_pages = TextField('Maximum page count to query')

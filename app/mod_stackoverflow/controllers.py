# Import flask dependencies
from flask import Blueprint, render_template, request

# StackExchange API key
SE_API_KEY = "pXlviKYs*UZIwKLPwJGgpg(("

# Import module models
from app.mod_stackoverflow.models import Posts

# Import module stackapi
from app.mod_stackapi.stackapi import StackAPI

# Define the blueprint: 'stackoverflow', set its url prefix: app.url/stackoverflow
mod_stackoverflow = Blueprint('stackoverflow', __name__, url_prefix='/stackoverflow', static_folder='../../static', template_folder='../../templates')

# Set the route and accepted methods
@mod_stackoverflow.route('/', methods=['GET'])
def defaultpage():
    return render_template("stackoverflow/getposts.html")

@mod_stackoverflow.route('/getposts', methods=['POST'])
def getposts():

    if 'uid' in request.form:
        _uid = request.form['uid']
    else:
        _uid = None
    if 'querypos' in request.form:
        _query_pos = request.form['querypos']
    else:
        _query_pos = None
    if 'pagesize' in request.form:
        _page_size = request.form['pagesize']
    else:
        _page_size = None
    if 'maxpages' in request.form:
        _max_pages = request.form['maxpages']
    else:
        _max_pages = None

    if _query_pos is None or _query_pos < 0:
        _query_pos = 1

    if _page_size is None or _page_size <= 0 or _page_size > 100:
        _page_size = 10

    if _max_pages is None or _max_pages <= 0 or _max_pages > 10:
        _max_pages = 2

    _page = int((_query_pos - 1) / _page_size) + 1
    _itempos = int((_query_pos - 1) % _page_size)

    # validate the received values
    if _uid is None or len(_uid) <= 0:
        return Posts(404, "no_method", "no method found with this name").toJSON()

    SITE = StackAPI('stackoverflow', key=SE_API_KEY)
    SITE.page_size=_page_size
    SITE.max_pages=_max_pages
    _res = SITE.fetch('users/'+_uid+'/posts', page=_page, order='desc', sort='activity')

    _posts = Posts.load(_res, _itempos)

    if hasattr(_posts, 'items'):
        _posts.query_pos = _query_pos

    return _posts.toJSON()


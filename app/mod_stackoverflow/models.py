
import json


def check_value(dict_obj, element_name):
    return dict_obj is not None and element_name in dict_obj


def get_value(dict_obj, element_name):
    if dict_obj is None or element_name not in dict_obj:
        return None
    return dict_obj[element_name]


class Owner:
    @staticmethod
    def load(dict_obj):
        if dict_obj is None:
            return None

        _owner = Owner()

        _profile_image = get_value(dict_obj, 'profile_image')
        if _profile_image is not None:
            _owner.profile_image = _profile_image
        _display_name = get_value(dict_obj, 'display_name')
        if _display_name is not None:
            _owner.display_name = _display_name
        _link = get_value(dict_obj, 'link')
        if _link is not None:
            _owner.link = _link

        return _owner

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class Post:
    @staticmethod
    def load(dict_obj):
        if dict_obj is None:
            return None

        _post = Post()

        _owner = Owner.load(get_value(dict_obj, 'owner'))
        if _owner is not None:
            _post.owner = _owner

        _post_type = get_value(dict_obj, 'post_type')
        if _post_type is not None:
            _post.post_type = _post_type
        _creation_date = get_value(dict_obj, 'creation_date')
        if _creation_date is not None:
            _post.creation_date = _creation_date
        _last_edit_date = get_value(dict_obj, 'last_edit_date')
        if _last_edit_date is not None:
            _post.last_edit_date = _last_edit_date
        _last_activity_date = get_value(dict_obj, 'last_activity_date')
        if _last_activity_date is not None:
            _post.last_activity_date = _last_activity_date
        _link = get_value(dict_obj, 'link')
        if _link is not None:
            _post.link = _link

        return _post

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class Posts:
    @staticmethod
    def error(id, name, message):
        #self.items = []
        #self.has_more = False
        _posts = Post()
        _posts.error_id = id
        _posts.error_name = name
        _posts.error_message = message
        return _posts

    def add_item(self, post):
        if not hasattr(self, 'items') or self.items is None:
            self.items = []
        self.items.append(post)

    @staticmethod
    def load(dict_obj, item_pos):
        if dict_obj is None:
            return Posts.error(500, "not_reach", "could not reach out server")

        _items = get_value(dict_obj, 'items')
        if _items is None or check_value(dict_obj, 'error_id'):
            return Posts.error(get_value(dict_obj, 'error_id'), get_value(dict_obj, 'error_name'), get_value(dict_obj, 'error_message'))

        _posts = Posts()

        _posts.has_more = get_value(dict_obj, 'has_more')

        _i = item_pos
        _count = len(_items)
        while _i < _count:
            _post = Post.load(_items[_i])
            if _post:
                _posts.add_item(_post)
            _i = _i + 1

        return _posts

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)


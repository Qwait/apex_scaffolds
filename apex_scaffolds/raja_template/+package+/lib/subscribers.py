from pyramid.threadlocal import get_current_request

def add_renderer_globals(event):
    request = event.get('request')
    if request is None:
        request = get_current_request()

    globs = {}
    event.update(globs)
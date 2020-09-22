def create_url(host=None, port=None):
    if host is None:
        host = 'localhost'
    if port is None:
        port = '443'
    return "https://{0}:{1}".format(host, port)
'''others solution
def create_url(host='localhost', port=443) -> str:
    return f'https://{host}:{port}'
'''

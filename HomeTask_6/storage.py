import time
data = {}

def force_add_url(k, url, alias, id_):
    data.pop(k)
    data[id_] = {'url': url, 'alias': alias}
    return 'Done'

def add_url(url, alias):
    ccount =0
    id_ = time.time()
    for k in list(data.keys()):
        if data[k].get('alias') == alias:
            return tuple((k, 'alias_exist', id_))
            break
        else:
            ccount += 1
            pass
    if ccount == len(list(data.keys())):
        data[id_] = {'url': url, 'alias': alias}
        return '\nDone'

def get_url(alias):
    for k in list(data.keys()):
        if data[k].get('alias') == alias:
            return (data[k].get('url'))
    else:
        return "not found URL by alias"

def print_all():
    return (data)



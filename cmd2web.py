import web
import subprocess
import io
import json
import sys

def generate_config(config):
    """ generate config """

    def _gen_non_leaf(config):
        """ gen config for non leaf node """
        ret = []
        for k, elem in config.items():
            gen_items = generate_config(elem)
            print (gen_items)
            for gen in gen_items:
                sub_uri, class_object = gen
                ret.append(['/{}{}'.format(k, sub_uri), class_object])
        return ret

    if 'cmd' in config:
        class __unnamed__:
            def GET(self):
                cmd = config['cmd'].format(**dict(web.input()))
                proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
                proc.wait()
                stream_stdout = io.TextIOWrapper(proc.stdout, encoding='utf-8')
                stream_stderr = io.TextIOWrapper(proc.stderr, encoding='utf-8')
                ret = {
                    'ret': proc.returncode,
                    'stdout': stream_stdout.read(),
                    'stderr': stream_stderr.read()
                }
                return json.dumps(ret)

        return [('/.*', __unnamed__)]

    elif isinstance(config, list) or isinstance(config, tuple):
        return _gen_non_leaf(dict(enumerate(config)))
    elif isinstance(config, dict):
        return _gen_non_leaf(config)
    else:
        raise NotImplementedError('type not support in config for {}'.format(config))


if __name__ == "__main__":
    config_file='config.json'
    if len(sys.argv) >= 2:
        config_file = sys.argv[1]
    with open(config_file) as f:
        gen = generate_config(json.load(f))
        
    urls = []
    for url, action in gen:
        urls.append(url)
        urls.append(action)

    app = web.application(urls, globals())

    app.run()

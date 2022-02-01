import os

import requests
import yaml
from tqdm import tqdm


class DownloadManager:
    def __init__(self, name, path, tag, proxy=None):
        self.path = path + '\\' + name + '\\' + tag + '\\'
        self.proxy = proxy
        self.tag = tag
        self.name = name

    def download(self, url, filename, path):
        if path == '':
            file_path = self.path + filename
        else:
            file_path = path + '/' + filename
            self.path = path

        if not os.path.exists(self.path):
            os.makedirs(self.path)
        print('Target: ' + file_path)
        if self.proxy is not None:
            r = requests.get(url, proxies=self.proxy, stream=True)
        else:
            r = requests.get(url, stream=True)
        print('Calculating size...')
        file_size = int(r.headers['content-length'])
        with tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024, ascii=True,
                  desc=filename) as bar:
            with open(file_path, 'wb') as fp:
                for chunk in r.iter_content(chunk_size=512):
                    if chunk:
                        fp.write(chunk)
                        bar.update(len(chunk))
        # self.update_tag()

    def update_tag(self):
        config_path = 'config.yaml'
        config_file = open(config_path, 'r', encoding='utf-8').read()
        config = yaml.load(config_file, Loader=yaml.BaseLoader)
        for index, repo in enumerate(config['repos']):
            if repo['name'] == self.name:
                config['repos'][index]['tag'] = self.tag
                with open(config_path, 'w') as old_config:
                    yaml.dump(config, old_config)

import os
import re

import yaml

import decompress
from download import DownloadManager
from spider import GitRepoSpider


class GitRepoManager:

    def __init__(self):
        self.config_path = 'config.yaml'
        config_file = open(self.config_path, 'r', encoding='utf-8').read()
        self.config = yaml.load(config_file, Loader=yaml.BaseLoader)
        self.proxy = self.config.get('proxy')
        self.path = self.config.get('path')

    def check_update(self):
        up = True
        for repo in self.config['repos']:
            spider = GitRepoSpider(repo['name'], repo['author'], repo['tag'], repo['key'], self.proxy)
            spider.get_latest_tag()
            if spider.flag:
                up = False
        if up:
            print('Everything is up to date.')

    def update_all(self):
        for repo in self.config['repos']:
            spider = GitRepoSpider(repo['name'], repo['author'], repo['tag'], repo['key'], self.proxy)
            tag = spider.get_latest_tag()
            if spider.flag:
                spider.get_assets()
                downloading = DownloadManager(repo['name'], self.path, tag, self.proxy)
                for download_name, download_url in spider.download.items():
                    print('Start downloading from ' + download_name)
                    downloading.download(download_url, download_name, repo['target'])

                    if repo['target'] == '':
                        file_path = self.path + '\\' + repo['name'] + '\\' + tag
                    else:
                        file_path = repo['target']

                    # 下载完成后进行文件处理
                    pattern = re.compile(r'[^.]+$')
                    download_suffixes = re.search(pattern, download_name).group()
                    setting = repo['setting']
                    if download_suffixes in ['gz', 'tar', 'zip', 'rar']:
                        eval(
                            'decompress.un_' + download_suffixes + '(r\'' + file_path + '\', r\'' + download_name + '\', r\'' +
                            setting['decompress'] + '\')')
                        if setting['clean']:
                            os.remove(file_path + '/' + download_name)
        print('Now everything is up to date.')

    def list_all(self):
        print('Installed apps: ')
        for repo in self.config['repos']:
            print(repo['author'] + '/' + repo['name'] + ' ' + repo['tag'])

    def modify_config(self):
        print('Open config.yaml')
        try:
            os.system('code ' + self.config_path)
        except:
            os.system('notepad ' + self.config_path)

    def empty(self):
        decompress.un_zip('a', 'b', 'c')

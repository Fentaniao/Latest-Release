import re

import requests


class GitRepoSpider:
    download = {}
    flag = False
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.107 '
                      'Safari/537.36 '
                      'Edg/92.0.902.55'
    }

    def __init__(self, name, author, tag, key=None, proxy=None):
        git_repo_url = 'https://api.github.com/repos/' + author + '/' + name + '/releases/latest'
        try:
            if proxy is not None:
                self.json = requests.get(git_repo_url, proxies=proxy, headers=self.headers).json()
            else:
                self.json = requests.get(git_repo_url, headers=self.headers).json()
        except Exception as e:
            print('Error: Can\'t get github api, Exception is: ' + str(e))
        self.name = name
        self.tag = tag
        self.key = key

    def get_latest_tag(self):
        latest_tag = self.json['tag_name']
        current_tag = "not exists" if self.tag == "" else self.tag
        if self.tag == latest_tag:
            return latest_tag
        else:
            print(self.name + ' : ' + current_tag + ' ---> ' + latest_tag)
            self.flag = True
            return latest_tag

    def get_assets(self):
        assets_list = self.json['assets']
        assets_num = len(assets_list)
        # 全部下载
        if self.key in ['', 'all']:
            for assets in assets_list:
                browser_download_url = assets['browser_download_url']
                pattern = re.compile(r'[^/]+$')
                download_name = re.search(pattern, browser_download_url).group()
                self.download[download_name] = browser_download_url
        # 下载单个文件
        else:
            for assets in assets_list:
                browser_download_url = assets['browser_download_url']
                pattern = re.compile(r'[^/]+$')
                download_name = re.search(pattern, browser_download_url).group()
                if self.key in download_name:
                    self.download[download_name] = browser_download_url
                    return
            print('Key ' + self.key + ' not exit.')

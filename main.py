import os

from manager import GitRepoManager

if __name__ == '__main__':
    print(
        'Welcome to Command Windows for Latest Release.\n'
        'Github repo: https://github.com/Fentaniao/Latest-Release.\n'
        'Enter help for more actions.'
    )
    # 自检
    if not os.path.exists('config.yaml'):
        print('\nInitial config.yaml file...')
        config_default = '''\
path: download
proxy:
  http: http://127.0.0.1:7890
  https: http://127.0.0.1:7890
repos:
  - author: Fentaniao
    name: Liquid
    tag:
    key: Liquid.zip
    target:
    compress_setting: { decompress: auto, clean: true }
    '''
        with open('config.yaml', 'w', encoding='utf-8') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(config_default)
        print('Complete initialization.\n'
              'Please fill in you own configuration in config.yaml file, you can turn to README.md for help.'
              )

    while True:
        manager = GitRepoManager()

        command = input('\n>>')
        if command == 'help':
            print('''\
    Command[<args>]        :           Usage
    list/ls                :           List installed apps
    status/st              :           Show status and check for new app versions
    update/up              :           Update all apps
    config/cf              :           Open config file to add an app or modify other settings
    exit/et                :           Exit the shell
            ''')
        elif command == 'list' or command == 'ls':
            manager.list_all()
        elif command == 'status' or command == 'st':
            manager.check_update()
        elif command == 'update' or command == 'up':
            manager.update_all()
        elif command == 'config' or command == 'cf':
            manager.modify_config()
        elif command == 'exit' or command == 'et':
            break
        else:
            print('Command not defined')

import os

from manager import GitRepoManager

if __name__ == '__main__':
    # 自检
    if os.path.exists('config.yaml'):
        pass
    else:
        print('Please add config.yaml file before running.')
        exit()

    manager = GitRepoManager()
    print(
        'Welcome to Command Windows for Latest Release\n'
        'Github repo: https://github.com/Fentaniao/Latest-Release\n'
        'Enter help for more actions'
    )
    while True:
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

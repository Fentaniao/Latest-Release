# Latest Release

<p>
    <img src="https://img.shields.io/github/v/release/fentaniao/Latest--Release?&color=blue&logo=hack-the-box)" />
    <img alt="C++" src="https://img.shields.io/badge/-Python-9f62a5?style=flat&logo=python&logoColor=white" />
<!--    <img alt="C#" src="https://img.shields.io/badge/-C_Sharp-9f62a5?style=flat&logo=csharp&logoColor=white" />
    <img alt="WinUI_3" src="https://img.shields.io/badge/-WinUI_3-9f62a5?style=flat&logo=windows&logoColor=white" />-->
</p>

[English Readme](https://github.com/Fentaniao/Latest-Release/blob/main/README.md) | [中文自述文件](https://github.com/Fentaniao/Latest-Release/blob/main/README_zh.md)

A powerful application to automatically deploy GitHub Release.

## Features

- 1
- 1
- 1

## Install
There are many ways for you to install this program.

### Run the script though exe file

Only for Windows user.

1. Turn to [GitHub releases page](https://github.com/Fentaniao/Latest-Release/releases), then click on **Assets** at the bottom to show the files available in the release.
2. Download the **exe** file and decompress it.
3. Create the `config.yaml` file and then configure it by referencing to the Usage in [`README.md`.](https://github.com/Fentaniao/Latest-Release/blob/main/README.md)
4. Run the exe file.

### Run the script though Python

You should first install Python3 into your desktop.

1. Turn to [GitHub releases page](https://github.com/Fentaniao/Latest-Release/releases), then click on **Assets** at the bottom to show the files available in the release.
2. Download the **Source code (zip)** and decompress it.
3. Create the `config.yaml` file and then configure it by referencing to the Usage in [`README.md`.](https://github.com/Fentaniao/Latest-Release/blob/main/README.md)
4. Install the package the scripts need.
5. Run the main.py file.

## Usage

### Commands

After start the exe file, you can enter `help` in the Command Windows to see the commands with their description.

```
    Command[<args>]        :           Usage
    list/ls                :           List installed apps
    status/st              :           Show status and check for new app versions
    update/up              :           Update all apps
    config/cf              :           Open config file to add an app or modify other settings
    exit/et                :           Exit the shell
```

### How to Configure the `config.yaml` file

A simplest `config.yaml` file is shown like this:

```yaml
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
```

#### Default configuration

1

## Roadmap

- A client with a GUI based on WinUI3 is coming soon.
- Support more functions and more ways of configuration.

## Contact

Author: Fentaniao

Email: [Fentaniao@gmail.com](mailto:Fentaniao@gmail.com)

## License

[GPL-3.0 License](https://github.com/Fentaniao/Latest-Release/blob/main/LICENSE) © Fentaniao

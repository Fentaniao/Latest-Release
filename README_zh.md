# Latest Release

<p>
    <img src="https://img.shields.io/github/v/release/fentaniao/Latest-Release?&color=blue&logo=hack-the-box)" />
    <img alt="C++" src="https://img.shields.io/badge/-Python-9f62a5?style=flat&logo=python&logoColor=white" />
<!--    <img alt="C#" src="https://img.shields.io/badge/-C_Sharp-9f62a5?style=flat&logo=csharp&logoColor=white" />
    <img alt="WinUI_3" src="https://img.shields.io/badge/-WinUI_3-9f62a5?style=flat&logo=windows&logoColor=white" />-->
</p>

[English Readme](https://github.com/Fentaniao/Latest-Release/blob/main/README.md) | [中文自述文件](https://github.com/Fentaniao/Latest-Release/blob/main/README_zh.md)

一个用于自动部署GitHub Release的Python程序。

## 特点

### 高度自动化的流程

- 包括自动解压和自动清理功能
- 自动安装功能正在开发中

### 简单而强大的配置方案

- 只需要一个配置，可以一直使用
- 支持配置文件的热更新

## 安装

你有多种方法来安装这个程序。

### 通过exe文件运行脚本

只适用于Windows用户。

1. 导航到[GitHub 发布页](https://github.com/Fentaniao/Latest-Release/releases)，然后点击底部的**Assets**，显示该版本中的可用文件。
2. 下载**Latest Release.zip**文件并解压。
3. 创建`config.yaml`文件，然后参照然后参照[`README.md`.](https://github.com/Fentaniao/Latest-Release/blob/main/README.md)中的用法进行配置。
4. 在**命令行中启动**exe文件。

### 通过Python运行脚本

这种方法要求你首先将Python3安装到你的电脑上。

1. 转到 [GitHub 发布页](https://github.com/Fentaniao/Latest-Release/releases)，然后点击底部的**资产**，显示该版本中的可用文件。
2. 下载**源代码（zip）**并解压。
3. 创建`config.yaml`文件，然后参照[`README.md`.](https://github.com/Fentaniao/Latest-Release/blob/main/README.md)中的用法进行配置。
4. 安装脚本需要的软件包。
5. 运行main.py文件。

## 用法

### 命令

启动exe文件后，你可以在命令窗口中输入`help`来查看命令及其说明。

```
    Command[<args>]        :           Usage
    list/ls                :           List installed apps
    status/st              :           Show status and check for new app versions
    update/up              :           Update all apps
    config/cf              :           Open config file to add an app or modify other settings
    exit/et                :           Exit the shell
```


### 如何配置`config.yaml`文件

一个最简单的`config.yaml`文件是这样的。

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
    setting: { decompress: auto, clean: true }
```

#### 一级参数

##### 参数

| 参数   | 数据类型 | 默认值 | 说明                                             |
| ------ | -------- | ------ | ------------------------------------------------ |
| `path` | 字符串   | -      | 默认储存路径，未指定target时自动存储到path路径下 |
| `proxy` | 字典   | -      | 代理信息 |
| `repos` | 字典   | -      | 存储库信息 |

#### `repos`存储库信息

##### 参数

| 参数         | 数据类型 | 默认值 | 说明       |
| ------------ | -------- | ------ | ---------- |
| `author` | 字符串   | -      | 存储库所有者 |
| `name` | 字符串   | -      | 存储库名称 |
| `tag` | 字符串   | -                                   | 发行版的标签 |
| `key` | 字符串   | "all"      | 要下载的文件名 |
| `target` | 字符串   | path      | 下载文件的路径 |
| `setting` | 字典   | { decompress: auto, clean: true }      | 解压设置 |

#### `setting`设置

##### 参数

| 参数         | 数据类型 | 默认值 | 说明       |
| ------------ | -------- | ------ | ---------- |
| `decompress` | 字符串   | -      | 解压方式，`"auto"`表示自动解压，其他非空字符串表示安装在同名目录下，放空则解压到`file_name + '_files'`目录下 |
| `clean` | 字符串   | true      | true表示解压完成后自动清理压缩文件 |

## 路线图

- 基于WinUI3的GUI客户端即将问世。
- 支持更多的功能和更多的配置方式。

## 联系

作者： Fentaniao

邮箱： [Fentaniao@gmail.com](mailto:Fentaniao@gmail.com)

## 许可证

[GPL-3.0 License](https://github.com/Fentaniao/Latest-Release/blob/main/LICENSE) © Fentaniao

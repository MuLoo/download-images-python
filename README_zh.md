# Image Downloader
Fork 自: https://github.com/QianyanTech/Image-Downloader

[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)

## 1. 简介

+ 从图片搜索引擎，爬取关键字搜索的原图URL并下载
+ 开发语言python，采用Requests、Selenium等库进行开发

## 2. 功能

+ 支持的搜索引擎: Google, 必应, 百度
+ 提供GUI及CMD版本
+ GUI版本支持关键词键入，以及通过关键词列表文件（行分隔,**使用UTF-8编码**）输入进行批处理爬图下载
+ 可配置线程数进行并发下载，提高下载速度
+ 支持搜索引擎的条件查询（如 :site）
+ 支持socks5和http代理的配置，方便科学上网用户

## 3. 用法

需要安装于当前chrome对应的chromedriver版本，下载地址：https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html

下载chromedriver之后，解压缩，并移动到系统PATH目录下，或者将其路径添加到系统PATH环境变量中

```bash
sudo mv /path/to/chromedriver /usr/local/bin/
```


### 3.1 图形界面

运行`image_downloader_gui.py`脚本以启动GUI界面

```bash
python image_downloader_gui.py
```

![GUI](/GUI.png)

### 3.2 命令行

```bash
usage: image_downloader.py [-h] [--engine {Google,Bing,Baidu}]
                           [--driver {chrome_headless,chrome,api}]
                           [--max-number MAX_NUMBER]
                           [--num-threads NUM_THREADS] [--timeout TIMEOUT]
                           [--output OUTPUT] [--safe-mode] [--face-only]
                           [--proxy_http PROXY_HTTP]
                           [--proxy_socks5 PROXY_SOCKS5]
                           keywords
```


### 二次开发者的提示

启动项目前，请确保已经安装了chromedriver，添加到系统环境变量中，比如在Linux系统中，可以将chromedriver放到`/usr/local/bin`目录下

```bash
sudo mv /path/to/chromedriver /usr/local/bin/
```

如果无法确定最新的chrome和chromedriver，请在[这里](https://googlechromelabs.github.io/chrome-for-testing/#stable) 下载。

正确设置了 chromedriver后，在终端输入 `chromedriver --help`，如果出现帮助信息，则表明设置成功.


#### 打包
因为目前我只打包了mac环境，使用的是py2app.

  ```bash
  pip install -U py2app
  python setup.py py2app
  ```

  如果打包windows版本，可以使用pyinstaller.


## 许可

+ MIT License
+ 996ICU License

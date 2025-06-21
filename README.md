# 🎮 OK School Life - 校园生活模拟游戏

*一个充满惊喜(惊吓)的校园模拟游戏*
![1745061328893](/assets/images/welcome/welcome-v4.png)

## 📖 游戏简介

《OK School Life》是一款模拟中国高中生校园生活的文字选择游戏。通过不同选择体验从入学到毕业的酸甜苦辣，每个决定都可能改变你的游戏结局！

## ✨ 游戏特色

- 🏠 **3种家庭背景**：富裕/普通/贫穷（随机加权分配）
- 🏫 **3所特色学校**：每所学校有专属事件链
- 📚 **25+随机事件**：涵盖学习、社交、生活各方面
- 💀 **多结局系统**：包括被开除、住院、顺利毕业等
- 😂 **黑色幽默**：各种离谱又真实的校园梗
- 所有事件来自真实事件

## 🚀 快速开始

如果你有python环境，使用git来下载此仓库
### 1.下载仓库
```bash
git clone https://github.com/still-alive-hhz/OK-School-Life.git
cd ok-school-life
python ok-school-life.py
```
### 2.安装依赖
#### a.使用虚拟环境
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
#### b.下载依赖
```bash
pip install pywebview
```
```bash
pip install flask
```
#### c.使用QT依赖和Python扩展
```bash
sudo apt update
sudo apt install python3-pyqt5
pip install qtpy PyQt5
```
#### c.或者使用GTK
```bash
sudo apt install python3-gi gir1.2-webkit2-4.0
pip install PyGObject
```
#### d.PyQt5 及其 WebEngine 支持
```bash
pip install PyQt5 PyQtWebEngine
```
若执行d后报错,`“没有 gi”`,则使用退回c步骤下载GTK,但是Linux系统源中有可能找不到gir1.2-webkit2-4.0包，原因是Linux 发行版较新或源未启用 universe/multiverse。解决办法
#### “没有 gi”的解决办法
##### 方法一 使用 PyQt5 作为 webview 后端
```bash
pip install PyQt5 PyQtWebEngine
```
##### 方法二 如果必须用GTK则安装旧版的
可以尝试添加旧源或用 snap/flatpak 安装 webkit2gtk，但操作较复杂，不推荐。

## 🎯 游戏玩法

1. 随机分配家庭背景
2. 选择心仪的高中
3. 应对各种校园事件
4. 努力不被开除！
5. 尝试解锁所有结局

## 📜 事件示例

- 单休制引发的思考
- 神秘黑色高级车同学
- 传奇浴室里的烟哥
- 突如其来的仪容检查
- 原神玩家 VS LOL玩家的战争
- 数学建模活动中的冲突
- 英语老师的听写突袭

## 🏆 成就系统

游戏中包含多个隐藏成就，例如：

- **视力5.0**：通过历史考试的特殊选择解锁
- **开发者の感谢**：在特定事件中鼓励开发者
- **西格玛人**：在考试中保持冷静
- **不哑巴英语**：正确发音英语单词
- **丞相：有容乃大**：在冲突中选择原谅他人

尝试解锁所有成就，记录你的校园旅程！

## 📌 注意事项

❗ 本游戏包含夸张表现手法
❗ 部分结局含黑色幽默元素
❗ 开发者不对游戏中的选择负责

## 📅 版本信息

目前处于Beta版本

## ✅TO-DO

* [x] 图形化界面
* [ ] 增添更多内容（包括数值系统，特殊事件库等）
* [x] 先实现界面美化，再实现web游玩此python
* [x] 对exe进行标准化设置图标等
* [x] 大更代码，让事件与脚本分离
* [x] 加入劳大复活系统，用2D动作小游戏的方式复活
* [ ] 对GUI进行优化，如具体样式修改和相对值大小
* [ ] 保存成就，关闭程序仍然可用
* [ ] 移动端适配

## 🎆 我们的愿景

游戏正式发布的时候在其他平台发布1元付费版，收益全部用于公益事业。

## 👨‍💻 开发者

Still_Alive with GitHub Copilot and OpenAI ChatGPT

WaiJade with his clever brain

## 📊 项目统计

![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=still-alive-hhz.OK-School-Life) ![GitHub issues](https://img.shields.io/github/issues/still-alive-hhz/OK-School-Life)
![GitHub stars](https://img.shields.io/github/stars/still-alive-hhz/OK-School-Life?style=social) ![GitHub forks](https://img.shields.io/github/forks/still-alive-hhz/OK-School-Life) 

![GitHub Stats](https://github-readme-stats.vercel.app/api/pin/?username=still-alive-hhz&repo=OK-School-Life&show_owner=true)

![Top Language](https://img.shields.io/github/languages/top/still-alive-hhz/OK-School-Life) ![Code Size](https://img.shields.io/github/languages/code-size/still-alive-hhz/OK-School-Life)

## 🌟 最近活动

![GitHub Last Commit](https://img.shields.io/github/last-commit/still-alive-hhz/OK-School-Life) ![GitHub Commit Activity](https://img.shields.io/github/commit-activity/y/still-alive-hhz/OK-School-Life)



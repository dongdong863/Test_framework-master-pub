#  Web端 Selenium 测试框架介绍

**在开始之前，请让我先声明几点：**

1. 请确保你已经掌握了基本的Python语法、函数的二次封装等
2. 如果你要搭建UI框架，请确保你已经掌握了Selenium的基本用法


框架主要的作用就是帮助我们编写更加简单而且好维护的用例，让我们把主要精力放在测试用例的设计上，那么我们就需要把所有额外的东西抽象出来作为框架的部分。

比如这些额外的需要用到的公共部分，如：

1. 日志以及报告
2. 日志级别、URL、浏览器类型等基本配置
3. 参数化
4. 公共方法


## 搭建框架目录结构

    Test_framework
        |--config（配置文件）
        |--data（数据文件）
        |--drivers（驱动）
        |--log（日志）
        |--report（报告）
        |--test（测试用例）
        |--utils（公共方法）
        |--ReadMe.md（加个说明性的文件，告诉团队成员框架需要的环境以及用法）


编程语言的选择，Python 3的使用越来越多，而且3的unittest中带有subTest，能够通过子用例实现参数化。而用2的话需要unittest2或其他的库来实现，所以我们这里选用Python 3。


## 配置文件

yaml config文件夹里创建config.yml文件，在utils里创建一个config.py文件读取配置，内容暂且不管。


## 该框架的大概编写思路如下：

1. 首先把配置抽出来，用yaml文件放配置。在config层添加配置文件config.yml，在utils层添加file_reader.py与config.py来管理。
2. 将python自带的logging模块封装了一下，从配置文件读取并设置固定的logger。在utils中创建了log.py。
3. 然后封装xlrd模块，读取excel，实现用例的参数化。
4. 然后是生成HTML测试报告，修改网上原有的HTMLTestRunner，改为中文并美化，然后修改其支持PY3。
5. 添加发送邮件报告的能力。在utils中添加了mail.py。
6. 测试用例用Page-Object思想进行封装，进一步划分test层的子层。
7. 然后添加了一个简单的自定义断言，在utils中添加assertion.py，可用同样的方法自行扩展。


未来可以结合 `Jenkins` 部署起来，定期或每次代码提交后可自动运行测试，直接把测试报告发送到相应成员手中。

## 联系作者
- 头条：https://www.toutiao.com/c/user/3307855419/#mid=1588463609030669
- 知乎：https://zhuanlan.zhihu.com/xitest
- 微博：https://weibo.com/vb88
- CSDN：https://blog.csdn.net/mcfnhm
- QQ群：330374464
- 公众号：软件测试资源站
- by：西边人、马蚁蛋


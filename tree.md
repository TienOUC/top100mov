top100mov
├── scrapy.cfg                          # Scrapy部署时的配置文件，定义了配置文件路径、部署相关信息等内容
├── top100mov
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── items.cpython-38.pyc
│   │   ├── pipelines.cpython-38.pyc
│   │   └── settings.cpython-38.pyc
│   ├── items.py                        # Items定义抓取的数据结构
│   ├── middlewares.py                  # 定义Spider和Downloader的Middlewares中间件实现
│   ├── pipelines.py                    # 定义Item Pipeline的实现，即数据管道
│   ├── settings.py                     # 项目全局配置（其中 ROBOTSTXT_OBEY = True 设置是否遵守robots.txt rules）
│   └── spiders                         # 存放各个Spider
│       ├── __init__.py
│       ├── __pycache__
│       └── top100mv.py                 # 新建的Sipder文件
└── top100mv.json                       # 执行top100mv.py后输出的json格式数据文件
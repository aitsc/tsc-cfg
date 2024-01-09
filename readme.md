# 介绍
## Cfg
- 优势：可以构建出支持代码跳转的配置文件，同时还能保持类似yaml的层次结构，也可以模仿一般的json进行赋值/遍历/列表操作
## GlobalInfo
- 优势：建立了一个redis到本地的映射，可以通过redis的key来访问本地的变量，实时读写

# 安装
- 正常安装：`pip install tsc-cfg`
- 如果依赖包出现重大变化可以尝试：`pip install tsc-cfg[recommended]`

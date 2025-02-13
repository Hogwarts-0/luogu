# luogu
洛谷测试点文件生成工具
# 测试点文件生成工具
![Uploading image.png…]()


## 项目简介

该工具是一个 **Python** 编写的应用程序，用于自动生成 **编程题目** 的测试点文件。它的主要功能是：
- 根据用户提供的程序和输入数据，自动生成测试点文件。
- 适用于国内多个编程刷题平台（如洛谷等）的自动化评判工具。
- 支持输入输出格式规范化，避免数据格式错误。

## 功能

- 生成指定格式的输入文件 (`.in`) 和输出文件 (`.out`)。
- 支持用户上传代码并根据提供的输入数据自动生成对应的输出文件。
- 可以在自定义路径保存生成的文件。

## 特性

- **简单易用**：用户只需提交代码和输入数据，工具会自动生成对应的测试点文件。
- **多样化配置**：用户可以选择保存文件的路径，并能自动生成标准化的 `.in` 和 `.out` 文件。
- **图形化界面**：提供一个简洁的图形化界面，允许用户选择代码文件、输入数据，并指定输出路径。

## 安装与使用

### 1. 克隆仓库

```bash
git clone https://github.com/yourusername/testcase-generator.git
cd testcase-generator

2. 创建虚拟环境并安装依赖

python -m venv .venv
source .venv/bin/activate  # Windows：.venv\Scripts\activate
pip install -r requirements.txt

3. 运行程序

python main.py

或者使用打包后的 可执行文件（.exe）：

直接运行 testcase_generator.exe 文件，按照图形化界面操作。


4. 生成测试点文件

1. 点击 “选择代码文件” 按钮，选择要提交的程序。


2. 点击 “输入数据” 区域，输入需要测试的数据（例如 5\n3 1 4 1 5）。


3. 选择保存测试点文件的路径。


4. 点击 “生成” 按钮，工具会自动生成 001.in、001.out 等文件，保存到指定路径。



项目结构

testcase-generator/
│
├── main.py               # 主程序文件
├── requirements.txt      # Python 依赖包列表
├── README.md             # 项目自述文件

依赖

Python 3.x 或更高版本

Pillow：用于处理图标

tkinter：用于图形化界面

PyInstaller：用于打包成可执行文件


安装依赖：

pip install -r requirements.txt

打包为可执行文件

使用 PyInstaller 打包程序为 .exe 文件，步骤如下：

pyinstaller --noconsole --onefile --windowed --icon=app.ico main.py

常见问题

1. 运行时缺少 PIL 库？

在虚拟环境中运行以下命令：

pip install pillow

2. 生成的 .exe 无法正常启动？

确保程序打包后，所有依赖库都已正确安装，并且文件路径没有空格或特殊字符。

贡献

欢迎提交 issue 或 pull request，帮助我们改进该工具。对于任何问题或建议，欢迎通过 Issues 区域提出。

授权许可

本项目采用 MIT License 进行许可。

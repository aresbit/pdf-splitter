# PDF Splitter

按指定页数拆分PDF文件的命令行工具

## 安装

### 方法1：使用pip安装（开发模式）

```bash
cd pdf-splitter
pip install -e .
```
### 方法2：直接安装

```bash
cd pdf-splitter
pip install .
```
### 方法3：从GitHub安装（如果发布到GitHub）

```bash
pip install git+https://github.com/aresbit/pdf-splitter.git
```
## 使用

### 命令行使用

```bash
# 每10页拆分一次
pdf-split input.pdf 10

# 每5页拆分，输出到指定目录
pdf-split input.pdf 5 -o output_folder/

# 查看帮助
pdf-split -h
```
### Python代码中使用

```python
from pdf_splitter import split_pdf

# 拆分PDF
split_pdf('input.pdf', 10, 'output_folder/')
```
## 卸载

```bash
pip uninstall pdf-splitter
```

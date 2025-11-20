# PDF Splitter

按指定页数拆分PDF文件的命令行工具

## 开发

#### 使用 kimicc 开发
claude 输出的代码作为随机种子 输出到Claude.md， 
然后使用kimicc 修复直到项目可以运行。

### 安装：使用 uv + pipx 安装

```bash
  uv venv
  source .venv/bin/activate
  uv pip install PyPDF2
  kimicc
  uv pip install -e .
  pwd
  which pdf-split
  echo $PATH
  echo $VIRTUAL_ENV
  uv pip install pipx
  pipx ensurepath
  deactivate # 如果您在虚拟环境中
  z yyscode
  z pdf-splitter
  ll
  pipx install ./pdf-splitter
  pdf-split -h
  git init
  git add .
  git commit -m "fst pr"
  git remote add origin git@github.com:xxx/pdf-splitter.git
  git push -u origin master
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

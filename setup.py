from setuptools import setup, find_packages

setup(
name="pdf-splitter",
version="1.0.0",
description="按指定页数拆分PDF文件的命令行工具",
author="ares yang",
author_email="yangyang1120161122@gmail.com",
packages=find_packages(),
install_requires=[
"PyPDF2>=3.0.0",
],
entry_points={
'console_scripts': [
'pdf-split=pdf_splitter.cli:main',
],
},
python_requires='>=3.6',
classifiers=[
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
"Operating System :: POSIX :: Linux",
],
)
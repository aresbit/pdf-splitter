#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import os
import sys
from PyPDF2 import PdfReader, PdfWriter
import argparse

def split_pdf(input_file, pages_per_split, output_dir=None):
    """
    将PDF文件按指定页数拆分

    参数:
        input_file: 输入PDF文件路径
        pages_per_split: 每个输出文件包含的页数
        output_dir: 输出目录，默认为输入文件所在目录

    返回:
        bool: 成功返回True，失败返回False
    """
    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"错误: 文件 '{input_file}' 不存在")
        return False

    # 读取PDF文件
    try:
        reader = PdfReader(input_file)
        total_pages = len(reader.pages)
        print(f"PDF总页数: {total_pages}")
    except Exception as e:
        print(f"错误: 无法读取PDF文件 - {e}")
        return False

    # 设置输出目录
    if output_dir is None:
        output_dir = os.path.dirname(input_file)
        if not output_dir:
            output_dir = "."

    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 获取输入文件名（不含扩展名）
    base_name = os.path.splitext(os.path.basename(input_file))[0]

    # 开始拆分
    split_count = 0
    for start_page in range(0, total_pages, pages_per_split):
        end_page = min(start_page + pages_per_split, total_pages)
      
        # 创建新的PDF写入器
        writer = PdfWriter()
      
        # 添加页面
        for page_num in range(start_page, end_page):
            writer.add_page(reader.pages[page_num])
      
        # 生成输出文件名
        split_count += 1
        output_file = os.path.join(
            output_dir, 
            f"{base_name}_part{split_count:03d}.pdf"
        )
      
        # 写入文件
        try:
            with open(output_file, 'wb') as output_pdf:
                writer.write(output_pdf)
            print(f"已创建: {output_file} (页 {start_page + 1}-{end_page})")
        except Exception as e:
            print(f"错误: 无法写入文件 {output_file} - {e}")
            return False

    print(f"\n拆分完成! 共生成 {split_count} 个文件")
    return True

def main():
    parser = argparse.ArgumentParser(
        description='按指定页数拆分PDF文件',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
    示例:
    pdf-split input.pdf 10              # 每10页拆分一次
    pdf-split input.pdf 5 -o output/    # 每5页拆分，输出到output目录
    '''
    )

    parser.add_argument('input_file', help='输入PDF文件路径')
    parser.add_argument('pages', type=int, help='每个输出文件的页数')
    parser.add_argument('-o', '--output', 
                       help='输出目录（默认为输入文件所在目录）',
                       default=None)

    args = parser.parse_args()

    # 验证页数
    if args.pages <= 0:
        print("错误: 页数必须大于0")
        sys.exit(1)

    # 执行拆分
    success = split_pdf(args.input_file, args.pages, args.output)

    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
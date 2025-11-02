#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
arXiv 论文转 Markdown 格式工具
支持输入 arXiv 链接或 ID，输出指定格式的 markdown
"""

import re
import sys
import argparse
import arxiv

def extract_arxiv_id(input_string):
    """
    从输入字符串中提取 arXiv ID
    支持格式：
    - 2301.12345
    - arXiv:2301.12345
    - https://arxiv.org/abs/2301.12345
    - https://arxiv.org/pdf/2301.12345.pdf
    """
    patterns = [
        r'(\d{4}\.\d{4,5}(?:v\d+)?)',  # 2301.12345 或 2301.12345v1
        r'arXiv:(\d{4}\.\d{4,5}(?:v\d+)?)',  # arXiv:2301.12345
        r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5}(?:v\d+)?)',  # URL 格式
    ]
    
    for pattern in patterns:
        match = re.search(pattern, input_string)
        if match:
            return match.group(1)
    
    return None

def get_paper_info(arxiv_id):
    try:
        client = arxiv.Client()
        search = arxiv.Search(id_list=[arxiv_id])
        paper = next(client.results(search))
        return paper
    except Exception as e:
        print(f"Error: Cannot load - {e}", file=sys.stderr)
        return None

def extract_institutions(authors):
    """
    从作者信息中提取机构（arXiv API 可能不提供完整机构信息）
    """
    # arXiv API 通常不提供机构信息，返回占位符
    return "[Institution information not available from arXiv API - Please fill manually]"

def generate_markdown(paper, language='en'):
    """
    生成 markdown 格式
    
    Args:
        paper: arxiv.Result 对象
        language: 'en' 或 'zh'，控制输出语言
    """
    # 基本信息
    title = paper.title
    abstract = paper.summary.replace('\n', ' ').strip()
    authors = ", ".join([author.name for author in paper.authors[:5]])  # 只显示前5个作者
    if len(paper.authors) > 5:
        authors += ", et al."
    
    published_date = paper.published.strftime("%Y")
    arxiv_id = paper.get_short_id()
    paper_link = paper.entry_id
    pdf_link = paper.pdf_url
    
    if language == 'zh':
        one_liner_template = "[此论文的核心贡献或发现的简洁一句话总结]"
        institution_template = "[机构信息需要手动填写]"
        published_template = f"arXiv {published_date}"
        relevance_template = "[简要说明此论文为何与主题相关，以及它解决了什么具体问题]"
        code_template = "代码"
        project_template = "项目页面"
        authors_label = "作者："
        arxiv_id_label = "arXiv ID："
        abstract_label = "摘要"
        key_points_label = "要点"
        image_comment = "<!-- 您可以在此处嵌入论文中的关键图示或图表，强烈推荐 -->"
        image_desc = "图示描述：图示内容的简要描述"
    else:  # en
        one_liner_template = "[A concise, one-sentence summary of the paper's core contribution or findings.]"
        institution_template = "[Institution information not available from arXiv API - Please fill manually]"
        published_template = f"arXiv {published_date}"
        relevance_template = "[Briefly explain why this paper is relevant to the Awesome List's topic and what specific problem it addresses.]"
        code_template = "Code"
        project_template = "Project Page"
        authors_label = "Authors:"
        arxiv_id_label = "arXiv ID:"
        abstract_label = "Abstract"
        key_points_label = "Key points"
        image_comment = "<!-- You can embed a key figure or diagram from the paper here. It's highly recommended. -->"
        image_desc = "Image Description: A brief description of what the image shows."
    
    markdown = f"""**{title}**

* **{authors_label}** {authors}
* **{arxiv_id_label}** {arxiv_id}
*   **One-liner:** {one_liner_template}
*   **Institution(s):** {institution_template}
*   **Published in:** {published_template}
*   **Relevance:** {relevance_template}
*   **Links:** [[Paper]]({paper_link}) | [[PDF]]({pdf_link}) | [[{code_template}]](link_to_code_if_available) | [[{project_template}]](link_to_project_page_if_available)
<details>
    <summary>{abstract_label}</summary>
    
    {abstract}
</details>
<details>
    <summary>{key_points_label}</summary>
    
    some related figures and descriptions
    {image_comment}
        ![{image_desc}](path_to_your_image.png)
</details>

---
"""
    
    return markdown

def main():
    parser = argparse.ArgumentParser(
        description='将 arXiv 论文转换为 Markdown 格式',
        epilog='示例: python arxiv_to_markdown.py 2301.12345'
    )
    parser.add_argument(
        'input',
        nargs='?',
        help='arXiv ID 或链接（如 2301.12345 或 https://arxiv.org/abs/2301.12345）'
    )
    parser.add_argument(
        '-l', '--language',
        choices=['en', 'zh'],
        default='en',
        help='输出语言：en (英文) 或 zh (中文)，默认为英文'
    )
    parser.add_argument(
        '-o', '--output',
        help='输出文件路径（可选，默认输出到标准输出）'
    )
    
    args = parser.parse_args()
    
    if args.input:
        input_string = args.input
    else:
        if sys.stdin.isatty():
            parser.print_help()
            sys.exit(1)
        input_string = sys.stdin.read().strip()
    
    # 提取 arXiv ID
    arxiv_id = extract_arxiv_id(input_string)
    if not arxiv_id:
        print(f"错误：无法从输入中提取 arXiv ID: {input_string}", file=sys.stderr)
        sys.exit(1)
    
    print(f"正在获取论文信息: {arxiv_id}", file=sys.stderr)
    
    paper = get_paper_info(arxiv_id)
    if not paper:
        sys.exit(1)
    
    markdown = generate_markdown(paper, language=args.language)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(markdown)
        print(f"Markdown 已保存到: {args.output}", file=sys.stderr)
    else:
        print(markdown)

if __name__ == '__main__':
    main()


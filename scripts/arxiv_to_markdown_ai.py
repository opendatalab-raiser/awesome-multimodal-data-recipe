#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用 OpenAI API 自动生成 One-liner、Relevance 和 Key points
"""

import re
import sys
import os
import argparse
import arxiv
from openai import OpenAI

def extract_arxiv_id(input_string):
    """
    从输入字符串中提取 arXiv ID
    支持格式：
    - 2301.12345
    - arXiv:2301.12345
    - https://arxiv.org/abs/2301.12345
    - https://arxiv.org/pdf/2301.12345.pdf
    """
    # 尝试匹配各种格式的 arXiv ID
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
    """
    通过 arXiv API 获取论文信息
    """
    try:
        client = arxiv.Client()
        search = arxiv.Search(id_list=[arxiv_id])
        paper = next(client.results(search))
        return paper
    except Exception as e:
        print(f"错误：无法获取论文信息 - {e}", file=sys.stderr)
        return None

def generate_ai_content(paper, topic_context, language='en', api_key=None, base_url=None):
    """
    使用 OpenAI API 生成 One-liner、Relevance 和 Key points
    
    Args:
        paper: arxiv.Result 对象
        topic_context: 主题上下文（用于生成 Relevance）
        language: 'en' 或 'zh'
        api_key: OpenAI API key
        base_url: OpenAI API base URL（可选）
    
    Returns:
        dict: 包含 one_liner, relevance, key_points 的字典
    """
    if not api_key:
        api_key = os.environ.get('OPENAI_API_KEY')
    
    if not api_key:
        print("警告：未提供 OPENAI_API_KEY，将使用占位符", file=sys.stderr)
        return None
    
    # 如果没有提供 base_url，尝试从环境变量获取
    if not base_url:
        base_url = os.environ.get('OPENAI_BASE_URL')
    
    try:
        # 根据是否提供 base_url 创建客户端
        if base_url:
            client = OpenAI(api_key=api_key, base_url=base_url)
            print(f"使用自定义 API 端点: {base_url}", file=sys.stderr)
        else:
            client = OpenAI(api_key=api_key)
        
        title = paper.title
        abstract = paper.summary.replace('\n', ' ').strip()
        
        if language == 'zh':
            system_prompt = """你是一位专业的学术论文分析助手。请根据提供的论文标题和摘要，生成以下内容：
1. One-liner: 用一句话（不超过30个字）概括论文的核心贡献或发现
2. Relevance: 简要说明此论文的重要性和它解决的具体问题（2-3句话）
3. Key points: 列出3-5个关键要点，每个要点一行，使用项目符号

请以JSON格式返回，包含three个字段：one_liner, relevance, key_points（数组）"""
            
            user_prompt = f"""论文标题：{title}

摘要：{abstract}

主题上下文：{topic_context if topic_context else '通用AI/机器学习研究'}

请生成上述三个内容。"""
        else:
            system_prompt = """You are a professional academic paper analysis assistant. Based on the provided paper title and abstract, please generate:
1. One-liner: A concise one-sentence summary (max 30 words) of the paper's core contribution or findings
2. Relevance: Briefly explain why this paper is important and what specific problem it addresses (2-3 sentences)
3. Key points: List 3-5 key points, one per line, using bullet points

Please return in JSON format with three fields: one_liner, relevance, key_points (array)"""
            
            user_prompt = f"""Paper Title: {title}

Abstract: {abstract}

Topic Context: {topic_context if topic_context else 'General AI/Machine Learning Research'}

Please generate the three items above."""
        
        print("正在调用 OpenAI API 生成内容...", file=sys.stderr)
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.7,
            max_tokens=1000
        )
        
        import json
        result = json.loads(response.choices[0].message.content)
        
        # 格式化 key_points
        if isinstance(result.get('key_points'), list):
            key_points_text = '\n'.join([f"    - {point}" for point in result['key_points']])
        else:
            key_points_text = "    some related figures and descriptions"
        
        return {
            'one_liner': result.get('one_liner', ''),
            'relevance': result.get('relevance', ''),
            'key_points': key_points_text
        }
        
    except Exception as e:
        print(f"警告：AI 生成失败 - {e}", file=sys.stderr)
        return None

def generate_markdown(paper, language='en', ai_content=None):
    """
    生成 markdown 格式
    
    Args:
        paper: arxiv.Result 对象
        language: 'en' 或 'zh'，控制输出语言
        ai_content: AI 生成的内容字典（可选）
    """
    # 基本信息
    title = paper.title
    abstract = paper.summary.replace('\n', ' ').strip()
    authors = ", ".join([author.name for author in paper.authors[:5]])  # 只显示前5个作者
    if len(paper.authors) > 5:
        authors += ", et al."
    
    # 发布信息
    published_date = paper.published.strftime("%Y")
    arxiv_id = paper.get_short_id()
    paper_link = paper.entry_id
    pdf_link = paper.pdf_url
    
    # 根据语言选择模板
    if language == 'zh':
        one_liner_template = ai_content['one_liner'] if ai_content else "[此论文的核心贡献或发现的简洁一句话总结]"
        institution_template = "[机构信息需要手动填写]"
        published_template = f"arXiv {published_date}"
        relevance_template = ai_content['relevance'] if ai_content else "[简要说明此论文为何与主题相关，以及它解决了什么具体问题]"
        code_template = "代码"
        project_template = "项目页面"
        authors_label = "作者："
        arxiv_id_label = "arXiv ID："
        abstract_label = "摘要"
        key_points_label = "要点"
        image_comment = "<!-- 您可以在此处嵌入论文中的关键图示或图表，强烈推荐 -->"
        image_desc = "图示描述：图示内容的简要描述"
        key_points_content = ai_content['key_points'] if ai_content else "    相关图示和描述"
    else:  # en
        one_liner_template = ai_content['one_liner'] if ai_content else "[A concise, one-sentence summary of the paper's core contribution or findings.]"
        institution_template = "[Institution information not available from arXiv API - Please fill manually]"
        published_template = f"arXiv {published_date}"
        relevance_template = ai_content['relevance'] if ai_content else "[Briefly explain why this paper is relevant to the Awesome List's topic and what specific problem it addresses.]"
        code_template = "Code"
        project_template = "Project Page"
        authors_label = "Authors:"
        arxiv_id_label = "arXiv ID:"
        abstract_label = "Abstract"
        key_points_label = "Key points"
        image_comment = "<!-- You can embed a key figure or diagram from the paper here. It's highly recommended. -->"
        image_desc = "Image Description: A brief description of what the image shows."
        key_points_content = ai_content['key_points'] if ai_content else "    some related figures and descriptions"
    
    # 生成 markdown
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
    
{key_points_content}
    {image_comment}
        ![{image_desc}](path_to_your_image.png)
</details>

---
"""
    
    return markdown

def main():
    parser = argparse.ArgumentParser(
        description='将 arXiv 论文转换为 Markdown 格式（AI 增强版）',
        epilog='示例: python arxiv_to_markdown_ai.py 2301.12345 --ai'
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
    parser.add_argument(
        '--ai',
        action='store_true',
        help='使用 AI（gpt-4o-mini）自动生成 One-liner、Relevance 和 Key points'
    )
    parser.add_argument(
        '--api-key',
        help='OpenAI API Key（也可以通过 OPENAI_API_KEY 环境变量设置）'
    )
    parser.add_argument(
        '--base-url',
        help='OpenAI API Base URL（可选，也可以通过 OPENAI_BASE_URL 环境变量设置）'
    )
    parser.add_argument(
        '--topic',
        help='主题上下文（用于生成更相关的 Relevance），如 "大语言模型"、"计算机视觉" 等'
    )
    
    args = parser.parse_args()
    
    # 如果没有提供参数，尝试从标准输入读取
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
    
    # 生成 AI 内容（如果启用）
    ai_content = None
    if args.ai:
        ai_content = generate_ai_content(
            paper, 
            args.topic, 
            language=args.language,
            api_key=args.api_key,
            base_url=args.base_url
        )
        if ai_content:
            print("AI 内容生成成功！", file=sys.stderr)
    
    markdown = generate_markdown(paper, language=args.language, ai_content=ai_content)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(markdown)
        print(f"Markdown 已保存到: {args.output}", file=sys.stderr)
    else:
        print(markdown)

if __name__ == '__main__':
    main()


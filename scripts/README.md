# arXiv to Markdown Conversion Scripts

This directory contains Python scripts to automatically convert arXiv papers to properly formatted Markdown entries for the Awesome list.

## 📋 Prerequisites

```bash
pip install arxiv>=2.0.0
pip install openai  # Only needed for AI-enhanced version
```

## 🛠️ Scripts

### 1. Basic Converter (`arxiv_to_markdown.py`)

Converts arXiv papers to Markdown format with placeholders for manual filling.

**Usage:**

```bash
# Using arXiv ID
python arxiv_to_markdown.py 2304.08485

# Using arXiv URL
python arxiv_to_markdown.py https://arxiv.org/abs/2304.08485

# Chinese version
python arxiv_to_markdown.py 2304.08485 -l zh

# Save to file
python arxiv_to_markdown.py 2304.08485 -o paper.md
```

**Options:**
- `-l, --language`: Output language (`en` or `zh`), default: `en`
- `-o, --output`: Output file path (optional, default: stdout)

### 2. AI-Enhanced Converter (`arxiv_to_markdown_ai.py`)

Uses OpenAI API to automatically generate One-liner, Relevance, and Key points.

**Setup:**

```bash
# Set environment variables
export OPENAI_API_KEY='your-api-key-here'
export OPENAI_BASE_URL='your-base-url-here'  # Optional
```

**Usage:**

```bash
# Basic AI-enhanced conversion
python arxiv_to_markdown_ai.py 2304.08485 --ai

# With topic context for better relevance
python arxiv_to_markdown_ai.py 2304.08485 --ai --topic "multimodal data synthesis"

# Chinese version with AI
python arxiv_to_markdown_ai.py 2304.08485 --ai -l zh --topic "多模态数据合成"

# Pass API key directly
python arxiv_to_markdown_ai.py 2304.08485 --ai \
    --api-key your-api-key-here \
    --base-url your-base-url-here

# Save to file
python arxiv_to_markdown_ai.py 2304.08485 --ai -o paper.md
```

**Options:**
- `--ai`: Enable AI content generation
- `--api-key`: OpenAI API key (or use `OPENAI_API_KEY` env var)
- `--base-url`: OpenAI API base URL (or use `OPENAI_BASE_URL` env var)
- `--topic`: Topic context for better relevance generation
- `-l, --language`: Output language (`en` or `zh`), default: `en`
- `-o, --output`: Output file path (optional, default: stdout)

## 📝 Output Format

The scripts generate markdown entries in the following format:

```markdown
**[Paper Title]**

* **Authors:** [Author1, Author2, et al.]
* **arXiv ID:** [2304.08485]
*   **One-liner:** [Core contribution summary]
*   **Institution(s):** [Institution - needs manual filling]
*   **Published in:** arXiv [2024]
*   **Relevance:** [Why this paper matters]
*   **Links:** [[Paper]](link) | [[PDF]](link) | [[Code]](link) | [[Project Page]](link)
<details>
    <summary>Abstract</summary>
    
    [Abstract text]
</details>
<details>
    <summary>Key points</summary>
    
    - Key point 1
    - Key point 2
    - Key point 3
    <!-- You can embed a key figure or diagram from the paper here -->
        ![Image Description](path_to_your_image.png)
</details>

---
```

## 🔄 Manual Steps After Generation

Even with AI-enhanced conversion, you still need to manually:

1. **✏️ Fill in Institution(s)**: arXiv API doesn't provide institution information
2. **🔗 Add Code links**: If the paper has an official code repository
3. **🌐 Add Project Page**: If the paper has a project website
4. **🖼️ Add Key Figures**: Download important figures from the paper
5. **✅ Verify AI Content**: Check that AI-generated summaries are accurate
6. **📝 Add Section References**: Specify which sections describe data synthesis methods

## 💡 Tips

1. **Use the HTML version** of arXiv papers for easier text extraction:
   - HTML: `https://arxiv.org/html/2304.08485`
   - PDF: `https://arxiv.org/pdf/2304.08485.pdf`

2. **Provide topic context** when using AI to get more relevant descriptions:
   ```bash
   --topic "multimodal data synthesis for vision-language models"
   ```

3. **Review AI output** carefully - the AI only sees the abstract, not the full paper

4. **Check paper sections** to find:
   - Data synthesis methods (usually in Section 3 or "Data" sections)
   - Appendices for detailed prompts and methods
   - Experimental results and data scales

## ⚠️ Limitations

- **AI limitations**: The AI only reads the abstract, so it may miss important details in the full paper
- **Institution info**: arXiv API doesn't provide author affiliations
- **Code links**: Need to manually search for official repositories (usually on GitHub)
- **Accuracy**: Always verify that the paper actually describes data synthesis methods

## 📧 Troubleshooting

**Problem**: `ModuleNotFoundError: No module named 'arxiv'`
```bash
pip install arxiv
```

**Problem**: `AI generation failed - No API key provided`
```bash
export OPENAI_API_KEY='your-key-here'
```

**Problem**: PDF parsing failed
- Try using the HTML version of the paper instead
- Example: `https://arxiv.org/html/2304.08485`

## 🎯 Example Workflow

```bash
# 1. Convert paper with AI
python arxiv_to_markdown_ai.py 2304.08485 --ai --topic "multimodal data synthesis" -o temp.md

# 2. Review the output
cat temp.md

# 3. Manually fill in:
#    - Institution information
#    - Code/project links
#    - Download and add key figures
#    - Add specific section references

# 4. Copy to README.md or README_zh.md
```

## 📚 Further Reading

- [arXiv API Documentation](https://arxiv.org/help/api)
- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)
- [Markdown Guide](https://www.markdownguide.org/)

---

<p align="center">
  Made with ❤️ for the Awesome Multimodal Data Recipe community
</p>


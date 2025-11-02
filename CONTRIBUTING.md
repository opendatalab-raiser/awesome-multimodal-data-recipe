# Contribution Guidelines

Thank you for your interest in contributing to Awesome Multimodal Data Recipe! We welcome all forms of contributions.

## 🎯 How to Contribute

### ✅ Submitting a New Paper

Please ensure that your submission meets the following criteria:
- ✅ **Explicitly describes data synthesis methods** - The paper must detail how data is generated/synthesized, not just collected or filtered
- ✅ **Multimodal focus** - Specifically related to vision-language models and multimodal data
- ✅ **Published or preprint** - Published in a top-tier conference/journal or available as an arXiv preprint
- ✅ **Complete information** - Provides title, authors, links, and clear description of synthesis methods
- ✅ **Verified accuracy** - Ensure the synthesis method description is accurate and traceable to specific sections of the paper

### 📝 What We Include

**✅ DO Include:**
- Papers with detailed data synthesis pipelines (e.g., LLaVA, Oasis, Florence-2)
- Industrial technical reports describing data generation methods
- Methods that generate new annotations, captions, or instructions
- Programmatic data generation approaches
- LLM/VLM-based data synthesis methods

**❌ DO NOT Include:**
- Papers only about data collection or curation
- Pure data filtering/cleaning methods (unless part of synthesis pipeline)
- General model architectures without data synthesis details
- Benchmark/evaluation papers without synthesis methods
- Papers where synthesis methods are not explicitly described

### 🔄 Pull Request Process

1. **Fork** this repository
2. **Create a new branch**: `git checkout -b add-paper-[paper-name]`
3. **Add your entry** following the template below
4. **Submit a Pull Request (PR)** with a clear description, including:
   - The core contribution of the paper (especially the data synthesis method)
   - Why it is a valuable addition to this list
   - **Specific section references** where synthesis methods are described
   - Confirmation that you have verified all links are working

### 📋 Entry Template

Please use the following template when adding new papers:

```markdown
- **📄 [Paper Title]** [(arxiv XXXX.XXXXX)](arxiv_link)
  - **Data Synthesis Method** (Section X explicitly describes):
    - [Detailed description of HOW data is synthesized]
    - [Key techniques used]
    - [Data scale generated]
  - **Data Scale**: [Number] samples
  - **Experimental Results**: [Key findings]
  - **Open Source**: ✅/❌ [Links if available]
```

### 📐 Formatting Standards

- When adding entries, please **strictly adhere to the template format**
- **Cite specific sections** where synthesis methods are described (e.g., "Section 3.2", "Appendix B")
- Keep image sizes under **500KB** if adding figures
- Ensure all links are accessible and not broken
- Use emojis consistently: 📄 for papers, ✅ for open-source, ⚠️ for notes, 🔬 for methods, 📊 for data

### 🎖️ Quality Standards

We prioritize works that are:
- Published in **top-tier conferences** (e.g., NeurIPS, CVPR, ICLR, ACL, ICCV)
- From **leading tech companies** with detailed technical reports
- **Highly cited** or demonstrate significant impact
- Accompanied by **open-source code or data**
- Techniques with **practical application value**

### 🔍 Review Criteria

Your contribution will be reviewed based on:
1. **Accuracy**: Does the paper actually describe data synthesis methods?
2. **Relevance**: Is it directly related to multimodal data synthesis for VLMs?
3. **Clarity**: Is the description clear and includes specific section references?
4. **Completeness**: Are all required fields filled in?
5. **Formatting**: Does it follow the template?

## 📂 Repository Structure

```
awesome-multimodal-data-recipe/
├── README.md              # English version
├── README_zh.md           # Chinese version
├── CONTRIBUTING.md        # This file
├── LICENSE                # CC0-1.0 License
├── .gitignore             # Git ignore rules
└── assets/
    ├── images/           # Paper figures and diagrams
    ├── figures/          # Custom illustrations
    └── logos/            # Project logos
```

### 📁 Adding Images

If you want to add images:
1. Place images in the appropriate `assets/` subdirectory
2. Use descriptive filenames: `paper-[first-author]-[year]-[fig-number].png`
3. Example: `paper-radford-2021-fig1.png`
4. Keep file sizes under 500KB
5. Reference in markdown: `![Description](assets/images/paper-radford-2021-fig1.png)`

## 🌍 Language Versions

- When adding content, please update **both** English (`README.md`) and Chinese (`README_zh.md`) versions
- Maintain consistency between versions
- If you can only provide one language, maintainers will help translate

## 💬 Code of Conduct

- **Respect copyright**: Always respect the original authors' copyrights and provide proper attribution
- **Be objective**: Evaluate papers objectively and avoid personal bias
- **Be professional**: Maintain a professional and respectful tone in all discussions
- **Be accurate**: Verify information before submitting, especially synthesis method descriptions
- **No fabrication**: Never fabricate or exaggerate paper contributions

## 📧 Contact

For any questions or suggestions, please:
- **Open an issue** to start a discussion
- **Tag maintainers** in your PR for faster review
- **Provide context** when reporting issues

## 🙏 Thank You!

Your contributions help make this resource valuable for the entire multimodal AI research community. We appreciate your time and effort!

---

## 📝 Quick Checklist Before Submitting

- [ ] Paper explicitly describes data synthesis methods
- [ ] Specific section references provided
- [ ] All links tested and working
- [ ] Follows the template format
- [ ] Both README.md and README_zh.md updated (or noted that translation is needed)
- [ ] Commit message is clear and descriptive
- [ ] PR description explains the contribution

---

<p align="center">
  Made with ❤️ by the multimodal research community
</p>

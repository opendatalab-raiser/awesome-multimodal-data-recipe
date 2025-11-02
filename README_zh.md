# Awesome 多模态数据合成方法 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<div align="center">
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome">
  <img src="https://img.shields.io/github/stars/opendatalab-raiser/awesome-multimodal-data-recipe?style=flat-square" alt="Stars">
  <img src="https://img.shields.io/github/forks/opendatalab-raiser/awesome-multimodal-data-recipe?style=flat-square" alt="Forks">
  <img src="https://img.shields.io/github/license/opendatalab-raiser/awesome-multimodal-data-recipe?style=flat-square" alt="License">
  <img src="https://img.shields.io/github/last-commit/opendatalab-raiser/awesome-multimodal-data-recipe?style=flat-square" alt="Last Commit">
</div>

<p align="center">
  <a href="README.md">English</a> | <a href="README_zh.md">中文</a>
</p>

<p align="center">
  <b>精选的多模态数据合成方法、工具和资源列表，专注于视觉-语言模型</b>
</p>

---

## 📊 统计信息

- **论文总数：** 12篇（数据合成方法）
- **大厂报告：** 6篇（百度、微软、阿里巴巴、字节跳动）
- **数据合成方法：** 图像不变(12篇)
- **开源数据集：** 11个数据集完全开源

---

## 📋 目录

- [简介](#-简介)
- [大厂与开源项目的数据合成方法](#-大厂与开源项目的数据合成方法)
- [按图像处理方式分类](#-按图像处理方式分类)
  - [图像不变 - 文本增强](#图像不变---文本增强)
- [工具与框架](#-工具与框架)
- [基准数据集](#-基准数据集)
- [资源](#-资源)
- [贡献指南](#-贡献指南)

---

## 🎯 简介

多模态数据合成是提升视觉-语言模型(VLMs)性能的关键技术。本仓库收集并整理：

- 🏢 **大厂报告**：来自领先科技公司的详细数据合成pipeline和最佳实践
- 📚 **学术论文**：最先进的研究方法和创新技术
- 🛠️ **工具与框架**：实用的数据合成工具和代码库
- 📊 **数据集**：高质量的多模态数据集

**关键观察**：当前多模态数据合成主要遵循"图像不变+文本增强"范式，利用Web资源、工具API或其他大模型来提升图像-文本对的质量和多样性。

---

## 🏢 大厂与开源项目的数据合成方法

> 本节包含明确记录了数据合成pipeline的工作。**仅收录具有详细数据构建和合成方法描述的项目。**

### 百度 - 千帆-VL

<details>
<summary>点击展开</summary>

**论文**: [Qianfan-VL: Domain-Enhanced Universal Vision-Language Models](https://arxiv.org/abs/2509.18189)

**发布时间**: arXiv 2025年9月

**机构**: 百度AI云千帆团队

**📊 数据合成方法（Introduction & Section 3.2）**:

千帆-VL为关键企业场景开发了**comprehensive data synthesis pipelines**，涵盖六大任务类别：

**1. 合成范围**（Introduction明确指出）:
> "Our synthesis covers **six major task categories**: document OCR, mathematical problem-solving, chart understanding, table recognition, formula recognition, and natural scene OCR."

**任务类别**:
- **文档OCR**: 合成文档图像生成及标注
- **数学问题求解**: 自动化数学问题和解答生成
- **图表理解**: 程序化图表生成及QA对
- **表格识别**: 合成表格结构和内容生成
- **公式识别**: 数学公式渲染和标注
- **自然场景OCR**: 场景文字图像合成

**2. 合成方法**（Introduction）:
> "By **combining traditional computer vision models with programmatic generation techniques**, we create high-quality training data at scale."

**关键技术**:
- **传统CV模型**: 利用现有计算机视觉模型进行标注
- **程序化生成**: 使用基于代码的生成方法处理结构化内容
- **领域特定增强**: 针对每种任务类型的定制增强策略
- **质量验证机制**: 自动化质量检查确保数据可靠性

**3. 训练数据规模**（Section 3.1 - 四阶段渐进式训练）:
- 跨模态对齐: 100B tokens
- 通用知识注入: 2.66T tokens
- **领域增强: 0.32T tokens**（合成数据应用于此阶段）
- 指令微调: 1B tokens

**4. 质量保证**（Introduction）:
> "Each pipeline incorporates **domain-specific augmentation strategies and quality verification mechanisms** to ensure data reliability."

**模型变体与能力**:
- **Qianfan-VL-3B**: 32K上下文，优化用于边缘设备和实时OCR
- **Qianfan-VL-8B**: 32K上下文，带思维链，用于服务器和通用应用
- **Qianfan-VL-70B**: 32K上下文，带思维链，用于云端和复杂推理

**实验结果**:
- **OCRBench**: 873分（70B版本）
- **DocVQA**: 94.75%准确率（70B版本）
- **MathVista**: 78.6%分数（70B版本）
- 通用基准强劲表现: CCBench, SEEDBench_IMG, ScienceQA, MMStar

**训练基础设施**:
- 完全在百度**昆仑P800芯片**上训练
- 在5000+芯片集群上实现**>90%扩展效率**
- 验证了专有硬件训练SOTA模型的可行性

**✅ 技术报告**: 
- [arXiv:2509.18189](https://arxiv.org/abs/2509.18189)
- 领域增强多模态模型的综合方法论

**意义**:
- **多领域合成**: 覆盖六大关键企业任务类别
- **混合方法**: 结合CV模型和程序化生成
- **大规模应用**: 0.32T tokens的领域特定合成数据
- **质量优先**: 整个pipeline融入验证机制
- **企业就绪**: 为企业部署场景而设计

</details>

### 阿里巴巴 - Qwen-VL系列

<details>
<summary>点击展开</summary>

**论文**: 
- [Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond](https://arxiv.org/abs/2308.12966)

**📊 数据合成方法（Section 3.1.2）**:

Qwen-VL论文在Section 3.1.2描述了grounding数据构建：

1. **Grounding数据合成**（Section 3.1.2）:
   - 利用现有检测数据集（COCO, Objects365）的bbox标注
   - **将bbox坐标转换为归一化文本格式**（例如：`<box>0.1,0.2,0.3,0.4</box>`）
   - **生成指令**: 创建指令-响应对，如"在图像中找到X"
   - 这是一种将结构化标注转换为文本格式的数据合成方法

**⚠️ 注意**: 
- 这属于**数据格式转换和指令生成**，归类为数据合成
- 论文未完全公开prompt模板或生成方法
- 其他部分（数据来源、清洗）主要是数据收集和过滤，非合成

</details>

### 阿里巴巴 - MMEvol（2024）

<details>
<summary>点击展开</summary>

**论文**: [MMEvol: Empowering Multimodal Large Language Models with Evol-Instruct](https://arxiv.org/abs/2409.05840)

**机构**: 阿里巴巴达摩院（Fei Huang, Yongbin Li等）

**📊 数据合成方法（明确描述）**:

MMEvol提出了一种**多模态指令进化框架**，通过迭代提升数据质量和复杂度：

1. **核心方法 - Evol-Instruct范式**（基于文本领域的Evol-Instruct）:
   - 从初始种子数据**SEED-163K**开始
   - **迭代进化**: 通过多轮持续改进指令数据
   - 三个进化维度:
     a) **细粒度感知**: 挖掘图像中的详细信息
     b) **认知推理**: 扩展视觉推理步骤，增强推理能力
     c) **交互进化**: 提升指令类型的多样性

2. **数据进化Pipeline**:
   - 初始指令 → 进化操作 → 更复杂/多样的指令
   - 系统化扩展指令类型多样性
   - 逐步提升视觉推理复杂度
   - 深入探索图像中的细粒度信息

3. **实验结果**（Section 5）:
   - 相比基线模型（使用种子数据），**平均准确率提升3.1个百分点**
   - **在9个任务上达到SOTA**，使用更少数据
   - 在13个视觉-语言任务上全面评估

**数据规模**:
- 初始种子: SEED-163K
- 通过进化生成更多样化和复杂的数据

**✅ 论文**: 
- [arXiv:2409.05840](https://arxiv.org/abs/2409.05840)
- 最新版本: v5（2024年12月31日）

**与Oasis的关系**:
- Oasis论文将MMEvol作为对比方法之一
- MMEvol专注于迭代进化已有数据，而Oasis专注于从单图生成数据
- 两种方法都能提升数据多样性和质量

</details>

### 字节跳动 - Oasis

<details>
<summary>点击展开</summary>

**论文**: [Oasis: One Image is All You Need for Multimodal Instruction Data Synthesis](https://arxiv.org/html/2503.08741v2)

**📊 数据合成方法（Section 3.2详细描述）**:

**这是最新的突破性工作！** Oasis提出了一种极简的数据合成方法，灵感来自Magpie，但应用于多模态领域：

1. **核心创新 - "Hooking" Prompt**（Section 3.2 Step 1）:

   **关键突破**:
   - **只输入图像**，不需要任何文本prompt！
   - 让MLLM（如Qwen2-VL）自己生成instruction
   - 利用模型的自回归特性，基于图像自动生成多样化的问题

   **为什么有效**:
   - 打破传统的固定prompt模式，大幅提升数据多样性
   - 模型根据自己的知识库生成问题，覆盖面更广
   - 简单高效，不需要人工设计复杂的prompt

2. **数据分类**（Section 3.2 Step 2）:
   - 使用LLM过滤掉非指令类数据（如纯描述性文本）
   - 确保生成的都是question-answer格式

3. **四维质量控制**（Section 3.2 Step 3，附录B.2完整公开）:

   论文设计了严格的质量评估标准（1-5分）：

   a) **Solvability（可解性）**: 图像是否包含足够信息回答问题
   b) **Hallucination（幻觉）**: 问题是否与图像内容一致
   c) **Clarity（清晰度）**: 问题表述是否明确
   d) **Nonsense（无意义）**: 问题是否语法正确、逻辑合理

   - 每个维度都有详细的评分标准（附录B.2完整prompt）
   - 多维度综合评估，确保高质量

**数据规模**:
- 生成了500K高质量指令数据
- 在LLaVA-NeXT上验证有效性

**领域定制能力**:
- 由于只依赖图像，可以通过控制图像来源来生成特定领域数据
- 论文展示了OCR领域的案例（Section 4.3）

**实验结果**（Section 4.2）:
- 在14个benchmark上显著提升性能
- 优于其他数据合成方法（包括LLaVA、ALLAVA、MMEvol等）

**Oasis论文中提到的对比方法**（Section 4.2）:
- **LLaVA** [24]: GPT-4辅助生成（见下方"LLaVA系列"条目）
- **MMEvol** [29]: 阿里巴巴达摩院的图像-文本指令进化框架（见上方"阿里巴巴 - MMEvol"条目）
- **ALLaVA** [4]: Captioning-then-QA方式（见下方"按图像处理方式分类"条目）

**Oasis灵感来源**:
- **Magpie** [43]: 文本领域自对齐指令生成方法（启发了Oasis的"hooking prompt"核心思想）
  - Oasis将Magpie的思想扩展到多模态领域，实现了仅用图像的指令生成

**✅ 完全开源**: 
- 论文承诺开源500K数据和模型
- 所有质量控制的prompt都在附录B公开

**重要性**:
- **极简方法论**: 只需要图像，不需要caption或其他文本
- **质量保证**: 四维质量控制非常系统
- **可复现**: 所有prompt和方法都完整公开

</details>

### 微软 - Florence-2

<details>
<summary>点击展开</summary>

**论文**: [Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks](https://arxiv.org/abs/2311.06242)

**发布时间**: arXiv 2023年11月

**机构**: Azure AI, Microsoft

**📊 数据合成方法（Introduction & Section 2）**:

Florence-2开发了一个**自动化数据引擎**来生成大规模**FLD-5B**数据集：

1. **数据规模**（Abstract）:
   - **54亿comprehensive visual annotations**
   - 覆盖**1.26亿images**
   - 最大规模的自动标注多模态数据集之一

2. **自动化数据引擎 - 双模块Pipeline**（Introduction，第2页）:

   **模块1 - 协作自动标注**:
   > "uses specialized models to collaboratively and autonomously annotate images, moving away from the traditional single and manual annotation approach. Multiple models work together to reach a consensus"
   
   - 利用多个专门模型协作进行图像标注
   - 模型通过多模型一致性达成共识（受"群体智慧"概念启发）
   - 确保更可靠和无偏的图像理解
   - 完全自动化，消除人工标注需求

   **模块2 - 迭代精炼与过滤**:
   > "iteratively refines and filters these automated annotations using well-trained foundational models"
   
   - 使用训练良好的基础模型迭代精炼和过滤标注
   - **迭代策略**: 模型标注 → 精炼 → 模型重训练 → 再标注循环
   - 持续提升标注质量

3. **标注覆盖范围**（Introduction）:
   FLD-5B数据集涵盖多个视觉任务：
   - **图像captioning**（各种语义粒度）
   - **物体检测**（空间层次理解）
   - **Grounding**（文本-区域对齐）
   - **分割**（细粒度视觉理解）

4. **核心创新**:
   - **完全自动化pipeline**: 无需人工标注
   - **多任务统一格式**: 所有标注转换为文本格式用于统一学习
   - **迭代改进**: 通过模型-标注共同进化持续提升质量
   - **Billion级规模**: 达到前所未有的标注规模

**模型架构**:
- Sequence-to-sequence (seq2seq)结构
- 统一的基于prompt的表示用于多种视觉任务
- 单一模型处理多个任务，无需任务特定架构修改

**实验结果**:
- **Zero-shot SOTA**: 在COCO captioning、Flickr30k visual grounding、RefCOCO/+/g referring expression comprehension上达到新的zero-shot SOTA
- **迁移学习**: 大幅超越ImageNet预训练，在COCO和ADE20K数据集上提升6.9、5.5和5.9个点
- **训练效率**: 比监督预训练快4×

**✅ 开源**: 
- 模型: 在HuggingFace可用
- 代码: [Microsoft Florence](https://github.com/microsoft/Florence)

**意义**:
- **工业规模数据引擎**: 展示了完全自动化大规模标注的可行性
- **多任务合成**: 统一方法生成多种标注类型
- **通过共识保证质量**: 多模型协作确保标注可靠性

</details>

### LLaVA系列（威斯康星大学麦迪逊分校 & 微软）

<details>
<summary>点击展开</summary>

**论文**: 
- [Visual Instruction Tuning (LLaVA)](https://arxiv.org/abs/2304.08485)
- [Improved Baselines with Visual Instruction Tuning (LLaVA-1.5)](https://arxiv.org/abs/2310.03744)

**📊 数据合成方法（Section 3详细描述）**:

**多模态数据合成领域最有影响力的工作之一！** LLaVA论文Section 3 "GPT-assisted Visual Instruction Data Generation"提供了完整的pipeline细节：

1. **数据生成Pipeline**（图2展示完整流程）:
   
   **输入材料**:
   - COCO图像
   - COCO人工标注captions（每张图5个）
   - COCO bbox标注

   **使用GPT-4生成三类数据**:
   
   a) **Conversation**（多轮对话，58K）:
   - Prompt模板: 附录A.2.1提供完整prompt
   - 输入: Caption列表
   - 输出: 关于图像内容的多轮Q&A

   b) **Detailed Description**（详细描述，23K）:
   - Prompt模板: 附录A.2.2
   - 要求GPT-4生成比原始captions更详细的描述

   c) **Complex Reasoning**（复杂推理，77K）:
   - Prompt模板: 附录A.2.3
   - 基于bbox，生成需要推理的问题（如计数、空间关系）

2. **完整数据规模**:
   - 总计: 158K指令-响应对
   - 基于约80K COCO图像

3. **Prompt工程细节**（附录完整公开）:
   - 附录A完整公开所有prompt模板
   - 包含system prompts、few-shot示例
   - 完全可复现

**LLaVA-1.5数据改进**:
- 添加更多学术任务数据集（VQAv2, GQA, OKVQA等）
- 增强数据多样性
- 保持相同生成方法

**✅ 数据完全开源**: 
- [HuggingFace Dataset](https://huggingface.co/datasets/liuhaotian/LLaVA-Instruct-150K)
- Prompt模板直接可用

**影响**: 
这种方法几乎被所有后续开源VLM项目采用或改进（ShareGPT4V、SVIT、InternVL等都基于此范式）。

</details>

---

## 📂 按图像处理方式分类

### 图像不变 - 文本增强

这类方法保持原始图像不变，通过各种技术丰富和改进配对文本质量。**这是目前最主流的多模态数据合成范式。**

> **注意**: 仅收录明确描述数据合成/生成方法的论文，并标注具体的合成组件。

#### 🔬 基于大模型的文本生成

> **核心思想**: 使用强大的VLMs（如GPT-4V）或LLMs（如GPT-4）为图像生成更高质量的captions/对话数据

- **📄 ShareGPT4V** [(arxiv 2311.12793)](https://arxiv.org/abs/2311.12793)
  - **数据合成方法**（Section 3.1）:
    - 使用**GPT-4V**为100K图像生成高质量captions
    - Prompt设计: 要求详细描述（比原始captions详细3-5倍）
    - 图像来源: 从COCO、SAM、LAION等精选图像
  - **数据规模**: 100K高质量captions
  - **开源**: ✅ [Dataset](https://huggingface.co/datasets/Lin-Chen/ShareGPT4V) | [Code](https://github.com/InternLM/InternLM-XComposer/tree/main/projects/ShareGPT4V)
  
- **📄 SVIT** [(arxiv 2307.04087)](https://arxiv.org/abs/2307.04087)
  - **数据合成方法**（Section 3.2）:
    - 使用**GPT-4**生成大规模视觉指令数据
    - 4.2M对话 + 1.6M复杂推理
    - 基于多个数据集的captions（COCO, VG, CC3M等）
  - **数据规模**: 5.8M指令数据
  - **开源**: ✅ [Dataset](https://huggingface.co/datasets/BAAI/SVIT)

- **📄 CapsFusion** [(arxiv 2310.20550)](https://arxiv.org/abs/2310.20550)
  - **数据合成方法**（Section 3）:
    - **融合多个captioning模型的输出**（BLIP-2, CoCa, GPT-4V等）
    - 使用加权融合策略，结合不同模型的优势
    - 为DataComp-1B重新生成captions
  - **数据规模**: Billion级重新captioning
  - **开源**: ✅ [Code](https://github.com/baaivision/CapsFusion)

#### 🤖 基于VLM/LLM的合成文本生成

> 以下论文明确描述了如何使用大模型为图像生成合成captions/对话

- **📄 LLaVAR** [(arxiv 2306.17107)](https://arxiv.org/abs/2306.17107)
  - **数据合成方法**（Section 3.2）:
    - 针对富文本图像（文档、海报、图表等）
    - 使用**GPT-4**基于OCR结果生成指令Q&A对
    - 生成"理解+推理"类型问题（不只是读文本）
  - **数据规模**: 422K指令数据
  - **开源**: ✅ [Code](https://github.com/SALT-NLP/LLaVAR)

- **📄 ALLaVA** [(arxiv 2402.11684)](https://arxiv.org/abs/2402.11684)
  - **数据合成方法**（Abstract明确描述）:
    - **Captioning-then-QA范式**: 两阶段数据生成
    - 使用**GPT-4V**生成两类数据:
      a) **细粒度图像标注**用于视觉-语言对齐
      b) **复杂推理的视觉问答对**用于视觉指令微调
    - 完整的数据生成pipeline，利用强大的专有模型合成高质量数据
  - **数据规模**: 1.3M样本
  - **实验结果**: 在4B规模模型中达到竞争力性能，甚至在部分benchmark上与7B/13B模型相当
  - **开源**: ✅ 数据集开源（论文中提到）

- **📄 COGS** [(arxiv 2510.15040)](https://arxiv.org/abs/2510.15040)
  - **数据合成方法**（Abstract明确描述）:
    - **Composition-Grounded Instruction Synthesis（组合式指令合成）**
    - 从**少量种子问题**开始，通过分解-重组生成大规模数据:
      a) **分解**: 将种子问题分解为原始感知和推理因子
      b) **重组**: 将因子与新图像系统地重组
      c) **生成**: 创建大量合成问答对，每个配有子问题和中间答案
    - 支持因子级过程奖励的强化学习
  - **应用领域**: 图表、网页、渲染文档等人工图像领域
  - **实验结果**: 在未见问题上大幅提升，推理密集型和组合性问题提升最大，跨数据集迁移效果好
  - **发布时间**: arXiv 2025年10月
  - **机构**: MIT、IBM Research等

#### 🛠️ 工具辅助标注生成（用于数据合成）

> 以下工具常用于数据合成pipeline

- **📄 All-Seeing Project** [(arxiv 2308.01907)](https://arxiv.org/abs/2308.01907)
  - **数据合成方法**（Section 3）:
    - 使用SAM、RAM、Tag2Text等工具自动生成多层级标注
    - Pipeline: 图像 → 分割+Tags → 区域描述 → 指令数据
    - 构建AS-1B数据集（12亿region-text对）
  - **这是真正的数据合成**: 使用工具组合生成新标注
  - **开源**: ✅ [Dataset](https://huggingface.co/datasets/OpenGVLab/all-seeing) | [Code](https://github.com/OpenGVLab/all-seeing)


---

## 🧠 跨领域方法论启发

> **说明**: 本节收录来自相邻领域（如LLM推理、数学数据筛选）的有影响力工作，这些工作的**数据筛选与质量评估方法论**为多模态场景提供了有价值的可迁移框架。虽然不是直接的VLM论文，但它们在数据质量评估、混合优化和高效过滤管道方面的系统化方法为多模态数据从业者提供了重要启发。

### 📚 基础模型中期训练与数据筛选

<details>
<summary><b>OctoThinker: 中期训练激励强化学习扩展</b> - 系统化的数据筛选、质量评估与混合优化</summary>

**论文**: [OctoThinker: Mid-training Incentivizes Reinforcement Learning Scaling](https://arxiv.org/abs/2506.20512)

**机构**: 上海交通大学 GAIR Lab (Wang等)

**发布时间**: arXiv 2025年6月

**领域**: 数学推理 / LLM中期训练

**🔬 为何与VLM数据筛选相关？**

**核心贡献**: 本文**并非关于数据合成/生成**，而是关于**系统化的数据质量评估、大规模过滤/筛选和混合优化**。虽然专注于文本领域的数学推理，OctoThinker提供了一个严谨的实验框架，用于从现有语料中评估和选择高质量数据——这些方法高度可迁移到多模态场景，特别是从噪声网络源中筛选十亿级数据集时。

---

**📊 核心可迁移洞察**:

**1. 两阶段质量评估管道**
- **方法**: LLM标注(0-5分) → 训练高效分类器(FastText) → 大规模过滤(阈值0.4) → 可选LLM精炼
- **关键发现**: 预处理至关重要；阈值0.4平衡质量-数量权衡（前人使用0.9）
- **成果**: MegaMath-Web-Pro-Max (73.8B tokens, 是MegaMath-Web-Pro 13B的5.5倍)
- **VLM迁移**: 构建多模态标注schema以评估视觉-语言对齐质量、信息密度和组合推理复杂度；训练轻量级跨模态判别器（冻结视觉编码器）实现成本可控的十亿级数据筛选，同时保持高保真过滤能力

**2. 系统化数据混合优化**
- **严格测试**: 跨多个维度测试10%、20%、30%、40%比例
- **最优发现**: 30% QA数据（超过后因冗余而收益递减）
- **核心洞察**: *"训练数据与下游任务的分布差距显著影响性能"*
- **VLM迁移**: 建立受控实验框架，系统性变化caption粒度（实体级 vs 场景级 vs 推理级）、数据来源（网页爬取 vs 人工标注 vs 模型合成）和跨模态交互模式；采用网格搜索结合严格下游评估，而非启发式混合

**3. 分布对齐 > 数据规模**
- **观察**: 结构化QA数据集(OpenR1, OMI2)在竞赛风格基准上优于网页来源QA(MegaMath-QA)，原因是分布对齐而非数据体量
- **原则**: 匹配预训练分布到下游任务格式，而非仅匹配领域
- **VLM迁移**: 优先考虑分布感知的数据筛选而非体量最大化——文档理解受益于文本密集的多样排版布局而非自然图像；视觉推理需要多跳关系标注而非描述性captions；领域特定应用要求模态一致且结构对齐的预训练语料

**4. 少量"稳定剂"数据影响巨大**
- **发现**: 少量(1-10%)高质量指令数据解锁其他数据类型的潜力
- **效果**: 稳定训练，减少长格式数据不稳定性，使RL扩展成功
- **VLM迁移**: 引入小比例高质量视觉-语言对齐数据(1-10%)以正则化训练动态，特别是在扩展到密集长文本captions或复杂多图推理场景时；充当分布锚点防止模式坍塌和表征漂移

---

**🎯 总结: VLM数据从业者的关键要点**

| # | 原则 | OctoThinker方法 | VLM应用 |
|---|------|----------------|---------|
| 1 | **质量 > 数量** | 过滤后的MegaMath-Web-Pro-Max >> 原始语料 | 精筛选的高精度数据对在下游迁移中显著优于原始网络规模噪声语料 |
| 2 | **高效过滤** | LLM标注 → FastText分类器 → 规模化 | 可扩展两阶段管道实现十亿级筛选并保持计算效率 |
| 3 | **系统化实验** | 测试10%, 20%, 30%, 40%比例 | 在数据混合超参数空间进行网格搜索与严格消融研究 |
| 4 | **收益递减** | 超过30% QA，冗余有害 | 识别边际效用因分布冗余而递减的饱和点 |
| 5 | **分布对齐** | 匹配下游任务格式 | 数据格式与任务对齐比领域匹配更重要 |
| 6 | **稳定剂数据** | 1-10%指令数据解锁QA潜力 | 小比例正则化数据防止训练不稳定并实现扩展 |
| 7 | **格式意识** | 长CoT = 高能力 + 不稳定性 | 高容量密集输出需要稳定机制以防止模式坍塌 |
| 8 | **两阶段哲学** | 基础 (90%) → 专门化 (10%) | 广泛的分布覆盖后进行针对性能力专门化 |
| 9 | **预处理很重要** | 对分类器性能至关重要 | 系统化归一化和伪影消除对判别器泛化能力至关重要 |
| 10 | **实证验证** | 阈值在下游任务上验证 | 超参数选择由下游任务性能指导而非代理指标 |

---

**📈 规模与资源**:
- **基础模型**: Llama-3.2-1B/3B/8B
- **中期训练预算**: 最多200B tokens (稳定阶段) + 20B tokens (衰减阶段)
- **最终语料**: MegaMath-Web-Pro-Max (73.8B tokens, 是MegaMath-Web-Pro的5.5倍)
- **消融研究**: 系统化的受控实验，涵盖数据质量、混合比例、QA来源和格式特征
- **性能提升**: 比基础模型提升10-20%，RL后匹配Qwen2.5

**🔗 资源**:
- ✅ **论文**: [arXiv:2506.20512](https://arxiv.org/abs/2506.20512)
- ✅ **代码**: [GitHub - GAIR-NLP/OctoThinker](https://github.com/GAIR-NLP/OctoThinker)
- ✅ **模型**: [HuggingFace - OctoThinker](https://huggingface.co/OctoThinker)
- ✅ **数据集**: MegaMath-Web-Pro-Max (70B+ tokens, 承诺开源)
- ✅ **完全公开**: 论文附录详述所有prompts和方法

**💡 潜在的VLM后续工作**:
- 系统化的视觉-语言数据混合优化
- 高效多模态质量分类器
- 针对特定领域的分布对齐合成caption生成
- 带有专门化分支的两阶段VLM预训练

</details>

---

## 🛠️ 工具与框架

### 📦 数据合成工具

| 工具 | 描述 | 链接 |
|------|------|------|
| GPT-4V API | 高质量caption/指令生成的行业标准 | [官方文档](https://platform.openai.com/docs/guides/vision) |
| LLaVA Toolkit | 完整的指令数据生成pipeline | [GitHub](https://github.com/haotian-liu/LLaVA) |
| SAM (Segment Anything) | 用于自动分割标注 | [官网](https://segment-anything.com/) |
| RAM/Tag2Text | 用于自动图像标签 | [GitHub](https://github.com/xinyu1205/recognize-anything) |

### 🔧 数据处理框架

| 框架 | 描述 | 链接 |
|------|------|------|
| MMEval | 多模态模型评估框架 | [GitHub](https://github.com/open-compass/MMEval) |
| LLaVA-NeXT | 下一代视觉-语言助手 | [官网](https://llava-vl.github.io/) |

---

## 📊 基准数据集

### 🎯 指令跟随基准

| 基准 | 描述 | 链接 |
|------|------|------|
| MMBench | 综合多模态能力评估 | [GitHub](https://github.com/open-compass/MMBench) |
| SEED-Bench | 层次化多模态理解评估 | [GitHub](https://github.com/AILab-CVC/SEED-Bench) |
| LLaVA-Bench | 野外指令跟随评估 | [GitHub](https://github.com/haotian-liu/LLaVA) |

### 📝 任务特定基准

| 基准 | 描述 | 链接 |
|------|------|------|
| VQAv2 | 视觉问答 | [官网](https://visualqa.org/) |
| GQA | 组合推理评估 | [官网](https://cs.stanford.edu/people/dorarad/gqa/) |
| MMMU | 多模态多任务理解 | [官网](https://mmmu-benchmark.github.io/) |

---

## 🎓 资源

### 💡 重要启发性工作

| 论文 | 年份 | 重要性 | 链接 |
|------|------|--------|------|
| Magpie: Alignment Data Synthesis from Scratch | 2024 | Oasis的核心灵感来源，文本领域的自对齐指令生成方法 | [arXiv](https://arxiv.org/abs/2406.08464) |

> ⚠️ **注意**: Magpie本身是纯文本LLM的方法，不是多模态数据合成

### 📖 综述论文（涵盖数据合成）

| 论文 | 年份 | 重点内容 | 链接 |
|------|------|----------|------|
| A Survey on Multimodal Large Language Models | 2023 | Section 3.2专门讨论训练数据构建 | [arXiv](https://arxiv.org/abs/2306.13549) |
| Multimodal Foundation Models: From Specialists to General-Purpose Assistants | 2024 | 包含数据收集和合成方法综述 | [arXiv](https://arxiv.org/abs/2309.10020) |

### 🔗 相关Awesome列表

| 列表 | 描述 | 链接 |
|------|------|------|
| Awesome Data for LLM | LLM数据工程（文本领域） | [GitHub](https://github.com/weAIDB/awesome-data-llm) |
| Awesome Scientific Datasets and LLMs | 科学领域数据集 | [GitHub](https://github.com/open-sciencelab/Awesome-Scientific-Datasets-and-LLMs) |
| Awesome Multimodal ML | 综合多模态ML资源 | [GitHub](https://github.com/pliang279/awesome-multimodal-ml) |

### 📝 重要博客

| 博客 | 描述 | 链接 |
|------|------|------|
| LLaVA Blog | LLaVA系列数据生成方法详解 | [官网](https://llava-vl.github.io/) |
| HuggingFace Blog | 多模态数据和模型教程 | [官网](https://huggingface.co/blog) |

---

## 🤝 贡献指南

我们欢迎各种形式的贡献！包括但不限于：

- 🆕 添加新论文、工具或数据集
- 📝 改进现有条目的描述
- 🐛 修正错误或过时信息
- 💡 提出改进建议

### 如何贡献

1. Fork本仓库
2. 创建特性分支（`git checkout -b feature/AmazingFeature`）
3. 提交更改（`git commit -m 'Add some AmazingFeature'`）
4. 推送到分支（`git push origin feature/AmazingFeature`）
5. 开启Pull Request

### 贡献指南

- 添加新条目时，请确保包含：
  - 📄 论文/工具名称和链接
  - 📝 清晰简洁的描述（1-2句话）
  - 🔗 相关链接（代码、数据集、博客等）
- 保持条目按字母顺序或重要性排序
- 确保链接有效且指向官方资源
- 使用中文进行描述

---

## ⭐ Star历史

如果这个项目对您有帮助，请给我们一个Star ⭐️！

[![Star History Chart](https://api.star-history.com/svg?repos=opendatalab-raiser/Awesome-Multimodal-Data-Recipe&type=Date)](https://star-history.com/#opendatalab-raiser/Awesome-Multimodal-Data-Recipe&Date)

---

## 📄 许可证

本项目采用[CC0-1.0 License](LICENSE)。

---

## 🙏 致谢

感谢所有为多模态数据合成领域做出贡献的研究人员和工程师！

特别感谢以下项目的启发：
- [awesome-data-llm](https://github.com/weAIDB/awesome-data-llm)
- [Awesome-Scientific-Datasets-and-LLMs](https://github.com/open-sciencelab/Awesome-Scientific-Datasets-and-LLMs)

---

<p align="center">
  由多模态研究社区用 ❤️ 制作
</p>


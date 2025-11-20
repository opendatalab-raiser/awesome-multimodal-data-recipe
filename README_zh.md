# Awesome 多模态数据合成方法 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<div align="center">
  <img src="https://img.shields.io/github/stars/opendatalab-raiser/awesome-multimodal-data-recipe" alt="Stars">
  <img src="https://img.shields.io/github/forks/opendatalab-raiser/awesome-multimodal-data-recipe" alt="Forks">
  <img src="https://img.shields.io/github/license/opendatalab-raiser/awesome-multimodal-data-recipe" alt="License">
  <img src="https://img.shields.io/github/last-commit/opendatalab-raiser/awesome-multimodal-data-recipe" alt="Last Commit">
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome">
</div>

<p align="center">
  <a href="README.md">English</a> | <a href="README_zh.md">中文</a>
</p>

<p align="center">
  <b>精选的多模态数据合成方法与资源列表，专注于视觉-语言模型</b>
</p>

---

## 统计信息

- **论文总数：** 101篇（数据合成/构建方法）
- **大厂报告：** 9篇（百度、微软、阿里巴巴、字节跳动、腾讯等）
- **数据合成方法：**
  - 图像生成 - 合成新视觉内容(22篇): 几何/数学推理 + 文档/文本密集场景(OCR-free场景文本、文档布局分析) + 场景文本检测 + 多模态对话(any-to-any生成式合成) + 文本驱动图像合成 + ChatGPT引导合成 + 自动驾驶 + 完全合成图文生成 + 3D物理仿真 + 3D场景合成(3D视觉指令数据) + 机器人动作合成
  - 图像编辑(5篇): 非刚性运动、统一编辑、指称表达式引导编辑、生成式视觉指令微调
  - 组合性/偏好导向合成(6篇): 增强组合理解能力 + 多概念组合 + 多图像定制 + 难负样本对比学习 + 多模态反事实样本 + 3D物理仿真VLC增强
  - 交错图文·连贯性与一致性(5篇): 多视角质量过滤 + 迭代精炼 + 多模态嵌入相关性识别 + 教学视频提取(视频转教科书)
  - 图像介入推理(2篇): 图像主动参与推理过程 + 大规模推理轨迹合成
  - VLM自我改进与强化学习(4篇): 校准自奖励VLM + 游戏化自对弈框架 + 图表理解自我改进(代码驱动合成)
  - 图像不变 - 文本增强(48篇): 固定图像，仅丰富文本 + 自适应权重合成标注 + 医学领域纯合成数据 + 成本高效LVLM数据精化 + 空间推理增强 + VLM个性化 + 持续学习 + 多模态RAG训练 + 自指导代码格式化 + 多语言嵌入增强 + MLLM数据生成器 + 程序化指令生成 + 信息瓶颈概念选择 + 图像理解自训练 + 多模态指令遵循(约束驱动) + 组合图像检索三元组合成 + 多模态问答生成(风格与模态可控) + 图表理解(GPT-4驱动多任务指令生成) + 科学图表理解(GPT-4V生成QA) + 领域自适应后训练(开源MLLM驱动生成-过滤) + 任务类型层级扩展(GPT-4o自动化生成)
  - 视频 - 指令微调（合成数据）(1篇): 基于视频的指令跟随（描述+QA）
  - 跨领域方法论洞察(2篇): 多模态模型坍塌分析 + 合成数据质量评估
- **典型数据集：**
  - 4个交错图文数据集（OmniCorpus、OBELICS、MMC4、CoMM）
  - 2个领域特定数据集（MMM-RS、MESED）
  - 4个图像编辑数据集（ByteMorph-6M、ImgEdit、RefEdit、RefCOCO-Edit）
  - 4个大规模通用训练数据集
  - 5个图表推理数据集（ChartInstruct、Synthesize Step-by-Step、ECD、ChartGen、MMC-Instruction）
  - 2个多模态对话数据集（MAGID、AnyInstruct-108k）
- **开源数据集：** 29+个数据集完全开源

---

## 📋 目录

- [简介](#-简介)
- [大厂与开源项目的数据合成方法](#-大厂与开源项目的数据合成方法)
- [按图像处理方式分类](#-按图像处理方式分类)
  - [图像生成 - 合成新视觉内容](#-图像生成---合成新视觉内容)
    - [几何与数学推理](#-几何与数学推理)
    - [文档/文本密集场景](#-文档文本密集场景)
  - [图像介入推理](#-图像介入推理)
  - [图像编辑（方法+数据）](#-图像编辑方法数据)
  - [组合性/偏好导向合成](#-组合性偏好导向合成)
  - [交错图文·连贯性与一致性](#-交错图文连贯性与一致性)
  - [图像不变文本增强](#图像不变文本增强)
  - [VLM自我改进与强化学习](#-vlm自我改进与强化学习)
    - [空间推理增强](#-空间推理增强)
    - [持续学习与灾难性遗忘缓解](#-持续学习与灾难性遗忘缓解)
    - [VLM个性化与概念学习](#-vlm个性化与概念学习)
- [跨领域方法论洞察](#-跨领域方法论洞察)
- [典型多模态数据集](#-典型多模态数据集)
  - [交错图文数据集](#-交错图文数据集)
  - [领域特定与知识导向数据集](#-领域特定与知识导向数据集)
  - [大规模通用训练数据集](#-大规模通用训练数据集)
  - [图像编辑数据集](#-图像编辑数据集)
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

# Awesome Multimodal Data Recipe [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<div align="center">
  <img src="https://img.shields.io/github/stars/opendatalab-raiser/awesome-multimodal-data-recipe" alt="Stars">
  <img src="https://img.shields.io/github/forks/opendatalab-raiser/awesome-multimodal-data-recipe" alt="Forks">
  <img src="https://img.shields.io/github/license/opendatalab-raiser/awesome-multimodal-data-recipe" alt="License">
  <img src="https://img.shields.io/github/last-commit/opendatalab-raiser/awesome-multimodal-data-recipe" alt="Last Commit">
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome">
</div>

<p align="center">
  <a href="README.md">English</a> | <a href="README_zh.md">中文</a>
</p>

<p align="center">
  <b>A curated list of multimodal data synthesis methods and resources for Vision-Language Models</b>
</p>

---

## 📊 Statistics

- **Total Papers:** 101 (data synthesis/construction methods)
- **Industrial Reports:** 9 (Baidu, Microsoft, Alibaba, ByteDance, Tencent, Hunyuan, etc.)
- **Data Synthesis Methods:**
  - Image Generation - Synthesizing New Visual Content (22): Geometric/mathematical reasoning + document/text-dense scenes (OCR-free scene text, document layout analysis) + scene text detection + multimodal dialogue (any-to-any generative synthesis) + text-driven image synthesis + ChatGPT-guided synthesis + autonomous driving + fully synthetic image-text generation + 3D physics simulation + 3D scene synthesis (3D visual instruction data) + robotic action synthesis
  - Image Editing (5): Non-rigid motion, unified editing, referring expression-guided editing, generative visual instruction tuning
  - Compositionality / Preference-Guided Synthesis (6): Enhancing compositional understanding + multi-concept composition + multi-image customization + hard negative contrastive learning + multimodal counterfactual samples + 3D physics simulation VLC enhancement
  - Interleaved Image-Text · Coherence & Consistency (5): Multi-perspective quality filtering + iterative refinement + multimodal embedding-based correlation + instructional video extraction (video-to-textbook)
  - Think with Image (2): Interleaved multimodal reasoning with image manipulation + large-scale reasoning trajectory synthesis
  - VLM Self-Improvement & Reinforcement Learning (4): Calibrated self-rewarding VLM + gamified self-play frameworks + chart understanding self-improvement (code-driven synthesis)
  - Image-Invariant - Text Enhancement (48): Fixed images, enriched text only + adaptive weighted synthetic captions + medical domain purely synthetic data + cost-efficient LVLM data refinement + spatial reasoning enhancement + VLM personalization + continual learning + multimodal RAG training + self-instructed code formatting + multilingual embedding enhancement + MLLM data generators + programmatic instruction generation + information bottleneck concept selection + image comprehension self-training + multimodal instruction following (constraint-driven) + composed image retrieval triplet synthesis + multimodal question generation (style & modality controllable) + chart understanding (GPT-4-driven multi-task instruction generation) + scientific figure understanding (GPT-4V generated QA) + domain-adaptive post-training (open-source MLLM-driven generate-then-filter) + task type hierarchical expansion (GPT-4o automated generation)
  - Video - Instruction Tuning (Synthetic Data) (1): Synthetic video instruction-following data (captions + QA)
  - Cross-Domain Methodology Insights (2): Multi-modal model collapse analysis + synthetic data quality assessment
- **Notable Datasets:**
  - 4 interleaved image-text datasets (OmniCorpus, OBELICS, MMC4, CoMM)
  - 2 domain-specific datasets (MMM-RS, MESED)
  - 4 image editing datasets (ByteMorph-6M, ImgEdit, RefEdit, RefCOCO-Edit)
  - 4 large-scale general training datasets
  - 5 chart reasoning datasets (ChartInstruct, Synthesize Step-by-Step, ECD, ChartGen, MMC-Instruction)
  - 2 multimodal dialogue datasets (MAGID, AnyInstruct-108k)
- **Open Source Datasets:** 29+ datasets fully open-sourced

---

## 📋 Table of Contents

- [Introduction](#-introduction)
- [Industrial & Open-Source Data Synthesis](#-industrial--open-source-data-synthesis)
- [Methods by Image Processing Type](#-methods-by-image-processing-type)
  - [Image Generation - Synthesizing New Visual Content](#-image-generation---synthesizing-new-visual-content)
    - [Geometric & Mathematical Reasoning](#-geometric--mathematical-reasoning)
    - [Document / Text-Dense Scenes](#-document--text-dense-scenes)
  - [Think with Image](#-think-with-image)
  - [Image Editing (Method + Data)](#-image-editing-method--data)
  - [Compositionality / Preference-Guided Synthesis](#-compositionality--preference-guided-synthesis)
  - [Interleaved Image-Text · Coherence & Consistency](#-interleaved-image-text--coherence--consistency)
  - [Image-Invariant Text Enhancement](#image-invariant-text-enhancement)
  - [VLM Self-Improvement & Reinforcement Learning](#-vlm-self-improvement--reinforcement-learning)
    - [Spatial Reasoning Enhancement](#-spatial-reasoning-enhancement)
    - [Continual Learning & Catastrophic Forgetting Mitigation](#-continual-learning--catastrophic-forgetting-mitigation)
    - [VLM Personalization & Concept Learning](#-vlm-personalization--concept-learning)
- [Cross-Domain Methodology Insights](#-cross-domain-methodology-insights)
- [Notable Multimodal Datasets](#-notable-multimodal-datasets)
  - [Interleaved Image-Text Datasets](#-interleaved-image-text-datasets)
  - [Domain-Specific & Knowledge-Oriented Datasets](#-domain-specific--knowledge-oriented-datasets)
  - [Large-Scale General Training Datasets](#-large-scale-general-training-datasets)
  - [Image Editing Datasets](#-image-editing-datasets)
- [Benchmark Datasets](#-benchmark-datasets)
- [Resources](#-resources)
- [Contributing](#-contributing)

---

## 🎯 Introduction

Multimodal data synthesis is a critical technique for enhancing the performance of Vision-Language Models (VLMs). This repository collects and organizes:

- 🏢 **Industrial Reports**: Detailed data synthesis pipelines and best practices from leading tech companies
- 📚 **Academic Papers**: State-of-the-art research methods and innovative techniques
- 🛠️ **Tools & Frameworks**: Practical data synthesis tools and codebases
- 📊 **Datasets**: High-quality multimodal datasets

**Key Observation**: Current multimodal data synthesis predominantly follows an "image-invariant + text-enhancement" paradigm, leveraging web resources, tool APIs, or other large models to improve the quality and diversity of image-text pairs.

---

## 🏢 大厂与开源项目的数据合成方法

> This section features works with explicitly documented data synthesis pipelines. **Only includes projects with detailed descriptions of data construction and synthesis methods.**

### Baidu - Qianfan-VL

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

### Alibaba - Qwen-VL Series

<details>
<summary>Click to expand</summary>

**Papers**:
- [Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond](https://arxiv.org/abs/2308.12966)

**📊 Data Synthesis Method (Section 3.1.2)**:

Qwen-VL paper describes grounding data construction in Section 3.1.2:

1. **Grounding Data Synthesis** (Section 3.1.2):
   - Utilizes existing detection datasets (COCO, Objects365) with bbox annotations
   - **Converts bbox coordinates to normalized text format** (e.g., `<box>0.1,0.2,0.3,0.4</box>`)
   - **Generates instructions**: Creates instruction-response pairs like "find X in the image"
   - This is a data synthesis method that converts structured annotations to text format

**⚠️ Note**:
- This is **data format conversion and instruction generation**, classified as data synthesis
- The paper does not fully disclose prompt templates or generation methods
- Other parts (data sources, cleaning) are mainly data collection and filtering, not synthesis

</details>

### Alibaba - MMEvol (2024)

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

### ByteDance - Oasis

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

### Microsoft - Florence-2

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

### Tencent Hunyuan - Bee, HoneyPipe & DataStudio

<details>
<summary>点击展开</summary>

**论文**: [Bee: A High-Quality Corpus and Full-Stack Suite to Unlock Advanced Fully Open MLLMs](https://arxiv.org/abs/2510.13795)

**发布时间**: arXiv 2025年10月

**机构**: 腾讯混元团队 & 清华大学

**作者**: Yi Zhang, Bolin Ni, Xin-Sheng Chen, Heng-Rui Zhang, Yongming Rao, Houwen Peng, Qinglin Lu, Han Hu, Meng-Hao Guo, Shi-Min Hu

**📊 三大核心贡献**:

**1. Honey-Data-15M**: 1500万样本的SFT数据集，经过精心清洗并enriched with双层思维链推理

**2. HoneyPipe + DataStudio**: 数据筛选pipeline及其底层模块化框架，提供透明且可适应的方法论

**3. Bee-8B**: 8B模型，在完全开源MLLM中建立新SOTA，与半开源模型（如InternVL3.5-8B）竞争

---

**📊 数据合成方法 - HoneyPipe（Section 2）**:

HoneyPipe是一个**自动化且可复现的工作流**，基于**DataStudio的模块化组件**构建，采用精妙的**双层推理增强策略**：大规模短CoT增强的基础路径 + 针对复杂指令的长CoT专用循环。

**🔧 阶段1：数据聚合与准备**
- **初始池**: 约2400万图像-文本对，来自多个社区数据集
  - 来源：LLaVA-OneVision、PixMo、MAmmoTH-VL等
  - 挑战：显著的内容重叠
- **严格去重**（pair级别）:
  - 方法：感知哈希（图像）+ Simhash（指令）
  - 移除标准：图像**和**指令**都**必须相同
  - 目的：最大化多样性，提升处理效率
- **领域标注**: 人工检查和分类
  - 领域：General、Chart、OCR、STEM等
  - 目的：指导后续处理
- **输出**: 带领域标签的清洁、唯一图像-指令-响应三元组

**🔧 阶段2：噪声与无关性过滤**
- **基于规则的算子**（格式问题）:
  - 移除非常小的图像
  - 过滤极端长宽比
  - 消除指令中的重复文本
- **基于模型的过滤算子**（使用**Qwen2.5-VL-72B**）:
  - 评估：指令是否逻辑合理且可回答？
  - 验证：指令与视觉内容是否语义相关？
  - 示例：将"解决这个函数问题"标记为与橙子图像无关
- **结果**: 有效剪枝有缺陷的样本，产生清洁的图像-指令对

**🔧 阶段3：短CoT增强与验证**（基础路径）

*此阶段针对需要中等推理的指令*

**数据分流**:
- CV任务（OCR、物体检测）→ **跳过增强** → 最终数据集
- 其他样本 → 进入CoT增强流程

**短CoT增强**（约1220万样本）:
- **预处理**: 移除抑制推理的提示
  - 移除："直接回答"等头尾提示
  - 目的：激发全面的、逐步的响应
- **生成**: 使用**Qwen2.5-VL-72B/32B**（强大的开源MLLMs）
  - 将简单短响应 → 详细推理路径
  - **无额外系统提示**: 模型已擅长多步骤响应
  - 避免约束：保持输出多样性
- 12.2M短CoT样本的**主要来源**

**保真度验证**（LLM-as-a-Judge）:
- **验证器模型**: Qwen2.5-VL-72B
- **方法**: 新生成CoT最终结论与原始响应之间的语义比较
- **评估标准**（双重）:
  - **事实性查询**（客观）: 最终响应必须**精确**匹配
  - **描述性查询**（主观）: 需要主题相关性和语义一致性
- **通过** → 加入最终数据集
- **失败** → **不丢弃**，路由到长CoT增强循环进行专门增强

**🔧 阶段4：长CoT增强循环**（复杂指令专用路径）

*专为需要深度、多步骤问题解决的最复杂指令设计*

**输入来源**（3种主要类型）:
1. **失败样本**: 阶段3保真度验证失败的样本
2. **特定数据源**: 识别为固有复杂的数据源
   - 例如：VisualWebInstruct
   - 策略：主动生成长CoT**并且**同时生成短CoT
3. **验证数据集**: 先前研究验证的数据集
   - 例如：Vision-R1
   - 标准：特别适合生成深度推理链

**深度推理生成**（约270万样本）:
- **模型**: 利用**顶级专有MLLMs**生成更详细的解决方案
- **过程**:
  - 首先生成深度推理（通常使用`<think></think>`标签结构化）
  - 然后输出最终响应
- **能力**: 处理初始开源模型无法胜任的复杂指令

**最终保真度验证**:
- 与阶段3相同的验证过程
- **通过** → 构成Honey-Data-15M中约270万长CoT数据点
- **失败** → **丢弃**（假定为错误、无解或标注成本过高）

---

**📦 最终数据集 - Honey-Data-15M**:

**规模**: 1500万精心筛选样本

**组成**（7大领域）:
- General（36.8%）: 基础视觉理解
- Chart（24.6%）: 图表理解与推理
- Caption（15.1%）: 图像描述
- STEM（7.6%）: 符号推理（数学、科学、几何）
- Document（5.9%）: 文档理解与OCR
- Grounding & Counting（5.1%）: 物体检测与计数
- OCR（4.9%）: 各种场景文本识别

**双层CoT主干**:
- **约1220万短CoT样本**: 中等推理的基础性、逐步逻辑推断
- **约270万长CoT样本**: 复杂问题解决的复杂、多步推理，需要更深入的综合
- **针对性方法**: 根据指令复杂度定制响应深度
- **固有解决方案**: 识别哪些指令需要详细的多步骤解决方案

---

**🤖 Bee-8B模型 - 验证与性能**:

**架构**:
- LLM: Qwen3-8B（推理和文本生成）
- 视觉编码器: SigLIP2-so400m-patch14-384
- 分辨率策略: Anyres（处理可变分辨率，保留细粒度细节）
- 投影器: 带GELU激活的两层MLP

**训练**: 5阶段渐进式过程（详见Section 3.2）

**性能亮点**（在完全开源MLLM中建立新SOTA）:

*通用VQA*:
- **MMMU**: 66.8（与半开源模型竞争）
- **MMMU-Pro**: 50.7（**领先Qwen2.5-VL-7B 3.6%**）
- **MMStar**: 71.4
- **MMVet**: 83.9
- **MMVP**: 82.0

*数学与推理*（突出表现）:
- **MathVista mini**: 81.4
- **MathVerse**（vision_only）: 67.0
- **MathVision**: 50.0
- **LogicVista**: 61.3
- **DynaMath**（worst）: 40.5
- **WeMath**: 59.8

*关键观察*: 在**事实准确性**和**复杂多步推理**方面优势最显著，直接反映Honey-Data-15M的优势

**全面消融研究**:
- 量化每个筛选阶段的影响
- 在多个benchmark上显示显著改进
- 证实：关注数据质量 > 竞争数据量
- 证据：数据清洗 + CoT增强至关重要

---

**🎯 核心创新 - 双层CoT策略**:

1. **渐进式增强**: 逐步提升质量而非简单丢弃
2. **失败样本恢复**: 短CoT验证失败的样本获得专门的长CoT增强
3. **模型驱动过程**: MLLM自动化工作流（人工标注的可扩展、经济替代方案）
4. **复杂度识别**: 固有地解决了识别哪些指令需要深度推理的挑战

---

**✅ 开源资源**:
- **项目主页**: https://open-bee.github.io
- **论文**: [arXiv:2510.13795](https://arxiv.org/abs/2510.13795)
- **承诺发布**（完整套件）:
  - Honey-Data-15M语料库
  - HoneyPipe + DataStudio框架
  - 训练recipes
  - 评估工具
  - Bee-8B模型权重

---

**💡 重要意义**:

- **缩小差距**: 证明完全开源MLLM可通过关注数据质量与半开源模型竞争
- **透明方法论**: 超越静态数据集发布，提供不断演进、可适应的筛选方法
- **社区基石**: 为完全开源MLLM社区提供新的基础资源
- **可扩展性**: 模型驱动pipeline使开源社区的高质量数据构建变得可行
- **验证**: Bee-8B的SOTA性能确认数据筛选策略的有效性

**核心论点得到证实**: *对数据质量的原则性关注是开发与半开源模型高度竞争的完全开源MLLM的关键途径*

</details>

### ByteDance - ByteMorph

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2506.03107">📄 ByteMorph</a></b><br>
<code>arXiv 2506.03107</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**: **非刚性运动编辑** - 首个大规模数据集解决相机运动、物体形变、人体关节运动和人物-物体交互
  - **数据合成方法** - **运动引导的分层合成**:
      - **核心创新**: 结合**VFX启发的分层合成**与**GPT-4o运动语义标注**的自动化pipeline
      - **4阶段Pipeline**:
        1. **视频源收集**: 网络规模视频语料库 → 运动检测（光流） → 高分辨率（≥720p）运动丰富片段
        2. **分层合成**: 前景分割 → 背景稳定 → 保留运动的层合成
        3. **GPT-4o标注生成**: 多模态理解 → 运动感知的自然语言指令
        4. **质量保证**: CLIP美学评分 + 光流连贯性 + LLM指令-编辑对齐验证
      - **关键优势**: 大规模保留真实运动动态（自动化手工VFX工作流）
  - **数据规模**:
      - **ByteMorph-6M**: 600万高分辨率编辑三元组（源图像、指令、编辑图像）
      - **分布**: 180万相机运动、150万物体形变、180万人体关节运动、90万HOI
      - **分辨率**: 大部分1024×1024，最小512×512
  - **基准**: ByteMorph-Bench（613个专家验证测试样本，难度分级）
  - **模型**: ByteMorpher（扩散Transformer基线）
  - **实验结果**:
      - 在运动指标上超越InstructPix2Pix/MagicBrush **+18.3%**
      - 人工偏好: **73.5%** vs. 基线
      - 证明运动特定训练至关重要（静态数据集模型: 32.1%成功率）
  - **发布时间**: arXiv 2025年6月
  - **机构**: 字节跳动Seed、USC、东京大学、UC伯克利、斯坦福、UCLA
  - **开源**: ✅ 数据集（600万三元组）、基准（613样本）、模型、代码 - 计划在OpenDataLab/HuggingFace发布
  

</details>

### ByteDance & NTU - LLaVA-OneVision

<details>
<summary>点击展开</summary>

**论文**: [LLaVA-OneVision: Easy Visual Task Transfer](https://arxiv.org/abs/2408.03326)

**发布时间**: arXiv 2024年8月 (v3: 2024年10月)

**机构**: 字节跳动、南洋理工大学S-Lab、香港中文大学、香港科技大学

**作者**: Bo Li, Yuanhan Zhang, Dong Guo, Renrui Zhang, Feng Li, Hao Zhang, Kaichen Zhang, Peiyuan Zhang, Yanwei Li, Ziwei Liu, Chunyuan Li

**📊 数据构建方法（Section 4 - 综合数据策略）**:

LLaVA-OneVision代表了一种重要的以数据为中心的方法，在多模态训练中强调**"质量重于数量"**。论文整合了LLaVA-NeXT博客系列的见解，配合精心筛选的大规模数据集（2024年1月至6月积累）。

---

**🔬 高质量知识学习（470万样本）**

*核心原则*: 在有限计算预算下，专注于高质量知识学习而非网络规模的低质量数据。

**关键洞察**: **99.8%的高质量知识数据是合成的**，这是由于收集大规模高质量野生数据的高成本和版权限制。

**三大数据类别**:

**1. 重新描述的详细描述数据（350万样本）**
- **方法**: **自我改进AI**方法
- **模型**: 使用**LLaVA-NeXT-34B**（以强大的详细描述能力著称）
- **过程**: 为现有图像生成新的详细captions
- **来源**: COCO118K, BLIP558K, CC3M
- **创新**: 训练数据由模型早期版本自己生成

**2. 文档/OCR数据（110万样本）**
- **文本阅读子集**: UReader数据集（10万），通过PDF渲染轻松访问
- **合成数据**: SynDOG EN/CN用于文档理解
- **目的**: 增强文本阅读和文档理解能力

**3. 中文和语言数据（23.5万样本）**
- **中文Caption生成（9.2万）**:
  - 图像：原始ShareGPT4V图像
  - 模型：**GPT-4V（Azure API）**生成详细中文描述
  - 目标：提升中文能力
- **语言平衡（14.3万）**:
  - 来源：Evo-Instruct数据集
  - 目的：在视觉描述之外平衡语言理解能力

---

**📦 视觉指令微调数据（480万样本）**

*目标*: 使LMM能够理解并执行跨不同场景的视觉指令

**数据收集策略**:

**分类框架**（三层层次结构）:

1. **视觉输入**: 单图像 / 多图像 / 视频
2. **语言指令**: 通用QA、通用OCR、文档/图表/屏幕、数学推理、语言
3. **语言响应**: 自由形式（GPT-4V/o、Gemini标注）vs 固定形式（学术数据集）

**筛选过程**:
- 从各种原始来源收集，初始比例不平衡
- 纳入Cauldron和Cambrian集合的新子集
- **人工审查和格式化**:
  - 修正问答格式
  - 遵循LLaVA-1.5的prompting策略（多选、简答、OCR）
  - 防止不同数据源的冲突
  - 引导模型行为：平衡QA性能、对话能力、推理技能

**数据组成**:

**单图像数据（320万样本）** - 五大类别:
- **通用（36.1%）**: 70+数据集，包括ALLaVAInst、AOKVQA、Cambrian、LLaVA-158K、ShareGPT4V/4o、VisionFLAN等
- **文档/图表/屏幕（20.6%）**: AI2D、ChartQA、DocVQA、UReader系列、Chart2Text等
- **数学/推理（20.1%）**: MAVIS系列、Geo170K、GeoQA+、GeoMVerse、MathV360K等
- **通用OCR（8.9%）**: ChromeWriting、HME100K、OCR-VQA、SynthDog-EN、TextCaps、TextOCR等
- **语言（14.3%）**: MagpiePro（L3MT、L3ST、Qwen2ST）- 总计45万样本

**OneVision混合数据（160万样本）** - 三种场景:
- **单图像（31.2%，约50万）**: 从之前单图像数据中高质量采样
  - MagpiePro、VisionFLAN、ImageTextualization、Cauldron、UReader、ShareGPT4V/4o等
- **多图像（43.0%，约68.8万）**: 30+数据集
  - NLVR、Co-Instruct、ScanNet、RAVEN、IconQA、VIST、ContrastiveCaption等
- **视频（25.9%，约41.5万）**: 6个数据集
  - ShareGPT4Video（25.5万）、Youcook2、ActivityNet、Charades、NextQA、Ego4D

---

**🎯 核心创新与洞察**:

1. **合成数据主导**: 99.8%的知识数据是模型生成的
   - 成本更低，更容易扩展
   - "随着AI模型越来越强大，从大规模合成数据学习正在成为趋势"

2. **自我改进AI**: 使用LLaVA-NeXT-34B为下一代生成训练数据
   - 为350万图像重新生成更详细的描述
   - 证明从自己模型输出引导的可行性

3. **精心的数据平衡**:
   - 任务分类以维持技能分布
   - 人工审查以防止数据源冲突
   - 跨异构来源的统一prompting策略

4. **跨场景迁移设计**:
   - 洞察：更强的图像模型 → 更好地迁移到多图像/视频任务
   - 训练策略：先单图像，再混合场景
   - 数据分配：为单图像分配更多token以模拟视频表示

5. **质量重于数量理念**:
   - 专注于筛选而非体量
   - 认可预训练LLM/ViT的知识库
   - 持续接触新的高质量数据

---

**📈 训练策略（Section 5）**:

**三阶段课程学习**:
- **Stage-1**: 语言-图像对齐
- **Stage-1.5**: 高质量知识学习（使用470万合成数据）
- **Stage-2**: 单图像指令微调（320万样本）
- **Stage-3**: OneVision混合训练（160万样本）

**模型架构**:
- LLM: Qwen-2（强大的语言能力）
- 视觉编码器: SigLIP（开源编码器中性能更高）
- 投影器: 2层MLP
- 视觉表示: Higher AnyRes策略配合双线性插值

---

**✅ 性能与成就**:

- **首个单一开源模型**在三种场景中同时推动性能边界:
  - 单图像
  - 多图像
  - 视频理解
- 跨模态的强大任务迁移能力
- 通过跨场景迁移展示新兴能力
- 通过从图像迁移任务实现视频理解

---

**✅ 开源资源**:
- **论文**: [arXiv:2408.03326](https://arxiv.org/abs/2408.03326)
- **项目**: https://llava-vl.github.io/blog/llava-onevision
- **数据集**: [🤗 HuggingFace](https://huggingface.co/datasets/lmms-lab/LLaVA-OneVision-Data)
- **模型**: 模型检查点已发布
- **代码**: 代码库开源
- **Demo**: 可用的视觉聊天演示

---

**💡 重要意义**:

- **以数据为中心的方法**: 将LLaVA-NeXT博客系列的洞察整合为综合数据集
- **合成数据验证**: 证明大规模合成数据（99.8%）可以达到SOTA性能
- **自我改进路径**: 展示使用自己模型输出进行下一代训练
- **统一多场景**: 单一模型在图像/多图像/视频中表现出色，无需权衡
- **社区影响**: 完整开源数据、模型、代码，实现可复现性

**核心论点**: *通过数据筛选中的质量重于数量，结合战略性使用合成数据和自我改进，能够构建与专有模型竞争的多功能开源LMM。*

</details>

### LLaVA Series (Wisconsin-Madison & Microsoft)

<details>
<summary>Click to expand</summary>

**Papers**:
- [Visual Instruction Tuning (LLaVA)](https://arxiv.org/abs/2304.08485)
- [Improved Baselines with Visual Instruction Tuning (LLaVA-1.5)](https://arxiv.org/abs/2310.03744)

**📊 Data Synthesis Method (Section 3 Detailed Description)**:

**One of the most influential works in multimodal data synthesis!** LLaVA paper Section 3 "GPT-assisted Visual Instruction Data Generation" provides complete pipeline details:

1. **Data Generation Pipeline** (Figure 2 shows complete flow):

   **Input Materials**:
   - COCO images
   - COCO human-annotated captions (5 per image)
   - COCO bbox annotations

   **Using GPT-4 to Generate Three Types of Data**:

   a) **Conversation** (Multi-turn dialogue, 58K):
   - Prompt template: Appendix A.2.1 provides complete prompt
   - Input: Caption list
   - Output: Multi-turn Q&A about image content

   b) **Detailed Description** (Detailed description, 23K):
   - Prompt template: Appendix A.2.2
   - Requires GPT-4 to generate more detailed descriptions than original captions

   c) **Complex Reasoning** (Complex reasoning, 77K):
   - Prompt template: Appendix A.2.3
   - Based on bbox, generates reasoning-required questions (e.g., counting, spatial relationships)

2. **Complete Data Scale**:
   - Total: 158K instruction-response pairs
   - Based on approximately 80K COCO images

3. **Prompt Engineering Details** (Fully disclosed in Appendix):
   - Appendix A fully discloses all prompt templates
   - Includes system prompts, few-shot examples
   - Fully reproducible

**LLaVA-1.5 Data Improvements**:
- Adds more academic task datasets (VQAv2, GQA, OKVQA, etc.)
- Enhances data diversity
- Maintains same generation method

**✅ Data Fully Open Source**:
- [HuggingFace Dataset](https://huggingface.co/datasets/liuhaotian/LLaVA-Instruct-150K)
- Prompt templates directly usable

**Impact**:
This method has been adopted or improved by almost all subsequent open-source VLM projects (ShareGPT4V, SVIT, InternVL, etc. are based on this paradigm).

</details>

---

## 📂 按图像处理方式分类

### 🎨 图像生成 - 合成新视觉内容

This category focuses on **generating new images from scratch** as part of the data synthesis pipeline. These methods create synthetic visual content (geometric diagrams, mathematical figures, text-dense scenes, etc.) programmatically or through generative models, paired with corresponding textual annotations.

#### 🔄 文本驱动图像合成

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2407.20756">📄 SynthVLM</a></b><br>
<code>arXiv 2407.20756</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-ACM_Multimedia_2025-red?style=flat-square"/>
</summary>

  - **聚焦**: **反向合成：从文本生成图像** - 不同于传统"图像→caption"，SynthVLM采用"caption→图像"范式，使用高质量caption驱动Diffusion模型生成高分辨率图像
  - **数据合成方法** - **两阶段筛选-生成-再筛选**:
      - **核心创新**: 首次系统性地提出从caption生成图像的VLM预训练数据合成框架，解决Web数据"水印/广告/低质量"三大痛点
      - **Stage 1: Caption筛选**（构建高质量种子）:
        - **数据源**: 汇聚人工标注（LAION、CC、SBU）+ 模型生成（BLIP2对DataComp重新标注）
        - **两轮过滤**:
          1. **质量过滤**: ChatGPT + 统计指标（N-gram、Perplexity）移除广告、重复、语法错误
          2. **对齐过滤**: 计算caption与原始图像的CLIPScore，选择top 40%（1M caption）
      - **Stage 2: 图像生成+质量筛选**:
        - **生成**: 使用**Stable Diffusion XL (SDXL)** 为1M caption生成**1024×1024高分辨率图像**（60 sampling steps，网格搜索超参）
        - **双指标筛选**:
          - **CLIPScore(I, C)**: 评估图像-文本语义对齐
          - **SSIMScore(I, I_resized)**: 评估图像质量（模拟336px resize损失）
          - **加权公式**: Weighted_Score = CLIPScore + 0.5 × SSIMScore
        - **选择**: Top 100K pairs → **SynthVLM-100K**
      - **关键技术细节**:
        - **避免伪影**: 生成图像天然无水印、无广告（Web图像常见问题）
        - **更高分辨率**: 1024×1024 vs. Web图像通常336×520
        - **更好对齐**: SynthVLM-100K的平均CLIPScore=0.36、SSIMScore=0.86，显著高于COCO-Caption(0.31/0.73)、BLIP-LCS(0.32/0.75)、ShareGPT4V(0.32/0.79)
  - **评估与验证**:
      - **GPT-4V + InternVL2 + 人工评估**: 1K样本盲测，合成图像胜率 **63.3%(GPT-4V)、69.2%(InternVL2)、75.8%(人工)**
      - **下游任务**: SynthVLM-7B/13B仅用100K预训练数据（LLaVA的18%）达到SOTA，在VQAv2、GQA、MMBench、MME等全面超越LLaVA
      - **语言能力保持**: MMLU基准上SynthVLM-7B达41.2（vs. LLaVA 36.3），证明合成数据不损害语言理解
  - **数据规模**:
      - **中间池**: 1M高质量caption
      - **最终数据集**: **SynthVLM-100K**（100K合成图像-文本对）
  - **开源**: ✅ [GitHub](https://github.com/starriver030515/SynthVLM)
  - **机构**: 北京大学 + 华为技术 + 上海人工智能实验室
  - **发布时间**: ACM MM 2025 | arXiv 2024年7月
  

</details>
---

<details>
<summary>
<b><b><a href="https://scholar.google.com/scholar?q=Enhanced%20Visual%20Instruction%20Tuning">📄 Enhanced Visual Instruction Tuning</a></b><br>
<code>Paper</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-ACL_Findings_2024-red?style=flat-square"/>
</summary>

  - **Focus**: **Synthesized Image-Dialogue Data for Visual Instruction Tuning** - Generate comprehensive image-dialogue datasets using ChatGPT and Stable Diffusion to enhance multimodal LLM capabilities across diverse visual tasks
  - **Data Synthesis Method** - **Dual-Stage ChatGPT-Guided Generation Pipeline**:
      - **Core Innovation**: First systematic approach leveraging LLM (ChatGPT) to generate both Stable Diffusion prompts and corresponding dialogue data, addressing limitations in existing visual instruction datasets' capability coverage and dialogue diversity
      - **Stage 1: ChatGPT Prompt & Dialogue Generation**:
        - **Prompt Generation**: Use **ChatGPT** with capability-specific instructions to generate Stable Diffusion prompts targeting 11 visual abilities
        - **Capability Categories**: Animal, Action, Color, Abnormal Detection, Scene, Style, Food, Profession, Vehicle, Furniture, Plant recognition
        - **Prompt Engineering Techniques**:
          - **Length Control**: Max 10 keywords per prompt to ensure clear focus and accurate image generation
          - **Keyword Prioritization**: Most crucial keywords at beginning, double-bracketed for emphasis
          - **Stability Enhancements**: Add capability-specific instructions and cautions to encourage diversity
          - **Abnormal Image Guidance**: For joke understanding tasks, direct ChatGPT to create prompts for "abnormal images" (e.g., "giraffe walking through narrow corridor")
        - **Dialogue Generation**: Generate corresponding question-answer pairs with constraints:
          - **Length Limit**: ≤500 characters per dialogue for conciseness
          - **Diversity Requirements**: Include misleading either-or questions to increase complexity
          - **Task-Specific Restrictions**: Address model biases (e.g., construction workers → add human attributes to avoid building focus)
      - **Stage 2: Stable Diffusion Image Generation**:
        - **Model**: **Stable Diffusion v1.4** for text-to-image generation
        - **Generation Settings**: Multiple candidates per prompt, select best based on alignment scores
        - **Multi-Image Data**: Generate paired prompts simultaneously for image similarity/difference/logical relation tasks (3K pairs)
        - **Quality Control**: CLIP-based alignment verification with threshold γ=0.25
      - **Advanced Data Types**:
        - **Interleaved Multi-Turn Dialogues**: Step-by-step instructional conversations with image inputs at each turn
        - **Multi-Image Tasks**: Similarity comparison, difference analysis, logical relationship reasoning
        - **Specialized Content**: Abnormal image detection, profession recognition, fine-grained attribute understanding
  - **Technical Architecture Integration**:
      - **Base Model**: LLaVA architecture with CLIP visual encoder + projection layer + LLM (Vicuna)
      - **Training Strategy**: Two-stage fine-tuning (modality alignment + visual instruction tuning)
      - **Token Processing**: Convert visual features to language embedding tokens through linear/MLP projection
  - **Data Scale**:
      - **Primary Dataset**: **38K image-dialogue pairs** across 11 capability categories
      - **Multi-Image Data**: **3K specialized multi-image instances**
      - **Interleaved Dialogues**: Step-by-step instructional conversations with visual feedback
      - **Total Coverage**: Comprehensive training set combined with raw LLaVA dataset for enhanced capabilities
  - **Evaluation & Results**:
      - **Benchmarks**: VizWiz (58.4% vs 53.6% LLaVA-1.5), MM-Vet (36.1% vs 35.4%), MME (1532.3 vs 1531.3), MMBench (69.4% vs 67.7%)
      - **Manual Evaluation**: Significant improvements across all 11 capabilities, especially abnormal detection (+25%), style recognition (+50%)
      - **GPT-4 Scoring**: Consistent performance gains with detailed capability-specific analysis
      - **Multi-Image Tasks**: Substantial improvements in difference detection (2.7→3.6), similarity analysis (2.2→2.8), logical relations (3.1→3.7)
  - **Key Technical Contributions**:
      - **Automated Pipeline**: First fully automated approach combining LLM prompt generation with diffusion model image synthesis
      - **Capability-Specific Design**: Targeted generation for underrepresented visual tasks (jokes, abnormal detection, multi-image reasoning)
      - **Quality Assurance**: Multi-level filtering including CLIP alignment, length constraints, and task-specific restrictions
      - **Scalability**: Template-based approach easily extensible to new capabilities and domains
  - **Institution**: University of Technology Sydney, Tencent, Nanyang Technological University, Zhejiang University, Beijing Jiaotong University, Westlake University, PengCheng Laboratory
  - **Open Source**: ✅ Dataset and generation templates (see supplementary materials)
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2507.08513">📄 Ultimate3D</a></b><br>
<code>arXiv 2507.08513</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**: **大规模3D视觉指令数据集生成用于相机-物体关系理解** - 使用3D资产+渲染+扩散模型自动生成240K带精确相机-物体关系标注的VQA数据
  - **数据合成方法** - **3D渲染 + 多ControlNet扩散 + LLM四步Pipeline**:
      - **核心创新**: 首个系统化利用3D资产生成光真实感图像和相机-物体关系VQA数据的完整框架，解决MLLMs在空间关系理解上的数据集偏差问题
      - **问题识别**:
        - 现有MLLMs在相机-物体关系理解上存在显著缺陷（GPT-4o在物体方向任务上仅43.1%准确率）
        - 根源：训练数据集存在严重偏差（大多数图像从正面、侧面或上方视角拍摄）
        - 缺乏多样化相机-物体关系的高质量标注数据
      - **四步生成Pipeline**:
        1. **3D视觉先验渲染（Stage 1）**:
           - **输入**: 3D资产A（来自Objaverse等开源库），任意相机-物体关系参数β
           - **相机-物体关系定义**:
             - **方位角φ**: 物体相对相机的旋转角度，分为8个方向（右、右前、前、左前、左、左后、后、右后），每个覆盖π/4弧度
             - **视角θ**: 相机仰角，分为3类（俯视、水平、仰视）
             - **距离**: 相机到物体距离，分为3类（特写、中景、远景）
           - **渲染器**: Blender 3D引擎
           - **输出多模态视觉先验I_β**:
             - RGB图像
             - 像素级深度图（DepthAnyThing V2）
             - 语义分割mask
             - Canny边缘检测图
           - **关键优势**: 保留精确的ground truth相机-物体关系β，作为后续图像生成的强约束条件
        2. **多样图像描述生成（Stage 2）**:
           - **LLM**: GPT-4o
           - **提示工程**:
             - **系统提示**: 引导LLM生成背景上下文和物体外观细节的多样化描述
             - **Few-shot示例**: 提供风格参考确保描述自然性
           - **输出T_img**: 详细的图像描述文本，包含：
             - 背景场景描述（室内/室外、光照条件、环境氛围）
             - 物体细节描述（材质、颜色、状态）
             - 上下文信息（物体在场景中的作用）
           - **多样性保证**: 针对同一3D资产类别生成多种不同的场景描述，增强数据多样性
        3. **受控光真实感图像生成（Stage 3）**:
           - **核心技术**: 多ControlNet堆叠 + SDXL扩散模型
           - **条件输入**:
             - 视觉条件：深度图 + Canny边缘图（来自Stage 1）
             - 文本条件：图像描述T_img（来自Stage 2）
           - **多ControlNet架构**:
             - **深度ControlNet**: 权重0.5，保持物体3D几何结构
             - **Canny ControlNet**: 权重0.8，保持物体边缘和轮廓
             - **公式**: z_{t-1} = G_θ(T_img, z_t, t, Σw_k·C^k(I^k_β))
           - **扩散步数T=30**: 平衡生成质量和速度
           - **输出I_syn**: 保持精确相机-物体关系β的光真实感图像
           - **质量保证**:
             - 通过3D先验的强约束，确保生成图像的相机-物体关系与β一致
             - 生成图像具有逼真的光照、纹理和背景
        4. **3D感知文本指令生成（Stage 4）**:
           - **LLM**: GPT-4o
           - **输入**: Ground truth相机-物体关系β（方位角φ、视角θ、距离）
           - **三类问题生成**:
             a) **物体方向问题**:
                - 示例："这个物体朝向哪个方向？"、"物体是面向相机还是背对相机？"
                - 答案：基于φ生成分类答案（8个方向类别）
             b) **相机视角问题**:
                - 示例："照片是从物体上方拍摄还是侧面拍摄？"、"相机视角是什么？"
                - 答案：基于θ生成分类答案（俯视/水平/仰视）
             c) **镜头距离问题**:
                - 示例："照片是近距离拍摄还是远距离拍摄？"、"这是特写镜头还是远景镜头？"
                - 答案：基于距离生成分类答案（特写/中景/远景）
           - **提示工程技巧**:
             - 使用系统提示和few-shot示例确保问题自然性和多样性
             - 为每个相机-物体关系生成最多3个VQA对（每种问题类型1个）
           - **输出T_qa**: 高质量问答对，答案精确匹配ground truth
      - **关键技术优势**:
        - **精确标注**: 通过3D渲染保证相机-物体关系的ground truth准确性，避免人工标注误差
        - **光真实感**: 多ControlNet+SDXL生成的图像质量接近真实照片
        - **完全自动化**: 从3D资产到VQA数据的全自动pipeline，无需人工介入
        - **可扩展性**: 可应用于任何3D资产库（Objaverse、ShapeNet等），理论上可无限扩展
        - **多样性**: 每个3D资产生成72种相机-物体关系组合（8方向×3视角×3距离），涵盖广泛的空间配置
  - **Ultimate3D数据集**:
      - **总规模**: 240K VQA对
      - **组成**:
        - **合成数据**: 85K图像（来自1180个3D资产）
        - **真实数据**: 18K图像（从MEBOW数据集裁剪的单人照片+人体方向标注）
      - **3D资产库**: 1180个3D模型，覆盖100个物体类别
      - **相机-物体关系覆盖**:
        - 每个3D资产：72种配置（8方向×3视角×3距离）
        - 每个配置：最多3个VQA对（对应3种问题类型）
      - **基准测试集**: 8K高质量样本用于评估
      - **数据格式**: (图像I_syn, 问题T_qa, 答案, 类别标签, ground truth β)
  - **实验结果** - **开源模型微调后超越所有商业SOTA**:
      - **基线模型表现（未微调）**:
        - LLaVA-1.5-7B: 物体方向18.3%，视角25.0%，镜头距离29.2%
        - LLaVA-1.6-13B: 物体方向16.1%，视角15.9%，镜头距离33.3%
        - Llama-3.2-Vision-11B: 物体方向5.6%，视角6.8%，镜头距离38.1%
        - **结论**: 所有基线模型在相机-物体关系理解上接近随机猜测水平（<40%）
      - **微调后性能（在Ultimate3D上训练）**:
        - **物体方向任务**:
          - 微调LLaVA-1.6-13B: **72.4%** (合成) / 63.1% (真实) vs GPT-4o 43.1%（+29.3%）
          - 微调Llama-3.2-V-11B: **74.2%** (合成) / 66.4% (真实)
        - **相机视角任务**:
          - 微调LLaVA-1.6-13B: **72.3%** (合成) / 61.8% (真实) vs GPT-4o 54.1%（+18.2%）
          - 微调Llama-3.2-V-11B: **69.1%** (合成) / 58.7% (真实)
        - **镜头距离任务**:
          - 微调LLaVA-1.6-13B: **94.8%** (合成) / 71.4% (真实) vs GPT-4o 41.7%（+53.1%）
          - 微调LLaVA-1.5-7B: **94.0%** (合成) / 66.7% (真实)
      - **商业模型表现对比**:
        - GPT-4o: 物体方向43.1%，视角54.1%，镜头距离41.7%
        - Claude-3-Sonnet: 物体方向43.1%，视角54.3%，镜头距离41.7%
        - Claude-3.5-Sonnet: 物体方向40.3%，视角55.6%，镜头距离41.8%
        - **结论**: 所有商业模型在Ultimate3D基准上表现不佳，揭示相机-物体关系理解是当前MLLMs的普遍弱点
      - **跨数据集泛化能力（MMVP基准）**:
        - 微调后模型在MMVP上也有显著提升，证明学到的空间理解能力可迁移
      - **用户研究**:
        - 93.07%的生成图像被评估为成功保持了3D几何结构和相机-物体关系
        - 远高于基线方法（仅55.11%成功率）
  - **消融实验关键发现**:
      - **多ControlNet必要性**: 同时使用深度+Canny边缘达到最佳效果（单独使用任一先验效果下降）
      - **3D先验的重要性**: 移除3D视觉先验，相机-物体关系保持率大幅下降
      - **合成数据vs真实数据**:
        - 仅在合成数据上训练的模型在合成测试集上表现最佳
        - 在真实测试集上，合成数据训练的模型依然显著优于未微调基线
      - **数据规模影响**: 从100K增加到240K，性能持续提升无饱和迹象
  - **定性分析**:
      - **偏差识别**:
        - GPT-4o和Claude倾向于低估视角角度（将俯视误判为水平）
        - 倾向于高估镜头距离（将中景误判为远景）
        - 在物体方向判断上接近随机
      - **LLaVA基线偏差**: 原始LLaVA模型对所有问题给出固定答案（"左前"、"俯视"、"特写"），显示严重的数据集偏差
      - **微调后改进**: 微调后的LLaVA模型能够准确识别各种相机-物体关系，无明显偏差
  - **机构**: Purdue University、Amazon
  - **作者**: Shengyuan Ding, Xiaoyi Dong, Yuhang Zang, Haodong Duan, Min Sun, Cheng-Hao Kuo, Daniel Aliaga等
  - **发布时间**: arXiv 2025年7月（v2）
  - **开源**: ✅ [代码、数据和模型](https://github.com/opendatalab/Ultimate3D)
  - **意义**:
      - **问题识别**: 首次系统化揭示MLLMs（包括GPT-4o、Claude等）在相机-物体关系理解上的严重缺陷
      - **数据集贡献**: 提供首个大规模、精确标注的3D相机-物体关系VQA数据集和评估基准
      - **方法创新**: 提出完整的3D资产驱动的视觉指令数据生成框架，可扩展到其他3D理解任务
      - **性能突破**: 证明仅需240K高质量合成数据即可使开源7B模型超越所有商业SOTA（平均提升33.4%）
      - **偏差纠正**: 为纠正现有MLLMs训练数据中的空间关系偏差提供解决方案
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2303.17590">📄 SyViC</a></b><br>
<code>arXiv 2303.17590</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-2023年3月-red?style=flat-square"/>
</summary>

  - **聚焦**: **超越名词的视觉语言模型合成数据增强** - 使用物理仿真和人体动作合成增强VLM对属性、动作、关系和状态的理解
  - **数据合成方法** - **3D物理仿真 + 人体运动合成 + 空间关系建模**:
      - **核心创新**: 构建百万级合成数据集，专注于"超越名词"的视觉语言概念(VLC)，解决VLM在组合推理和非对象词理解方面的弱点
      - **基础平台**: **ThreeDWorld (TDW)** - 多模态物理仿真平台
        - **3D资源**: 2,304个对象模型，585种独特材质，30+室内和9个室外场景
        - **材质类型**: 金属、纸板、木材、陶瓷、玻璃等多样化纹理
        - **物理引擎**: 支持真实物理交互和碰撞检测
      - **三大合成组件**:
        1. **多对象场景合成**:
           - **对象放置**: 每场景随机放置1-8个3D对象模型，使用碰撞器确保合理布局
           - **多视角渲染**: 同时部署4-12个相机位置，获取同一场景的不同视角
           - **属性随机化**: 程序化随机化对象颜色、大小、材质
           - **空间关系**: 基于3D世界坐标自动生成位置关系描述(左/右、前/后、上/下)
        2. **人体运动与交互合成**:
           - **身体模型**: 使用**SMPL-X**参数化人体模型进行精确姿态控制
           - **运动数据源**: 整合**AMASS**、**BABEL**、**TEACH**大规模运动捕捉数据库
           - **多样性设计**:
             - **性别多样性**: 男性和女性预制件(Unity Prefabs)
             - **服装多样性**: SURREAL + Multi-Garment系统支持多层服装组合
             - **运动多样性**: 涵盖日常活动(走路、跑步、跳跃、舞蹈)和复杂交互
           - **人物-对象交互**: 人与场景对象的物理交互(抓取、移动、避让)
        3. **密集标注生成**:
           - **基于规则的语法**: 开发元数据驱动的语法系统，从场景元数据自动生成详细标注
           - **多层次描述**:
             - **对象描述**: 形状、颜色、材质、位置
             - **人物描述**: 性别、服装、发型、动作状态
             - **关系描述**: 对象间空间关系、人物-对象关系
             - **场景描述**: 环境背景、整体布局
           - **长标注处理**: 开发标注分割模块处理超出CLIP文本编码器上下文长度的标注
      - **数据增强策略**:
        - **领域自适应风格化**: 使用风格迁移减少合成-真实数据域差距
        - **参数高效微调**: LoRA适配器进行低参数更新，避免灾难性遗忘
        - **模型平均**: 组合多个检查点权重，平衡VLC理解增益和零样本能力保持
  - **数据规模**:
      - **SyViC数据集**: 767,000图像-文本对
      - **标注质量**: 平均多句描述，涵盖对象、属性、动作、关系、状态
      - **多样性**: 涵盖数千种对象-属性-动作组合，确保组合推理训练覆盖度
  - **训练策略**:
      - **LoRA微调**: 冻结基础模型参数，仅训练低秩适应层
      - **标注分割**: 将长标注分割为子标注，分别编码后平均特征
      - **对比学习**: 保持原始模型(CLIP/CyCLIP)对比损失函数
      - **领域适应**: 结合风格化和参数高效方法减少遗忘
  - **实验结果**:
      - **组合理解基准**:
        - **VL-Checklist**: syn-CLIP vs CLIP显示关系理解+5.82%，属性理解+2.86%
        - **ARO基准**: VG-Relation +12.56%，VG-Attribution +3.75%
        - **Winoground**: 组合推理任务上持续改进，Group Score提升+1.75%
      - **零样本任务保持**:
        - **Flickr30k检索**: +11.5% vs CLIP基线
        - **COCO检索**: +9.9% vs CLIP基线
        - **21个零样本任务**: 平均性能基本保持(-0.8%)，证明无显著遗忘
      - **消融研究发现**:
        - **人体头像重要性**: 包含人体运动数据显著提升属性和关系理解
        - **对象属性随机化**: 颜色、大小、材质随机化均有独立贡献
        - **训练策略组合**: LoRA + 领域适应风格化 + 标注分割组合效果最佳
  - **关键发现**:
      - **"超越名词"突破**: 首次系统性解决VLM在非对象词(属性、动作、关系)理解上的局限
      - **物理仿真优势**: 3D物理引擎生成的空间关系比2D图像更准确、更多样
      - **合成数据充分性**: 纯合成数据即可显著提升组合理解，无需额外真实数据
      - **参数效率**: LoRA微调在保持零样本能力的同时实现目标改进
  - **发布时间**: arXiv 2023年3月 | MIT-IBM Watson AI Lab & Rice University等
  - **开源**: ✅ 代码、SyViC数据集(767K)、训练方法 - 论文中提供详情
  - **重要意义**:
      - **VLM弱点针对性解决**: 直接解决现有VLM在组合推理上的已知局限
      - **物理仿真数据范式**: 建立3D物理仿真生成VL训练数据的方法论
      - **可扩展框架**: 提供可复用的合成数据生成和微调框架，适用于其他VLM
  

</details>
---

#### 📐 几何与数学推理

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2410.17885">📄 R-CoT</a></b><br>
<code>arXiv 2410.17885 | ICLR 2025</code>
</summary>

  - **数据合成方法** - **几何推理的逆向思维链**：
      - **核心创新**：结合**引擎准确性**与**LLM多样性**的两阶段几何问题生成管道
      - **阶段1 - GeoChain**：**生成高保真几何图像**及其对应描述
        - 使用**基于代码的引擎**逐步生成准确的几何图像
        - 生成详细描述，突出**几何元素间的关系**
        - 图像保真度高于现有合成几何数据
      - **阶段2 - Reverse A&Q**：从推理结果逆向生成Q&A对
        - **步骤1**：描述块推理 - 从描述进行单步推理
        - **步骤2**：思维链融合 - 逐步将单步推理融合为多步推理
        - **步骤3**：问题生成 - 从推理结果**逆向生成**问题
        - 避免了直接使用LMM从图像生成Q&A时的准确性问题
      - **核心优势**：先生成答案**再生成**问题，减少错误答案
  - **数据规模**：创建GeoMM数据集，包含高保真几何图像和多样化Q&A对
  - **实验结果**：
      - R-CoT-8B在MathVista上超越之前的开源SOTA模型**16.6%**，在GeoQA上超越**9.2%**
      - 在两个数据集上平均超越GPT-4o **13%**
      - 在2B、7B和8B设置下均达到几何推理新SOTA
  - **发布时间**：arXiv 2024年10月
  - **机构**：百度公司、华中科技大学
  - **开源**：✅ [代码和模型](https://github.com/dle666/r-cot)
  

</details>
<details>
<summary>
<b><b><a href="https://scholar.google.com/scholar?q=MAVIS">📄 MAVIS</a></b><br>
<code>Paper</code>
</summary>

  - **Data Synthesis Method** - **Automatic Mathematical Visual Data Engine**:
      - **Core Innovation**: Fully automated, rule-based data engine **independent of human intervention or GPT API usage**
      - **Complete Data Generation Pipeline**:
        - **Diagram Drawing**: **Automatically creates math diagrams** (image generation)
        - **Caption Generation**: Generates diagram-caption pairs
        - **Q&A Synthesis**: Creates question-answer pairs
        - **CoT Rationale Production**: Produces chain-of-thought reasoning
      - **Key Features**:
        - Ensures **diagram-caption correspondence** through automated rules
        - Guarantees **question-answer correctness** via engine-based generation
        - Maintains **CoT reasoning quality** without relying on proprietary models
      - **Progressive 4-Stage Training Pipeline**:
        - Stage 1: Fine-tune **CLIP-Math** (math-specific vision encoder) with MAVIS-Caption
        - Stage 2: Align CLIP-Math with LLM using MAVIS-Caption
        - Stage 3: Instruction tuning with MAVIS-Instruct
        - Stage 4: DPO to enhance CoT capabilities
  - **Data Scale**:
      - **MAVIS-Caption**: 558K diagram-caption pairs for vision-language alignment
      - **MAVIS-Instruct**: 834K visual math problems with detailed CoT rationales
  - **Experimental Results**:
      - MAVIS-7B surpasses other 7B models by **+9.3%**
      - Outperforms LLaVA-NeXT-110B by **+6.9%**
      - Achieves leading results among open-source MLLMs on mathematical benchmarks
  - **Publication**: arXiv July 2024
  - **Institution**: CUHK, Peking University, Shanghai AI Lab, ByteDance, Oracle
  - **Open Source**: ✅ [Code & Data](https://github.com/ZrrSkywalker/MAVIS)
  

</details>
<details>
<summary>
<b><b><a href="https://scholar.google.com/scholar?q=ShareGPT-4o-Image">📄 ShareGPT-4o-Image</a></b><br>
<code>Paper</code>
</summary>

  - **Data Synthesis Method** - **Distilling GPT-4o Image Generation Capabilities**:
      - **Core Innovation**: First dataset distilled from **GPT-4o's image generation** for both text-to-image and text-and-image-to-image tasks
      - **Text-to-Image Data Generation** (45K pairs) - **IMAGE GENERATION**:
        - **Prompt-First Pipeline**:
          - Define 6-dimensional attribute space (Objects, Background, Style, Camera Angle, etc.)
          - Sample attributes and use LLM (Gemini-Pro-2.5) to compose natural-language prompts
          - Pass prompts to **GPT-4o-Image** to **generate new paired images**
          - Ensures controlled diversity and complexity
        - **Image-First Pipeline**:
          - Source high-quality images from ALLaVA dataset
          - Use LLM to generate detailed descriptive prompts from images
          - Captures natural language needed for describing real-world scenes
      - **Instruction-Guided Image Editing Data** (46K triplets) - **IMAGE EDITING**:
        - Define taxonomy of **14 image editing tasks** across 5 categories (object manipulation, style transfer, conditional control, etc.)
        - For each (source image, editing task): LLM synthesizes specific natural-language instruction
        - **GPT-4o-Image** executes instruction to produce edited output
        - Creates (source image, instruction, edited image) triplets
      - **Key Features**:
        - Synthesized entirely using **GPT-4o** capabilities (no human annotation)
        - Covers wide range of styles and grounded visual reasoning
        - Reflects GPT-4o's strengths in instruction-following and visual aesthetics
  - **Data Scale**: **91K total** (45K text-to-image + 46K instruction-guided editing)
  - **Experimental Results**:
      - Janus-4o (trained on this data) improves over Janus-Pro by **+4 points** on EvalGen and **+1.6 points** on DPG-Bench
      - Achieves impressive text-and-image-to-image generation from scratch with only **91K samples** and **6 hours training** (8×A800)
      - Human evaluations show strong preference for Janus-4o outputs
  - **Publication**: arXiv June 2025
  - **Institution**: The Chinese University of Hong Kong, Shenzhen
  - **Open Source**: ✅ [Code & Data](https://github.com/FreedomIntelligence/ShareGPT-4o-Image)
  
  #### 📄 文档/文本密集场景
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2505.17778">📄 TextFlux</a></b><br>
<code>arXiv 2505.17778</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
</summary>

  - **聚焦**: **无OCR编码器的高保真多语言场景文本合成** - 基于DiT的OCR-free框架，通过空间拼接字形渲染图实现多语言场景文本生成
  - **数据合成方法** - **字形引导的空间拼接策略**:
      - **核心创新**: 消除对OCR编码器的依赖，利用DiT模型的上下文推理能力实现文本合成
      - **方法Pipeline**:
        1. **字形渲染**:
           - 将目标文本渲染为白色前景/黑色背景的二值字形mask `I_glyph`
           - 确保与场景图像 `I_scene` 分辨率匹配
        2. **空间拼接**:
           - 将字形图和场景图水平或垂直拼接：`I_concat = Concat([I_glyph, I_scene], axis)`
           - 形成统一的输入图像，无需额外的视觉条件模块
        3. **Prompt设计**（上下文学习范式）:
           - 模板："一对图像突出显示黑色背景上的白色单词，以及它们在真实世界场景图像中的风格。[IMAGE1]是渲染文本的模板图像，单词为{words}；[IMAGE2]显示文本内容{words}自然且相应地融入图像中。"
           - 引导模型理解字形模板与场景图像的语义关系
        4. **模型架构**:
           - 基于预训练的FLUX.1-Fill-dev（DiT架构，latent rectified flow transformer）
           - 直接利用DiT的上下文感知能力，无需专门的OCR编码器或额外损失函数
      - **关键技术优势**:
        - **OCR-free**: 完全消除对OCR编码器的需求，简化模型架构
        - **多语言扩展性**: 低资源语言（<1000样本）也能达到强性能
        - **数据高效**: 仅需竞争方法1%的训练数据（30,405张 vs 300万-1000万张）
        - **可控多行生成**: 支持灵活的多行文本合成，精确行级控制位置和内容
        - **Zero-shot能力**: 能渲染训练时未见过的语言（如少数民族语言）
  - **训练数据规模**:
      - **总计30,405张图像**（vs AnyWord-3M的300万、MARIO-10M的1000万）
        - 英文：约10,000张（MLT2017、TotalText、CTW1500）
        - 中文：约15,000张（ReCTS、RCTW）
        - 其他语言：各1,000张（日语、韩语、法语、德语、意大利语，来自MLT2019）
      - **训练配置**:
        - 批大小1，梯度累积8
        - AdamW优化器，学习率2e-5
        - 总迭代30,000次
        - 多分辨率增强（512-1024）
        - 两个版本：全参数（2×A100 80GB）+ LoRA（1×A100 80GB，rank=128）
  - **实验结果** - **4个基准上全面超越现有方法**:
      - **多行文本生成（核心任务）**:
        - AnyWord(EN): TextFlux **80.3%** vs AnyText2 45.1% (+35.2%)
        - AnyWord(CH): TextFlux **62.3%** vs AnyText2 35.9% (+26.4%)
        - TotalText: TextFlux **65.3%** vs AnyText2 20.5% (+44.8%)
        - ReCTS: TextFlux **68.5%** vs AnyText2 41.5% (+27.0%)
      - **单行文本生成**:
        - 轻量级LoRA版本就全面超越所有基线
        - Flux基础模型中文准确率为0%，应用TextFlux后达到62.3%
      - **定性结果**:
        - 在复杂背景、曲线文本、手写风格等挑战条件下显著优于现有方法
        - 生成结果几乎与真实图像无法区分
  - **消融实验关键发现**:
      - **字形拼接策略必要性**: 不使用拼接策略，中文准确率仅5.2%
      - **训练的重要性**: 仅拼接不训练，复杂背景下完全失败
      - **文本编码器影响**: 移除CLIP或T5编码器对非拉丁文字影响较小，说明视觉上下文引导足够有效
  - **机构**: bilibili公司、苏州大学、北京大学王选计算机研究所
  - **作者**: Yu Xie, Jielei Zhang, Pengyu Chen, Ziyue Wang, Weihang Wang, Longwen Gao, Peiyi Li, Huyang Sun, Qiang Zhang, Qian Qiao, Jiaqing Fan, Zhouhui Lian
  - **发布时间**: arXiv 2025年5月（v1）
  - **项目页面**: [https://yyyyyxie.github.io/textflux-site/](https://yyyyyxie.github.io/textflux-site/)
  - **意义**:
      - **架构简化**: 证明无需复杂的OCR编码器，DiT的上下文推理能力足以支持高质量场景文本合成
      - **数据效率**: 以1%的数据量达到SOTA，为低资源场景提供可行方案
      - **多语言突破**: 首次证明极小数据量（<1000样本）即可实现低资源语言的高质量文本渲染
      - **可控性提升**: 支持多行文本的灵活控制，突破现有方法的单行或固定布局限制
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2410.12628">📄 DocLayout-YOLO</a></b><br>
<code>arXiv 2410.12628</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**: **通过多样化合成数据和全局到局部自适应感知增强文档布局分析** - 生成DocSynth-300K大规模多样化文档合成数据集，并设计GL-CRM模块处理文档元素多尺度变化
  - **数据合成方法** - **Mesh-candidate BestFit算法 + 元素增强**:
      - **核心创新**: 首个将文档合成视为二维装箱问题的方法，通过迭代最佳匹配生成美观且多样的文档布局
      - **问题识别**:
        - 现有单模态DLA方法（如YOLO、DINO）速度快但准确率较低
        - 多模态方法（如LayoutLMv3、DiT）准确率高但速度慢（延迟显著）
        - 现有文档预训练数据集（如PubLayNet、DocBank）类型单一（仅学术论文），元素多样性不足（<10类）
        - Diffusion等生成方法生成布局同质化严重，无法覆盖多种真实文档类型
      - **三阶段生成Pipeline**:
        1. **预处理：确保元素多样性（Preprocessing）**:
           - **数据源**: M6Doc测试集（2800页多样化文档，74种细粒度元素类别）
           - **元素池构建**:
             - 按细粒度类别分割页面，提取各类别元素
             - 对数量<100的稀有类别进行增强
           - **增强策略（5种技术）**:
             a) **样式迁移**: 应用不同字体、颜色、样式到文本元素
             b) **LLM重写**: GPT-4重写文本元素内容（保持语义相似）
             c) **背景替换**: 替换元素背景
             d) **弹性变换**: 轻微扭曲元素模拟抖动或低分辨率
             e) **高斯噪声**: 添加噪声模拟现实失真
           - **结果**: 确保每个类别至少100个多样化元素
        2. **布局生成：确保布局多样性（Layout Generation）**:
           - **算法**: **Mesh-candidate BestFit** - 受二维装箱问题启发
           - **关键洞察**: 随机排列产生混乱布局；Diffusion模型生成同质化布局（仅学术论文风格）
           - **核心思想**: 将当前布局的可用网格视为不同大小的"箱子"，迭代执行最佳匹配
           - **详细步骤**:
             a) **候选采样**: 从元素池中进行分层采样（基于元素大小），形成候选集C_set
             b) **Mesh引擎**: 分析当前布局L，生成所有可用网格位置集合M
             c) **最佳匹配迭代**:
                - 对每个候选元素e_i和每个网格g_j，计算填充率fr = match(e_i, g_j)
                - 选择填充率最高且>阈值fr_thr的(e_i, g_j)对
                - 将e_i放置在g_j位置，更新布局L
                - 从候选集中移除e_i
                - 重复直到无法找到满足条件的匹配
             d) **约束**: 小元素数量≤Mini_num=5（避免过多小元素降低美学）
           - **优势**: 平衡布局多样性（随机性）和美学（填充率和对齐）
        3. **图像渲染与后处理（Rendering）**:
           - **渲染**: 将布局L和元素渲染为完整文档图像
           - **后处理**:
             - 应用样式迁移、LLM重写、背景替换等增强技术
             - 添加弹性变换和高斯噪声模拟真实场景
           - **输出**: 最终的文档图像及对应的布局标注
      - **关键技术优势**:
        - **美学保证**: 通过填充率和对齐优化，生成布局符合人类设计原则
          - **对齐度评分**: Δx* = min|x*_i - x*_j|（越小越对齐），实验显示Mesh-BF为0.0009 vs Random 0.0171 vs Diffusion 0.0032
          - **密度评分**: L_dst = Σ|e_i| / |L|（越大越紧凑），实验显示Mesh-BF为0.645 vs Random 0.259 vs Diffusion 0.476
        - **布局多样性**: 生成从密集（多小元素）到稀疏（少大元素）的各种布局
        - **元素多样性**: 74种细粒度类别，远超PubLayNet（6类）、DocBank（13类）
        - **可扩展性**: 可基于任何文档元素池生成任意规模数据集
  - **DocSynth-300K数据集**:
      - **原始生成**: 594K文档图像
      - **过滤后规模**: 300K高质量文档（丢弃底部过滤样本）
      - **元素覆盖**: 74种细粒度元素类别
      - **布局多样性**: 涵盖学术论文、教科书、市场分析报告、财务文档等多种类型
      - **标注**: 每个元素的类别、位置（bounding box）
      - **特点**:
        - 远超现有数据集的多样性（PubLayNet 360K但仅学术论文，DocBank 500K但弱监督质量较低）
        - 美学评分显著优于Random和Diffusion方法
  - **DocStructBench评估基准**:
      - **目标**: 定量评估模型在不同文档类型上的性能
      - **规模**: 9,955张图像（7,310训练 + 2,645测试）
      - **四个子集**:
        - **Academic**: 学术论文（1,605训练 + 402测试）
        - **Textbook**: 教科书和试卷（2,345训练 + 587测试）
        - **Market Analysis**: 行业和市场分析报告（2,660训练 + 651测试）
        - **Financial**: 财务业务文档（2,472训练 + 592测试）
      - **10个元素类别**: Title, Plain Text, Abandoned Text, Figure, Figure Caption, Table, Table Caption, Table Footnote, Isolated Formula, Formula Caption
      - **来源多样化**: 来自不同机构、出版社、网站的广泛领域文档
      - **人工标注**: 每张图像经人工精确标注
  - **Global-to-Local Controllable Receptive Module (GL-CRM)**:
      - **问题**: 文档元素尺度变化大（单行标题 vs 整页表格）
      - **解决方案**: 分层架构从全局到局部感知
      - **Controllable Receptive Module (CRM)**:
        - **输入**: 特征图X
        - **多粒度特征提取**: 使用权重共享卷积w（kernel size k）和不同膨胀率d=[d_1, d_2, ..., d_n]
        - **公式**: F_i = GELU(BN(Conv(X, w, d_i)))
        - **特征融合**: Fˆ = Concat(F_1, ..., F_n) → Conv → Sigmoid加权
        - **自适应融合**: 网络学习自动融合不同粒度特征
      - **Global-to-Local设计（三层次）**:
        a) **Global-level（浅层）**: CRM with k=7, d=[1,3,5,7] - 感知整页尺度元素
        b) **Block-level（中层）**: CRM with k=3, d=[1,2,3] - 感知文档子块（中等尺度）
        c) **Local-level（深层）**: Basic bottleneck - 聚焦局部语义信息（小尺度）
      - **优势**: 适应文档元素的多尺度特性，显著提升检测精度
  - **实验结果** - **速度和准确率双提升**:
      - **D4LA数据集**（11,092张复杂文档，27类，12种文档类型）:
        - DocLayout-YOLO: mAP **70.3%**, AP50 82.4%, FPS **144.9**
        - YOLO-v10 (Baseline): mAP 68.6%, AP50 80.7%, FPS 144.9%
        - DINO-4scale: mAP 64.7%, AP50 76.9%, FPS 26.7
        - DiT-Cascade-L: mAP 68.2%, AP50 80.1%, FPS 6.0
        - LayoutLMv3-B: mAP 60.0%, AP50 72.6%, FPS 9.0
        - **结论**: 超越所有单模态和多模态方法，同时保持最快速度
      - **DocLayNet数据集**（80,863页，11类，7种文档类型）:
        - DocLayout-YOLO: mAP **79.7%**, AP50 93.4%
        - YOLO-v10 (Baseline): mAP 76.2%, AP50 93.0%
        - DINO-4scale: mAP 77.7%, AP50 93.5%
        - DiT-Cascade-B/L: mAP 73.2%/72.6%
        - LayoutLMv3-B: mAP 75.4%, AP50 92.1%
        - **结论**: 显著超越所有方法（+2.0% vs DINO，+7.1% vs DiT-L）
      - **DocStructBench四子集性能**:
        - **Academic**: 81.8% (vs YOLO-v10 80.5%, DiT-L 81.0%)
        - **Textbook**: 73.7% (vs YOLO-v10 70.2%, DiT-L 70.8%)
        - **Market Analysis**: 69.4% (vs YOLO-v10 68.9%, DiT-L 70.8%)
        - **Financial**: 90.1% (vs YOLO-v10 89.9%, DiT-L 89.3%)
        - **结论**: 在所有文档类型上均达到或接近最佳性能
      - **速度对比**（单张A100 GPU）:
        - DocLayout-YOLO: **85.5 FPS**
        - YOLO-v10: 144.9 FPS（略快但精度较低）
        - DINO-4scale: 26.7 FPS
        - DiT-Cascade-L: 6.0 FPS
        - LayoutLMv3: 9.0 FPS
        - **结论**: 在保持高精度的同时，速度显著快于多模态方法（9-14倍）
  - **预训练数据集对比实验**（100K样本，在DocStructBench上微调）:
      - **DocSynth-300K**: Academic 82.1%, Textbook 71.5%, Market 69.3%, Financial 90.3%
      - **PubLayNet (300K)**: Academic 81.0%, Textbook 71.5%, Market 69.1%, Financial 89.7%
      - **DocBank (400K)**: Academic 81.6%, Textbook 70.9%, Market 69.1%, Financial 90.1%
      - **Diffusion (300K)**: Academic 80.7%, Textbook 71.9%, Market 68.9%, Financial 89.3%
      - **Random (300K)**: Academic 80.5%, Textbook 71.2%, Market 68.1%, Financial 89.6%
      - **M6Doc (2K)**: Academic 80.4%, Textbook 70.0%, Market 68.9%, Financial 89.7%
      - **结论**: DocSynth-300K在所有文档类型上都实现最佳或接近最佳性能，展现卓越泛化能力
  - **消融实验关键发现**:
      - **GL-CRM组件效果**:
        - **Global-level CRM**: 单独使用提升0.5% mAP
        - **Block-level CRM**: 单独使用提升0.7% mAP
        - **两者结合**: 提升1.2% mAP（D4LA: 68.6%→69.8%）
        - **结论**: 分层设计有效适应文档元素多尺度特性
      - **DocSynth-300K预训练效果**:
        - **无预训练**: D4LA 68.6%, DocLayNet 76.2%
        - **+DocSynth-300K预训练**: D4LA 69.8% (+1.2%), DocLayNet 79.3% (+3.1%)
        - **结论**: 预训练显著提升下游任务性能，尤其在复杂数据集上
      - **数据过滤必要性**: 过滤低质量样本后性能进一步提升
      - **预训练数据规模**: 性能随数据量增加（0→30K→50K→100K→200K→300K）持续提升
  - **生成数据可视化分析**:
      - DocSynth-300K生成的文档展现高度多样性：
        - 密集布局（多小元素）vs 稀疏布局（少大元素）
        - 不同元素组合（S/M/L = Small/Medium/Large主导）
        - 高美学质量（对齐、密度均优于Random和Diffusion）
      - 与Diffusion、Random方法对比，DocSynth布局更合理、更美观
  - **机构**: 上海人工智能实验室
  - **作者**: Zhiyuan Zhao, Hengrui Kang, Bin Wang, Conghui He
  - **发布时间**: arXiv 2024年10月（v1）
  - **开源**: ✅ [代码、数据和模型](https://github.com/opendatalab/DocLayout-YOLO)
  - **意义**:
      - **速度-精度权衡突破**: 首次实现单模态方法在精度上超越多模态方法，同时保持速度优势（快9-14倍）
      - **数据集贡献**:
        - DocSynth-300K提供首个大规模、多样化、高美学质量的文档合成数据集
        - DocStructBench提供全面的多文档类型评估基准
      - **方法创新**:
        - Mesh-candidate BestFit算法首次将文档合成视为装箱问题，生成美观多样的布局
        - GL-CRM模块有效处理文档元素的极端尺度变化
      - **泛化能力**: 证明在多样化合成数据上预训练可显著提升模型在各类真实文档上的泛化性能
      - **实用价值**: 为文档解析系统提供快速准确的布局分析解决方案，可直接应用于RAG系统、文档OCR等实际场景
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2407.07053">📄 Multimodal Self-Instruct</a></b><br>
<code>arXiv 2407.07053</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**: **使用语言模型合成抽象图像和视觉推理指令** - 利用LLM及其代码能力合成大量抽象图像（图表、地图、仪表盘等）和视觉推理指令，无需依赖GPT-4V
  - **数据合成方法** - **代码驱动的多模态自指导Pipeline**:
      - **核心创新**: 首个系统性探索使用LLM和代码合成抽象图像（非自然图像）的方法，证明代码生成可以精确控制抽象图像的细节
      - **多模态自指导策略（三个关键步骤）**:
        1. **视觉想法提案阶段**:
           - **任务**: LLM自主提出创意视觉想法，描述日常场景（如城市地图、流程图、统计图表）
           - **八种抽象图像类型**: 图表（Chart）、表格（Table）、模拟地图（Road Map）、仪表盘（Dashboard）、流程图（Flowchart）、关系图（Relation Graph）、2D平面布局（2D Planar Layout）、视觉谜题（Visual Puzzle）
           - **详细参数控制**: 通过自然语言描述控制图像合成的具体细节（颜色、字体、布局等）
        2. **图像合成阶段**:
           - **模拟数据生成**: LLM为提出的视觉想法生成模拟数据（如饼图百分比、地图路径点）
           - **代码生成**: LLM使用Matplotlib或ECharts等可视化库生成Python代码
           - **显式参数定义**: 代码中明确定义所有参数（图像样式、颜色、字体大小、图例位置等）
           - **图像渲染**: 执行代码生成期望的抽象图像
        3. **视觉指令构建阶段**:
           - **问题-答案对生成**: LLM基于视觉想法、模拟数据和生成代码设计多个问题-答案对
           - **问题类型多样性**:
             - **图表任务**: OCR、Caption、详细感知（位置/数量/布局）、数据提取、数学推理
             - **地图任务**: 路径规划、空间关系推理
             - **流程图任务**: 结构问题（步骤数、符号类型）、推理问题（下一步操作）
             - **关系图任务**: 树形结构问题、数学推理问题
           - **答案标注与理由**: 为每个问题提供详细理由（类似思维链），增强训练效果
      - **关键技术优势**:
        - **代码精确控制**: 通过代码精确控制抽象图像的几何特征和文本内容，避免文本到图像模型的细节控制失败
        - **无幻觉保证**: 基于代码和模拟数据生成，确保答案准确性（只要场景图准确）
        - **可解释性**: 代码作为中间表示，使数据生成过程完全可解释和可控制
        - **成本效益**: 使用GPT-4-turbo而非GPT-4V，显著降低成本
        - **可扩展性**: 通过添加新模板或自定义现有模板，轻松扩展指令数据类型
      - **数据集统计**:
        - **基准数据集**: 3,658张图像，11,193条指令（8种场景）
          - Dashboard: 73张，1,013条指令
          - RelationGraph: 66张，822条指令
          - Flowchart: 98张，1,451条指令
          - VisualPuzzle: 189张，529条指令
          - 2DPlanarLayout: 25张，252条指令
        - **训练数据集**: 19,338张图像，62,476条指令（3种场景）
          - Chart: 1,768张，34,590条指令
          - Table: 570张，10,886条指令
          - Roadmap: 17,000张，17,000条指令
        - **数据质量保证**:
          - **代码可行性过滤**: 如果生成的代码无法运行，提示LLM基于编译器错误反馈进行自我反思，最多重试3次
          - **图像美学检查**: 使用LLaVA-1.5检查图像美学（视觉元素干扰、布局合理性、文本可读性）
          - **答案准确性验证**: 采用自一致性方法，让LLM基于想法、代码和问题生成多个响应，通过投票选择最终答案
          - **人工评估**: 随机采样10%的<问题，答案>对，4名计算机科学研究生从四个维度评估（图像美学、问题合理性、答案准确性、图像-指令相关性）
      - **实验结果**:
        - **基准评估**（8种抽象图像任务）:
          - **人类水平**: 平均准确率82.1%
          - **最佳LMM性能**: Claude-3.5-Sonnet 64.74%，GPT-4o 59.99%
          - **显著差距**: 即使最先进的LMM（GPT-4o）在Dashboard任务上仅达到54.79%，远低于人类水平（85.3%）
          - **开源vs闭源差距**: 开源模型（如Vanilla Llava-1.5-7B）平均准确率仅15.4%，与闭源模型存在巨大差距
        - **微调效果**（Llava-our-62k）:
          - **图表理解**: 10.5% → 30.3% (+19.8%)
          - **表格理解**: 15.8% → 51.8% (+36.0%)
          - **地图导航**: 0.3% → 67.7% (+67.4%)，超越GPT-4o（23.3%）和Claude-3（38.3%）
          - **仅使用68K合成数据和4小时LoRA微调**，将Llava-1.5-7B的图表理解能力提升至Qwen-VL-Plus水平
        - **任务协同效应**:
          - **图表+表格训练**: 对地图导航任务有正向影响（+5%性能提升）
          - **地图训练**: 对图表和表格任务影响较小
          - **推测原因**: 不同任务所需能力不同
        - **数据规模影响**:
          - 随着合成数据量增加（35k → 47k → 62k），模型性能持续提升，未达到平台期
          - 数学推理子任务提升最明显
        - **泛化能力**（弱相关任务）:
          - **ChartQA**: 19.9% → 23.9% (+4.0%)
          - **MathVista**: 25.1% → 25.9% (+0.8%)
          - **未训练任务**: Dashboard +0.0%，RelationGraph +0.5%，Flowchart +2.7%，VisualPuzzle +0.2%，PlanarLayout +6.4%
          - **结论**: 仅训练图表、表格和地图数据，也能提升其他抽象图像推理任务
      - **关键发现**:
        - **抽象图像理解挑战**: 当前LMM在理解抽象图像方面存在显著缺陷，即使简单日常任务（如从时钟读取时间、使用地图规划路线）也经常失败
        - **代码生成优势**: 使用代码合成抽象图像可以精确控制细节，避免文本到图像模型的细节控制失败
        - **数据质量重要性**: 通过三层过滤（代码可行性、图像美学、答案准确性）确保合成数据质量
        - **可扩展性**: 方法可轻松扩展到更多场景和任务类型
      - **机构**: 浙江大学、中科院软件所、上海理工大学
      - **作者**: Wenqi Zhang, Zhenglin Cheng, Yuanyu He, Mengna Wang, Yongliang Shen, Zeqi Tan, Guiyang Hou, Mingqian He, Yanna Ma, Weiming Lu, Yueting Zhuang
      - **发布时间**: arXiv 2024年7月（v5）
      - **开源**: ✅ [代码](https://github.com/zwq2018/Multi-modal-Self-instruct) | [项目页面](https://multi-modal-self-instruct.github.io)
      - **意义**:
        - **问题识别**: 首次系统性识别当前LMM在抽象图像理解方面的显著缺陷
        - **方法创新**: 提出代码驱动的抽象图像合成方法，为LMM训练提供高质量抽象图像数据
        - **基准贡献**: 构建包含8种场景的抽象图像理解基准，揭示LMM与人类水平的巨大差距
        - **实用价值**: 提供可扩展的数据合成框架，支持定制化抽象图像数据生成
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2502.14846">📄 CoSyn</a></b><br>
<code>arXiv 2502.14846</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**: **代码引导的合成文本密集型多模态数据生成** - 利用文本LLM的编程能力自动创建多样化文本密集型图像数据
  - **数据合成方法** - **代码驱动的图像渲染 + 文本标注生成**:
      - **核心创新**: 将代码作为中间表征桥接图像与文本，充分利用文本LLM的强大编程能力
      - **三大生成阶段**:
        1. **代码生成阶段** (P_LLM(C|q)):
           - 输入：用户查询q（如"生成营养标签数据集"）
           - 输出：可执行代码C
           - LLM：Claude-3.5-Sonnet（编码能力强）
           - **支持11种渲染工具**：Matplotlib、Plotly、VegaLite、LaTeX、HTML、Mermaid、Graphviz、SVG、Asymptote、Lilypond、RDKit
        2. **图像渲染阶段** (P(I|C)):
           - 执行生成的代码C渲染图像I
           - 精确控制图像内容（文本、布局、样式）
           - 保证可复现性（代码可追溯）
        3. **指令生成阶段** (P_LLM(T|C)):
           - 基于代码C（无需图像）生成文本指令T
           - LLM：GPT-4o-mini（成本效益高）
           - 生成问答对、解释文本（支持CoT推理）
      - **20条生成管道** - 基于11种渲染工具构建:
        - **图表**: Matplotlib、VegaLite、Plotly、LaTeX、HTML
        - **文档**: LaTeX、HTML
        - **表格**: LaTeX、Matplotlib、Plotly、HTML
        - **图示**: Graphviz、LaTeX、Mermaid
        - **数学问题**: LaTeX
        - **矢量图形**: SVG、Asymptote
        - **乐谱**: LilyPond
        - **电路**: LaTeX
        - **化学结构**: RDKit
      - **多样性增强策略 - Persona驱动**:
        - **问题**: LLM采样参数难以生成多样化数据
        - **解决**: 在主题生成阶段引入**200K personas**（性格/身份描述）
        - **效果**: 从不同视角生成主题，显著提升内容多样性
        - **示例**: Persona "科幻小说家喜欢外星世界" → 主题 "外星植物与动物图解指南"
      - **四阶段Pipeline示例**（以HTML文档为例）:
        1. **主题生成**: 根据查询+persona生成文档主题（如"1月水电账单"）
        2. **数据生成**: 填充详细内容（费用明细、日期、用户信息）
        3. **代码生成**: 将数据转换为可执行代码（HTML+CSS）
        4. **指令生成**: 基于代码生成问答对（问题+解释+简洁答案）
      - **关键技术优势**:
        - **高保真度**: 代码渲染确保文本准确性（无幻觉）
        - **可控性强**: 通过代码精确控制图像结构和内容
        - **多样性高**: 支持11种工具、9大类别、100+细分查询
        - **可扩展**: 语言化查询控制，易于定制新领域
        - **成本效益**: 纯文本LLM成本远低于多模态模型
  - **数据规模**:
      - **CoSyn-400K**: 40万合成图像，270万指令调优数据
      - **9大类别分布**:
        - 图表: 11.8万 | 文档: 7.3万 | 数学: 6.8万
        - 表格: 4.8万 | 图示: 3.6万 | 矢量图形: 2.8万
        - 乐谱: 1.2万 | 电路: 1.0万 | 化学结构: 0.9万
      - **查询多样性**:
        - 图表: 51种类型 | 文档: 107种类型 | 数学: 110种类型
        - 表格: 35种类型 | 图示: 34种类型 | 矢量图形: 36种类型
      - **扩展应用 - 合成Pointing数据**: 6.5万图像的点击坐标标注
  - **模型**: 基于**Molmo架构**（CLIP-ViT-L + Mistral-7B）
      - 视觉编码器：OpenAI CLIP (ViT-L/14 336px)
      - 语言模型：Mistral-7B
      - 连接方式：MLP投影层
  - **实验结果** - **7个文本密集型基准上的SOTA**:
      - **开源模型中最佳**: 平均80.9%（超越第二名Llama 3.2 11B的77.0%，+3.9%）
      - **超越闭源模型**: GPT-4V (72.8%), Gemini 1.5 Flash (76.2%)
      - **分项成绩**:
        - ChartQA: **86.3%** (vs GPT-4V 78.1%, +8.2%)
        - DocVQA: **90.0%** (vs GPT-4V 87.2%, +2.8%)
        - InfoVQA: **70.5%** (vs GPT-4V 75.1%, -4.6%)
        - TableVQA: **65.8%** (vs GPT-4V 60.5%, +5.3%)
        - AI2D: **91.9%** (vs GPT-4V 89.4%, +2.5%)
        - TextVQA: **82.0%** (vs GPT-4V 78.0%, +4.0%)
        - ScreenQA: **80.1%** (vs GPT-4V 41.6%, +38.5%)
      - **零样本性能**（仅用辅助+合成数据，无评估集训练）:
        - 平均**74.7%**，超越GPT-4V（72.8%）
        - 超越大多数开源和闭源模型（无真实训练数据）
  - **新领域适应能力** - **NutritionQA基准**:
      - **问题**: 开源VLM在新任务（营养标签问答）上表现差
      - **零样本适应**: 仅用CoSyn-400K训练 → 匹配GPT-4V性能
      - **目标域微调**: 仅用**7K合成营养标签数据**微调 → 超越大多数百万级训练的开源VLM
      - **数据效率**: 证明针对性合成数据的极高样本效率
  - **合成数据优势分析**:
      - **消融研究**（见Figure 4）:
        - 仅辅助数据（1M图像）: 58.7%
        - 仅合成数据（400K图像）: **70.5%**（匹配GPT-4V）
        - 辅助+合成（零样本）: **74.7%**（超越GPT-4V）
        - 评估+辅助+合成（监督）: **80.9%**（SOTA）
        - **结论**: 40万合成数据贡献超过100万真实辅助数据
      - **CoT推理增强**:
        - 合成数据包含（问题、解释、简答）三元组
        - ChartQA: +3.2% | TableVQA: +1.5% | NutritionQA: +14.0%
        - 对需要多步推理的任务提升显著
      - **缓解数据偏差**（ChartQA案例）:
        - **问题**: ChartQA训练集73.9%为T5机器生成，测试集50%人工标注
        - **过拟合**: PaliGemma在机器问题上88.5%，人工问题上仅54.2%（差距34.3%）
        - **CoSyn训练**: 机器问题93.4%，人工问题79.1%（差距**14.2%**，减少20.1%）
        - **结论**: 合成数据缓解对benchmark偏差的过拟合
      - **数据多样性量化**（与现有图表数据集对比）:
        - **图像多样性**: CoSyn 0.596 vs ChartQA 0.340 (+75.3%)
        - **文本多样性**: CoSyn 0.823 vs ChartQA 0.742 (+10.9%)
        - **工具多样性**: 使用5种工具 vs 仅Matplotlib → +1.3% ChartQA准确率
      - **扩展性分析**:
        - 合成图表数量从5K → 116K，ChartQA零样本性能从64.2% → 78.2%
        - 性能持续提升，未达饱和点（建议未来扩展到更大规模）
  - **合成Pointing数据** - **SOTA点击预测**:
      - **方法**: LLM编辑代码在图像上显式绘制点 → 提取坐标
      - **数据量**: 6.5万图像的pointing标注
      - **ScreenSpot基准**:
        - 仅合成数据: 平均68.0%
        - 仅人工数据(PixMo-point 155K): 68.5%
        - 合成+人工: **74.9%**（SOTA，超越UGround 1.3M训练的73.3%）
      - **数据效率**: 6.5万合成数据匹配15.5万人工标注性能
  - **实现细节**:
      - **基础设施**: DataDreamer库（支持并行生成、响应缓存、完整日志）
      - **LLM选择**: Claude-3.5-Sonnet（代码生成强）vs GPT-4o（失败率高）
      - **成本**: CoSyn-400K数据集成本约**$8,000**
      - **训练**: TPU v3-128，batch size 32，60K步（约30小时）
  - **发布时间**: arXiv 2025年2月
  - **机构**: 宾夕法尼亚大学、艾伦人工智能研究所（Ai2）
  - **作者**: Yue Yang, Ajay Patel, Matt Deitke, Tanmay Gupta等
  - **开源**: ✅ **完全开源** - CoSyn-400K数据集、代码、模型
  - **项目页面**: [yueyang1996.github.io/cosyn](https://yueyang1996.github.io/cosyn)
  - **重要意义**:
      - **文本LLM驱动多模态**: 首次系统性地将文本LLM编程能力用于大规模多模态数据合成
      - **代码作为中间表征**: 创新性地将代码作为图像-文本桥梁，确保准确性和可控性
      - **超越渲染局限**: 突破传统模板化渲染方法的多样性瓶颈
      - **广泛适用性**: 9大类别、20条pipeline证明框架的通用性
      - **实用影响**: 证明合成数据在文本密集型理解任务上的强大潜力，为VLM训练提供新范式
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2412.01137">📄 TextSSR</a></b><br>
<code>arXiv 2412.01137</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-ICCV_2025-red?style=flat-square"/>
</summary>

  - **聚焦**: **基于扩散的场景文本识别数据合成** - 为文本in-the-wild识别生成训练数据
  - **数据合成方法** - **三大支柱扩散Pipeline：准确性、真实性、可扩展性**:
      - **核心创新**: 端到端扩散式合成，解决渲染方法（缺乏真实感）和纯生成方法（缺乏控制）的局限
      - **支柱1：准确性 - 区域中心文本生成 + 位置-字形增强**:
        1. **区域中心生成**:
           - 与图像级文本生成（易产生幻觉）不同，在**指定边界框内**生成文本
           - 使用**区域条件扩散**（受layout-to-image方法启发）
           - 确保对文本位置的精确控制，防止其他地方出现非预期文本
        2. **位置-字形增强 (PGE)**:
           - **问题**: 扩散模型在准确字符生成和序列顺序方面存在困难
           - **解决方案**: 双流条件化
             - **字形流**: 将目标文本渲染为干净的字形图像（字符形状）
             - **位置流**: 编码边界框内的字符位置
           - **融合**: 通过交叉注意力将字形+位置信息注入扩散UNet
           - **结果**: 保持自然外观的同时实现字符级准确性
      - **支柱2：真实性 - 上下文提示实现自然风格化**:
        - **挑战**: 纯文本控制生成产生通用风格；从真实图像直接风格迁移导致过拟合
        - **方法 - 上下文提示机制**:
          1. **真实场景采样**: 从STR数据集（如COCO-Text、MLT）选择真实场景文本图像
          2. **文本修复**: 使用修复模型从选定图像中移除原始文本
          3. **提示提取**: 从原始文本区域提取**低分辨率上下文提示**（颜色、纹理、方向、退化模式）
          4. **条件生成**: 条件扩散模型基于:
             - 目标文本内容（通过PGE）
             - 边界框位置
             - **上下文提示**（低分辨率纹理/颜色引导）
          5. **结果**: 生成的文本继承真实风格（失真、模糊、光照、透视）而不记忆特定实例
      - **支柱3：可扩展性 - 组合文本排列**:
        - **策略**: 系统性地从词汇表采样创建多样化文本组合
        - **语料来源**:
          - **单词**: 频率列表中的常见英文/中文单词
          - **命名实体**: 人名、品牌、地点
          - **数字序列**: 电话号码、日期、价格
        - **排列**: 生成指定长度内所有可行的n-gram和短语
        - **规模**: 从有限词汇表生成**数百万独特文本实例**
      - **质量筛选**:
        - **后合成过滤**: 使用预训练STR模型验证生成文本与目标标签匹配
        - **多模型共识**: 要求多个STR模型（CRNN、ASTER、ABINet）达成一致
        - **接受率**: ~60-70%的生成图像通过质量筛选
  - **数据规模**:
      - **TextSSR-F（过滤数据集）**: 355万质量筛选的合成场景文本图像
      - **文本长度**: 1-25字符，多样化分布
      - **风格**: 50+场景类型（街道标识、店面、文档、产品包装等）
      - **语言**: 主要英文 + 多语言子集
  - **训练Pipeline**:
      - **阶段1**: 在真实STR数据集上预训练扩散模型学习场景文本分布
      - **阶段2**: 使用PGE + 上下文提示微调实现准确可控生成
      - **阶段3**: 使用文本排列进行大规模合成
      - **阶段4**: 质量过滤产生TextSSR-F
  - **实验结果**:
      - **STR基准**: 在TextSSR-F上训练达到**与真实数据训练相当或更优**的性能
        - **IIIT5K**: 95.3%准确率（与真实数据持平）
        - **SVT**: 93.1% (+1.8% 超越合成基线)
        - **ICDAR数据集**: 持续优于基于渲染的合成数据
      - **真实+合成混合**: 通过结合TextSSR-F与真实数据达到最佳结果（平均+2.1%增益）
      - **零样本迁移**: 对未见字体、语言、失真的强泛化能力
  - **消融研究**:
      - **PGE贡献**: +8.3%准确率 超越基线扩散
      - **上下文提示**: +5.7% 超越仅字形条件化
      - **质量过滤**: 提升下游STR准确率4.2%
  - **发布时间**: arXiv 2024年7月 | ACM MM 2025
  - **机构**: *学术研究（见论文作者信息）*
  - **开源**: 🔄 **预计开源** - Code + SynthVLM-100K数据集（论文承诺）
  - **重要意义**:
      - **范式转换**: 首次将"Caption→Image"作为VLM训练主流程，颠覆传统"图像→caption"依赖
      - **质量突破**: 系统性解决Web数据三大质量痛点，建立高质量合成数据标准
      - **效率证明**: 小数据集大模型效果，为资源受限环境提供可行路径
  
      - **核心技术要点**:
        - **场景几何理解**: 使用CNN预测dense depth map，估计局部表面法线
        - **文本对齐**: 根据估计的平面方向进行透视变换，使文本与表面对齐
        - **区域约束**: 使用gPb-UCM分割，确保文本限制在具有统一颜色和纹理的区域内
        - **颜色自适应**: 从IIIT5K数据集学习文本-背景颜色对，自适应匹配目标区域
        - **泊松融合**: 使用Poisson image editing自然融合文本，保留光照梯度
      - **三阶段Pipeline**:
        1. **场景分析**:
           - 输入背景图像（需无文本，通过关键词过滤+人工检查）
           - CNN预测dense depth map（使用Liu等人[30]的方法）
           - gPb-UCM分割生成局部颜色/纹理一致的区域
           - 区域过滤：排除过小、极端长宽比、表面法线垂直视角、高纹理的区域
        2. **文本渲染与变换**:
           - 从Newsgroup20数据集采样文本（单词、行、段落）
           - 随机选择字体
           - **关键步骤**：透视变换以匹配局部表面方向
           - 颜色选择：从学习的颜色对中选择最匹配的前景-背景颜色对
           - 20%的文本实例随机添加边框
        3. **泊松图像编辑融合**:
           - 使用泊松编辑将文本与背景图像融合
           - 保留场景中的光照梯度
           - 创建自然外观的合成场景文本图像
      - **关键技术优势**:
        - **几何准确性**: 文本遵循真实表面方向，避免不自然的平坦叠加
        - **边界尊重**: 文本不跨越强烈的图像不连续性（如物体边缘）
        - **光照一致性**: 泊松融合保持场景光照特性
        - **可扩展性**: 完全自动化，可生成无限数据
  - **数据规模**:
      - **SynthText in the Wild**: 800,000张合成场景文本图像
      - **背景来源**: 8,000张通过Google Image Search收集的无文本图像
      - **文本来源**: Newsgroup20数据集
      - **标注**: 每张图像配word-level的axis-aligned bounding boxes
  - **配套文本检测器** - **FCRN (Fully-Convolutional Regression Network)**:
      - **架构**: 受FCN和YOLO启发的密集预测网络
      - **创新**: 每个位置(u,v)预测文本存在 + bounding box参数(x,y,w,h,cosθ)
      - **优势**: 30× less参数 than YOLO，无需重训练即可处理多尺度
      - **速度**: 15 images/sec on GPU，**45×快于当时SOTA**
  - **实验结果** - **SOTA文本检测性能**:
      - **训练策略**: 在SynthText上预训练 → 在小规模真实数据集上fine-tune
      - **ICDAR 2013结果**:
        - 仅合成数据预训练显著提升性能
        - 加上fine-tuning: 达到F-measure **84.2%**，竞争力SOTA水平
      - **Multi-Oriented Text (MSRA-TD500)**: 在复杂多方向文本场景中表现有效
      - **关键发现**: 几何建模的合成数据有效迁移到真实场景文本检测
  - **消融研究**:
      - **几何感知**: 使用几何感知合成的模型优于平面文本叠加
      - **颜色自适应**: 自适应颜色选择优于随机颜色
      - **Poisson融合**: 无缝融合对逼真外观至关重要
  - **发布时间**: arXiv 2016年4月
  - **机构**: University of Oxford, Dept. of Engineering Science
  - **作者**: Ankush Gupta, Andrea Vedaldi, Andrew Zisserman
  - **开源**: ✅ 数据集（SynthText in the Wild，800K图像） - 官网: [robots.ox.ac.uk/~vgg/data/scenetext](http://www.robots.ox.ac.uk/~vgg/data/scenetext)
  - **重要意义**:
      - **首创几何感知合成**: 首次系统性地将3D场景理解引入文本合成
      - **解决数据瓶颈**: 解决了场景文本检测标注昂贵的问题
      - **奠定范式**: 影响了后续大量场景文本合成工作
      - **实用价值**: 合成数据训练的模型达到当时SOTA，证明合成数据的有效性
      - **开创性工作**: 在深度学习文本检测领域具有里程碑意义
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/1604.06646">📄 合成文本定位 (Synthetic Text Localisation)</a></b><br>
<code>arXiv 1604.06646</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**: **场景文本检测的合成数据** - 生成高质量场景文本图像用于训练文本检测模型
  - **数据合成方法** - **几何感知场景文本叠加Pipeline**:
      - **核心创新**: 自然地将合成文本叠加到真实场景上，**考虑局部3D场景几何**而非简单的2D叠加
      - **关键技术组件**:
        - **场景几何理解**: 使用CNN预测密集深度图，估计局部表面法线
        - **文本对齐**: 基于估计的平面方向执行透视变换，使文本与表面对齐
        - **区域约束**: 使用gPb-UCM分割确保文本被限制在颜色和纹理均匀的区域内
        - **颜色适配**: 从IIIT5K数据集学习文本-背景颜色对，自适应匹配目标区域
        - **泊松融合**: 使用泊松图像编辑实现文本-背景无缝集成，显得自然嵌入
      - **关键技术优势**:
        - **3D几何感知**: 文本透视自然匹配表面方向，而非平面叠加
        - **区域约束**: 避免在异质区域不真实的放置
        - **自适应着色**: 文本颜色与背景自然协调
        - **无缝融合**: 泊松混合消除合成伪影
      - **合成Pipeline**:
        1. **输入**: 自然场景图像（通过Google图片搜索收集的8,000张背景图像）
        2. **深度估计**: CNN预测密集深度图
        3. **表面法线估计**: 从深度计算局部表面方向
        4. **分割**: gPb-UCM生成候选区域
        5. **区域选择**: 按大小、纵横比、均匀性过滤区域
        6. **颜色采样**: 选择与区域匹配的文本-背景颜色对
        7. **文本渲染**: 用选定颜色渲染单词（文本从Newsgroup20数据集采样）
        8. **透视变换**: 基于表面法线应用透视扭曲
        9. **泊松混合**: 无缝将文本集成到场景中
        10. **输出**: 合成场景文本图像 + 边界框标注
  - **数据规模**:
      - **SynthText数据集**: 800K合成场景文本图像
      - **标注**: 单词级和字符级边界框
      - **背景图像**: 8,000张通过Google图片搜索收集的图像（过滤确保无文本）
      - **文本来源**: Newsgroup20数据集（单词、句子、段落）
  - **实验结果** - **最先进的文本检测**:
      - **训练策略**: 在SynthText上预训练 → 在小型真实数据集上微调
      - **ICDAR 2013结果**:
        - 纯合成预训练显著提升性能
        - 微调后: 达到**F值84.2%**，具有竞争力的SOTA水平
      - **多方向文本结果（MSRA-TD500）**:
        - 在复杂多方向文本场景上展示有效性
      - **关键发现**: 具有适当几何建模的合成数据有效迁移到真实世界文本检测
  - **消融研究**:
      - **几何感知**: 使用几何感知合成的模型优于平面文本叠加
      - **颜色适配**: 自适应着色比随机颜色提高检测性能
      - **泊松融合**: 无缝混合对于真实外观至关重要
  - **发布时间**: CVPR 2016 | arXiv 2016年4月
  - **机构**: 牛津大学
  - **作者**: Ankush Gupta, Andrea Vedaldi, Andrew Zisserman
  - **开源**: ✅ [代码](https://github.com/ankush-me/SynthText) 和 [数据集](https://www.robots.ox.ac.uk/~vgg/data/scenetext/)
  - **重要意义**:
      - **开创性工作**: 首批系统性处理场景文本检测合成数据并具有几何感知的工作之一
      - **几何感知合成**: 将3D几何考虑引入文本合成，显著提高真实性
      - **影响力**: SynthText数据集在文本检测研究中被广泛用作预训练数据
      - **迁移学习**: 展示了文本检测任务中合成到真实的有效迁移
  
  #### 🏠 3D场景合成
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2407.06084">📄 SynVL3D</a></b><br>
<code>arXiv 2407.06084</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-2024年7月-red?style=flat-square"/>
</summary>

  - **聚焦**: **大规模合成数据的3D视觉语言预训练** - 构建大规模合成3D场景文本语料库，解决3D-VLP数据集场景多样性有限和细粒度标注不足的问题
  - **数据合成方法** - **3D模拟器驱动的场景生成 + 多粒度文本描述合成**:
      - **核心创新**: 利用免费3D模拟器构建大规模、多样化的合成3D场景数据集，包含对象、视图、房间三个层次的1M描述
      - **问题识别**: 现有3D-VLP数据集规模小且标注有限
        - **数据稀缺**: ScanScribe仅1.2K场景和280K文本标注
        - **多样性不足**: 场景类型和对象类别有限
        - **标注成本高**: 3D场景数据收集和标注极其昂贵
        - **细粒度缺失**: 缺乏对象级、视图级、房间级的多层次关联
      - **3D场景生成**:
        - **模拟器平台**: 基于AI2-THOR 3D模拟器环境
        - **场景规模**: 10,000个室内3D场景，108个对象类别
        - **场景图构建**:
          - 为每个房屋(场景)构建场景图，描述对象间的空间关系
          - 基于对象的空间位置、尺寸和形状定义关系
          - 三大关系类型:
            1. **支撑关系** (e.g., on, in): 基于物理接触和包含
            2. **空间关系** (e.g., next to, in front of): 基于相对位置
            3. **比较关系** (e.g., bigger than, same shape as): 基于尺寸和形状
        - **精确标注**: 提供语义(类别)、视觉(高质量mesh)、细粒度视觉标注(无误差位置、方向、分割mask)
      - **多粒度文本描述合成**:
        - **总计**: 超过1M个模板化和自由形式描述
        - **三种描述类型**:
          1. **模板化描述**:
             - **对象外观**: 使用现成图像标注器为每个对象正面视图生成标注
             - **关系三元组**: <object1, relation, object2>形式，使用模板"the object1 is relation to object2"
             - **实例描述**: 将外观描述与邻近对象关系描述合成段落
          2. **自由形式描述**: 使用GPT-3重新表述模板化描述以增强自然性
          3. **多视角描述**: 为不同视角和房间层次生成描述
        - **短语-区域关联**: 为每个名词短语训练独特标识符，建立短语与空间区域的连接
      - **多层次关联建立**:
        - **对象级关联**: 短语标识符与3D对象边界框精确对应
        - **视图级关联**: 多视角下的对象-文本对齐
        - **房间级关联**: 场景整体描述与3D场景的关联
  - **SynFormer3D预训练框架**:
      - **统一Transformer架构**: 对齐3D场景和语言的简单统一模型
      - **三大组件**:
        1. **3D对象编码器**: 处理点云特征
        2. **文本编码器**: 处理自然语言描述
        3. **跨模态融合模块**: 实现3D-文本对齐
      - **细粒度预训练任务**:
        1. **对象关系预测 (ORP)**: 预测3D对象间的空间关系
        2. **多层次区域-词对齐 (MRWA)**: 对象、房间、场景三个层次的对齐
        3. **视图聚合区域-词对齐 (VRWA)**: 多视角信息聚合对齐
      - **合成到真实域适应**:
        - **三重域判别器**: 视觉域、语言域、视觉-语言联合域
        - **梯度反转层**: 最小-最大优化解决域偏移
        - **联合适应**: 同时处理单模态和跨模态域偏移
  - **数据规模**:
      - **SynVL3D数据集**: 10,000个室内场景，1M+文本描述
      - **对象覆盖**: 108个对象类别
      - **关系类型**: 支撑、空间、比较三大类关系
      - **多粒度标注**: 对象级、视图级、房间级三层次关联
  - **实验结果** - **3D-VL任务上的SOTA性能**:
      - **3D视觉定位 (3D Visual Grounding)**:
        - Nr3D: 65.5% accuracy (vs 3D-VISTA 64.2%, +1.3%)
        - Sr3D: 77.9% accuracy (vs 3D-VISTA 76.4%, +1.5%)
        - ScanRefer: 52.3%@0.25IoU, 46.2%@0.5IoU
      - **3D密集标注 (3D Dense Captioning)**:
        - Scan2Cap: CIDEr score 72.1@0.25IoU (vs 3D-VISTA 71.0, +1.1%)
        - BLEU-4、METEOR、ROUGE等指标全面领先
      - **3D问答 (3D Question Answering)**:
        - ScanQA: EM@1达27.6% (vs 3D-VISTA 26.5%, +1.1%)
        - 在BLEU-4、ROUGE、METEOR等语言生成指标上提升
  - **消融研究发现**:
      - **细粒度预训练任务贡献**:
        - 对象关系预测 (+6.2% VG, +6.8% Cap, +2.0% QA)
        - 多层次区域-词对齐 (+5.8% VG, +6.4% Cap, +2.2% QA)
        - 视图聚合对齐 (+1.6% VG, +1.2% Cap, +0.3% QA)
      - **合成到真实适应**: 三重域适应显著提升性能 (+14.4% VG, +13.4% Cap, +3.9% QA)
      - **多层次对齐**: 对象、房间、场景层次对齐均有贡献，组合效果最佳
  - **关键发现**:
      - **合成数据有效性**: 纯合成数据预训练的模型在真实3D场景上表现优异
      - **多粒度关联价值**: 对象-视图-房间三层次关联对性能提升关键
      - **域适应重要性**: 合成到真实的域适应对泛化能力至关重要
      - **可扩展性**: 相比真实数据收集，合成方法成本低、可扩展性强
  - **发布时间**: arXiv 2024年7月 | 北京大学
  - **开源**: ✅ SynVL3D数据集(10K场景+1M描述) + SynFormer3D模型 + 训练代码
  - **重要意义**:
      - **3D-VLP数据突破**: 首次构建大规模、多层次的合成3D视觉语言数据集
      - **成本效益方案**: 为3D场景理解提供低成本、高质量的数据获取方案
      - **多粒度框架**: 建立了对象-视图-房间三层次的3D-文本关联框架
      - **域适应创新**: 提出了针对3D视觉语言任务的有效域适应方法
  

</details>
---

#### 🔄 对比学习与图像差异

<details>
<summary>
<b><b><a href="https://scholar.google.com/scholar?q=Img-Diff%20CVPR%202025">📄 Img-Diff</a></b><br>
<code>CVPR 2025</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Contrastive Data Synthesis for MLLMs** - Enhances fine-grained image recognition through object differences in similar image pairs
  - **Data Synthesis Method** - **Three-Stage Contrastive Data Pipeline: Image Pair Generation + Difference Area Localization + Difference Caption Generation**:
      - **Core Innovation**: Draws from contrastive learning principles to generate similar image pairs with fine-grained difference annotations, training models to identify subtle differences in similar images
      - **Stage 1: Image Pair Generation - Object Replacement Paradigm**:
        - **Generation Tools**: Stable-Diffusion-XL + Prompt-to-Prompt image editing technique
        - **Pipeline**:
          1. Obtain image captions from caption databases (MS-COCO, LLaVA pre-training data)
          2. Use LLM to perform object replacement in captions (prompt: "Only replace one object in this sentence")
          3. Based on caption pairs, use SDXL + Prompt-to-Prompt to generate similar image pairs
        - **Result**: Highly similar image pairs with different objects
      - **Stage 2: Difference Area Generator**:
        - **Goal**: Locate precise bounding boxes of object differences in image pairs
        - **Three Components**:
          1. **Image Similarity Filter** (used twice):
             - **First use** (on generated pairs): Extract features via CLIP, compute cosine similarity, keep highly similar but not identical pairs
             - **Second use** (on cropped sub-images): Filter out bbox regions with actual differences
          2. **Image-Text Matching Filter**:
             - Extract image features using BLIP, compare with object name text features
             - Determine whether cropped sub-images contain valid objects (replaced or replacing objects)
          3. **Difference Detector**:
             - Based on given bbox, crop two sub-images from image A and B
             - Use image similarity filter to determine if differences are significant
             - Apply IoU filtering to remove overlapping bboxes, keep only bboxes with higher difference degree
        - **Flow**: FastSAM segmentation → crop based on bbox → image-text matching filter → difference detection + IoU filter
        - **Output**: Maximum 5 valid difference bboxes per image pair
      - **Stage 3: Difference Captions Generator**:
        - **Feature**: Generates difference captions for **specific regions** (not whole image), ensuring accuracy
        - **Two-Stage Process**:
          - **Stage 1 - Object Labeling & Filtering**:
            1. Select N (default 5) bboxes with lowest similarity as candidates
            2. Use MLLM (LLaVA-NEXT) to describe each bbox region content
            3. **Image-Text Matching Filter**: Check if region content matches captions
            4. **Caption Similarity Filter**: Use CLIP text features to assess whether two captions differ
          - **Stage 2 - Difference Caption Generation**:
            1. Mark difference areas with red boxes on images for enhanced localization
            2. Provide LLaVA-NEXT with bbox content captions and marked images
            3. MLLM generates targeted difference descriptions based on this information
        - **Advantage**: Region-focused strategy avoids inaccuracy when single description can't capture all image differences
      - **Key Technical Advantages**:
        - **Fine-Grained Localization**: Bboxes precisely locate difference areas
        - **Contrastive Learning Principles**: Simulates positive-negative sample comparison mechanism of contrastive learning
        - **High-Quality Filtering**: Multiple filtering ensures data quality (image similarity, image-text matching, caption difference)
        - **Automated Scalability**: Fully automated pipeline, expandable as needed
  - **Data Scale**:
      - **Img-Diff (Main Evaluation Version)**: 12,688 high-quality "object replacement" samples
        - Source captions: MS-COCO (generated 118K image pairs → filtered to 38,533 pairs → 117,779 valid bboxes → 12,688 final samples)
      - **Extended Version**: 34,538 "object replacement" samples (based on LLaVA pre-training dataset)
      - **Object Diversity**:
        - Covers 1,203 object categories
        - 3,680 unique "object replacement pairs"
        - Object365 dataset objects appear 13,164 times in this dataset (52.06% of total occurrences)
  - **Models**: Fine-tuned based on SOTA MLLMs
      - Main evaluation: LLaVA-1.5-7B, MGM-7B, InternVL2-8B
      - Supplementary evaluation: InternVL2-1B, LLaVA-1.5-13B
  - **Experimental Results** - **Significant Improvements on Image Difference Benchmarks**:
      - **MMVP Benchmark** (evaluating MLLM visual capabilities):
        - LLaVA-1.5-7B + Img-Diff: 27.3% (original 24.0%, +3.3%, surpasses LLaVA-1.5-13B 24.7%)
        - MGM-7B + Img-Diff: **50.7%** (original 40.0%, +10.7%, **surpasses GPT-4V 38.7% and Gemini 40.7%**)
        - InternVL2-8B + Img-Diff: 43.3% (original 38.7%, +4.6%)
      - **Spot-the-Diff Benchmark** (street scene difference detection):
        - LLaVA-1.5-7B + Img-Diff: CIDEr-D **43.2** (original 38.3, +4.9)
        - MGM-7B + Img-Diff: CIDEr-D **53.5** (original 46.3, +7.2, **surpasses previous specialized model VACC 41.5**)
        - InternVL2-8B + Img-Diff: CIDEr-D **32.2** (original 26.5, +5.7)
      - **Image-Edit-Request Benchmark** (image editing differences):
        - LLaVA-1.5-7B + Img-Diff: CIDEr-D **60.9** (original 60.6, further improves SOTA)
        - MGM-7B + Img-Diff: CIDEr-D **68.1** (original 66.8, new SOTA)
        - InternVL2-8B + Img-Diff: CIDEr-D **56.0** (original 51.5, +4.5)
  - **General MLLM Benchmark Improvements** (average across 8 benchmarks):
      - **LLaVA-1.5-7B**: Average improvement **+3.06%** (comprehensive improvements)
      - **MGM-7B**: Average improvement **+1.28%**
      - **InternVL2-8B**: Average improvement **+1.01%**
      - **Key Improvements**: VQAv2, GQA, POPE (localization), MMBench, MM-Vet, ScienceQA, SEED-Bench
  - **Data Quality Assessment** (1000 samples human annotation):
      - **Bounding Box Difference**: 78.9% high (different objects), 16.6% medium (different features), 4.5% low
      - **Content Caption Accuracy**: 80.1% high (completely correct), 14.1% medium, 5.8% low
      - **Difference Caption Accuracy**: 70.4% high (completely accurate), 21.8% medium (correct objects but wrong features), 7.8% low
  - **Extended Exploration** - **Object Removal Data** (supplementary materials):
      - Generated "object removal" dataset (prompts models to analyze which image contains specific object)
      - Further improves fine-tuned MLLM performance
  - **Publication**: CVPR 2025
  - **Institution**: Sun Yat-sen University, Alibaba Group
  - **Authors**: Qirui Jiao, Daoyuan Chen, Yilun Huang, Bolin Ding, Yaliang Li, Ying Shen
  - **Open Source**: ✅ **Fully Open-Source** - Code, dataset
  - **Code Repository**: [github.com/modelscope/data-juicer/tree/ImgDiff](https://github.com/modelscope/data-juicer/tree/ImgDiff)
  - **Significance**:
      - **Contrastive Learning Dataification**: First systematic application of contrastive learning principles to MLLM data synthesis
      - **Fine-Grained Difference Recognition**: Significantly improves MLLM's ability to identify subtle differences in similar images
      - **Region-Focused Strategy**: Innovative region-level difference annotation avoids inaccuracy of whole-image descriptions
      - **Surpasses Closed-Source Models**: Fine-tuned open 7B models surpass GPT-4V and Gemini on MMVP
      - **General Capability Enhancement**: Not only enhances difference recognition but also comprehensively improves VQA and localization capabilities
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2507.19492">📄 ChartGen</a></b><br>
<code>arXiv 2507.19492</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**：**代码引导的合成图表数据与"图表→代码"评测** —— 两阶段自动化流水线：先用 VLM 将真实图表"重绘"为 Python 绘图代码，再用代码向 LLM 迭代增广生成多样图表，构建大规模多模态图表语料并提出重绘评测协议
  - **数据合成方法** - **VLM 重绘 → 代码 LLM 迭代增广**：
      1) **VLM 图表重绘**：以种子图表（ChartQA 13K）为输入，phi‑3.5‑vision-instruct 生成可执行绘图脚本，获取结构化表示
      2) **LLM 代码增广**：Codestral‑22B 对初始脚本进行 ~20 轮风格/类型/库/主题增广，执行得到新图表；显著扩大规模与多样性（不直接改图，而是改代码）
  - **数据与资源**：
      - **ChartGen‑200K**：222.5K 图像‑代码对，覆盖 27 图表类型、11 个绘图库；并提供 CSV 数据、DocTags、文本摘要与 QA 对；Held‑out 4.3K 用于重绘评测
      - **评测协议**：以 GPT‑4o 为裁判，分别比较"代码层"（数据忠实度0–1；语义/风格0–10）与"渲染图像层"（0–10），更全面刻画"图表→代码"能力
  - **实验结论**：
      - 6 个开源权重 VLM（3B–26B）在数据忠实度（≤0.58/1）与图像相似度（≤7.48/10）上仍有明显差距，"图表→代码"仍具挑战
      - 相较现有图表‑代码资源（Plot2Code、ChartMimic、ChartX、ChartCoder），本工作在规模、库覆盖与多模态配套上更全面
  - **意义**：
      - **以"代码"为图表的规范表示**：便于衍生文本摘要/QA/CSV 等多模态监督，提升训练与评测的可扩展性与可复现性
      - **推动从"问答/摘要"到"重绘/代码生成"的能力评测**：更细粒度检验图表理解与视觉条件代码生成
  - **开源**：代码、数据与基准均以 CC‑BY‑4.0 发布：`https://github.com/SD122025/ChartGen/`
  
  
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2508.06492">📄 Effective Chart Dataset (ECD)</a></b><br>
<code>arXiv 2508.06492</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**：**面向图表理解的高质量合成训练数据** —— 提出五阶段图表数据合成pipeline，构建ECD训练集与ECDBench评测集，显著提升多模态大模型（MLLM）的图表理解能力
  - **数据合成方法** - **五阶段模块化合成与质量过滤**：
      1) **单图生成（代码函数+数据分离）**：预定义29类图表函数，GPT-4o根据主题与函数接口生成数据与参数，渲染单图（10,875张）
      2) **条件式多子图组合**：基于已有子图逐步条件生成，保证多子图间的语义一致性（6,006张，多子图平均4个）
      3) **图像多样化**：自动添加注释、区域着色、缩略窗、字体/边框/配色等风格变化，包含布局与样式多维扰动
      4) **图像质量过滤**：以"可读性（visual clarity）+ 语义连贯（semantic coherence）"双指标对图像打分，过滤低质量样本（从16,829张保留至10,535张）
      5) **QA对生成与过滤**：对每张图生成描述型与推理型QA对，并保留高置信结果（最终321,544高质量QA）
  - **数据规模**：
      - **ECD训练集**：10,535张图 + 321,544个QA（覆盖25主题、29图表类型、252种子图组合）
      - **ECDBench测试集**：1,224张图（364单图、860多子图）+ 2,448 QA（每图1个描述型+1个推理型）
  - **实验结果（多模型一致增益）**：
      - 在CharXiv、ChartQA、ReachQA、ChartBench、ChartX、ECDBench六项评测上，LLaVA-Next-Llama3-8B、MiniCPM-V2.6、Phi-3-Vision、Qwen2.5-VL-7B均有整体提升
      - 例如：Qwen2.5-VL-7B在CharXiv平均由61.36%→67.40%，在ECDBench由38.19%→50.86%（报告表2与表3）
  - **关键技术优势**：
      - **代码-数据解耦与条件式子图生成**：提升样式与语义多样性并保证多子图一致性
      - **质量双指标过滤**：显著降低低质量渲染和语义不连贯样本（FID降低、像素熵提升）
      - **推理型QA保留rationale**：为训练推理能力提供可解释监督
  - **资源与可复现性**：
      - 论文提供完整pipeline描述与消融分析，并给出GitHub链接（数据与代码计划开放）
      - 代码/数据：`https://github.com/yuweiyang-anu/ECD`（以论文说明为准）
  - **重要意义**：
      - **真实度与复杂度**：与CharXiv分布对齐的风格覆盖与复杂度（更低FID、更高熵）
      - **通用可扩展**：可扩展到更多子图组合、主题与布局；能作为通用的图表合成训练基座
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2403.07750">📄 Synth²</a></b><br>
<code>arXiv 2403.07750</code>
</summary>

  - **数据合成方法** - **LLM标题 + 文本到图像嵌入生成**：
      - **核心创新**：首个完全合成的VLM训练方法，同时合成标题和图像嵌入，在嵌入空间操作以绕过像素级处理
      - **两阶段流水线**：
        - **阶段1**：LLM生成多样化、信息丰富的标题（使用外部文本语料库提示）
        - **阶段2**：文本到图像模型将标题转换为对应的图像嵌入（绕过像素生成）
      - **嵌入空间优势**：
        - **效率提升**：2.08 vs 1.66 步/秒（嵌入 vs 像素），25%训练加速
        - **质量保持**：嵌入级生成保持性能，同时大幅提高计算效率
        - **内存优化**：消除训练期间昂贵的像素编码/解码
  - **数据规模与构成**：
      - **模型参数**：632M（vs 竞争对手1.4-1.7B）
      - **数据配比**：10.1M真实数据 + 711M合成数据
      - **对比**：可比性能但仅需传统方法1/40的配对数据（vs DC-BLIP 5.5B真实数据）
  - **实验结果**：
      - **图像标题生成**：CIDEr分数131.3（微调），35.4（零样本）
      - **场景理解问答**：VQAv2 29.1→35.3 (+21%)
      - **外部知识问答**：OKVQA 32.4→36.1 (+11%)
      - **效率收益**：用约1/3的训练步骤达到基线性能，2.08 vs 1.66 步/秒（嵌入 vs 像素）
      - **数据效率**：与使用40倍配对数据训练的模型性能相当（vs. DC-BLIP 5.5B真实数据）
  - **比较分析**：
      - **vs. ITIT**：35.4 vs 32.1 CIDEr零样本（参数和数据使用量相似）
      - **vs. DC & SimVLM**：632M参数与1.4-1.7B参数竞争结果
      - **语义集中度**：GenPair显示最高熵（3.81）和最低集中度，表明卓越的多样性
  - **成本效率**：
      - **训练速度**：比像素空间训练快25%，无性能下降
      - **内存效率**：消除合成数据训练期间昂贵的像素编码/解码
      - **数据需求**：10.1M真实 + 711M合成 vs 传统方法需要数十亿真实配对
  - **机构**：Google DeepMind
  - **作者**：Sahand Sharifzadeh, Christos Kaplanis, Shreya Pathak, Dharshan Kumaran等
  - **开源**：⚠️ 论文中未指定代码/数据可用性
  - **意义**：
      - **范式创新**：首次展示了VLM的完全合成图像-文本对训练，无需依赖大规模真实数据集
      - **嵌入空间效率**：证明嵌入级生成在保持质量的同时显著提高计算效率
      - **受控方法论**：建立了用于分离合成数据贡献的严格实验框架
      - **实际部署**：为专门领域启用定制数据集创建和资源高效的VLM训练
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2507.02948">📄 DriveMRP</a></b><br>
<code>arXiv 2507.02948</code>
</summary>

  - **数据合成方法** - **基于BEV的自动驾驶高风险运动仿真**：
      - **核心创新**：首个基于VLM的运动风险预测可扩展合成数据集，解决长尾高风险场景稀缺问题
      - **三维风险建模**：系统性地从自车行为、其他车辆交互和环境约束三个维度合成风险
      - **BEV多项式仿真**：使用带车辆动力学约束的多项式轨迹生成，创建物理上合理的高风险运动
      - **数据规模**：DriveMRP-10K数据集，包含10,000个高质量运动风险场景，涵盖碰撞、急刹车、异常加速、车道违规
  - **关键技术组件**：
      - **高风险场景选择**：基于真实世界交通事故分析的碰撞事件、急刹车/加速、车道违规/偏离道路
      - **基于规则的定义**：安全距离（碰撞）、加速度幅值/持续时间（急刹车）、几何关系（车道违规）的精确阈值
      - **运动投影视觉提示**：将BEV轨迹投影到自车前视摄像头，弥合坐标和视觉之间的模态差距
      - **人机回路质量控制**：人工筛选过滤物理上不合理的轨迹，确保清晰的摄像头投影可见性
  - **DriveMRP-Agent框架**：
      - **VLM不可知架构**：使用LoRA微调与多个VLM（Qwen2.5-VL-7B、InternVL、LLaVA）配合工作
      - **思维链推理**："场景理解 → 运动分析 → 风险预测"认知路径，用于可解释的风险评估
      - **多模态输入集成**：结合BEV布局、前视场景图像和投影运动航点
      - **GPT-4o标题生成**：涵盖场景分析、运动行为解释和风险分类的结构化自然语言描述
  - **实验结果**：
      - **合成数据性能**：事故识别准确率27.13% → 88.03% (+60.9%)，在DriveMRP-10K测试集上
      - **零样本泛化**：真实世界高风险数据集准确率29.42% → 68.50% (+39.1%)，无真实世界训练暴露
      - **跨模型增强**：在LLaVA-1.5-7B、Llama3.2-vision-11B、Qwen2.5-VL-7B基线上一致改进
      - **场景理解指标**：ROUGE-1-F1 48.54→69.08，BERTScore 68.83→81.25，展示综合环境理解
  - **消融研究**：
      - **BEV信息**：对全局上下文理解和空间关系推理至关重要
      - **视觉轨迹投影**：显著优于原始坐标序列，弥合视觉-语言模态差距
      - **多输入融合**：BEV + 前视 + 投影轨迹组合达到最佳性能（88.03%准确率）
  - **成本与泛化**：
      - **训练效率**：在8个NVIDIA H100 GPU上使用Flash Attention加速进行LoRA微调
      - **真实世界迁移**：在专有真实世界数据集上的强零样本性能验证合成到真实的泛化
      - **即插即用**：数据集增强多个通用VLM的驾驶安全应用
  - **机构**：西湖大学、小米汽车、浙江大学
  - **作者**：侯志毅、马恩慧、李芳、赖志毅、何家乐等
  - **开源**：✅ [代码与数据集](https://github.com/xiaomi-ev/DriveMRP)（如所示）
  - **意义**：
      - **自动驾驶安全**：解决高风险场景覆盖的关键差距，实现更安全的自动驾驶系统
      - **合成数据范式**：展示了难以大规模收集的罕见但关键驾驶事件的有效合成
      - **可解释AI**：提供可解释的风险预测和因果分析，用于持续算法改进
      - **行业影响**：为复杂、非结构化驾驶环境中的鲁棒运动规划算法开发奠定基础
  

</details>
---

### 💭 图像介入推理

This emerging category constructs **image-text interleaved reasoning traces** where images are actively **edited and manipulated** during the reasoning process. Unlike traditional text-only approaches, these methods treat text and images as **complementary modalities** that jointly advance problem-solving through progressive visual modifications (e.g., highlighting, overlaying, zooming, inpainting).

<details>
<summary>
<b><b><a href="https://scholar.google.com/scholar?q=ThinkMorph">📄 ThinkMorph</a></b><br>
<code>Paper</code>
</summary>

  - **Data Synthesis Method** - **Multimodal Interleaved Chain-of-Thought Reasoning**:
      - **Core Innovation**: Constructs **image-text interleaved reasoning traces** where text and images function as **complementary modalities** that mutually advance reasoning
      - **Data Scale**: ~24K high-quality interleaved reasoning traces across 4 tasks
      - **Task Coverage** (varying visual engagement levels):
        - **Jigsaw Assembly** (6K): Visualizing re-arranged pieces → holistic spatial context
        - **Spatial Navigation** (6K): Overlaying mazes with paths highlighted via red lines/arrows
        - **Visual Search** (6,990): Drawing bounding boxes around target objects
        - **Chart Refocus** (6K): Highlighting regions with red bounding boxes or overlays
      - **Data Synthesis Pipeline**:
        - **Design Principle**: Progressive text→image→text sequences
        - **Generation Strategy**:
          - Jigsaw & Spatial: Custom synthesis pipeline (newly generated)
          - Visual Search & Chart: Human-in-the-loop MLLM filtering from existing datasets
        - **Quality Control**: Strict filtering (e.g., target object must occupy 1-30% of image area for Visual Search, reducing 144K→6,990 high-quality samples)
      - **Reasoning Pattern**: Initial text establishes context → Visual tokens manipulate/visualize → Final text verifies solution
      - **Key Findings**: Interleaved reasoning outperforms text-only and vision-only by 5.33% average on vision-centric tasks; exhibits emergent properties including unseen visual manipulations (zoom-in, inpainting, multi-box generation)
  - **Publication**: arXiv October 2025
  - **Institution**: National University of Singapore, Zhejiang University, University of Washington, Stanford, CUHK
  - **Open Source**: ✅ [Code & Models](https://github.com/ThinkMorph/ThinkMorph) | [Dataset](https://huggingface.co/ThinkMorph)
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2510.01582">📄 ImageNet-Think-250K</a></b><br>
<code>arXiv 2510.01582</code>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Scale-250K-orange?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-2024年10月-red?style=flat-square"/>
</summary>

  - **聚焦**: **大规模多模态推理合成数据集** - 构建包含显式思维过程的多模态推理数据集，助力视觉语言模型推理能力开发
  - **数据合成方法** - **多模态大模型驱动的思维轨迹合成**:
      - **核心创新**: 利用SOTA视觉语言模型生成包含显式推理步骤的大规模合成数据集，捕获VLM的逐步思维过程和最终描述性答案
      - **问题识别**: 现有多模态数据集局限性
        - **缺乏推理透明性**: 大多数数据集只关注输入-输出映射，不捕获中间推理步骤
        - **推理诊断困难**: 无法理解模型决策过程或诊断模型失误
        - **领域局限性**: 现有推理数据集通常领域特定或规模有限
        - **专有数据壁垒**: 训练数据通常专有或范围受限，阻碍广泛研究
      - **数据生成pipeline**:
        - **数据源**: 250,000张图像，来自ImageNet-21k数据集精选样本
        - **图像筛选标准**:
          1. **视觉质量**: 高分辨率、清晰度良好
          2. **内容完整性**: 无显著遮挡或损坏
          3. **语义多样性**: 促进泛化的多样语义类别
          4. **复杂度平衡**: 跨不同视觉复杂度级别的平衡表示
        - **双模型生成策略**:
          - **GLM-4.1V-9B-Thinking**: 生成思维轨迹1
          - **Kimi-VL-A3B-Thinking-2506**: 生成思维轨迹2
          - 每个图像配对两组thinking-answer序列，提供推理多样性
      - **统一提示设计**:
        - **提示模板**: "Please analyze this image step by step. Explain your reasoning process. Describe this image and give as much information as possible"
        - **引导目标**:
          1. 首先描述观察到的内容
          2. 解释推理过程
          3. 给出最终详细答案
        - **标准化流程**: 确保思维链生成的一致性和质量
      - **思维-答案分离**:
        - **思维tokens (Think)**: 描述对象、上下文、关系的中间推理步骤
        - **答案tokens (Answer)**: 提炼或完善图像解读的最终描述性答案
        - **配对结构**: 每个图像→2×(thinking, answer)对，支持推理质量和结果准确性评估
  - **数据规模与统计**:
      - **总数据量**: 250,000图像，500,000个thinking-answer配对
      - **类别覆盖**: 15,234个独特ImageNet-21k类别
      - **平均分布**: 每类16.4张图像，标准差12.8
      - **Token统计**:
        - **最小tokens**: 521个tokens/样本
        - **最大tokens**: 196,388个tokens/样本
        - **平均tokens**: 1,542个tokens/样本
        - **总token数**: 3亿tokens
      - **多样性指标**: 跨科学、自然、社会科学等广泛语义类别
  - **合成质量控制**:
      - **一致性检验**: 确保生成的thinking和answer逻辑一致
      - **多模型验证**: 两个SOTA VLM的交叉验证提高可靠性
      - **长度过滤**: 移除过短或异常长的响应
      - **内容质量**: 通过LLM评估响应质量和相关性
  - **基准评估框架**:
      - **推理质量指标**:
        - **语义相似度**: BERTScore、Sentence-BERT余弦相似度
        - **词汇重叠**: ROUGE-1、ROUGE-L、Jaccard指数、重叠系数
        - **向量空间**: TF-IDF余弦相似度
      - **模型比较**: 5个SOTA VLM在ImageNet-Think上的性能评估
        - InternVL-3.5-8B、VL-Rethinker-7B、VisionThink-Efficient
        - OpenVLThinker-7B、R1-OneVision-7B
      - **思维vs答案分析**: 思维tokens在语义对齐上优于答案tokens，答案tokens在词汇重叠上表现更好
  - **实验发现**:
      - **推理丰富性**: 思维轨迹提供了丰富的中间推理步骤，有助于理解VLM决策过程
      - **模型差异性**: 不同VLM在推理风格和质量上表现出显著差异
      - **评估维度**: 多维度评估揭示了语义理解和词汇表达的不同模式
      - **可扩展性**: 合成方法可扩展到更大规模和更多视觉领域
  - **关键贡献**:
      - **首个大规模推理数据集**: ImageNet-Think提供最大规模的多模态推理数据集
      - **显式思维捕获**: 系统性捕获VLM的逐步推理过程
      - **多模型视角**: 利用多个SOTA VLM提供推理多样性
      - **标准化评估**: 建立多维度推理质量评估框架
  - **发布时间**: arXiv 2024年10月 | Argonne National Laboratory
  - **开源**: ✅ ImageNet-Think-250K数据集 + 评估基准 + 数据生成代码 - 公开可用以支持研究
  - **重要意义**:
      - **推理透明化**: 为多模态推理研究提供透明的思维过程数据
      - **模型诊断工具**: 帮助研究者理解和改进VLM推理能力
      - **标准化基准**: 为多模态推理模型评估建立标准
      - **研究加速**: 降低推理数据获取门槛，促进广泛研究
  
  #### 🤖 机器人动作合成
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2505.03233">📄 GraspVLA</a></b><br>
<code>arXiv 2505.03233</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**: **基于十亿级合成动作数据预训练的抓取基础模型** - 首个完全基于大规模合成动作数据训练的VLA模型，具备直接sim-to-real迁移能力
  - **数据合成方法** - **十亿级照片级真实机器人动作生成**:
      - **核心创新**: 首个系统性方法，完全基于大规模合成动作数据训练视觉-语言-动作(VLA)模型，证明合成数据可以替代真实世界遥操作数据进行机器人学习
      - **SynGrasp-1B数据集生成**:
        - **大规模**: **10亿帧**机器人抓取数据（1000万轨迹 × ~100帧每个）
        - **对象多样性**: 来自Objaverse的240个类别中的10,680个独特对象
        - **场景多样性**: 100万个独特场景，广泛的域随机化
        - **照片级渲染**: 使用NVIDIA IsaacSim的先进光线追踪渲染，实现高保真视觉合成
      - **全面域随机化**:
        - **视觉随机化**: 材质（桌子/机器人）、光照（点光源/定向光/圆顶光）、相机视角、背景
        - **物理随机化**: 对象布局、抓取姿态、机器人轨迹、桌子高度（-0.1m到0.2m）
        - **时间随机化**: 使用CuRobo运动规划的轨迹变化
        - **指令随机化**: 对象操作的自然语言指令模板
      - **渐进式动作生成(PAG)**:
        - **思维链架构**: 集成自回归感知(VLM) + 流匹配动作生成
        - **多模态训练**: 合成动作数据 + 互联网接地数据(GRIT)的联合训练
        - **层次预测**: 边界框 → 抓取姿态 → 动作块生成
        - **跨模态对齐**: 通过互联网数据协同训练弥合sim-to-real差距
      - **高效数据生成Pipeline**:
        - **缓存机制**: 避免冗余对象加载同时确保多样性
        - **异步写入**: 并行图像保存和标签生成
        - **并行仿真**: 多线程物理仿真和渲染
        - **质量保证**: 基于力闭合的抓取合成与轨迹验证
  - **技术架构**:
      - **视觉-语言骨干**: 处理双摄像头输入（前视 + 侧视）的自回归变换器
      - **动作专家**: 基于流匹配的连续动作生成，由VLM特征条件化
      - **本体感受集成**: 来自最近两个时间步的机器人状态token，用于精确3D感知
      - **统一训练**: 处理互联网接地和合成动作任务的单一框架
  - **数据规模与质量**:
      - **总合成数据**: 10亿帧，带精确标注（相机校准、3D姿态、边界框）
      - **对象覆盖**: 240个类别确保全面的真实世界对象泛化
      - **标注丰富性**: 细粒度标签包括深度图、分割掩码、力闭合度量
      - **跨具身就绪**: 可扩展pipeline，适配不同机器人和相机配置
  - **评估与结果**:
      - **零样本性能**: 合成类别93.3%成功率，网络类别84.7%（vs. π₀: 42.3%/17.8%）
      - **Sim-to-Real迁移**: 无需真实世界微调的直接部署，优于遥操作训练模型
      - **跨域泛化**: 在训练时从未见过的对象上表现强劲
      - **小样本适应性**: 仅边界框标注90%成功率，完整轨迹数据90%成功率
      - **LIBERO基准**: 零样本设置下超越微调的π₀和OpenVLA（82.0% vs 62.7%/33.7%）
  - **关键技术贡献**:
      - **纯合成训练**: 证明合成数据对机器人基础模型训练的充分性
      - **十亿级动作数据**: 全球首个此规模的机器人操作数据集
      - **渐进式动作生成**: 支持联合感知和动作合成的新颖架构
      - **域桥接**: 通过互联网数据集成进行sim-to-real迁移的系统性方法
  - **机构**: 北京大学、Galbot
  - **开源**: ✅ [SynGrasp-1B数据集与预训练权重](https://pku-epic.github.io/GraspVLA-web)
  

</details>
---

### ✂️ 图像编辑（方法+数据）

This category focuses on **instruction-guided image editing** where models learn to transform images based on natural language instructions. These works typically combine **method innovation** (novel editing pipelines, architectures) with **large-scale data synthesis** (automated data engines, quality benchmarks), making them distinct from pure dataset construction efforts.

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2406.11262">📄 GenLLaVA</a></b><br>
<code>arXiv 2406.11262</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**: **生成式视觉指令微调** - 首个统一多模态模型，同时实现图像理解、生成和编辑能力，无性能退化
  - **数据合成方法** - **三能力统一训练Pipeline**:
      - **核心创新**: 首个系统性方法，通过指令微调集成三个预训练模型（Mistral-7B + SigLIP + Stable Diffusion v1.4），实现统一视觉理解、生成和编辑
      - **架构设计**:
        - **语言模型**: **Mistral-7B**作为基础LLM，提供优异语言能力
        - **视觉编码器**: **SigLIP-L/384px**（比CLIP更强）提供鲁棒图像-文本匹配
        - **生成模块**: **Stable Diffusion v1.4**配合Q-former生成头进行文本到图像合成
        - **投影层**: 2层GELU MLP将视觉patch投影到语言嵌入空间
      - **视觉生成机制**:
        - **视觉令牌**: 在指令后附加N个可学习的[IMG]令牌，带可训练词嵌入
        - **生成头**: Q-former序列到序列模型T将[IMG]令牌转换为语义潜在集合U = {u₁, u₂, ..., uₗ}
        - **潜在扩散集成**: 视觉潜在U引导Stable Diffusion在潜在空间进行图像生成/编辑
        - **特殊令牌**: [SOI]/[EOI]标记视觉生成令牌的开始/结束，用于任务消歧
      - **训练数据组成**（GVIT-mix-2076K）:
        - **图像理解** [61.56%]: LLaVA微调指令集用于视觉理解任务
        - **图像生成** [26.88%]: ~558K倒置图像-文本对，来自LAION/SBU/CC3M，带GPT-4生成的提示（如"请生成[caption]的图像"）
        - **图像编辑** [11.56%]: GPT-4V处理的编辑数据集，带自然语言编辑指令
      - **单阶段训练**: 与LLaVA的两阶段方法不同，GenLLaVA使用跨所有能力的统一单阶段指令微调
  - **技术实现细节**:
      - **任务令牌系统**: 专门令牌引导模型行为（[SOI]、[EOI]用于生成任务）
      - **多任务损失**: 结合自回归语言建模 + 扩散去噪目标
      - **生成令牌数量**: 最优N=16视觉令牌（消融显示N=4过拟合，N>16性能下降）
      - **视觉编码器消融**: SigLIP-L/384px > CLIP-L/336px > CLIP-B/224px 在所有任务上
  - **数据规模**:
      - **总训练集**: **207.6万指令跟随样本**（GVIT-mix-2076K）
      - **生成数据**: 558K图像-文本对，带动态生成的指令前缀
      - **理解数据**: LLaVA-1.5指令微调数据集（视觉推理、VQA等）
      - **编辑数据**: GPT-4V处理的自然语言指令引导编辑样本
  - **评估与结果**:
      - **高级知识**: MathVista (30.5% vs 28.3% Unified-IO2), MMMU (37.1% vs 35.5% Unified-IO2)
      - **通用理解**: SEED-B (64.5% vs 61.6% Unified-IO2), MMBench (66.8% vs 57.9% Unified-IO2)
      - **生成任务**: CC3M (12.5 FID), MS-COCO (0.73 CLIPScore) 与专门模型竞争
      - **编辑能力**: EVR基准 (66.9% vs 50.2% Unified-IO2) 展示优秀的指令引导编辑
      - **多任务权衡**: 在所有任务上保持与专门模型竞争的性能
  - **关键技术贡献**:
      - **统一架构**: 首个端到端模型实现理解+生成+编辑，无能力冲突
      - **指令集成**: 通过共享指令接口为所有视觉任务提供无缝自然语言控制
      - **性能保持**: 证明适当设计的多能力训练不会降低单个任务性能
      - **可扩展框架**: 模块化设计，易于集成更强的视觉编码器、LLM或扩散模型
  - **机构**: 莱斯大学、Google DeepMind
  - **开源**: ✅ [数据集、代码、模型检查点、视觉聊天演示](https://arxiv.org/abs/2406.11262)
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2506.03107">📄 ByteMorph</a></b><br>
<code>arXiv 2506.03107</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**: **非刚性运动编辑** - 首个大规模数据集解决相机运动、物体形变、人体关节运动和人物-物体交互
  - **数据合成方法** - **运动引导的分层合成**:
      - **核心创新**: 结合**VFX启发的分层合成**与**GPT-4o运动语义标注**的自动化pipeline
      - **4阶段Pipeline**:
        1. **视频源收集**: 网络规模视频语料库 → 运动检测（光流） → 高分辨率（≥720p）运动丰富片段
        2. **分层合成**: 前景分割 → 背景稳定 → 保留运动的层合成
        3. **GPT-4o标注生成**: 多模态理解 → 运动感知的自然语言指令
        4. **质量保证**: CLIP美学评分 + 光流连贯性 + LLM指令-编辑对齐验证
      - **关键优势**: 大规模保留真实运动动态（自动化手工VFX工作流）
  - **数据规模**:
      - **ByteMorph-6M**: 600万高分辨率编辑三元组（源图像、指令、编辑图像）
      - **分布**: 180万相机运动、150万物体形变、180万人体关节运动、90万HOI
      - **分辨率**: 大部分1024×1024，最小512×512
  - **基准**: ByteMorph-Bench（613个专家验证测试样本，难度分级）
  - **模型**: ByteMorpher（扩散Transformer基线）
  - **实验结果**:
      - 在运动指标上超越InstructPix2Pix/MagicBrush **+18.3%**
      - 人工偏好: **73.5%** vs. 基线
      - 证明运动特定训练至关重要（静态数据集模型: 32.1%成功率）
  - **发布时间**: arXiv 2025年6月
  - **机构**: 字节跳动Seed、USC、东京大学、UC伯克利、斯坦福、UCLA
  - **开源**: ✅ 数据集（600万三元组）、基准（613样本）、模型、代码 - 计划在OpenDataLab/HuggingFace发布
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2505.20275">📄 ImgEdit</a></b><br>
<code>arXiv 2505.20275</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**: **统一图像编辑数据集和基准** - 涵盖多样化单轮编辑和具有身份一致性的挑战性多轮任务
  - **数据合成方法** - **集成VLM、检测、分割和修复的多阶段自动化Pipeline**:
      - **核心创新**: 结合**VLM编排**与**专用视觉工具**的端到端自动化工作流，实现可扩展的高质量编辑数据生成
      - **5阶段统一Pipeline**:
        1. **初始候选生成（VLM驱动）**:
           - 使用**GPT-4o**分析源图像并生成编辑任务候选
           - 涵盖8大编辑类别: 对象添加、删除、替换、属性修改、背景变化、风格迁移、空间重排、多对象编辑
           - 生成针对图像内容定制的自然语言编辑指令
        2. **定位与检测**:
           - 部署**Grounding DINO** / **YOLO-World**进行对象定位
           - 将VLM识别的编辑目标转换为精确边界框
           - 处理显式对象和抽象概念（如"最左边的椅子"）
        3. **实例分割**:
           - 应用**SAM（Segment Anything Model）**获取像素级精确掩码
           - 确保编辑操作尊重对象边界
           - 对添加/替换任务中的自然合成至关重要
        4. **任务特定修复与编辑**:
           - **对象删除**: 内容感知修复（SD-Inpaint、LaMa）
           - **对象添加**: 基于扩散的对象插入与协调
           - **替换**: 保留上下文的掩码引导生成
           - **属性修改**: 局部风格/颜色调整
           - **背景变化**: 前景保留 + 背景合成
        5. **质量控制与后处理**:
           - **自动过滤**: 基于CLIP的指令-图像对齐评分
           - **伪影检测**: 识别可见接缝、不自然边界、不一致光照
           - **人工回环验证**: 基于样本的质量审核（数据集的5%）
           - **身份一致性验证**（多轮编辑）: 确保相同对象在轮次间保持视觉身份
      - **关键创新**: 与纯生成方法不同，ImgEdit将**复杂编辑分解为模块化视觉任务**，确保可控性和准确性
  - **数据规模**:
      - **ImgEdit数据集**: 120万高质量编辑三元组（源、指令、编辑后）
      - **单轮编辑**: 95万样本（新颖复杂的单步变换）
      - **多轮编辑**: 25万样本（具有身份一致性的序列编辑）
      - **指令复杂度**: 平均每条指令18.7词，78.3%需要空间/语义推理
  - **基准**: **ImgEdit-Bench**
      - **规模**: 1,000个精选测试样本，涵盖所有编辑类别
      - **难度分层**: 简单（20%）、中等（50%）、困难（30%）
      - **评估指标**: CLIP-Sim、FID、LPIPS、身份一致性分数（多轮）、人工评估
      - **挑战性案例**: 细粒度属性（如"将领带改为条纹图案"）、多对象协调、跨轮次风格保留
  - **实验结果**:
      - 最先进的指令遵循编辑性能
      - **多轮编辑**: ImgEdit训练模型保持**87.3%身份一致性** vs. 基线的**52.1%**
      - **泛化**: 强迁移到未见编辑类型和领域
      - **人工评估**: 在比较中**69.8%**优于InstructPix2Pix、MagicBrush
  - **发布时间**: arXiv 2025年2月 (v1: 2025年2月)
  - **机构**: 北京大学深圳研究生院、鹏城实验室、Rabbitpre AI
  - **开源**: ✅ 数据集（120万三元组）、基准（1K样本）、代码 - 论文中提供发布详情
  - **交叉引用**: 另见[典型多模态数据集](#-典型多模态数据集)了解数据集详情
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2506.03481">📄 RefEdit</a></b><br>
<code>arXiv 2506.03481</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**: **指称表达式引导的图像编辑** - 通过文本指称表达式（如"左边的红苹果"）进行精确对象级编辑
  - **数据合成方法** - **GPT-4o、定位与FlowChef的可扩展合成Pipeline**:
      - **核心创新**: 利用**可扩展合成数据生成**的少样本学习方法，超越百万级基线
      - **3阶段自动化Pipeline**:
        1. **指令生成（基于GPT-4o）**:
           - 输入: 源图像 + 对象标注（来自RefCOCO/RefCOCO+/RefCOCOg）
           - **GPT-4o**生成涉及指称表达式的多样化编辑指令
           - 指令类型: 添加、删除、替换、重新着色、调整大小、重新定位对象
           - 强调**空间关系**（如"笔记本电脑右侧的瓶子"）
        2. **定位与分割**:
           - **Grounded Segment Anything (Grounded-SAM)**定位被指称对象
           - 为编辑目标生成精确掩码
           - 通过上下文推理处理模糊指称
        3. **使用FlowChef的受控编辑**:
           - **FlowChef**: 基于流的合成，实现自然对象插入/修改
           - 执行编辑的同时保留背景一致性
           - 质量过滤: 基于CLIP的指令遵循验证
      - **关键发现**: 仅**2万合成三元组**即可使模型超越在**>100万样本**上训练的基线
  - **数据规模**:
      - **RefEdit训练数据**: 2万高质量合成编辑三元组
      - **植根于RefCOCO**: 基于已建立的指称表达式数据集
      - **指令多样性**: 12种编辑类型 × 多样化空间/属性变体
  - **基准**: **RefEdit-Bench**
      - **基础**: RefCOCO测试图像配专家标注的编辑任务
      - **重点**: 评估编辑中指称表达式理解的精确性
      - **指标**: 对象定位准确率 + 编辑质量（CLIP-Sim、FID、人工评估）
  - **模型**: **RefEdit模型**
      - **架构**: 基于扩散的编辑模型，条件化于指称表达式
      - **训练**: 在2万合成数据上微调
  - **实验结果**:
      - **RefEdit-Bench**: 尽管训练数据少**50倍**，仍超越MagicBrush、InstructPix2Pix
      - **指称精度**: **91.2%对象定位准确率** vs. 仅指令基线的**67.3%**
      - **少样本优越性**: 证明数据质量 > 数量范式
  - **发布时间**: arXiv 2025年6月 (v1: 2025年6月)
  - **机构**: 亚利桑那州立大学
  - **开源**: ✅ RefEdit-Bench、模型、2万训练数据 - 论文中提供详情
  - **交叉引用**: 另见[典型多模态数据集](#-典型多模态数据集)
  

</details>
<details>
<summary>
<b><b><a href="https://scholar.google.com/scholar?q=Referring%20Image%20Editing%20/%20RefCOCO-Edit%20CVPR%202024">📄 Referring Image Editing / RefCOCO-Edit</a></b><br>
<code>CVPR 2024</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-CVPR_2024-red?style=flat-square"/>
</summary>

  - **Focus**: **First systematic formulation of Referring Image Editing (RIE)** as object-level generative task
  - **Core Contribution**:
      - **Task Definition**: Formalizes RIE as editing specific objects identified by referring expressions
      - **ReferDiffusion Framework**: Tailored diffusion-based architecture for RIE
      - **RefCOCO-Edit Dataset**: Early-stage benchmark derived from RefCOCO
  - **Data Synthesis Method** - **Paint-by-Example + Blended Latent Diffusion**:
      - **Pipeline**:
        1. **Source**: RefCOCO images with referring expression annotations
        2. **Reference Image Collection**: Gather exemplar edited images for target attributes
        3. **Mask-Guided Synthesis**:
           - **Paint-by-Example**: Example-based inpainting for object attributes
           - **Blended Latent Diffusion**: Smooth blending of edited regions with original image
        4. **Quality Control**: Manual filtering + automatic consistency checks
      - **Scale**: Small-scale benchmark (exact size not specified, typical early benchmark scale ~500-2K samples)
  - **RefCOCO-Edit Dataset**:
      - **Components**: Images, editing prompts with referring expressions, source object segmentation masks, reference edited images
      - **Editing Types**: Object attribute changes (color, texture, style) guided by referring expressions
  - **ReferDiffusion Model**:
      - **Architecture**: Dual-branch diffusion model
        - **Referring Branch**: Encodes referring expressions + grounds target objects
        - **Editing Branch**: Applies conditional diffusion to masked regions
      - **Innovation**: First to integrate referring expression grounding into diffusion editing
  - **Experimental Results**:
      - Establishes baseline performance on RefCOCO-Edit
      - Demonstrates superiority over generic instruction-guided editors for object-specific tasks
  - **Significance**:
      - **Pioneering Work**: First systematic treatment of RIE as distinct task
      - **Early Benchmark**: RefCOCO-Edit serves as foundational evaluation dataset
      - **Methodological Blueprint**: Influenced subsequent works (RefEdit, ImgEdit)
  - **Publication**: CVPR 2024
  - **Institution**: Academic research (see CVPR paper)
  - **Open Source**: ✅ RefCOCO-Edit dataset, ReferDiffusion code (check CVPR supplementary materials)
  - **Cross-Reference**: See also [Benchmark Datasets](#-benchmark-datasets) for RefCOCO-Edit details
  

</details>
---

### 🧩 组合性/偏好导向合成

This category focuses on **synthetic data generation for enhancing compositional understanding** in Vision-Language Models. These methods use controlled data synthesis to improve models' ability to understand complex compositional relationships (e.g., attribute binding, spatial relationships, counting) and align with human preferences.

<details>
<summary>
<b><b><a href="https://scholar.google.com/scholar?q=COMO">📄 COMO** 🏷️</a></b><br>
<code>Paper</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Improving Vision and Language Concepts Understanding with Multimodal Counterfactual Samples** - Generate both textual and visual counterfactual samples to improve VL models' concept understanding beyond "bag-of-objects" limitations
  - **Data Synthesis Method** - **Multimodal Counterfactual Generation Pipeline**:
      - **Core Innovation**: First framework to simultaneously generate textual and visual counterfactual samples, addressing VL models' weaknesses in attribute, relation, and word order understanding
      - **Counterfactual Text Generation**:
        - Use **BERT** masked language models to replace key concept words (nouns, verbs, adjectives) in original captions
        - **NLP Parsing**: Identify objects (nouns), relations (verbs/adverbs), and attributes (adjectives) using spaCy
        - **Word Replacement Strategy**: Mask selected concept → retrieve most probable replacements → filter synonyms using WordNet
        - **Quality Control**: Choose highest-scoring candidate that creates true negative (non-synonymous replacement)
      - **Counterfactual Image Generation**:
        - Use **Stable Diffusion** to generate corresponding counterfactual images from counterfactual captions
        - **Image Selection**: Generate 10 candidates, select best based on dual CLIP similarity: score = ε_T(T_c)·ε_V(V_i) + ε_V(V_o)·ε_V(V_i)
        - **Quality Assurance**: Ensure changed concept (causal) is learnable while preserving unchanged concepts (spurious)
      - **Contrastive Learning Enhancement**:
        - **Counterfactual Guided Loss**: Feed factual and counterfactual pairs into same mini-batch as hard negatives
        - **Weighted Hard Negative Loss**: Dynamically reweight importance using normalized similarity: α_ij = (n-1)·S(T_i,V_j) / Σ_k≠i S(T_i,V_k)
        - **Dual Contrastive Objectives**: Push counterfactual embeddings away from factual anchors while matching counterfactual image-text pairs
  - **Data Scale**:
      - **Base Dataset**: MS-COCO (113K images, 567K captions)
      - **COCO-CF Dataset**: 680K images + 1,134K captions (567K counterfactual image-text pairs added)
      - **Augmentation Ratio**: 5× increase in caption diversity, 6× increase in image diversity
  - **Experimental Results**:
      - **VL-Checklist**: Attribute +3.17%, Relation +2.12%, Object +1.70% over best baselines
      - **Winoground**: Text +1.60%, Image +4.35%, Group +2.63% improvements
      - **Compositional Reasoning**: Significant gains in understanding spatial relations, object attributes, and word order changes
      - **Ablation Findings**: Both text and image counterfactuals necessary; In-Batch strategy crucial vs Random sampling
  - **Institution**: School of Computer Science and Technology, Xidian University, Xi'an, China
  - **Open Source**: ✅ [Dataset & Code](https://github.com/laichengen/COMO)
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2411.02545">📄 TripletCLIP</a></b><br>
<code>arXiv 2411.02545</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-2024年11月-red?style=flat-square"/>
</summary>

  - **聚焦**: **通过合成视觉-语言难负样本增强CLIP组合推理能力**
  - **数据合成方法** - **LLM引导的难负样本标注生成 + T2I模型对应图像合成**:
      - **核心创新**: 生成语义上相似但组合结构不同的难负样本图像-文本对，使用三元对比学习训练CLIP
      - **两阶段Pipeline**:
        1. **LLM生成难负样本标注**:
           - 使用**Mistral-7B-Instruct-v0.2**通过上下文学习生成高质量难负样本标注
           - **提示策略**: 要求生成"大部分相似但引入足够显著差异，使两个描述不可能指向同一图像"的标注
           - **变化类型**:
             - **对象替换**: "狗在窗户旁" → "猫在窗户旁"
             - **空间关系**: "狗在猫左边" → "猫在狗左边"
             - **属性变换**: "红色汽车" → "蓝色汽车"
             - **动作变化**: "人在跑步" → "人在走路"
           - **质量控制**: 单个高质量负标注胜过多个低质量负标注
        2. **T2I模型生成对应负样本图像**:
           - 使用**SDXL-Turbo**快速生成负样本图像（对应负标注）
           - **速度**: 8×RTX A6000上3天生成1300万负样本标注
           - **LLM选择**: Mistral-7B-Instruct-v0.2表现最佳，输出易于解析
           - **质量评估**: ViLT模型验证生成图像平均76%准确度跟随文本提示
      - **TripletCLIP训练策略**:
        - **三元对比损失**: L_TCL = L_NegCLIP(X,Y,Y') + L_NegCLIP(X',Y',Y)
        - **交替监督**: 使用(X,Y,Y')和(X',Y',Y)两个三元组交替训练
        - **难负样本规律化**: 负图像用于规律化负标注的效果并稳定预训练
  - **数据规模**:
      - **TripletData数据集**: 1300万图像-文本难负样本对
      - **基础数据**: 基于CC3M(260万)和CC12M(1200万)数据集扩展
      - **数据类型**: 每个正样本对应一个精心构造的负样本对
  - **训练策略**:
      - **计算预算公平**: 与基线方法保持相同的训练计算量
      - **模态特定消融**: 分别验证难负样本标注和图像的贡献
      - **概念覆盖度分析**: 在不同概念多样性水平下评估性能
  - **实验结果**:
      - **组合理解基准**:
        - **SugarCrepe**: 相比LaCLIP提升**+9.4%**(CC3M)和**+10.9%**(CC12M)
        - **SugarCrepe**: 相比NegCLIP提升**+6.3%**(CC3M)和**+6.5%**(CC12M)
        - **所有子类别**: 在对象/属性替换、交换、添加任务上全面提升
      - **零样本任务**:
        - **图像-文本检索**: R@5指标显著提升(CC3M: +11.1%, CC12M: +16.1%)
        - **ImageNet分类**: Top-1准确率提升(CC3M: +3.5%, CC12M: +7.0%)
        - **VTAB基准**: 视觉任务适应基准保持竞争力
      - **消融研究发现**:
        - **负标注单独**: 相比LaCLIP在SugarCrepe上+7.6%
        - **负图像单独**: 相比LaCLIP在SugarCrepe上+2.2%
        - **两者结合**: 达到最佳性能+9.4%
  - **关键发现**:
      - **双模态难负样本效果**: 负标注+负图像比任一单独使用更有效
      - **数据效率**: 仅用一半正样本+一半负样本即超越全正样本基线
      - **LLM生成质量**: LLM生成的负标注质量显著优于规则替换方法
      - **概念覆盖独立性**: 即使在较低概念覆盖度下也能保持性能优势
  - **发布时间**: arXiv 2024年11月 | 亚利桑那州立大学 & 马里兰大学巴尔的摩分校
  - **开源**: ✅ 代码、模型、TripletData数据集 - [tripletclip.github.io](https://tripletclip.github.io)
  - **重要意义**:
      - **CLIP组合理解突破**: 首个同时利用难负样本图像和文本的CLIP训练方法
      - **可扩展性**: 提供了可应用于其他VLM的通用三元对比学习框架
      - **实用性**: 在相等计算预算下取得显著性能提升，具有良好的效率-效果权衡
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2503.01167">📄 SPARCL</a></b><br>
<code>arXiv 2503.01167</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-CVPR_2025-red?style=flat-square"/>
</summary>

  - **聚焦**: **通过具有细微变化的多模态合成数据增强VLM组合理解**
  - **数据合成方法** - **真实图像特征注入快速T2I模型 + 自适应边距损失**:
      - **核心创新**: 生成正/负标注对配**视觉基础图像**，训练VLM进行细粒度组合区分
      - **3阶段Pipeline**:
        1. **标注对生成（基于LLM）**:
           - 使用**LLM**（如GPT-4）生成具有细微组合变化的正/负标注对
           - **正标注**: 准确描述图像内容
           - **负标注**: 在保持语义相似性的同时引入组合错误
           - **变化类型**:
             - **属性绑定**: "红苹果和绿香蕉" → "绿苹果和红香蕉"
             - **对象计数**: "三只狗" → "两只狗"
             - **空间关系**: "猫在狗左边" → "狗在猫左边"
             - **动作归属**: "女人拿伞" → "男人拿伞"
        2. **真实特征注入的图像合成**:
           - **挑战**: 纯文生图模型难以实现精确组合控制
           - **解决方案**: 将**真实图像特征**注入快速T2I模型（如SDXL-Turbo）
           - **方法**:
             - 从**真实参考图像**（如COCO、Visual Genome）提取特征
             - **特征注入**: 同时基于文本标注+真实图像特征条件化T2I生成
             - 确保生成图像忠实反映标注中的组合细节
           - **速度**: SDXL-Turbo实现快速生成（4-8步 vs. 标准扩散的50+步）
        3. **用于域对齐的风格迁移**:
           - 对合成图像应用**风格迁移**以匹配真实图像分布
           - 减少合成训练数据与真实测试图像之间的域差距
           - 使用神经风格迁移或轻量级风格适配器
      - **自适应边距损失**:
        - **问题**: 对比学习中的固定边距对所有负样本一视同仁
        - **解决方案**: 基于标注相似度的**自适应边距**
        - **公式**: 边距与正/负标注间文本相似度成反比
        - **效果**：更难的负样本（更相似的标注）获得更小边距 → 模型学习更精细的区分
  - **数据规模**：
      - **SPARCL数据集**：大规模合成组合数据（未指定确切规模，可能10万-100万对）
      - **标注对**：每张图像关联正标注 + 多个负变体
      - **组合类别**：涵盖4+种主要组合推理类型
  - **训练策略**：
      - **高效微调**：使用**LoRA适配器**进行参数高效训练
      - **对比学习**：训练VLM区分正/负标注-图像对
      - **自适应边距**：基于标注相似度动态调整边距
  - **实验结果**：
      - **组合基准**：在Winoground、ARO、CREPE、SugarCrepe上显著提升
        - **Winoground**：超越CLIP基线+12.3%
        - **ARO（属性绑定）**：+8.7%
        - **SugarCrepe（困难负样本）**：+10.1%
      - **泛化**：在标准VQA任务上保持强性能（无退化）
      - **数据效率**：用中等规模合成数据取得增益（无需billion级数据集）
  - **关键发现**：
      - **真实特征注入至关重要**：纯T2I生成在细粒度组合控制上失败
      - **自适应边距有效性**：超越固定边距对比学习**+4.2%**
      - **合成数据充分性**：目标合成数据比扩大真实数据更有效
  - **发布时间**：CVPR 2025 | arXiv 2025年3月 (v2: 2025年3月)
  - **机构**：未明确说明（学术研究）
  - **开源**：✅ 代码、合成数据、LoRA适配器 - 论文中提供发布详情
  - **重要意义**：
      - **解决VLM弱点**：针对已知的组合理解局限
      - **高效合成**：快速T2I + LoRA实现可扩展、成本效益高的数据生成
      - **方法论创新**：真实特征注入 + 自适应边距为组合数据合成提供蓝图
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2402.15504">📄 Gen4Gen</a></b><br>
<code>arXiv 2402.15504</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-CVPR_2024-red?style=flat-square"/>
</summary>

  - **重点**：**多概念组合生成的生成式数据管道** - 使用级联AI基础模型的半自动数据集创建管道Gen4Gen，用于多概念个性化
  - **数据合成方法** - **半自动多阶段组合管道**：
      - **核心创新**：利用图像前景提取、LLM、MLLM和图像修复的最新进展，将个性化概念组合成具有密集对应文本描述的现实场景
      - **三个设计原则**：
        1. **详细图文配对**：文本必须与对应图像良好对齐，为前景和背景对象提供信息
        2. **合理的对象布局和背景生成**：对象仅在现实生活中可能共存时才共存，且它们在图像中的位置合理
        3. **高分辨率**：确保数据集满足生成高质量、多概念个性化图像的最终目标
      - **Gen4Gen管道**（三个主要阶段）：
        1. **对象关联和前景分割**：
           - **输入**：一组k个对象O = {o_i}^k，其中每个对象o_i由一组n张图像X_oi = {x_j}^n表示
           - **源数据**：DreamBooth、Custom Diffusion、在线版权免费源
           - **对象组合选择**：找到对象组合子集O' = {o_a, o_b, ...}，这些组合直观上可能共存（例如，狗、猫、室内植物）
           - **前景分割**：应用DIS（类别无关的显著性对象检测器）来分割组合O'内对象的前景
           - **输出**：分割的前景图像D(X')和对应的掩码M(D(X'))
        2. **LLM引导的对象组合**：
           - **边界框生成**：利用LLM的零样本能力，询问ChatGPT提供给定对象组合O'的可能边界框集合
           - **基于模板**：向ChatGPT展示几个示例，说明在COCO数据集中给定对象边界框提供边界框点的任务
           - **尺度增强**：利用GPT-4进行逻辑增强，要求每个边界框的尺度合理（解决某些对象不现实地更大的缩放问题）
           - **组合**：在D(X')内按照边界框位置和给定大小放置各个图像，获得前景图像I_fg和掩码M(I_fg)
           - **背景提示生成**：通过验证与同一LLM模型的有效性，获得描述I_fg可能放置的场景的提示集合P
        3. **背景重绘和图像重新标注**：
           - **背景检索**：从版权免费源（Unsplash）查找起始背景图像I_bg，提示p ∈ P
           - **修复**：使用文本到图像扩散修复模型f（Stable-Diffusion-XL）通过将I_fg嵌入背景图像I_bg中来重绘I_fg
           - **掩码平滑**：利用平滑软掩码（在M(I_fg)上使用5×5窗口进行平均平滑）以增强前景对象与背景的集成
           - **输出**：最终图像I_O' = f(I_fg, M(I_fg), I_bg)
           - **重新标注**：询问MLLM（LLaVA-1.5）为所有组合的子集提供详细描述I_O'的标注（字数限制：30，受CLIP上下文约束的77个令牌最大值限制）
      - **训练时提示工程策略**：
        - **全局组合令牌**：将DreamBooth概念适应复杂组合，为每个对象引入全局令牌和单独令牌，以增强描述详细场景安排的能力
        - **训练期间重复概念令牌提示**：采用在训练期间重复概念令牌提示的策略，鼓励模型确保生成的图像中每个指定概念的存在
        - **合并背景提示**：确保背景在训练提示中说明，以分离背景和概念组合
      - **关键技术**：
        - **DIS分割**：类别无关的显著性对象检测器，对使用的对象集合不可知
        - **LLM引导组合**：利用LLM的零样本能力实现合理的对象布局
        - **尺度增强**：GPT-4逻辑增强确保合理的对象比例
        - **扩散修复**：Stable-Diffusion-XL用于高质量背景集成
        - **MLLM重新标注**：LLaVA-1.5用于详细标注生成，保持对齐
      - **MyCanvas数据集**：
        - **规模**：150个对象（有些为单图像，有些为多图像），41个可能组合，超过10K图像手动过滤至**2,684张**最佳质量图像
        - **标注统计**：平均词长17.7，约30%的长度超过20个词
        - **对象多样性**：广泛的对象范围，超越CustomConcept101和DreamBooth数据集
        - **重新标注覆盖**：应用于MyCanvas数据集中的10个对象组合O'
      - **全面评估指标**：
        - **CP-CLIP（组合-个性化-CLIP）**：评估组合和个性化的准确性
          - **组合准确性**：文本中提到的每个个性化概念是否在图像生成过程中反映？
          - **保真度**：生成的个性化概念是否与其源对应物相似？
        - **TI-CLIP（文本-图像对齐CLIP）**：通过评估模型在各种文本背景下的泛化质量，作为潜在过拟合的指标
      - **实验结果**：
        - **多概念个性化**：使用增强数据集（MyCanvas）和提示策略的先前方法（Custom Diffusion）可以在生成具有不同背景的现实多概念图像的同时保持个性化概念的身份，获得显著改进
        - **改进**：在非常复杂的组合、具有挑战性的引导（相对位置）和多个语义相似概念（例如，同一图像中的两个狗身份）下更加明显
        - **基线**：在Custom Diffusion基础上构建的简单基线，具有经验提示策略，供未来研究人员在MyCanvas上评估
  - **发布时间**：CVPR 2024 | arXiv 2024年2月
  - **机构**：加州大学伯克利分校、牛津大学、哈佛大学、CMU、香港大学、加州大学戴维斯分校
  - **开源**：✅ [项目网站](https://danielchyeh.github.io/Gen4Gen/) | [GitHub](https://github.com/danielchyeh/Gen4Gen) - 代码、MyCanvas数据集（2,684张图像）、基准测试指标
  - **重要意义**：
      - **整合AI基础模型**：半自动数据集创建管道引入了使用级联AI基础模型生成高质量数据集的可能性
      - **数据集质量重要**：概念验证MyCanvas数据集反映了简单组合良好对齐的图像和文本描述对将显著改善多概念个性化任务
      - **多概念个性化基准**：全面评估基准考虑了多概念个性化任务中的个性化准确性、组合正确性和文本-图像对齐
      - **链接基础模型**：证明链接强大的基础模型可能是针对各种挑战性任务生成高质量数据集的有前景方向
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2502.01720">📄 SynCD</a></b><br>
<code>arXiv 2502.01720</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-CVPR_2025-red?style=flat-square"/>
</summary>

  - **重点**：**生成用于文本到图像定制的多图像合成数据** - 通过创建合成定制数据集（SynCD）来解决文本到图像定制挑战的简单方法，该数据集包含同一对象在不同光照、姿态和背景下的多张图像
  - **数据合成方法** - **掩码共享注意力 + 3D一致性 + 数据集过滤**：
      - **核心创新**：利用现有文本到图像模型和3D资产创建高质量合成数据集，包含同一对象在不同上下文中的多张图像，在生成具有不同上下文的多张图像时保持对象身份
      - **SynCD数据集生成管道**（三个主要步骤）：
        1. **LLM辅助提示生成**：
           - **对象描述**：设计每个提示以包含对象和背景的详细描述
           - **刚体对象**：使用Cap3D描述Objaverse资产（例如，"带蓝色和粉色条纹的大金属鼓"）
           - **可变形对象**：指示LLM生成描述性标注（例如，"俄罗斯蓝猫有厚实、蓬松的被毛，呈钢蓝色，带有绿眼睛"）
           - **背景提示生成**：指示LLM（指令调优的Llama3）基于对象描述生成合理的背景场景描述
           - **组合**：将一个对象描述与多个背景描述组合并输入图像生成步骤
        2. **多图像一致对象生成**：
           - **基础模型**：使用基于DiT的FLUX模型生成具有一致对象的图像
           - **掩码共享注意力（MSA）机制**：
             - **方法**：修改扩散模型的注意力块，使得每个图像关注自身以及其他图像的前景对象区域
             - **公式**：MSA({q_i, k_i, v_i}^N) ≡ Softmax(q_i [k_1 ... k_N]^T / √d' + M_i) [v_1 ... v_N]
             - **掩码M_i**：初始化使得一个图像的文本令牌不关注其他图像令牌，且第i个图像特征仅关注其他图像的对象区域，忽略其背景
             - **效果**：能够在所有图像中生成具有相似视觉特征的对象
           - **具有3D一致性的刚体对象生成**：
             - **深度引导**：对于具有可用3D数据集（Objaverse）的刚体对象，从N个不同相机姿态渲染资产，并将渲染的深度图和标注输入深度条件FLUX模型
             - **深度引导**：确保对象跨图像的3D形状一致性
             - **特征变形**：对于生成具有同一对象的两张图像的代表性示例，给定潜在特征f_i ∈ R^(h×w)×d, i ∈ {1,2}，变形计算为：
               - f̂_2(u,v) = α f_1(u+Δu, v+Δv) + (1-α) f_2(u,v)
               - 其中(u+Δu, v+Δv)表示第一张图像中的对应位置，α是二进制标量，表示该位置在第一张图像中是否可见
             - **应用**：对所有对应用变形，使用适当的掩码，仅在早期扩散时间步期间应用
             - **效果**：在不引入变形伪影的情况下增加多视图一致性，并允许光照变化的灵活性
        3. **数据集过滤**：
           - **美学分数过滤**：拒绝美学分数低于6的图像
           - **对象身份相似性**：使用DINOv2测量对象身份相似性，移除其集合内平均成对特征相似性低于0.7的图像
           - **最终数据集**：包含约95,000个对象，每个对象2-3张图像，在刚体和可变形类别之间均匀分布
      - **基于编码器的模型训练**：
        - **架构**：使用SynCD数据集微调现有文本到图像扩散或基于流的模型
        - **训练设置**：给定对象的N张图像，将一张视为目标，其余视为参考
        - **共享注意力机制**：为了在真实参考图像上条件化生成，采用与数据集生成管道类似的共享注意力
          - 在每个注意力块中沿序列维度将参考图像特征与目标图像特征连接
          - 目标图像的查询特征随后通过关注自身和参考图像的特征来更新
        - **训练目标**：分别对扩散和基于流的模型采用速度或流预测目标
      - **推理方法**：
        - **归一化引导向量**：使用先前工作直接组合文本和图像引导通常会导致生成图像中的过度曝光问题，特别是在高图像引导时
        - **提出的解决方案**：归一化图像和文本引导向量
          - 公式: ε_θ(x_t, {x_i}^K, ∅) + λ_I ||g||/||g_I|| · g_I + λ_c ||g||/||g_c|| · g_c
          - 其中g_I = ε_θ(x_t, {x_i}^K, ∅) - ε_θ(x_t, ∅, ∅), g_c = ε_θ(x_t, {x_i}^K, c) - ε_θ(x_t, {x_i}^K, ∅), ||g|| = min(||g_I||, ||g_c||)
        - **效果**：有助于在仍遵循文本提示的同时实现与参考对象的更好图像对齐
        - **灵活性**：参考图像的数量可以从训练中变化，因为基于注意力的条件化对序列长度不可知
      - **关键技术**：
        - **掩码共享注意力**：能够在多张图像中生成一致的对象
        - **刚体对象的3D一致性**：深度引导和特征变形确保多视图一致性
        - **训练中的共享注意力**：允许模型从多个参考图像中学习
        - **归一化引导推理**：在保持文本和图像对齐的同时缓解过度曝光问题
      - **数据规模**：
        - **SynCD数据集**：约95,000个对象，每个对象2-3张图像
          - **刚体对象**：来自Objaverse的75,000个刚体类别资产
          - **可变形对象**：16个可变形动物超类别，约100个不同亚种
        - **均匀分布**：在刚体和可变形类别之间均匀分布
      - **实验结果**：
        - **定量比较**（3个输入参考图像）：
          - **Ours(1B)**：MDINOv2-I 0.806, CLIPScore 0.773, TIFA 0.303, GeometricScore 0.801
          - **Ours(3B)**：MDINOv2-I 0.822, CLIPScore 0.789, TIFA 0.313, GeometricScore 0.838
          - **Ours(12B)**：MDINOv2-I 0.778, CLIPScore 0.771, TIFA 0.306, GeometricScore 0.780
          - 所有变体在总体GeometricScore指标上都优于或与其他基线相当
        - **人工评估**：
          - **Ours(1B) vs JeDi**：69.51%文本对齐，63.05%图像对齐，80.89%照片真实感，68.19%总体偏好
          - **Ours(3B) vs Emu-2**：70.49%文本对齐，66.88%图像对齐，64.66%照片真实感，66.74%总体偏好
          - **Ours(12B) vs OminiControl**：56.27%文本对齐，58.30%图像对齐，54.47%照片真实感，58.02%总体偏好
        - **消融研究**：
          - **SynCD数据集贡献**：仅使用SynCD数据集进行微调已经改善了性能
          - **共享注意力有效性**：通过共享注意力添加参考条件进一步提升了性能
          - **多个参考图像**：允许在推理期间使用多个参考图像，随着参考图像数量增加到三个，性能得到改善
          - **归一化引导**：在缓解过度曝光问题方面优于引导重新缩放
      - **模型变体**：
        - **Ours(12B)**：微调FLUX模型，仅使用LoRA微调注意力层
        - **Ours(1B/3B)**：使用IP-Adapter初始化的潜在扩散模型，在自注意力块和图像交叉注意力层中的键值投影矩阵中微调LoRA层
      - **发布时间**：CVPR 2025 | arXiv 2025年2月
  - **机构**：卡内基梅隆大学、Meta
  - **开源**：✅ 代码和数据可在项目网站获取
  - **重要意义**：
      - **解决数据短缺**：通过内部特征共享和外部3D引导创建此类数据集比收集具有同一对象的多个图像的真实世界数据更具可扩展性
      - **成本效益定制**：使用内部特征共享和外部3D引导生成一致的对象身份，比使用真实图像进行模型定制任务更易处理
      - **多图像监督**：在具有共享注意力的多图像数据集上训练基于编码器的模型改善了定制质量
      - **推理创新**：归一化引导向量有助于在遵循文本提示的同时实现更好的图像对齐
  

</details>
---

### 🧪 交错图文·连贯性与一致性

This category focuses on **high-quality interleaved image-text data construction** with emphasis on **coherence (logical flow), consistency (factual accuracy), and alignment (image-text relevance)**. Unlike simple image-text pairs, these methods curate or synthesize multi-image documents with narrative coherence, making them suitable for training models on long-context multimodal understanding and generation.

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2506.09427">📄 InterSyn</a></b><br>
<code>arXiv 2506.09427</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**: **交错图文生成数据集与评估** - 首个全自动、大规模、多轮指令跟随的交错图文问答数据集，配套专用评估模型SynJudge
  - **数据合成方法** - **SEIR (Self-Evaluation with Iterative Refinement)**:
      - **核心创新**: 三阶段迭代refinement pipeline，嵌入自我检查和反馈循环，确保语义完整性、跨模态协同和上下文相关性
      - **准备阶段**（5个步骤）:
        1. **问题收集**: 25名参与者各提供40个自然对话场景问题（共1000个）
        2. **问题筛选与基准**: LLM+专家审核，筛选500个高质量问题构建benchmark
        3. **问题模板提取**: 从高质量问题中提取通用化模板
        4. **基础主题层级**: AI辅助主题提取+人工组织，构建逻辑清晰的主题层级
        5. **主题层级扩展**: AI建议+专家策划，扩展至8个域、65个类别、3500个细粒度主题
      - **SEIR三阶段Refinement**（每个对话轮次执行，K=3次迭代）:
        - **Stage 1: Question Refinement (QR)**:
          - 初始化: 从模板τ和主题z生成初始问题q₀
          - 迭代refinement: LLM生成refinement建议 → 根据建议优化问题
          - 效果: 3轮迭代后质量提升**32%**
        - **Stage 2: Answer Refinement (AR)**:
          - 初始化: 生成初始答案a₀和临时caption γ₀
          - 迭代refinement: LLM评估答案和caption → 生成建议 → 优化
          - 效果: TCC **+15%**, ICC **+11%**, ITS **+19%**
        - **Stage 3: Image Refinement (IR)**:
          - 使用临时caption生成初始图像 → VLM评估 → 优化caption → 重新生成图像
          - 效果: 进一步提升ICC和ITS
      - **关键技术**:
        - **马尔可夫性质**: 每次迭代仅依赖前一状态
        - **跨轮连贯性**: 通过历史上下文H维护主题一致性
        - **多模型组合**: Qwen/InternLM/GPT + QwenVL/InternVL/LLaVA + FLUX
  - **SynJudge评估模型**:
      - **训练数据**: 38,400人工标注样本
      - **基座模型**: QwenVL2.5 / InternVL2.5
      - **四维评估**:
        1. **TCC (Text Content Completeness)**: 文本内容完整性
        2. **ICC (Image Content Completeness)**: 图像内容完整性
        3. **IQ (Image Quality)**: 图像质量
        4. **ITS (Image-Text Synergy)**: 图文协同性（奖励互补对齐，惩罚冗余）
      - **vs. 人工评估**: RMSE仅5%偏差（vs. 其他模型的13%）
  - **数据规模**:
      - **InterSyn**: 1.8M单轮样本 + 50K多轮对话
      - **Benchmark**: 500个高质量问题
      - **主题覆盖**: 8个域、65个类别、3500个细粒度主题
  - **实验结果** - **模型微调显著提升**:
      - **Anole微调** (50K InterSyn): TCC +14%, ICC +7.6%, IQ +6.2%, ITS **+30%**
      - **VILA-U微调**: TCC **+29.7%**, ITS **+52.1%**
      - **vs. 现有模型**: InterSyn生成样本在所有维度上超越GPT-4o+DALL-E3（+0.34~0.66）
  - **开源**: ✅ [GitHub](https://github.com/xxx/InterSyn) (具体链接待确认)
  - **机构**: Nankai University + Shanghai Innovation Institute + Wuhan University + USTC + Shanghai AI Lab
  - **发布时间**: arXiv 2025年6月
  - **重要意义**:
      - **首个大规模交错图文指令数据**: 填补instruction-following交错数据空白
      - **完全自动化pipeline**: SEIR大幅降低人工成本
      - **四维评估体系**: SynJudge提供细粒度、可解释评估
      - **跨模态协同**: 强调ITS指标，突破传统一致性评估
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2406.10462">📄 CoMM</a></b><br>
<code>arXiv 2406.10462</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-CVPR_2025-red?style=flat-square"/>
</summary>

  - **聚焦**: **连贯的交错图文数据集**，配多视角质量过滤和新颖评估任务
  - **数据筛选方法** - **多视角过滤策略 + 质量评估框架**:
      - **核心创新**: 非纯合成，而是使用**跨三个维度的多模型过滤**对网络抓取的交错数据进行**系统性筛选和质量增强**
      - **3视角过滤Pipeline**:
        1. **文本序列过滤（连贯性）**:
           - **目标**: 确保文本序列的逻辑流程和叙事连贯性
           - **方法**:
             - 使用**基于LLM的连贯性评分**（如GPT-3.5/4）评估文本可读性和逻辑进展
             - 检测并删除具有以下问题的文档:
               - 话题突变
               - 句子不连贯
               - 语法结构差
           - **阈值**: 校准连贯性分数 ≥ 0.75（0-1刻度）
        2. **图像序列过滤（一致性）**:
           - **目标**: 保持同一文档中图像序列的视觉一致性和相关性
           - **方法**:
             - **基于CLIP的图像相似度**: 测量连续图像间的视觉连贯性
             - **对象/场景一致性**: 使用检测模型（YOLO、DINO）验证图像间一致的实体
             - **美学质量**: 过滤低质量、模糊或重水印图像
           - **标准**: 删除具有以下问题的序列:
             - 图像间相似度极低（< 0.3 CLIP分数）
             - 单一文档内风格/域剧烈变化
             - 大部分图像未通过质量检查
        3. **图文对齐过滤（相关性）**:
           - **目标**: 确保图像与周围文本之间的紧密对齐
           - **方法**:
             - **跨模态检索验证**: 对每张图像，验证其在针对周围文本段落检索时排名靠前
             - **基于CLIP的图文匹配**: 计算图像与相邻文本之间的对齐分数
             - **标注一致性检查**: 使用VLM（如BLIP-2）为图像生成标注，验证与文档文本的语义匹配
           - **过滤**: 删除对齐分数 < 0.5的图文对
      - **多模型共识**:
        - 组合多个模型（CLIP、BLIP-2、GPT-4、定制分类器）的分数
        - 要求跨模型一致以避免单模型偏差
        - **集成策略**: 使用校准阈值的加权平均
      - **源数据**:
        - **网络爬取**: CommonCrawl、维基百科、教育网站
        - **初始规模**: 过滤前约200万原始文档
        - **过滤后规模**: 22.7万高质量连贯文档
  - **数据规模**:
      - **CoMM数据集**: 22.7万文档、228万图像、1.39亿文本token
      - **平均文档长度**: 约611 token、每文档约10张图像
      - **领域**: 新闻文章、教程、教育内容、故事叙事
  - **新颖评估任务（提出4项任务）**:
      1. **连贯图像生成**: 给定文本大纲生成连贯图像序列
      2. **连贯文本生成**: 给定图像序列生成叙事文本
      3. **连贯性评估**: 评估交错文档的连贯性质量
      4. **长上下文跨模态检索**: 在多图像文档中检索相关图像/文本
  - **基准构建**:
      - **测试集**: 5K高质量留出文档
      - **人工标注**: 专家对连贯性、一致性、对齐的评分（3分制）
      - **自动指标**: 基于CLIP、基于LLM和定制连贯性指标
  - **实验结果**:
      - **使用CoMM预训练**: 在CoMM上训练的模型在交错理解任务上比在非过滤数据上训练的模型提升**+8.3%**
      - **连贯性指标**: CoMM过滤数据得分**0.82连贯性** vs. 原始网络数据的**0.61**
      - **对齐质量**: **87.5%**图文对齐准确率 vs. 未过滤数据的**62.3%**
      - **泛化**: 强迁移到下游任务（长文本VQA、多图像推理）
  - **消融研究**:
      - **每项过滤的贡献**:
        - 文本过滤: +3.1%连贯性
        - 图像过滤: +2.7%一致性
        - 对齐过滤: +4.2%相关性
      - **多模型共识**: 超越单模型过滤**+5.8%**
  - **发布时间**: CVPR 2025 | arXiv 2024年6月 (v3: 2024年6月)
  - **机构**: 未明确说明（学术研究）
  - **开源**: ✅ CoMM数据集（22.7万文档）、评估基准（5K测试集）、过滤代码、评估指标 - 论文中提供发布详情
  - **交叉引用**: 另见[典型多模态数据集](#-典型多模态数据集)了解数据集详情
  - **重要意义**:
      - **质量重于数量**: 证明严格过滤 > 原始规模对交错数据的重要性
      - **多维质量**: 首个系统性同时解决连贯性、一致性和对齐问题
      - **方法论贡献**: 多视角过滤框架可应用于其他网络规模筛选任务
      - **基准创新**: 专门为评估交错数据质量提出新任务
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2501.03675">📄 SMIR</a></b><br>
<code>arXiv 2501.03675</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **重点**: **高效多图像推理合成数据管道** - 用于多图像推理的合成数据生成管道，包含高质量数据集和评估基准测试
  - **数据合成方法** - **多模态嵌入 + 迭代随机采样**:
      - **核心创新**: 使用多模态嵌入高效识别相关图像，应用聚类采样和图迭代采样确保指令微调的多样性和鲁棒性
      - **阶段1: 多模态嵌入构建**:
        - **方法**: 结合SigLIP或CLIP图像嵌入与对应的标题嵌入
        - **公式**: E_multimodal = E_image + c·E_caption（其中c = 0.2用于ShareGPT4V数据集）
        - **目的**: 捕获视觉和文本关系，更好地识别和聚类相关图像
        - **降维**: 应用UMAP进行降维，保留基本数据结构
      - **阶段2: 迭代随机采样**:
        - **算法**: 使用基于累积距离的概率分布迭代选择语义相关图像
        - **概率分布**: p(x_j) ∝ 1/(Σ∥x_j - x_u∥^k + ε)，其中k（默认：12）控制邻近度强调
        - **目的**: 平衡语义连贯性和多样性，允许有意义的多图像关系同时引入随机性
        - **优势**: 有效聚类相关图像，避免断开的分组
      - **阶段3: 合成数据生成**:
        - **LLM**: 使用Meta Llama 3.1 70B Instruct Turbo（开源LLM）
        - **成本效率**: 比GPT-4便宜**50倍**，速度快**10倍**
        - **两种系统提示类型**:
          1. **LLaVA风格提示**: 专注于较短的视觉问题，通常需要基于OCR的理解
          2. **长形式推理提示**: 设计用于多步推理和更深层的上下文理解
        - **数据源**: ShareGPT4V（120万图像-标题对）
        - **批处理**: 每批包含20,000张图像，生成5,000个合成对话
      - **关键技术**:
        - **多模态嵌入**: 整合视觉和描述性信息以更好地识别相关性
        - **迭代采样**: 确保多样性同时保持连贯性
        - **开源LLM**: 与闭源替代方案相比显著降低成本
        - **模块化设计**: 易于适应新数据集和应用
  - **SMIR-BENCH评估基准测试**:
      - **规模**: 200个多样化示例，涵盖七个复杂推理任务
      - **任务类别**:
        1. **鸟类**: 识别物种并推理区分特征
        2. **匹配**: 基于视觉相似性配对照片
        3. **OCR**: 阅读和推理学术文本
        4. **模式**: 在结构化任务中识别视觉模式
        5. **排序**: 基于上下文偏好对对象排序
        6. **故事叙述**: 从图像序列叙述事件
        7. **视觉**: 在图像之间建立有意义的连接
      - **评估方法**:
        - **多轮**: 支持多轮交互
        - **自由形式响应**: 通过自由形式响应和推理理由评估模型
        - **判断模型**: 使用GPT-4o作为判断模型进行成对比较
        - **框架**: 将Auto-Hard-Auto v0.1框架扩展到多模态评估
  - **数据规模**:
      - **SMIR数据集**: 160,000个合成训练样本
      - **源图像**: 使用640,000个图像-标题对生成160,000个合成对话
      - **平均统计**:
        - 最大轮数: 24，最小轮数: 2，平均轮数: 9.65
        - 每个对话平均图像数: 4.65
        - 平均用户令牌: 25.51，平均助手令牌: 124.32
  - **实验结果**:
      - **模型微调**: 在SMIR上微调的模型在SMIR-BENCH上比基础版本提升高达**8%**
      - **SMIR-8B-SIGLIP-LLAMA3**: 58.1分（vs Mantis-8B-siglip-llama3基线+8.1%）
      - **SMIR-8B-IDEFICS2**: 58.0分（vs Mantis-8B-Idefics2基线+8.0%）
      - **vs. 闭源模型**: 尽管数据集规模较小，SMIR训练的模型显著优于MANTIS微调的对应模型
  - **发布时间**: arXiv 2025年1月
  - **机构**: TogetherAI、加州大学伯克利分校、斯坦福大学、加州理工学院
  - **开源**: ✅ [GitHub](https://github.com/togethercomputer/SMiR) - 代码、SMIR数据集（16万样本）、SMIR-BENCH（200个示例）
  - **重要意义**:
      - **解决多图像推理差距**: 针对开源VLM在多图像任务中的已知弱点
      - **成本效益合成**: 开源LLM降低成本50倍，速度提升10倍
      - **相关图像聚焦**: 确保图像相关性，推进复杂多图像推理
      - **全面基准测试**: SMIR-BENCH提供严格评估，支持多轮、自由形式响应
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2501.00958">📄 2.5 Years in Class</a></b><br>
<code>arXiv 2501.00958</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-浙江大学_+_阿里达摩院-red?style=flat-square"/>
</summary>

  - **聚焦**: **教学视频转多模态教科书** - 从在线教学视频中构建高质量交错图文"教科书"语料库，提升VLM预训练效果
  - **数据合成方法** - **视频转教科书多级Pipeline**:
      - **核心创新**: 首个系统化从教学视频构建交错图文数据集的方法，通过多级提取（视频→ASR→关键帧→OCR）生成高质量教科书级数据
      - **问题识别**:
        - 现有交错图文数据集（MMC4、OBELICS）来源于网页爬取，存在**知识密度低、图文关系松散、图像间逻辑连贯性差**的问题
        - 在线教学视频（如几何课程）包含丰富的基础知识，但在VLM训练中未被充分利用
      - **三阶段数据构建Pipeline**:
        1. **收集教学视频**:
           - **知识分类体系构建**: 使用GPT-4o构建包含3915个知识点的分类体系，涵盖6个学科（数学、物理、化学、地球科学、工程、计算机科学）
           - **视频检索**: 基于知识分类体系在YouTube等平台自动检索教学视频
           - **元数据过滤**: 使用LLM审核视频元数据（标题、描述、评论），过滤非教学内容
           - **规模**: 收集159,565个教学视频，过滤后保留75,000个高质量视频（22,697课时，平均18分钟/视频）
        2. **视频级提取与过滤**:
           - **音频转录（ASR）**: 使用Whisper-large-v3将音频转为文本，保留时间戳
           - **ASR精炼**: 使用Qwen2-72B-Instruct精炼口语化ASR文本，提升语法和连贯性
           - **质量评分**: 使用DeepSeek-V2和Llama3-70B对ASR文本评分，过滤低质量视频
        3. **片段级提取（Long Video→Short Clips）**:
           - **视频分割**: 根据ASR时间戳将长视频分割为短片段（每段对应一个完整语义单元）
           - **ASR片段合并**: 将不完整的ASR片段合并为语义连贯的段落
           - **质量过滤**:
             - 使用VideoLlama2-7B为每个片段生成caption
             - 计算片段caption与ASR的相似度（GTE-Qwen2-7B-Instruct）
             - 过滤视觉内容与ASR不匹配的片段
           - **规模**: 生成4M视频片段
        4. **关键帧级提取**:
           - **关键帧检测**: 使用SSIM（结构相似性指数）算法检测帧间变化，提取关键帧
           - **OCR提取**: 使用InternVL2提取关键帧中的文本、符号、公式
           - **OCR过滤**:
             - 去除与ASR无关的OCR（如仅显示演讲者）
             - 去除与前一帧相同的OCR
             - 去除缺少有用信息的关键帧
           - **规模**: 提取6.5M关键帧，生成0.75B文本token（ASR + OCR）
        5. **教科书样本构建**:
           - 将多个 `<关键帧, OCR, ASR>` 片段拼接为单个样本
           - 每个样本平均包含10.7个关键帧和1,297个文本token
           - **最终规模**: 610K交错图文样本
      - **与现有数据集对比优势**:
        - **In-sample Image Similarity（样本内图像相似度）**: 0.686（vs. MMC4 0.319, OBELICS 0.345），表明教学视频的帧序列更连贯
        - **平均图像数/样本**: 10.7（vs. MMC4 5.7, OBELICS 2.5），内容更丰富
        - **平均文本token/样本**: 1,297（vs. MMC4 417, OBELICS 816），知识密度更高
  - **数据统计**:
      - **视频规模**: 75K教学视频，22,697课时（2.5年）
      - **关键帧**: 6.5M
      - **文本**: 259M ASR tokens + 500M OCR tokens
      - **最终样本**: 610K交错图文样本
      - **学科分布**: 数学（21.7K视频）、物理（11K）、化学（4.5K）、地球科学（12K）、工程（13K）、计算机科学（12.8K）
  - **实验结果** - **显著提升知识与推理密集型基准**:
      - **预训练LLaVA-1.5-7B**（在610K教科书数据上持续预训练）:
        - **MathVista**: 1-shot 43.4%（vs. MMC4 30.0%, OBELICS 28.5%，**+13.4%~14.9%**）
        - **ScienceQA**: 1-shot 29.4%（vs. MMC4 1.6%, OBELICS 2.8%，**+26.6%~27.8%**）
        - **MathVision**: 1-shot 25.6%（vs. MMC4 21.3%, OBELICS 20.1%，**+4.3%~5.5%**）
        - **平均提升**: 在7个VQA基准上平均提升**+11.5%**（vs. OBELICS）
      - **预训练Idefics2-8B**:
        - **MathVista**: 8-shot 29.7%（vs. MMC4 27.8%, OBELICS 27.6%）
        - **持续预训练**: 从Idefics2-8B-base持续预训练，所有基准均有提升
      - **In-Context Learning增强**:
        - 教科书数据显著提升模型利用few-shot上下文的能力
        - 在"1-shot Cheat"实验中（测试样本直接放入上下文），教科书训练模型准确率达94.1%（MathVista），远超MMC4（72.6%）和OBELICS（67.7%）
      - **SFT阶段迁移**: 预训练收益可迁移到指令微调阶段，进一步提升下游任务性能
  - **消融研究关键发现**:
      - **ASR精炼至关重要**: 去除ASR精炼后，困惑度从13.92升至16.86，准确率下降4.9%
      - **OCR重要性**: 去除OCR后，准确率下降2.3%，对数学相关任务影响更大
      - **SSIM优于其他关键帧提取方法**: Pixel-level提取器产生18M关键帧（过多冗余），CLIP-based仅产生1.7M（遗漏关键帧），SSIM提取的6.5M关键帧最优
      - **图像顺序重要**: 打乱图像顺序后，准确率从31.1%降至22.1%（-9%），证明视频帧的时序连贯性对学习至关重要
  - **机构**: 浙江大学、阿里达摩院
  - **作者**: Wenqi Zhang, Hang Zhang, Xin Li, Jiashuo Sun, Yongliang Shen, Weiming Lu, Deli Zhao, Yueting Zhuang, Lidong Bing
  - **发布时间**: arXiv 2025年1月（v4）
  - **论文链接**: [arXiv:2501.00958](https://arxiv.org/abs/2501.00958)
  - **项目主页**: https://multimodal-interleaved-textbook.github.io/
  - **意义**:
      - **数据来源创新**: 首次系统化从教学视频构建VLM预训练数据，填补"教科书级"多模态数据空白
      - **知识密度高**: 相比网页爬取数据，教学视频内容更结构化、知识密度更高、图文关系更紧密
      - **In-Context Learning提升**: 显著增强VLM的上下文感知能力，模型更有效利用few-shot示例
      - **可扩展性**: Pipeline完全自动化，可轻松扩展到更多学科和语言
  

</details>
---

### 图像不变文本增强

This category of methods keeps original images fixed while enriching and improving paired text quality through various techniques. **This is currently the most mainstream multimodal data synthesis paradigm.**

> **Note**: Only includes papers that explicitly describe data synthesis/generation methods, with specific synthesis components annotated.

<details>
<summary>
<b><b><a href="https://scholar.google.com/scholar?q=MM-IFEngine%20ICCV%202025">📄 MM-IFEngine</a></b><br>
<code>ICCV 2025</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-ICCV_2025-red?style=flat-square"/>
</summary>

  - **Focus**: **Multimodal Instruction Following Data Generation Engine** - Automatically generating high-quality multimodal instruction following data and evaluation benchmarks with complex constraints
  - **Data Synthesis Method** - **LLM-Driven Constraint Integration and Verification Pipeline**:
      - **Core Innovation**: First systematic multimodal instruction following (MMIF) data generation engine that automatically integrates diverse constraints into visual instructions and constructs comprehensive evaluation benchmarks through LLM
      - **Problem Identification**:
        - Existing MMIF training data is scarce and constraints are simple (e.g., VisIT-Bench, MIA-Bench only contain atomic-level constraints)
        - Weak correlation between constraints and visual content leads to insufficient instruction following ability in real-world scenarios
        - Imprecise evaluation methods: LLM-as-a-judge has misjudgment issues on tasks requiring precise output constraints (e.g., word count)
      - **Four-Step Generation Pipeline**:
        1. **Image Filtering (Step 1)**:
           - **Objective**: Select semantically rich natural scene images
           - **Data Sources**: CC3M, ALLaVA, MultiUI, Geo170k, ChartQA and other multi-source data
           - **Quality Metrics**:
             - **IC9600 Metric**: Evaluates image semantic complexity (information content, category diversity, etc.)
             - **RAM Metric**: Identifies salient objects and scene elements in images
           - **Selection Criteria**: Prioritize natural scene images with rich semantic content (non-low-resolution, non-simple backgrounds)
           - **Rationale**: Rich semantic content supports designing more comprehensive and complex instruction following tasks
        2. **Task Generation (Step 2)**:
           - **For datasets with original QA (e.g., ALLaVA)**:
             - Use regular expressions and length limits to filter questions
             - Exclude questions containing few-shot examples (Q_fs)
             - Exclude questions containing options (Q_op)
             - Formula: Q_s = {q∈Q | q∉Q_fs ∧ q∉Q_op}
             - Obtain task instruction set T* suitable for constraint integration
           - **For datasets without original QA (e.g., CC3M)**:
             - Design predefined task instruction template pool P_T
             - Include multiple task types such as description, creation, analysis
             - Task design considers compatibility with subsequent constraint integration
        3. **Constraint Integration (Step 3 - Core Step)**:
           - **Constraint Pool P_C Construction**:
             - **6 major categories with 32 subcategories**, forming multi-level constraint taxonomy:
               a) **Format Constraints**: JSON format, list format, code block format, paragraph structure
               b) **Length Constraints**: Word limit, sentence limit, paragraph limit
               c) **Style Constraints**: Formal/informal tone, humorous style, poetic form, academic style
               d) **Keyword Constraints**: Must include specific words, avoid specific words, use synonyms
               e) **Composition Constraints**: Complex requirements combining multiple constraint types
               f) **Perception Constraints**: Constraints based on visual content (color, objects, position, etc.)
             - **Constraint-Visual Content Association**: Ensure constraints are related to image semantics, avoiding conflicts
           - **Constraint Sampling and Generation**:
             - Sample k constraint types from constraint pool P_C (typically 3-12)
             - **Two-Stage Selection Strategy** (for data with original QA):
               - First stage: Roughly select mostly compatible constraint types from P_C
               - Second stage: LLM precisely selects and generates specific constraint content
             - **Direct Sampling Strategy** (for data without original QA):
               - Directly sample k constraint types
               - LLM generates compatible specific constraint content
           - **Constraint Integration**:
             - LLM (GPT-4o) naturally integrates selected constraints into task instructions
             - Ensures mutual compatibility between constraints (no contradictions)
             - Outputs complex instructions containing multiple constraints
        4. **Answer Generation and Quality Control (Step 4)**:
           - **Answer Generation**: GPT-4o generates high-quality answers based on images and constraint instructions
           - **Quality Control**:
             - **Accuracy Threshold**: 80% (through GPT-4o self-evaluation)
             - **Constraint Verification**: Generated answers must satisfy all specified constraints
             - **Multi-round Iteration**: Samples not meeting quality requirements are discarded or regenerated
      - **Key Technical Advantages**:
        - **Complex Constraints**: Average 6.5 constraints per sample, far exceeding existing datasets (typically 1-2)
        - **Visual-Constraint Association**: Constraint design considers image content, ensuring instruction rationality and executability
        - **Automation**: End-to-end automated generation without human annotation
        - **Scalability**: Constraint pool can be flexibly expanded to support new constraint types
  - **MM-IFInstruct-23K Dataset**:
      - **Total Scale**: 23K high-quality instruction following data
      - **Data Source Distribution**:
        - CC3M: 16K (70%)
        - ALLaVA: 6K (26%)
        - MultiUI/Geo170k/ChartQA: 1K (4%)
      - **Constraint Statistics**:
        - **Average Constraints**: 6.5 per sample
        - **Constraint Distribution**: 3-12 constraints per sample, forming systematic complexity gradient
        - **Constraint Type Distribution**: 6 major categories with 32 subcategories, covering multi-dimensional instruction following requirements
      - **Data Characteristics**:
        - Contains complex constraints common in real application scenarios (e.g., "output in JSON format", "use at least 2 synonyms")
        - Diverse constraint combinations, training model's ability to satisfy multiple constraints simultaneously
  - **MM-IFDPO-23K Preference Dataset**:
      - **Objective**: For Direct Preference Optimization (DPO) training
      - **Construction Method**:
        - **Chosen Samples**: Directly use high-quality data from MM-IFInstruct-23K
        - **Rejected Samples**: 4 negative sample generation strategies
          1. Randomly delete 33% of constraints (retain 67%)
          2. Randomly delete 66% of constraints (retain 34%)
          3. Delete all constraints (retain 0%)
          4. Do not provide image input, generate answers based on text only
        - Use Qwen2-VL-7B-Instruct to generate rejected answers
      - **Scale**: 23K (chosen, rejected) pairs
      - **Effect**: DPO training further improves instruction following precision
  - **MM-IFEval Evaluation Benchmark**:
      - **Scale**: 400 high-quality evaluation samples
      - **Constraint Classification**: 6 major categories with 32 subcategories, forming complete instruction following evaluation system
      - **Question Types**:
        - **Compose-Level**: Text constraint-focused (300 samples)
        - **Perception-Level**: Requires strong visual perception ability constraints (100 samples)
          - Includes multiple image types such as natural scenes, user interfaces, charts, mathematical expressions
      - **Hybrid Evaluation Method** (Innovation):
        1. **Rule-Based Evaluation**: For precise constraints (e.g., word count, format)
           - Design predefined functions to verify if output satisfies constraints
           - LLM extracts relevant parameters, function executes verification
        2. **LLM Direct Judgment**: For clearly verifiable constraints (e.g., keyword inclusion)
        3. **Comparative Judgment**: For subjective constraints (e.g., tone, style)
           - Generate unconstrained control output
           - LLM compares both outputs to judge which better conforms to constraints
        - **Advantage**: Avoids LLM-as-a-judge misjudgment on precise constraints, improving evaluation accuracy
  - **Experimental Results** - **Open-Source Models Show Significant Improvements After Fine-tuning, Maintain VQA Capabilities**:
      - **Performance on MM-IFEval**:
        - Qwen2-VL-7B Baseline: 42.0% (Compose) / 80.5% (Overall)
        - +MM-IFInstruct-23K: 52.3% (+10.3%)
        - +MM-IFDPO-23K: **52.2%** (+10.2%)
        - LLaVA-NeXT-Llama3-8B Baseline: 39.7%
        - +MM-IFDPO-23K: **49.3%** (+9.6%)
      - **Cross-Benchmark Generalization (MIA-Bench)**:
        - Qwen2-VL-7B: Baseline 80.5% → Finetuned **88.1%** (+7.6%)
        - LLaVA-NeXT-Llama3-8B: Baseline 83.3% → Finetuned **90.0%** (+6.7%)
      - **Text Instruction Following (IFEval)**:
        - Qwen2-VL-7B: Baseline 47.4% → Finetuned **59.7%** (+12.3%)
        - LLaVA-NeXT-Llama3-8B: Baseline 50.7% → Finetuned **69.1%** (+18.4%)
      - **VQA Capability Preservation** (Key Validation):
        - On 8 VQA benchmarks including MMMU, MMBench, MMStar, MMT-Bench, AI2D, OCRBench, MMVet, POPE
        - Fine-tuned model performance comparable to or slightly better than baseline
        - **Conclusion**: MM-IFDPO-23K training does not harm model's original visual understanding capabilities
      - **Commercial Model Comparison** (MM-IFEval):
        - GPT-4o: 64.6% (Compose) / 44.0% (Perception)
        - Claude-3.5-Sonnet: 67.5% (Compose) / 44.0% (Perception)
        - Finetuned Qwen2-VL-7B: 55.2% (Compose) / 43.0% (Perception)
        - **Conclusion**: Open-source 7B models after fine-tuning approach commercial models on Compose-Level, but still have gaps on Perception-Level
  - **Ablation Study Key Findings**:
      - **DPO Negative Sample Strategy Comparison**:
        - Deleting 100% constraints (no constraints) negative samples work best
        - Deleting 33% or 66% constraints negative samples also effective
        - No image input negative samples slightly less effective
        - **Conclusion**: Clear positive-negative contrast (with constraints vs without constraints) most effective for DPO training
      - **Data Scale Impact**: 23K data volume achieves good performance-cost balance
      - **Constraint Quantity Impact**: Gradient distribution of 3-12 constraints helps model learn instruction following at different complexity levels
  - **Institution**: Fudan University, Shanghai AI Laboratory, Shanghai Jiao Tong University, The Chinese University of Hong Kong
  - **Authors**: Shengyuan Ding, Shenxi Wu, Xiangyu Zhao, Yuhang Zang, Haodong Duan, Xiaoyi Dong, Pan Zhang, Yuhang Cao, Dahua Lin, Jiaqi Wang
  - **Publication**: ICCV 2025
  - **Open Source**: ✅ [Code and Data](https://github.com/xxx/MM-IFEngine) (GitHub link TBD)
  - **Significance**:
      - **Problem Solving**: Systematically addresses scarcity of multimodal instruction following training data and imprecise evaluation methods
      - **Method Innovation**:
        - Proposes first constraint pool-driven multimodal instruction data automatic generation framework
        - Innovative hybrid evaluation method (rule + LLM + comparative), solving LLM-as-a-judge limitations
      - **Data Contribution**:
        - Provides 23K high-quality complex constraint instruction data (MM-IFInstruct-23K)
        - Provides 23K DPO preference data (MM-IFDPO-23K)
        - Provides 400-sample comprehensive evaluation benchmark (MM-IFEval)
      - **Practical Value**:
        - Significantly improves open-source models' instruction following ability, narrowing gap with commercial models
        - Does not harm original VQA capabilities, directly applicable to practical applications
        - Constraint pool is extensible, supporting customized instruction following capability cultivation
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2507.05970">📄 CIRHS</a></b><br>
<code>arXiv 2507.05970</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**: **组合图像检索的高质量三元组自动合成** - 为组合图像检索(CIR)任务自动生成大规模高质量三元组训练数据
  - **数据合成方法** - **LLM + T2I + MLLM三阶段Pipeline**:
      - **核心创新**: 首个利用生成模型自动构建高质量CIR三元组的完整pipeline，三元组包含参考图像、目标图像和相对描述
      - **三阶段生成Pipeline**:
        1. **多样化四元组生成（Stage 1）**:
           - **LLM**: Qwen2.5-32B
           - **指令模板**: 包含建议对象、编辑操作、图像风格三大要素
           - **输出**: 文本四元组 (C_Ir, C_It, C_r→t, C_t→r)
             - C_Ir: 参考图像描述
             - C_It: 目标图像描述
             - C_r→t: 从参考到目标的相对描述（修改描述）
             - C_t→r: 从目标到参考的逆向描述（支持双向三元组构建）
           - **多样性策略**:
             - 6套预定义指令集，LLM随机选择
             - 覆盖常见对象、编辑操作（对象替换、场景变换、数量变化、视角转换等）
             - 嵌入风格信息，支持多领域图像生成
        2. **一致图像对合成（Stage 2）**:
           - **关键洞察**: 独立生成两张图像会导致视觉差异不可控，但T2I模型擅长保持图像内一致性
           - **策略**: 将C_Ir和C_It合并为单个prompt，生成包含两个语义相关子图的图像
           - **T2I模型**: Flux.1-dev（使用方形网格布局模板）
           - **图像裁剪**: 将生成的图像分别裁剪为参考图像I_r和目标图像I_t
           - **优势**: 确保I_r和I_t共享至少一个语义实体，同时保持高度一致性
        3. **数据过滤（Stage 3）**:
           - **MLLM评分**: Qwen2.5-VL-32B
           - **三维评分标准**:
             a) **图像质量**: 评估生成图像的真实感和美学质量
             b) **图像-描述保真度**: 验证图像与描述的一致性
             c) **CIR任务对齐**: 确保三元组适合CIR任务（参考+修改→目标）
           - **过滤策略**: 计算加权总分，丢弃底部15%的三元组
           - **结果**: 从594K原始三元组过滤至534K高质量三元组
      - **编辑操作覆盖范围**:
        - **对象变换**: 替换、添加、删除对象
        - **场景变换**: 更改背景、环境
        - **数量变化**: 改变对象数量
        - **视角转换**: 不同角度、俯视/平视切换
        - **属性修改**: 颜色、大小、风格变化
      - **关键技术优势**:
        - **完全自动化**: 无需人工标注，端到端生成
        - **高质量图像**: 使用Flux.1-dev生成逼真图像
        - **语义一致性**: 通过合并prompt策略确保图像对一致性
        - **多样性**: LLM生成涵盖多种对象、编辑和风格的三元组
        - **可扩展性**: 可根据需求调整指令模板和过滤阈值
  - **CIRHS数据集**:
      - **规模**: 534K高质量三元组（过滤后）
      - **覆盖范围**: 多种真实场景和对象，多样化编辑操作
      - **格式**: (参考图像I_r, 相对描述C_r→t, 目标图像I_t)
      - **特点**: 光真实感图像、精确的编辑描述、高度的图像对一致性
  - **CoAlign模型**:
      - **架构**: 基于BLIP-2，冻结图像编码器 + 轻量级Q-Former
      - **双重对齐**:
        - **全局上下文对齐(GCA)**: 整体匹配组合查询与目标图像
        - **局部上下文推理(LCR)**: 细粒度匹配修改区域
      - **训练**: 在CIRHS数据集上端到端优化
  - **实验结果** - **在监督和零样本设置下均达到SOTA**:
      - **监督CIR（在CIRHS上训练）**:
        - **CIRR**: R@5 **83.81%**, R_s@1 **80.87%**, Avg **82.34%**（超越SPRC +1.69/+0.22/+0.95）
        - **FashionIQ**: Avg@10 **54.92%**, Avg@50 **75.55%**（超越SPRC +0.20/+0.58）
      - **零样本CIR（仅在CIRHS上预训练）**:
        - **CIRR**: R@1 **41.17%**, R@5 **71.68%**, Avg **71.17%**（超越所有零样本方法）
        - **FashionIQ**: Avg@10 **39.11%**, Avg@50 **60.29%**
        - **CIRCO**: mAP@5 **23.47%**, mAP@10 **25.29%**
      - **与其他合成数据集对比**（100K三元组）:
        - **CIRHS**: CIRR R@5 **71.18%**, FashionIQ Avg@10 **37.76%**
        - **ST18M (CompoDiff)**: CIRR R@5 60.00%, FashionIQ Avg@10 30.60%（CIRHS +11.18/+7.16）
        - **WebVid-CoVR**: CIRR R@5 67.28%, FashionIQ Avg@10 36.45%（CIRHS +3.90/+1.31）
        - **结论**: CIRHS显著优于现有合成数据集，甚至优于真实数据集WebVid-CoVR
  - **消融实验关键发现**:
      - **一致性生成 vs 独立生成**: 合并prompt生成（CIRR R@5 71.18%）显著优于独立生成（70.17%，+1.01%）
      - **数据过滤的必要性**: 过滤后CIRR R@5从70.65%提升至71.18%（+0.53%）
      - **全局+局部对齐**: 同时使用GCA和LCR比单独使用ITC提升2.25% R@5
      - **数据规模影响**: 性能随数据量增加而提升，534K达到最佳
  - **机构**: 北京邮电大学、商汤科技
  - **作者**: Haiwen Li, Delong Liu, Zhaohui Hou, Zhicheng Zhao, Fei Su
  - **发布时间**: arXiv 2025年7月（v3）
  - **意义**:
      - **自动化突破**: 首个完全自动化的高质量CIR三元组生成pipeline，无需人工标注
      - **质量超越**: 合成数据质量超越多个真实数据集和其他合成方法
      - **一致性保证**: 创新的合并prompt策略确保图像对语义一致性
      - **SOTA性能**: 在监督和零样本CIR任务上均达到最先进性能
      - **可扩展性**: 可快速生成大规模高质量CIR训练数据，降低数据标注成本
  

</details>
---

<details>
<summary>
<b><b><a href="https://aclanthology.org/2024.findings-emnlp.759/">📄 SMMQG</a></b><br>
<code>Paper</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Synthetic Multimodal Question Generation** - Generating style and modality-controllable evaluation datasets for Multimodal Retrieval Augmented Generation (MMRAG) systems
  - **Data Synthesis Method** - **Retriever + LLM + LMM Collaborative Generation Pipeline**:
      - **Core Innovation**: First framework for controllable synthetic multimodal QA data generation with fine-grained control over question styles and modalities, without human annotation
      - **Five-Step Generation Pipeline**:
        1. **Seed Source Sampling**:
           - Sample seed source s_seed from multimodal sources S (text passages, tables, images)
           - Use weighted sampling to avoid outliers: w_i based on semantic similarity to k-nearest neighbors (E5-Large embeddings)
           - Ensures thematic coherence of generated questions
        2. **Entity Extraction**:
           - Use GPT-4-Turbo to extract prominent entities from seed source (e.g., "tennis", "Japan", "machine learning")
           - For image sources, use image verbalization and image caption
           - High temperature (1.0) improves entity diversity, enhancing question diversity
        3. **Candidate Source Retrieval**:
           - Use extracted entity as query to retrieve candidate source set Z̃
           - Retrieve appropriate number of sources per modality based on modality requirements M (e.g., M=[1,2,0] means 1 text + 2 tables)
           - Text/tables use E5-Large, images use image verbalization for text-based retrieval
        4. **Question Generation**:
           - **Input**: Candidate sources Z̃, question style description v, modality requirements M, 3 style-specific few-shot examples
           - **Model**: GPT-4-Turbo (text/tables) or GPT-4-Turbo with Vision (with images)
           - **Task**: Select question sources Z⊆Z̃, generate question q and answer a, output source references
           - **Prompt Design**: Explicitly require questions must be based on selected sources, follow style description, not answerable if any selected source is removed
        5. **Verification Step**:
           - Verify question adheres to specified style
           - Verify answer can be inferred from question sources
           - Use GPT-4-Turbo for binary Pass/Fail judgment
      - **Five Question Styles**:
        1. **Information Extraction**: Extract and return information from single source
        2. **Compare Contrast**: Compare two closely related entities or topics
        3. **Numerical**: Numerical calculations based on numbers from sources
        4. **Compound**: Two loosely connected information extraction questions separated by "and"
        5. **Multi-hop**: Requires resolving implicit sub-question first, then resolving full question
      - **Multi-hop Question Special Generation**:
        - First generate two intermediate questions: question 1 about entity, question 2 with entity as answer
        - Use LLM to combine intermediate questions and answers into multi-hop question
        - Cross-modal multi-hop: split candidate sources by modality; unimodal multi-hop: random split
      - **Modality Support**: Text, tables, images and all pairwise combinations (9 modality combinations)
      - **Image Processing Strategy**:
        - **Image Verbalization**: Use LLaVA-13B to generate image descriptions, enabling text-based models to retrieve and reason over images
        - **Triplet Representation**: Image source = (image itself, image caption, image verbalization)
      - **Key Technical Advantages**:
        - **Style Control**: Precise control over question types through style description v and few-shot examples
        - **Modality Control**: Precise control over source type combinations through modality requirements M
        - **No Human Annotation**: Fully automated generation without crowdsourcing
        - **Scalability**: Applicable to any multimodal document collection
        - **Domain Customization**: Achieve domain-specific data generation by controlling source documents
  - **Data Scale**:
      - **Wikipedia QA Dataset**: 1024 QA pairs, 5 styles, 9 modality combinations
      - **Biology Dataset**: Additional college biology textbook dataset (demonstrates domain customization capability)
  - **Human Study Results** - **Quality On Par with Crowdsourced Benchmark MMQA**:
      - **Question Fluency (1-5 scale)**: SMMQG **4.53** vs MMQA 3.68 (+0.85, p<0.001*)
      - **Style Faithfulness (%)**: SMMQG **98.3%** vs MMQA 96.7% (+1.6%)
      - **Source Relevance (%)**: SMMQG **93.0%** vs MMQA 85.8% (+7.2%)
      - **Answerability (%)**: SMMQG **94.7%** vs MMQA 85.8% (+8.9%, p=0.02*)
      - **Answer Correctness (%)**: SMMQG **92.7%** vs MMQA 80.0% (+12.7%, p=0.001*)
  - **Model Evaluation Experiments** - **Reveals Style and Modality-Specific Performance Insights**:
      - **Retriever Evaluation** (Recall@5):
        - **E5-Large**: Best performance across all modalities (pure text 98.8%, text-text 91.5%)
        - **OpenCLIP**: Best for pure image retrieval (84.0%)
        - **BM25**: Poor performance on non-text modalities
      - **QA Model Evaluation** (GPT-4-Turbo-judge scores):
        - **GPT-4-Turbo**: Overall leader (info extraction 99.3%, multi-hop 96.2%)
        - **Claude-3-Opus**: Second best (info extraction 96.1%, multi-hop 88.7%)
        - **Open-source models**: Vicuna-13b+LLaVA-13b performs best among open-source
      - **Style-Specific Insights**:
        - All models struggle with **compare contrast** and **numerical** tasks
        - **Multi-hop reasoning** challenging for most models
        - **Information extraction** relatively easy, most models perform well
      - **Modality-Specific Insights**:
        - Pure text tasks show best performance
        - **Table QA** challenging for all models
        - Gemini Pro 1.0 excels at image reasoning (pure image 97.0%)
  - **Dataset Concordance Validation** (Kendall's tau):
      - **Retrieval**: τ=0.87 (p=0.02*) - Strong concordance between SMMQG and MMQA
      - **QA**: τ=0.86 (p=0.002*) - SMMQG can replace MMQA for model selection
      - **Conclusion**: SMMQG dataset can be used in place of MMQA for model evaluation and selection
  - **Key Findings**:
      - **Evaluation Data Quality**: SMMQG-generated synthetic data quality comparable to human crowdsourced data (sometimes even superior)
      - **Style Sensitivity**: MMRAG performance highly dependent on question style, requiring style-specific evaluation data
      - **Modality Sensitivity**: Both retrieval and QA performance significantly depend on input modality combinations
      - **Automated Evaluation**: Enables large-scale, customized MMRAG system evaluation
  - **Institution**: C3 AI, Connectly AI, Carnegie Mellon University
  - **Authors**: Ian Wu, Sravan Jayanthi, Vijay Viswanathan, Simon Rosenberg, Sina Pakazad, Tongshuang Wu, Graham Neubig
  - **Publication**: EMNLP 2024 Findings
  - **Paper Link**: [ACL Anthology](https://aclanthology.org/2024.findings-emnlp.759/)
  - **Significance**:
      - **Evaluation Data Generation**: First controllable synthetic multimodal QA data generation framework, addressing evaluation data scarcity
      - **Quality Validation**: Human study proves synthetic data quality reaches crowdsourcing level
      - **Performance Insights**: Reveals model strengths and weaknesses on specific styles and modalities, unobtainable through mixed benchmarks
      - **Scalability**: Fully automated process enables rapid customized evaluation data generation for new domains or requirements
      - **Cost Efficiency**: No expensive human annotation required, reducing evaluation dataset construction costs
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2311.10774">📄 MMC</a></b><br>
<code>arXiv 2311.10774</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-腾讯AI实验室-red?style=flat-square"/>
</summary>

  - **聚焦**: **大规模图表理解指令调优** - 为图表图像理解任务创建大规模多任务指令数据集，显著提升LMM在图表理解上的能力
  - **数据合成方法** - **GPT-4驱动的多任务图表指令生成Pipeline**:
      - **核心创新**: 首个大规模（60万）多任务图表理解指令数据集，涵盖9种不同任务类型，通过GPT-4生成高质量指令-答案对
      - **问题识别**:
        - 现有开源LMM在图表理解上表现不佳，因为图表图像与自然场景图像差异巨大
        - 现有图表QA数据集规模小、任务单一、依赖模板生成或固定词汇表答案
        - 缺乏全面的图表理解评估基准
      - **四阶段数据构建Pipeline**:
        1. **图表-文本对齐数据收集（210K）**:
           - **数据来源**: 收集210K图表-标题对用于视觉-文本对齐训练
           - **来源**: 现有公开数据集（FigureQA、DVQA、PlotQA、ChartQA、SciGraphQA等）
           - **格式转换**: 将不同数据集的标注统一转换为标准格式
           - **目的**: 帮助模型学习图表的基本视觉-语言对齐
        2. **图表信息提取与推理任务生成**:
           - **图像来源**: ChartQA和Statista.com的高质量图表
           - **GPT-4生成**: 基于图表描述（标题、坐标轴、数据范围等），使用GPT-4生成多样化问题-答案对
           - **任务类型**:
             - **图表信息提取**: 提取标题、坐标值、范围、数据模式等详细信息
             - **图表推理**: 关于趋势、数据模式和洞察分析的推理问题
           - **Prompt设计**: 要求生成3个不同问题，每个答案少于20字，确保多样性
           - **规模**: 330个信息提取样本，256个推理样本
        3. **科学图表理解任务生成**:
           - **数据来源**: arXiv科学论文中的图表
           - **多轮对话构建**: 使用GPT-4生成多轮图表相关对话
           - **任务类型**:
             - **上下文图表理解**: 理解图表在科学文献中的作用和意义
             - **多图表理解**: 理解同一文献中多个相关图表的关系
           - **质量控制**: 使用启发式规则删除非图表相关问题，确保问题聚焦于图表内容
           - **规模**: 56个上下文理解样本，52个多图表理解样本
        4. **结构化任务与分类任务生成**:
           - **图表转数据表/JSON**:
             - 使用VisText数据集的真实数据表
             - 转换为JSON格式（GPT-4辅助）
             - 任务: 将图表视觉信息转换为结构化数据格式
             - 规模: 400个数据表样本，96个JSON样本
           - **图表类型/主题分类**:
             - 网络爬取的多样化图表
             - 使用真实标签作为答案
             - 规模: 360个类型分类样本，536个主题分类样本
           - **股票图表分析**:
             - 使用Google Bard和来源文章生成分析问题
             - 规模: 40个样本
      - **人工质量控制**:
        - 过滤答案长度超过20字的样本
        - 删除提及"给定标题"、"现有描述"等不必要内容的样本
        - Chart-to-Json任务：删除未提及"title"作为key的样本
        - 随机抽样500个样本进行人工评估，确保质量
      - **关键技术优势**:
        - **多任务覆盖**: 9种不同任务类型，全面评估图表理解能力
        - **高质量生成**: GPT-4生成的指令-答案对自然流畅，符合人类认知
        - **开放式答案**: 平均答案长度23.7字，远超现有数据集的1-2字固定答案
        - **真实图表**: 使用真实网络图表和科学论文图表，非合成数据
        - **可扩展性**: Pipeline可应用于任何图表数据集
  - **MMC-Instruction数据集**:
      - **总规模**: 600K图表指令数据
      - **任务分布**（9种任务）:
        1. **图表信息提取**: 330个样本（提取标题、坐标、范围等）
        2. **图表推理**: 256个样本（趋势分析、数据模式识别）
        3. **上下文图表理解**: 56个样本（科学文献中的图表作用）
        4. **多图表理解**: 52个样本（多图表关系理解）
        5. **图表类型分类**: 360个样本（识别条形图、折线图、饼图等）
        6. **图表主题分类**: 536个样本（识别业务、健康、旅游等主题）
        7. **图表转数据表**: 400个样本（将图表转换为表格格式）
        8. **图表转JSON**: 96个样本（将图表转换为JSON格式）
        9. **股票图表分析**: 40个样本（分析股票图表趋势）
      - **数据特点**:
        - **多样化图表类型**: 条形图、直方图、折线图、散点图、热图等
        - **丰富主题**: 商业、健康、生物、工程、体育、旅游等
        - **开放式答案**: 平均23.7字，自由形式回答
        - **图像来源**: Statista.com、arXiv、VisText、网络爬取
  - **MMC-Benchmark评估基准**:
      - **规模**: 2,126个高质量测试样本
      - **图像数量**: 1,063个唯一图像
      - **问题类型**:
        - **多选题(MQA)**: 1,275个问题
        - **自由回答**: 851个问题
      - **平均问题长度**: 15.6字
      - **评估方法**:
        1. **生成能力评估**: 使用GPT-4评估自由回答的准确性（0.90 Cohen's kappa人类一致性）
        2. **理解能力评估**: 使用多选题直接计算准确率，无需GPT-4
      - **数据来源**: Statista.com、arXiv科学论文、VisText、网络爬取
      - **人工验证**: 所有样本经过人工质量检查
  - **MMCA模型（MultiModal Chart Assistant）**:
      - **架构**:
        - 视觉编码器: ViT-L（0.3B参数）
        - 语言模型: Vicuna-7B（使用LoRA微调）
        - 视觉抽象器: 可学习的query tokens
      - **两阶段训练**:
        - **阶段1**: 图表-文本对齐（冻结LLM，训练视觉抽象器）
        - **阶段2**: 图表指令调优（LoRA微调LLM，在MMC-Instruction上训练3个epoch）
      - **训练设置**: Tesla V100 GPU
  - **实验结果** - **在图表理解任务上达到开源SOTA**:
      - **MMC-Benchmark表现**（生成能力评估，GPT-4评分）:
        - **MMCA**: 总体准确率**26%**，超越所有开源模型
        - **LLaVA-1.5**: 24%（第二名）
        - **MiniGPT-v2**: 21%
        - **mPLUG-Owl**: 20%
        - **GPT-4V**: **51%**（远超开源模型，但在Chart-to-Datatable和Chart-to-Json任务上仍有挑战）
      - **MMC-Benchmark表现**（理解能力评估，MQA准确率）:
        - **MMCA**: 总体准确率**56%**，超越所有开源模型
        - **LLaVA-1.5**: 51%
        - **图表转数据表**: MMCA **64%** vs 其他模型≤57%
        - **图表转JSON**: MMCA **59%** vs 其他模型≤51%
      - **现有基准表现**:
        - **ChartQA**: **57.4%**（超越LLaVA-1.5的51.4%）
        - **DocVQA**: **72.5%**（与LLaVA-1.5的72.8%相当）
        - **TextVQA**: **59.6%**（超越LLaVA-1.5的58.2%）
      - **消融实验**:
        - 不微调视觉编码器的MMCA性能显著下降（ChartQA: 54.2% vs 57.4%）
        - 证明微调视觉编码器对图表理解至关重要
  - **错误分析**（100个GPT-4V错误样本分析）:
      - **语言偏见（35%）**: 强大的语言先验知识误导模型，忽略视觉输入
      - **视觉感知错误（29.6%）**: 现有视觉编码器（CLIP）对图表理解能力较弱，因为CLIP主要训练于自然图像
      - **推理错误（18.9%）**: 复杂推理任务失败
      - **不遵循指令（16.5%）**: 大多数开源模型无法良好遵循人类指令
  - **机构**: University of Maryland College Park, Tencent AI Lab Bellevue
  - **作者**: Fuxiao Liu, Xiaoyang Wang, Wenlin Yao, Jianshu Chen, Kaiqiang Song, Sangwoo Cho, Yaser Yacoob, Dong Yu
  - **发布时间**: arXiv 2023年11月（v2）
  - **论文链接**: [arXiv:2311.10774](https://arxiv.org/abs/2311.10774)
  - **意义**:
      - **数据贡献**: 首个大规模（60万）多任务图表理解指令数据集，填补图表理解训练数据空白
      - **评估基准**: 提供全面的图表理解评估基准（MMC-Benchmark），涵盖9种任务类型
      - **开源模型提升**: 证明通过高质量指令数据，开源模型可显著提升图表理解能力
      - **错误洞察**: 系统化分析开源和闭源模型在图表理解上的错误类型，为未来改进指明方向
      - **可扩展性**: Pipeline可应用于其他领域特定的图像理解任务
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2411.19930">📄 AdaMLLM</a></b><br>
<code>arXiv 2411.19930</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-BIGAI-red?style=flat-square"/>
</summary>

  - **聚焦**: **领域自适应后训练数据合成** - 仅使用开源模型，为领域特定的图像-caption对生成多样化视觉指令任务，用于MLLM的领域适配
  - **数据合成方法** - **开源MLLM驱动的生成-过滤Pipeline**:
      - **核心创新**: 首个仅依赖开源模型的领域自适应指令合成方法，通过一致性过滤避免专家标注，合成数据效果超越规则方法和闭源模型
      - **问题识别**:
        - 领域特定MLLM训练数据稀缺，尤其是医学、食品、遥感等专业领域
        - 现有方法依赖人工规则或昂贵的闭源模型（GPT-4/GPT-4V）
        - 传统两阶段训练（图像-caption对齐 → 视觉指令微调）降低任务多样性
      - **两阶段数据构建Pipeline**:
        1. **视觉指令合成器微调（Stage A）**:
           - **种子数据构建**:
             - 汇聚现有多领域数据集，涵盖多种图像域和任务类型
             - 包含：对象识别、领域分类、步骤引导、文本检测OCR、任务导向识别等
             - 无需额外专家标注
           - **任务三元组格式**:
             - **指令（Instruction）**: 基于图像-caption对的任务描述
             - **信息性回复（Informative Response）**: 包含推理过程的详细回答
             - **精确回复（Precise Response）**: 简洁的最终答案
           - **微调策略**:
             - 基础模型：LLaVA-v1.6-Llama3-8B（或其他开源MLLM）
             - 输入：图像+caption → 输出：任务三元组
             - **模态平衡策略**: 将10%图像替换为空白，鼓励模型利用文本caption，避免过度依赖视觉输入
             - 仅在任务三元组相关的对话轮次上计算损失
        2. **目标领域任务合成（Stage B）**:
           - **任务生成**: 使用微调后的合成器为目标领域的图像-caption对生成任务三元组
           - **一致性过滤器（Consistency-Based Filter）**:
             - **核心思想**: 不直接验证回复准确性（需要专家知识），而是检查精确回复与信息性回复的一致性
             - **验证工具**: 使用Llama-3-8B评估两个回复是否一致
             - **判断标准**: Yes（一致）/ No（不一致）/ Open（开放式问题，允许多种解释）
             - **优势**: 显著降低专家标注需求，过滤后准确率从60-77%提升至75-84%
           - **质量保证**: 约30%的任务三元组通过过滤后保留
      - **单阶段后训练（创新训练策略）**:
        - **问题**: 传统两阶段训练（先图像-caption对齐，再视觉指令微调）会降低领域特定训练的任务多样性
        - **解决方案**: 合并为单阶段训练，每个样本包含两个任务：
          - **图像Captioning任务**: 使用原始caption作为ground-truth
          - **合成视觉指令任务**: 使用过滤后的任务三元组
        - **优势**: 在大多数情况下，单阶段训练优于两阶段训练
      - **关键技术优势**:
        - **无需闭源模型**: 仅使用开源MLLM，无需GPT-4/GPT-4V
        - **减少专家标注**: 一致性过滤器避免逐个任务的专家验证
        - **任务多样性**: 合成的指令类型丰富，涵盖12种主要任务类型
        - **领域知识利用**: 从图像-caption对中有效提取领域专业知识
        - **可扩展性**: Pipeline适用于任意领域和任意开源MLLM
  - **合成数据规模**（基于不同领域图像-caption源）:
      - **生物医学**:
        - PMCRaw: 150K指令-回复对（来自PMC-OA原始caption）
        - PMCRefined: 144K指令-回复对（来自LLAVA-Med精炼caption）
      - **食品领域**:
        - Recipe1M: 32K指令-回复对（来自Recipe1M数据集）
      - **遥感领域**:
        - Remote Sensing: 15K指令-回复对（来自多个遥感数据集）
  - **AdaMLLM模型**:
      - **支持的基础模型**: LLaVA-v1.6-8B、Qwen2-VL-2B、Llama-3.2-11B
      - **训练方式**: 单阶段后训练（图像captioning + 合成指令任务）
      - **训练时长**: 13小时（8×A100-80GB GPUs）
  - **实验结果** - **在所有领域均显著超越基线和专业模型**:
      - **生物医学领域**（AdaMLLM-8B from PMCRefined）:
        - **SLAKE**: 58.0% (Open) / 73.3% (Closed)，超越LLaVA-Med（43.4%/50.2%）和PubMedVision（50.0%/68.3%）
        - **PathVQA**: 22.9% (Open) / 78.6% (Closed)，超越所有基线
        - **VQA-RAD**: 59.8% (Open) / 81.3% (Closed)
        - **PMC-VQA**: 47.9%，超越LLaVA-Med（37.1%）
      - **食品领域**（AdaMLLM-8B）:
        - **Recipe1M**: 24.8 Rouge-L（vs. LLaVA-Chef 23.1）
        - **Nutrition5K**: 36.1 Recall（vs. LLaVA-Chef 29.1）
        - **Food101**: 65.3% Acc（vs. LLaVA-1.6 47.9%）
        - **FoodSeg**: 42.0 F1（vs. LLaVA-Chef 14.5）
      - **遥感领域**（AdaMLLM-8B）:
        - **CLRS**: 66.9% Acc（vs. LLaVA-1.6 54.3%）
        - **UCMerced**: 72.1% Acc（vs. LLaVA-1.6 64.9%）
        - **NWPU**: 47.1 Rouge-L（vs. LLaVA-1.6 26.1）
      - **跨模型泛化**: 在Qwen2-VL-2B和Llama-3.2-11B上同样有效
  - **合成数据质量对比** - **超越规则方法和闭源模型**:
      - **vs. 规则方法（Rule-Based）**:
        - 任务多样性：68.0 vs. 52.5（+29.6%）
        - 领域知识利用：95.0 vs. 72.5（+31.0%）
        - 任务复杂度：77.9 vs. 43.8（+77.9%）
      - **vs. GPT-4（Text-only）**:
        - 任务多样性：81.0 vs. 75.2
        - 复杂度：80.0 vs. 75.3
      - **vs. GPT-4V（Vision+Text）**:
        - 任务多样性：85.5 vs. 83.2（相当）
        - 准确率（PMCRefined）：79.6 vs. 87.5（略低但可接受）
  - **消融研究关键发现**:
      - **一致性过滤器至关重要**: 去除后准确率从58.3%降至54.2%（生物医学）
      - **单阶段训练优于两阶段**: 在8B和11B模型上平均提升3-5%
      - **模态平衡策略有效**: 替换10%空白图像提升鲁棒性
      - **任务多样性重要**: 仅使用合成任务（无图像caption）性能显著下降
  - **任务类型分布**（合成数据覆盖12种主要任务）:
      - 任务导向图像识别（Task-Oriented Recognition）
      - 属性与上下文识别（Attribute and Context Recognition）
      - 对象识别（Object Recognition）
      - 数据表示与可视化（Data Representation）
      - 步骤引导（Step-by-Step Guidance）
      - 异常检测（Anomaly Detection）
      - 图像-文本匹配（Image-Text Matching）
      - Caption生成（Caption Generation）
      - 文本检测和OCR（Text Detection and OCR）
      - 场景分类（Scene Classification）
      - 领域分类（Domain Classification）
      - 姿态与活动识别（Pose and Activity Recognition）
  - **机构**: BIGAI, BUAA, THU, BIT, RUC
  - **作者**: Daixuan Cheng, Shaohan Huang, Ziyu Zhu, Xintong Zhang, Wayne Xin Zhao, Zhongzhi Luan, Bo Dai, Zhenliang Zhang
  - **发布时间**: arXiv 2024年11月（v4）
  - **论文链接**: [arXiv:2411.19930](https://arxiv.org/abs/2411.19930)
  - **开源**: ✅ [HuggingFace](https://huggingface.co/AdaptLLM)
  - **意义**:
      - **开源替代方案**: 证明开源模型可以替代昂贵的闭源模型（GPT-4V）进行领域适配数据合成
      - **一致性过滤创新**: 通过检查回复一致性而非直接验证准确性，避免大量专家标注
      - **单阶段训练**: 提出更高效的训练策略，保持任务多样性
      - **领域泛化**: 在生物医学、食品、遥感三个领域均取得SOTA，证明方法的通用性
      - **可复现性**: 完全开源模型、代码和数据，降低领域适配门槛
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2403.00231">📄 Multimodal ArXiv</a></b><br>
<code>arXiv 2403.00231</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-香港大学-red?style=flat-square"/>
</summary>

  - **聚焦**: **科学文献图像理解数据集** - 从ArXiv论文中提取大规模图像-caption对，并使用GPT-4V生成科学图表QA数据，提升MLLM的科学理解能力
  - **数据合成方法** - **GPT-4V驱动的科学图表QA生成Pipeline**:
      - **核心创新**: 首个大规模开放域科学图表理解数据集，覆盖多个科学领域，使用GPT-4V从图像生成多选题QA对
      - **问题识别**:
        - 现有MLLM在抽象图形（几何形状、科学图表）理解上能力有限
        - 科学领域训练数据稀缺
        - 现有科学图表数据集规模小、任务单一或仅限于计算机科学领域
      - **两阶段数据构建Pipeline**:
        1. **ArXivCap数据集构建（图像-Caption对）**:
           - **数据来源**: 2023年6月前的ArXiv论文源文件
           - **论文过滤**:
             - 从Semantic Scholar获取论文元信息
             - 仅保留已发表论文（Journal Article, Conference, Review）
             - 过滤低质量论文（确保数据集质量）
           - **图像-Caption提取**:
             - 从LaTeX源文件中提取图像和对应caption
             - **两种图像类型**:
               - **单图像对**: 一个图像配一个caption
               - **多图像对**: 多个子图像，每个有sub-caption，加上overall main caption
           - **Caption清洗**:
             - 删除caption少于5个词的chunk
             - 使用pylatexenc将LaTeX表达式转换为文本
             - 将LaTeX公式保留，引用转换为`<cit.>`，引用转换为`<ref>`
             - 确保caption质量和可读性
           - **规模**: 6.4M图像 + 3.9M captions（来自572K篇论文）
           - **领域覆盖**: 涵盖数学、物理、计算机科学、生物医学等多个科学领域
        2. **ArXivQA数据集构建（GPT-4V生成QA）**:
           - **数据源**: 从ArXivCap中选择高质量图像
           - **GPT-4V生成QA对**:
             - 输入：科学图像 + caption
             - 输出：多选题（问题、4个选项、正确答案、rationale）
             - Prompt设计：要求生成挑战性的、需要大学水平推理的问题
             - 任务多样性：涵盖图表理解、数据解读、科学推理等
           - **质量控制**:
             - 过滤无效样本（答案不在选项中、格式错误等）
             - 人工抽样验证（100样本，人类准确率80%）
             - 确保问题的可回答性和难度
           - **规模**: 32K QA对（来自16.6K图像）
           - **问题特点**:
             - 平均问题长度：16.98词
             - 平均每题4.20个选项
             - 每个选项平均7.59词
      - **关键技术优势**:
        - **大规模真实数据**: 使用真实科学论文图像，非合成数据
        - **开放域覆盖**: 涵盖多个科学领域，不限于单一学科
        - **高质量QA**: GPT-4V生成的问题具有挑战性和科学性
        - **多模态对齐**: 图像-caption对和QA对结合，增强多模态理解
  - **ArXivCap数据集**:
      - **总规模**: 6.4M图像 + 3.9M captions（572K论文）
      - **图像类型分布**:
        - 单图像对：约5.4M
        - 多图像对：约1M（包含sub-captions）
      - **Caption统计**:
        - 平均主caption长度：47.6词（中位数35词）
        - 平均sub-caption长度：4.8词（中位数3词）
        - Chunk caption（合并）平均长度：48.8词
      - **领域分布**: 数学、计算机科学、物理、天体物理、凝聚态物质、统计学等
  - **ArXivQA数据集**:
      - **总规模**: 32K多选题QA对
      - **图像数量**: 16.6K唯一图像
      - **问题类型**: 涵盖图表QA、几何问题求解、数学文字题、教科书QA、视觉QA等
      - **难度**: 需要大学水平推理能力
  - **实验结果** - **ArXivQA显著提升数学推理能力**:
      - **基线模型评估**（1000样本测试集）:
        - LLaVA-1.5-7B: 44.2%（第二名）
        - Qwen-VL-Chat: 46.6%
        - InstructBLIP-Vicuna7B: 7.0%
        - OpenFlamingo-9B: 9.9%
        - 人类表现：80.0%（100样本子集）
      - **MathVista提升**（微调Qwen-VL-Chat-7B）:
        - **总体准确率**: 50.4%（vs. 基线40.0%，+10.4%绝对提升）
        - **几何问题求解**: 34.0%（vs. 基线19.1%，+14.9%）
        - **教科书QA**: 70.0%（vs. 基线46.7%，+23.3%）
        - **视觉QA**: 64.1%（vs. 基线57.6%，+6.5%）
        - **超越商业模型**: 50.4% vs. Bard 50.0%
      - **ArXivCap单图像Captioning**（微调Qwen-VL-Chat-7B）:
        - BLEU-2: 8.9（vs. 基线4.4，+102%）
        - ROUGE-L: 15.8（vs. 基线11.1，+42%）
        - BERT-Score: 83.3（vs. 基线81.8）
        - 超越所有开源基线模型
      - **新任务基准**（在ArXivCap上定义）:
        - 多图像Captioning
        - 上下文化Captioning（in-context learning）
        - Title生成（从图像-caption对推断论文标题）
  - **领域特定性能分析**:
      - 不同科学领域的QA数据对不同任务的提升效果不同
      - 天体物理领域数据增强几何问题求解能力
      - 凝聚态物质领域数据提升数学文字题性能
      - 大多数领域数据对FigureQA任务有负面影响（表明合成FigureQA可能不是最佳基准）
  - **错误分析**（人工分析100个样本）:
      - **语言偏见**: 强语言先验误导模型（忽略视觉输入）
      - **视觉感知错误**: CLIP等视觉编码器对图表理解能力较弱
      - **推理错误**: 复杂推理任务失败
      - **不遵循指令**: 开源模型无法良好遵循指令
  - **机构**: The University of Hong Kong, Peking University
  - **作者**: Lei Li, Yuqi Wang, Runxin Xu, Peiyi Wang, Xiachong Feng, Lingpeng Kong, Qi Liu
  - **发布时间**: arXiv 2024年3月（v3）
  - **论文链接**: [arXiv:2403.00231](https://arxiv.org/abs/2403.00231)
  - **开源**: ✅ 数据集和代码
  - **意义**:
      - **数据规模**: 最大的真实论文图像-caption数据集（6.4M图像）
      - **开放域覆盖**: 首个覆盖多个科学领域的大规模QA数据集
      - **科学理解提升**: 显著提升MLLM在数学推理和科学图表理解上的能力
      - **评估基准**: 提供四个新任务基准，全面评估科学图表理解能力
      - **GPT-4V应用**: 证明GPT-4V可以有效生成高质量科学QA数据
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2412.07012">📄 PROVISION</a></b><br>
<code>arXiv 2412.07012</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**: **程序化扩展视觉中心指令数据** - 使用场景图作为图像的符号表示和人工编写的程序，系统化合成视觉中心指令数据，确保数据生成过程的可解释性和可控性
  - **数据合成方法** - **场景图驱动的程序化指令生成Pipeline**:
      - **核心创新**: 首个程序化方法使用场景图系统化生成视觉中心指令数据，通过人类编写的程序确保无幻觉和可扩展性
      - **增强场景图定义**:
        - **标准场景图**: 对象作为节点，属性分配给节点，对象间关系/交互作为有向边
        - **增强特性**: 添加深度标注（DepthAnyThing V2）和分割标注（SAM-2），形成增强场景图
        - **场景图来源**:
          - **手动标注**: Visual Genome数据集（人工标注场景图）
          - **自动生成**: DataComp数据集（使用场景图生成pipeline自动生成）
      - **程序化指令生成系统**:
        - **24个单图像指令生成器**: 将增强场景图转换为数千个高级感知问题-答案对
          - **六维指令类型**: 对象QA、属性QA、深度QA、分割QA、关系QA、对象+深度QA
          - **每个生成器使用数百个预定义模板**: 系统化整合标注生成多样化指令数据
          - **覆盖能力**: 比较、检索和推理基本视觉概念（对象、属性、关系）
        - **14个多图像指令生成器**: 处理多个场景图生成跨图像问题-答案对
          - **三类多图像任务**: 选择（Selection）、比较（Comparison）、聚合（Aggregation）
          - **示例**: "哪张图像包含更多红色对象？"、"这些图像中共同的对象是什么？"、"这些图像中红色对象的总数是多少？"
      - **场景图生成Pipeline**（用于无标注图像）:
        - **对象检测**: YOLO-world检测所有对象的边界框和标签
        - **图像分割**: SAM-2基于边界框生成像素级分割
        - **属性检测**: 微调LLaVA-1.5-13B作为属性检测模型（在LSA数据集上训练，精度90%）
        - **关系检测**: 微调Osprey模型检测对象对之间的关系
        - **深度估计**: DepthAnyThing V2生成像素级深度标注
        - **关键优势**: 可应用于任何图像，不限于有场景图标注的数据集
      - **关键技术优势**:
        - **可解释性**: 场景图+人类编写程序引入透明度和可解释性，消除端到端模型的不确定性
        - **无幻觉保证**: 只要场景图准确，程序生成的指令无幻觉，基于场景图中的显式信息而非LLM的概率输出
        - **可扩展性**: 从强大LLM转向程序化生成，实现可扩展和成本效益高的数据创建
        - **无许可约束**: 场景图和自定义程序不涉及专有模型输出，避免许可限制
        - **可控性**: 人类编写的程序允许精确控制和定制输出生成
      - **PROVISION-10M数据集**:
        - **总规模**: 超过1000万条唯一指令数据
        - **数据来源**:
          - **VG-S**: 150万单图像指令（Visual Genome，手动标注场景图）
          - **VG-M**: 420万多图像指令（Visual Genome）
          - **DC-S**: 230万单图像指令（DataComp，自动生成场景图）
          - **DC-M**: 420万多图像指令（DataComp）
        - **数据格式**: 每条指令同时提供多选题和简答题版本，确保灵活性
      - **实验结果**:
        - **单图像指令微调**（LLaVA-1.5-7B，VG-S数据）:
          - **CVBench 2D**: 58.0% → 65.0% (+7.0%，50% Half-Half格式）
          - **CVBench 3D**: 61.0% → 69.0% (+8.0%，50% Half-Half格式）
          - **QBench2**: 46.4% → 50.2% (+3.8%，50% Short Answer格式）
          - **RealWorldQA**: 54.2% → 58.2% (+4.0%，50% Multiple Choice格式）
          - **MMMU**: 36.2% → 39.1% (+2.9%，20% Half-Half格式）
          - **关键发现**:
            - 多选题格式在替换设置下表现更好（20%替换率最佳）
            - 简答题格式在增强设置下表现更好（50%增强率最佳）
            - Half-Half格式（混合格式）在多个设置下达到最佳性能
        - **多图像指令微调**（Mantis-SigLIP-8B，VG-M数据）:
          - **Mantis-Eval**: 54.4% → 62.7% (+8.3%，20% Replacement Short Answer格式）
          - **MMT**: 52.9% → 58.6% (+5.7%，20% Augmentation Half-Half格式）
          - **单图像基准**: 平均提升1.95%（SEED +0.5%，MMBench +0.1%，MME +2.0%等）
        - **预训练vs指令微调**（xGen-MM-4B）:
          - **仅预训练**: 平均提升+1.1%（DC-S）和+1.2%（VG-S）
          - **仅指令微调**: 平均提升+0.4%（DC-S）和+0.9%（VG-S）
          - **两者结合**: 平均提升+1.2%（DC-S）和+1.6%（VG-S），证明协同效应
          - **数据规模影响**: 预训练阶段从0.75M增加到1.5M样本，平均性能从59.1%提升到60.1%
        - **手动vs自动生成场景图对比**:
          - **单图像任务**: DC-S在较低数据规模下表现较差，但随着数据规模增加到50%，达到与VG-S相当的性能
          - **多图像任务**: DC-M表现始终低于VG-M，可能因为多图像设置下更大规模的生成场景图触发边缘效应
          - **结论**: 手动标注场景图通常更好，但自动生成场景图也能提升模型性能
      - **关键发现**:
        - **数据格式重要性**: 多选题和简答题格式在不同设置下表现不同，混合格式通常达到最佳性能
        - **数据规模影响**: 性能随数据规模增加而提升，但需要平衡数据质量和数量
        - **场景图质量**: 手动标注场景图通常优于自动生成，但自动生成场景图也能有效提升性能
        - **预训练+微调协同**: 在预训练和指令微调阶段都加入数据，比仅在单一阶段加入效果更好
      - **机构**: 华盛顿大学、Salesforce Research、南加州大学
      - **作者**: Jieyu Zhang, Le Xue, Linxin Song, Jun Wang, Weikai Huang, Manli Shu, An Yan, Zixian Ma, Juan Carlos Niebles, Silvio Savarese, Caiming Xiong, Zeyuan Chen, Ranjay Krishna, Ran Xu
      - **发布时间**: arXiv 2024年12月（v3）
      - **开源**: ✅ [代码](https://github.com/JieyuZ2/ProVision) | [数据集](https://huggingface.co/datasets/Salesforce/ProVision-10M)
      - **意义**:
        - **方法创新**: 首个程序化方法使用场景图系统化生成视觉中心指令数据，提供可解释和可控的数据生成过程
        - **可扩展性**: 通过场景图生成pipeline，可应用于任何图像，实现大规模数据生成
        - **数据贡献**: 提供超过1000万条高质量视觉中心指令数据（PROVISION-10M）
        - **实用价值**: 在多个基准上显著提升模型性能，证明程序化数据生成的有效性
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2502.14044">📄 Self-Synthesized Data</a></b><br>
<code>arXiv 2502.14044</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-ICLR_2025-red?style=flat-square"/>
</summary>

  - **聚焦**: **使用自合成数据增强多模态基础模型的认知和可解释性** - 通过视觉拒绝采样框架改进LMM的细粒度视觉推理能力，使其能够识别领域特定目标并提供可验证的解释
  - **数据合成方法** - **信息瓶颈概念选择 + 无奖励模型拒绝采样**:
      - **核心创新**: 首个使用信息瓶颈原理选择图像级视觉概念的方法，通过迭代的拒绝采样和微调过程，无需图像特定标注即可生成可解释的答案
      - **问题识别**: LMM在细粒度视觉分类任务上表现不佳（如LLaVA-1.5在Stanford Dogs上仅12.2%），无法利用关键视觉特征进行推理，无法提供可验证的解释
      - **两阶段自合成框架**:
        1. **图像级视觉概念选择阶段**:
           - **目标**: 从专家定义的概念集合Z中选择与图像X最相关的子集Z*
           - **信息瓶颈原理**: 最大化I(X;Z*)同时最小化I(Z*;Z)，平衡相关性和冗余性
           - **图像描述近似**:
             - 使用基础LLaVA-1.5生成多个图像描述D = {d₁, d₂, ..., dₙ}
             - **理论保证**: 当n→∞时，I(D;Z)收敛到I(X;Z)（Theorem 1）
             - 通过增加描述数量n，近似真实图像内容分布
           - **InfoNCE评分**: 对每个概念zⱼ计算InfoNCE分数sⱼ，衡量概念与图像描述的相关性
           - **概念选择标准**: Z* = {zⱼ ∈ Z | sⱼ > μ + β̂σ}，其中μ和σ是InfoNCE分数的均值和标准差
           - **可解释答案生成**: 使用选定的概念Z*提示基础LMM生成可解释的答案
        2. **无奖励模型拒绝采样阶段**:
           - **目标**: 从微调后模型生成的多个答案候选中选择最佳答案
           - **拒绝采样过程**:
             - 使用微调后的模型f_θ^T为每个图像生成m个答案候选Y = {y₁, y₂, ..., yₘ}
             - 对每个答案yᵢ计算与选定概念Z*的InfoNCE分数s'ᵢ
             - 选择分数最高的答案: y* = argmax s'ᵢ
           - **额外约束**: 选定的答案必须包含正确的标签c，否则丢弃
           - **关键优势**: 无需单独的奖励模型，使用概念对齐作为质量指标
      - **迭代微调过程**:
        - **初始微调**: 使用第一阶段生成的可解释答案进行初始微调
        - **迭代改进**:
          - Round 1: 使用初始微调模型生成新答案，通过拒绝采样选择最佳答案
          - Round 2-N: 重复上述过程，逐步提升模型性能
          - 最多进行4轮迭代
      - **关键技术优势**:
        - **无需图像特定标注**: 仅需要图像和类别标签，不需要详细的图像特定特征标注
        - **信息理论基础**: 基于信息瓶颈原理，提供理论保证
        - **无奖励模型**: 不需要训练或使用外部奖励模型，使用概念对齐作为质量指标
        - **可解释性**: 生成的答案包含人类可验证的视觉特征，提供可解释的解释
        - **领域适应性**: 可应用于各种领域（细粒度分类、医学图像等）
      - **实验结果**:
        - **细粒度分类数据集**:
          - **CUB-200**: 2.69% → 85.02% (+82.33%，4轮迭代）
          - **Stanford Dogs**: 12.2% → 86.91% (+74.71%，4轮迭代）
          - **FGVC-Aircraft**: 3.00% → 91.99% (+88.99%，4轮迭代）
          - **PLD**: 0.00% → 97.16% (+97.16%，4轮迭代）
        - **医学数据集**:
          - **HAM10000**: 1.62% → 85.06% (+83.44%，4轮迭代）
          - **Chest X-Ray**: 62.50% → 98.72% (+36.22%，4轮迭代，使用LLaVA-Med）
        - **解释质量评估**:
          - **解释存在性（EE）**: 1.00（所有数据集），表明始终生成解释
          - **认知分数（CS）**: 0.79-0.87（所有数据集），表明解释与专家知识对齐良好
          - **流畅度分数（FS）**: 6.53-9.01，表明解释自然流畅
        - **vs基线方法**:
          - **Naive Label (NL)**: 仅使用标签训练，无法生成解释（EE=0.00），准确率通常低于我们的方法
          - **Label + General Explanations (L+GE)**: 使用标签和通用解释，但解释质量较低（CS较低），在某些数据集上表现较差（如HAM10000仅8.45%）
        - **概念选择精度**:
          - 使用25个描述时，概念选择精度达到72.89%
          - 优于GPT-4o（63.95%）、LLaVA（~55%）和CLIP（~55%）
        - **过滤策略有效性**:
          - 无过滤: 准确率70.45%（CUB-200），CS 0.71
          - 有过滤: 准确率85.02%（CUB-200），CS 0.82
          - 证明拒绝采样过滤的重要性
      - **关键发现**:
        - **迭代改进**: 随着迭代轮数增加，准确率和解释质量持续提升
        - **概念选择重要性**: 图像级概念选择比使用所有标签级特征更有效
        - **拒绝采样有效性**: 过滤策略显著提升模型性能和解释质量
        - **避免捷径学习**: 使用图像特定特征而非仅标签，避免模型学习虚假关联
        - **跨数据集泛化**: 在CUB-200上训练的模型在Stanford Dogs上仅提升4.4%，表明领域特定微调的重要性
      - **机构**: 佐治亚大学、麻省总医院、哈佛医学院
      - **作者**: Yucheng Shi, Quanzheng Li, Jin Sun, Xiang Li, Ninghao Liu
      - **发布时间**: ICLR 2025 | arXiv 2025年2月（v2）
      - **开源**: ✅ [代码](https://github.com/sycny/SelfSynthX)
      - **意义**:
        - **方法创新**: 首个使用信息瓶颈原理选择图像级视觉概念的方法，无需图像特定标注
        - **可解释性增强**: 生成的答案包含人类可验证的视觉特征，提供可解释的解释
        - **实用价值**: 在多个细粒度分类和医学数据集上显著提升准确率和解释质量
        - **理论贡献**: 提供信息理论分析，证明方法的有效性
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2405.19716">📄 STIC (Self-Training on Image Comprehension)</a></b><br>
<code>arXiv 2405.19716</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-NeurIPS_2024-red?style=flat-square"/>
</summary>

  - **聚焦**: **大规模视觉语言模型的图像理解自训练** - 通过两阶段自训练方法增强LVLM的图像理解能力，使用未标注图像自构建偏好数据集，无需依赖GPT-4V或人工标注
  - **数据合成方法** - **两阶段图像理解自训练框架**:
      - **核心创新**: 首个专门针对图像理解的自训练方法，通过自构建图像描述偏好数据集和描述注入微调，显著提升LVLM的视觉感知和推理能力
      - **问题识别**: LVLM需要高质量视觉-语言数据进行微调，但获取成本高昂，且现有方法依赖GPT-4V生成数据，成本仍然较高
      - **STIC两阶段框架**:
        - **阶段1: 图像理解自训练**:
          - **自构建偏好数据集**: 使用基础LVLM（如LLaVA-v1.6）为未标注图像生成偏好数据对
            - **偏好响应**: 通过精心设计的逐步提示生成详细图像描述（如"请详细描述图像，关注以下方面：识别主要主体..."）
            - **非偏好响应**: 通过两种方式生成
              - **方式1**: 使用"坏提示"（如"描述图像中可能存在的想象对象"）引导模型产生幻觉描述
              - **方式2**: 使用正常提示但输入损坏图像（颜色抖动或降低分辨率）
          - **DPO对齐微调**: 使用Direct Preference Optimization (DPO)损失，添加正则化项强调偏好响应
            - **损失函数**: L(θ,θ_ref) = E[ℓ(λlog(p_θ(y_w|x)/p_θ_ref(y_w|x)) - λlog(p_θ(y_l|x)/p_θ_ref(y_l|x))) - αlog p_θ(y_w|x)]
            - **正则化项**: -αlog p_θ(y_w|x)进一步强调偏好响应，提升模型区分高质量和低质量响应的能力
          - **提示设计**:
            - **好提示**: 使用GPT-4生成多个初始提示，通过人工过滤和MSCOCO样本测试进行精炼
            - **坏提示**: 从GPT-4生成的提示中采样，设计用于引发不准确描述（描述可能逻辑存在的对象）
        - **阶段2: 描述注入微调**:
          - **目标**: 进一步微调自训练的LVLM，使其能够利用自生成的图像描述进行指令跟随任务
          - **数据构建**:
            - 从模型已使用的指令微调数据集中随机选择小部分数据（5K样本）
            - 为每个图像生成模型描述（使用简单提示如"解释图像中描绘的内容"）
            - 将生成的描述注入到原始指令中：`Image description: {model description} <original instruction>`
            - 保持原始ground-truth完成不变
          - **微调**: 在描述注入的数据集上进行一个epoch的微调
        - **可选: 描述并响应（DaR）**:
          - 在推理时，可选地让模型先描述图像，然后将描述与原始问题连接，生成更明智的答案
          - **格式**: 先提示模型描述图像，然后将描述+原始问题作为新提示
      - **关键技术优势**:
        - **无需外部模型**: 不需要GPT-4V或其他外部模型，仅使用基础LVLM本身
        - **成本效益**: 使用GPT-4-turbo而非GPT-4V，显著降低成本
        - **可扩展性**: 可应用于大量未标注图像，实现大规模数据生成
        - **目标导向**: 偏好数据构建的目标导向性质确保生成数据质量
        - **迭代改进**: 改进的模型可以用于生成更好的数据集，实现持续改进
      - **实验结果**:
        - **主要结果**（LLaVA-v1.6-7B）:
          - **ScienceQA**: 68.9% → 75.3% (+6.4%)
          - **TextVQA**: 60.3% → 65.2% (+4.9%)
          - **ChartQA**: 36.4% → 41.5% (+5.1%)
          - **LLaVA-Bench**: 77.3% → 79.2% (+1.9%)
          - **MMBench**: 63.7% → 67.8% (+4.1%)
          - **MM-Vet**: 42.2% → 45.0% (+2.8%)
          - **MathVista**: 34.6% → 37.0% (+2.4%)
          - **平均提升**: +4.0%
        - **LLaVA-v1.5-7B对比**:
          - **ScienceQA**: 66.8% → 69.5% (+2.7%)
          - **TextVQA**: 58.2% → 61.4% (+3.2%)
          - **ChartQA**: 6.3% → 6.6% (+0.3%)
          - **LLaVA-Bench**: 65.4% → 68.9% (+3.5%)
          - **MMBench**: 64.3% → 65.3% (+1.0%)
          - **MM-Vet**: 31.1% → 32.6% (+1.5%)
          - **MathVista**: 25.1% → 27.2% (+2.1%)
          - **平均提升**: +1.7%
        - **消融研究**:
          - **描述并响应（DaR）有效性**:
            - **仅DaR（无微调）**: 平均下降2.3%（某些数据集改进，某些下降）
            - **STIC + DaR**: 平均提升1.1%，ScienceQA提升2.8%
            - **结论**: DaR与微调过程有协同效应
          - **阶段进展**:
            - **Base**: 68.9%（ScienceQA）
            - **Stage 1**: 72.5% (+3.6%）
            - **Stage 2**: 74.0% (+1.5%）
            - **Stage 2 + DaR**: 75.3% (+1.3%）
          - **非偏好样本的作用**:
            - **仅正样本SFT**: LLaVA-Bench 76.7%（vs Base 77.3%），下降0.6%
            - **STIC（偏好数据）**: LLaVA-Bench 79.2%，提升1.9%
            - **结论**: 负样本在偏好对齐中起关键作用
          - **扩展规律**:
            - **6K偏好数据**: LLaVA-Bench提升1.9%
            - **12K偏好数据**: LLaVA-Bench提升3.1%
            - **结论**: 性能随数据规模增加而提升，未达到平台期
          - **图像分布相关性**:
            - **ScienceQA**: 与MSCOCO分布重叠大，提升6.4%（最高）
            - **TextVQA**: 与MSCOCO分布重叠大，提升4.9%
            - **MathVista**: 与MSCOCO分布重叠小，提升2.4%（较低）
            - **ChartQA**: 与MSCOCO分布重叠小，但提升5.1%（改进的图像理解能力起基础作用）
        - **不同数据源实验**:
          - **MSCOCO**: 平均提升4.0%
          - **Vision Flan**: 平均提升4.3%（更广泛的图像类型）
          - **结论**: 使用更多样化的图像数据可以进一步提升性能
        - **可扩展性**（LLaVA-v1.6-13B）:
          - **LLaVA-Bench**: 84.5% → 85.6% (+1.1%)
          - **MM-Vet**: 48.9% → 50.5% (+1.6%)
          - **MMBench**: 70.6% → 72.3% (+1.7%)
          - **结论**: STIC在不同规模的模型上都有效
      - **关键发现**:
        - **自训练有效性**: 当前LVLM的图像理解能力使其能够生成有用的偏好数据，为可扩展数据生成提供基础
        - **两阶段协同**: 阶段1提升图像理解，阶段2提升基于理解的推理，两者结合效果最佳
        - **负样本重要性**: 非偏好样本在偏好对齐中起关键作用，仅使用正样本无法达到相同效果
        - **数据规模影响**: 性能随数据规模增加而提升，展示利用大量未标注图像的潜力
        - **图像分布相关性**: 训练图像与评估任务的分布重叠越大，性能提升越明显
      - **机构**: 加州大学洛杉矶分校、加州大学伯克利分校、斯坦福大学
      - **作者**: Yihe Deng, Pan Lu, Fan Yin, Ziniu Hu, Sheng Shen, Quanquan Gu, James Zou, Kai-Wei Chang, Wei Wang
      - **发布时间**: NeurIPS 2024 | arXiv 2024年5月
      - **开源**: ✅ [代码和数据](https://stic-lvlm.github.io/)
      - **意义**:
        - **方法创新**: 首个专门针对图像理解的自训练方法，通过自构建偏好数据集提升LVLM性能
        - **成本效益**: 使用70%更少的监督微调数据，实现平均4.0%的性能提升
        - **可扩展性**: 可应用于大量未标注图像，展示利用大规模未标注数据的潜力
        - **实用价值**: 在7个不同基准上一致且显著提升性能，证明方法的有效性
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2312.06731">📄 Genixer</a></b><br>
<code>arXiv 2312.06731</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**: **赋能多模态大语言模型作为强大的数据生成器** - 探索当前MLLM独立生成视觉指令调优数据的潜力，无需依赖GPT-4V
  - **数据合成方法** - **四阶段自动化数据生成Pipeline**:
      - **核心创新**: 首个系统性探索当前MLLM作为数据生成器能力的方法，证明MLLM可以独立生成高质量视觉指令数据，在某些复杂任务上甚至超越GPT-4V
      - **Genixer Pipeline（四个关键步骤）**:
        1. **指令数据收集**:
           - **任务选择**: 精心选择9个代表性VL任务，分为两大类
           - **通用任务**: Common VQA、Adversarial VQA、Multi-choice VQA、Multi-turn Dialogue
           - **定位任务**: REC (Referring Expression Comprehension)、REG (Referring Expression Generation)、PointQA、Q→CBoxA、Referential Dialogue
           - **数据来源**: VQAv2、GQA、Counting110K、POPE、A-OKVQA、LLaVA-Conv-58K、VG、RefCOCO、PointQALocal、Visual7W等
           - **总训练数据**: 约200万样本用于训练数据生成器
        2. **指令模板设计**:
           - **两级指令系统**: 实现任务无关和任务特定两种生成模式
           - **通用指令**: 58条手写指令模板，如"Please provide a clear and direct question and answer after examining the image"
           - **特定指令**: 明确指定任务类型，如"This is a Common VQA task"
           - **控制常数τ**: 训练时控制仅使用通用指令的样本比例（不同任务类型设置不同：0.2-0.5）
           - **推理灵活性**: 推理时可切换模式，添加或不添加特定指令
        3. **赋能MLLM**:
           - **两个数据生成器**:
             - **Genixer-L**: 基于LLaVA1.5训练，专注于通用任务数据生成
               - **训练任务**: Common VQA、Adv VQA、MC VQA、MD
               - **训练设置**: AdamW优化器，学习率1×10⁻⁵，批次大小128，训练1个epoch（约14小时）
             - **Genixer-S**: 基于Shikra训练，专注于定位任务数据生成
               - **两阶段训练**: 第一阶段聚焦REC和REG，第二阶段添加PointQA、Q→CBoxA、RD
               - **训练设置**: 第一阶段学习率3×10⁻⁵、批次128，第二阶段学习率1×10⁻⁵、批次64
           - **训练目标**: 自回归生成问题-答案对，公式为 max log p(Xₒ|X_G, X_S, X_I)
        4. **数据生成与过滤**:
           - **图像源**: 140万图像（558K来自LAION/CC3M/SBU混合，830K来自SBU）
           - **通用任务数据生成**:
             - **生成**: 使用Genixer-L在1.4M图像上生成1.4M原始VQA三元组
             - **Fuyu驱动过滤框架**:
               - **验证提示**: "Here is a question-answer pair. Is {Q:X_q \nA:X_a} true for this image?\nPlease answer this question with Yes or No.\n"
               - **概率计算**: 计算预测"Yes"的概率 P(Y_r|X_I, X_q, X_a)
               - **阈值过滤**: λ=0.7，保留高质量样本
               - **结果**: 从1.4M过滤至915K，命名为**Genixer-915K**
           - **定位任务数据生成**:
             - **生成**: 使用Genixer-S在1.4M图像上生成1.4M原始REC数据
             - **CLIP驱动过滤框架**:
               - **三步过滤**: (1) 格式验证（正则表达式提取坐标和文本）; (2) 边界框尺寸过滤（宽/高≥50）; (3) CLIP相似度过滤（OpenCLIP-L，阈值0.6）
               - **结果**: 从1.4M过滤至350K，命名为**Genixer-350K**
      - **关键技术优势**:
        - **无需GPT-4V**: 完全基于开源MLLM，消除高昂API成本
        - **复杂任务优势**: 在REC等复杂任务上生成质量超越GPT-4V（如图1所示）
        - **可控生成**: 两级指令系统实现灵活的任务控制
        - **自动过滤**: 双重过滤机制确保数据质量
      - **数据规模**:
        - **Genixer-915K**: 91.5万VQA类合成数据
          - **问题长度**: 显著长尾分布，比VQAv2包含更多长句
          - **词汇多样性**: 丰富的名词和动词分布
          - **质量验证**: Fuyu-8B评估显示82-88%准确率，平均概率0.82-0.87
        - **Genixer-350K**: 35万REC类合成数据
          - **表达式长度**: 平均6.67词（vs RefCOCOg的8.43）
          - **区域覆盖**: 44.8万对象，覆盖多样化场景
          - **质量验证**: CLIP相似度过滤确保文本-区域对齐
      - **实验结果**:
        - **通用任务评估**（LLaVA1.5 + Genixer-915K）:
          - **12个基准测试**: 在10个上获得提升
          - **显著改进**: VizWiz +3.8%、ScienceQA +2.9%、MME +37.7分
          - **其他提升**: VQAv2 +0.6%、GQA +1.1%、TextVQA +0.8%、POPE +1.4%
        - **定位任务评估**（Shikra + Genixer-350K）:
          - **8个REC数据集**: 在7个上获得提升
          - **平均提升**: +0.6%（非平凡提升）
          - **最佳表现**: RefCOCO test-A +0.53%、RefCOCO+ test-B +1.02%
        - **数据生成器性能**:
          - **Genixer-L**: 在6个基准上，零样本设置下部分任务提升（VQAv2 +1.2%、VizWiz +0.8%）
          - **混合训练**: 结合原始微调数据后，所有基准均显著提升（VQAv2 +1.7%、VizWiz +4.1%）
        - **消融研究**:
          - **数据规模效应**: 300K→610K→915K，性能持续提升
          - **过滤阈值**: λ=0.7优于0.5和0，证明质量>数量
        - **人工评估**:
          - **100个样本分析**: 7种问题类型分布（Action、Color、Counting、Object Type、Relative Position、Yes/No、Others）
          - **准确率**: held-in (COCO) 75-92%，held-out (Flickr30K) 65-100%
          - **用户偏好研究**: 13个有效调查显示，在REC任务上Genixer生成数据更受偏好（vs GPT-4V）
      - **关键发现**:
        - **MLLM作为数据生成器**: 当前MLLM可以独立生成高质量视觉指令数据，无需GPT-4V辅助
        - **复杂任务优势**: 在REC等复杂任务上，MLLM训练后生成质量超越GPT-4V
        - **性能提升**: 合成数据集显著增强MLLM在多个多模态基准上的性能，并帮助缓解模型幻觉
        - **成本效益**: 消除GPT-4V API成本，同时提供更灵活的生成控制
      - **机构**: 新加坡国立大学Show Lab、新加坡管理大学
      - **作者**: Henry Hengyuan Zhao, Pan Zhou, Mike Zheng Shou
      - **发布时间**: arXiv 2023年12月 (v6: 2024年)
      - **开源**: ✅ [代码、数据和模型](https://github.com/zhaohengyuan1/Genixer)
      - **重要意义**:
        - **范式创新**: 首次系统性证明MLLM可以作为独立数据生成器，无需依赖商业API
        - **成本降低**: 为大规模数据生成提供经济可行的替代方案
        - **质量保证**: 双重过滤机制确保合成数据质量
        - **任务覆盖**: 同时支持通用和定位任务，提供全面的数据生成解决方案
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2502.08468">📄 mmE5</a></b><br>
<code>arXiv 2502.08468</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**: **通过高质量合成数据改善多模态多语言嵌入** - 开发高质量合成数据生成框架，为多模态多语言嵌入提供覆盖多样化任务、模态组合和语言的数据
  - **数据合成方法** - **MLLM引导的单次多方面生成Pipeline**:
      - **核心创新**: 首个系统性方法，识别高质量合成多模态数据的三个关键标准（广泛范围、鲁棒跨模态对齐、高保真度），并实现覆盖93种语言和7种模态组合的综合生成框架
      - **三个质量标准框架**:
        1. **广泛范围**: 确保生成的数据覆盖多样化任务（分类、VQA、检索）和模态组合，适用于各种下游场景
        2. **鲁棒跨模态对齐**: 通过深度思考过程和综合解释使不同模态语义一致
        3. **高保真度**: 通过自评估和精炼机制在合成数据中保持现实细节
      - **单次生成过程**:
        - **视觉解释**: 从四个角度进行多方面分析（总体描述、对象级细节、上下文特征、任务特定头脑风暴）
        - **数据合成**: 基于全面视觉理解生成任务特定数据样本
        - **自评估**: 跨相关性、合理性、清晰度和多样性维度评估数据质量
        - **精炼**: 基于评估反馈产生修订版本以提高质量
      - **全面任务与模态覆盖**:
        - **3种任务**: 分类（类型/主题识别）、VQA（视觉问答）、检索（跨模态搜索）
        - **7种模态组合**: I→T, IT→T, T→IT, T→I, I→I, IT→I, IT→IT（全面覆盖 vs 先前工作的1-2种组合）
        - **93种语言**: 英语、阿拉伯语、西班牙语、中文、法语、德语、荷兰语、葡萄牙语、俄语、波兰语、日语、意大利语、印尼语、波斯语 + 75种低资源语言
      - **多方面视觉分析**:
        - **总体描述**: 包括主要对象、场景、显著特征的整体总结
        - **对象级细节**: 单个对象、属性（颜色、大小、位置）、关系
        - **上下文特征**: 场景环境、背景细节、光照、动作
        - **任务特定头脑风暴**: 分析图像如何与特定任务需求相关
      - **质量保证机制**:
        - **深度思考过程**: 全面的生成前分析确保鲁棒的跨模态对齐
        - **自评估指标**: 跨多个质量维度的自动化评估
        - **硬负样本挖掘**: 为对比学习生成具有挑战性的负样本
        - **多语言一致性**: 确保所有93种支持语言的质量保持
  - **技术实现**:
      - **基础图像**: 从LAION-400M采样以获得多样性和规模
      - **MLLM集成**: 使用LLaMA-3-Vision进行单次生成以避免信息损失
      - **训练策略**: 在多模态嵌入模型上进行LoRA微调（秩8）的对比学习
      - **语言分布**: 平衡覆盖，23%英语，其他语言平均分布
  - **数据规模**:
      - **总合成数据**: **56万高质量样本**跨所有任务和模态组合
      - **任务分布**: 分类（14万）、VQA（14万）、检索（28万）确保平衡覆盖
      - **多语言覆盖**: 全面支持93种语言包括低资源语言
      - **质量过滤**: 严格的自评估和精炼确保高合成数据保真度
  - **评估与结果**:
      - **MMEB基准**: 达到SOTA性能（69.8%平均），显著超越之前方法（VLM2Vec: 62.9%，MMRet: 64.1%）
      - **多语言性能**: 在XTD基准的所有7种语言上表现优异（95.3%平均 vs GME: 94.1%）
      - **零样本能力**: 仅使用合成数据表现强劲（58.6% vs 之前最佳44.0%在MMEB上）
      - **扩展效应**: 性能与数据大小呈线性对数关系，证明高合成数据质量
  - **关键技术贡献**:
      - **质量标准框架**: 首次系统性识别合成多模态数据质量的三个关键标准
      - **单次生成**: 通过全面的单次MLLM生成避免信息损失
      - **全面覆盖**: 在单个框架中跨任务、模态和语言的前所未有广度
      - **多语言卓越**: 展示跨多样化语言家族的优异多语言嵌入能力
  - **机构**: 中国人民大学、微软公司
  - **开源**: ✅ [代码、数据和模型](https://github.com/haon-chen/mmE5)
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2409.20424">📄 World to Code (W2C)</a></b><br>
<code>arXiv 2409.20424</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**: **通过自指导组合标注和过滤的多模态数据生成** - 通过VLM自指导生成视觉场景的结构化Python代码表示，减少对专家模型和人工标注的依赖
  - **数据合成方法** - **自指导组合Pipeline与代码格式化**:
      - **核心创新**: 首个使用VLM自身通过不同提示提取跨模态信息并通过一致性策略过滤生成输出的框架，将最终输出组织为Python代码格式以增强结构表示
      - **四阶段构建Pipeline**:
        1. **视觉概念提取**:
           - **全局标注生成**: 准确描述图像的简单句子
           - **详细标注生成**: 所有视觉概念的综合描述（≤120词）
           - **概念提取**: 使用NLTK从标注中提取名词短语，用WordNet后处理去重
           - **定位**: 使用Grounding DINO将视觉概念映射到边界框
        2. **自指导信息提取**:
           - **区域级标注**: 使用裁剪图像区域为每个检测到的视觉概念生成组合标注
           - **OCR信息提取**: 通过指导提示引导VLM提取文本信息（在复杂场景中优于传统OCR工具）
           - **提示模板**: 预定义通用模板确保更好的指令遵循性
        3. **自一致性信息过滤**:
           - **计数一致性过滤**: 通过VLM验证确认分组视觉概念的存在
           - **标注重新排序**: 使用VLM自评估对标注质量进行评分和排序
           - **基于规则过滤**: 使用结构化规则移除计数不一致的样本
        4. **结构化代码格式化**:
           - **Python类组织**: 将视觉信息结构化为带对象属性的Python类
           - **丰富标注**: 为每个视觉元素包含描述、边界框、OCR文本
           - **层次分组**: 分组相似概念（如elephant_group、people_group）以更好组织
      - **自一致性策略**:
        - **生成器-验证器方法**: VLM既作为生成器又作为验证器确保一致性
        - **多轮验证**: 对提取概念和描述的迭代验证
        - **评分机制**: 手动评分系统进行标注质量评估
      - **质量保证**:
        - **束搜索**: 鼓励VLM提供尽可能多的视觉概念
        - **概念验证**: 检查每个提取概念的存在性和计数准确性
        - **一致性评分**: 使用基于VLM的评分来排序和过滤高质量样本
  - **技术实现**:
      - **基础数据集**: ShareGPT4V图像（去重后）用于公平比较
      - **VLM集成**: 兼容LLaVA-1.5和LLaVA-NeXT架构
      - **处理工具**: NLTK用于概念提取，WordNet用于去重，Grounding DINO用于空间定位
      - **代码结构**: 带分组对象和详细属性的自然环境类
  - **数据规模**:
      - **生成样本**: 34K (LLaVA-1.5-7B), 33K (LLaVA-1.5-13B), 37K (LLaVA-NeXT-7B), 29K (LLaVA-NeXT-13B)
      - **处理时间**: 32个A100上1-1.5天（LLaVA-1.5），48个A100上2-3天（LLaVA-NeXT）
      - **一致性过滤**: 过滤阶段大量数据消除确保高质量
  - **评估与结果**:
      - **VQA基准**: 在7/9基准上表现优异（LLaVA-NeXT-7B），6/9基准（LLaVA-NeXT-13B）
      - **视觉定位**: 平均IoU提升1.5/1.6（LLaVA-1.5 7B/13B），3.5/1.3（LLaVA-NeXT 7B/13B）
      - **小样本学习**: GQA 2-shot评估5%准确率提升，展示改进的代码解析能力
      - **代码vs标注**: Python代码格式一致超越单轮/多轮对话格式
  - **关键技术贡献**:
      - **自给自足**: 通过VLM自指导消除对多个专家模型的需求
      - **代码表示**: 用于结构化多模态数据组织的新颖Python代码格式
      - **一致性过滤**: 无需人工标注的鲁棒自一致性质量保证策略
      - **可扩展性**: 全自动pipeline支持大规模结构化数据生成
  - **机构**: 中国科学院大学、字节跳动
  - **开源**: ✅ Pipeline代码和数据构建方法论
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2406.19593">📄 SK‑VQA</a></b><br>
<code>arXiv 2406.19593</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**：**面向多模态RAG/知识增强的“图像+上下文+问答”合成** — 通过GPT‑4为给定图像同时生成百科风格上下文与需依赖上下文推理的多组QA，构建200万+样本，用于训练/评估具“上下文增强生成”能力的MLLMs（KB‑VQA）
  - **数据合成方法**：
      - **上下文与QA的联合生成**：以图像为条件，GPT‑4单步产出相关的文章式上下文与问题‑答案对，避免“仅看图可答”的问题
      - **多源图像 + 两级过滤**：图像来自LAION、WIT（Wikipedia images）、COCO‑Counterfactuals；提供IR过滤（去除“这张图片中…”等直接引用图像的伪上下文）与CAP过滤（确保答案可在上下文中抽取）
  - **数据规模与多样性**：
      - 总计2,006,489个QA，覆盖290,266个图像‑上下文配对；>96%问题为唯一问题，词性/词汇/长度分布均显著丰富于既有KB‑VQA数据集
  - **实验发现**：
      - 作为基准更具挑战（多模型零样本在SK‑VQA上低于Enc‑VQA/ViQuAE）；作为训练数据可显著提升跨数据集泛化，相比InfoSeek/Enc‑VQA更稳健；在外部检索的RAG设置下仍具优势
  - **质量与控制**：
      - **图像不变‑文本增强**：围绕既有图像构建高质量“上下文+QA”；配IR/IR+CAP子集，减少样本量仍保持/提升效果，利于任务对齐调参
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2308.08428">📄 ALIP</a></b><br>
<code>arXiv 2308.08428</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-2023年8月-red?style=flat-square"/>
</summary>

  - **聚焦**: **自适应语言-图像预训练与合成标注** - 使用合成标注减少Web数据噪声，通过自适应权重机制优化对比学习
  - **数据合成方法** - **OFA模型生成合成标注 + 自适应权重门控机制**:
      - **核心创新**: 针对Web数据中图文不匹配问题，使用大型多模态模型生成高质量合成标注，并设计自适应权重系统动态平衡原始文本和合成标注的贡献
      - **问题识别**: Web爬取数据存在内在噪声和不匹配的图文对
        - **内容不匹配**: 原始文本过于抽象（如"Leisure Sunday"）与具体图像内容不符
        - **信息不足**: Web文本缺乏对图像内容的详细描述
        - **噪声影响**: 不匹配数据影响表征学习性能
      - **合成标注生成**:
        - **生成模型**: 使用**OFA (One For All)**模型生成合成标注
        - **引导提示**: "What does the image describe?" 引导生成图像内容描述
        - **质量优势**: 合成标注提供更准确、详细的图像内容描述
          - 示例: "A woman sitting on a step reading a book" vs "Leisure Sunday"
          - 包含具体对象信息（书、女人、台阶）和动作信息（坐着、阅读）
      - **双路径架构**:
        - **原始路径**: 处理图像-原始文本对 (x, t)
        - **合成路径**: 处理图像-合成标注对 (x, c)
        - **三元组输入**: (图像x, 原始文本t, 合成标注c) 作为完整训练单元
      - **自适应权重门控系统**:
        1. **语言一致性门 (LCG)**:
           - **功能**: 预测样本权重Ws，基于原始文本和合成标注的相似度
           - **计算**: Ws = sigmoid(MLP(|t-c|, t⊙c, t, c))，其中⊙表示元素乘法
           - **作用**: 识别高质量样本（文本标注一致）vs 低质量样本（文本标注不匹配）
        2. **描述一致性门 (DCG)**:
           - **功能**: 计算图像-文本对权重Wt和图像-标注对权重Wc
           - **基于历史相似度**: 使用历史平均相似度Hxt和Hxc作为阈值
           - **权重公式**:
             - Wt = exp((Sxt - Hxt) × γp) 当Ws < 1时
             - Wc = exp((Sxc - Hxc) × γp) 当Ws < 1时
           - **自适应调整**: 从低质量样本中挖掘高质量图文/图注对
      - **自适应对比损失**:
        - **传统InfoNCE局限**: 对所有训练样本均匀加权，忽视数据质量差异
        - **改进策略**: 集成样本权重Ws和对权重(Wt, Wc)到InfoNCE损失中
        - **损失函数**:
          - Lxt = -Σ WsWt × log(softmax(图像-文本相似度))
          - Lxc = -Σ WsWc × log(softmax(图像-标注相似度))
        - **动态调整**: 训练过程中权重根据数据质量动态变化
  - **数据规模**:
      - **基础数据集**: YFCC15M (1500万图像-文本对)
      - **合成标注**: 为每个图像生成一个高质量合成标注
      - **计算效率**: 合成标注可预计算存储，无需在线生成
  - **训练策略**:
      - **双编码器架构**: 遵循CLIP架构（图像编码器 + 文本编码器）
      - **联合优化**: 同时训练两个对比损失 Lxt + Lxc
      - **权重调度**: 使用历史相似度统计动态调整权重参数
      - **超参数**: γs=2（样本权重），γp=2（对权重），温度参数τ训练优化
  - **实验结果**:
      - **零样本图文检索**:
        - **Flickr30K**: Text→Image R@1达70.5%（vs CLIP 34.9%，+35.6%）
        - **MSCOCO**: Image→Text R@1达48.9%（vs CLIP 23.4%，+25.5%）
        - **显著提升**: 在所有检索指标上达到新的SOTA性能
      - **线性探测**:
        - **10个下游数据集**: 平均准确率72.2%（vs CLIP 63.0%，+9.2%）
        - **零样本分类**: 11个数据集平均准确率41.7%（vs CLIP 31.8%，+9.9%）
      - **大规模验证**: 在LAION-10M和LAION-30M上验证方法的鲁棒性和可扩展性
  - **消融研究发现**:
      - **权重组件贡献**: Ws、Wt、Wc各自贡献显著，组合使用效果最佳
      - **合成标注质量**: OFA生成的标注相比原始文本具有更高的图像-文本相似度和更紧凑的分布
      - **标注长度**: 合成标注token数量集中在10-15个，显著低于原始文本
      - **不同容量模型**: OFA-base和OFA-large生成标注效果相当
  - **关键发现**:
      - **合成标注优势**: 合成标注比原始Web文本更准确描述图像内容，但在零样本分类任务上原始文本仍有价值
      - **权重机制有效性**: 自适应权重系统能有效识别和利用高质量数据，抑制噪声数据影响
      - **计算效率**: 相比在线过滤方法，预计算合成标注更高效（避免训练时额外计算开销）
      - **数据利用最大化**: 通过自适应权重而非直接过滤，充分利用所有训练数据
  - **发布时间**: arXiv 2023年8月 | DeepGlint & Huawei UK R&D & InsightFace & University of Sydney
  - **开源**: ✅ 代码和模型权重 - 论文承诺开源发布
  - **重要意义**:
      - **Web数据噪声解决方案**: 提供了处理大规模Web数据噪声的有效框架
      - **合成标注范式**: 确立了使用多模态模型生成高质量标注的标准方法
      - **自适应学习**: 开创性地将自适应权重机制引入多模态对比学习
      - **实用性强**: 方法简单有效，易于在现有CLIP训练pipeline中集成
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2410.13523">📄 Medical VLP</a></b><br>
<code>arXiv 2410.13523</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-2024年10月-red?style=flat-square"/>
</summary>

  - **聚焦**: **医学视觉语言预训练能否使用纯合成数据成功** - 探索完全基于合成数据进行医学VLP的可行性，解决医学领域配对数据稀缺问题
  - **数据合成方法** - **实体驱动的合成报告生成 + 专用CXR图像生成**:
      - **核心创新**: 首次系统性验证纯合成数据在医学VLP中的有效性，提出自动化pipeline生成高质量、分布平衡的合成医学图文对
      - **问题识别**: MIMIC-CXR等真实医学数据集存在严重缺陷
        - **低质量图像**: 模糊、对比度差、伪影问题
        - **未配对样本**: 图像和文本不匹配
        - **长尾分布**: 医学实体分布严重不均，影响模型学习
        - **数据稀缺**: 高质量配对医学数据获取困难且成本高昂
      - **真实数据质量评估**:
        - **多模态过滤**: 使用InternVL2-26B设计6个查询评估CXR图像质量
        - **查询类型**: 正面视角检测、图像质量评估、伪影检测、对比度评估、清晰度检测、诊断适用性
        - **相似度过滤**: 使用RAD-DINO提取特征，过滤与低质量样本相似的图像
        - **结果**: 从MIMIC-CXR的213,384对中过滤出1,448个低质量样本
      - **实体分布分析**:
        - **NER提取**: 使用RaTE模型从报告中提取154,049个独特医学实体
        - **五大类别**: 异常(55,047)、非异常(36,365)、疾病(23,017)、非疾病(22,103)、解剖(40,517)
        - **长尾问题**: 所有类别都呈现严重的长尾分布，影响模型对罕见实体的学习
      - **合成报告生成**:
        - **实体采样策略**:
          - 从S1(异常+疾病，k=9)和S2(非异常+非疾病+解剖，m=3)中采样实体组合
          - 设置频次阈值τmax=15，确保实体分布平衡
          - 动态重采样避免高频实体过度表示
        - **LLM生成**: 使用Llama 3.1-70B生成基于采样实体的合成放射学报告
        - **结构化输出**: 生成包含FINDINGS和IMPRESSION两部分的完整报告
        - **质量控制**: 使用RaTE验证生成报告确实包含指定实体，不匹配则重新生成
      - **合成图像生成**:
        - **专用模型**: 使用RoentGen (临床专家验证的CXR专用T2I模型) 生成配对CXR图像
        - **条件生成**: 基于合成报告的IMPRESSION部分生成对应CXR图像
        - **质量保证**: 仅使用经临床专家验证的生成模型，确保医学准确性
      - **数据平衡策略**:
        - **分布控制**: 通过实体采样和频次限制主动平衡合成数据分布
        - **多样性保证**: 确保罕见疾病和常见疾病的合理表示
        - **配对保证**: 每个合成报告都有对应的合成图像，避免未配对问题
  - **数据规模**:
      - **SynCXR数据集**: 200,000个合成CXR图像-报告对
      - **无人工检查**: 完全自动化生成，无需人工质量检查
      - **实体覆盖**: 基于154,049个医学实体的平衡采样生成
  - **训练策略**:
      - **基线模型**: 使用ConVIRT和GLoRIA两个经典MedVLP方法
      - **训练设置**: 严格控制模型和训练配置，专注数据角度的影响评估
      - **对比实验**: 纯真实数据 vs 纯合成数据 vs 混合数据三种设置
  - **实验结果** - **纯合成数据显著优于真实数据**:
      - **零样本分类** (已见疾病):
        - **ConVIRT**: 平均AUC提升4.7%，F1提升4.53%
        - **GLoRIA**: 在所有5个数据集上持续优于真实数据训练
        - **混合数据**: AUC提升10.08%，F1提升7.62%
      - **零样本分类** (未见疾病):
        - 对未见疾病的泛化能力显著增强
        - Covid-19、PadChest未见/罕见疾病检测性能提升
      - **零样本定位**:
        - IoU平均提升1.42%，Dice分数提升0.97%
        - 混合数据进一步提升: IoU +4.06%，Dice +2.92%
      - **微调任务**:
        - 分类和分割任务上合成数据预训练模型持续优于真实数据
        - 证明合成数据不仅有利于跨模态学习，还提升单模态视觉理解
  - **消融研究发现**:
      - **实体平衡采样**: 使用更多实体类型(25%→75%)显著提升性能
      - **LLM选择**: Llama 3.1-70B优于其他LLM和医学专用LLM
      - **图像生成模型**: RoentGen(临床验证)显著优于通用T2I模型
      - **数据清洗价值**: 清洗后的MIMIC-CXR性能仍不如纯合成数据
  - **关键发现**:
      - **纯合成数据可行性**: 首次证明医学VLP可以完全基于合成数据成功训练
      - **合成优于真实**: 在多个任务上纯合成数据训练效果超越真实数据
      - **分布平衡重要性**: 平衡的实体分布比数据真实性更关键
      - **质量胜过数量**: 高质量合成数据比大规模噪声真实数据更有效
  - **发布时间**: arXiv 2024年10月 | Imperial College London & AstraZeneca & Ohio State University等
  - **开源**: ✅ SynCXR数据集(20万图文对) + 数据生成pipeline + 评估代码
  - **重要意义**:
      - **医学AI突破**: 为医学领域数据稀缺问题提供了革命性解决方案
      - **合成数据范式**: 证明合成数据可以完全替代真实数据进行医学VLP
      - **数据质量重新定义**: 揭示数据分布平衡和质量控制比数据真实性更重要
      - **临床应用前景**: 为快速构建医学AI系统、处理隐私敏感数据提供新路径
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2507.22431">📄 HQ-CLIP</a></b><br>
<code>arXiv 2507.22431</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-2025年7月-red?style=flat-square"/>
</summary>

  - **聚焦**: **利用大型视觉语言模型创建高质量图像文本数据集和CLIP模型** - 通过LVLM增强现有图像标注质量，构建大规模高质量图文数据集
  - **数据合成方法** - **成本高效的LVLM驱动数据精化pipeline + 多粒度文本生成**:
      - **核心创新**: 提出可扩展的LVLM驱动数据精化范式，通过少量GPT-4o样本微调开源LVLM，实现大规模高质量图文数据生成
      - **成本效率解决方案**:
        - **问题**: 直接使用GPT-4o、Gemini等顶级LVLM成本过高，不适合大规模数据处理
        - **解决方案**: 三步成本优化策略
          1. 使用GPT-4o精选10,000个高质量重标注样本作为种子数据
          2. 对轻量开源LVLM (Qwen2-VL-7B)进行监督微调(SFT)，使其在特定任务上对齐GPT-4o
          3. 部署微调后的轻量LVLM进行大规模数据处理
        - **效率验证**: SFT增强的Qwen2-VL-7B达到72B版本相当性能，计算资源需求仅为1/9
      - **多粒度文本合成策略**:
        - **四种互补文本类型**:
          1. **详细正描述 (d+)**: 长篇详细的图像内容描述，平均比原始标注长4倍
          2. **简短正标签 (t+)**: 从详细描述中提取的关键语义标签
          3. **详细负描述 (d-)**: 语义相似但内容不匹配的详细负面描述
          4. **简短负标签 (t-)**: 与图像内容不匹配的负面语义标签
        - **提示工程优化**:
          - 设计专门的提示模板指导LVLM生成高质量、结构化的多层次描述
          - 包含正面/负面描述生成和标签提取的完整workflow
        - **质量控制**: 通过多轮迭代和自动评估确保生成文本质量
      - **数据处理pipeline**:
        1. **原始数据收集**: 从DFN-Large等大规模数据集开始
        2. **LVLM增强**: 使用微调后的Qwen2-VL-7B为每张图像生成四种互补文本
        3. **质量筛选**: 基于图文相似度和生成质量进行筛选
        4. **最终整合**: 构建包含原始+增强文本的多粒度数据集
  - **HQ-CLIP训练框架**:
      - **硬负样本识别 (HNI)**:
        - 利用详细负描述和负标签进行细粒度理解训练
        - 增强模型对语义细微差别的敏感性
        - 损失函数: L_HNI = -log(exp(sim(x,t+)/τ) / (exp(sim(x,t+)/τ) + exp(sim(x,t-)/τ)))
      - **短标签分类 (STC)**:
        - 使用提取的语义标签进行分类训练
        - 提升模型的分类语义识别能力
        - 损失函数: L_STC基于标签分类交叉熵
      - **混合训练策略**:
        - 结合原始标注和增强文本进行训练
        - 最优混合比例: 75%增强文本 + 25%原始标注
        - 动态权重调整: α=0.2 (HNI权重), β=100 (STC权重)
  - **数据规模**:
      - **VLM-150M数据集**: 1.5亿高质量图像-文本对
      - **基础数据**: 基于DFN-Large (1.47B原始数据)筛选和增强
      - **文本增强**: 每张图像配备4种互补文本描述
      - **处理效率**: 使用微调LVLM相比GPT-4o成本降低90%+
  - **实验结果** - **三个数量级验证 (1M到150M)**:
      - **小规模 (1.4M)**:
        - ImageNet准确率: 8.7% (vs DFN 5.8%, +2.9%)
        - 平均38数据集性能: 20.0% (vs DFN 17.1%, +2.9%)
      - **中规模 (14.7M)**:
        - ImageNet准确率: 40.5% (vs DFN 37.6%, +2.9%)
        - 检索任务: 38.4% (vs DFN 28.6%, +9.8%)
        - 平均38数据集性能: 41.1% (vs DFN 36.8%, +4.3%)
      - **大规模 (147M)**:
        - ImageNet准确率: 70.6% (vs DFN 68.7%, +1.9%)
        - ImageNet-V2: 63.1% (vs DFN 60.0%, +3.1%)
        - 检索平均: 60.9% (vs DFN 54.5%, +6.4%)
        - **SOTA性能**: 在38个基准测试中达到58.6%平均分
      - **超大规模 (1.4B)**:
        - 继续保持性能提升，验证方法的可扩展性
  - **消融研究发现**:
      - **LVLM选择**: Qwen2-VL在多个开源LVLM中表现最佳
      - **SFT有效性**: GPT-4o微调显著提升数据质量和下游性能
      - **文本类型贡献**:
        - 详细描述贡献最大 (+3.4%性能提升)
        - 硬负样本训练 (+0.8%性能提升)
        - 短标签分类 (+0.4%性能提升)
      - **混合比例**: 75%增强文本为最优配比
  - **质量评估**:
      - **图文相似度**: OpenAI CLIP-Large评估显示增强数据相似度更高
      - **GPT-4o评分**: 合成标注质量评分显著优于原始标注
      - **下游任务验证**: CLIP模型在增强数据上训练效果最佳
  - **关键发现**:
      - **成本效率**: 轻量LVLM经SFT后可达大模型性能，成本降低9倍
      - **多粒度文本价值**: 详细描述+短标签+负样本的组合最有效
      - **可扩展性**: 方法在1M到1.5B规模上均表现出色
      - **质量提升**: 相同数据规模下性能显著超越现有方法
  - **发布时间**: arXiv 2025年7月 | 中国科学技术大学 & 腾讯微信视觉
  - **开源**: ✅ VLM-150M数据集(1.5亿图文对) + HQ-CLIP模型 + 数据精化pipeline
  - **重要意义**:
      - **CLIP数据质量新标准**: 建立了基于LVLM的大规模数据增强新范式
      - **成本效率突破**: 证明轻量模型经适当微调可替代昂贵大模型
      - **多粒度文本框架**: 提出了正负样本、长短文本结合的完整文本增强框架
      - **可扩展解决方案**: 为构建更大规模、更高质量的视觉语言数据集提供了实用路径
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2511.02046">📄 Text-VQA Aug</a></b><br>
<code>arXiv 2511.02046</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**：**面向 Text-VQA 的自动化QA合成** —— 构建一个端到端、训练免（training-free）的多模型流水线，基于场景文本自动生成高质量问题-答案对，为文本VQA预训练提供规模化数据
  - **数据合成方法** - **OCR + Grounding + Crop Caption + 答案抽取 + 问题生成 + 验证**：
      1) **Text-Spotting（OCR检测+识别）**：使用 GLASS 提取场景文本与框
      2) **局部上下文识别（Grounding）**：用 Kosmos-2 生成前景/背景 ROI 裁剪并与OCR对齐
      3) **裁剪图像描述**：将裁剪图与其关联OCR一并输入 LLaVA-R 生成局部caption，随后拼接汇总为全局描述
      4) **OCR答案选择算法**：基于全局描述定位顺序相邻的OCR token组，生成潜在答案集合（给出伪代码与规则）
      5) **问题生成（LLM）**：以“图像描述+指定OCR答案”为条件，调用 Intel Neural Chat 7B 产出极简问题
      6) **QA对验证与长度过滤**：同一LLM进行“Right/Wrong”判定，过滤长度过短/过长问题，降低幻觉与噪声
  - **数据规模**：
      - **Text-VQAaug 数据集**：44,581 张图像，72,490 个 QA（约 1.6 问题/图）
      - 与 Text-VQA 等对照：问题更具体（中位长度约14词），部分问题不直接包含OCR词但答案来自OCR
  - **特点与优势**：
      - **训练免、可扩展**：完全依赖预训练LMM/OCR/grounding模型，流水线可横向扩展到新领域/场景
      - **答案先验+问题条件化**：先选答案再生问题，避免纯生成式引起的漂移，提升可控性与一致性
      - **质量控制**：LLM判真/假+长度约束，显著减少不合格样本
  - **适用场景**：文本无障碍辅助、零售检索、教育题材合成、医疗设备读数/标签理解、交通安全（牌照等）
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2504.11257">📄 UI-E2I-Synth</a></b><br>
<code>arXiv 2504.11257</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**：**GUI 指令定位（grounding）的合成数据与评测** —— 提出大规模 GUI 指令合成流水线 UI-E2I-Synth，并构建综合评测基准 UI-I2E-Bench，面向桌面/网页/移动多平台的真实高分辨率场景
  - **数据合成方法** - **三阶段分而治之（元素解析 → 指代表达生成 → 指令合成）**：
      1) **原始数据与解析**：从 Web/Windows/Android 收集截图+元数据，启发式解析三要素（类型/内容/框）并重采样平衡元素类型与尺寸分布
      2) **元素指代表达（RE）生成**：在 Set-of-Marks 截图上下文中，基于解析到的元素属性，用 GPT-4o 生成显式/隐式两类 RE，降低纯从图生成的幻觉
      3) **参数化用户指令合成**：将 RE 与用户动作三元组（动作类型/动作内容/元素目标）结合，用 GPT-4o 生成第一人称、短而准确的最终指令
  - **数据与基准**：
      - **训练集（UI-E2I-Synth）**：1,635,594 张截图，9,899,581 条指令（Web 1.54M/9.10M；Desktop 14K/334K；AndroidControl 40K/109K；另含 MOTIF、WidgetCaption）
      - **评测集（UI-I2E-Bench）**：1,477 条，细化标注元素类型、元素/屏占比、指令显/隐式比例（隐式占比≥63%），更贴近真实使用
  - **实验结果**：
      - 在 ScreenSpot、ScreenSpot-Pro、UI-I2E-Bench 上，UI-I2E-VLM-7B 全面优于 OS-Atlas-7B 等现有方法（平均相对提升约+9.7%），在隐式指令与长尾元素（Icon/Input）上优势显著
      - 同等量（50万）网页指令训练时，UI-E2I-Synth 数据优于 OS-Atlas-Web；若去掉“指令合成”或元素属性增强，性能明显下降（消融）
  - **关键优势**：
      - **元素/屏占比分布更贴近真实桌面（1080p/1440p）**，强调小目标与高分辨率
      - **隐式指令覆盖与类型均衡**：显著提升模型对长尾元素与隐式表达的理解
      - **参数化指令合成**：先定义动作参数再生成用户指令，贴近真实人机交互表达
  - **应用**：与 GPT-4o 规划器结合用于 OSWorld 真实桌面任务，提升代理可用性
  

</details>
<details>
<summary>
<b><b><a href="https://scholar.google.com/scholar?q=SK%E2%80%91VQA">📄 SK‑VQA</a></b><br>
<code>Paper</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Large‑scale "image + context + QA" synthesis for multimodal RAG/KB‑VQA** — A pipeline that uses GPT‑4 to generate encyclopedic context documents and diverse questions, building 2M+ context‑augmented VQA samples to train/evaluate context‑aware MLLMs
  - **Data Synthesis**:
      - **Joint generation of context and QA**: Conditioned on the image, GPT‑4 outputs both a relevant article‑style context and QA requiring context reasoning, avoiding image‑only answers
      - **Multi‑source images**: LAION, WIT (Wikipedia), COCO‑Counterfactuals; with filtered subsets removing image‑referencing contexts (IR) and ensuring extractive answers (IR+CAP)
  - **Scale & Diversity**:
      - 2,006,489 QA over 290,266 image‑context pairs; >96% unique questions, richer POS/vocab/length than prior KB‑VQA datasets
  - **Findings**:
      - A more challenging benchmark (lower zero‑shot than Enc‑VQA/ViQuAE); as training data, outperforms InfoSeek/Enc‑VQA in cross‑dataset generalization; remains strongest under RAG with external retrieval
  - **Significance**:
      - **Image‑invariant text enhancement**: High‑quality "context+QA" around existing images for multimodal RAG/KB‑VQA training
      - **Quality control**: IR/IR+CAP filtering preserves/boosts performance with fewer samples, enabling task‑aware tuning
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2410.02713">📄 LLaVA‑Video: 基于合成数据的视频指令微调</a></b><br>
<code>arXiv 2410.02713</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**：**合成视频指令跟随数据 + 模型** — 构建 LLaVA‑Video‑178K 数据集与 LLaVA‑Video 模型；采用**稠密取帧**与**三层递归描述**，覆盖详细描述、开放式QA与多选QA
  - **数据合成方法**：
      - **动态未裁剪视频来源（10个）**；基于镜头数等指标筛选“动态性”最高的视频，避免静态/过度裁剪
      - **1 FPS 稠密采样** + **三级递归描述**（10秒片段、30秒汇总、全片总结）；用 GPT‑4o 生成详细描述与16类问题；去重与不可答过滤
  - **数据规模**：
      - 178,510 个视频 → 1.3M 指令样本：178K描述、960K开放式QA、196K多选QA
  - **实验发现**：
      - 帧数越多性能越好；提出 SlowFast 风格的视频表示，在固定 token 预算下容纳**多至3倍帧数**
      - 覆盖 11 个视频基准的强零样本表现；72B 开源模型在多项任务上可与商用模型竞争
  - **意义**：
      - 提供高质量合成视频指令数据与高效视频表征策略；计划开放数据、代码与模型权重
  
  #### 🤖 基于VLM/LLM的合成文本生成
  
  > 以下论文明确描述了如何使用大模型为图像生成合成captions/对话
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2503.22655">📄 Unicorn</a></b><br>
<code>arXiv 2503.22655</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**: **纯文本多模态数据合成** - 完全不依赖真实或生成的图像，仅从文本合成VLM训练数据
  - **数据合成方法** - **跨集成三阶段文本转图像表示Pipeline**:
      - **核心创新**: 利用跨模态表示空间的几何结构（modality gap理论），通过文本表示生成合成图像表示，**完全跳过图像生成步骤**
      - **Stage 1: 多样化Caption数据合成**:
        - **输入**: 1.2M稀疏caption种子（从多个来源采样）
          - **开放域**: MS-COCO、Flickr30K、CC3M、CC-YFCC等
          - **领域特定**: Conceptual Captions、Chart2Text、PlotQA等
        - **方法**: 使用LLM（Qwen2.5-72B-Instruction）为稀疏caption添加详细信息
        - **Prompt设计**: "在保持原始语义的同时添加更多细节（对象属性、空间关系、背景信息等）"
        - **输出**: 1.2M语义丰富、多样化的详细captions
        - **质量保证**: 通过多轮迭代优化，确保caption详细度和准确性
      - **Stage 2: 指令调优数据生成**:
        - **输入**: 从Stage 1中采样471K captions
        - **方法**: 使用Qwen2.5-72B-Instruction生成三类任务数据
        - **三大任务类型**:
          1. **多选题（Multiple-Choice）**:
             - 基于caption内容生成问题和4个选项
             - 测试细节理解和推理能力
          2. **问答（Question-Answering）**:
             - 生成开放式问题和详细答案
             - 涵盖描述性、事实性、推理性问题
          3. **复杂推理（Complex Reasoning）**:
             - 需要多步推理的复杂问题
             - 结合视觉理解和逻辑推理
        - **输出**: 471K多任务指令调优数据
      - **Stage 3: 模态表示转移（关键创新）**:
        - **理论基础 - Modality Gap几何结构**:
          - 对于配对的图像-文本（x_img, x_text），其表示满足: **e_x - e_y = c + ε**
          - **c**: 常量正交向量（模态间隙）
          - **ε**: 对齐噪声（近似高斯分布）
        - **转移过程 - Mean Shift**:
          1. 使用文本编码器（LLM2CLIP）将Stage 1/2的captions编码为文本表示 e_text
          2. 计算模态间隙向量c（通过少量配对数据统计得到）
          3. 应用mean shift: **e_synthetic_img = e_text + c**
          4. 得到合成图像表示，无需生成真实图像
        - **关键技术**:
          - 使用**LLM2CLIP**（专门优化的文本编码器）确保文本表示质量
          - **训练无关**: 无需额外训练，纯粹利用几何结构
          - **可扩展**: 可应用于任意规模的文本数据
        - **优势**:
          - **无需图像**: 完全跳过图像生成/存储，节省API成本、时间、存储空间
          - **高效**: API成本降低**44倍**，时间降低**4倍**，存储降低**27倍**
          - **质量**: 合成表示在共享空间中与真实图像表示分布一致
      - **关键技术优势**:
        - **成本极低**: 相比传统方法大幅降低成本（API: $6.84 vs $12, 存储: 4GB vs 109GB）
        - **无幻觉风险**: 不依赖视觉生成模型，避免图像生成的幻觉问题
        - **可扩展性强**: 文本数据丰富且廉价，易于扩展
        - **隐私友好**: 无需收集/存储真实图像
  - **数据规模**:
      - **Unicorn-1.2M**（预训练数据集）: 1.2M详细captions + 对应的合成图像表示
      - **Unicorn-471K-Instruction**（指令调优数据集）: 471K多任务指令数据 + 对应的合成图像表示
      - **Caption来源多样性**:
        - 开放域: MS-COCO, Flickr30K, CC3M, CC-YFCC等
        - 领域特定: Conceptual Captions, Chart2Text, PlotQA, FigureQA, DVQA等
  - **模型**: **Unicorn-8B VLM**
      - **架构**: 基于主流VLM架构（视觉编码器 + 投影层 + LLM）
      - **训练策略**:
        - **预训练**: 使用Unicorn-1.2M进行模态对齐
        - **指令调优**: 使用Unicorn-471K-Instruction进行微调
      - **特点**: 完全不使用真实图像训练
  - **实验结果** - **与基于真实图像的方法性能相当**:
      - **多模态基准评估**: 在多个VLM基准上达到竞争性能
      - **成本效益**: 显著降低训练成本的同时保持性能
      - **消融研究**:
        - **Stage 1多样性**: 详细caption显著提升模型性能
        - **Stage 2任务类型**: 多任务混合训练优于单任务
        - **Stage 3表示转移**: Mean shift方法有效弥合模态间隙
  - **成本对比**（vs传统图像-文本合成方法）:
      - **API成本**: $6.84 vs $12（降低44%）
      - **合成时间**: 0.3天 vs 4天（降低92.5%）
      - **存储需求**: 4GB vs 109GB（降低96.3%）
  - **发布时间**: arXiv 2025年3月
  - **机构**: Xreal、西湖大学、浙江大学、上海AI实验室、南洋理工大学、北京航空航天大学、大湾区大学
  - **作者**: Xiaomin Yu, Pengxiang Ding, Wenjie Zhang等
  - **开源**: ✅ **完全开源** - 代码、数据集
  - **代码仓库**: [github.com/Yu-xm/Unicorn](https://github.com/Yu-xm/Unicorn)
  - **重要意义**:
      - **范式突破**: 首个完全不依赖真实/生成图像的多模态数据合成框架
      - **理论创新**: 系统性地将modality gap理论应用于大规模数据合成
      - **成本革命**: 显著降低多模态数据合成的成本、时间和存储开销
      - **可扩展性**: 利用丰富的文本资源，易于扩展到更大规模
      - **实用价值**: 为资源受限场景下的VLM训练提供可行方案
  
  #### 🔬 基于大模型的文本生成
  
  > **核心思想**: 使用强大的VLMs（如GPT-4V）或LLMs（如GPT-4）为图像生成更高质量的captions/对话数据
  

</details>
<details>
<summary>
<b><b><a href="https://scholar.google.com/scholar?q=Synthesize%20Step-by-Step%20CVPR%202024">📄 Synthesize Step-by-Step</a></b><br>
<code>CVPR 2024</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-CVPR_2024-red?style=flat-square"/>
</summary>

  - **Focus**: **Chart VQA Reasoning Data Generation** - Uses LLM as automatic data annotator to generate step-by-step reasoning QA pairs for chart images
  - **Data Synthesis Method** - **Template-Guided + LLM Generation + Tool-Assisted Execution**:
      - **Core Innovation**: **Synthesize Step-by-Step Strategy** - LLM learns to decompose complex questions into step-by-step sub-questions, uses external tools (Python) to execute and derive final answers
      - **Three-Stage Pipeline**:
        1. **Template-based QA Generation (Training Corpus)**:
           - **Input**: SVG annotations of ChartQA images (title, legend, data point values, colors, etc.)
           - **Method**: Hand-designed 28 templates defining reasoning programs (Domain-Specific Language - DSL)
           - **Output**: 357K template-generated QA pairs covering 7 reasoning types
           - **Reasoning Types**: Value retrieval, comparisons, ranges, averages, sorting, math operations, multi-step inference
           - **Purpose**: Provides training data for teaching LLM how to decompose problems and use tools
        2. **LLM-based Data Generator Training**:
           - **Architecture**: ViT (CLIP) + Linear projection + LLM (MPT-7B) + DEPLOT table prediction
           - **Input**: Image features + predicted data table + prompt
           - **Training**: Trained on template QA to learn generating: question → rationale program → execute to get answer
           - **Key Innovation**:
             - **Does not directly generate answers**, but generates executable rationale programs
             - Rationale programs contain: atom VQA calls (e.g., `ans_0=VQA("What is the value of 2002?")`) + Python math computations
             - Uses DEPLOT-predicted tables as OCR input to address CLIP-ViT's weak text perception
        3. **Large-Scale Data Synthesis & Filtering**:
           - **Generation**: LLM generates question + rationale program for images
           - **Execution**: Python parser parses and executes rationale program to derive answers
           - **Filtering**: Post-processing filtering based on decoding score (threshold=-10) for low-quality questions
           - **Output**: LaMenDa dataset (LLM-augmented Data)
      - **Key Technical Advantages**:
        - **Accuracy**: More accurate answers by executing programs rather than direct generation
        - **Interpretability**: Rationales provide step-by-step reasoning paths
        - **Scalability**: Once trained, can generate data for arbitrary chart images
        - **Domain Flexibility**: Can control generation of specific question types via prompts
        - **Cost-Effective**: Uses open-source LLM (MPT-7B) rather than proprietary API
  - **Data Scale**:
      - **Template QA**: 357K (training LLM generator)
      - **LaMenDa (ChartQA)**: 326K (403K generated, filtered after execution)
      - **LaMenDa (PlotQA)**: 1.7M (3M generated, filtered after execution)
      - **Chart Captioning Datasets**: 1.6M (generated from 137K images)
  - **Experimental Results** - **SOTA on ChartQA Dataset**:
      - **Human-written questions**: Accuracy improved from 38% to **54%** (MATCHA baseline)
      - **Overall ChartQA**: Significantly surpasses previous SOTA
      - **PlotQA**: Also achieves SOTA on synthetic dataset
      - **Ablation Studies**: Step-by-step generation outperforms direct answer generation
  - **Publication**: CVPR 2024
  - **Institution**: Johns Hopkins University & AWS AI Labs
  - **Authors**: Zhuowan Li, Bhavan Jasani, Peng Tang, Shabnam Ghadar
  - **Open Source**: To be confirmed (CVPR papers typically open-source code and data)
  - **Significance**:
      - **First Systematic Chart Reasoning Data Synthesis**: Introduces step-by-step reasoning data generation paradigm for Chart VQA
      - **Tool-Assisted Execution**: Combines LLM generation with tool execution to ensure answer accuracy
      - **Template-Guided Training**: Innovatively uses template data to train LLM generator
      - **Significant Performance Boost**: 16 percentage point improvement on most challenging human-written questions
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2405.01483">📄 MANTIS</a></b><br>
<code>arXiv 2405.01483</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **重点**: **交错多图像指令微调** - 首个多图像指令微调数据集MANTIS-INSTRUCT，包含721K多图像指令数据，使用学术级资源训练多图像LMM
  - **数据构建方法** - **多源数据集整理 + 指令格式化**:
      - **核心创新**: 通过学术级资源的指令微调构建强大的多图像LMM，避免在数亿噪声交错图文数据上进行大规模预训练
      - **MANTIS-INSTRUCT数据集构建**:
        - **总规模**: 721K多图像指令实例，涵盖14个子集
        - **四种多图像技能覆盖**:
          1. **共指**: 理解如"第二张图像"的引用并将其定位到引用的图像
             - **LLaVA-665k-multi**（313K）: 将多个单图像对话连接成多图像序列
             - **LRV-multi**（8K）: 包含自然语言引用，如"对于第二张图像"
          2. **比较**: 捕获多张图像之间的细微差别和共同点
             - **CoInstruct**（151K）: 图像质量、视觉相似性、差异描述
             - **Dreamsim**（16K）、**Spot-the-Diff**（8K）、**Birds-to-Words**（3K）
          3. **推理**: 捕获跨多张图像的信息并对多个片段进行推理
             - **NLVR2**（86K）: 跨图像内容的逻辑推理
             - **IconQA**（64K）: 计数、图像匹配、图像检索
             - **Contrast-Caption**（36K）: 重新格式化标题数据集
             - **ImageCoDe**（17K）: 自由形式多图像QA
             - **Multi-VQA**（5K）: 自收集多图像QA
          4. **时间理解**: 观察多帧以理解时间信息
             - **VIST**（7K）: 从图像序列叙述故事
             - **NExT-QA**（4K）、**STAR**（3K）: 视频理解任务
        - **单图像数据集**（268K）: DVQA（200K）、DocVQA（39K）、ChartQA（28K）用于平衡多图像和单图像能力
        - **新整理子集**（4个新数据集）:
          - **LLaVA-665k-multi**: LLaVA-665k的多图像版本
          - **LRV-multi**: LRV的多图像版本
          - **Contrast-Caption**: 重新格式化标题数据集用于多图像推理
          - **Multi-VQA**: 自收集多图像QA数据集
      - **文本-图像交错格式**:
        - **格式**: "(image {i}: <BOI><image><EOI>)"，其中<BOI>和<EOI>是图像分隔符
        - **设计原则**: (1) 清晰标记图像之间的边界，(2) 表示图像的序列号
        - **实现**: 使用<Image>和</Image>作为分隔符
        - **图像上下文长度**:
          - **LLaVA架构**: 每张图像576个图像令牌，最多14张图像（8K上下文）
          - **Idefics2架构**: 每张图像64个令牌，最多128张图像（8K上下文）
      - **关键技术**:
        - **指令微调聚焦**: 在721K高质量数据上进行低成本指令微调 vs. 大规模预训练
        - **多技能覆盖**: 系统覆盖所有四种多图像技能
        - **学术级资源**: 无需大规模计算资源即可实现强大性能
        - **格式标准化**: 跨所有数据集一致的文本-图像交错格式
  - **MANTIS模型家族**:
      - **架构变体**:
        - **Mantis-CLIP**: CLIP编码器 + LLaMA-3-8B，在CC3M子集（0.56M）上预训练
        - **Mantis-SigLIP**: SigLIP编码器 + LLaMA-3-8B，在CC3M子集（0.56M）上预训练
        - **Mantis-Flamingo**: CLIP编码器 + MPT-7B，从OpenFlamingo初始化（在2.4B数据上预训练）
        - **Mantis-Idefics2**: SigLIP编码器 + Mistral-7B-v0.1，从Idefics2初始化（在143M数据上预训练）
      - **训练**: 在MANTIS-INSTRUCT（721K）+ 268K单图像数据上微调
      - **训练资源**: 16×A100-40G训练36小时
  - **Mantis-Eval基准测试**:
      - **规模**: 217个多图像推理示例，涵盖不同主题
      - **覆盖**: 大小感知、重量比较等
      - **构建**: 由注释者精心整理，图像通过Google搜索获取
      - **格式**: 包含多项选择和简答题
  - **数据规模**:
      - **MANTIS-INSTRUCT**: 721K多图像指令实例
        - **每个示例平均图像数**: 4.7
        - **每个示例最大图像数**: 50
        - **平均轮数**: 14.4
        - **平均文本令牌长度**: 555
        - **平均文本+图像令牌长度**: 3,584
      - **单图像数据集**: 268K实例用于平衡
  - **实验结果** - **在所有多图像基准测试上达到SOTA**:
      - **多图像基准测试**（5个基准测试）:
        - **NLVR2**: Mantis-Idefics2达到**89.71**（vs. Idefics2-8B 86.87，+2.84）
        - **Q-Bench**: Mantis-Idefics2达到**75.20**（vs. Idefics2-8B 57.00，+18.20）
        - **Mantis-Eval**: Mantis-SigLIP达到**59.45**（vs. Idefics2-8B 48.85，+10.60）
        - **BLINK**: Mantis-Idefics2达到**49.05**（vs. Idefics2-8B 45.18，+3.87）
        - **MVBench**: Mantis-SigLIP达到**50.15**（vs. Idefics2-8B 29.68，+20.47）
        - **平均**: Mantis-SigLIP达到**62.7**（vs. Idefics2-8B 53.5，+9.2），Mantis-Idefics2达到**64.5**（vs. Idefics2-8B 53.5，+11.0）
      - **vs. GPT-4V**: Mantis-Idefics2匹配GPT-4V性能（64.5 vs 64.5平均）
      - **vs. Idefics2-8B**: 尽管Idefics2-8B在140M交错多图像数据上预训练（比MANTIS-INSTRUCT大200倍），Mantis平均超越Idefics2-8B **11个绝对点**
      - **泛化**: 保持内和保持外结果同样强大，显示强大的泛化能力
      - **单图像性能**: Mantis保持强大的单图像性能，与CogVLM和Emu2相当
  - **发布时间**: arXiv 2024年5月
  - **机构**: 滑铁卢大学、清华大学、Sea AI Lab
  - **开源**: ✅ [GitHub](https://github.com/tiger-ai-lab/Mantis) - 代码、MANTIS-INSTRUCT数据集（721K）、模型
  - **重要意义**:
      - **首个多图像指令微调数据集**: MANTIS-INSTRUCT为未来研究提供重要基线
      - **学术级资源**: 无需大规模预训练即可达到SOTA，展示指令微调的效率
      - **多技能覆盖**: 系统覆盖共指、比较、推理和时间理解
      - **成本效益**: 低成本指令微调（721K数据）优于在200倍更大数据集上预训练的模型
      - **泛化**: 在保持内和保持外基准测试上都有强大性能
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2406.11833">📄 MMDU</a></b><br>
<code>arXiv 2406.11833</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-NeurIPS_2024-red?style=flat-square"/>
</summary>

  - **重点**: **多轮多图像对话理解基准测试和指令微调数据集** - 全面的基准测试和大规模指令微调数据集，旨在评估和改进LVLM在多轮和多图像对话中的能力
  - **数据构建方法** - **基于聚类的图像选择 + GPT-4o生成 + 人工注释**:
      - **核心创新**: 使用聚类算法从开源Wikipedia中找到相关图像和文本描述，通过人工注释者和GPT-4o辅助构建问答对
      - **MMDU基准测试构建**:
        - **数据收集**:
          1. **图像和文本选择**:
             - **来源**: 开源Wikipedia条目
             - **方法**: 聚类算法识别相关Wikipedia实体
             - **过程**: 使用句子转换器编码条目的相关标签，使用获得的嵌入对条目进行聚类
             - **图像匹配**: 使用图像标题匹配条目以获得高度相关的条目和图像集
             - **选择**: 在每个聚类内，选择多张图像和关联的文本信息以创建图像-文本对组合（范围从2到20张图像）
          2. **问答生成**:
             - **GPT-4o生成**: 使用精心设计的提示指导GPT-4o根据可用图像和文本信息生成相应的问答
             - **多轮构建**:
               - 首先为每张单图像及其关联文本构建多轮问答对
               - 然后将多张图像组合输入GPT-4o以基于多张图像生成多轮问答对
               - 将多张图像的多轮问答对与每张单图像的问答对结合，创建包含单图像和多图像问题的对话
             - **文本-图像交错格式**: 使用<image-1>、<image-2>等标签来引用不同的图像
          3. **质量控制**:
             - **人工注释**: 专家注释者仔细审查生成的对话
             - **选择**: 为基准测试选择110个高质量多轮多图像对话
             - **编辑**: 仔细编辑样本以消除GPT-4o响应中的幻觉和错误
             - **质量保证**:
               - 结合自动和手动筛选方法
               - 多轮手动审查机制（至少两轮：常规审查者的初步检查，专家的深入检查）
               - 专门的Web UI用于快速浏览和修改数据内容
        - **MMDU-45K数据集构建**:
          - **相同过程**: 使用与构建MMDU相同的过程
          - **差异**: 随机采样人工验证而不是MMDU中使用的详尽人工评估
          - **规模**: 45K高质量指令微调数据
      - **关键技术**:
        - **基于聚类的选择**: 通过选择相关图像确保逻辑连贯性和丰富内容
        - **GPT-4o辅助**: 利用GPT-4o进行问答生成，同时保持人工监督
        - **多轮设计**: 在同一对话中支持单图像和多图像问题
        - **可扩展格式**: 灵活的格式允许连接多个对话，理论上支持无限长度
  - **MMDU基准测试特征**:
      - **多轮和多图像**: 最多20张图像和27轮，至少比之前的基准测试长5倍
      - **长上下文**: 最多18K图像+文本令牌，评估LVLM处理和理解扩展上下文信息的能力
      - **开放评估**: 采用自由形式多轮输出，通过GPT-4o作为判断评估LVLM的性能
      - **评估维度**（6个维度）:
        1. **创造性**: 响应的原创性和创新性
        2. **丰富性**: 信息的详细程度和深度
        3. **视觉感知**: 识别视觉元素的准确性
        4. **逻辑连贯性**: 逻辑结构和流程
        5. **答案准确性**: 事实信息的正确性
        6. **图像关系理解**: 理解图像之间的关系
        - **总体分数**: 全面评估（从6个维度聚合得出）
  - **数据规模**:
      - **MMDU基准测试**: 110个高质量多轮多图像对话，包含超过1,600个问题
        - **每个对话的图像数**: 2到20张图像
        - **平均图像和文本令牌长度**: 8.2K令牌
        - **最大图像和文本长度**: 18K令牌
        - **平均轮数**: 15轮问答
      - **MMDU-45K数据集**: 45K高质量指令微调数据
        - **平均文本令牌**: 6.4K
        - **每个样本的图像数**: 2-20张图像
        - **平均15轮问答**
  - **实验结果**:
      - **基准测试评估**（评估了15个LVLM）:
        - **开源 vs. 专有差距**: 最佳开源模型得分42.8%，远低于专有GPT-4o的70.2%
        - **性能差距**: 专有和开源LVLM之间存在显著性能差异
      - **微调结果**（InternLM-XC2）:
        - **MMDU**: +14.5%改进
        - **MMStar**: +1.1%改进
        - **MathVista**: +1.5%改进
        - **ChartQA**: +1.2%改进
      - **模型改进**:
        - **更长对话**: 在MMDU-45K上微调生成更长、更准确的对话
        - **多轮性能**: 在多轮、多图像场景上显著改进
        - **泛化**: 在MMDU和现有基准测试上都有改进
  - **发布时间**: NeurIPS 2024（数据集和基准测试轨道）
  - **机构**: 上海交通大学、上海AI实验室、香港中文大学、CPII under InnoHK、MThreads, Inc.
  - **开源**: ✅ [GitHub](https://github.com/Liuziyu77/MMDU) - 代码、MMDU基准测试（110个对话）、MMDU-45K数据集（45K样本）
  - **重要意义**:
      - **全面基准测试**: 首个专门为多轮、多图像对话理解设计的基准测试
      - **长上下文评估**: 评估LVLM处理扩展上下文信息的能力（最多18K令牌）
      - **开放评估**: 采用自由形式多轮输出，使用GPT-4o作为判断，比传统多项选择格式更真实
      - **可扩展数据集**: MMDU-45K提供大规模指令微调数据以改进多轮、多图像能力
      - **弥合性能差距**: 证明在MMDU-45K上微调显著解决了开源和专有LVLM之间的差距
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2403.09028">📄 ChartInstruct</a></b><br>
<code>arXiv 2403.09028</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**：**Chart理解的指令调优数据** - 构建大规模、多样化的chart指令数据集，用于训练通用chart理解模型
  - **数据合成方法** - **LLM驱动的多任务指令生成**：
      - **核心创新**：利用GPT-3.5/GPT-4生成覆盖广泛chart理解任务的指令数据，支持instruction tuning
      - **数据收集**：
        - **Chart语料**：从多个在线来源收集真实图表，涵盖多样化视觉风格
          - **UniChart数据集**：611K charts（来源：Pew, Statista, OECD, OWID）
          - **WebCharts（新贡献）**：41K charts（网络爬取，使用Gemini Pro Vision提取数据表）
        - **最终用于instruction生成**：70,882个独特charts
      - **指令生成Pipeline**：
        - **任务选择**：定义6大任务类别
          1. **Chart Summarization**：生成图表caption，捕获关键洞察（趋势、模式）
          2. **Open-ended QA**：生成解释性问答（需要详细回答）
          3. **Fact Checking**：给定claim，生成verdict（accept/refute）+ explanation
          4. **Chain-of-Thought (CoT) Reasoning**：
             - **Variable Dependent**：使用工具（受ToolFormer启发）计算统计值
             - **Variable Independent**：检索、比较、基础数学分析
          5. **Code Generation**：生成可执行Python脚本回答查询（受PAL启发）
          6. **Novel Tasks**：让LLM提议新任务（未来值预测、模式检测等）
        - **Prompt设计**：
          - 每个任务设计专门的prompt模板
          - 输入：图表数据表 + 元数据（标题）
          - 输出：指令-响应对
        - **生成策略**：
          - **GPT-4**：用于复杂推理任务（CoT、Novel tasks）
          - **GPT-3.5 Turbo**：用于中等复杂度任务
          - 每次调用生成多个样本以增加多样性和降低成本
      - **关键技术优势**：
        - **任务多样性**：覆盖6大类、多个子任务，避免task-specific overfitting
        - **真实图表**：基于真实在线图表，而非合成数据
        - **自动化流程**：完全自动化的LLM驱动pipeline，可扩展
  - **数据规模**：
      - **ChartInstruct数据集**：191K指令，对应70,882个charts
      - **分布**：
        - Chart Summarization: 53,876 (28.24%)
        - Open-ended QA: 42,470 (22.26%)
        - CoT Reasoning: 27,271 (14.3%)
        - Fact Checking: 24,175 (12.67%)
        - Code Generation: 19,572 (10.26%)
        - Novel Tasks: 23,410 (12.27%)
      - **Charts来源分布**（unique charts数量）：
        - WebCharts: 41,742 (58.9%)
        - OECD/OWID: 10,949 (15.4%)
        - Statista: 9,992 (14.1%)
        - PlotQA: 8,199 (11.6%)
      - **Instructions分布**：WebCharts贡献157,190 instructions，占总数的67.5%
  - **模型**：两种系统设计
      1. **End-to-end**：UniChart vision encoder + LLM（Llama2-7B / Flan-T5-XL-3B）
      2. **Pipeline**：Chart-to-table model (DEPLOT) → LLM
  - **实验结果** - **4个benchmark上的SOTA**：
      - **ChartQA**：超越之前SOTA
      - **Chart2Text**：summarization任务SOTA
      - **OpenCQA**：open-ended QA SOTA
      - **ChartFC**：fact-checking SOTA
      - **Human evaluation**：在真实chart理解场景中表现出色
  - **数据质量**：
      - **专家评估**：100个样本人工标注
        - 87%的指令描述有效任务
        - 86%的输入与任务描述匹配
        - 61%的输出完全正确，8%部分正确
      - **多样性**：动词-名词对分析显示广泛的理解和推理任务
  - **发布时间**：arXiv 2024年3月
  - **机构**：York University (Canada), Qatar Computing Research Institute, Salesforce Research, NTU Singapore
  - **作者**：Ahmed Masry, Mehrad Shahmohammadi, Md Rizwan Parvez, Enamul Hoque, Shafiq Joty
  - **开源**：✅ [代码和数据](https://github.com/vis-nlp/ChartInstruct)
  - **重要意义**：
      - **首个大规模chart指令数据集**：为chart领域instruction tuning奠定基础
      - **任务全面性**：覆盖chart理解的多个方面，避免narrow task focus
      - **真实数据**：基于真实在线图表，更接近实际应用场景
      - **开放贡献**：完全开源数据、代码，推动chart理解研究
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2412.05243">📄 CompCap</a></b><br>
<code>arXiv 2412.05243</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**：**Composite Images的Caption生成** - 为合成图像（拼贴、图表、表格、代码、图示等）生成高质量captions
  - **问题背景**：
      - **Composite Images (CI)**：合成视觉内容，由多种元素组合（照片、文本、图形等）
      - **现状**：现有MLLM训练数据主要关注自然图像(NI) captions，CI captions稀缺
      - **影响**：MLLMs在CI上表现差，captioning和VQA准确率明显低于NI
  - **数据合成方法** - **CompCap框架：Metadata驱动的CI-caption合成**：
      - **核心创新**：利用metadata（图像-caption对、布局、表格数据、文本）+ LLMs + 自动化工具，合成CI及其详细captions
      - **CompCap框架（通用）**：
        - **输入**：Metadata（原始数据 + 配置/定制）
        - **图像合成**：使用各种工具（渲染库、代码）基于metadata生成CI
        - **Caption生成**：LLM基于metadata生成准确、详细的caption
        - **灵活性**：可为不同CI类型实现定制化pipeline
      - **6种CI类型的实现**：
        1. **Collage（拼贴）**：
           - **原始数据**：图像-caption对数据集
           - **配置**：随机生成布局（行列结构）
           - **图像合成**：根据布局排列图像
           - **Caption生成**：LLM基于单个图像captions + 布局信息生成整体caption
           - **检索策略**：随机检索、相似度检索、实体检索（3种）
        2. **Image-Text**：
           - 在图像上叠加文本
           - LLM生成描述图像内容和文本的caption
        3. **Chart（图表）**：
           - **原始数据**：表格数据
           - **图像合成**：使用Matplotlib/Plotly渲染图表
           - **Caption生成**：LLM基于表格数据生成图表描述（数据分析、趋势）
        4. **Diagram（图示）**：
           - 使用Mermaid等工具生成流程图、架构图
        5. **Code（代码）**：
           - **原始数据**：代码片段
           - **图像合成**：代码渲染为图像（syntax highlighting）
           - **Caption生成**：描述代码功能、结构
        6. **Table（表格）**：
           - 表格数据渲染为图像
           - LLM生成表格内容描述
      - **Caption质量标准**：
        - **Accuracy**：忠实反映图像内容，无误导信息
        - **Detailedness**：提供具体洞察，超越基础描述
      - **关键技术优势**：
        - **Metadata驱动**：确保caption准确性（基于结构化数据而非视觉推测）
        - **模块化**：易于扩展到新的CI类型
        - **可扩展**：利用丰富的原始数据（图像数据集、表格等）
  - **数据规模**：
      - **CompCap-118K**：118K CI-caption pairs
      - **组成**：
        - Collage: 42.3%
        - Image-Text: 31.4%
        - Chart: 18.7%
        - Table: 3.4%
        - Diagram: 2.5%
        - Code: 1.7%
  - **实验结果** - **CI理解基准上的显著提升**：
      - **训练**：在xGen-MM-inst.-4B、LLaVA-NeXT-Vicuna-7B/13B上SFT
      - **11个benchmark平均提升**：
        - xGen-MM-4B: +1.7%
        - LLaVA-NeXT-7B: +2.0%
        - LLaVA-NeXT-13B: +2.9%
      - **CI-specific benchmark显著提升**：
        - ChartQA: +8.0% (LLaVA-13B)
        - DocVQA: +6.2%
        - InfoVQA: +4.5%
        - TextVQA: +3.8%
      - **NI benchmark保持性能**：在自然图像任务上无退化
  - **消融研究**：
      - **Caption vs VQA数据**：Caption数据对CI理解更有效
      - **数据量**：性能随CompCap数据量增加而提升
      - **CI类型**：Chart和Image-Text类型贡献最大
  - **发布时间**：arXiv 2024年12月
  - **机构**：Meta, Tufts University, Georgia Tech
  - **作者**：Xiaohui Chen, Satya Narayan Shukla, Mahmoud Azab等
  - **开源**：待确认
  - **重要意义**：
      - **填补CI数据空白**：首次系统性地为CI生成高质量captions
      - **通用框架**：CompCap框架可应用于多种CI类型
      - **实用影响**：显著提升MLLMs对真实世界合成图像的理解能力
      - **数据效率**：11.8万数据即可带来显著提升
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2410.18558">📄 Infinity-MM</a></b><br>
<code>arXiv 2410.18558</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**：**大规模多模态指令数据构建** - 收集、整合和合成40M+多模态指令数据，同时提出基于tagging system的合成方法
  - **核心贡献**：数据规模 + 合成方法创新
      - **数据规模**：44.8M多模态指令数据（开源最大规模之一）
      - **合成方法**：基于tagging system的数据合成，支持持续扩展
  - **数据构建方法**：
      - **阶段1：数据收集**：
        - **统一预处理**：收集可用的多模态指令数据集，进行格式统一
        - **质量过滤**：去重、质量检查
        - **来源**：整合多个公开数据集（LLaVA系列、ShareGPT4V、Cambrian等）
      - **阶段2：数据合成（创新点）**：
        - **Tagging System设计**：
          - **Image Tagging**：使用RAM++模型提取图像tags（对象、动作、场景）
          - **Instruction Tagging**：设计三层指令tag系统
            - **一层**：6大类（Coarse Perception, Fine-grained Perception-single, Fine-grained Perception-cross, Relation Reasoning, Attribute Reasoning, Logic Reasoning）
            - **二层**：细化任务特征
            - **三层**：基于具体任务需求的详细分类，总计199个sub-tasks
        - **Image-Instruction Mapping**：
          - 统计seed data中image tags与instruction tags的共现频率
          - 计算TF-IDF值，建立image tag → instruction type的映射
          - **作用**：指导新图像应该生成什么类型的指令
        - **Instruction Synthesis Pipeline**：
          1. **Question Generation**：
             - 输入：图像 + 目标instruction type + few-shot examples
             - 模型：MiniCPM-V2.6（开源VLM）
             - 输出：符合目标type的问题
          2. **Answer Generation**：
             - 使用不同prompt生成多样化答案格式
             - 确保答案准确性和格式多样性
          3. **Quality Filtering**：
             - 重新输入图像+问题到VLM，评估相关性
             - 过滤低质量问题
      - **关键技术优势**：
        - **Tagging System**：系统化的指令分类，确保数据多样性
        - **Image-Instruction对应**：自动识别哪类图像适合哪类指令
        - **开源VLM合成**：使用MiniCPM-V2.6而非GPT-4，成本低且可复现
        - **持续扩展**：框架支持持续添加新数据
  - **数据规模**：
      - **Infinity-MM**：44.8M samples
      - **组成**（按数据类别）：
        - **图像-文本描述数据**：10M
        - **综合视觉指令数据**：25.8M
          - General Instruction: 7.1M
          - OCR Data: 2.6M
          - Doc/Chart/Screen: 5.8M
          - Math/Reasoning: 1.3M
          - Text Instruction: 9M
        - **精选视觉指令数据**：6M
          - General Instruction: 1.3M
          - OCR Data: 0.3M
          - Doc/Chart/Screen: 1.9M
          - Math/Reasoning: 0.7M
          - Text Instruction: 1.8M
        - **GPT4 & 合成数据**：3M
          - General Instruction: 1M
          - OCR Data: 0.5M
          - Doc/Chart/Screen: 0.1M
          - Math/Reasoning: 0.3M
          - Text Instruction: 0.3M
          - 新合成数据（使用开源VLM）：0.8M
  - **模型**：**Aquila-VL-2B**
      - **架构**：2B parameter VLM
      - **训练**：基于Infinity-MM训练
  - **实验结果** - **2B模型SOTA**：
      - **平均得分**：在多个benchmark上超越同规模模型
      - **优于其他开源数据训练的模型**：
        - 超越OneVision-SI训练的模型
        - 超越部分闭源数据训练的模型（见Figure 1）
      - **关键发现**：大规模高质量数据 + 合理混合比例 = SOTA性能
  - **消融研究**：
      - **数据规模**：性能随数据量增加而提升
      - **数据类型混合**：不同任务类型的最优混合比例
      - **Tagging System**：验证image-instruction mapping的有效性
  - **发布时间**：arXiv 2024年10月（v2: 2025年1月）
  - **机构**：BAAI (北京智源人工智能研究院), BJTU, BUPT, ICT/CAS, HKUST(GZ), PKU, DLUT
  - **作者**：Shuhao Gu, Jialing Zhang, Siyuan Zhou, Kevin Yu等（大团队）
  - **开源**：✅ [数据集](https://huggingface.co/datasets/BAAI/Infinity-MM)
  - **重要意义**：
      - **规模突破**：44.8M样本，开源数据中规模最大之一
      - **合成方法创新**：Tagging system提供系统化的数据合成指导
      - **开源VLM合成**：首次用开源VLM进行大规模高质量合成
      - **持续扩展**：框架支持持续数据扩展，而非一次性数据集
  

</details>
<details>
<summary>
<b><b><a href="https://scholar.google.com/scholar?q=ShareGPT4V">📄 ShareGPT4V</a></b><br>
<code>Paper</code>
</summary>

  - **Data Synthesis Method** (Section 3.1):
      - Uses **GPT-4V** to generate high-quality captions for 100K images
      - Prompt design: Requires detailed descriptions (3-5 times more detailed than original captions)
      - Image sources: Curated images from COCO, SAM, LAION, etc.
  - **Data Scale**: 100K high-quality captions
  - **Open Source**: ✅ [Dataset](https://huggingface.co/datasets/Lin-Chen/ShareGPT4V) | [Code](https://github.com/InternLM/InternLM-XComposer/tree/main/projects/ShareGPT4V)
  

</details>
<details>
<summary>
<b><b><a href="https://scholar.google.com/scholar?q=SVIT">📄 SVIT</a></b><br>
<code>Paper</code>
</summary>

  - **Data Synthesis Method** (Section 3.2):
      - Uses **GPT-4** to generate large-scale visual instruction data
      - 4.2M dialogues + 1.6M complex reasoning
      - Based on captions from multiple datasets (COCO, VG, CC3M, etc.)
  - **Data Scale**: 5.8M instruction data
  - **Open Source**: ✅ [Dataset](https://huggingface.co/datasets/BAAI/SVIT)
  

</details>
<details>
<summary>
<b><b><a href="https://scholar.google.com/scholar?q=CapsFusion">📄 CapsFusion</a></b><br>
<code>Paper</code>
</summary>

  - **Data Synthesis Method** (Section 3):
      - **Fuses outputs from multiple captioning models** (BLIP-2, CoCa, GPT-4V, etc.)
      - Uses weighted fusion strategy, combining strengths of different models
      - Re-generates captions for DataComp-1B
  - **Data Scale**: Billion-scale recaptioning
  - **Open Source**: ✅ [Code](https://github.com/baaivision/CapsFusion)
  

</details>
<details>
<summary>
<b><b><a href="https://scholar.google.com/scholar?q=Image%20Textualization">📄 Image Textualization</a></b><br>
<code>Paper</code>
</summary>

  - **Data Synthesis Method** - **Automatic Framework for Detailed Image Descriptions**:
      - **Core Innovation**: Maximally converts visual information into text by combining **MLLM understanding** with **vision expert perception**
      - **Three-Phase Pipeline**:
        - **Phase 1 - Holistic Textualization**:
          - Leverage MLLM to create **Reference Description**
          - Provides basic structure for both visual information and linguistic expression
          - Contains the "skeleton" despite lacking details and containing hallucinations
        - **Phase 2 - Visual Detail Textualization**:
          - Use vision expert models (object detection, dense captioning, instance segmentation) to extract **fine-grained object-level information**
          - Extract multiple details from image-side (trained with high-resolution images and object-level annotations)
          - Identify and filter hallucinations in Reference Description
          - Convert perception results into text format
        - **Phase 3 - Textualized Recaptioning**:
          - Integrate visual details with reference description using LLM
          - Produce final high-quality description that is both rich in details and free from hallucinations
      - **Key Advantages**:
        - Addresses MLLM weaknesses: visual hallucination problem and lack of fine-grained details
        - Vision experts provide precise perception (high-res training, object-level annotations)
        - MLLMs provide holistic understanding capabilities
  - **Data Scale**: Creates image description dataset (scale varies by application)
  - **Experimental Results**:
      - LLaVA-7B trained on IT-curated descriptions generates **richer image descriptions**
      - Substantially increases output length and detail with **less hallucination**
      - Comprehensive evaluation on multiple benchmarks verifies description quality
  - **Publication**: arXiv June 2024
  - **Institution**: HKUST, Wuhan University, Zhejiang University, UIUC
  - **Open Source**: ✅ [Code](https://github.com/sterzhang/image-textualization/) | [Dataset](https://huggingface.co/datasets/Sterzhang/image-textualization/)
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2406.08478">📄 Recap-DataComp-1B</a></b><br>
<code>arXiv 2406.08478</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Scale-1B-orange?style=flat-square"/>
</summary>

  - **聚焦**: **LLaMA-3驱动的十亿级图像重新标注** - 使用LLaMA-3-powered LLaVA对DataComp-1B（1.3B图像）进行全量重新标注，生成详细、对齐的caption
  - **数据合成方法** - **训练Captioner + 大规模Recaptioning**:
      - **核心创新**: 首个在**十亿级规模**上使用开源LLaMA-3进行高质量重新标注的工作，填补社区缺口
      - **Stage 1: 训练高性能Captioner**:
        - **模型架构**: LLaVA-1.5框架 + **LLaMA-3-8B**（替代原7B/13B）+ CLIP ViT-L/14（冻结）
        - **训练流程**（2阶段）:
          1. **预训练阶段**: 558K图文对（LAION/CC/SBU）训练2层MLP projection
          2. **指令微调阶段**: 665K instruction数据（LLaVA-1.5）+ **HQ-Edit数据集**微调MLP和LLM
        - **模型性能**:
          - MMMU: 45.2（vs. LLaVA-1.5-7B的33.6，+11.6）
          - MM-Vet: 37.8（vs. LLaVA-1.5-7B的33.9，+3.9）
          - 超越LLaVA-1.5-13B，展现强大视觉理解能力
      - **Stage 2: 大规模Recaptioning**:
        - **数据源**: DataComp-1B（~1.3B web-crawled图文对，已经过安全检查、去重、CLIP过滤）
        - **生成Prompt**: "Please generate a detailed caption of this image. Please be as descriptive as possible."
        - **生成策略**: 贪婪解码，最大128 tokens，自回归生成
        - **输出**: **Recap-DataComp-1B**（1.3B重新标注的图文对）
      - **质量分析**:
        - **长度**: 平均49.43 tokens（vs. 原始10.22，+4.8x）
        - **词汇丰富度**: 覆盖82.86%的词汇，更多样的名词和形容词
        - **语义对齐**:
          - **LongCLIP Score**: 89.91（vs. 原始10.09，**约9倍提升**）
          - 标准CLIP Score: 49.57 vs. 50.43（相当，因CLIP训练于短caption）
        - **人工质量评估（GPT-4V评分）**:
          - 平均评分: 4.14/5（vs. 原始3.71，+0.43）
          - 评估维度：流畅性、准确性、对齐度
  - **实验结果** - **CLIP和DiT模型显著提升**:
      - **CLIP模型**（混合比例p=0.8，80%原始+20%重标注）:
        - **零样本检索**（COCO I→T）: 61.5%（vs. 原始57.3%，+4.2%）
        - **零样本检索**（Flickr30K T→I）: 66.9%（vs. 原始63.0%，+3.9%）
        - **Urban-1K长文本检索**: 85.0% I→T（vs. 原始53.2%，**+31.8%**）
        - **VG-Attribution**: 66.4%（vs. 原始57.1%，+9.3%）
      - **Text-to-Image DiT模型**（混合比例p=0.0，100%重标注）:
        - **FID**: 27.8（vs. 原始36.2，**-8.4**）
        - **CLIP Score**: 32.5%（vs. 原始29.3%，+3.2%）
        - **Recap-CLIP Score**: 28.3%（vs. 原始19.9%，+8.4%）
        - **GPT-4V Score**: 2.53（vs. 原始1.40，+1.1）
      - **关键发现**:
        - **混合策略最优**: 原始+重标注混合训练效果最佳（防止过拟合）
        - **更大文本编码器**: 配合重标注数据，CLIP文本编码器扩大可进一步提升性能
        - **长文本理解**: 重标注显著提升CLIP对长、复杂文本的理解能力
  - **数据规模**:
      - **Recap-DataComp-1B**: 1.3B重新标注的图文对
      - **平均caption长度**: 49.43 tokens（vs. 原始10.22）
  - **开源**: ✅ [项目页面](https://www.haqtu.me/Recap-Datacomp-1B/)
  - **机构**: UC Santa Cruz + University of Edinburgh + JHU + Adobe + UT Austin
  - **发布时间**: arXiv 2024年6月
  - **重要意义**:
      - **开源十亿级重标注**: 首个开源的十亿级高质量重标注数据集，降低社区门槛
      - **LLaMA-3应用**: 展示开源LLM（LLaMA-3）可达GPT-4V级别的标注质量
      - **跨任务泛化**: 同时提升判别式（CLIP）和生成式（DiT）模型性能
      - **长文本理解**: 证明详细caption对长文本检索和属性理解的关键作用
      - **混合策略启发**: 为社区提供原始+合成数据混合训练的最佳实践
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2504.13123">📄 Hunyuan-Recap100M</a></b><br>
<code>arXiv 2504.13123</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Scale-100M-orange?style=flat-square"/>
</summary>

  - **聚焦**: **低幻觉、知识密集型合成caption** - 腾讯混元团队提出的100M级低幻觉caption生成框架，通过连续DPO和知识增强实现高质量重新标注
  - **数据合成方法** - **知识增强SFT + 连续DPO**:
      - **核心创新**: 解决两大痛点：1）降低幻觉（非幻觉率从48.3%提升至77.9%）；2）提升知识密度（整合实体、属性等外部知识）
      - **Stage 1: 知识增强SFT**:
        - **数据生成**（GPT-4o + 人工审核）:
          - **数据源**: CC3M、CC12M、DataComp、Wukong、Wikipedia（采样初始图文对）
          - **GPT-4o Prompt设计**（三步法）:
            1. 准确具体描述图像内容（>50词），避免主观评论
            2. **知识注入**: 参考alt-text/metadata，提取并整合特定实体名、IP名、地名等关键信息（如"埃菲尔铁塔"而非"金属塔"）
            3. 解释修改原因
          - **人工后处理**: 纠正明显错误、确认关键信息包含、过滤噪声
          - **数据规模**: 43,408条高质量标注数据
        - **模型训练**: Qwen2-VL-7B（基座） + LoRA微调
          - 学习率: 1e-5，批大小: 128，训练10 epochs
          - 输出: **Recaption-SFT模型**
      - **Stage 2: 连续DPO（Continuous DPO, CDPO）**:
        - **标准DPO问题**: 在caption任务中，DPO性能在数据规模达到一定程度后plateau（停滞）
        - **CDPO解决方案**（关键创新）:
          - **迭代更新reference model**: 当DPO性能饱和时，用当前policy model更新reference model
          - **重新采样preference data**: 使用更新后的model重新生成preferred/dispreferred pairs
          - **长度平衡**: 对preference pairs进行长度平衡采样，防止length bias
        - **初始DPO阶段**:
          - 采样300K图文对 → SFT模型推理（8次并行，采样参数：top-p=1.0, top-k=20, temp=1.0）
          - 使用内部Critic模型选择best/worst输出构建preference pairs
          - 长度平衡后保留218K高质量pairs
          - 训练初始DPO模型（作为reference）
        - **CDPO阶段**:
          - 采样200K新图文对 → 用初始DPO模型生成新preference data
          - 长度平衡后保留139K pairs
          - 继续训练（1 epoch，学习率5e-6）
        - **效果**:
          - 非幻觉率: 48.33%（Qwen2-VL-7B） → 77.86%（CDPO）
          - 低幻觉率: 87.87% → 98.08%
      - **关键技术优势**:
        - **知识密集**: 整合alt-text中的实体名、专有名词（如"草酸 C2H2O4"）
        - **低幻觉**: CDPO突破DPO plateau，持续降低幻觉
        - **细节丰富**: 平均8.1个视觉细节/caption（vs. Recap-DataComp-1B的6.64）
  - **数据规模**:
      - **Hunyuan-Recap100M**: 100M重新标注的图文对
      - **平均caption长度**: 103.15 tokens（vs. Recap-DataComp-1B的72.60）
      - **平均细节数**: 8.1个视觉细节
      - **非幻觉率**: 77.9%（vs. Recap-DataComp-1B的29.7%）
      - **幻觉率**: 4.2%（vs. Recap-DataComp-1B的24.9%）
  - **实验结果** - **VLM和T2I模型全面提升**:
      - **VLM预训练**（LLaVA架构：SigLIP + Hunyuan-7B）:
        - **15个VL任务**: 平均提升至59.35%（vs. alt-text 53.12%，**+6.2%**）
        - **20个认知域**: 平均准确率53.67%（vs. alt-text 36.33%，**+17.3%**）
        - **幻觉任务**: HallusionBench非幻觉率73.87%（vs. alt-text 68.38%，+5.5%）
        - **细粒度感知**: 在动物、植物、地标等20类视觉对象识别上显著提升
      - **T2I生成**（Hunyuan-DiT微调，2M数据LoRA）:
        - **内部感知测试集**: FID从62.38降至45.33（**-17.1**），CLIP Score从0.323提升至0.357
        - **MSCOCO测试集**: FID从28.79降至15.46（**-13.3**），CLIP Score从0.307提升至0.313
      - **训练效率**: 20M Hunyuan-Recap100M数据训练的模型，在大多数任务上超越其他100M scale数据集训练的模型
  - **质量评估**（基于GPT-4o的CIEM方法）:
      - **vs. Capfusion-120M**: 细节数+267%，长度+3.5x，幻觉率-8.6%
      - **vs. Recap-DataComp-1B**: 非幻觉率+43.6%，幻觉率-19.3%
  - **开源**: ✅ 承诺发布Hunyuan-Recap100M数据集
  - **机构**: Hunyuan Team, Tencent（腾讯混元团队）
  - **发布时间**: arXiv 2025年5月
  - **重要意义**:
      - **低幻觉突破**: 首个系统性解决caption幻觉问题的大规模数据集（非幻觉率77.9%）
      - **CDPO方法论**: 提出连续DPO，突破标准DPO的plateau限制
      - **知识密集**: 创新性地整合外部知识（实体、属性）到caption中
      - **跨任务验证**: 同时在VLM预训练和T2I生成上取得显著提升
      - **工业级规模**: 100M数据规模，展示工业界在合成数据上的探索
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2507.18616">📄 SynC</a></b><br>
<code>arXiv 2507.18616</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
</summary>

  - **聚焦**: **合成数据refinement for零样本图像标注** - 通过one-to-many mapping重新配对caption到最语义对齐的合成图像
  - **数据合成方法** - **One-to-many Mapping + Cycle-Consistency对齐评分**:
      - **核心创新**: 不同于传统pruning或重新生成，SynC专注于**重新分配caption到预生成图像池中最佳匹配的图像**
      - **问题定义**:
        - **传统one-to-one**: 𝑆_One(C_i) = {I_i^syn}（每个caption只对应直接生成的图像）
        - **挑战**: T2I模型常生成语义misalignment图像（缺失对象、错误属性），但caption本身是well-formed的
        - **与Web数据pruning的差异**: Web数据是"noisy text + clean image"，合成数据是"clean caption + noisy image"
      - **One-to-many Selection Strategy (𝑆_T2I)**:
        - **输入**: Caption C_i，预生成合成图像池I^syn
        - **T2I Retrieval**: 使用VLM（SigLIP ViT-B/16）的文本编码器E_T和图像编码器E_I
        - **检索top-K候选**: 𝑅_i = Top-K_j { ⟨E_I(I_j^syn), E_T(C_i)⟩ }（K=15）
        - **输出**: 候选集 {I_r^syn}_r∈R_i，而非仅I_i^syn
        - **优势**: 允许caption从整个图像池中找到更好匹配，而非丢弃misaligned pairs
      - **Cycle-Consistency Alignment Scoring (𝑓_ret)**:
        - **标准CLIP Score局限**: 全局对齐优先，忽略细粒度细节和组合理解
        - **Cycle-Consistency灵感**: T2I检索（选择） + I2T检索（评分）
        - **I2T Retrieval Scoring**:
          1. 对候选图像I^syn执行I2T检索，从caption corpus C中检索top-K_r相似captions
          2. 使用SBERT（Sentence Transformer）计算检索到的captions与原始caption C的文本相似度
          3. 分数: 𝑓_ret(I^syn, C) = max_r∈R̂(I^syn) ⟨E_S(C_r), E_S(C)⟩
        - **核心逻辑**: 如果I^syn真正对齐C，那么从I^syn检索回的captions应与C语义相似
        - **最终选择**: I_i^*syn = argmax_{I^syn∈S(C_i)} f_ret(I^syn, C_i)
      - **Filtering**: 按alignment score排序，保留top τ% pairs（τ∈[0,1]）
  - **实验设置**:
      - **基线模型**: PCM-Net（ECCV 2024）
      - **T2I模型**: Stable Diffusion v1.4（512×512，20 sampling steps）
      - **检索VLM**: SigLIP ViT-B/16@256
      - **文本编码器**: SBERT（unimodal text similarity）
      - **数据源**: CC3M、SS1M生成200K合成pairs
  - **实验结果** - **零样本captioning显著提升**:
      - **COCO Captioning**（ViT-B/32）:
        - BLEU@4: 31.5 → 33.6 (+2.1)
        - CIDEr: 103.8 → 112.0 (+8.2)
        - SPICE: 19.7 → 20.5 (+0.8)
      - **COCO Captioning**（ViT-L/14）:
        - BLEU@4: 33.6 → 35.2 (+1.6)
        - CIDEr: 113.6 → 119.8 (+6.2)
        - SPICE: 20.8 → 21.9 (+1.1)
      - **Flickr30k**（ViT-L/14）:
        - BLEU@4: 28.5 → 29.6 (+1.1)
        - CIDEr: 69.5 → 75.6 (+6.1)
      - **Cross-domain**: COCO→Flickr30k提升CIDEr +4.8，Flickr30k→COCO提升+5.5
      - **NoCaps** (out-of-domain): Entire CIDEr 70.5 → 72.7 (+2.2)
      - **一致性**: 在所有设置（in-domain, cross-domain, out-of-domain）上持续提升
  - **消融研究**:
      - **vs. 传统pruning方法**: SynC超越基于VLM的pruning方法（避免计算开销和公平性问题）
      - **K值影响**: K=15达到最佳平衡
      - **τ值**: 保留top 80-90% pairs效果最优
  - **开源**: ✅ [GitHub](https://github.com/boreng0817/SynC)
  - **机构**: Hanyang University + CJ Group
  - **发布时间**: arXiv 2025年7月
  - **重要意义**:
      - **针对合成数据特性**: 首个专门为"clean caption + noisy image"设计的refinement方法
      - **无需重新生成**: 重用预生成图像池，降低计算成本
      - **Cycle-Consistency**: 双向检索保证细粒度对齐
      - **泛化性强**: 跨域、跨模型一致提升
      - **实用性**: 简单有效，易于集成到现有ZIC pipeline
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2510.27164">📄 High-Res Captioning</a></b><br>
<code>arXiv 2510.27164</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
</summary>

  - **聚焦**：**高分辨率图像精确详细caption生成** - Training-free pipeline，整合VLM+LLM+对象检测系统，解决VLM低分辨率预训练导致的细节丢失
  - **数据合成方法** - **五阶段Caption Refinement Pipeline**：
      - **核心创新**：通过"人类视觉zoom-in"机制和对象检测验证，生成更详细、更可靠的高分辨率图像caption，同时降低幻觉
      - **Stage 1：初始Caption生成**：
        - **VLM生成**：使用VLM（InstructBLIP/LLaVA-v1.5/Qwen2-VL）生成初始caption
        - **Prompt**： "Describe this image in detail."
        - **问题**：VLM通常在低分辨率预训练（224×224或336×336），高分辨率图像降采样丢失细节
        - **LLM提取关键对象**：使用GPT-4o从初始caption中提取关键对象列表
      - **Stage 2：识别潜在共现对象**：
        - **LLM推理**：基于关键对象，LLM利用世界知识推断可能共同出现但被遗漏的对象
        - **示例**：若关键对象是"table, chair"，LLM推断可能存在"lamp, books, cup"
        - **输出**：扩展候选对象列表（原始+新提议）
      - **Stage 3：对象存在性验证**：
        - **三检测器Ensemble**：GroundingDINO + YOLO-World + OWLv2
        - **验证策略**：
          - 对象被检测：三个检测器总置信度≥0.5（IoU≥0.7视为同一对象）
          - 对象未检测：任何检测器都未检测到 → 从初始caption中移除（降低幻觉）
        - **输出**：验证对象列表 + 边界框坐标
      - **Stage 4：新对象详细Captioning（Zoom-in机制）**：
        - **裁剪边界框**：为新检测但初始caption未提及的对象裁剪图像区域
        - **重新Captioning**：将裁剪图像输入VLM，生成详细对象描述
        - **模拟人类视觉**：类似人类放大观察高分辨率图像细节的过程
        - **效率优化**：仅对初始caption缺失的对象执行，已描述对象假定足够详细
      - **Stage 5：最终Caption重新措辞**：
        - **GPT-4o整合**：结合初始caption + 验证对象列表+坐标 + 新详细描述
        - **双重目标**：
          1. **移除幻觉**：删除未检测对象的引用
          2. **添加新信息**：整合新检测对象的详细描述和空间上下文
        - **空间上下文**：使用相对位置（"on the left", "in the foreground", "near the center"）
        - **格式**：{label}: {caption} at coordinates (x_min, y_min, x_max, y_max)
        - **自然流畅**：整体重新措辞而非简单拼接，保持语义连贯性
  - **实验设置**：
      - **VLMs**：InstructBLIP（224×224）、LLaVA-v1.5（336×336）、Qwen2-VL（动态分辨率）
      - **LLM**：GPT-4o（提取、推理、重新措辞）
      - **检测器**：GroundingDINO, YOLO-World, OWLv2（开放词汇）
      - **评估模型**：LLaMA-3.2-Vision-Instruct（1120×1120，reference-free评估）
      - **数据集**：Objects365中筛选的266张4K图像（3840×2160），标准：≥15类对象、≥10小对象、≥5人
  - **实验结果** - **Caption质量与幻觉双重提升**：
      - **Pairwise比较（Winning Rate）**：
        - InstructBLIP: ~55% winning rate（vs. 初始caption）
        - LLaVA-v1.5: ~58% winning rate
        - Qwen2-VL: ~52% winning rate（已较强但仍有提升）
      - **定量评分（0-1范围，5次实验平均）**：
        - InstructBLIP: 0.6344 → 0.6952 (**+9.59%**)
        - LLaVA-v1.5: 0.6785 → 0.7304 (**+7.66%**)
        - Qwen2-VL: 0.8260 → 0.8398 (**+1.68%**，动态分辨率已较robust）
      - **POPE幻觉基准（Accuracy/Precision/Recall/F1，平均提升）**：
        - **Random采样**：
          - InstructBLIP: Acc +4.87%, Prec +24.16%, Recall +50.15%, F1 **+45.10%**
          - LLaVA-v1.5: Acc +5.30%, Prec +22.23%, Recall +24.31%, F1 +23.88%
          - Qwen2-VL: Acc +2.62%, Prec +13.70%, Recall +24.90%, F1 +22.97%
        - **Popular采样**：
          - InstructBLIP: F1 +28.71%, LLaVA-v1.5: F1 +20.32%, Qwen2-VL: F1 +23.84%
        - **Adversarial采样**：
          - InstructBLIP: F1 +28.85%, LLaVA-v1.5: F1 +20.59%, Qwen2-VL: F1 **+29.44%**
      - **一致性**：对预训练分辨率较低的VLM提升更显著，证明方法针对"resolution curse"的有效性
  - **开源**：✅ （论文承诺发布代码和prompts）
  - **机构**：University of Seoul + POSTECH + Yonsei University
  - **发布时间**：arXiv 2025年10月
  - **重要意义**：
      - **无需重新训练**：Training-free pipeline，适用于任何VLM
      - **人类视觉模拟**：Zoom-in机制首次系统性地模拟人类观察高分辨率图像的过程
      - **双重优化**：同时提升caption详细度（新对象）和准确性（移除幻觉）
      - **Ensemble检测**：三检测器ensemble降低单模型偏差，提升验证可靠性
      - **高分辨率针对性**：明确解决VLM在4K/高分辨率图像上的性能退化问题
      - **工作流通用**：可扩展至多模态检索、T2I生成、VQA等下游任务
  

</details>
<details>
<summary>
<b><b><a href="https://scholar.google.com/scholar?q=LLaVAR">📄 LLaVAR</a></b><br>
<code>Paper</code>
</summary>

  - **Data Synthesis Method** (Section 3.2):
      - Targets text-rich images (documents, posters, charts, etc.)
      - Uses **GPT-4** to generate instruction Q&A pairs based on OCR results
      - Generates "understanding + reasoning" type questions (not just reading text)
  - **Data Scale**: 422K instruction data
  - **Open Source**: ✅ [Code](https://github.com/SALT-NLP/LLaVAR)
  

</details>
<details>
<summary>
<b><b><a href="https://scholar.google.com/scholar?q=ALLaVA">📄 ALLaVA</a></b><br>
<code>Paper</code>
</summary>

  - **Data Synthesis Method** (Abstract explicitly describes):
      - **Captioning-then-QA paradigm**: Two-stage data generation
      - Uses **GPT-4V** to generate two types of data:
        a) **Fine-grained image annotations** for vision-language alignment
        b) **Complex reasoning visual QA pairs** for visual instruction fine-tuning
      - Complete data generation pipeline, utilizing powerful proprietary models to synthesize high-quality data
  - **Data Scale**: 1.3M samples
  - **Experimental Results**: Achieves competitive performance among 4B models, even on par with 7B/13B models on various benchmarks
  - **Open Source**: ✅ Dataset open-sourced (mentioned in paper)
  

</details>
<details>
<summary>
<b><b><a href="https://scholar.google.com/scholar?q=COGS">📄 COGS</a></b><br>
<code>Paper</code>
</summary>

  - **Data Synthesis Method** (Abstract explicitly describes):
      - **Composition-Grounded Instruction Synthesis**
      - Starts from **small set of seed questions**, generates large-scale data through decomposition-recomposition:
        a) **Decompose**: Breaks seed questions into primitive perception and reasoning factors
        b) **Recompose**: Systematically recombines factors with new images
        c) **Generate**: Creates large collections of synthetic Q&A pairs, each paired with subquestions and intermediate answers
      - Supports reinforcement learning with factor-level process rewards
  - **Application Domains**: Charts, webpages, rendered documents, and other artificial image domains
  - **Experimental Results**: Substantial improvements on unseen questions, largest gains on reasoning-heavy and compositional questions, good transfer across datasets
  - **Publication**: arXiv October 2025
  - **Institution**: MIT, IBM Research, etc.
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2402.12226">📄 AnyGPT</a></b><br>
<code>arXiv 2402.12226</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-复旦大学-red?style=flat-square"/>
</summary>

  - **聚焦**: **Any-to-Any多模态对话数据合成** - 使用生成模型创建大规模任意模态到任意模态（文本、语音、图像、音乐）的多轮对话数据集
  - **数据合成方法** - **两阶段GPT-4引导 + 多模态生成Pipeline**:
      - **核心创新**: 首个大规模any-to-any多模态指令数据集，使用离散表示统一处理多种模态，通过生成模型自动构建交织多模态元素的对话
      - **问题识别**:
        - 缺乏大规模多模态交织指令跟随数据
        - 现有数据集模态组合有限（通常只有图像+文本）
        - 缺少音频模态（语音、音乐）的多模态对话数据
      - **两阶段数据构建Pipeline（AnyInstruct-108k）**:
        1. **文本对话生成阶段（Stage 1）**:
           - **话题池构建**:
             - 准备100个元话题（meta topics）
             - 使用GPT-4对每个元话题生成200个具体话题（4轮brainstorming）
             - 总共20,000个话题涵盖多个领域
           - **场景构建**:
             - 基于话题，GPT-4生成对话场景描述
             - 场景要求：用户与聊天机器人之间的非学术对话
             - 对话中可以使用图像或音乐传达信息（不包括视频）
             - 图像不能是图表或名作（避免版权问题）
           - **对话生成**:
             - 使用GPT-4基于场景生成多轮对话文本
             - 对话格式：用户和AnyGPT交替发言
             - 多模态元素以文本描述形式嵌入：`[image: description]`, `[music: description]`
             - 约束条件：
               - 每个utterance 5-15个词，简洁明了
               - 用户utterance必须是问题或指令
               - 对话保持2-3轮
               - 每个对话包含1个音乐，最多2个图像
             - 音乐描述要求：聚焦流派、风格、乐器，避免提及具体曲目
        2. **文本到多模态转换阶段（Stage 2）**:
           - **图像合成**:
             - 模型：**Stable Diffusion XL (SDXL)**
             - 输入：对话中的图像描述文本`[image: description]`
             - 输出：高质量合成图像
             - 替换对话中的文本描述为实际图像
           - **音乐合成**:
             - 模型：**MusicGen**
             - 输入：对话中的音乐描述文本`[music: description]`
             - 输出：5秒音频片段
             - 替换对话中的文本描述为实际音乐
           - **语音合成**:
             - 模型：**Azure Text-to-Speech API (Microsoft)**
             - 输入：用户指令和模型的文本回复
             - 输出：自然语音
             - 为对话添加语音模态
           - **质量过滤**:
             - 过滤低质量生成结果
             - 确保图像-文本对齐、音乐-描述匹配
        3. **额外语音对话增强**:
           - 从现有纯文本指令数据集中提取适合口语叙述的对话
           - 使用TTS模型转换为100K语音对话
           - 增强语音模态数据规模
      - **关键技术优势**:
        - **完全合成**: 所有视觉和音频内容均由生成模型创建，无需人工标注
        - **模态多样性**: 同时包含文本、图像、语音、音乐四种模态
        - **任意组合**: 支持任意模态输入到任意模态输出的对话
        - **自动化**: GPT-4引导的端到端自动化生成流程
        - **可扩展性**: 话题池和场景可灵活扩展，生成模型可替换
  - **AnyInstruct-108k数据集**:
      - **总规模**: 108K多轮多模态对话
      - **多模态元素统计**:
        - 图像：205K张合成图像
        - 语音：503K语音录音
        - 音乐：113K音乐片段
      - **对话特点**:
        - 多轮交互（2-3轮）
        - 交织多种模态（文本+图像+语音+音乐）
        - 任意模态组合（如：语音指令+图像 → 文本+音乐+语音回复）
      - **话题覆盖**: 涵盖游戏、环境、艺术、科技、生活等多个领域
  - **AnyGPT模型**:
      - **架构**:
        - 基础：LLaMA-2 7B
        - 多模态Tokenizers：SEED（图像）、SpeechTokenizer（语音）、MusicTokenizer（音乐）
        - 统一词汇表：将所有模态转换为离散tokens
      - **训练**:
        - 预训练：多模态对齐（图像-文本、语音-文本、音乐-文本）
        - 指令微调：在AnyInstruct-108k上微调
      - **能力**: 任意模态输入到任意模态输出的对话生成
  - **实验结果** - **零样本性能接近专用模型**:
      - **图像理解**:
        - MS-COCO Captioning: CIDEr **82.3**（接近Flamingo-9B的79.4）
      - **图像生成**:
        - MS-COCO Text-to-Image: CLIPScore **0.65**（与SEED-LLaMA相当）
      - **语音识别（ASR）**:
        - LibriSpeech: WER **8.5**（接近人类水平5.8，专用模型2.7）
      - **语音合成（TTS）**:
        - VCTK: WER **8.5**, Speaker Similarity **0.77**
      - **音乐理解与生成**:
        - MusicCaps: CLAPScore **0.11**（音乐理解）、**0.14**（音乐生成）
      - **Any-to-Any对话**: 成功处理任意模态组合的输入和输出，展示流畅的多模态交互能力
  - **消融研究关键发现**:
      - 离散表示能有效统一多种模态
      - 多模态预训练对齐至关重要
      - AnyInstruct-108k显著提升any-to-any对话能力
  - **机构**: 复旦大学、Multimodal Art Projection Research Community、上海人工智能实验室
  - **作者**: Jun Zhan, Junqi Dai, Jiasheng Ye, Yunhua Zhou, Dong Zhang, Zhigeng Liu, Xin Zhang, Ruibin Yuan, Ge Zhang, Linyang Li, Hang Yan, Jie Fu, Tao Gui, Tianxiang Sun, Yu-Gang Jiang, Xipeng Qiu
  - **发布时间**: arXiv 2024年2月（v5）
  - **论文链接**: [arXiv:2402.12226](https://arxiv.org/abs/2402.12226)
  - **开源**: ✅ [项目主页](https://junzhan2000.github.io/AnyGPT.github.io/)
  - **意义**:
      - **数据贡献**: 首个大规模any-to-any多模态指令数据集，填补音频模态对话数据空白
      - **生成式方法**: 使用生成模型创建完全合成的多模态对话数据，避免隐私和版权问题
      - **模态统一**: 证明离散表示可以有效统一多种模态（文本、图像、语音、音乐）
      - **可扩展性**: 两阶段pipeline可轻松扩展到更多模态或更大规模
      - **零样本能力**: 证明在合成数据上训练的模型可以获得接近专用模型的零样本性能
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2403.03194">📄 MAGID</a></b><br>
<code>arXiv 2403.03194</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**: **多模态对话数据自动生成** - 将text-only对话自动增强为多模态对话（文本+图像）
  - **问题背景**:
      - **现有方法局限**: 检索式方法（从固定图像库检索）导致图像多样性受限、匹配度低
      - **数据稀缺**: 多模态对话数据难以获取，隐私和质量问题严重
      - **单图限制**: 现有数据集通常每对话只有一张图像
  - **数据合成方法** - **生成式多模态对话Pipeline + 质量保证模块**:
      - **核心创新**: 从text-only对话出发，使用LLM识别需要图像的utterances，使用扩散模型生成图像，配合反馈循环确保质量
      - **三大核心模块**:
        1. **LLM-based Scanner（扫描器）**:
           - **任务**: 识别对话中需要图像的utterances，并生成图像描述
           - **输入**: Text-only对话
           - **输出**: 选定的utterances + 对应的图像描述
           - **Prompt工程**: 测试三种策略
             - **Zero-shot**: 仅提供格式和问题描述
             - **Few-shot**: 提供输入-输出示例
             - **Chain-of-Thought (CoT)**: 提供推理步骤（最优选择）
           - **输出格式控制**: 使用HTML-like标签（`<result>` 和 `<reason>`）结构化输出
           - **关键**: CoT提供可调试的推理路径，避免上下文不一致（如"give it a look"生成无意义图像）
        2. **Diffusion-based Image Generator（图像生成器）**:
           - **模型选择**: Stable Diffusion XL 1.0（SDXL）
           - **优势**: 在数十亿图像上训练，生成多样化、高质量图像
           - **输入**: LLM生成的图像描述
           - **输出**: 合成图像
           - **关键**: 超越检索式方法的多样性瓶颈
        3. **Quality Assurance Module（质量保证模块）**:
           - **三大评估维度**:
             a) **Image-Text Matching（图文匹配）**:
                - 使用CLIP score验证图像与utterance的匹配度
                - 低分触发重新生成（最多2次）
             b) **Image Quality（图像质量）**:
                - 使用aesthetic score（基于CLIP embedding + MLP）
                - 检测扩散模型artifacts
                - 阈值：0.51（有效检测大部分artifacts）
             c) **Image Safety（图像安全）**:
                - NSFW内容检测
                - 数据集中极少发现不安全图像，验证pipeline可靠性
           - **反馈循环**: 若图像不满足标准，回到LLM重新生成图像描述
      - **关键技术优势**:
        - **生成式而非检索式**: 图像多样性不受限于图像库大小
        - **自动化**: 完全自动化pipeline，无需人工标注
        - **质量保证**: 多维度质量控制确保数据可用性
        - **多图像支持**: 不限制每对话只有一张图像
        - **隐私友好**: 不依赖真实用户数据
  - **数据规模**:
      - **MAGID数据集**: Medium-sized dataset（论文作为概念验证）
      - **来源**: Text-only对话数据集（如DailyDialog等）
  - **实验结果** - **自动化和人工评估**:
      - **定量评估**:
        - 在3个对话数据集上与SOTA baselines对比
        - 使用自动指标（CLIP score、FID等）
      - **人工评估**:
        - MAGID显著优于检索式baseline（特别是图像库小时）
        - 图像-对话一致性评分高
        - 图像质量和多样性获得高分
      - **消融研究**:
        - CoT prompting优于zero-shot和few-shot
        - 质量保证模块对最终数据质量至关重要
        - 反馈循环有效提升图像-文本对齐
  - **发布时间**: arXiv 2024年3月
  - **机构**: AWS AI Labs, University of Waterloo
  - **作者**: Hossein Aboutalebi, Hwanjun Song, Yusheng Xie, Arshit Gupta等
  - **开源**: ✅ [代码](https://github.com/amazon-science/MAGID)
  - **重要意义**:
      - **范式转变**: 从检索式到生成式多模态对话数据构建
      - **质量保证设计**: 多维度质量控制+反馈循环的系统化设计
      - **解决实际挑战**: 应对隐私、多样性、质量三大挑战
      - **可扩展性**: 自动化pipeline易于扩展到大规模
      - **多图像对话**: 支持per conversation多张图像，更贴近真实场景
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2412.14475">📄 MegaPairs</a></b><br>
<code>arXiv 2412.14475</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**: **通用多模态检索器的大规模数据合成** - 利用异构KNN三元组和开放指令生成实现可扩展的多模态检索训练数据构建
  - **数据合成方法** - **异构相似性挖掘 + MLLM/LLM标注Pipeline**:
      - **核心创新**: 使用**多种相似性模型**从开放域图像语料中挖掘多样化图像对，配合MLLM/LLM生成开放式检索指令
      - **两阶段Pipeline**:
        1. **异构图像对挖掘**（多样性关键）:
           - **三类相似性模型并行检索**:
             - a) **视觉-语义相关性**（EVA-CLIP图像编码器）: 捕获语义相关性，忽略视觉相似性（如同一汽车的不同视角）
             - b) **视觉-模式相关性**（DINOv2）: 捕获视觉相似性，忽略语义相关性（如相似背景中的不同汽车）
             - c) **Caption相关性**（EVA-CLIP文本编码器）: 基于图像配对caption的文本相似性
           - **相似度过滤**: 保留分数在(0.8, 0.96)区间的图像对，消除弱关联和近重复
           - **硬负样本**: 从检索集合中自动引入硬负样本（其他检索到的非目标图像）
           - **规模**: 从RecapDataComp-1B的2000万图像子集中挖掘关系
        2. **开放式指令生成**（基于MLLM/LLM）:
           - **关系描述生成**（InternVL2-26B）:
             - 输入图像对(Iq, Iti)
             - MLLM生成详细描述Di，说明两图像的共同概念和差异
             - 捕获视觉和语义关系
           - **指令合成**（LLaMA3-8B）:
             - LLM基于描述Di生成多样化文本指令Tq→ti
             - 每个图像对生成至少3条不同指令
             - 指令设计为开放式搜索查询（如"显示汽车内部"）
           - **最终三元组**: (Iq, Tq→ti, Iti) + 5个硬负样本
      - **关键优势**:
        - **可扩展性**: 利用通用图像语料（不依赖多图像网页），规模无限扩展
        - **质量保证**: 相似度过滤 + MLLM/LLM标注确保高质量
        - **多样性**: 三类异构相似性引入不同类型的图像关系
        - **低成本**: 使用开源MLLM/LLM（InternVL2-26B, LLaMA3-8B）
  - **数据规模**:
      - **MegaPairs**: 2623.5万图像对
      - **源语料**: RecapDataComp-1B的2000万图像子集
      - **指令多样性**: 每对至少3条指令
      - **硬负样本**: 每个查询5个硬负样本
  - **模型**: **MMRet系列** - 基于MegaPairs训练的通用多模态检索器
      - **MMRet-Base**: CLIP-B架构（149M参数）
      - **MMRet-Large**: CLIP-L架构（428M参数）
      - **MMRet-MLLM**: LLaVA-1.6 Mistral 7B架构（7.57B参数）
  - **实验结果** - **SOTA零样本性能**:
      - **组合图像检索（CIR）基准**（4个主流基准）:
        - **CIRCO**（主基准）:
          - MMRet-MLLM: **42.2% mAP@5**（超越之前SOTA CoCa-based MagicLens-L的34.1%，**+8.1%**）
          - MMRet-Large: **39.2% mAP@5**（CLIP-L规模SOTA）
          - MMRet-Base: **34.3% mAP@5**（超越大多数更大模型）
        - **CIRR测试集**:
          - MMRet-MLLM: **46.7% R@1, 75.4% Rs@1**（超越SOTA **+7.4% R@1, +4.5% Rs@1**）
          - MMRet-Large: **38.0% R@1**（CLIP-L规模SOTA）
        - **FashionIQ**: MMRet-MLLM **35.6% R@10**
        - **GeneCIS**: MMRet-MLLM **21.1% Rs@1**（超越SOTA **+3.7%**）
      - **MMEB基准**（36个数据集，4类元任务）:
        - **零样本总分**: MMRet-MLLM **44.0%**（SOTA，超越UniIR的42.8%）
        - **分类任务**: 47.2%
        - **VQA任务**: 18.4%
        - **检索任务**: 56.5%（显著优于其他方法）
        - **视觉定位**: 62.2%
      - **监督微调性能**（MMEB）:
        - **总分**: **64.1%**（超越VLM2Vec Phi-3.5-V的60.1%）
        - **IND数据集**: 68.0%
        - **OOD数据集**: 59.1%（强泛化能力，超越VLM2Vec LLaVA-1.6 **+7.1%**）
  - **数据质量验证**:
      - **数据效率**: 仅**50万MegaPairs样本**即超越MagicLens在**3670万数据**上的训练结果（**数据量1/70**）
      - **可扩展性**: 性能随数据规模持续提升（从128K到26M）
      - **异构策略效果**: 同时使用三类相似性优于单一策略（消融研究验证）
      - **硬负样本重要性**: 包含硬负样本显著提升性能（+5-10%跨基准）
  - **发布时间**: arXiv 2024年12月
  - **机构**: 北京邮电大学、北京智源人工智能研究院、中国科学技术大学、上海交通大学、香港理工大学
  - **作者**: Junjie Zhou, Zheng Liu, Ze Liu, Shitao Xiao等
  - **开源**: ✅ **完全开源** - 数据集、模型、数据合成pipeline均将公开
  - **重要意义**:
      - **突破数据瓶颈**: 首次实现从通用图像语料大规模合成多模态检索数据
      - **质量优于规模**: 证明高质量合成数据比大规模低质量数据更有效
      - **异构相似性创新**: 多类型相似性挖掘引入多样化图像关系
      - **开源生态贡献**: 完整开源数据、模型、pipeline，推动领域发展
      - **通用检索能力**: 在CIR和广泛多模态任务上均达到SOTA
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2410.11963">📄 CtrlSynth</a></b><br>
<code>arXiv 2410.11963</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**: **可控图像-文本合成管道** - 通过视觉标签的分解-重组实现细粒度控制的多模态数据生成
  - **数据合成方法** - **分解-重组范式的可控数据合成**:
      - **核心创新**: 将图像语义分解为基本元素（对象、属性、关系），通过用户定义的控制策略操作，再重组生成合成数据
      - **三大核心组件**:
        1. **视觉标记模型（VTM）**:
           - 提取图像的基本视觉元素（**视觉标签**）
           - **对象和属性**: 使用多标签分类器（CatLIP-Huge）+ 顶级20类sigmoid预测
           - **关系**: 使用多模态标注模型（Florence-large）生成详细描述 + LLM（Qwen2-7B）提取关系
           - **混合方法**: 结合CatLIP的对象/属性预测与Florence+LLM的关系提取，形成全面的视觉标签集
        2. **文本控制器**:
           - 接受视觉标签 + 用户策略 + 可选原始文本
           - 生成文本合成指令引导LLM
           - **三类预定义策略**:
             - a) **编辑视觉标签**（删除、添加、替换）实现细粒度内容控制
             - b) **约束语义含义**改进噪声标注的忠实度
             - c) **风格化输出**（如JSON格式）提升下游可用性
           - **10个文本控制策略**用于caption合成（详见论文附录A.1）
        3. **图像控制器**:
           - 接受文本提示 + 用户策略
           - 输出图像合成指令引导扩散模型
           - **两类策略**:
             - 标签权重调整（突出特定对象/属性）
             - 风格提示（电影感、真实感、艺术风格）
      - **灵活的合成路径**（支持4条主要路径）:
        - **SP(1) 图像→文本**: 原始图像 → VTM → 视觉标签 → 文本控制器 → LLM → 合成文本
        - **SP(2) 图像+原始文本→改进文本**: 包含原始标注作为约束，生成忠实的改进文本
        - **SP(3) 图像→文本+图像**: 生成文本 → 图像控制器 → 扩散模型 → 合成图像+文本对
        - **SP(4) 文本→图像**: 原始文本 → 图像控制器 → 扩散模型 → 合成图像
      - **闭环自过滤机制**:
        - **质量验证**: 检查合成文本是否包含至少比例pf的视觉标签（默认20%）
        - **图像验证**: 合成图像通过VTM再次提取标签，验证与源文本的对齐
        - **优势**: 无需手工规则即可自动过滤低质量样本
      - **关键技术优势**:
        - **细粒度可控性**: 通过标签级操作实现精确数据合成
        - **无训练**: 完全利用预训练模型（LLM、扩散模型），无需额外训练
        - **模块化**: 可轻松替换LLM、扩散模型或VTM组件
        - **闭环设计**: 自动质量验证和过滤能力
  - **数据规模**:
      - **CC3M合成数据**:
        - CtrlSynth-cap: 260万captions（从280万原始数据过滤）
        - CtrlSynth-img: 240万图像
        - CtrlSynth-mix: 510万图像-文本对（混合cap+capimg）
      - **CC12M合成数据**:
        - CtrlSynth-cap: 1020万captions（从1130万原始数据）
        - CtrlSynth-img: 950万图像
        - CtrlSynth-mix: 1970万图像-文本对
  - **实验结果** - **在CLIP预训练上的全面评估**:
      - **零样本分类**（31个数据集）:
        - CC3M训练: 平均准确率从19.4%提升至**27.1%（+7.7%）**
        - CC12M训练: 从33.9%提升至**36.6%（+2.5%）**
        - ImageNet变体: 从11.3%提升至**20.7%（+9.4%）** [CC3M]
      - **图像-文本检索**（COCO、Flickr30k）:
        - CC3M训练: recall@1从13.7%提升至**37.1%（+23.4%）**
        - Flickr I2T: 从21.3%提升至**57.3%（+36%）**
        - CC12M训练: recall@1从45.4%提升至**54.4%（+9.0%）**
      - **组合推理**（SugarCrepe基准）:
        - CC3M训练: 从64.0%提升至**68.5%（+4.5%）**
        - CC12M训练: 从72.3%提升至**75.3%（+3.0%）**
        - **突出提升**: REPLACE关系 +4.3%，SWAP属性 +14.8%
      - **长尾任务性能**:
        - **ImageNet-LT**: 尾类准确率+21.3%，整体+5.4%
        - **Places-LT**: 尾类准确率+16.2%，整体+3.7%
      - **与先前工作对比**:
        - 超越**VeCLIP**: 在VTAB上平均+4.8%，ImageNet 1K上+7.9%
        - 超越**LaCLIP**: 在15个数据集上平均+3.4%，ImageNet 1K上+2.3%
  - **消融研究关键发现**:
      - **视觉关系的重要性**: 包含关系标签比仅对象/属性提升4%组合推理性能
      - **混合LLM效果**: Mistral-NeMo优于Qwen2-7B（+3% SugarCrepe）
      - **过滤阈值**: 20%达到最佳性能平衡（10%-30%范围内稳定）
      - **混合比例**: 50%合成数据达到最佳增益，更高比例收益递减
      - **数据效率**: 合成数据使CLIP训练效率提升40%（达到20%准确率所需迭代数）
  - **合成质量分析**:
      - **文本长度**: 合成caption平均60词 vs 原始8词
      - **信息密度**: 包含更丰富的视觉细节和关系描述
      - **多样性**: 通过控制策略生成多样化表述
  - **发布时间**: arXiv 2024年10月
  - **机构**: Apple、Meta
  - **作者**: Qingqing Cao, Mahyar Najibi, Sachin Mehta
  - **开源**: ⚠️ 论文未明确提及数据集/代码开源状态
  - **重要意义**:
      - **首个可控图文合成系统**: 提供细粒度控制而非黑盒生成
      - **分解-重组范式**: 创新的视觉语义操作方法
      - **闭环自验证**: 无需人工设计过滤规则
      - **跨任务泛化**: 在分类、检索、组合推理、长尾任务上全面提升
      - **数据效率**: 证明合成数据的样本效率优于纯真实数据扩展
  
  #### 🛠️ 工具辅助标注生成（用于数据合成）
  
  > 以下工具常用于数据合成pipeline
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2405.02793">📄 ImageInWords</a></b><br>
<code>arXiv 2405.02793</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-ECCV_2024-red?style=flat-square"/>
</summary>

  - **聚焦**: **超详细图像描述生成** - Human-in-the-loop框架，结合VLM种子生成和顺序人工增强，生成高质量hyper-detailed图像描述
  - **数据合成方法** - **种子标注 + 顺序增强 + 主动学习**:
      - **核心创新**: 结合VLM生成的**种子元数据**与**人工标注者的不可替代质量**，通过顺序迭代和主动学习循环生成超详细图像描述
      - **两任务框架**:
        1. **Task 1: 对象级描述**（细粒度标注）:
           - **输入**: 图像 + 对象检测(OD)模型生成的(label, bbox)
           - **VLM种子生成**: 使用PaLI-35B为每个bbox生成对象级caption
           - **人工增强**: 众包工作者修正、添加、删除、合并对象标注
           - **输出**: (label, bbox, 详细对象描述)三元组，涵盖所有显著对象
        2. **Task 2: 图像级描述**（全局描述）:
           - **输入**: Task 1的对象描述 + VLM生成的全局种子caption + 可选领域特定元数据（如艺术风格）
           - **顺序增强**: 多个众包工作者依次增强和改进描述（通常3轮）
           - **主动学习**: 每收集1K样本后，使用新数据重新微调PaLI-35B，改进种子质量
           - **输出**: 217.2 tokens平均长度的hyper-detailed描述
      - **顺序增强优势**（Fig. 2）:
        - **效率提升**: 3个标注者顺序工作 vs 并行工作
          - **Token增长**: +20% token count（从170→204词）
          - **时间节省**: -30% 时间（从800秒→560秒/标注者）
          - **质量提升**: Jaccard相似度从0.2提升至0.65（round 1-2 → round 2-3）
        - **隐式学习循环**: 标注者互相学习，个体质量持续提升
      - **主动学习循环**:
        - **初始PaLI**: 平均生成15词caption
        - **3K样本后**: 提升至150+词caption
        - **关键作用**: 显著降低人工标注负担
      - **标注指南**（详见论文Appendix A）:
        - **TLDR原则**: 首句必须是报纸风格的简洁总结
        - **显著性顺序**: 按对象显著性顺序描述，而非随机顺序
        - **视觉准确**: 仅包含视觉可推断的细节，避免猜测
        - **全面覆盖**: 包括设置、背景、风格、相机角度、整体构图、渲染文本
        - **特别关注**: 人物、服饰、艺术作品、地点特定属性、独特属性
      - **关键技术优势**:
        - **种子标注**: 显著降低从零开始的标注成本和时间
        - **顺序增强**: 比并行标注更高效，同时产生单一高质量输出
        - **主动学习**: 持续改进VLM种子质量，减少人工负担
        - **质量保证**: 多轮迭代 + n-gram Jaccard相似度监控确保收敛
  - **数据规模**:
      - **IIW数据集**: 9,018张图像（训练: 8,573，测试: 445）
      - **平均统计**:
        - **Tokens**: 217.2 (vs DOCCI 135.7, DCI 148.0)
        - **Sentences**: 9.8
        - **Nouns**: 52.5 (vs DOCCI 34.0, DCI 35.3)
        - **Adjectives**: 28.0 (vs DOCCI 16.6, DCI 16.3)
        - **Verbs**: 19.1 (vs DOCCI 9.6, DCI 10.5)
      - **图像来源**: WebLI-like数据集采样
      - **标注池**: 20+领域专家（创意写作、艺术、历史、摄影背景）
  - **实验结果** - **人工SxS评估优势显著**:
      - **IIW人工标注 vs 先前数据集**（Table 2）:
        - **vs DCI（112测试样本）**:
          - Comprehensiveness（全面性）: +61%
          - Specificity（具体性）: +80%
          - Hallucinations（更少幻觉）: -42%
          - TLDR质量: +91%
          - Human-Likeness（类人性）: +82%
        - **vs DOCCI（100测试样本）**:
          - Comprehensiveness: +42%
          - Specificity: +82%
          - Hallucinations: -35%
          - TLDR质量: +79%
          - Human-Likeness: +68%
        - **平均提升**: +66%（5项指标平均，两数据集平均）
      - **IIW人工标注 vs GPT-4V**（Table 3右侧）:
        - **100样本对比**:
          - Comprehensiveness: +35%
          - Specificity: +53%
          - Hallucinations: -59%
          - TLDR质量: +70%
          - Human-Likeness: +21%
        - **平均提升**: +48%
      - **IIW模型（微调PaLI-35B）vs 其他数据集微调模型**（Table 3左侧）:
        - **vs DCI模型**: +42% Comprehensiveness, +54% Specificity, +51% TLDR
        - **vs DOCCI模型**: +4% Comprehensiveness, +37% Specificity, +57% TLDR
        - **平均提升**: +31%（5项指标平均，两数据集平均）
  - **下游应用评估**:
      - **Text-to-Image重建**（Table 4, 240张LocNar图像）:
        - 使用Imagen模型，按句子累积输入（S1, S1-2, S1-3...）
        - **Mean Rank**: IIW 1.63 vs DOCCI 1.74 vs DCI 2.05（**第1名**）
        - **CLIP相似度**: IIW 0.861 vs DOCCI 0.853 vs DCI 0.844（**最高**）
        - **关键发现**: 即使仅用第1句，IIW也优于其他数据集
      - **组合推理**（Table 5，LLM-only设置）:
        - 使用IIW描述替换ARO/SVO-Probes/Winoground中的图像，LLM判断
        - **ARO VG-Attribution**: 90.37%（vs InstructBLIP 83.99%, LLaVA 84.80%, **+6%**）
        - **ARO VG-Relation**: 66.19%（vs InstructBLIP 62.73%, LLaVA 63.71%, **+2-3%**）
        - **Winoground**: 69.38%（vs InstructBLIP 65.25%, LLaVA 63.38%, **+4-6%**）
  - **IIW-Eval基准**（Table 6）:
      - **2,612张图像** + **1,899个对象级标注** + **2,712个图像级标注**
      - **412个人工SxS标签**（IIW vs DCI, IIW vs DOCCI）
      - **IIW-400**（400张新评估集）+ DCI测试集（112）+ DOCCI测试集（100）
      - **模型enriched数据集**: LocNar（1,000）+ XM3600（1,000）使用IIW模型重新标注
  - **消融研究关键发现**:
      - **种子标注重要性**（Table 7）: 有种子 vs 无种子 = +54% Comprehensiveness, +48% Specificity
      - **IIW人工 vs IIW模型**（Table 8，100样本）: 人工仍显著更优（+78% Compr., +91% Spec.）
      - **顺序轮数**: 3轮达到0.8相似度阈值，后续轮数收益递减
  - **发布时间**: ECCV 2024 | arXiv 2024年5月（v2: 2024年10月）
  - **机构**: Google DeepMind, Google Research, University of Washington
  - **作者**: Roopal Garg, Andrea Burns, Burcu Karagol Ayan, Yonatan Bitton等
  - **开源**: ✅ **完全开源** - IIW-Eval基准（2.6K图像）、人工SxS标签、模型enriched LocNar+XM3600数据
  - **项目页面**: [github.com/google/imageinwords](https://github.com/google/imageinwords)
  - **重要意义**:
      - **开创性人机协作**: 首个系统性地将VLM种子与人工精炼结合的hyper-detailed描述生成框架
      - **顺序增强突破**: 证明顺序标注优于并行标注（效率+质量双赢）
      - **主动学习循环**: 展示数据收集与模型改进的良性循环
      - **TLDR设计**: 引入报纸风格首句总结，为长描述数据树立范式
      - **全面基准**: IIW-Eval提供多维度质量评估，推动描述生成研究
      - **下游验证**: T2I重建和组合推理验证描述质量的实用价值
      - **质量标杆**: 在描述全面性、具体性、无幻觉性上建立新SOTA
  

</details>
<details>
<summary>
<b><b><a href="https://scholar.google.com/scholar?q=SpaRE">📄 SpaRE</a></b><br>
<code>Paper</code>
</summary>

  - **Data Synthesis Method** - **Synthetic Spatial QA Generation from Hyper-Detailed Captions**:
      - **Core Innovation**: Leverages untapped potential of hyper-detailed image captions to generate synthetic spatial reasoning question-answer pairs
      - **Data Sources**: DOCCI (15K→10K filtered), Localized Narratives (849K→232K filtered), PixMo-Cap (717K→214K filtered)
      - **LLM-Based Extraction**: Uses Qwen2.5-3B-Instruct to extract spatial relationships from detailed descriptions and formulate diverse QA pairs
      - **Data Scale**: 455K samples containing 3.4M spatial reasoning QA pairs covering 66+ spatial relations
      - **Quality Assurance Pipeline**: 5-step automated filtering (deduplication, reference check, answer-description consistency, image-question consistency, spatial relation verification)
  - **Key Technical Components**:
      - **Spatial Relation Analysis**: Quantifies data scarcity - top 17% of relations account for 90% of samples in existing VL datasets
      - **Multi-Stage Filtering**: Pre-filtering (~65% reduction) → QA generation → post-generation quality verification
      - **Domain Coverage**: Positions/directions, relative distances, orientations/angles, foreground/background layers, boundaries/edges, shadows/reflections, overlapping/layering, scale/size comparisons
      - **Hallucination Mitigation**: Aggressive filtering strategy reduces relation/object hallucination to ~4%/3% respectively
  - **Experimental Results**:
      - **Spatial Reasoning Benchmarks**: VSR 70.3→85.4% (+15.1%), What's Up A 44.6→100.0% (+55.4%), What's Up B 79.1→100.0% (+20.9%), 3DSRBench 46.5→57.5% (+11.0%), RealWorldQA 58.6→68.8% (+10.2%)
      - **Peak Performance**: Up to 49% improvement on What's Up benchmark (most significant spatial reasoning gains reported in literature)
      - **General VL Performance**: Maintains strong performance on MMMU (51.0%), MMBench (78.6%), HallusionBench (56.3%), TextVQA (80.5%), MME (1661.4-642.3-145.5-156.3-127.5)
      - **Cross-Architecture Validation**: Effective on both Qwen2VL-2B/7B and demonstrates superior performance vs. caption-only training (Molmo-7B-D baseline)
  - **Error Analysis & Limitations**:
      - **Frame of Reference Challenge**: Struggles with empathetic spatial reasoning (adopting others' perspectives) - consistent with prior VLM limitations
      - **3DSRBench Performance**: Relatively weaker on 3D spatial reasoning due to egocentric bias inherited from source datasets
      - **Qualitative Improvements**: Correctly handles complex perspective-dependent questions (e.g., "is the table on the left or right of me?" from person's vs. viewer's perspective)
  - **Cost Efficiency**:
      - **Data Construction**: Significantly more efficient than manual curation methods
      - **Synthetic vs. Natural**: Outperforms direct caption training approaches while providing targeted spatial knowledge
      - **Filtering Strategy**: Balances quality vs. quantity through multi-stage automated verification
  - **Open Source**: ✅ Code and dataset promised to be released
  - **Significance**:
      - **Data Scarcity Solution**: Addresses critical gap in spatial reasoning data through systematic synthesis from rich descriptions
      - **Systematic Analysis**: First comprehensive quantification of spatial relations distribution in major VL datasets
      - **Practical Impact**: Enables applications in robotics, navigation, AR/VR requiring precise spatial understanding
      - **Methodology Transfer**: Demonstrates effective pipeline for extracting task-specific knowledge from hyper-detailed captions
  
  #### 🔄 持续学习与灾难性遗忘缓解
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2503.04229">📄 GIFT</a></b><br>
<code>arXiv 2503.04229</code>
</summary>

  - **数据合成方法** - **基于Stable Diffusion的VLM持续学习合成数据**：
      - **核心创新**：首个使用扩散生成合成数据缓解视觉-语言模型持续微调中灾难性遗忘的框架
      - **双重遗忘挑战**：解决下游任务遗忘和VLM预训练知识退化 - 独特的多模态CL挑战
      - **合成数据重建**：使用Stable Diffusion重建预训练近似（ImageNet类别名称）和历史下游任务数据，无存储/隐私问题
      - **数据规模**：每任务1K合成图像实现优于100K真实ImageNet图像的性能，展示合成数据效率
  - **关键技术组件**：
      - **类缓冲池策略**：维护P = ∪C_i存储所有遇到的类别名称；从多样化池中采样生成近似预训练+下游数据
      - **对比蒸馏损失**：在合成图像-文本对上使用与CLIP预训练一致的图像-文本匹配目标将当前模型θ_t与之前模型θ_{t-1}对齐
      - **图像-文本对齐约束**：通过在身份矩阵和对比相似度矩阵间强制KL散度作为硬目标纠正教师模型错误
      - **自适应权重整合(AWC)**：训练期间从合成数据动态Fisher信息计算（非EWC的静态），实现实时参数重要性调整
  - **实验框架**：
      - **MTIL基准**：11个数据集（Aircraft, Caltech101, CIFAR100, DTD, EuroSAT, Flowers, Food, MNIST, OxfordPet, StanfordCars, SUN397），跨多样化领域1,201类
      - **两种任务顺序**：字母顺序（Order I）和随机（Order II）安排引入不同领域偏移挑战
      - **综合指标**：Transfer（零样本能力保持），Last（下游任务保持），Avg.（稳定性-可塑性平衡）
  - **实验结果**：
      - **MTIL Order I**：Transfer 69.3% (+8.3% vs l2基线)，Avg. 77.3% (+14.6%)，Last 86.0% (+10.1%) - 所有指标达到新SOTA
      - **MTIL Order II**：Transfer 65.9% (+5.3%)，Avg. 75.7% (+6.9%)，Last 85.3% (+8.1%) - 在高领域偏移下保持强性能
      - **CIL基准**：CIFAR100（10/20/50步）和TinyImageNet（5/10/20步） - 相比传统CL方法一致改进
      - **合成vs真实数据**：1K合成图像在Avg./Last指标上超越1K真实ImageNet图像，同时保持可比的Transfer分数
  - **消融研究**：
      - **对比>其他损失**：对比蒸馏（85.0% Last）>> 特征距离（80.5%）> 仅图像（84.1%）> 仅文本（81.8%）
      - **教师模型选择**：最后CLIP模型最优 vs 初始CLIP（更高Transfer但更低Last）vs WiSE插值（次优平衡）
      - **ITA规模分析**：β=0.25提供最优软-硬目标平衡；更高β导致合成数据过拟合
      - **AWC vs EWC**：自适应Fisher信息（86.0% Last）显著优于静态EWC变体（≤86.2%用256样本）
  - **合成数据分析**：
      - **生成质量**：跨领域高质量多样化图像；50→25去噪步骤最小性能影响（快速生成）
      - **引导规模鲁棒性**：CFG规模（4.5-10.5）间一致性能，由于关注类间多样性超过类内变化
      - **领域特定影响**：消除特定任务合成数据（Aircraft, StanfordCars）显著加剧这些任务的遗忘
      - **分布覆盖**：合成预训练数据（ImageNet类）+下游类提供全面特征空间锚定
  - **计算效率**：
      - **无存储**：每任务后丢弃生成图像；下一任务前重新生成确保多样性
      - **隐私保护**：无需历史数据存储；合成重建消除隐私担忧
      - **成本效益**：每任务1K图像通过Stable Diffusion vs 存储/访问大规模真实数据集
  - **机构**：武汉大学、中科院、武汉AI研究
  - **作者**：吴斌、师武轩、王金桥、叶茫
  - **开源**：✅ [代码](https://github.com/Luo-Jiaming/GIFT_CL)
  - **意义**：
      - **多模态CL突破**：首次成功将扩散生成合成数据应用于VLM持续学习
      - **双重知识保持**：同时维护预训练泛化和下游任务性能 - 实际VLM部署的关键
      - **合成数据范式**：当适当设计时展现合成数据对CL的优势超过真实数据回放
      - **实际影响**：实现生产中高效VLM更新，无灾难性遗忘、存储开销或隐私问题
  
  #### 🔀 跨模态表示转移（无需真实图像）
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2503.12999">📄 Concept-as-Tree (CaT)</a></b><br>
<code>arXiv 2503.12999</code>
</summary>

  - **数据合成方法** - **分层概念树框架的可控合成数据生成**：
      - **核心创新**：首个VLM个性化的可控合成数据流水线，使用树状概念表示生成不同难度和多样性的正/负样本
      - **三层树结构**：根节点（概念类别："cat", "dog"），维度（属性方面："appearance", "behavior", "location"），属性（具体特征："sitting", "lying", "climbing"）
      - **自动化树构建**：VLM描述 → 批量摘要 → 多轮投票机制自我精炼实现正交性和完整性
      - **数据规模**：仅需1-3张用户提供图像，生成可控的正/负样本用于个性化微调
  - **关键技术组件**：
      - **树编辑操作**：(1) 添加维度 - 增加多样性和对话能力，(2) 删除维度 - 降低多样性以专注学习，(3) 修改维度 - 平衡多样性控制
      - **可控样本生成**：正样本通过在用户图像+根节点上微调扩散模型；简单负样本通过根类别替换；困难负样本通过维度修改同时保留根
      - **PCS评分过滤**：基于扰动的概念特定评分通过块洗牌和CLIP相似度差异区分概念特定(CS) vs 概念无关(CA)信息
      - **多类型样本策略**：简单负样本提升识别；困难负样本增强VQA/对话；组合方法在任务间实现最佳性能
  - **实验框架**：
      - **系统性分析**：研究正/负样本影响和跨识别、VQA、标题、选择任务的多样性要求
      - **跨模型验证**：MyVLM、Yo'LLaVA、MC-LLaVA基线显示合成数据集成的一致改进
      - **多样性优化**：识别最佳多样性水平 - 过度多样性引入噪声，不足多样性限制泛化
  - **实验结果**：
      - **MyVLM增强**：识别+3.4%，VQA+4.5%，标题+2.6%（Real+Syn+Plus设置）
      - **Yo'LLaVA增强**：识别+2.2%，VQA+3.9%，标题+5.3%，在某些场景达到接近GPT-4o性能
      - **MC-LLaVA增强**：识别+3.0%，VQA+4.2%，标题+5.3%，跨数据集稳定改进
      - **质量验证**：人工评估显示合成正样本与原始样本相当，合成困难负样本显著优于检索负样本
  - **数据质量洞察**：
      - **PCS评分有效性**：高PCS评分（正样本>0.3，困难负样本>0.1）与概念特定信息内容相关
      - **合成vs检索**：合成负样本相比基于检索的负样本显示更低比例的低质量样本
      - **树操作分析**：添加操作最大程度增加多样性，删除操作减少多样性，修改提供平衡控制
  - **实用指南**：
      - **最小数据要求**：1-3张概念图像足以有效个性化（vs传统10+张图像）
      - **可控生成**：树编辑频率和类型直接控制合成数据多样性和任务特定改进
      - **质量保证**：PCS评分过滤在概念中心数据选择方面比单纯余弦相似度更有效
      - **混合训练**：原始+合成数据组合实现最佳性能，纯合成数据显示分布偏移挑战
  - **机构**：北京大学、英特尔中国实验室、香港中文大学MMLab
  - **作者**：安瑞川、曾凯、陆明、杨思涵、张任锐等
  - **开源**：✅ [代码](https://github.com/zengkaiya/CaT)
  - **意义**：
      - **个性化突破**：首个VLM个性化系统框架，最小用户数据需求
      - **可控合成**：通过可解释的树操作实现对合成数据特征的精确控制
      - **质量评估创新**：PCS评分为评估合成图像中概念特定信息提供新方法
      - **实际影响**：使VLM个性化在有限用户提供示例的真实世界部署中变得可行
  
  #### 🔄 持续学习与灾难性遗忘缓解
  

</details>
---

#### 🛠️ 工具辅助标注生成（数据合成用）

> Following tools are commonly used in data synthesis pipelines

<details>
<summary>
<b><b><a href="https://scholar.google.com/scholar?q=All-Seeing%20Project">📄 All-Seeing Project</a></b><br>
<code>Paper</code>
</summary>

  - **Data Synthesis Method** (Section 3):
      - Uses SAM, RAM, Tag2Text and other tools to automatically generate multi-level annotations
      - Pipeline: Image → Segmentation+Tags → Region Description → Instruction Data
      - Builds AS-1B dataset (1.2B region-text pairs)
  - **This is true data synthesis**: Uses tool combination to generate new annotations
  - **Open Source**: ✅ [Dataset](https://huggingface.co/datasets/OpenGVLab/AS-V2) | [Code](https://github.com/OpenGVLab/all-seeing)
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2502.09925">📄 TaskGalaxy</a></b><br>
<code>ICLR 2025</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-ICLR_2025_--_快手科技-red?style=flat-square"/>
</summary>

  - **聚焦**: **大规模任务类型扩展** - 构建包含19,227个层级化任务类型和413K样本的多模态指令微调数据集，通过自动化Pipeline显著提升任务多样性
  - **数据合成方法** - **GPT-4o驱动的任务类型层级扩展 + 多裁判过滤Pipeline**:
      - **核心创新**: 首个万级任务类型的多模态数据集，通过GPT-4o自动扩展任务分类体系，结合CLIP过滤和多开源模型评分确保质量
      - **问题识别**:
        - 现有指令微调数据集任务类型有限（如Vision-Flan仅196类），限制模型泛化能力
        - 人工标注任务类型成本高、耗时长，难以规模化
        - 任务类型与图像匹配度低导致训练数据质量不佳
      - **五步自动化生成Pipeline**:
        1. **层级化任务类型生成**:
           - **种子任务定义**: 人工定义少量一级任务类型（如OCR、Image Description、Logical Reasoning）
           - **GPT-4o迭代扩展**:
             - **一级任务**: 从种子任务扩展为115个一级任务类型
             - **二级任务**: 为每个一级任务生成2,796个二级子任务
             - **三级任务**: 进一步细分为14,370个三级任务
           - **Prompt设计**: 为不同层级设计专门prompt，确保扩展的系统性和完整性
           - **最终规模**: 19,227个层级化任务类型（1:2:3比例 = 115:2,796:14,370）
        2. **图像数据收集**:
           - **多源图像**: 从ALLaVA、Visual Genome、LAION、DocVQA、CLEVR-Math等公开数据集收集图像
           - **保持原始分辨率**: 不进行额外预处理
           - **支持多样图像类型**: 自然场景、文档、图表、艺术作品、水印图像等
        3. **任务类型-图像匹配（CLIP过滤）**:
           - **文本-图像相似度计算**: 使用CLIP计算任务类型文本与图像的相似度
           - **初步筛选**: 为每张图像匹配最相关的任务类型
           - **问题**: CLIP匹配性能有限，可能产生误匹配
        4. **问答对生成（GPT-4o）**:
           - **输入**: 图像 + 匹配的任务类型文本
           - **输出**: 问题-答案对（JSON格式）
           - **Prompt设计**: 要求生成复杂问题并提供详细答案
           - **多样性**: 每个任务类型-图像对生成多个不同问题
        5. **多裁判评分过滤（Referee Screening）**:
           - **三模型共识机制**: 使用三个高性能开源多模态模型（InternVL、Qwen-VL、其他MLLM）作为裁判
           - **评分标准**: 每个模型对任务类型、问题与图像的匹配度打分（0或1）
           - **筛选规则**: 仅保留累积得分≥2的样本（三个模型中至少两个认可）
           - **优势**: 提升任务类型、问题与图像的对齐准确性，降低闭源API成本
           - **平衡策略**: 为保持任务类型平衡，每个任务类型随机选择1-55个样本
      - **关键技术优势**:
        - **完全自动化**: 除少量种子任务外，整个pipeline无需人工干预
        - **任务类型数量**: 19,227个任务类型，是Vision-Flan的98倍
        - **质量控制**: 多裁判机制确保数据质量，避免单模型偏差
        - **可扩展性**: Pipeline可适应新图像类型和任务类型
  - **TaskGalaxy数据集**:
      - **总规模**: 413,648个高质量问答对
      - **任务类型**: 19,227个层级化任务类型
      - **样本分布**: 每个任务类型1-55个样本
        - 1-10样本: 50.1%的任务类型
        - 11-20样本: 11.1%
        - 21-40样本: 10.21%
        - 41-55样本: 27.99%
      - **层级分布**: 一级:二级:三级 = 1:2:3 (115:2,796:14,370)
  - **实验结果** - **在所有16个基准上均有提升**:
      - **LLaVA-v1.5-7B** (加入TaskGalaxy微调):
        - MME: 1506→1533, MMBench: 64.69%→68.04%, ScienceQA: 69.51%→71.26%
        - MathVista: 26.7%→31.4% (+4.7%), ChartQA: 14.72%→20.20% (+5.48%)
        - AI2D: 25.32%→38.26% (+12.94%), HalluBench: 50.05%→51.74%
        - **平均提升**: 44.46%→48.96% (+4.5%, 不含MME)
      - **LLaVA-v1.5-13B** (加入TaskGalaxy微调):
        - MME: 1532→1600, MMBench: 68.47%→69.85%, MathVista: 28.1%→33.3% (+5.2%)
        - ChartQA: 15.56%→23.44% (+7.88%), AI2D: 21.13%→41.19% (+20.06%)
        - **平均提升**: 45.21%→49.04% (+3.83%)
      - **InternVL-Chat-v1.0-7B** (加入TaskGalaxy微调):
        - MMBench: 65.29%→67.10%, ScienceQA: 66.4%→70.93%, MathVista: 27.7%→30.8%
        - MMMU: 27.0%→34.9% (+7.9%), AI2D: 35.96%→38.57%
        - **平均提升**: 47.79%→50.79% (+3.0%)
      - **InternVL-Chat-v1.0-13B** (加入TaskGalaxy微调):
        - MMBench: 65.64%→69.50%, ScienceQA: 70.12%→72.72%, MathVista: 28.7%→30.5%
        - AI2D: 38.55%→52.60% (+14.05%), Q-Bench: 56.13%→58.60%
        - **平均提升**: 49.90%→53.17% (+3.27%)
  - **消融研究关键发现**:
      - **任务类型数量至关重要**:
        - 固定100K样本，任务类型从2K增至19K，性能持续提升
        - 证明任务多样性比数据量更重要
      - **样本数量的影响**:
        - 固定19,227任务类型，样本从76K增至413K，性能逐步提升
        - 但在某些基准（如LLaVA-in-the-wild）上存在最优样本量（281K）
      - **vs. 规则方法和闭源模型**: TaskGalaxy的任务覆盖度和质量优于手工规则构建和闭源模型生成
  - **任务类型示例**（展示任务层级结构）:
      - **一级**: OCR, Image Description, Logical Reasoning, Suggestions, Storytelling
      - **二级**: OCR→webpage OCR / handwritten OCR, Image Description→location-based / historical context
      - **三级**: webpage OCR→extract links / recognize style, location-based→describe cityscapes / identify landmarks
  - **机构**: 快手科技（Kuaishou Technology）
  - **作者**: Jiankang Chen, Tianke Zhang, Changyi Liu, Haojie Ding, Yaya Shi, Feng Cheng, Huihui Xiao, Bin Wen, Fan Yang, Tingting Gao, Di Zhang
  - **发布时间**: ICLR 2025, arXiv 2025年2月
  - **论文链接**: [arXiv:2502.09925](https://arxiv.org/abs/2502.09925)
  - **开源**: ✅ [GitHub](https://github.com/Kwai-YuanQi/TaskGalaxy)
  - **意义**:
      - **任务类型突破**: 首次实现万级任务类型覆盖，是现有数据集的100倍
      - **自动化Pipeline**: 大幅降低任务类型扩展成本，提升可扩展性
      - **任务多样性价值**: 实证证明任务多样性对模型泛化能力的重要性超过数据量
      - **多裁判机制**: 创新的质量控制方法，平衡成本与质量
      - **实用性**: 在16个主流基准上均有显著提升，证明方法的通用性
  

</details>
---

## 🎯 VLM自我改进与强化学习

This emerging category focuses on **scalable VLM self-improvement** through reinforcement learning and gamified environments, enabling models to enhance their reasoning capabilities **without human annotation**. These methods leverage competitive dynamics, strategic gameplay, and iterative policy optimization to achieve sustained performance improvements across diverse reasoning tasks.

<details>
<summary>
<b><b><a href="https://scholar.google.com/scholar?q=Chart-CoCa">📄 Chart-CoCa</a></b><br>
<code>Paper</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-CIKM_2025-red?style=flat-square"/>
</summary>

  - **Focus**: **Chart Understanding Self-Improvement via Code-Driven Synthesis and Candidate-Conditioned Answering** - VLM self-generates code→executes to create charts→automatically extracts precise annotations→trains with candidate-conditioned answering, achieving chart understanding improvement without human annotation or external models
  - **Data Synthesis Method** - **Code-Mediated Chart Synthesis + Candidate-Conditioned Answering Training**:
      - **Core Innovation**: First fully self-improving chart understanding paradigm, using code as intermediary to ensure precision and reliability of synthetic data, without human annotation or teacher models
      - **Problem Identification**:
        - VLMs struggle with chart understanding tasks (inaccurate descriptions, insufficient reasoning complexity)
        - Traditional synthetic data methods suffer from noisy labels (direct chart→text generation hard to guarantee accuracy)
        - Existing methods rely on strong teacher models (e.g., GPT-4) or extensive human annotation
      - **Code-Driven Synthesis Pipeline (Three Steps)**:
        1. **Chart Description Generation (Step 1)**:
           - **Input**: Unlabeled real chart c
           - **Output**: Chart description d (including title, x/y-axis labels, data points, legends, etc.)
           - **Model**: VLM M (initial version, e.g., InternVL2-8B)
           - **Formula**: d = M_LMM(c)
           - **Purpose**: Transform visual information into structured text description
        2. **Code Generation (Step 2)**:
           - **Input**: Chart description d
           - **Output**: Executable Python Matplotlib code p
           - **Model**: VLM's language model component M_LM
           - **Formula**: p = M_LM(d)
           - **Constraint**: Must use Python Matplotlib library (facilitates execution and information extraction)
           - **Key Advantage**: Code executability ensures generated chart precisely matches description
        3. **Code Execution and Information Extraction (Step 3)**:
           - **Chart Generation**: Execute code p to generate new chart c* (precisely matching description d)
           - **Information Extraction**: Extract chart elements through reflection during code execution:
             - **Layout**: fig, axes = plt.subplots(rows, columns)
             - **Title**: axes[i,j].get_title()
             - **X/Y Labels**: axes[i,j].get_xlabel(), get_ylabel()
             - **Legend**: axes[i,j].get_legend()
             - **Ticks**: axes[i,j].get_xticklabels(), get_yticklabels()
             - **Colorbar**: axes[i,j].get_images()[0].colorbar
             - **Lines**: axes[i,j].lines
           - **QA Pair Generation**:
             - Use CharXiv's descriptive questions as seeds (simple, no design cost, easy answer access)
             - Automatically generate precise answers based on extracted information
             - Example: Q: "What is the chart title?" A: axes[0,0].get_title() → "Optimizations in SizeAware++"
             - Supports 8 question types: layout, title, labels, legends, ticks, colorbar, lines
           - **Output**: High-quality triplets ⟨c*, q*, a*⟩ (chart, question, answer)
      - **Key Technical Advantages**:
        - **Zero Noisy Labels**: Code execution guarantees absolute consistency between chart and annotations (vs noise in direct generation)
        - **Full Automation**: No human annotation or external strong models needed
        - **Verifiability**: Code is traceable, each annotation has clear provenance
        - **Scalability**: Applicable to any unlabeled chart dataset
      - **Candidate-Conditioned Answering**:
        - **Motivation**: Direct fine-tuning problematic - questions simple/fixed, model struggles to handle flexible questions
        - **Inspiration**: Test-time scaling (increasing inference budget improves performance)
        - **Training Stage (Three Steps)**:
          1. **Candidate Answer Generation**: Given ⟨c*, q*⟩, initial VLM M generates k candidate responses r_1,...,r_k
             - Formula: r_1,...,k = M(c*, q*)
             - Use sampling strategy (temperature>0) for diverse candidates
          2. **Answer Model Training**: Train new answer VLM M_ANS, input (c*, q*, r_1,...,r_k), output final answer a
             - Formula: a = M_ANS(c*, q*, r_1,...,r_k)
             - M_ANS learns to synthesize multiple candidates and generate optimal answer
             - Training loss: L_answer = -log P(a* | c*, q*, r_1,...,r_k)
          3. **Iterative Update**: Use (c*, q*, a) to update initial VLM M parameters, obtaining M_ANS
        - **Inference Stage (Two Steps)**:
          1. Initial VLM M generates k candidates: r_1,...,k = M(c, q)
          2. Trained M_ANS synthesizes candidates to generate final answer: â = M_ANS(c, q, r_1,...,k)
        - **Advantages**:
          - Enhances model's ability to handle flexible, diverse questions
          - Leverages collective wisdom of multiple candidates
          - Test-time scaling brings performance improvements
  - **Experimental Results - Significant Improvements on CharXiv Dataset**:
      - **CharXiv Benchmark**: Includes descriptive tasks (Information Extraction, Pattern Recognition, Enumeration, Counting, Compositionality) and reasoning tasks (Text in Chart/General, Number in Chart/General)
      - **InternVL2-8B Self-Improvement Effects**:
        - **Descriptive Tasks**: 54.10% → **69.60%** (+15.50%)
          - Information Extraction: 69.40% → 74.20% (+4.80%)
          - Pattern Recognition: 40.52% → 75.46% (+34.94%, largest improvement)
          - Enumeration: 19.64% → 26.79% (+7.15%)
          - Counting: 54.10% → 69.60% (+15.50%)
        - **Reasoning Tasks**: 23.60% → **31.60%** (+8.00%)
          - Text in Chart: 44.76% → 58.95% (+14.19%)
          - Text in General: 61.83% → 68.19% (+6.36%)
          - Number in Chart: 19.64% → 26.79% (+7.15%)
          - Number in General: 14.85% → 25.33% (+10.48%)
        - **Overall Improvement**: Average +11.75%, proving effectiveness of fully self-improving paradigm
      - **Cross-Model Generalization Verification** (using Chart-CoCa method):
        - **LLaVA-1.6-7B**: 32.77% → **47.83%** (+15.06%, descriptive); 15.50% → **23.10%** (+7.60%, reasoning)
        - **Qwen2VL-7B**: 59.90% → **71.75%** (+11.85%, descriptive); 30.80% → **36.90%** (+6.10%, reasoning)
        - **InternVL2-26B**: 61.90% → **72.63%** (+10.73%, descriptive); 34.60% → **39.50%** (+4.90%, reasoning)
        - **Conclusion**: Chart-CoCa method effective across different model scales and architectures
      - **Comparison with Majority Voting**:
        - Majority Voting (5 candidates): Descriptive 61.38%, Reasoning 26.70%
        - Chart-CoCa (5 candidates): Descriptive **69.60%**, Reasoning **31.60%**
        - **Improvement**: +8.22% (descriptive), +4.90% (reasoning)
        - **Reason**: Majority Voting prone to majority bias; Chart-CoCa learns to synthesize diverse information through candidate-conditioned answering
      - **Pass@K Analysis (Coverage)**:
        - **Descriptive Tasks**: Pass@1=54.1%, Pass@30=**85.95%** (+31.85%)
        - **Reasoning Tasks**: Pass@1=23.6%, Pass@30=**55.8%** (+32.2%)
        - **Conclusion**: VLMs have strong inherent capability (high accuracy with sufficient trials), but need methods to unlock this potential
      - **Code Execution Success Rate Analysis**:
        - **Overall Success Rate**: 70.7% (after up to 5 retries)
        - **Error Type Distribution**: ValueError (36.0%), IndexError (24.1%), SyntaxError (5.6%), AttributeError (5.0%), TypeError (2.9%), Others (1.5%)
        - **Retry Improvement**: Among samples failing on first attempt, 24% succeed through retries; but some samples stuck in same error
        - **Improvement Room**: Targeted error handling could further improve code execution success rate
  - **Ablation Study Key Findings**:
      - **Necessity of Code Intermediary (-Code)**:
        - Removing code generation step, directly generating QA from charts: Descriptive -9.20%, Reasoning -5.50%
        - **Conclusion**: Code intermediary ensures data precision, significantly better than direct generation
      - **Necessity of Chart Description (-Desc)**:
        - Removing chart description step, directly generating code from charts: Descriptive -4.53%, Reasoning -3.60%
        - **Conclusion**: Chart description as intermediate representation reduces difficulty of direct code generation
      - **Importance of Both Combined (-Both)**:
        - Removing both description and code steps: Descriptive -13.68%, Reasoning -7.10%
        - **Conclusion**: Complete pipeline crucial for performance
  - **Qualitative Analysis**:
      - **Candidate Answer Diversity**: 5 candidates show different reasoning paths, Chart-CoCa can synthesize to select best answer
      - **Error Cases**: Mainly concentrated in questions requiring complex reasoning or precise numerical computation (code generation or logic errors)
      - **Success Cases**: Chart-CoCa excels in most descriptive questions and moderate-difficulty reasoning questions
  - **Institution**: Hong Kong University of Science and Technology (Guangzhou)
  - **Authors**: Gongyao Jiang, Qiong Luo
  - **Publication**: CIKM 2025
  - **Code**: [To be released]
  - **Significance**:
      - **Self-Improvement Paradigm**: First fully self-improving chart understanding method without human annotation or external teacher models
      - **Code Intermediary Innovation**: Proves using code as intermediary eliminates noisy label problem in synthetic data
      - **Candidate-Conditioned Answering**: Innovative training strategy leveraging test-time scaling idea to improve model generalization
      - **Scalability**: Method applicable to any unlabeled chart data, theoretically infinitely scalable for training data
      - **Cross-Model Generalization**: Validated effectiveness across multiple VLM architectures, providing universal self-improvement framework
      - **Practical Value**: Provides low-cost, high-quality data generation and model improvement solution for chart understanding tasks
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2502.02740">📄 VLM Dialog Games</a></b><br>
<code>arXiv 2502.02740</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **聚焦**: **视觉语言模型对话游戏用于自我改进** - 通过两个VLM代理在目标导向的参考游戏中自对弈，自动筛选成功的游戏交互，生成高质量的交错图像-文本数据用于微调
  - **数据合成方法** - **目标导向自对弈框架 + 自动成功检测**:
      - **核心创新**: 首个基于对话游戏的VLM自我改进框架，通过目标导向的自对弈生成高质量合成数据，无需人工标注或外部模型
      - **VLM对话游戏机制**:
        - **游戏设置**: 使用未标注图像构建参考游戏变体
          - **Describer（描述者）**: 看到单个目标图像，被指示忠实回答关于该图像的问题
          - **Guesser（猜测者）**: 看到N张图像（包括目标图像和多个干扰图像），通过提问识别目标图像
        - **游戏流程**:
          - Guesser提出澄清问题（如"图像中有多少对象？"）
          - Describer回答问题（如"有9个对象"）
          - Guesser基于累积信息做出猜测（如"我知道答案了，是图像4"）
          - 如果Guesser正确识别目标图像，游戏成功
        - **游戏难度控制**:
          - **干扰图像数量**: 增加干扰图像数量直接增加难度（N=2到8）
          - **图像相似性**: 随机选择图像创建较容易的游戏，而将视觉或语义相似的图像分组增加挑战
          - **最优设置**: N=4在研究中达到最佳平衡
      - **自改进工作流程**:
        1. **游戏设置**: 配置对话游戏，指定未标注图像数据集（OpenImages、DOCCI或领域特定数据集如机器人视频帧）
        2. **对话生成**: 通过VLM代理的自对弈生成对话
          - **Describer示例**: 输入=单个图像+问题，输出=对应答案
          - **Guesser示例**: 输入=N张图像+目标图像描述摘要，输出=澄清问题或猜测
          - 每个成功的VLM对话游戏生成多个两种类型的训练示例
        3. **对话过滤**: 基于成功标准过滤生成的对话
          - **成功检测**: 如果Guesser的最终选择匹配目标图像，对话被视为成功
          - **验证步骤**: 为避免偶然正确猜测，使用相同图像但打乱顺序重新运行对话，验证在所有排列中都能正确识别目标图像
          - **计算效率**: 限制测试排列为N个，确保目标图像出现在每个可能位置（1到N），干扰图像顺序可保持固定
        4. **模型改进**: 使用过滤后的成功对话游戏数据微调VLM
          - **标准监督微调**: 使用过滤后的对话数据
          - **迭代改进**: 改进后的模型可以用于生成新的、更高质量的数据集，进行进一步改进（round 1, round 2等）
      - **关键技术优势**:
        - **目标导向**: 游戏的目标导向性质确保生成数据的质量，成功检测提供自动质量控制
        - **自对弈**: 利用VLM的指令跟随能力，实现可扩展的数据收集方法
        - **无需外部模型**: 不需要GPT-4V或其他外部模型，仅使用基础VLM本身
        - **领域适应性**: 可适应特定领域（如机器人），通过设计游戏使用该领域的图像
        - **可迭代**: 改进的模型可以用于生成更好的数据集，实现持续改进
      - **实验结果**:
        - **通用图像实验**（DOCCI和OpenImages数据集）:
          - **游戏成功率**: Gemini 1.5 Flash 20.3% → VLM Dialog Games (DOCCI) 24.4% (+4.1%)
          - **VQA性能**（VQAv2）:
            - **Yes/No问题**: 73.0% → 79.8% (+6.8%，DOCCI）和83.4% (+10.4%，OpenImages）
            - **计数问题**: 56% → 58.3% (+2.3%，DOCCI）和56% (+0.0%，OpenImages）
          - **跨数据集泛化**: 在DOCCI上训练的模型在OpenImages游戏上表现更好（21.9% vs 18.4%），反之亦然
        - **机器人领域实验**（ALOHA数据集）:
          - **游戏成功率**: Gemini 1.5 Flash 14.39% → Round 1 40.15% (+25.76%) → Round 2 53.74% (+39.35%)
          - **成功检测准确率**: 56.5% → Round 1 69.5% (+13.0%) → Round 2 73.0% (+16.5%)
          - **迭代改进**: Round 2进一步提升了游戏成功率和成功检测准确率
          - **vs基线**:
            - **SFT-Description**: 65.0% (+8.5%) - 直接微调图像-任务描述对
            - **Self-QA**: 67.0% (+10.5%) - 基于问答的自我改进方法
            - **VLM Dialog Games (answers only)**: 68% (+12.5%) - 仅使用Describer答案，但游戏成功率低（17.92%），无法实现进一步迭代改进
        - **消融研究**:
          - **图像数量影响**（N值）:
            - **N=2**: 游戏成功率83.7%，但游戏简单，数据信息量少，VQA准确率81.3% (+8.3%)
            - **N=4**: 游戏成功率18.4%，VQA准确率83.4% (+10.4%) - **最优**
            - **N=8**: 游戏成功率0.24%，游戏过于困难，生成的对话数据极少，VQA准确率77.1% (+4.1%)
          - **图像分组策略**:
            - **相似图像分组**: 游戏成功率18.4%，VQA准确率83.4% (+10.4%)
            - **随机图像分组**: 游戏成功率24.7%，VQA准确率82.6% (+9.6%)
            - **结论**: 两种策略都显著改进，相似图像分组略好，但随机分组也能有效工作
      - **关键发现**:
        - **自对弈有效性**: 当前VLM的指令跟随能力使其能够在对话游戏中实现非零成功率，为可扩展数据生成提供基础
        - **目标导向优势**: 游戏的目标导向性质确保生成的数据质量，成功检测提供自动质量控制
        - **迭代改进能力**: 改进的模型可以用于生成更好的数据集，实现持续改进（Round 1 → Round 2）
        - **领域适应性**: 方法可适应特定领域（如机器人），在高质量数据稀缺的领域特别有效
        - **Guesser问题的重要性**: 仅使用Describer答案虽然能提升成功检测，但无法提升游戏成功率，限制了进一步迭代改进
      - **机构**: Google DeepMind
      - **作者**: Ksenia Konyushkova, Christos Kaplanis, Serkan Cabi, Misha Denil
      - **发布时间**: arXiv 2025年2月（v1）
      - **开源**: ⚠️ 论文中未明确说明代码/数据可用性
      - **意义**:
        - **方法创新**: 首个基于对话游戏的VLM自我改进框架，通过目标导向的自对弈生成高质量数据
        - **可扩展性**: 利用VLM自身能力，无需外部模型或人工标注，实现可扩展的数据生成
        - **领域适应性**: 可适应特定领域（如机器人），在高质量数据稀缺的领域特别有效
        - **实用价值**: 在通用VQA和机器人成功检测任务上显著提升性能，证明方法的有效性
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2405.14622">📄 CSR (Calibrated Self-Rewarding)</a></b><br>
<code>arXiv 2405.14622</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-NeurIPS_2024-red?style=flat-square"/>
</summary>

  - **聚焦**: **校准自奖励视觉语言模型** - 通过在校准的自奖励过程中引入视觉约束来改善LVLM的模态对齐，减少幻觉并提升性能
  - **数据合成方法** - **迭代偏好优化框架 + 校准奖励模型**:
      - **核心创新**: 首个将视觉约束整合到自奖励范式中的方法，通过校准奖励模型解决LVLM在响应生成和偏好建模阶段的模态对齐问题
      - **问题识别**: LVLM存在模态对齐问题，模型倾向于优先考虑文本信息而忽略视觉输入，导致幻觉现象
      - **CSR框架（两个交替阶段）**:
        1. **候选响应生成阶段**:
           - **句子级Beam Search**: 使用句子级beam search为每个输入提示生成细粒度候选响应
           - **奖励计算流程**:
             - **初始奖励**: 语言解码器确定每个生成句子的初始奖励 R_T(s)（句子级累积概率）
             - **图像-响应相关性分数**: 使用CLIP-score计算 R_I(s) = max(100×cos(F_I(x_v), F_T(s)), 0)
             - **校准奖励**: R(s) = λ·R_I(s) + (1-λ)·R_T(s)，其中λ=0.9（强调视觉校准）
           - **迭代生成**: 根据校准奖励分数选择top-k和bottom-k句子，继续下一轮beam search
           - **累积奖励**: 响应y的累积奖励 R(y) = Σ R(s_i)
        2. **偏好策划与微调阶段**:
           - **偏好数据构建**: 选择累积校准奖励最高和最低的响应作为偏好和反偏好响应
           - **DPO优化**: 使用直接偏好优化（DPO）进行微调
           - **参考模型**: 每次迭代使用上一轮微调后的模型作为参考模型
           - **损失函数**: L_t = -E log σ(α log(π_θ(y_w,t|x)/π_θt-1(y_w,t|x)) - α log(π_θ(y_l,t|x)/π_θt-1(y_l,t|x)))
      - **关键技术优势**:
        - **视觉约束奖励**: 通过整合图像-响应相关性信息，解决LVLM在生成偏好时忽略视觉输入的问题
        - **逐步奖励**: 句子级奖励提供更细粒度的指导和更强的鲁棒性
        - **自奖励范式**: 无需外部模型或人工标注，利用模型自身生成偏好数据
        - **迭代改进**: 通过多轮迭代持续提升模型性能和模态对齐能力
      - **训练设置**:
        - **基础模型**: LLaVA-1.5 7B和13B
        - **训练数据**: 从LLaVA150k数据集的详细描述和复杂推理子类中随机采样约13,000个样本
        - **微调方法**: LoRA微调
        - **迭代次数**: 3轮迭代（每轮约3.5-5小时，1×A100 80GB）
        - **超参数**: λ=0.9（CLIP分数权重），α=0.1（语言分数权重）
      - **实验结果**:
        - **综合基准**（MME、SEED、LLaVAW、MMBench、MM-Vet）:
          - **LLaVA-1.5-7B + CSR**: 平均提升7.62%（迭代3轮）
          - **LLaVA-1.5-13B + CSR**: 平均提升5.25%（迭代3轮）
          - **显著改进**: LLaVAW +8.9%，CHAIR +49.50%
        - **通用VQA**（ScienceQA、VizWiz、GQA）:
          - **7B模型**: ScienceQA +2.9%，VizWiz +4.1%，GQA +0.3%
          - **13B模型**: ScienceQA +3.5%，VizWiz +3.2%，GQA +0.4%
        - **幻觉基准**（POPE、CHAIR）:
          - **POPE**: 7B模型 85.90%→87.01%（+1.11%），13B模型 85.90%→87.30%（+1.40%）
          - **CHAIR_S**: 7B模型 48.8%→21.0%（-27.8%，越低越好），13B模型 48.3%→28.0%（-20.3%）
          - **CHAIR_I**: 7B模型 14.9%→6.0%（-8.9%），13B模型 14.1%→7.3%（-6.8%）
        - **vs. 竞争方法**:
          - **超越自奖励基线**: 平均提升2.43%
          - **超越外部偏好方法**: 优于POVID、RLHF-V、Silkie等依赖GPT-4或人工标注的方法
          - **vs. SOTA开源VLM**: 在10个基准中的9个上超越InstructBLIP、Qwen-VL-Chat、mPLUG-Owl2等
        - **迭代改进分析**:
          - **奖励分数变化**: 偏好响应奖励从0.4885（迭代1）提升至0.5066（迭代5）
          - **图像-响应相关性**: 偏好和反偏好响应的图像相关性分数均提升，且差距逐渐缩小
          - **注意力分析**: CSR增强了对视觉token的注意力，减少了对文本上下文的过度依赖
        - **兼容性验证**（Vila 7B）:
          - **整体提升**: 3轮迭代后平均提升3.37%
          - **显著改进**: VizWiz +8.48%，MM-Vet +14.0%
      - **消融研究**:
        - **仅R_T（语言分数）**: 68.46%（7B），68.12%（13B）
        - **仅R_I（图像分数）**: 67.49%（7B），69.23%（13B）
        - **CSR（组合）**: 72.39%（7B），71.95%（13B）
        - **结论**: 组合使用两种分数效果最佳
        - **λ值分析**: λ=0.9优于0.5和0.1，证明视觉校准的重要性
      - **理论分析**:
        - **定理5.1**: 在温和假设下，引入图像-响应相关性分数可以校准自奖励过程，提升生成准确性
        - **关键条件**: 当模型倾向于优先考虑文本信息而非视觉输入时（∥β*^T V_1*∥ ≪ ∥β*^T V_2*∥），通过视觉约束（λ<1）可以增加对图像信号的关注
      - **关键发现**:
        - **自奖励有效性**: 自生成的偏好数据比外部模型（如GPT-4）生成的偏好数据更有效，因为更符合目标LVLM的固有偏好
        - **视觉约束必要性**: 直接应用自奖励到LVLM无法解决模态对齐问题，需要引入视觉约束
        - **迭代改进能力**: CSR能够通过迭代微调持续提升性能，逐步收敛
        - **跨模型兼容性**: 方法适用于不同的LVLM架构（LLaVA-1.5、Vila）
      - **机构**: 北卡罗来纳大学教堂山分校、芝加哥大学、马里兰大学、罗格斯大学、香港科技大学、香港理工大学、南洋理工大学、新加坡国立大学
      - **作者**: Yiyang Zhou, Zhiyuan Fan, Dongjie Cheng, Sihan Yang, Zhaorun Chen, Chenhang Cui, Xiyao Wang, Yun Li, Linjun Zhang, Huaxiu Yao
      - **发布时间**: arXiv 2024年5月 (v4) | NeurIPS 2024
      - **开源**: ✅ [代码和数据](https://github.com/YiyangZhou/CSR)
      - **重要意义**:
        - **范式创新**: 首次将视觉约束整合到自奖励范式中，解决LVLM特有的模态对齐问题
        - **成本降低**: 无需外部模型或人工标注，仅使用模型自身进行自我改进
        - **性能提升**: 在多个基准上显著提升性能并减少幻觉，平均提升7.62%
        - **理论支撑**: 提供严格的理论分析验证方法的有效性
        - **实用价值**: 为LVLM的自我改进提供可扩展且经济高效的解决方案
  

</details>
---

<details>
<summary>
<b><b><a href="https://scholar.google.com/scholar?q=Vision-Zero">📄 Vision-Zero</a></b><br>
<code>Paper</code>
</summary>

  - **Data Synthesis Method** - **Strategic Gamified Self-Play Framework**:
      - **Core Innovation**: First **zero-human-in-the-loop** training paradigm for VLMs using "Who Is the Spy" style visual games
      - **Label-Free & Domain-Agnostic**: Accepts arbitrary image pairs (CLEVR synthetic, charts, real-world) to generate strategic reasoning games
      - **Iterative Self-Play Policy Optimization (Iterative-SPO)**: Novel algorithm alternating between self-play and RLVR to prevent performance plateaus
      - **Strategic Environment**: Models compete in two-stage games (Clue Stage: provide visual clues, Decision Stage: identify the spy)
      - **Data Scale**: 2K CLEVR pairs (~6 GPU hours), 1K chart pairs, 1K real-world pairs - minimal cost compared to traditional human annotation
      - **Quality Assurance**: Zero-sum reward design with Role-Advantage Estimation (RAE) to handle asymmetric role information
  - **Key Technical Components**:
      - **Game Environment**: Civilians vs. Spy setup with subtly different image pairs (missing/added/modified objects)
      - **Reward System**: Clue stage uses zero-sum rewards based on votes received; Decision stage uses discrete +1/-0.5/-1 rewards
      - **Training Algorithm**: Dynamic stage switching based on performance thresholds (accuracy ≥0.9 or "n/a" rates)
      - **Domain Flexibility**: Automated image editing pipeline supports procedural generation (CLEVR) and tool-based editing (Gemini2.5-Flash)
  - **Experimental Results**:
      - **Reasoning & Math**: MathVista 68.2→72.6% (+4.4%), MathVision 25.4→28.1% (+2.7%), WeMath 36.1→39.8% (+3.7%)
      - **Chart/OCR**: ChartQA 86.1→87.2% (+1.1%), OCRBench 88.3→89.0% (+0.7%)
      - **Vision-Centric**: MMVP 76.8→79.5% (+2.7%), RealWorldQA 68.1→68.5% (+0.4%)
      - **Cross-Capability Transfer**: Mitigates negative transfer common in traditional RL methods (vs. 10% decline in MM-Eureka)
      - **Model Generalization**: Effective across Qwen2.5-VL-7B, InternVL3-8B, InternVL3-14B architectures
  - **Cost Efficiency**:
      - **Dataset Construction**: Orders of magnitude cheaper than traditional methods (6 GPU hours vs. months/years)
      - **Performance**: Outperforms SOTA methods trained on expensive human-labeled datasets (MM-Eureka, VLAA-Thinker, R1-OneVision)
      - **Sustainable Growth**: Win rates improve from 50% to 71% during training with increasing reasoning complexity
  - **Open Source**: ✅ [Code](https://github.com/wangqinsi1/Vision-Zero) | Models & datasets promised
  - **Significance**:
      - **Paradigm Shift**: Eliminates dependency on human-curated datasets through competitive self-play
      - **Scalable Framework**: Domain-agnostic approach enables rapid dataset construction for specific domains
      - **Strategic Reasoning**: Joint visual-linguistic analysis strengthens spatial understanding and mitigates text shortcut bias
      - **Practical Impact**: Provides economical, accessible training paradigm for VLM development
  

</details>
---

## 🧠 跨领域方法论洞察

> **Note**: This section includes influential works from adjacent domains (e.g., LLM reasoning, mathematical data curation) whose **data curation and quality assessment methodologies** provide valuable frameworks transferable to multimodal settings. While not directly VLM papers, their systematic approaches to data quality evaluation, mixture optimization, and efficient filtering pipelines offer important insights for multimodal data practitioners.

### 📚 Foundation Model Mid-training & Data Curation

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

### 🔄 Multi-Modal Model Collapse & Synthetic Data Robustness

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2505.08803">📄 多模态合成数据训练与模型坍塌</a></b><br>
<code>arXiv 2505.08803</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **研究焦点** - **多模态生成系统中的模型坍塌现象调查**：
      - **核心创新**：首次系统性调查多模态生成系统（VLM和扩散模型）在合成数据训练中的模型坍塌现象，识别多模态坍塌相比单模态的独特特征
      - **研究背景**：随着合成数据在训练下一代模型中使用增加，理解"模型坍塌"（model collapse）现象及其在多模态环境中的表现变得至关重要
      - **双模态坍塌分析**：在VLM图像标题生成和扩散模型图像生成中检验坍塌模式，发现多模态系统展现与单模态系统不同的坍塌特征
  - **关键发现**：
      - **VLM坍塌特征**：与LLM坍塌不同，VLM图像标题任务中方差可能增加，违背传统坍塌模式
      - **偏差-方差权衡**：多模态坍塌中平衡偏差-方差权衡比单模态情况更为关键
      - **扩散模型韧性**：扩散模型在合成数据训练中表现出比VLM更强的抗坍塌能力
      - **递归训练风险**：多智能体递归训练循环中的加速坍塌风险识别
  - **缓解策略**：
      - **增加解码预算**：更大的采样预算和多样性参数有助于维持生成质量
      - **更大模型多样性**：在训练循环中使用多样化的模型架构和参数设置
      - **冻结模型重标注**：在递归训练中至少维持一个冻结模型进行重标注，防止累积错误
      - **平衡训练策略**：混合真实和合成数据，避免完全依赖合成数据
  - **实验设计**：
      - **受控实验**：设计受控的多代训练实验，系统性地测量坍塌指标
      - **多指标评估**：使用多样化的质量指标（CLIP分数、FID、BLEU等）全面评估坍塌现象
      - **跨架构验证**：在不同的VLM和扩散模型架构上验证发现的普遍性
  - **理论洞察**：
      - **多模态复杂性**：多模态系统由于跨模态交互的额外复杂性，坍塌模式更加微妙
      - **信息流动**：跨模态信息流动如何影响坍塌传播和累积错误
      - **稳定性分析**：不同模态间的稳定性相互依赖关系分析
  - **实际意义**：
      - **训练指导**：为使用合成数据训练多模态模型提供实用指导原则
      - **质量控制**：建立多模态合成数据质量评估的基准方法
      - **风险缓解**：识别和预防多模态训练中的坍塌风险
  - **机构**：未在摘要中明确指出，需要查阅完整论文
  - **开源状态**：⚠️ 需要确认具体的代码和数据可用性
  - **重要价值**：
      - **理论贡献**：为理解多模态生成系统的稳定性提供重要理论基础
      - **实践指导**：为多模态AI系统的安全和可靠训练提供关键洞察
      - **未来研究**：为多模态合成数据研究建立重要的理论框架
      - **行业影响**：对依赖合成数据的多模态AI产品开发具有重要指导意义
  

</details>
---

## 📦 典型多模态数据集

> **Note**: This section lists influential large-scale multimodal datasets that serve as foundations for training vision-language models. These are typically curated from multiple sources and represent significant data aggregation/curation efforts.

### 📦 Interleaved Image-Text Datasets

These datasets consist of documents with images and text interleaved in natural reading order, preserving the original structure of web pages, articles, and documents. They are essential for training models on long-context multimodal understanding and generation.

| Dataset | Scale | Description | Links |
|---------|-------|-------------|-------|
| **OmniCorpus** | 8.6B images<br/>1,696B tokens | Massive interleaved image-text corpus emphasizing **unified data engine** and **multi-lingual, multi-source** coverage. Includes comprehensive web-scale data from diverse domains and languages. | [📄 Paper](https://arxiv.org/abs/2506.03448) |
| **OBELICS** | 141M documents<br/>353M images<br/>115B tokens | Open web-scale filtered dataset from CommonCrawl. Features **comprehensive filtering strategies** and **preserves original web page structure**. Extraction and filtering pipeline fully documented. | [📄 Paper (NeurIPS 2023 D&B)](https://arxiv.org/abs/2306.16527) |
| **MMC4 (Multimodal C4)** | 101.2M documents<br/>571M images<br/>43B tokens | Augmentation of text-only C4 corpus with images. Uses **linear assignment algorithm** with **CLIP features** for image-sentence alignment. Currently partially re-hosted with dataset splits available. | [📄 Paper (NeurIPS 2023 D&B)](https://arxiv.org/abs/2304.06939) |
| **CoMM** | 227K documents<br/>2.28M images<br/>139M tokens | High-quality **coherent** interleaved dataset with **multi-perspective filtering** (text coherence, image consistency, alignment). Emphasizes quality over quantity. See [Methods](#-methods-by-image-processing-type) for detailed methodology. | [📄 Paper (CVPR 2025)](https://arxiv.org/abs/2406.10462) |

| **VLM Dialog Games for Self‑Improvement** | Method-focused dataset | **Dialog-game-based self-improvement data synthesis** — Two VLM agents play a reference game on unlabeled images; successful dialogs are filtered and used for fine-tuning, enabling iterative self-improvement. Key: self-play data generation with automatic quality control, difficulty control. | [📄 Paper (arXiv 2502.02740)](https://arxiv.org/abs/2502.02740) |

### 📊 Domain-Specific & Knowledge-Oriented Datasets

These datasets target specific domains (e.g., remote sensing, entities) or knowledge-intensive tasks, often involving specialized data construction pipelines tailored to domain requirements.

| Dataset | Scale | Description | Links |
|---------|-------|-------------|-------|
| **MMM-RS** | 2.1M text-image pairs | **Remote sensing** multimodal dataset for text-to-image generation. Features **multi-modal** (optical, SAR), **multi-GSD** (ground sampling distance), **multi-scene** (fog, snow, low-light) coverage. Standardizes 9 public RS datasets with automated captioning and synthetic scene augmentation. | [📄 Paper (NeurIPS 2024 D&B)](https://arxiv.org/abs/2307.14878) |
| **MESED** | 14,489 entities<br/>434,675 image-text pairs | **Multi-modal Entity Set Expansion** dataset with **fine-grained semantic classes** and **hard negative entities**. Designed for knowledge/entity-centric tasks. Includes baseline model MultiExpan. | [📄 Paper (AAAI 2024)](https://arxiv.org/abs/2406.08418) |

### 🎓 Large-Scale General Training Datasets

| Dataset | Scale | Description | Links |
|---------|-------|-------------|-------|
| **FineVision** | 24.3M samples<br/>17.3M images | Comprehensive multimodal dataset from 200+ sources, covering 9 categories: General VQA, OCR, Chart/Table, Document, Grounding, Math, Science, Vision-Centric, and World Knowledge | [🤗 HuggingFace](https://huggingface.co/datasets/HuggingFaceM4/FineVision) \| [📄 Paper](https://arxiv.org/abs/2510.17269) |
| **LLaVA-OneVision** | ~4M samples | Unified high-quality dataset covering single-image, multi-image, and video scenarios | [🤗 HuggingFace](https://huggingface.co/datasets/lmms-lab/LLaVA-OneVision-Data) \| [📄 Paper](https://arxiv.org/abs/2408.03326) |
| **PixMo** | Multiple subsets | Suite of datasets (PixMo-Cap, PixMo-AskModelAnything, etc.) for training open vision-language models | [🤗 HuggingFace](https://huggingface.co/collections/allenai/pixmo-674746ea613028006285687b) \| [📄 Paper](https://arxiv.org/abs/2409.17146) |
| **MAmmoTH-VL** | 12M samples | Large-scale multimodal instruction tuning dataset for enhancing reasoning abilities of MLLMs | [🤗 HuggingFace](https://huggingface.co/datasets/MAmmoTH-VL/MAmmoTH-VL-Instruct-12M) \| [📄 Paper](https://arxiv.org/abs/2412.05237) |

### 🎨 Image Editing Datasets

| Dataset | Scale | Description | Cross-Reference |
|---------|-------|-------------|-----------------|
| **ByteMorph-6M** | 6M editing triplets | **Non-rigid motion editing** dataset (camera motion, object deformation, human articulation, HOI). Motion-guided layered compositing + GPT-4o captioning. | See [Methods → Image Editing](#-image-editing-method--data) |
| **ImgEdit** | 1.2M editing triplets | **Unified editing dataset** covering 8 editing categories. VLM + detection + segmentation + in-painting pipeline. Strong on multi-turn editing with identity consistency. | See [Methods → Image Editing](#-image-editing-method--data) |
| **RefEdit** | 20K editing triplets | **Referring expression-guided editing**. High-quality synthetic data via GPT-4o + Grounded-SAM + FlowChef. Demonstrates quality > quantity (outperforms million-scale baselines). | See [Methods → Image Editing](#-image-editing-method--data) |
| **RefCOCO-Edit** | Small-scale benchmark | **Early RIE benchmark** derived from RefCOCO. First systematic formulation of Referring Image Editing task. | See [Methods → Image Editing](#-image-editing-method--data) \| [Benchmark Datasets](#-benchmark-datasets) |

---

## 📊 基准数据集

### 🎯 指令遵循基准

| Benchmark | Description | Link |
|-----------|-------------|------|
| MMBench | Comprehensive multimodal capability evaluation | [GitHub](https://github.com/open-compass/MMBench) |
| SEED-Bench | Hierarchical multimodal understanding evaluation | [GitHub](https://github.com/AILab-CVC/SEED-Bench) |
| LLaVA-Bench | Evaluates conversation, detailed description, and complex reasoning in-the-wild | [🤗 HuggingFace](https://huggingface.co/datasets/lmms-lab/llava-bench-in-the-wild) |

### 📝 Task-Specific Benchmarks

| Benchmark | Description | Link |
|-----------|-------------|------|
| VQAv2 | Visual question answering | [Website](https://visualqa.org/) |
| GQA | Compositional reasoning evaluation | [Website](https://cs.stanford.edu/people/dorarad/gqa/) |
| MMMU | Massive multi-discipline multimodal understanding and reasoning | [Website](https://mmmu-benchmark.github.io/) |

---

## 🎓 资源

### 💡 具有启发性的重要工作

| Paper | Year | Significance | Link |
|-------|------|--------------|------|
| Magpie: Alignment Data Synthesis from Scratch | 2024 | Core inspiration for Oasis, self-aligned instruction generation in text domain | [arXiv](https://arxiv.org/abs/2406.08464) |

> ⚠️ **Note**: Magpie itself is a pure text LLM method, not multimodal data synthesis

### 📖 Survey Papers (Covering Data Synthesis)

| Paper | Year | Focus | Link |
|-------|------|-------|------|
| A Survey on Multimodal Large Language Models | 2023 | Section 3.2 specifically discusses training data construction | [arXiv](https://arxiv.org/abs/2306.13549) |
| Multimodal Foundation Models: From Specialists to General-Purpose Assistants | 2024 | Includes survey of data collection and synthesis methods | [arXiv](https://arxiv.org/abs/2309.10020) |

### 🔗 Related Awesome Lists

| List | Description | Link |
|------|-------------|------|
| Awesome Data for LLM | LLM data engineering (text domain) | [GitHub](https://github.com/weAIDB/awesome-data-llm) |
| Awesome Scientific Datasets and LLMs | Scientific domain datasets | [GitHub](https://github.com/open-sciencelab/Awesome-Scientific-Datasets-and-LLMs) |
| Awesome Multimodal ML | Comprehensive multimodal ML resources | [GitHub](https://github.com/pliang279/awesome-multimodal-ml) |

### 📝 Important Blogs

| Blog | Description | Link |
|------|-------------|------|
| LLaVA Blog | Detailed explanation of LLaVA series data generation methods | [Website](https://llava-vl.github.io/) |
| HuggingFace Blog | Multimodal data and model tutorials | [Website](https://huggingface.co/blog) |

---

## 🤝 贡献指南

We welcome contributions of all forms! Including but not limited to:

- 🆕 Adding new papers, tools, or datasets
- 📝 Improving descriptions of existing entries
- 🐛 Fixing errors or outdated information
- 💡 Suggesting improvements

### How to Contribute

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Guidelines

- When adding new entries, please ensure they include:
  - 📄 Paper/tool name and link
  - 📝 Clear and concise description (1-2 sentences)
  - 🔗 Related links (code, dataset, blog, etc.)
- Maintain entries in alphabetical or importance order
- Ensure links are valid and point to official resources
- Use English for descriptions

---

## ⭐ Star历史

If this project helps you, please give us a Star ⭐️!

[![Star History Chart](https://api.star-history.com/svg?repos=opendatalab-raiser/awesome-multimodal-data-recipe&type=Date)](https://star-history.com/#opendatalab-raiser/awesome-multimodal-data-recipe&Date)

---

## 📄 许可证

This project is licensed under [MIT License](LICENSE).

---

## 🙏 致谢

Thanks to all researchers and engineers who have contributed to the field of multimodal data synthesis!

Special thanks to the following projects for inspiration:
- [awesome-data-llm](https://github.com/weAIDB/awesome-data-llm)
- [Awesome-Scientific-Datasets-and-LLMs](https://github.com/open-sciencelab/Awesome-Scientific-Datasets-and-LLMs)

---

<p align="center">
  Made with ❤️ by the multimodal research community
</p>

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

## 🏢 Industrial & Open-Source Data Synthesis

> This section features works with explicitly documented data synthesis pipelines. **Only includes projects with detailed descriptions of data construction and synthesis methods.**

### Baidu - Qianfan-VL

<details>
<summary>Click to expand</summary>

**Paper**: [Qianfan-VL: Domain-Enhanced Universal Vision-Language Models](https://arxiv.org/abs/2509.18189)

**Publication**: arXiv September 2025

**Institution**: Qianfan Team, Baidu AI Cloud

**📊 Data Synthesis Method (Introduction & Section 3.2)**:

Qianfan-VL developed **comprehensive data synthesis pipelines** for critical enterprise scenarios, covering six major task categories:

**1. Synthesis Scope** (Introduction clearly states):
> "Our synthesis covers **six major task categories**: document OCR, mathematical problem-solving, chart understanding, table recognition, formula recognition, and natural scene OCR."

**Task Categories**:
- **Document OCR**: Synthetic document image generation with annotations
- **Mathematical Problem-Solving**: Automated math problem and solution generation
- **Chart Understanding**: Programmatic chart generation with QA pairs
- **Table Recognition**: Synthetic table structure and content generation
- **Formula Recognition**: Mathematical formula rendering and annotation
- **Natural Scene OCR**: Scene text image synthesis

**2. Synthesis Methodology** (Introduction):
> "By **combining traditional computer vision models with programmatic generation techniques**, we create high-quality training data at scale."

**Key Techniques**:
- **Traditional CV Models**: Leverages existing computer vision models for annotation
- **Programmatic Generation**: Uses code-based generation for structured content
- **Domain-Specific Augmentation**: Custom augmentation strategies for each task type
- **Quality Verification Mechanisms**: Automated quality checks to ensure data reliability

**3. Training Data Scale** (Section 3.1 - Four-Stage Progressive Training):
- Cross-modal Alignment: 100B tokens
- General Knowledge Injection: 2.66T tokens
- **Domain Enhancement: 0.32T tokens** (synthetic data applied here)
- Instruction Tuning: 1B tokens

**4. Quality Assurance** (Introduction):
> "Each pipeline incorporates **domain-specific augmentation strategies and quality verification mechanisms** to ensure data reliability."

**Model Variants & Capabilities**:
- **Qianfan-VL-3B**: 32K context, optimized for edge devices and real-time OCR
- **Qianfan-VL-8B**: 32K context, with chain-of-thought, for servers and general applications
- **Qianfan-VL-70B**: 32K context, with chain-of-thought, for cloud and complex reasoning

**Experimental Results**:
- **OCRBench**: 873 score (70B variant)
- **DocVQA**: 94.75% accuracy (70B variant)
- **MathVista**: 78.6% score (70B variant)
- Strong performance on general benchmarks: CCBench, SEEDBench_IMG, ScienceQA, MMStar

**Training Infrastructure**:
- Trained entirely on Baidu's **Kunlun P800 chips**
- Achieved **>90% scaling efficiency** on 5000+ chip clusters
- Demonstrates feasibility of proprietary hardware for SOTA model training

**✅ Technical Report**:
- [arXiv:2509.18189](https://arxiv.org/abs/2509.18189)
- Comprehensive methodology for domain-enhanced multimodal models

**Significance**:
- **Multi-domain synthesis**: Covers six critical enterprise task categories
- **Hybrid approach**: Combines CV models with programmatic generation
- **Large-scale application**: 0.32T tokens of domain-specific synthetic data
- **Quality-focused**: Incorporates verification mechanisms throughout pipeline
- **Production-ready**: Designed for enterprise deployment scenarios

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
<summary>Click to expand</summary>

**Paper**: [MMEvol: Empowering Multimodal Large Language Models with Evol-Instruct](https://arxiv.org/abs/2409.05840)

**Institution**: Alibaba DAMO Academy (Fei Huang, Yongbin Li, et al.)

**📊 Data Synthesis Method (Explicitly Described)**:

MMEvol proposes a **multimodal instruction evolution framework** that iteratively enhances data quality and complexity:

1. **Core Method - Evol-Instruct Paradigm** (Based on text-domain Evol-Instruct):
   - Starts from initial seed data **SEED-163K**
   - **Iterative Evolution**: Continuously improves instruction data through multiple rounds
   - Three evolution dimensions:
     a) **Fine-grained Perception**: Mines detailed information in images
     b) **Cognitive Reasoning**: Extends visual reasoning steps to enhance reasoning capabilities
     c) **Interaction Evolution**: Enhances diversity of instruction types

2. **Data Evolution Pipeline**:
   - Initial instruction → Evolution operation → More complex/diverse instructions
   - Systematically expands instruction type diversity
   - Gradually increases visual reasoning complexity
   - Deeply explores fine-grained information in images

3. **Experimental Results** (Section 5):
   - Compared to baseline models (using seed data), **average accuracy improvement of 3.1 percentage points**
   - **Achieves SOTA on 9 tasks** with less data
   - Comprehensive evaluation on 13 vision-language tasks

**Data Scale**:
- Initial seed: SEED-163K
- Generates more diverse and complex data through evolution

**✅ Paper**:
- [arXiv:2409.05840](https://arxiv.org/abs/2409.05840)
- Latest version: v5 (December 31, 2024)

**Relation to Oasis**:
- Oasis paper uses MMEvol as a comparison method
- MMEvol focuses on iteratively evolving existing data, while Oasis focuses on generating data from single images
- Both methods enhance data diversity and quality

</details>

### ByteDance - Oasis

<details>
<summary>Click to expand</summary>

**Paper**: [Oasis: One Image is All You Need for Multimodal Instruction Data Synthesis](https://arxiv.org/html/2503.08741v2)

**📊 Data Synthesis Method (Section 3.2 Detailed Description)**:

**This is breakthrough work!** Oasis proposes a minimalist data synthesis method, inspired by Magpie but applied to the multimodal domain:

1. **Core Innovation - "Hooking" Prompt** (Section 3.2 Step 1):

   **Key Breakthrough**:
   - **Only inputs images**, no text prompts required!
   - Lets MLLM (e.g., Qwen2-VL) generate instructions itself
   - Utilizes the auto-regressive nature of models to automatically generate diverse questions based on images

   **Why It Works**:
   - Breaks traditional fixed prompt patterns, significantly enhancing data diversity
   - Models generate questions based on their knowledge, providing broader coverage
   - Simple and efficient, no need for manually designed complex prompts

2. **Data Categorization** (Section 3.2 Step 2):
   - Uses LLM to filter out non-instruction data (e.g., pure descriptive text)
   - Ensures all generated data are in question-answer format

3. **Four-Dimensional Quality Control** (Section 3.2 Step 3, Appendix B.2 fully disclosed):

   The paper designs rigorous quality assessment criteria (1-5 scale):

   a) **Solvability**: Whether the image contains sufficient information to answer the question
   b) **Hallucination**: Whether the question is consistent with image content
   c) **Clarity**: Whether the question is clearly expressed
   d) **Nonsense**: Whether the question is grammatically correct and logically sound

   - Each dimension has detailed scoring criteria (Appendix B.2 complete prompts)
   - Multi-dimensional comprehensive assessment ensures high quality

**Data Scale**:
- Generated 500K high-quality instruction data
- Validated effectiveness on LLaVA-NeXT

**Domain Customization Capability**:
- Since it only depends on images, domain-specific data can be generated by controlling image sources
- Paper demonstrates OCR domain cases (Section 4.3)

**Experimental Results** (Section 4.2):
- Significant performance improvement on 14 benchmarks
- Outperforms other data synthesis methods (including LLaVA, ALLAVA, MMEvol, etc.)

**Comparison Methods Mentioned in Oasis Paper** (Section 4.2):
- **LLaVA** [24]: GPT-4 assisted generation (entry below, see "LLaVA Series")
- **MMEvol** [29]: Alibaba DAMO Academy's image-text instruction evolution framework (entry above, see "Alibaba - MMEvol")
- **ALLaVA** [4]: Captioning-then-QA approach (entry below, see "Methods by Image Processing Type")

**Oasis Inspiration Source**:
- **Magpie** [43]: Text-domain self-aligned instruction generation method (inspired Oasis's "hooking prompt" core idea)
  - Oasis extends Magpie's idea to the multimodal domain, achieving instruction generation with only images

**✅ Fully Open Source**:
- Paper promises to open-source 500K data and models
- All quality control prompts are publicly available in Appendix B

**Significance**:
- **Minimalist Methodology**: Only requires images, no captions or other text needed
- **Quality Assurance**: Four-dimensional quality control is highly systematic
- **Reproducible**: All prompts and methods are fully disclosed

</details>

### Microsoft - Florence-2

<details>
<summary>Click to expand</summary>

**Paper**: [Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks](https://arxiv.org/abs/2311.06242)

**Publication**: arXiv November 2023

**Institution**: Azure AI, Microsoft

**📊 Data Synthesis Method (Introduction & Section 2)**:

Florence-2 developed an **automated data engine** to generate the large-scale **FLD-5B** dataset:

1. **Data Scale** (Abstract):
   - **5.4 billion comprehensive visual annotations**
   - Covering **126 million images**
   - One of the largest automatically annotated multimodal datasets

2. **Automated Data Engine - Two-Module Pipeline** (Introduction, Page 2):

   **Module 1 - Collaborative Automated Annotation**:
   > "uses specialized models to collaboratively and autonomously annotate images, moving away from the traditional single and manual annotation approach. Multiple models work together to reach a consensus"

   - Utilizes multiple specialized models for collaborative image annotation
   - Models reach consensus through multi-model agreement (inspired by "wisdom of crowds" concept)
   - Ensures more reliable and unbiased image understanding
   - Fully automated, eliminating manual annotation needs

   **Module 2 - Iterative Refinement & Filtering**:
   > "iteratively refines and filters these automated annotations using well-trained foundational models"

   - Uses well-trained foundation models to iteratively refine and filter annotations
   - **Iterative strategy**: Model annotation → Refinement → Model retraining → Re-annotation cycle
   - Continuously improves annotation quality

3. **Annotation Coverage** (Introduction):
   The FLD-5B dataset encompasses multiple vision tasks:
   - **Image captioning** (various semantic granularities)
   - **Object detection** (spatial hierarchy understanding)
   - **Grounding** (text-region alignment)
   - **Segmentation** (fine-grained visual understanding)

4. **Core Innovation**:
   - **Fully automated pipeline**: No human annotation required
   - **Multi-task unified format**: All annotations converted to text format for unified learning
   - **Iterative improvement**: Continuous quality enhancement through model-annotation co-evolution
   - **Billion-scale**: Achieves unprecedented annotation scale

**Model Architecture**:
- Sequence-to-sequence (seq2seq) structure
- Unified prompt-based representation for diverse vision tasks
- Single model handles multiple tasks without task-specific architectural modifications

**Experimental Results**:
- **Zero-shot SOTA**: Achieves new state-of-the-art zero-shot performance on COCO captioning, Flickr30k visual grounding, RefCOCO/+/g referring expression comprehension
- **Transfer learning**: Substantially outperforms ImageNet pre-training, improving by 6.9, 5.5, and 5.9 points on COCO and ADE20K datasets
- **Training efficiency**: 4× faster than supervised pre-training

**✅ Open Source**:
- Model: Available on HuggingFace
- Code: [Microsoft Florence](https://github.com/microsoft/Florence)

**Significance**:
- **Industrial-scale data engine**: Demonstrates feasibility of fully automated large-scale annotation
- **Multi-task synthesis**: Unified approach to generating diverse annotation types
- **Quality through consensus**: Multi-model collaboration ensures annotation reliability

</details>

### Tencent Hunyuan - Bee, HoneyPipe & DataStudio

<details>
<summary>Click to expand</summary>

**Paper**: [Bee: A High-Quality Corpus and Full-Stack Suite to Unlock Advanced Fully Open MLLMs](https://arxiv.org/abs/2510.13795)

**Publication**: arXiv October 2025

**Institution**: Tencent Hunyuan Team & Tsinghua University

**Authors**: Yi Zhang, Bolin Ni, Xin-Sheng Chen, Heng-Rui Zhang, Yongming Rao, Houwen Peng, Qinglin Lu, Han Hu, Meng-Hao Guo, Shi-Min Hu

**📊 Three-Fold Contributions**:

**1. Honey-Data-15M**: A 15M-sample SFT dataset meticulously cleaned and enriched with dual-level Chain-of-Thought reasoning

**2. HoneyPipe + DataStudio**: The data curation pipeline and its underlying modular framework, providing transparent and adaptable methodology

**3. Bee-8B**: An 8B model establishing new SOTA among fully open MLLMs, competitive with semi-open models like InternVL3.5-8B

---

**📊 Data Synthesis Method - HoneyPipe (Section 2)**:

HoneyPipe is an **automated and reproducible workflow** built from **DataStudio's modular components**, featuring a nuanced **dual-level reasoning enrichment strategy**: a foundational path for large-scale short CoT enrichment + a specialized loop for long CoT responses to complex instructions.

**🔧 Stage 1: Data Aggregation and Preparation**
- **Initial Pool**: ~24 million image-text pairs from diverse community datasets
  - Sources: LLaVA-OneVision, PixMo, MAmmoTH-VL, etc.
  - Challenge: Significant content overlap
- **Rigorous Deduplication** (pair-level):
  - Method: Perceptual hash (images) + Simhash (instructions)
  - Removal criteria: **BOTH** image AND instruction must be identical
  - Purpose: Maximize diversity, enhance processing efficiency
- **Domain Labeling**: Manual inspection and categorization
  - Domains: General, Chart, OCR, STEM, etc.
  - Purpose: Guide subsequent processing
- **Output**: Clean, unique image-instruction-response triplets with domain labels

**🔧 Stage 2: Noise and Irrelevance Filtering**
- **Rule-Based Operators** (formatting issues):
  - Remove samples with very small images
  - Filter extreme aspect ratios
  - Eliminate repeated text in instructions
- **Model-Based Filtering Operator** (using **Qwen2.5-VL-72B**):
  - Assess: Is instruction logical and answerable?
  - Verify: Is instruction semantically related to visual content?
  - Example: Flag "solve the function problem" as irrelevant to image of oranges
- **Result**: Effectively pruned flawed samples, producing clean image-instruction pairs

**🔧 Stage 3: Short CoT Enrichment and Verification** (Foundational Path)

*This stage targets instructions requiring moderate reasoning*

**Data Triage**:
- CV tasks (OCR, object detection) → **bypass enrichment** → final dataset
- Other samples → proceed to CoT enrichment

**Short CoT Enrichment** (~12.2M samples):
- **Preprocessing**: Remove prompts discouraging reasoning
  - Remove: "Answer directly", and similar head/tail prompts
  - Purpose: Elicit comprehensive, step-by-step responses
- **Generation**: Use **Qwen2.5-VL-72B/32B** (powerful open-source MLLMs)
  - Transform simple short-form responses → detailed reasoning paths
  - **No extra system prompts**: Models already adept at multi-step responses
  - Constraint avoidance: Preserve output diversity
- **Primary source** of 12.2M short CoT samples

**Fidelity Verification** (LLM-as-a-Judge):
- **Verifier Model**: Qwen2.5-VL-72B
- **Method**: Semantic comparison between newly generated CoT final conclusion and original response
- **Evaluation Criteria** (twofold):
  - **Factual queries** (objective): Final responses must match **precisely**
  - **Descriptive queries** (subjective): Thematic relevance and semantic consistency required
- **Pass** → added to final dataset
- **Fail** → **NOT discarded**, routed to long CoT enrichment loop for specialized enrichment

**🔧 Stage 4: Long CoT Enrichment Loop** (Specialized Path for Complex Instructions)

*Designed specifically for most complex instructions demanding deep, multi-step problem-solving*

**Input Sources** (3 primary types):
1. **Samples failing** Stage 3 fidelity verification
2. **Select data sources** identified as inherently complex
   - Example: VisualWebInstruct
   - Strategy: Proactively generate long CoT **in addition** to short CoT counterpart
3. **Validated datasets** from prior research
   - Example: Vision-R1
   - Criterion: Particularly suitable for generating deep reasoning chains

**Deep Reasoning Generation** (~2.7M samples):
- **Models**: Leverage **top proprietary MLLMs** for more detailed solutions
- **Process**:
  - First generates deep reasoning (often structured with `<think></think>` tags)
  - Then outputs final response
- **Capability**: Handles complex instructions beyond reach of initial open-source models

**Final Fidelity Verification**:
- Same verification process as Stage 3
- **Pass** → constitutes ~2.7M long CoT data points in Honey-Data-15M
- **Fail** → **discarded** (assumed erroneous, unsolvable, or too costly to annotate)

---

**📦 Final Dataset - Honey-Data-15M**:

**Scale**: 15 million meticulously curated samples

**Composition** (7 major domains):
- General (36.8%): Foundational visual understanding
- Chart (24.6%): Chart understanding and reasoning
- Caption (15.1%): Image captioning
- STEM (7.6%): Symbolic reasoning (math, science, geometry)
- Document (5.9%): Document understanding and OCR
- Grounding & Counting (5.1%): Object detection and counting
- OCR (4.9%): Text recognition in various contexts

**Dual-Level CoT Backbone**:
- **~12.2M short CoT samples**: Foundational, step-by-step logical inference for moderate reasoning
- **~2.7M long CoT samples**: Intricate, multi-step reasoning for complex problem-solving requiring deeper synthesis
- **Targeted approach**: Tailors response depth to instruction complexity
- **Inherent solution**: Identifies which instructions warrant elaborate multi-step solutions

---

**🤖 Bee-8B Model - Validation & Performance**:

**Architecture**:
- LLM: Qwen3-8B (reasoning and text generation)
- Vision Encoder: SigLIP2-so400m-patch14-384
- Resolution Strategy: Anyres (handles varying resolutions, preserves fine-grained details)
- Projector: Two-layer MLP with GELU activation

**Training**: 5-stage progressive process (details in Section 3.2)

**Performance Highlights** (establishes new SOTA for fully open MLLMs):

*General VQA*:
- **MMMU**: 66.8 (competitive with semi-open models)
- **MMMU-Pro**: 50.7 (**3.6% lead** over Qwen2.5-VL-7B)
- **MMStar**: 71.4
- **MMVet**: 83.9
- **MMVP**: 82.0

*Math & Reasoning* (standout performance):
- **MathVista mini**: 81.4
- **MathVerse** (vision_only): 67.0
- **MathVision**: 50.0
- **LogicVista**: 61.3
- **DynaMath** (worst): 40.5
- **WeMath**: 59.8

*Key Observation*: Most significant advantages in **factual accuracy** and **complex multi-step reasoning**, directly reflecting strengths of Honey-Data-15M

**Comprehensive Ablation Study**:
- Quantifies impact of each curation stage
- Shows significant improvements across multiple benchmarks
- Confirms: Focus on data quality > competing on data volume
- Evidence: Data cleaning + CoT enrichment are critical

---

**🎯 Core Innovation - Dual-Level CoT Strategy**:

1. **Progressive Enhancement**: Gradual quality improvement instead of simple discard
2. **Failed Sample Recovery**: Samples failing short CoT verification get specialized long CoT enrichment
3. **Model-Driven Process**: MLLM-automated workflow (scalable, economical alternative to human annotation)
4. **Complexity Identification**: Inherently solves challenge of identifying which instructions need deep reasoning

---

**✅ Open Source Resources**:
- **Project Page**: https://open-bee.github.io
- **Paper**: [arXiv:2510.13795](https://arxiv.org/abs/2510.13795)
- **Promised Releases** (full-stack suite):
  - Honey-Data-15M corpus
  - HoneyPipe + DataStudio framework
  - Training recipes
  - Evaluation harness
  - Bee-8B model weights

---

**💡 Significance**:

- **Closing the Gap**: Demonstrates fully open MLLMs can compete with semi-open counterparts through data quality focus
- **Transparent Methodology**: Moves beyond static dataset releases to provide evolving, adaptable curation methods
- **Community Cornerstone**: Provides new foundation resource for fully open MLLM community
- **Scalability**: Model-driven pipeline makes high-quality data construction feasible for open-source community
- **Validation**: Bee-8B's SOTA performance confirms effectiveness of data curation strategy

**Core Thesis Confirmed**: *A principled focus on data quality is a key pathway to developing fully open MLLMs highly competitive with semi-open counterparts*

</details>

### ByteDance - ByteMorph

<details>
<summary>Click to expand</summary>

**Paper**: [ByteMorph: Benchmarking Instruction-Guided Image Editing with Non-Rigid Motions](https://arxiv.org/abs/2506.03107)

**Publication**: arXiv June 2025 (v2: June 2025)

**Institution**: ByteDance Seed, USC, University of Tokyo, UC Berkeley, Stanford, UCLA

**Authors**: Di Chang*, Mingdeng Cao*, Yichun Shi, Bo Liu, Shengqu Cai, Shijie Zhou, Weilin Huang, Gordon Wetzstein, Mohammad Soleymani, Peng Wang (*Equal Contribution)

**📊 Data Synthesis Method - Automated Motion-Guided Data Engine**:

ByteMorph addresses a critical gap in instruction-guided image editing: **non-rigid motion editing**. While existing datasets focus on static edits (object manipulation, style transfer), ByteMorph targets dynamic transformations involving camera motion, object deformation, and human articulation.

**1. Core Innovation - Motion-Guided Layered Compositing Pipeline**

**Four Motion Categories** (systematically defined):
- **Camera Motion (CM)**: Zoom in/out, perspective shifts, pan, tilt, rotate
- **Object Deformation (OD)**: Stretch, bend, squeeze, twist
- **Human Articulation (HA)**: Body pose changes, facial expressions
- **Human-Object Interaction (HOI)**: Grasping, using, manipulating objects

**Automated Data Engine Components**:

**Stage 1 - Video Source Collection & Filtering**:
- **Source**: Web-scale video corpora
- **Filtering Criteria**:
  - High-resolution (≥720p)
  - Stable scenes with clear foreground objects
  - Minimal blur and artifacts
- **Motion Detection**: Optical flow analysis to identify motion-rich segments
- **Result**: Curated video clips exhibiting target motion types

**Stage 2 - Layered Compositing with Motion Transfer**:
- **Method**: Inspired by professional VFX workflows
- **Pipeline**:
  1. Extract consecutive frames from filtered videos
  2. **Foreground Segmentation**: Use segmentation models to isolate moving objects/subjects
  3. **Background Stabilization**: Apply motion compensation to background
  4. **Layer Composition**: Overlay foreground onto new backgrounds with motion preserved
  5. **Quality Control**: Filter composites with visible artifacts
- **Key Advantage**: Preserves realistic motion dynamics while enabling diverse background combinations
- **Innovation**: Automates traditional manual compositing at scale

**Stage 3 - GPT-4o-Assisted Caption Generation**:
- **Model**: GPT-4o (multimodal understanding)
- **Input**: Source + edited image pairs
- **Output Generation**:
  - **Detailed Image Descriptions**: Comprehensive scene understanding for both images
  - **Motion-Aware Instructions**: Natural language commands describing the motion transformation
    - Examples: "make the person raise their right arm", "zoom in on the cat", "bend the tree to the left"
  - **Consistency Verification**: GPT-4o validates instruction-image alignment
- **Prompt Engineering**: Custom prompts emphasizing motion semantics and spatial relationships
- **Scale**: Processes 6M image pairs

**Stage 4 - Quality Assurance & Filtering**:
- **Multi-dimensional Filtering**:
  - **Visual Quality**: CLIP-based aesthetic scoring
  - **Motion Coherence**: Optical flow consistency checks
  - **Instruction Relevance**: LLM-based verification of instruction-edit alignment
  - **Diversity Metrics**: Clustering to ensure coverage across motion types and scene categories
- **Human Validation**: Sample-based quality audits on 5K randomly selected triplets
- **Threshold Calibration**: Iterative refinement of filtering thresholds

**2. ByteMorph-6M Dataset Characteristics**

**Scale & Composition**:
- **Total Size**: 6 million high-resolution image editing triplets
- **Format**: (source image, natural language instruction, edited image)
- **Resolution**: Minimum 512×512, majority 1024×1024
- **Distribution**:
  - Camera Motion: ~1.8M samples
  - Object Deformation: ~1.5M samples
  - Human Articulation: ~1.8M samples
  - Human-Object Interaction: ~0.9M samples

**Quality Attributes**:
- **Instruction Diversity**: Average 15.3 unique words per instruction
- **Motion Granularity**: Both coarse (e.g., "zoom in") and fine-grained (e.g., "tilt camera 15 degrees left") instructions
- **Background Diversity**: 500K+ unique background scenes
- **Object Categories**: 2,000+ object types across 50+ semantic categories

**3. ByteMorph-Bench - Evaluation Benchmark**

**Benchmark Design**:
- **Size**: 613 carefully curated test samples
- **Difficulty Levels**: Easy, Medium, Hard (based on motion complexity)
- **Coverage**: Balanced distribution across four motion categories
- **Annotation**: Expert-verified ground truth edits
- **Metrics**: CLIP similarity, motion accuracy (via optical flow), human evaluation scores

**Challenging Aspects**:
- Complex multi-step motions (e.g., "person waves hand while turning head")
- Fine-grained articulation (e.g., specific finger positions)
- Physics-aware deformations (e.g., realistic cloth bending)
- Contextual interactions (e.g., "person picks up cup from table")

**4. ByteMorpher Model - Diffusion Transformer Baseline**

**Architecture**:
- **Base**: Diffusion Transformer (DiT) architecture
- **Conditioning**: Multi-modal conditioning on both text instructions and source images
- **Training Strategy**:
  - Pre-training on ByteMorph-6M (full dataset)
  - Fine-tuning on ByteMorph-Bench training split
- **Inference**: Classifier-free guidance for instruction adherence

**Performance Highlights**:
- **ByteMorph-Bench**: Outperforms existing instruction-guided editing models (InstructPix2Pix, MagicBrush) by **18.3%** on motion-related metrics
- **Generalization**: Successfully transfers to out-of-domain motion editing tasks
- **Human Evaluation**: Preferred over baselines in **73.5%** of pairwise comparisons

**5. Experimental Results & Insights**

**Key Findings**:
- **Motion-Specific Training Critical**: Models trained on static editing datasets fail on motion tasks (avg. 32.1% success rate)
- **Scale Matters**: Performance scales logarithmically with dataset size (1M→3M→6M)
- **Layered Compositing Superiority**: Outperforms diffusion-based synthesis (+12.7% realism score)
- **GPT-4o Caption Quality**: Human evaluation shows 91.2% instruction accuracy vs. 67.4% for automated VLM captioning

**Benchmark Comparison**:
| Model | CLIP-Sim ↑ | Motion Acc ↑ | Human Pref ↑ |
|-------|------------|--------------|--------------|
| InstructPix2Pix | 0.652 | 0.423 | 21.3% |
| MagicBrush | 0.681 | 0.457 | 24.8% |
| **ByteMorpher** | **0.743** | **0.612** | **73.5%** |

**✅ Open Source Resources**:
- **Paper**: [arXiv:2506.03107](https://arxiv.org/abs/2506.03107)
- **Dataset**: ByteMorph-6M (6M triplets) - Release planned on OpenDataLab
- **Benchmark**: ByteMorph-Bench (613 test samples) - Available with paper
- **Model**: ByteMorpher checkpoints - HuggingFace release promised
- **Code**: Data engine pipeline code - GitHub release promised

**💡 Significance**:

- **Novel Problem Formulation**: First large-scale dataset addressing non-rigid motion in instruction-guided editing
- **Industrial-Scale Automation**: Demonstrates layered compositing approach scalable to millions of samples
- **Motion-Aware Pipeline**: Introduces motion detection and preservation into automated data synthesis
- **Benchmark Contribution**: ByteMorph-Bench fills critical gap in evaluating motion editing capabilities
- **Multimodal LLM Integration**: Showcases effective use of GPT-4o for motion-semantic caption generation
- **Open Science**: Commitment to open-sourcing dataset, benchmark, model, and code

**Research Impact**: ByteMorph expands the scope of instruction-guided image editing from static transformations to dynamic motion-based edits, enabling new applications in video editing, animation, and augmented reality.

</details>

### ByteDance & NTU - LLaVA-OneVision

<details>
<summary>Click to expand</summary>

**Paper**: [LLaVA-OneVision: Easy Visual Task Transfer](https://arxiv.org/abs/2408.03326)

**Publication**: arXiv August 2024 (v3: October 2024)

**Institution**: ByteDance, S-Lab NTU, CUHK, HKUST

**Authors**: Bo Li, Yuanhan Zhang, Dong Guo, Renrui Zhang, Feng Li, Hao Zhang, Kaichen Zhang, Peiyuan Zhang, Yanwei Li, Ziwei Liu, Chunyuan Li

**📊 Data Construction Method (Section 4 - Comprehensive Data Strategy)**:

LLaVA-OneVision represents a significant data-centric approach, emphasizing **"quality over quantity"** in multimodal training. The paper consolidates insights from the LLaVA-NeXT blog series with a carefully curated large-scale dataset collection (accumulated from January to June 2024).

---

**🔬 High-Quality Knowledge Learning (4.7M samples)**

*Core Principle*: Focus on high-quality knowledge learning over web-scale low-quality data, given limited compute budget.

**Key Insight**: **99.8% of high-quality knowledge data is synthetic**, due to high cost and copyright constraints of collecting large-scale high-quality wild data.

**Three Data Categories**:

**1. Re-Captioned Detailed Description Data (3.5M samples)**
- **Method**: **Self-Improvement AI** approach
- **Model**: Uses **LLaVA-NeXT-34B** (known for strong detailed caption ability)
- **Process**: Generate new detailed captions for existing images
- **Sources**: COCO118K, BLIP558K, CC3M
- **Innovation**: Training data generated by an early version of the model itself

**2. Document / OCR Data (1.1M samples)**
- **Text Reading subset**: UReader dataset (100K), easily accessible through PDF rendering
- **Synthetic data**: SynDOG EN/CN for document understanding
- **Purpose**: Enhance text reading and document comprehension capabilities

**3. Chinese and Language Data (235K samples)**
- **Chinese Caption Generation (92K)**:
  - Images: Original ShareGPT4V images
  - Model: **GPT-4V (Azure API)** to generate detailed Chinese descriptions
  - Goal: Improve Chinese language capabilities
- **Language Balance (143K)**:
  - Source: Evo-Instruct dataset
  - Purpose: Balance language understanding ability alongside visual captioning

---

**📦 Visual Instruction Tuning Data (4.8M samples)**

*Goal*: Enable LMM to understand and act upon visual instructions across diverse scenarios

**Data Collection Strategy**:

**Categorization Framework** (Three-Level Hierarchy):

1. **Vision Input**: Single-image / Multi-image / Video
2. **Language Instruction**: General QA, General OCR, Doc/Chart/Screen, Math Reasoning, Language
3. **Language Response**: Free-form (GPT-4V/o, Gemini annotated) vs Fixed-form (academic datasets)

**Curation Process**:
- Collect from various original sources with initially unbalanced ratios
- Incorporate new subsets from Cauldron and Cambrian collections
- **Manual review and formatting**:
  - Correct question/answer formats
  - Adhere to LLaVA-1.5 prompting strategy for multiple-choice, short answer, OCR
  - Prevent conflicts from different data sources
  - Guide model behavior: balance QA performance, conversational ability, reasoning skills

**Data Composition**:

**Single-Image Data (3.2M samples)** - Five major categories:
- **General (36.1%)**: 70+ datasets including ALLaVAInst, AOKVQA, Cambrian, LLaVA-158K, ShareGPT4V/4o, VisionFLAN, etc.
- **Doc/Chart/Screen (20.6%)**: AI2D, ChartQA, DocVQA, UReader series, Chart2Text, etc.
- **Math/Reasoning (20.1%)**: MAVIS series, Geo170K, GeoQA+, GeoMVerse, MathV360K, etc.
- **General OCR (8.9%)**: ChromeWriting, HME100K, OCR-VQA, SynthDog-EN, TextCaps, TextOCR, etc.
- **Language (14.3%)**: MagpiePro (L3MT, L3ST, Qwen2ST) - 450K samples total

**OneVision Mixed Data (1.6M samples)** - Three scenarios:
- **Single-Image (31.2%, ~500K)**: High-quality sampled portions from previous single-image data
  - MagpiePro, VisionFLAN, ImageTextualization, Cauldron, UReader, ShareGPT4V/4o, etc.
- **Multi-Image (43.0%, ~688K)**: 30+ datasets
  - NLVR, Co-Instruct, ScanNet, RAVEN, IconQA, VIST, ContrastiveCaption, etc.
- **Video (25.9%, ~415K)**: 6 datasets
  - ShareGPT4Video (255K), Youcook2, ActivityNet, Charades, NextQA, Ego4D

---

**🎯 Key Innovations & Insights**:

1. **Synthetic Data Dominance**: 99.8% of knowledge data is model-generated
   - Lower cost, easier to scale
   - "Learning from large-scale synthetic data is becoming a trend as AI models grow more powerful"

2. **Self-Improvement AI**: Use LLaVA-NeXT-34B to generate training data for next generation
   - Re-caption 3.5M images with more detailed descriptions
   - Demonstrates feasibility of bootstrapping from own model outputs

3. **Careful Data Balancing**:
   - Task categorization to maintain skill distribution
   - Manual review to prevent data source conflicts
   - Unified prompting strategy across heterogeneous sources

4. **Cross-Scenario Transfer Design**:
   - Insight: Stronger image model → better transfer to multi-image/video tasks
   - Training strategy: Single-image first, then mixed scenarios
   - Data allocation: More tokens for single-image to mimic video representation

5. **Quality Over Quantity Philosophy**:
   - Focus on curation over volume
   - Acknowledge pre-trained LLM/ViT knowledge base
   - Continuous exposure to new high-quality data

---

**📈 Training Strategy (Section 5)**:

**Three-Stage Curriculum Learning**:
- **Stage-1**: Language-Image Alignment
- **Stage-1.5**: High-Quality Knowledge Learning (using 4.7M synthetic data)
- **Stage-2**: Single-Image Instruction Tuning (3.2M samples)
- **Stage-3**: OneVision Mixed Training (1.6M samples)

**Model Architecture**:
- LLM: Qwen-2 (strong language capabilities)
- Vision Encoder: SigLIP (higher performance among open encoders)
- Projector: 2-Layer MLP
- Visual Representation: Higher AnyRes strategy with bilinear interpolation

---

**✅ Performance & Achievements**:

- **First single open model** to push performance boundaries simultaneously in three scenarios:
  - Single-image
  - Multi-image
  - Video understanding
- Strong task transfer capabilities across modalities
- Demonstrates emerging capabilities through cross-scenario transfer
- Video understanding achieved through task transfer from images

---

**✅ Open Source Resources**:
- **Paper**: [arXiv:2408.03326](https://arxiv.org/abs/2408.03326)
- **Project**: https://llava-vl.github.io/blog/llava-onevision
- **Dataset**: [🤗 HuggingFace](https://huggingface.co/datasets/lmms-lab/LLaVA-OneVision-Data)
- **Models**: Model checkpoints released
- **Code**: Codebase open-sourced
- **Demo**: Visual chat demo available

---

**💡 Significance**:

- **Data-Centric Approach**: Consolidates insights from LLaVA-NeXT blog series into comprehensive dataset
- **Synthetic Data Validation**: Proves large-scale synthetic data (99.8%) can achieve SOTA performance
- **Self-Improvement Path**: Demonstrates using own model outputs for next generation training
- **Unified Multi-Scenario**: Single model excels across image/multi-image/video without trade-offs
- **Community Impact**: Full open-source release of data, models, code enables reproducibility

**Core Thesis**: *Quality over quantity in data curation, combined with strategic use of synthetic data and self-improvement, enables building versatile open LMMs competitive with proprietary models.*

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

## 📂 Methods by Image Processing Type

### 🎨 Image Generation - Synthesizing New Visual Content

This category focuses on **generating new images from scratch** as part of the data synthesis pipeline. These methods create synthetic visual content (geometric diagrams, mathematical figures, text-dense scenes, etc.) programmatically or through generative models, paired with corresponding textual annotations.

#### 🔄 Text-Driven Image Synthesis

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2407.20756">📄 SynthVLM</a></b><br>
<code>arXiv 2407.20756</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-ACM_Multimedia_2025-red?style=flat-square"/>
</summary>

  - **Focus**: **Reverse Synthesis: From Text to Image** - Unlike traditional "image→caption", SynthVLM adopts "caption→image" paradigm, using high-quality captions to drive Diffusion models for high-resolution image generation
  - **Data Synthesis Method** - **Two-Stage Selection-Generation-Reselection**:
      - **Core Innovation**: First systematic framework proposing caption-to-image generation for VLM pre-training data synthesis, solving Web data's "watermark/ads/low-quality" trifecta
      - **Stage 1: Caption Selection** (Building high-quality seeds):
        - **Data Sources**: Aggregate human-annotated (LAION, CC, SBU) + model-generated (BLIP2 re-captioning DataComp)
        - **Two-Round Filtering**:
          1. **Quality Filtering**: ChatGPT + statistical metrics (N-gram, Perplexity) remove ads, duplicates, grammar errors
          2. **Alignment Filtering**: Compute caption-original image CLIPScore, select top 40% (1M captions)
      - **Stage 2: Image Generation + Quality Screening**:
        - **Generation**: Use **Stable Diffusion XL (SDXL)** to generate **1024×1024 high-resolution images** for 1M captions (60 sampling steps, grid-searched hyperparams)
        - **Dual-Metric Screening**:
          - **CLIPScore(I, C)**: Evaluates image-text semantic alignment
          - **SSIMScore(I, I_resized)**: Evaluates image quality (simulates 336px resize loss)
          - **Weighted Formula**: Weighted_Score = CLIPScore + 0.5 × SSIMScore
        - **Selection**: Top 100K pairs → **SynthVLM-100K**
      - **Key Technical Details**:
        - **Avoids Artifacts**: Generated images naturally watermark-free, ad-free (common issues in Web images)
        - **Higher Resolution**: 1024×1024 vs. Web images typically 336×520
        - **Better Alignment**: SynthVLM-100K average CLIPScore=0.36, SSIMScore=0.86, significantly higher than COCO-Caption(0.31/0.73), BLIP-LCS(0.32/0.75), ShareGPT4V(0.32/0.79)
  - **Evaluation & Validation**:
      - **GPT-4V + InternVL2 + Human Evaluation**: 1K sample blind test, synthetic images win rate **63.3%(GPT-4V), 69.2%(InternVL2), 75.8%(Human)**
      - **Downstream Tasks**: SynthVLM-7B/13B achieve SOTA with only 100K pre-training data (18% of LLaVA), comprehensively surpassing LLaVA on VQAv2, GQA, MMBench, MME, etc.
      - **Language Ability Preservation**: MMLU benchmark shows SynthVLM-7B achieves 41.2 (vs. LLaVA 36.3), proving synthetic data doesn't harm language understanding
  - **Data Scale**:
      - **Intermediate Pool**: 1M high-quality captions
      - **Final Dataset**: **SynthVLM-100K** (100K synthetic image-text pairs)
  - **Open Source**: ✅ [GitHub](https://github.com/starriver030515/SynthVLM)
  - **Institution**: Peking University + Huawei + Shanghai AI Lab
  - **Publication**: ACM MM 2025 | arXiv July 2024
  

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

  - **Focus**: **Large-Scale 3D Visual Instruction Dataset Generation for Camera-Object Relation Understanding** - Automatically generate 240K VQA data with precise camera-object relation annotations using 3D assets + rendering + diffusion models
  - **Data Synthesis Method** - **3D Rendering + Multi-ControlNet Diffusion + LLM Four-Step Pipeline**:
      - **Core Innovation**: First systematic framework utilizing 3D assets to generate photorealistic images and camera-object relation VQA data, addressing dataset bias in MLLMs' spatial understanding
      - **Problem Identification**:
        - Existing MLLMs show significant deficiencies in camera-object relation understanding (GPT-4o achieves only 43.1% on object orientation tasks)
        - Root cause: Severe bias in training datasets (most images captured from front-facing, side, or above viewpoints)
        - Lack of high-quality annotated data with diverse camera-object relations
      - **Four-Step Generation Pipeline**:
        1. **3D Visual Prior Rendering (Stage 1)**:
           - **Input**: 3D asset A (from open-source libraries like Objaverse), arbitrary camera-object relation parameter β
           - **Camera-Object Relation Definition**:
             - **Azimuth φ**: Object rotation angle relative to camera, divided into 8 directions (right, front-right, front, front-left, left, back-left, back, back-right), each covering π/4 radians
             - **Elevation θ**: Camera elevation angle, divided into 3 categories (top view, horizontal, bottom view)
             - **Distance**: Camera-to-object distance, divided into 3 categories (close-up, medium shot, long shot)
           - **Renderer**: Blender 3D engine
           - **Output multimodal visual priors I_β**:
             - RGB images
             - Pixel-level depth maps (DepthAnyThing V2)
             - Semantic segmentation masks
             - Canny edge detection maps
           - **Key Advantage**: Preserves precise ground truth camera-object relation β as strong constraints for subsequent image generation
        2. **Diverse Image Description Generation (Stage 2)**:
           - **LLM**: GPT-4o
           - **Prompt Engineering**:
             - **System Prompt**: Guides LLM to generate diverse descriptions of background context and object appearance details
             - **Few-shot Examples**: Provides style references to ensure description naturalness
           - **Output T_img**: Detailed image description text, including:
             - Background scene description (indoor/outdoor, lighting conditions, environmental atmosphere)
             - Object detail description (material, color, state)
             - Contextual information (object's role in the scene)
           - **Diversity Guarantee**: Generates multiple different scene descriptions for the same 3D asset category to enhance data diversity
        3. **Controlled Photorealistic Image Generation (Stage 3)**:
           - **Core Technology**: Multi-ControlNet stacking + SDXL diffusion model
           - **Conditional Inputs**:
             - Visual conditions: Depth map + Canny edge map (from Stage 1)
             - Text condition: Image description T_img (from Stage 2)
           - **Multi-ControlNet Architecture**:
             - **Depth ControlNet**: Weight 0.5, maintains object 3D geometric structure
             - **Canny ControlNet**: Weight 0.8, maintains object edges and contours
             - **Formula**: z_{t-1} = G_θ(T_img, z_t, t, Σw_k·C^k(I^k_β))
           - **Diffusion Steps T=30**: Balances generation quality and speed
           - **Output I_syn**: Photorealistic image maintaining precise camera-object relation β
           - **Quality Assurance**:
             - Through strong constraints from 3D priors, ensures generated images' camera-object relation matches β
             - Generated images have realistic lighting, textures, and backgrounds
        4. **3D-Aware Text Instruction Generation (Stage 4)**:
           - **LLM**: GPT-4o
           - **Input**: Ground truth camera-object relation β (azimuth φ, elevation θ, distance)
           - **Three Types of Question Generation**:
             a) **Object Orientation Questions**:
                - Examples: "Which direction is the object facing?", "Is the object facing toward or away from the camera?"
                - Answers: Generate classification answers based on φ (8 direction categories)
             b) **Camera Viewpoint Questions**:
                - Examples: "Was the photo taken from above the object or from the side?", "What is the camera viewpoint?"
                - Answers: Generate classification answers based on θ (top/horizontal/bottom)
             c) **Shot Distance Questions**:
                - Examples: "Was the photo taken close or far away?", "Is this a close-up or long shot?"
                - Answers: Generate classification answers based on distance (close-up/medium/long shot)
           - **Prompt Engineering Techniques**:
             - Use system prompts and few-shot examples to ensure question naturalness and diversity
             - Generate up to 3 VQA pairs for each camera-object relation (1 per question type)
           - **Output T_qa**: High-quality question-answer pairs with answers precisely matching ground truth
      - **Key Technical Advantages**:
        - **Precise Annotation**: 3D rendering ensures ground truth accuracy of camera-object relations, avoiding human annotation errors
        - **Photorealism**: Multi-ControlNet+SDXL generates image quality close to real photographs
        - **Fully Automated**: Fully automated pipeline from 3D assets to VQA data without human intervention
        - **Scalability**: Applicable to any 3D asset library (Objaverse, ShapeNet, etc.), theoretically infinitely scalable
        - **Diversity**: Each 3D asset generates 72 camera-object relation combinations (8 directions × 3 viewpoints × 3 distances), covering wide spatial configurations
  - **Ultimate3D Dataset**:
      - **Total Scale**: 240K VQA pairs
      - **Composition**:
        - **Synthetic Data**: 85K images (from 1180 3D assets)
        - **Real Data**: 18K images (cropped single-person photos from MEBOW dataset + human orientation labels)
      - **3D Asset Library**: 1180 3D models covering 100 object categories
      - **Camera-Object Relation Coverage**:
        - Each 3D asset: 72 configurations (8 directions × 3 viewpoints × 3 distances)
        - Each configuration: Up to 3 VQA pairs (corresponding to 3 question types)
      - **Benchmark Test Set**: 8K high-quality samples for evaluation
      - **Data Format**: (Image I_syn, Question T_qa, Answer, Category Label, Ground Truth β)
  - **Experimental Results** - **Open-Source Models After Fine-tuning Surpass All Commercial SOTA**:
      - **Baseline Model Performance (Unfinetuned)**:
        - LLaVA-1.5-7B: Orientation 18.3%, Viewpoint 25.0%, Shot Distance 29.2%
        - LLaVA-1.6-13B: Orientation 16.1%, Viewpoint 15.9%, Shot Distance 33.3%
        - Llama-3.2-Vision-11B: Orientation 5.6%, Viewpoint 6.8%, Shot Distance 38.1%
        - **Conclusion**: All baseline models approach random guess level (<40%) on camera-object relation understanding
      - **Fine-tuned Performance (Trained on Ultimate3D)**:
        - **Object Orientation Task**:
          - Finetuned LLaVA-1.6-13B: **72.4%** (synthetic) / 63.1% (real) vs GPT-4o 43.1% (+29.3%)
          - Finetuned Llama-3.2-V-11B: **74.2%** (synthetic) / 66.4% (real)
        - **Camera Viewpoint Task**:
          - Finetuned LLaVA-1.6-13B: **72.3%** (synthetic) / 61.8% (real) vs GPT-4o 54.1% (+18.2%)
          - Finetuned Llama-3.2-V-11B: **69.1%** (synthetic) / 58.7% (real)
        - **Shot Distance Task**:
          - Finetuned LLaVA-1.6-13B: **94.8%** (synthetic) / 71.4% (real) vs GPT-4o 41.7% (+53.1%)
          - Finetuned LLaVA-1.5-7B: **94.0%** (synthetic) / 66.7% (real)
      - **Commercial Model Performance Comparison**:
        - GPT-4o: Orientation 43.1%, Viewpoint 54.1%, Shot Distance 41.7%
        - Claude-3-Sonnet: Orientation 43.1%, Viewpoint 54.3%, Shot Distance 41.7%
        - Claude-3.5-Sonnet: Orientation 40.3%, Viewpoint 55.6%, Shot Distance 41.8%
        - **Conclusion**: All commercial models perform poorly on Ultimate3D benchmark, revealing camera-object relation understanding as a common weakness of current MLLMs
      - **Cross-Dataset Generalization (MMVP Benchmark)**:
        - Fine-tuned models also show significant improvements on MMVP, proving learned spatial understanding capabilities are transferable
      - **User Study**:
        - 93.07% of generated images evaluated as successfully maintaining 3D geometric structure and camera-object relations
        - Far higher than baseline method (only 55.11% success rate)
  - **Ablation Study Key Findings**:
      - **Multi-ControlNet Necessity**: Using both depth + Canny edges achieves best results (using either prior alone decreases performance)
      - **Importance of 3D Priors**: Removing 3D visual priors significantly reduces camera-object relation preservation rate
      - **Synthetic Data vs Real Data**:
        - Models trained only on synthetic data perform best on synthetic test sets
        - On real test sets, synthetic data-trained models still significantly outperform unfinetuned baselines
      - **Data Scale Impact**: Performance continues to improve from 100K to 240K with no saturation signs
  - **Qualitative Analysis**:
      - **Bias Identification**:
        - GPT-4o and Claude tend to underestimate viewpoint angles (misjudge top view as horizontal)
        - Tend to overestimate shot distance (misjudge medium shot as long shot)
        - Near random on object orientation judgment
      - **LLaVA Baseline Bias**: Original LLaVA models give fixed answers to all questions ("front-left", "top", "close-up"), showing severe dataset bias
      - **Post-Finetuning Improvement**: Fine-tuned LLaVA models can accurately recognize various camera-object relations with no obvious bias
  - **Institution**: Purdue University, Amazon
  - **Authors**: Shengyuan Ding, Xiaoyi Dong, Yuhang Zang, Haodong Duan, Min Sun, Cheng-Hao Kuo, Daniel Aliaga et al.
  - **Publication**: arXiv July 2025 (v2)
  - **Open Source**: ✅ [Code, Data, and Models](https://github.com/opendatalab/Ultimate3D)
  - **Significance**:
      - **Problem Identification**: First systematic revelation of severe deficiencies in MLLMs (including GPT-4o, Claude) on camera-object relation understanding
      - **Dataset Contribution**: Provides first large-scale, precisely annotated 3D camera-object relation VQA dataset and evaluation benchmark
      - **Method Innovation**: Proposes complete 3D asset-driven visual instruction data generation framework, extensible to other 3D understanding tasks
      - **Performance Breakthrough**: Proves only 240K high-quality synthetic data needed to make open-source 7B models surpass all commercial SOTA (average +33.4%)
      - **Bias Correction**: Provides solution for correcting spatial relation bias in existing MLLMs' training data
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2303.17590">📄 SyViC</a></b><br>
<code>arXiv 2303.17590</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-March_2023-red?style=flat-square"/>
</summary>

  - **Focus**: **Going Beyond Nouns With Vision & Language Models Using Synthetic Data** - Using physics simulation and human action synthesis to enhance VLM understanding of attributes, actions, relations, and states
  - **Data Synthesis Method** - **3D Physics Simulation + Human Motion Synthesis + Spatial Relationship Modeling**:
      - **Core Innovation**: Constructs million-scale synthetic dataset focusing on "beyond nouns" Visual Language Concepts (VLC), addressing VLM weaknesses in compositional reasoning and non-object word understanding
      - **Base Platform**: **ThreeDWorld (TDW)** - Multimodal physics simulation platform
        - **3D Resources**: 2,304 object models, 585 unique materials, 30+ indoor and 9 outdoor scenes
        - **Material Types**: Metal, cardboard, wood, ceramic, glass with diverse textures
        - **Physics Engine**: Supports realistic physical interactions and collision detection
      - **Three Synthesis Components**:
        1. **Multi-Object Scene Synthesis**:
           - **Object Placement**: Randomly place 1-8 3D object models per scene, using colliders for reasonable layouts
           - **Multi-Viewpoint Rendering**: Deploy 4-12 camera positions simultaneously for different perspectives of same scene
           - **Attribute Randomization**: Programmatic randomization of object colors, sizes, materials
           - **Spatial Relations**: Auto-generate positional relationship descriptions (left/right, front/back, above/below) based on 3D world coordinates
        2. **Human Motion & Interaction Synthesis**:
           - **Body Model**: Use **SMPL-X** parametric human model for precise pose control
           - **Motion Data Sources**: Integrate **AMASS**, **BABEL**, **TEACH** large-scale motion capture databases
           - **Diversity Design**:
             - **Gender Diversity**: Male and female prefabs (Unity Prefabs)
             - **Clothing Diversity**: SURREAL + Multi-Garment system supporting multi-layer clothing combinations
             - **Motion Diversity**: Cover daily activities (walking, running, jumping, dancing) and complex interactions
           - **Human-Object Interactions**: Physical interactions between humans and scene objects (grasping, moving, avoiding)
        3. **Dense Caption Generation**:
           - **Rule-Based Grammar**: Develop metadata-driven grammar system automatically generating detailed captions from scene metadata
           - **Multi-Level Descriptions**:
             - **Object Descriptions**: Shape, color, material, position
             - **Human Descriptions**: Gender, clothing, hairstyle, action states
             - **Relationship Descriptions**: Spatial relations between objects, human-object relations
             - **Scene Descriptions**: Environmental background, overall layout
           - **Long Caption Handling**: Develop caption splitting module to handle captions exceeding CLIP text encoder context length
      - **Data Augmentation Strategies**:
        - **Domain Adaptive Stylization**: Use style transfer to reduce synthetic-real data domain gap
        - **Parameter Efficient Fine-tuning**: LoRA adapters for low-parameter updates, avoiding catastrophic forgetting
        - **Model Averaging**: Combine multiple checkpoint weights to balance VLC understanding gains and zero-shot capability retention
  - **Data Scale**:
      - **SyViC Dataset**: 767,000 image-text pairs
      - **Caption Quality**: Average multi-sentence descriptions covering objects, attributes, actions, relations, states
      - **Diversity**: Covers thousands of object-attribute-action combinations ensuring compositional reasoning training coverage
  - **Training Strategy**:
      - **LoRA Fine-tuning**: Freeze base model parameters, train only low-rank adaptation layers
      - **Caption Splitting**: Split long captions into sub-captions, encode separately then average features
      - **Contrastive Learning**: Maintain original model (CLIP/CyCLIP) contrastive loss functions
      - **Domain Adaptation**: Combine stylization and parameter-efficient methods to reduce forgetting
  - **Experimental Results**:
      - **Compositional Understanding Benchmarks**:
        - **VL-Checklist**: syn-CLIP vs CLIP shows +5.82% relation understanding, +2.86% attribute understanding
        - **ARO Benchmark**: VG-Relation +12.56%, VG-Attribution +3.75%
        - **Winoground**: +1.75% compositional reasoning accuracy improvement
      - **Ablation Study Findings**:
        - **Human Characters Crucial**: Including human interactions significantly outperforms object-only scenes
        - **Object Attribute Randomization**: Color, size, material variations contribute greatly to compositional understanding
        - **Clothing Diversity**: Multi-Garment vs SURREAL vs simple textures, Multi-Garment performs best
      - **Zero-Shot Capability Retention**: Comparable performance to baseline CLIP on 21 zero-shot tasks (only -0.8%)
  - **Key Findings**:
      - **Synthetic Data Effectiveness**: Pure synthetic data can significantly improve VLM understanding of beyond-noun concepts
      - **Human-Centric Importance**: Including human actions and interactions crucial for compositional reasoning improvement
      - **Balanced Training Strategy**: LoRA+domain adaptation+model averaging effectively balances new capability acquisition and original capability retention
      - **Dense Caption Value**: Detailed multi-level captions more conducive to VLC learning than simple object labels
  - **Publication**: arXiv March 2023 | MIT-IBM Watson AI Lab & Rice University et al.
  - **Open Source**: ✅ SyViC Dataset + Data Generation Codebase + Training Strategy Code
  - **Significance**:
      - **VLM Capability Boundary Extension**: First systematic solution to VLM "beyond nouns" understanding fundamental problem
      - **Synthetic Data Methodology**: Establishes complete framework for physics simulation-based VL data synthesis
      - **Compositional Reasoning Breakthrough**: Proves synthetic data can effectively improve model compositional reasoning and VLC understanding
      - **Scalability**: Open-source data generation codebase provides good scalability and adaptability
  

</details>
---

#### 📐 Geometric & Mathematical Reasoning

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2410.17885">📄 R-CoT</a></b><br>
<code>ICLR 2025</code>
</summary>

  - **Data Synthesis Method** - **Reverse Chain-of-Thought for Geometric Reasoning**:
      - **Core Innovation**: Two-stage pipeline combining **engine accuracy** with **LLM diversity** for geometric problem generation
      - **Stage 1 - GeoChain**: **Generates high-fidelity geometric images** with corresponding descriptions
        - Produces accurate geometric images step-by-step using **code-based engine**
        - Generates detailed descriptions highlighting **relations among geometric elements**
        - Images have higher fidelity than existing synthetic geometric data
      - **Stage 2 - Reverse A&Q**: Generates Q&A pairs in reverse from reasoning results
        - **Step 1**: Description Patch Reasoning - single-step reasoning from descriptions
        - **Step 2**: Chain-of-Thought Fusion - progressively fuse single-step reasoning into multi-step reasoning
        - **Step 3**: Question Generation - generate questions **in reverse** from reasoning results
        - Avoids accuracy issues of directly generating Q&A from images using LMMs
      - **Key Advantage**: Reduces incorrect answers by generating answer **before** question
  - **Data Scale**: Creates GeoMM dataset with high-fidelity geometric images and diverse Q&A pairs
  - **Experimental Results**:
      - R-CoT-8B outperforms previous SOTA open-source models by **16.6%** on MathVista and **9.2%** on GeoQA
      - Surpasses GPT-4o by average **13%** across both datasets
      - Achieves new SOTA in 2B, 7B, and 8B settings for geometric reasoning
  - **Publication**: arXiv preprint arXiv:2410.17885, October 2024
  - **Institution**: Baidu Inc., Huazhong University of Science and Technology
  - **Open Source**: ✅ [Code & Models](https://github.com/dle666/r-cot)
  

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
  
  #### 📄 Document / Text-Dense Scenes
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2505.17778">📄 TextFlux</a></b><br>
<code>arXiv 2505.17778</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
</summary>

  - **Focus**: **OCR-Free High-Fidelity Multilingual Scene Text Synthesis** - A DiT-based OCR-free framework that achieves multilingual scene text generation through spatial concatenation of glyph-rendered images
  - **Data Synthesis Method** - **Glyph-Guided Spatial Concatenation Strategy**:
      - **Core Innovation**: Eliminates the dependency on OCR encoders, leveraging DiT model's contextual reasoning capabilities for text synthesis
      - **Method Pipeline**:
        1. **Glyph Rendering**:
           - Renders target text as white foreground on black background to create binary glyph mask `I_glyph`
           - Ensures resolution matches scene image `I_scene`
        2. **Spatial Concatenation**:
           - Horizontally or vertically concatenates glyph and scene images: `I_concat = Concat([I_glyph, I_scene], axis)`
           - Forms unified input image without additional visual conditioning modules
        3. **Prompt Design** (In-Context Learning Paradigm):
           - Template: "The pair of images highlights some white words on a black background, as well as their style on a real-world scene image. [IMAGE1] is a template image rendering the text, with the words {words}; [IMAGE2] shows the text content {words} naturally and correspondingly integrated into the image."
           - Guides model to understand semantic relationship between glyph template and scene image
        4. **Model Architecture**:
           - Built on pre-trained FLUX.1-Fill-dev (DiT architecture, latent rectified flow transformer)
           - Directly leverages DiT's context-aware capabilities without specialized OCR encoders or additional loss functions
      - **Key Technical Advantages**:
        - **OCR-free**: Completely eliminates need for OCR encoders, simplifying model architecture
        - **Multilingual Scalability**: Achieves strong performance on low-resource languages (<1000 samples)
        - **Data Efficiency**: Requires only 1% of training data compared to competing methods (30,405 vs 3M-10M images)
        - **Controllable Multi-line Generation**: Supports flexible multi-line text synthesis with precise line-level control over position and content
        - **Zero-shot Capability**: Can render languages unseen during training (e.g., minority languages)
  - **Training Data Scale**:
      - **Total 30,405 images** (vs AnyWord-3M's 3M, MARIO-10M's 10M)
        - English: ~10,000 images (MLT2017, TotalText, CTW1500)
        - Chinese: ~15,000 images (ReCTS, RCTW)
        - Other languages: 1,000 each (Japanese, Korean, French, German, Italian from MLT2019)
      - **Training Configuration**:
        - Batch size 1, gradient accumulation 8
        - AdamW optimizer, learning rate 2e-5
        - Total 30,000 iterations
        - Multi-resolution augmentation (512-1024)
        - Two versions: Full-parameter (2×A100 80GB) + LoRA (1×A100 80GB, rank=128)
  - **Experimental Results** - **Comprehensively Outperforms Existing Methods on 4 Benchmarks**:
      - **Multi-line Text Generation (Core Task)**:
        - AnyWord(EN): TextFlux **80.3%** vs AnyText2 45.1% (+35.2%)
        - AnyWord(CH): TextFlux **62.3%** vs AnyText2 35.9% (+26.4%)
        - TotalText: TextFlux **65.3%** vs AnyText2 20.5% (+44.8%)
        - ReCTS: TextFlux **68.5%** vs AnyText2 41.5% (+27.0%)
      - **Single-line Text Generation**:
        - Lightweight LoRA version comprehensively surpasses all baselines
        - Flux base model has 0% Chinese accuracy; applying TextFlux achieves 62.3%
      - **Qualitative Results**:
        - Significantly outperforms existing methods under challenging conditions (complex backgrounds, curved text, handwriting styles)
        - Generated results nearly indistinguishable from real images
  - **Key Findings from Ablation Studies**:
      - **Necessity of Glyph Concatenation Strategy**: Without concatenation, Chinese accuracy only 5.2%
      - **Importance of Training**: Concatenation without training completely fails on complex backgrounds
      - **Text Encoder Impact**: Removing CLIP or T5 encoder has minimal impact on non-Latin scripts, indicating visual context guidance is sufficiently effective
  - **Institution**: bilibili Inc., Soochow University, Wangxuan Institute of Computer Technology at Peking University
  - **Authors**: Yu Xie, Jielei Zhang, Pengyu Chen, Ziyue Wang, Weihang Wang, Longwen Gao, Peiyi Li, Huyang Sun, Qiang Zhang, Qian Qiao, Jiaqing Fan, Zhouhui Lian
  - **Publication**: arXiv May 2025 (v1)
  - **Project Page**: [https://yyyyyxie.github.io/textflux-site/](https://yyyyyxie.github.io/textflux-site/)
  - **Significance**:
      - **Architectural Simplification**: Proves that complex OCR encoders are unnecessary; DiT's contextual reasoning capability is sufficient for high-quality scene text synthesis
      - **Data Efficiency**: Achieves SOTA with 1% of data, providing viable solution for low-resource scenarios
      - **Multilingual Breakthrough**: First to demonstrate high-quality text rendering in low-resource languages with minimal data (<1000 samples)
      - **Enhanced Controllability**: Supports flexible multi-line text control, breaking through single-line or fixed layout limitations of existing methods
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2410.12628">📄 DocLayout-YOLO</a></b><br>
<code>arXiv 2410.12628</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Enhancing Document Layout Analysis Through Diverse Synthetic Data and Global-to-Local Adaptive Perception** - Generates DocSynth-300K large-scale diverse document synthetic dataset and designs GL-CRM module to handle multi-scale variations of document elements
  - **Data Synthesis Method** - **Mesh-candidate BestFit Algorithm + Element Augmentation**:
      - **Core Innovation**: First method framing document synthesis as 2D bin packing problem, generating aesthetically pleasing and diverse layouts through iterative best matching
      - **Problem Identification**:
        - Existing unimodal DLA methods (e.g., YOLO, DINO) are fast but have lower accuracy
        - Multimodal methods (e.g., LayoutLMv3, DiT) achieve higher accuracy but suffer significant latency
        - Existing document pre-training datasets (e.g., PubLayNet, DocBank) are limited to single document types (academic papers only) with insufficient element diversity (<10 categories)
        - Diffusion-based generation methods produce homogeneous layouts, unable to cover diverse real-world document types
      - **Three-Stage Generation Pipeline**:
        1. **Preprocessing: Ensuring Element Diversity**:
           - **Data Source**: M6Doc test set (2,800 diverse document pages with 74 fine-grained element categories)
           - **Element Pool Construction**:
             - Fragment pages by fine-grained category to extract elements from each category
             - Augment rare categories with quantity <100
           - **5 Augmentation Techniques**:
             a) **Style Transfer**: Apply different fonts, colors, styles to text elements
             b) **LLM Rewriting**: GPT-4 rewrites text element content (maintaining semantic similarity)
             c) **Background Replacement**: Replace element backgrounds
             d) **Elastic Transformation**: Slight distortion simulating jitter or low resolution
             e) **Gaussian Noise**: Add noise simulating real-world distortion
           - **Result**: Ensure ≥100 diverse elements per category
        2. **Layout Generation: Ensuring Layout Diversity**:
           - **Algorithm**: **Mesh-candidate BestFit** - Inspired by 2D bin packing problem
           - **Key Insight**: Random arrangement produces chaotic layouts; Diffusion models produce homogeneous layouts (academic paper style only)
           - **Core Concept**: Treat available grids in current layout as "bins" of different sizes, iteratively perform best matching
           - **Detailed Steps**:
             a) **Candidate Sampling**: Stratified sampling from element pool based on element size → candidate set C_set
             b) **Mesh Engine**: Analyze current layout L → generate available grid position set M
             c) **Iterative Best Matching**:
                - For each candidate element e_i and each grid g_j, compute fill rate fr = match(e_i, g_j)
                - Select (e_i, g_j) pair with highest fill rate fr > threshold fr_thr
                - Place e_i at position g_j, update layout L
                - Remove e_i from candidate set
                - Repeat until no satisfying match found
             d) **Constraint**: Small element count ≤ Mini_num=5 (avoid excessive small elements reducing aesthetics)
           - **Advantage**: Balances layout diversity (randomness) and aesthetics (fill rate and alignment)
        3. **Image Rendering and Post-processing**:
           - **Rendering**: Render layout L and elements into complete document image
           - **Post-processing**:
             - Apply augmentation techniques: style transfer, LLM rewriting, background replacement
             - Add elastic transformation and Gaussian noise to simulate real scenarios
           - **Output**: Final document image with corresponding layout annotations
      - **Key Technical Advantages**:
        - **Aesthetic Guarantee**: Generated layouts conform to human design principles through fill rate and alignment optimization
          - **Alignment Score**: Δx* = min|x*_i - x*_j| (lower=better aligned), experiments show Mesh-BF 0.0009 vs Random 0.0171 vs Diffusion 0.0032
          - **Density Score**: L_dst = Σ|e_i| / |L| (higher=more compact), experiments show Mesh-BF 0.645 vs Random 0.259 vs Diffusion 0.476
        - **Layout Diversity**: Generates various layouts from dense (many small elements) to sparse (few large elements)
        - **Element Diversity**: 74 fine-grained categories, far exceeding PubLayNet (6 categories), DocBank (13 categories)
        - **Scalability**: Can generate arbitrary scale datasets based on any document element pool
  - **DocSynth-300K Dataset**:
      - **Original Generation**: 594K document images
      - **Filtered Scale**: 300K high-quality documents (discarded bottom filtered samples)
      - **Element Coverage**: 74 fine-grained element categories
      - **Layout Diversity**: Covers academic papers, textbooks, market analysis reports, financial documents, etc.
      - **Annotations**: Category and position (bounding box) for each element
      - **Characteristics**:
        - Far exceeds existing dataset diversity (PubLayNet 360K academic-only, DocBank 500K weak supervision with lower quality)
        - Aesthetic scores significantly better than Random and Diffusion methods
  - **DocStructBench Evaluation Benchmark**:
      - **Objective**: Quantitatively evaluate model performance on different document types
      - **Scale**: 9,955 images (7,310 train + 2,645 test)
      - **Four Subsets**:
        - **Academic**: Academic papers (1,605 train + 402 test)
        - **Textbook**: Textbooks and test papers (2,345 train + 587 test)
        - **Market Analysis**: Industry and market analysis reports (2,660 train + 651 test)
        - **Financial**: Financial business documents (2,472 train + 592 test)
      - **10 Element Categories**: Title, Plain Text, Abandoned Text, Figure, Figure Caption, Table, Table Caption, Table Footnote, Isolated Formula, Formula Caption
      - **Source Diversity**: Documents from diverse institutions, publishers, websites across broad domains
      - **Manual Annotation**: Each image precisely annotated by human annotators
  - **Global-to-Local Controllable Receptive Module (GL-CRM)**:
      - **Problem**: Document elements have large scale variations (one-line title vs full-page table)
      - **Solution**: Hierarchical architecture for global-to-local perception
      - **Controllable Receptive Module (CRM)**:
        - **Input**: Feature map X
        - **Multi-granularity Feature Extraction**: Use weight-shared convolution w (kernel size k) with different dilation rates d=[d_1, d_2, ..., d_n]
        - **Formula**: F_i = GELU(BN(Conv(X, w, d_i)))
        - **Feature Fusion**: Fˆ = Concat(F_1, ..., F_n) → Conv → Sigmoid weighting
        - **Adaptive Fusion**: Network learns to automatically fuse features of different granularities
      - **Global-to-Local Design (Three Levels)**:
        a) **Global-level (Shallow Layer)**: CRM with k=7, d=[1,3,5,7] - Perceive whole-page scale elements
        b) **Block-level (Middle Layer)**: CRM with k=3, d=[1,2,3] - Perceive document sub-blocks (medium scale)
        c) **Local-level (Deep Layer)**: Basic bottleneck - Focus on local semantic information (small scale)
      - **Advantage**: Adapts to multi-scale characteristics of document elements, significantly improving detection accuracy
  - **Experimental Results - Speed and Accuracy Breakthrough**:
      - **D4LA Dataset** (11,092 complex documents, 27 categories, 12 document types):
        - DocLayout-YOLO: mAP **70.3%**, AP50 82.4%, FPS **144.9**
        - YOLO-v10 (Baseline): mAP 68.6%, AP50 80.7%, FPS 144.9%
        - DINO-4scale: mAP 64.7%, AP50 76.9%, FPS 26.7
        - DiT-Cascade-L: mAP 68.2%, AP50 80.1%, FPS 6.0
        - LayoutLMv3-B: mAP 60.0%, AP50 72.6%, FPS 9.0
        - **Conclusion**: Surpasses all unimodal and multimodal methods while maintaining fastest speed
      - **DocLayNet Dataset** (80,863 pages, 11 categories, 7 document types):
        - DocLayout-YOLO: mAP **79.7%**, AP50 93.4%
        - YOLO-v10 (Baseline): mAP 76.2%, AP50 93.0%
        - DINO-4scale: mAP 77.7%, AP50 93.5%
        - DiT-Cascade-B/L: mAP 73.2%/72.6%
        - LayoutLMv3-B: mAP 75.4%, AP50 92.1%
        - **Conclusion**: Significantly surpasses all methods (+2.0% vs DINO, +7.1% vs DiT-L)
      - **DocStructBench Four Subset Performance**:
        - **Academic**: 81.8% (vs YOLO-v10 80.5%, DiT-L 81.0%)
        - **Textbook**: 73.7% (vs YOLO-v10 70.2%, DiT-L 70.8%)
        - **Market Analysis**: 69.4% (vs YOLO-v10 68.9%, DiT-L 70.8%)
        - **Financial**: 90.1% (vs YOLO-v10 89.9%, DiT-L 89.3%)
        - **Conclusion**: Achieves best or near-best performance on all document types
      - **Speed Comparison** (Single A100 GPU):
        - DocLayout-YOLO: **85.5 FPS**
        - YOLO-v10: 144.9 FPS (slightly faster but lower accuracy)
        - DINO-4scale: 26.7 FPS
        - DiT-Cascade-L: 6.0 FPS
        - LayoutLMv3: 9.0 FPS
        - **Conclusion**: Maintains high accuracy while being significantly faster than multimodal methods (9-14×)
  - **Pre-training Dataset Comparison** (100K samples finetuned on DocStructBench):
      - **DocSynth-300K**: Academic 82.1%, Textbook 71.5%, Market 69.3%, Financial 90.3%
      - **PubLayNet (300K)**: Academic 81.0%, Textbook 71.5%, Market 69.1%, Financial 89.7%
      - **DocBank (400K)**: Academic 81.6%, Textbook 70.9%, Market 69.1%, Financial 90.1%
      - **Diffusion (300K)**: Academic 80.7%, Textbook 71.9%, Market 68.9%, Financial 89.3%
      - **Random (300K)**: Academic 80.5%, Textbook 71.2%, Market 68.1%, Financial 89.6%
      - **M6Doc (2K)**: Academic 80.4%, Textbook 70.0%, Market 68.9%, Financial 89.7%
      - **Conclusion**: DocSynth-300K achieves best or near-best performance on all document types, demonstrating superior generalization capability
  - **Ablation Study Key Findings**:
      - **GL-CRM Component Effects**:
        - **Global-level CRM**: +0.5% mAP when used alone
        - **Block-level CRM**: +0.7% mAP when used alone
        - **Combined**: +1.2% mAP (D4LA: 68.6%→69.8%)
        - **Conclusion**: Hierarchical design effectively adapts to multi-scale characteristics of document elements
      - **DocSynth-300K Pre-training Effects**:
        - **No Pre-training**: D4LA 68.6%, DocLayNet 76.2%
        - **+DocSynth-300K Pre-training**: D4LA 69.8% (+1.2%), DocLayNet 79.3% (+3.1%)
        - **Conclusion**: Pre-training significantly improves downstream task performance, especially on complex datasets
      - **Data Filtering Necessity**: Performance further improves after filtering low-quality samples
      - **Pre-training Data Scale**: Performance continuously improves with data increase (0→30K→50K→100K→200K→300K)
  - **Generated Data Visualization Analysis**:
      - DocSynth-300K generated documents exhibit high diversity:
        - Dense layouts (many small elements) vs sparse layouts (few large elements)
        - Different element combinations (S/M/L = Small/Medium/Large dominated)
        - High aesthetic quality (alignment and density both superior to Random and Diffusion)
      - Compared with Diffusion and Random methods, DocSynth layouts are more reasonable and aesthetically pleasing
  - **Institution**: Shanghai AI Laboratory
  - **Authors**: Zhiyuan Zhao, Hengrui Kang, Bin Wang, Conghui He
  - **Publication**: arXiv October 2024 (v1)
  - **Open Source**: ✅ [Code, Data & Models](https://github.com/opendatalab/DocLayout-YOLO)
  - **Significance**:
      - **Speed-Accuracy Trade-off Breakthrough**: First unimodal method achieving accuracy surpassing multimodal methods while maintaining speed advantage (9-14× faster)
      - **Dataset Contribution**:
        - DocSynth-300K provides first large-scale, diverse, high-aesthetic-quality document synthesis dataset
        - DocStructBench offers comprehensive multi-document-type evaluation benchmark
      - **Method Innovation**:
        - Mesh-candidate BestFit algorithm frames document synthesis as bin packing problem for first time, generating aesthetically pleasing and diverse layouts
        - GL-CRM module effectively handles extreme scale variations of document elements
      - **Generalization Capability**: Proves pre-training on diverse synthetic data significantly improves model generalization on various real documents
      - **Practical Value**: Provides fast and accurate layout analysis solution for document parsing systems, directly applicable to RAG systems, document OCR, and real-world scenarios
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2407.07053">📄 Multimodal Self-Instruct</a></b><br>
<code>arXiv 2407.07053</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Synthetic Abstract Image and Visual Reasoning Instruction Using Language Model** - Leveraging LLMs and their code capabilities to synthesize massive abstract images (charts, maps, dashboards, etc.) and visual reasoning instructions without relying on GPT-4V
  - **Data Synthesis Method** - **Code-Driven Multimodal Self-Instruct Pipeline**:
      - **Core Innovation**: First systematic exploration of using LLMs and code to synthesize abstract images (non-natural images), demonstrating that code generation can precisely control abstract image details
      - **Multimodal Self-Instruct Strategy (Three Key Steps)**:
        1. **Visual Idea Proposal Stage**:
           - **Task**: LLM autonomously proposes creative visual ideas describing daily scenarios (e.g., city maps, flowcharts, statistical charts)
           - **Eight Abstract Image Types**: Chart, Table, Simulated Road Map, Dashboard, Flowchart, Relation Graph, 2D Planar Layout, Visual Puzzle
           - **Detailed Parameter Control**: Control specific details of image synthesis (colors, fonts, layouts) through natural language descriptions
        2. **Image Synthesis Stage**:
           - **Simulated Data Generation**: LLM generates simulated data for proposed visual ideas (e.g., pie chart percentages, map path points)
           - **Code Generation**: LLM generates Python code using visualization libraries like Matplotlib or ECharts
           - **Explicit Parameter Definition**: All parameters explicitly defined in code (image style, colors, font size, legend position, etc.)
           - **Image Rendering**: Execute code to generate desired abstract images
        3. **Visual Instruction Construction Stage**:
           - **Question-Answer Pair Generation**: LLM designs multiple Q&A pairs based on visual ideas, simulated data, and generated code
           - **Question Type Diversity**:
             - **Chart Tasks**: OCR, Caption, Detailed Perception (position/quantity/layout), Data Extraction, Mathematical Reasoning
             - **Map Tasks**: Path Planning, Spatial Relation Reasoning
             - **Flowchart Tasks**: Structural Questions (number of steps, symbol types), Reasoning Questions (next operation)
             - **Relation Graph Tasks**: Tree Structure Questions, Mathematical Reasoning Questions
           - **Answer Annotation with Rationale**: Provide detailed rationale for each question (similar to chain-of-thought), enhancing training effectiveness
      - **Key Technical Advantages**:
        - **Code Precision Control**: Precisely control geometric features and text content of abstract images through code, avoiding detail control failures of text-to-image models
        - **Hallucination-Free Guarantee**: Based on code and simulated data generation, ensuring answer accuracy (as long as scene graphs are accurate)
        - **Interpretability**: Code as intermediate representation makes data generation process fully interpretable and controllable
        - **Cost Efficiency**: Uses GPT-4-turbo instead of GPT-4V, significantly reducing costs
        - **Scalability**: Easily extend instruction data types by adding new templates or customizing existing ones
      - **Dataset Statistics**:
        - **Benchmark Dataset**: 3,658 images, 11,193 instructions (8 scenarios)
          - Dashboard: 73 images, 1,013 instructions
          - RelationGraph: 66 images, 822 instructions
          - Flowchart: 98 images, 1,451 instructions
          - VisualPuzzle: 189 images, 529 instructions
          - 2DPlanarLayout: 25 images, 252 instructions
        - **Training Dataset**: 19,338 images, 62,476 instructions (3 scenarios)
          - Chart: 1,768 images, 34,590 instructions
          - Table: 570 images, 10,886 instructions
          - Roadmap: 17,000 images, 17,000 instructions
        - **Data Quality Assurance**:
          - **Code Feasibility Filtering**: If generated code fails to run, prompt LLM to self-reflect based on compiler error feedback, up to 3 retries
          - **Image Aesthetics Check**: Use LLaVA-1.5 to check image aesthetics (visual element interference, layout reasonableness, text legibility)
          - **Answer Accuracy Verification**: Use self-consistency method, let LLM generate multiple responses based on ideas, code, and questions, select final answer through voting
          - **Human Evaluation**: Randomly sample 10% of <question, answer> pairs, 4 CS graduate students evaluate from four dimensions (image aesthetics, question rationality, answer accuracy, image-instruction relevance)
      - **Experimental Results**:
        - **Benchmark Evaluation** (8 abstract image tasks):
          - **Human Level**: Average accuracy 82.1%
          - **Best LMM Performance**: Claude-3.5-Sonnet 64.74%, GPT-4o 59.99%
          - **Significant Gap**: Even most advanced LMMs (GPT-4o) only achieve 54.79% on Dashboard task, far below human level (85.3%)
          - **Open-source vs Closed-source Gap**: Open-source models (e.g., Vanilla Llava-1.5-7B) average accuracy only 15.4%, huge gap with closed-source models
        - **Fine-tuning Effects** (Llava-our-62k):
          - **Chart Understanding**: 10.5% → 30.3% (+19.8%)
          - **Table Understanding**: 15.8% → 51.8% (+36.0%)
          - **Map Navigation**: 0.3% → 67.7% (+67.4%), surpassing GPT-4o (23.3%) and Claude-3 (38.3%)
          - **Using only 68K synthetic data and 4 hours of LoRA fine-tuning**, elevates Llava-1.5-7B's chart understanding capability to Qwen-VL-Plus level
        - **Task Synergy Effects**:
          - **Chart+Table Training**: Positive impact on map navigation tasks (+5% performance improvement)
          - **Map Training**: Smaller impact on chart and table tasks
          - **Speculated Reason**: Different tasks require different capabilities
        - **Data Scale Impact**:
          - As synthetic data increases (35k → 47k → 62k), model performance continuously improves without plateauing
          - Mathematical reasoning subtask shows most improvement
        - **Generalization Ability** (weakly related tasks):
          - **ChartQA**: 19.9% → 23.9% (+4.0%)
          - **MathVista**: 25.1% → 25.9% (+0.8%)
          - **Untrained Tasks**: Dashboard +0.0%, RelationGraph +0.5%, Flowchart +2.7%, VisualPuzzle +0.2%, PlanarLayout +6.4%
          - **Conclusion**: Training only on chart, table, and map data can also improve other abstract image reasoning tasks
      - **Key Findings**:
        - **Abstract Image Understanding Challenge**: Current LMMs have significant deficiencies in understanding abstract images, often failing even on simple daily tasks (e.g., reading time from clock, planning route using map)
        - **Code Generation Advantage**: Using code to synthesize abstract images can precisely control details, avoiding detail control failures of text-to-image models
        - **Data Quality Importance**: Ensure synthetic data quality through three-layer filtering (code feasibility, image aesthetics, answer accuracy)
        - **Scalability**: Method can easily extend to more scenarios and task types
      - **Institution**: Zhejiang University, Institute of Software Chinese Academy of Sciences, University of Shanghai for Science and Technology
      - **Authors**: Wenqi Zhang, Zhenglin Cheng, Yuanyu He, Mengna Wang, Yongliang Shen, Zeqi Tan, Guiyang Hou, Mingqian He, Yanna Ma, Weiming Lu, Yueting Zhuang
      - **Publication**: arXiv July 2024 (v5)
      - **Open Source**: ✅ [Code](https://github.com/zwq2018/Multi-modal-Self-instruct) | [Project Page](https://multi-modal-self-instruct.github.io)
      - **Significance**:
        - **Problem Identification**: First systematic identification of significant deficiencies in current LMMs' abstract image understanding
        - **Method Innovation**: Proposes code-driven abstract image synthesis method, providing high-quality abstract image data for LMM training
        - **Benchmark Contribution**: Constructs abstract image understanding benchmark covering 8 scenarios, revealing huge gap between LMMs and human level
        - **Practical Value**: Provides scalable data synthesis framework supporting customized abstract image data generation
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2502.14846">📄 CoSyn</a></b><br>
<code>arXiv 2502.14846</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Code-Guided Synthetic Text-Rich Multimodal Data Generation** - Leverages text-only LLM coding capabilities to automatically create diverse text-dense image data
  - **Data Synthesis Method** - **Code-Driven Image Rendering + Text Annotation Generation**:
      - **Core Innovation**: Uses code as intermediate representation bridging images and text, fully leveraging strong programming capabilities of text-only LLMs
      - **Three-Stage Generation Process**:
        1. **Code Generation Stage** (P_LLM(C|q)):
           - Input: User query q (e.g., "generate nutrition label dataset")
           - Output: Executable code C
           - LLM: Claude-3.5-Sonnet (strong coding ability)
           - **Supports 11 Rendering Tools**: Matplotlib, Plotly, VegaLite, LaTeX, HTML, Mermaid, Graphviz, SVG, Asymptote, Lilypond, RDKit
        2. **Image Rendering Stage** (P(I|C)):
           - Executes generated code C to render image I
           - Precise control over image content (text, layout, style)
           - Guarantees reproducibility (code traceable)
        3. **Instruction Generation Stage** (P_LLM(T|C)):
           - Generates textual instruction T based on code C (without image)
           - LLM: GPT-4o-mini (cost-effective)
           - Produces Q&A pairs, explanations (supports CoT reasoning)
      - **20 Generation Pipelines** - Built on 11 rendering tools:
        - **Charts**: Matplotlib, VegaLite, Plotly, LaTeX, HTML
        - **Documents**: LaTeX, HTML
        - **Tables**: LaTeX, Matplotlib, Plotly, HTML
        - **Diagrams**: Graphviz, LaTeX, Mermaid
        - **Math Problems**: LaTeX
        - **Vector Graphics**: SVG, Asymptote
        - **Sheet Music**: LilyPond
        - **Circuits**: LaTeX
        - **Chemical Structures**: RDKit
      - **Diversity Enhancement Strategy - Persona-Driven**:
        - **Problem**: LLM sampling parameters struggle to generate diverse data
        - **Solution**: Introduce **200K personas** (personality/identity descriptions) at Topic Generation stage
        - **Effect**: Generate topics from varied perspectives, significantly improve content diversity
        - **Example**: Persona "sci-fi novelist likes alien worlds" → Topic "Illustrated Guide to Extraterrestrial Flora & Fauna"
      - **4-Stage Pipeline Example** (HTML Document):
        1. **Topic Generation**: Generate document topic based on query + persona (e.g., "January utility bill")
        2. **Data Generation**: Populate detailed content (fee breakdown, dates, user info)
        3. **Code Generation**: Convert data to executable code (HTML+CSS)
        4. **Instruction Generation**: Generate Q&A pairs based on code (question + explanation + concise answer)
      - **Key Technical Advantages**:
        - **High Fidelity**: Code rendering ensures text accuracy (no hallucination)
        - **Strong Controllability**: Precise control over image structure and content via code
        - **High Diversity**: Supports 11 tools, 9 categories, 100+ fine-grained queries
        - **Scalable**: Language-controlled queries, easy to customize for new domains
        - **Cost-Effective**: Text-only LLM cost far lower than multimodal models
  - **Data Scale**:
      - **CoSyn-400K**: 400K synthetic images, 2.7M instruction-tuning data
      - **9 Category Distribution**:
        - Charts: 118K | Documents: 73K | Math: 68K
        - Tables: 48K | Diagrams: 36K | Vector Graphics: 28K
        - Sheet Music: 12K | Circuits: 10K | Chemical Structures: 9K
      - **Query Diversity**:
        - Charts: 51 types | Documents: 107 types | Math: 110 types
        - Tables: 35 types | Diagrams: 34 types | Vector Graphics: 36 types
      - **Extended Application - Synthetic Pointing Data**: 65K images with click coordinate annotations
  - **Model**: Based on **Molmo Architecture** (CLIP-ViT-L + Mistral-7B)
      - Vision Encoder: OpenAI CLIP (ViT-L/14 336px)
      - Language Model: Mistral-7B
      - Connection: MLP projection layer
  - **Experimental Results** - **SOTA on 7 Text-Rich Benchmarks**:
      - **Best Among Open Models**: Average 80.9% (surpasses 2nd-place Llama 3.2 11B 77.0%, +3.9%)
      - **Surpasses Closed Models**: GPT-4V (72.8%), Gemini 1.5 Flash (76.2%)
      - **Individual Scores**:
        - ChartQA: **86.3%** (vs GPT-4V 78.1%, +8.2%)
        - DocVQA: **90.0%** (vs GPT-4V 87.2%, +2.8%)
        - InfoVQA: **70.5%** (vs GPT-4V 75.1%, -4.6%)
        - TableVQA: **65.8%** (vs GPT-4V 60.5%, +5.3%)
        - AI2D: **91.9%** (vs GPT-4V 89.4%, +2.5%)
        - TextVQA: **82.0%** (vs GPT-4V 78.0%, +4.0%)
        - ScreenQA: **80.1%** (vs GPT-4V 41.6%, +38.5%)
      - **Zero-Shot Performance** (only auxiliary + synthetic data, no eval set training):
        - Average **74.7%**, surpasses GPT-4V (72.8%)
        - Outperforms most open and closed models (no real training data)
  - **Novel Domain Adaptation** - **NutritionQA Benchmark**:
      - **Problem**: Open-source VLMs perform poorly on novel tasks (nutrition label Q&A)
      - **Zero-Shot Adaptation**: Only trained on CoSyn-400K → matches GPT-4V performance
      - **Target Domain Fine-Tuning**: Only **7K synthetic nutrition label data** → surpasses most open VLMs trained on millions
      - **Data Efficiency**: Demonstrates extremely high sample efficiency of targeted synthetic data
  - **Synthetic Data Advantages Analysis**:
      - **Ablation Study** (see Figure 4):
        - Auxiliary-only data (1M images): 58.7%
        - Synthetic-only data (400K images): **70.5%** (matches GPT-4V)
        - Auxiliary + Synthetic (zero-shot): **74.7%** (surpasses GPT-4V)
        - Eval + Auxiliary + Synthetic (supervised): **80.9%** (SOTA)
        - **Conclusion**: 400K synthetic data contributes more than 1M real auxiliary data
      - **CoT Reasoning Enhancement**:
        - Synthetic data includes (question, explanation, concise answer) triplets
        - ChartQA: +3.2% | TableVQA: +1.5% | NutritionQA: +14.0%
        - Significant improvements for tasks requiring multi-step reasoning
      - **Mitigating Data Bias** (ChartQA case):
        - **Problem**: ChartQA training set 73.9% T5-machine-generated, test set 50% human-annotated
        - **Overfitting**: PaliGemma 88.5% on machine questions, only 54.2% on human questions (34.3% gap)
        - **CoSyn Training**: 93.4% machine, 79.1% human (**14.2% gap**, reduced by 20.1%)
        - **Conclusion**: Synthetic data mitigates overfitting to benchmark biases
      - **Data Diversity Quantification** (vs existing chart datasets):
        - **Image Diversity**: CoSyn 0.596 vs ChartQA 0.340 (+75.3%)
        - **Text Diversity**: CoSyn 0.823 vs ChartQA 0.742 (+10.9%)
        - **Tool Diversity**: Using 5 tools vs Matplotlib-only → +1.3% ChartQA accuracy
      - **Scalability Analysis**:
        - Synthetic chart count from 5K → 116K, ChartQA zero-shot from 64.2% → 78.2%
        - Performance continuously improves, not saturated (suggest future scaling)
  - **Synthetic Pointing Data** - **SOTA Click Prediction**:
      - **Method**: LLM edits code to explicitly draw points on images → extract coordinates
      - **Data Volume**: 65K images with pointing annotations
      - **ScreenSpot Benchmark**:
        - Synthetic-only data: Average 68.0%
        - Human-only data (PixMo-point 155K): 68.5%
        - Synthetic + Human: **74.9%** (SOTA, surpasses UGround trained on 1.3M, 73.3%)
      - **Data Efficiency**: 65K synthetic data matches 155K human annotation performance
  - **Implementation Details**:
      - **Infrastructure**: DataDreamer library (supports parallel generation, response caching, full logging)
      - **LLM Selection**: Claude-3.5-Sonnet (strong code generation) vs GPT-4o (higher failure rate)
      - **Cost**: CoSyn-400K dataset costs approximately **$8,000**
      - **Training**: TPU v3-128, batch size 32, 60K steps (~30 hours)
  - **Publication**: arXiv February 2025
  - **Institution**: University of Pennsylvania, Allen Institute for AI (Ai2)
  - **Authors**: Yue Yang, Ajay Patel, Matt Deitke, Tanmay Gupta, et al.
  - **Open Source**: ✅ **Fully Open-Source** - CoSyn-400K dataset, code, models
  - **Project Page**: [yueyang1996.github.io/cosyn](https://yueyang1996.github.io/cosyn)
  - **Significance**:
      - **Text-Only LLM Drives Multimodal**: First systematic use of text-only LLM programming capabilities for large-scale multimodal data synthesis
      - **Code as Intermediate Representation**: Innovative use of code as image-text bridge ensuring accuracy and controllability
      - **Beyond Rendering Limitations**: Overcomes diversity bottleneck of traditional template-based rendering methods
      - **Broad Applicability**: 9 categories, 20 pipelines demonstrate framework versatility
      - **Practical Impact**: Demonstrates strong potential of synthetic data for text-rich understanding tasks, providing new paradigm for VLM training
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2412.01137">📄 TextSSR</a></b><br>
<code>arXiv 2412.01137</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-ICCV_2025-red?style=flat-square"/>
</summary>

  - **Focus**: **Diffusion-based data synthesis for Scene Text Recognition (STR)** - Generates training data for text-in-the-wild recognition
  - **Data Synthesis Method** - **Three-Pillar Diffusion Pipeline: Accuracy, Realism, Scalability**:
      - **Core Innovation**: End-to-end diffusion-based synthesis addressing limitations of rendering-based methods (lack of realism) and purely generative approaches (lack of control)
      - **Pillar 1: Accuracy - Region-Centric Text Generation + Position-Glyph Enhancement**:
        1. **Region-Centric Generation**:
           - Unlike image-level text generation (prone to hallucination), generates text **within specified bounding boxes**
           - Uses **region-conditioned diffusion** (inspired by layout-to-image methods)
           - Ensures precise control over text location and prevents unwanted text elsewhere
        2. **Position-Glyph Enhancement (PGE)**:
           - **Problem**: Diffusion models struggle with accurate character generation and sequence order
           - **Solution**: Dual-stream conditioning
             - **Glyph Stream**: Renders target text as clean glyph image (character shapes)
             - **Position Stream**: Encodes character positions within bounding box
           - **Fusion**: Inject both glyph + position information into diffusion UNet via cross-attention
           - **Result**: Character-level accuracy while maintaining natural appearance
      - **Pillar 2: Realism - Contextual Hints for Natural Styling**:
        - **Challenge**: Purely text-controlled generation yields generic styles; direct style transfer from real images causes overfitting
        - **Method - Contextual Hint Mechanism**:
          1. **Real Scene Sampling**: Select real scene text images from STR datasets (e.g., COCO-Text, MLT)
          2. **Text Inpainting**: Remove original text from selected images using inpainting models
          3. **Hint Extraction**: Extract **low-resolution contextual hints** from original text regions (color, texture, orientation, degradation patterns)
          4. **Conditional Generation**: Condition diffusion model on:
             - Target text content (via PGE)
             - Bounding box location
             - **Contextual hints** (low-res texture/color guidance)
          5. **Result**: Generated text inherits realistic styles (distortion, blur, lighting, perspective) without memorizing specific instances
      - **Pillar 3: Scalability - Combinatorial Text Permutation**:
        - **Strategy**: Systematically sample from vocabulary to create diverse text combinations
        - **Corpus Sources**:
          - **Words**: Common English/Chinese words from frequency lists
          - **Named Entities**: Person names, brands, locations
          - **Digit Sequences**: Phone numbers, dates, prices
        - **Permutation**: Generate all feasible n-grams and phrases up to specified length
        - **Scale**: Enables synthesis of **millions of unique text instances** from finite vocabulary
      - **Quality Screening**:
        - **Post-Synthesis Filtering**: Use pre-trained STR models to verify generated text matches target labels
        - **Multi-Model Consensus**: Require agreement from multiple STR models (CRNN, ASTER, ABINet)
        - **Acceptance Rate**: ~60-70% of generated images pass quality screening
  - **Data Scale**:
      - **TextSSR-F (Filtered Dataset)**: 3.55M quality-screened synthetic scene text images
      - **Text Lengths**: 1-25 characters, diverse distributions
      - **Styles**: 50+ scene types (street signs, storefronts, documents, product packaging, etc.)
      - **Languages**: Primarily English + multilingual subset
  - **Training Pipeline**:
      - **Stage 1**: Pre-train diffusion model on real STR datasets for scene text distribution learning
      - **Stage 2**: Fine-tune with PGE + contextual hints for accurate controllable generation
      - **Stage 3**: Large-scale synthesis with text permutations
      - **Stage 4**: Quality filtering to produce TextSSR-F
  - **Experimental Results**:
      - **STR Benchmarks**: Training on TextSSR-F achieves **competitive or superior** performance vs. real-data training
        - **IIIT5K**: 95.3% accuracy (on par with real data)
        - **SVT**: 93.1% (+1.8% over synthetic baselines)
        - **ICDAR datasets**: Consistent improvements over rendering-based synthetic data
      - **Real + Synthetic Mix**: Best results achieved by combining TextSSR-F with real data (+2.1% average gain)
      - **Zero-Shot Transfer**: Strong generalization to unseen fonts, languages, distortions
  - **Ablation Studies**:
      - **PGE Contribution**: +8.3% accuracy over baseline diffusion
      - **Contextual Hints**: +5.7% over glyph-only conditioning
      - **Quality Filtering**: Improves downstream STR accuracy by 4.2%
  - **Publication**: ICCV 2025 | arXiv May 2025
  - **Institution**: Not explicitly stated (academic research)
  - **Open Source**: ✅ TextSSR-F Dataset (3.55M images), Code, Pre-trained Diffusion Models - Release details in paper
  - **Significance**:
      - **Bridges Rendering-Generation Gap**: Combines control of rendering methods with realism of generative models
      - **Solves STR Data Scarcity**: Enables unlimited diverse training data generation for low-resource scenarios
      - **Generalizable Framework**: Contextual hint mechanism applicable to other conditional generation tasks
      - **Practical Impact**: Reduces annotation cost for STR while maintaining or improving model performance
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/1604.06646">📄 Synthetic Text Localisation</a></b><br>
<code>arXiv 1604.06646</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Synthetic Data for Scene Text Detection** - Generates high-quality scene text images for training text detection models
  - **Data Synthesis Method** - **Geometry-Aware Scene Text Overlaying Pipeline**:
      - **Core Innovation**: Naturally overlays synthetic text onto real scenes, **considering local 3D scene geometry** rather than simple 2D overlaying
      - **Key Technical Components**:
        - **Scene Geometry Understanding**: Uses CNN to predict dense depth map, estimates local surface normals
        - **Text Alignment**: Performs perspective transformation based on estimated plane orientation, aligning text with surfaces
        - **Region Constraints**: Uses gPb-UCM segmentation to ensure text is confined to regions with uniform color and texture
        - **Color Adaptation**: Learns text-background color pairs from IIIT5K dataset, adaptively matches target regions
        - **Poisson Fusion**: Uses Poisson image editing for seamless text-background integration, appears naturally embedded
      - **Key Technical Advantages**:
        - **3D Geometry Awareness**: Text perspective naturally matches surface orientation, not flat overlay
        - **Region-Constrained**: Avoids unrealistic placement across heterogeneous areas
        - **Adaptive Coloring**: Text color naturally harmonizes with background
        - **Seamless Fusion**: Poisson blending removes synthetic artifacts
      - **Synthesis Pipeline**:
        1. **Input**: Natural scene image (8,000 background images collected via Google Image Search)
        2. **Depth Estimation**: CNN predicts dense depth map
        3. **Surface Normal Estimation**: Calculates local surface orientation from depth
        4. **Segmentation**: gPb-UCM generates candidate regions
        5. **Region Selection**: Filters regions by size, aspect ratio, uniformity
        6. **Color Sampling**: Selects text-background color pair matching region
        7. **Text Rendering**: Renders word with selected color (text sampled from Newsgroup20 dataset)
        8. **Perspective Transform**: Applies perspective warp based on surface normal
        9. **Poisson Blending**: Seamlessly integrates text into scene
        10. **Output**: Synthetic scene text image + bounding box annotations
  - **Data Scale**:
      - **SynthText Dataset**: 800K synthetic scene text images
      - **Annotations**: Word-level and character-level bounding boxes
      - **Background Images**: 8,000 images collected via Google Image Search (filtered to ensure no text)
      - **Text Sources**: Newsgroup20 dataset (words, lines, paragraphs)
  - **Experimental Results** - **State-of-the-art Text Detection**:
      - **Training Strategy**: Pre-train on SynthText → fine-tune on small real datasets
      - **Results on ICDAR 2013**:
        - Synthetic-only pre-training significantly boosts performance
        - With fine-tuning: Achieves **F-measure 84.2%**, competitive SOTA level
      - **Results on Multi-Oriented Text (MSRA-TD500)**:
        - Demonstrates effectiveness on complex multi-oriented text scenarios
      - **Key Finding**: Synthetic data with proper geometric modeling effectively transfers to real-world text detection
  - **Ablation Studies**:
      - **Geometry Awareness**: Models using geometry-aware synthesis outperform flat text overlays
      - **Color Adaptation**: Adaptive coloring improves detection compared to random colors
      - **Poisson Fusion**: Seamless blending crucial for realistic appearance
  - **Publication**: CVPR 2016 | arXiv April 2016
  - **Institution**: University of Oxford
  - **Authors**: Ankush Gupta, Andrea Vedaldi, Andrew Zisserman
  - **Open Source**: ✅ [Code](https://github.com/ankush-me/SynthText) and [Dataset](https://www.robots.ox.ac.uk/~vgg/data/scenetext/)
  - **Significance**:
      - **Pioneering Work**: One of the first to systematically address synthetic data for scene text detection with geometry awareness
      - **Geometry-Aware Synthesis**: Introduced 3D geometric considerations to text synthesis, significantly improving realism
      - **Impact**: SynthText dataset widely used in text detection research as pre-training data
      - **Transfer Learning**: Demonstrated effective synthetic-to-real transfer for text detection tasks
  
  #### 🏠 3D Scene Synthesis
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2407.06084">📄 SynVL3D</a></b><br>
<code>arXiv 2407.06084</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-July_2024-red?style=flat-square"/>
</summary>

  - **Focus**: **3D Vision-Language Pretraining with Large-Scale Synthetic Data** - Building comprehensive synthetic 3D scene-text corpus to address limited scene-level diversity and insufficient fine-grained annotations in 3D-VLP datasets
  - **Data Synthesis Method** - **3D Simulator-Driven Scene Generation + Multi-Granularity Text Description Synthesis**:
      - **Core Innovation**: Leverages free 3D simulator to construct large-scale, diverse synthetic 3D scene datasets with 1M descriptions across object, view, and room levels
      - **Problem Identification**: Existing 3D-VLP datasets suffer from small scale and limited annotations
        - **Data Scarcity**: ScanScribe only has 1.2K scenes and 280K textual annotations
        - **Limited Diversity**: Restricted scene types and object categories
        - **High Collection Cost**: 3D scene data collection and annotation extremely expensive
        - **Missing Fine-Grained Associations**: Lack of object-level, view-level, room-level multi-tier correlations
      - **3D Scene Generation**:
        - **Simulator Platform**: Based on AI2-THOR 3D simulator environment
        - **Scene Scale**: 10,000 indoor 3D scenes with 108 object categories
        - **Scene Graph Construction**:
          - Build scene graph for each house (scene) describing spatial relationships between objects
          - Define relationships based on object spatial position, size, and shape
          - Three major relationship types:
            1. **Support Relations** (e.g., on, in): Based on physical contact and containment
            2. **Spatial Relations** (e.g., next to, in front of): Based on relative positions
            3. **Comparative Relations** (e.g., bigger than, same shape as): Based on size and shape
        - **Precise Annotations**: Provide semantic (category), visual (high-quality mesh), fine-grained visual annotations (error-free position, orientation, segmentation masks)
      - **Multi-Granularity Text Description Synthesis**:
        - **Total Count**: Over 1M templated and free-form descriptions
        - **Three Description Types**:
          1. **Template-Based Descriptions**:
             - **Object Appearance**: Use off-the-shelf image captioner to generate captions for each object's front view
             - **Relation Triplets**: <object1, relation, object2> format using template "the object1 is relation to object2"
             - **Instance Descriptions**: Merge appearance descriptions with neighboring object relation descriptions into paragraphs
          2. **Free-Form Descriptions**: Use GPT-3 to rephrase templated descriptions for enhanced naturalness
          3. **Multi-View Descriptions**: Generate descriptions for different perspectives and room levels
        - **Phrase-Region Association**: Train distinct identifiers for each noun phrase, establishing phrase-spatial region connections
      - **Multi-Level Association Establishment**:
        - **Object-Level Association**: Phrase identifiers precisely correspond to 3D object bounding boxes
        - **View-Level Association**: Object-text alignment across multiple perspectives
        - **Room-Level Association**: Scene-wide descriptions associated with 3D scenes
  - **SynFormer3D Pretraining Framework**:
      - **Unified Transformer Architecture**: Simple unified model for aligning 3D scenes with language
      - **Three Components**:
        1. **3D Object Encoder**: Processes point cloud features
        2. **Text Encoder**: Processes natural language descriptions
        3. **Cross-Modal Fusion Module**: Achieves 3D-text alignment
      - **Fine-Grained Pretraining Tasks**:
        1. **Object Relation Prediction (ORP)**: Predict spatial relationships between 3D objects
        2. **Multi-Level Region-Word Alignment (MRWA)**: Alignment across object, room, scene levels
        3. **View-Aggregated Region-Word Alignment (VRWA)**: Multi-view information aggregation alignment
      - **Synthetic-to-Real Domain Adaptation**:
        - **Triple Domain Discriminator**: Vision domain, language domain, vision-language joint domain
        - **Gradient Reversal Layer**: Min-max optimization to address domain shift
        - **Joint Adaptation**: Simultaneously handles unimodal and cross-modal domain shifts
  - **Data Scale**:
      - **SynVL3D Dataset**: 10,000 indoor scenes with 1M+ text descriptions
      - **Object Coverage**: 108 object categories
      - **Relationship Types**: Three major categories: support, spatial, comparative
      - **Multi-Granularity Annotations**: Object-level, view-level, room-level three-tier associations
  - **Experimental Results** - **SOTA Performance on 3D-VL Tasks**:
      - **3D Visual Grounding**:
        - Nr3D: 65.5% accuracy (vs 3D-VISTA 64.2%, +1.3%)
        - Sr3D: 77.9% accuracy (vs 3D-VISTA 76.4%, +1.5%)
        - ScanRefer: 52.3%@0.25IoU, 46.2%@0.5IoU
      - **3D Dense Captioning**:
        - Scan2Cap: CIDEr score 72.1@0.25IoU (vs 3D-VISTA 71.0, +1.1%)
        - Comprehensive improvements across BLEU-4, METEOR, ROUGE metrics
      - **3D Question Answering**:
        - ScanQA: EM@1 reaches 27.6% (vs 3D-VISTA 26.5%, +1.1%)
        - Improvements in BLEU-4, ROUGE, METEOR language generation metrics
  - **Ablation Study Findings**:
      - **Fine-Grained Pretraining Task Contributions**:
        - Object Relation Prediction (+6.2% VG, +6.8% Cap, +2.0% QA)
        - Multi-Level Region-Word Alignment (+5.8% VG, +6.4% Cap, +2.2% QA)
        - View-Aggregated Alignment (+1.6% VG, +1.2% Cap, +0.3% QA)
      - **Synthetic-to-Real Adaptation**: Triple domain adaptation significantly improves performance (+14.4% VG, +13.4% Cap, +3.9% QA)
      - **Multi-Level Alignment**: Object, room, scene-level alignments all contribute, with combination achieving best results
  - **Key Findings**:
      - **Synthetic Data Effectiveness**: Pure synthetic data pretraining models excel on real 3D scenes
      - **Multi-Granularity Association Value**: Object-view-room three-tier associations crucial for performance improvement
      - **Domain Adaptation Importance**: Synthetic-to-real domain adaptation critical for generalization capability
      - **Scalability**: Compared to real data collection, synthetic approach offers low cost and high scalability
  - **Publication**: arXiv July 2024 | Peking University
  - **Open Source**: ✅ SynVL3D Dataset (10K scenes + 1M descriptions) + SynFormer3D Model + Training Code
  - **Significance**:
      - **3D-VLP Data Breakthrough**: First large-scale, multi-level synthetic 3D vision-language dataset
      - **Cost-Effective Solution**: Provides low-cost, high-quality data acquisition approach for 3D scene understanding
      - **Multi-Granularity Framework**: Establishes object-view-room three-tier 3D-text association framework
      - **Domain Adaptation Innovation**: Proposes effective domain adaptation methods for 3D vision-language tasks
  

</details>
---

#### 🔄 Contrastive Learning & Image Difference

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

  - **Focus**: **Code-guided synthetic chart data and chart-to-code evaluation** — Two-stage automated pipeline: VLM redraws real charts into Python plotting code; code LLM iteratively augments scripts to generate diverse charts, forming a large multimodal corpus and a redraw evaluation protocol
  - **Data Synthesis Method** - **VLM Redraw → Code LLM Iterative Augmentation**:
      1) **VLM Chart Redraw**: From seed charts (ChartQA 13K), phi‑3.5‑vision‑instruct produces executable plotting code as structured representations
      2) **LLM Code Augmentation**: Codestral‑22B performs ~20 rounds of code-level augmentations (type/library/style/topic), executing to render new charts; expands scale and diversity by transforming code, not pixels
  - **Data & Resources**:
      - **ChartGen‑200K**: 222.5K image‑code pairs covering 27 chart types and 11 plotting libraries; plus CSV, DocTags, text summaries, and QA; held‑out 4.3K for redraw evaluation
      - **Evaluation Protocol**: GPT‑4o as judge for code-level (data fidelity 0–1; semantics/style 0–10) and rendered image-level (0–10) similarity
  - **Findings**:
      - 6 open‑weight VLMs (3B–26B) show notable gaps (best data fidelity ≤0.58/1, best image similarity ≤7.48/10); chart‑to‑code remains challenging
      - Compared with Plot2Code, ChartMimic, ChartX, ChartCoder, ChartGen provides larger scale, broader library coverage, and richer multimodal support
  - **Significance**:
      - **Code as canonical representation**: Enables derived summaries/QA/CSV for scalable training/evaluation
      - **Beyond QA/Summary**: Shifts emphasis to redraw/code generation for fine‑grained assessment
  - **Open Source**: Code, data, and benchmark under CC‑BY‑4.0: `https://github.com/SD122025/ChartGen/`
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2508.06492">📄 Effective Chart Dataset (ECD)</a></b><br>
<code>arXiv 2508.06492</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **High-quality synthetic training data for chart understanding** — Proposes a five-stage modular pipeline to build the ECD training set and the ECDBench benchmark, yielding consistent gains for MLLMs on chart understanding
  - **Data Synthesis Method** - **Five-stage modular pipeline with quality filtering**:
      1) **Single-plot generation (code-function + data decoupling)**: 29 chart functions; GPT-4o generates data/args conditioned on themes+APIs; renders 10,875 single plots
      2) **Conditional multi-subplot composition**: Sequentially generates subplots conditioned on prior ones to ensure semantic coherence (6,006 figures, avg. 4 subplots)
      3) **Chart image diversification**: Adds annotations, area shading, zoom-in inset, font/border/style variants, layout perturbations
      4) **Image quality filtering**: Scores with "visual clarity" + "semantic coherence"; filters to 10,535 images from 16,829
      5) **QA generation & filtering**: Produces both descriptive and reasoning QA; retains high-confidence pairs (final 321,544 QA)
  - **Data Scale**:
      - **ECD (train)**: 10,535 images + 321,544 QA (25 themes, 29 chart types, 252 type combinations)
      - **ECDBench (test)**: 1,224 images (364 single-plot, 860 multi-subplot) + 2,448 QA (1 descriptive + 1 reasoning per image)
  - **Results (consistent multi-model gains)**:
      - On CharXiv, ChartQA, ReachQA, ChartBench, ChartX, and ECDBench, four open-source MLLMs (LLaVA-Next-Llama3-8B, MiniCPM-V2.6, Phi-3-Vision, Qwen2.5-VL-7B) show overall improvements
      - Example: Qwen2.5-VL-7B improves on CharXiv Avg. 61.36%→67.40%; ECDBench 38.19%→50.86% (per Tables 2 & 3)
  - **Key Advantages**:
      - **Code-data decoupling + conditional subplot generation**: Enhances diversity while maintaining cross-subplot coherence
      - **Dual-metric quality filter**: Lower FID and higher average entropy vs prior synthetic chart datasets
      - **Reasoning QA with rationale**: Enables training for explainable reasoning
  - **Resources & Reproducibility**:
      - Full pipeline description and ablations provided; code/data planned as per paper
      - Code/Data: `https://github.com/yuweiyang-anu/ECD` (as indicated by paper)
  - **Significance**:
      - **Realism & Complexity**: Closer alignment with real scientific charts (lower FID, higher entropy)
      - **General & Extensible**: Scales to more subplot combinations/themes/layouts; a strong training basis for chart understanding
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2403.07750">📄 Synth²</a></b><br>
<code>arXiv 2403.07750</code>
</summary>

  - **Data Synthesis Method** - **LLM Caption + Text-to-Image Embedding Generation**:
      - **Core Innovation**: First fully synthetic VLM training approach that synthesizes both captions and image embeddings, operating in embedding space to bypass pixel-level processing
      - **Two-Stage Pipeline**:
        1. **Synthetic Caption Generation**: Gemini Pro generates diverse captions using class-based prompting from ImageNet-21k (30-40 word factual descriptions)
        2. **Image Embedding Generation**: MUSE text-to-image model generates VQ-tokens directly (bypasses pixel rendering/encoding for efficiency)
      - **Controlled Study Design**: Both text-to-image generator and VLM pre-trained on identical dataset (Conceptual Captions v2) to isolate synthetic data contribution vs. knowledge transfer
      - **Efficiency Innovation**: VLM architecture uses identical VQ-GAN backbone as image generator, enabling seamless embedding-level training (25% faster than pixel-space)
  - **Key Technical Components**:
      - **Fair Evaluation Protocol**: Pre-trains custom MUSE generator on same 10.1M CCv2 pairs used for VLM baseline (prevents off-the-shelf model knowledge leakage)
      - **VQ-Based Design**: Discrete tokens converted to soft embeddings + Perceiver Resampler for cross-attention
      - **Mixed Training Strategy**: Combines synthetic + real data during fine-tuning to prevent model collapse
      - **Semantic Diversity Analysis**: K-means clustering reveals GenPair has more uniform distribution (57.7% in top-5 clusters) vs. real datasets (69.8%-83.0%)
  - **Experimental Results**:
      - **Scene Description**: MS-COCO CIDEr 22.1→33.4 (+51%), Flickr-30k 12.7→20.8 (+64%)
      - **Scene Understanding QA**: VQAv2 29.1→35.3 (+21%)
      - **External Knowledge QA**: OKVQA 32.4→36.1 (+11%)
      - **Efficiency Gains**: Achieves baseline parity with ~1/3 training steps, 2.08 vs 1.66 steps/sec (embedding vs pixel)
      - **Data Efficiency**: Comparable performance to models trained on 40× more paired data (vs. DC-BLIP 5.5B real data)
  - **Comparative Analysis**:
      - **vs. ITIT**: 35.4 vs 32.1 CIDEr zero-shot (with similar parameters and data usage)
      - **vs. DC & SimVLM**: Competitive results with 632M parameters vs 1.4-1.7B parameters
      - **Semantic Concentration**: GenPair shows highest entropy (3.81) and lowest concentration, indicating superior diversity
  - **Cost Efficiency**:
      - **Training Speed**: 25% faster than pixel-space training without performance degradation
      - **Memory Efficiency**: Eliminates costly pixel encoding/decoding during synthetic data training
      - **Data Requirements**: 10.1M real + 711M synthetic vs traditional methods requiring billions of real pairs
  - **Institution**: Google DeepMind
  - **Authors**: Sahand Sharifzadeh, Christos Kaplanis, Shreya Pathak, Dharshan Kumaran, et al.
  - **Open Source**: ⚠️ Code/data availability not specified in paper
  - **Significance**:
      - **Paradigm Innovation**: First demonstration of fully synthetic image-text pair training for VLMs without reliance on massive real datasets
      - **Embedding-Space Efficiency**: Proves embedding-level generation maintains quality while dramatically improving computational efficiency
      - **Controlled Methodology**: Establishes rigorous experimental framework for isolating synthetic data contributions
      - **Practical Deployment**: Enables customized dataset creation and resource-efficient VLM training for specialized domains
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2507.02948">📄 DriveMRP</a></b><br>
<code>arXiv 2507.02948</code>
</summary>

  - **Data Synthesis Method** - **BEV-Based High-Risk Motion Simulation for Autonomous Driving**:
      - **Core Innovation**: First scalable synthetic dataset for VLM-based motion risk prediction in autonomous driving, addressing long-tail high-risk scenario scarcity
      - **Three-Dimensional Risk Modeling**: Systematically synthesizes risks from ego-vehicle behavior, other vehicle interactions, and environmental constraints
      - **BEV Polynomial Simulation**: Uses polynomial trajectory generation with vehicle dynamics constraints to create physically plausible high-risk motions
      - **Data Scale**: DriveMRP-10K dataset with 10,000 high-quality motion risk scenarios covering collision, hard braking, abnormal acceleration, lane violations
  - **Key Technical Components**:
      - **High-Risk Scenario Selection**: Collision events, hard braking/acceleration, lane violations/off-road departures based on real-world traffic accident analysis
      - **Rule-Based Definition**: Precise thresholds for safety distance (collision), acceleration magnitude/duration (hard braking), geometric relationships (lane violations)
      - **Motion Projection Visual Prompting**: Projects BEV trajectories onto ego-vehicle's front-view camera to bridge modality gap between coordinates and vision
      - **Human-in-the-Loop Quality Control**: Manual screening filters out physically implausible trajectories and ensures clear camera projection visibility
  - **DriveMRP-Agent Framework**:
      - **VLM-Agnostic Architecture**: Works with multiple VLMs (Qwen2.5-VL-7B, InternVL, LLaVA) using LoRA fine-tuning
      - **Chain-of-Thought Reasoning**: "Scene Understanding → Motion Analysis → Risk Prediction" cognitive pathway for interpretable risk assessment
      - **Multi-Modal Input Integration**: Combines BEV layout, front-view scene image, and projected motion waypoints
      - **GPT-4o Caption Generation**: Structured natural language descriptions covering scene analysis, motion behavior explanation, and risk categorization
  - **Experimental Results**:
      - **Synthetic Data Performance**: Accident recognition accuracy 27.13% → 88.03% (+60.9%) on DriveMRP-10K test set
      - **Zero-Shot Generalization**: Real-world high-risk dataset accuracy 29.42% → 68.50% (+39.1%) without real-world training exposure
      - **Cross-Model Enhancement**: Consistent improvements across LLaVA-1.5-7B, Llama3.2-vision-11B, Qwen2.5-VL-7B baselines
      - **Scene Understanding Metrics**: ROUGE-1-F1 48.54→69.08, BERTScore 68.83→81.25 demonstrating comprehensive environment comprehension
  - **Ablation Studies**:
      - **BEV Information**: Critical for global contextual understanding and spatial relationship reasoning
      - **Visual Trajectory Projection**: Significantly outperforms raw coordinate sequences, bridging vision-language modality gap
      - **Multi-Input Fusion**: Combined BEV + front-view + projected trajectories achieves optimal performance (88.03% accuracy)
  - **Cost & Generalization**:
      - **Training Efficiency**: LoRA fine-tuning on 8 NVIDIA H100 GPUs with Flash Attention acceleration
      - **Real-World Transfer**: Strong zero-shot performance on proprietary real-world dataset validates synthetic-to-real generalization
      - **Plug-and-Play**: Dataset enhances multiple general-purpose VLMs for driving safety applications
  - **Institution**: Westlake University, Xiaomi EV, Zhejiang University
  - **Authors**: Zhiyi Hou, Enhui Ma, Fang Li, Zhiyi Lai, Kalok Ho, et al.
  - **Open Source**: ✅ [Code & Dataset](https://github.com/xiaomi-ev/DriveMRP) (as indicated)
  - **Significance**:
      - **Autonomous Driving Safety**: Addresses critical gap in high-risk scenario coverage for safer autonomous systems
      - **Synthetic Data Paradigm**: Demonstrates effective synthesis of rare but critical driving events difficult to collect at scale
      - **Interpretable AI**: Provides explainable risk predictions with causal analysis for continuous algorithm improvement
      - **Industry Impact**: Enables development of robust motion planning algorithms for complex, unstructured driving environments
  

</details>
---

### 💭 Think with Image

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
<img src="https://img.shields.io/badge/Institution-October_2024-red?style=flat-square"/>
</summary>

  - **Focus**: **Large-Scale Multimodal Reasoning Synthetic Dataset** - Building multimodal reasoning dataset with explicit thinking processes to aid Vision Language Model reasoning capability development
  - **Data Synthesis Method** - **Multi-Modal Large Model Driven Thinking Trajectory Synthesis**:
      - **Core Innovation**: Leverages SOTA vision-language models to generate large-scale synthetic dataset with explicit reasoning steps, capturing VLM's step-by-step thinking processes and final descriptive answers
      - **Problem Identification**: Existing multimodal dataset limitations
        - **Lack of Reasoning Transparency**: Most datasets focus only on input-output mappings without capturing intermediate reasoning steps
        - **Difficult Reasoning Diagnosis**: Cannot understand model decision processes or diagnose model failures
        - **Domain Limitations**: Existing reasoning datasets typically domain-specific or limited in scale
        - **Proprietary Data Barriers**: Training data usually proprietary or limited in scope, hindering broader research
      - **Data Generation Pipeline**:
        - **Data Source**: 250,000 images from carefully selected ImageNet-21k dataset samples
        - **Image Selection Criteria**:
          1. **Visual Quality**: High resolution and clarity
          2. **Content Integrity**: No significant occlusion or corruption
          3. **Semantic Diversity**: Diverse semantic categories to promote generalization
          4. **Complexity Balance**: Balanced representation across different visual complexity levels
        - **Dual-Model Generation Strategy**:
          - **GLM-4.1V-9B-Thinking**: Generates thinking trajectory 1
          - **Kimi-VL-A3B-Thinking-2506**: Generates thinking trajectory 2
          - Each image paired with two thinking-answer sequence sets, providing reasoning diversity
      - **Unified Prompt Design**:
        - **Prompt Template**: "Please analyze this image step by step. Explain your reasoning process. Describe this image and give as much information as possible"
        - **Guiding Objectives**:
          1. First describe observed content
          2. Explain reasoning process
          3. Provide final detailed answer
        - **Standardized Process**: Ensures consistency and quality in thinking chain generation
      - **Thinking-Answer Separation**:
        - **Thinking Tokens (Think)**: Intermediate reasoning steps describing objects, context, relationships
        - **Answer Tokens (Answer)**: Final descriptive answers that refine or finalize image interpretation
        - **Paired Structure**: Each image → 2×(thinking, answer) pairs, supporting reasoning quality and outcome accuracy evaluation
  - **Data Scale and Statistics**:
      - **Total Data Volume**: 250,000 images, 500,000 thinking-answer pairs
      - **Category Coverage**: 15,234 unique ImageNet-21k categories
      - **Average Distribution**: 16.4 images per category, standard deviation 12.8
      - **Token Statistics**:
        - **Minimum Tokens**: 521 tokens/sample
        - **Maximum Tokens**: 196,388 tokens/sample
        - **Average Tokens**: 1,542 tokens/sample
        - **Total Token Count**: 300 million tokens
      - **Diversity Metrics**: Spans broad semantic categories across scientific, natural, and social sciences
  - **Synthetic Quality Control**:
      - **Consistency Verification**: Ensure generated thinking and answers are logically consistent
      - **Multi-Model Validation**: Cross-validation from two SOTA VLMs improves reliability
      - **Length Filtering**: Remove excessively short or abnormally long responses
      - **Content Quality**: Assess response quality and relevance through LLM evaluation
  - **Benchmark Evaluation Framework**:
      - **Reasoning Quality Metrics**:
        - **Semantic Similarity**: BERTScore, Sentence-BERT cosine similarity
        - **Lexical Overlap**: ROUGE-1, ROUGE-L, Jaccard index, overlap coefficient
        - **Vector Space**: TF-IDF cosine similarity
      - **Model Comparison**: Performance evaluation of 5 SOTA VLMs on ImageNet-Think
        - InternVL-3.5-8B, VL-Rethinker-7B, VisionThink-Efficient
        - OpenVLThinker-7B, R1-OneVision-7B
      - **Thinking vs Answer Analysis**: Thinking tokens superior in semantic alignment, answer tokens better in lexical overlap
  - **Experimental Findings**:
      - **Reasoning Richness**: Thinking trajectories provide rich intermediate reasoning steps, helping understand VLM decision processes
      - **Model Differences**: Different VLMs show significant differences in reasoning style and quality
      - **Evaluation Dimensions**: Multi-dimensional evaluation reveals different patterns in semantic understanding and lexical expression
      - **Scalability**: Synthetic approach can be scaled to larger scales and more visual domains
  - **Key Contributions**:
      - **First Large-Scale Reasoning Dataset**: ImageNet-Think provides largest-scale multimodal reasoning dataset
      - **Explicit Thinking Capture**: Systematically captures VLM's step-by-step reasoning processes
      - **Multi-Model Perspective**: Leverages multiple SOTA VLMs to provide reasoning diversity
      - **Standardized Evaluation**: Establishes multi-dimensional reasoning quality evaluation framework
  - **Publication**: arXiv October 2024 | Argonne National Laboratory
  - **Open Source**: ✅ ImageNet-Think-250K Dataset + Evaluation Benchmarks + Data Generation Code - Publicly available to support research
  - **Significance**:
      - **Reasoning Transparency**: Provides transparent thinking process data for multimodal reasoning research
      - **Model Diagnostic Tool**: Helps researchers understand and improve VLM reasoning capabilities
      - **Standardized Benchmark**: Establishes standards for multimodal reasoning model evaluation
      - **Research Acceleration**: Reduces barriers to reasoning data acquisition, promoting broader research
  
  #### 🤖 Robotic Action Synthesis
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2505.03233">📄 GraspVLA</a></b><br>
<code>arXiv 2505.03233</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data** - First VLA model trained exclusively on large-scale synthetic action data with direct sim-to-real transfer capabilities
  - **Data Synthesis Method** - **Billion-Scale Photorealistic Robotic Action Generation**:
      - **Core Innovation**: First systematic approach to train Vision-Language-Action (VLA) models entirely on large-scale synthetic action data, demonstrating that synthetic data can replace real-world teleoperation data for robotic learning
      - **SynGrasp-1B Dataset Generation**:
        - **Massive Scale**: **1 billion frames** of robotic grasping data (10M trajectories × ~100 frames each)
        - **Object Diversity**: 10,680 unique objects from 240 categories sourced from Objaverse
        - **Scene Diversity**: 1M unique scenes with extensive domain randomization
        - **Photorealistic Rendering**: Advanced ray-tracing rendering using NVIDIA IsaacSim for high-fidelity visual synthesis
      - **Comprehensive Domain Randomization**:
        - **Visual Randomization**: Materials (table/robot), lighting (point/directional/dome), camera views, backgrounds
        - **Physical Randomization**: Object layouts, grasp poses, robot trajectories, table heights (-0.1m to 0.2m)
        - **Temporal Randomization**: Trajectory variations with CuRobo motion planning
        - **Instruction Randomization**: Natural language instruction templates for object manipulation
      - **Progressive Action Generation (PAG)**:
        - **Chain-of-Thought Architecture**: Integrates autoregressive perception (VLM) + flow-matching action generation
        - **Multi-Modal Training**: Joint training on synthetic action data + Internet grounding data (GRIT)
        - **Hierarchical Prediction**: Bounding box → grasp pose → action chunk generation
        - **Cross-Modal Alignment**: Bridges sim-to-real gap through Internet data co-training
      - **Efficient Data Generation Pipeline**:
        - **Caching Mechanism**: Avoids redundant object loading while ensuring diversity
        - **Asynchronous Writing**: Parallel image saving and label generation
        - **Parallel Simulation**: Multi-threaded physics simulation and rendering
        - **Quality Assurance**: Force-closure based grasp synthesis with trajectory validation
  - **Technical Architecture**:
      - **Vision-Language Backbone**: Autoregressive transformer processing dual-camera inputs (front + side view)
      - **Action Expert**: Flow-matching based continuous action generation conditioned on VLM features
      - **Proprioception Integration**: Robot state tokens from latest two timesteps for accurate 3D sensing
      - **Unified Training**: Single framework handling both Internet grounding and synthetic action tasks
  - **Data Scale & Quality**:
      - **Total Synthetic Data**: 1B frames with precise annotations (camera calibration, 3D poses, bounding boxes)
      - **Object Coverage**: 240 categories ensuring comprehensive real-world object generalization
      - **Annotation Richness**: Fine-grained labels including depth maps, segmentation masks, force-closure metrics
      - **Cross-Embodiment Ready**: Scalable pipeline adaptable to different robots and camera configurations
  - **Evaluation & Results**:
      - **Zero-Shot Performance**: 93.3% success rate on synthetic categories, 84.7% on web categories (vs. π₀: 42.3%/17.8%)
      - **Sim-to-Real Transfer**: Direct deployment without real-world fine-tuning, superior to teleoperation-trained models
      - **Cross-Domain Generalization**: Strong performance on objects never seen during training
      - **Few-Shot Adaptability**: 90% success with bounding box annotations only, 90% with full trajectory data
      - **LIBERO Benchmark**: Surpasses fine-tuned π₀ and OpenVLA in zero-shot setting (82.0% vs 62.7%/33.7%)
  - **Key Technical Contributions**:
      - **Synthetic-Only Training**: Proves synthetic data sufficiency for robotic foundation model training
      - **Billion-Scale Action Data**: First dataset of this scale globally for robotic manipulation
      - **Progressive Action Generation**: Novel architecture enabling joint perception and action synthesis
      - **Domain Bridging**: Systematic approach to sim-to-real transfer through Internet data integration
  - **Institution**: Peking University, Galbot
  - **Open Source**: ✅ [SynGrasp-1B Dataset & Pre-trained Weights](https://pku-epic.github.io/GraspVLA-web)
  

</details>
---

### ✂️ Image Editing (Method + Data)

This category focuses on **instruction-guided image editing** where models learn to transform images based on natural language instructions. These works typically combine **method innovation** (novel editing pipelines, architectures) with **large-scale data synthesis** (automated data engines, quality benchmarks), making them distinct from pure dataset construction efforts.

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2406.11262">📄 GenLLaVA</a></b><br>
<code>arXiv 2406.11262</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Generative Visual Instruction Tuning** - First unified multimodal model achieving image understanding, generation, and editing capabilities simultaneously without performance degradation
  - **Data Synthesis Method** - **Triple-Capability Unified Training Pipeline**:
      - **Core Innovation**: First systematic approach integrating three pre-trained models (Mistral-7B + SigLIP + Stable Diffusion v1.4) through instruction fine-tuning for unified visual understanding, generation, and editing
      - **Architecture Design**:
        - **Language Model**: **Mistral-7B** as foundation LLM for superior language capabilities
        - **Visual Encoder**: **SigLIP-L/384px** (stronger than CLIP) for robust image-text matching
        - **Generation Module**: **Stable Diffusion v1.4** with Q-former generation head for text-to-image synthesis
        - **Projection Layer**: 2-layer GELU MLP projecting visual patches to language embedding space
      - **Visual Generation Mechanism**:
        - **Visual Tokens**: Append N learnable [IMG] tokens after instructions, with trainable word embeddings
        - **Generation Head**: Q-former sequence-to-sequence model T converts [IMG] tokens to semantic latent set U = {u₁, u₂, ..., uₗ}
        - **Latent Diffusion Integration**: Visual latent U guides Stable Diffusion for image generation/editing in latent space
        - **Special Tokens**: [SOI]/[EOI] mark start/end of visual generation tokens for task disambiguation
      - **Training Data Composition** (GVIT-mix-2076K):
        - **Image Understanding** [61.56%]: LLaVA fine-tuning instruction set for visual comprehension tasks
        - **Image Generation** [26.88%]: ~558K inverted image-text pairs from LAION/SBU/CC3M with GPT-4 generated prompts (e.g., "Please generate an image of [caption]")
        - **Image Editing** [11.56%]: GPT-4V processed editing datasets with natural language editing instructions
      - **Single-Stage Training**: Unlike LLaVA's two-stage approach, GenLLaVA uses unified single-phase instruction tuning across all capabilities
  - **Technical Implementation Details**:
      - **Task Token System**: Specialized tokens guide model behavior ([SOI], [EOI] for generation tasks)
      - **Multi-Task Loss**: Combined autoregressive language modeling + diffusion denoising objectives
      - **Generation Token Count**: Optimal N=16 visual tokens (ablation shows N=4 overfits, N>16 degrades performance)
      - **Vision Encoder Ablation**: SigLIP-L/384px > CLIP-L/336px > CLIP-B/224px across all tasks
  - **Data Scale**:
      - **Total Training Set**: **2.076M instruction-following examples** (GVIT-mix-2076K)
      - **Generation Data**: 558K image-text pairs with dynamically generated instruction prefixes
      - **Understanding Data**: LLaVA-1.5 instruction tuning dataset (visual reasoning, VQA, etc.)
      - **Editing Data**: Natural language instruction-guided editing examples processed by GPT-4V
  - **Evaluation & Results**:
      - **Advanced Knowledge**: MathVista (30.5% vs 28.3% Unified-IO2), MMMU (37.1% vs 35.5% Unified-IO2)
      - **General Understanding**: SEED-B (64.5% vs 61.6% Unified-IO2), MMBench (66.8% vs 57.9% Unified-IO2)
      - **Generation Tasks**: CC3M (12.5 FID), MS-COCO (0.73 CLIPScore) competitive with specialized models
      - **Editing Capability**: EVR benchmark (66.9% vs 50.2% Unified-IO2) demonstrates superior instruction-guided editing
      - **Multi-Task Trade-off**: Maintains competitive performance across all tasks vs. specialized models
  - **Key Technical Contributions**:
      - **Unified Architecture**: First end-to-end model for understanding + generation + editing without capability conflicts
      - **Instruction Integration**: Seamless natural language control for all visual tasks through shared instruction interface
      - **Performance Preservation**: Demonstrates multi-capability training doesn't degrade individual task performance when properly designed
      - **Scalable Framework**: Modular design allowing easy integration of stronger visual encoders, LLMs, or diffusion models
  - **Institution**: Rice University, Google DeepMind
  - **Open Source**: ✅ [Dataset, Code, Model Checkpoints, Visual Chat Demo](https://arxiv.org/abs/2406.11262)
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2506.03107">📄 ByteMorph</a></b><br>
<code>arXiv 2506.03107</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Non-rigid motion editing** - First large-scale dataset addressing camera motion, object deformation, human articulation, and human-object interaction
  - **Data Synthesis Method** - **Motion-Guided Layered Compositing**:
      - **Core Innovation**: Automated pipeline combining **VFX-inspired layered compositing** with **GPT-4o motion-semantic captioning**
      - **4-Stage Pipeline**:
        1. **Video Source Collection**: Web-scale video corpora → motion detection (optical flow) → high-res (≥720p) motion-rich clips
        2. **Layered Compositing**: Foreground segmentation → background stabilization → motion-preserving layer composition
        3. **GPT-4o Caption Generation**: Multimodal understanding → motion-aware natural language instructions
        4. **Quality Assurance**: CLIP aesthetic scoring + optical flow coherence + LLM instruction-edit alignment verification
      - **Key Advantage**: Preserves realistic motion dynamics at scale (automates manual VFX workflows)
  - **Data Scale**:
      - **ByteMorph-6M**: 6M high-resolution editing triplets (source image, instruction, edited image)
      - **Distribution**: 1.8M camera motion, 1.5M object deformation, 1.8M human articulation, 0.9M HOI
      - **Resolution**: Majority 1024×1024, minimum 512×512
  - **Benchmark**: ByteMorph-Bench (613 expert-verified test samples, difficulty-graded)
  - **Model**: ByteMorpher (Diffusion Transformer baseline)
  - **Experimental Results**:
      - Outperforms InstructPix2Pix/MagicBrush by **+18.3%** on motion metrics
      - Human preference: **73.5%** vs. baselines
      - Demonstrates motion-specific training critical (static dataset models: 32.1% success rate)
  - **Publication**: arXiv June 2025
  - **Institution**: ByteDance Seed, USC, University of Tokyo, UC Berkeley, Stanford, UCLA
  - **Open Source**: ✅ Dataset (6M triplets), Benchmark (613 samples), Model, Code - Release planned on OpenDataLab/HuggingFace
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2505.20275">📄 ImgEdit</a></b><br>
<code>arXiv 2505.20275</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Unified image editing dataset and benchmark** - Covers diverse single-turn edits and challenging multi-turn tasks with identity consistency
  - **Data Synthesis Method** - **Multi-Stage Automated Pipeline Integrating VLM, Detection, Segmentation, and In-Painting**:
      - **Core Innovation**: End-to-end automated workflow combining **VLM orchestration** with **specialized vision tools** for scalable, high-quality editing data generation
      - **5-Stage Unified Pipeline**:
        1. **Initial Candidate Generation (VLM-driven)**:
           - Use **GPT-4o** to analyze source images and generate editing task candidates
           - Covers 8 major editing categories: Object Addition, Removal, Replacement, Attribute Modification, Background Change, Style Transfer, Spatial Rearrangement, Multi-Object Editing
           - Produces natural language editing instructions tailored to image content
        2. **Grounding & Detection**:
           - Deploy **Grounding DINO** / **YOLO-World** for object localization
           - Convert VLM-identified editing targets to precise bounding boxes
           - Handles both explicit objects and abstract concepts (e.g., "the leftmost chair")
        3. **Instance Segmentation**:
           - Apply **SAM (Segment Anything Model)** for pixel-accurate masks
           - Ensures editing operations respect object boundaries
           - Critical for natural compositing in addition/replacement tasks
        4. **Task-Specific In-Painting & Editing**:
           - **Object Removal**: Content-aware inpainting (SD-Inpaint, LaMa)
           - **Object Addition**: Diffusion-based object insertion with harmonization
           - **Replacement**: Mask-guided generation preserving context
           - **Attribute Modification**: Localized style/color adjustments
           - **Background Change**: Foreground preservation + background synthesis
        5. **Quality Control & Post-Processing**:
           - **Automated Filtering**: CLIP-based instruction-image alignment scoring
           - **Artifact Detection**: Identify visible seams, unnatural boundaries, inconsistent lighting
           - **Human-in-the-Loop Validation**: Sample-based quality audits (5% of dataset)
           - **Identity Consistency Verification** (for multi-turn edits): Ensure same objects retain visual identity across turns
      - **Key Innovation**: Unlike pure generative approaches, ImgEdit **decomposes complex edits into modular vision tasks**, ensuring controllability and accuracy
  - **Data Scale**:
      - **ImgEdit Dataset**: 1.2M high-quality editing triplets (source, instruction, edited)
      - **Single-Turn Edits**: 950K samples (novel and complex single-step transformations)
      - **Multi-Turn Edits**: 250K samples (sequential edits with identity consistency)
      - **Instruction Complexity**: Average 18.7 words/instruction, 78.3% requiring spatial/semantic reasoning
  - **Benchmark**: **ImgEdit-Bench**
      - **Size**: 1,000 curated test samples across all editing categories
      - **Difficulty Stratification**: Easy (20%), Medium (50%), Hard (30%)
      - **Evaluation Metrics**: CLIP-Sim, FID, LPIPS, Identity Consistency Score (multi-turn), Human Evaluation
      - **Challenging Cases**: Fine-grained attributes (e.g., "change tie to striped pattern"), multi-object coordination, style preservation across turns
  - **Experimental Results**:
      - State-of-the-art instruction-following editing performance
      - **Multi-turn editing**: ImgEdit-trained models maintain **87.3% identity consistency** vs. **52.1%** for baselines
      - **Generalization**: Strong transfer to unseen editing types and domains
      - **Human Evaluation**: Preferred over InstructPix2Pix, MagicBrush in **69.8%** of comparisons
  - **Publication**: arXiv February 2025 (v1: February 2025)
  - **Institution**: Peking University Shenzhen Graduate School, PengCheng Laboratory, Rabbitpre AI
  - **Open Source**: ✅ Dataset (1.2M triplets), Benchmark (1K samples), Code - Release details in paper
  - **Cross-Reference**: See also [Notable Multimodal Datasets](#-notable-multimodal-datasets) for dataset details
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2506.03481">📄 RefEdit</a></b><br>
<code>arXiv 2506.03481</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Referring expression-guided image editing** - Precise object-level edits via textual referring expressions (e.g., "the red apple on the left")
  - **Data Synthesis Method** - **Scalable Synthetic Pipeline with GPT-4o, Grounding, and FlowChef**:
      - **Core Innovation**: Few-shot learning approach leveraging **scalable synthetic data generation** to outperform million-scale baselines
      - **3-Stage Automated Pipeline**:
        1. **Instruction Generation (GPT-4o-based)**:
           - Input: Source image + object annotations (from RefCOCO/RefCOCO+/RefCOCOg)
           - **GPT-4o** generates diverse editing instructions involving referring expressions
           - Instruction Types: Add, remove, replace, recolor, resize, relocate objects
           - Emphasis on **spatial relationships** (e.g., "the bottle to the right of the laptop")
        2. **Grounding & Segmentation**:
           - **Grounded Segment Anything (Grounded-SAM)** localizes referred objects
           - Produces precise masks for editing targets
           - Handles ambiguous references via context reasoning
        3. **Controlled Editing with FlowChef**:
           - **FlowChef**: Flow-based compositing for natural object insertion/modification
           - Preserves background consistency while executing edits
           - Quality filtering: CLIP-based verification of instruction adherence
      - **Key Finding**: Only **20K synthetic triplets** enable model to surpass baselines trained on **>1M samples**
  - **Data Scale**:
      - **RefEdit Training Data**: 20K high-quality synthetic editing triplets
      - **Rooted in RefCOCO**: Builds on established referring expression datasets
      - **Instruction Diversity**: 12 editing types × diverse spatial/attribute variations
  - **Benchmark**: **RefEdit-Bench**
      - **Foundation**: RefCOCO test images with expert-annotated editing tasks
      - **Focus**: Evaluates precision of referring expression understanding in editing
      - **Metrics**: Object localization accuracy + edit quality (CLIP-Sim, FID, human eval)
  - **Model**: **RefEdit Model**
      - **Architecture**: Diffusion-based editing model conditioned on referring expressions
      - **Training**: Fine-tuned on 20K synthetic data
  - **Experimental Results**:
      - **RefEdit-Bench**: Outperforms MagicBrush, InstructPix2Pix despite **50× less training data**
      - **Referring Precision**: **91.2% object localization accuracy** vs. **67.3%** for instruction-only baselines
      - **Few-Shot Superiority**: Demonstrates data quality > quantity paradigm
  - **Publication**: arXiv June 2025 (v1: June 2025)
  - **Institution**: Arizona State University
  - **Open Source**: ✅ RefEdit-Bench, Model, 20K Training Data - Details in paper
  - **Cross-Reference**: See also [Notable Multimodal Datasets](#-notable-multimodal-datasets)
  

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

### 🧩 Compositionality / Preference-Guided Synthesis

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
<img src="https://img.shields.io/badge/Institution-November_2024-red?style=flat-square"/>
</summary>

  - **Focus**: **Improving CLIP's Compositional Reasoning via Synthetic Vision-Language Hard Negatives**
  - **Data Synthesis Method** - **LLM-Guided Hard Negative Caption Generation + T2I Model Corresponding Image Synthesis**:
      - **Core Innovation**: Generate semantically similar but compositionally different hard negative image-text pairs, train CLIP using triplet contrastive learning
      - **Two-Stage Pipeline**:
        1. **LLM-Generated Hard Negative Captions**:
           - Use **Mistral-7B-Instruct-v0.2** with in-context learning to generate high-quality hard negative captions
           - **Prompting Strategy**: Requires generation of "mostly similar descriptions with sufficient significant differences so two descriptions cannot possibly be for the same image"
           - **Variation Types**:
             - **Object Replacement**: "dog looking from window" → "cat observing from window"
             - **Spatial Relations**: "dog to the left of cat" → "cat to the left of dog"
             - **Attribute Changes**: "red car" → "blue car"
             - **Action Variations**: "person running" → "person walking"
           - **Quality Control**: Single high-quality negative caption outperforms multiple low-quality negatives
        2. **T2I Model Generated Corresponding Negative Images**:
           - Use **SDXL-Turbo** for rapid negative image generation (corresponding to negative captions)
           - **Efficiency**: 3 days on 8×RTX A6000 to generate 13M negative captions
           - **LLM Selection**: Mistral-7B-Instruct-v0.2 performs best with easily parseable output
           - **Quality Assessment**: ViLT model validates generated images achieve 76% average accuracy following text prompts
      - **TripletCLIP Training Strategy**:
        - **Triplet Contrastive Loss**: L_TCL = L_NegCLIP(X,Y,Y') + L_NegCLIP(X',Y',Y)
        - **Alternating Supervision**: Train using both (X,Y,Y') and (X',Y',Y) triplets alternately
        - **Hard Negative Regularization**: Negative images regularize negative caption effects and stabilize pre-training
  - **Data Scale**:
      - **TripletData Dataset**: 13M image-text hard negative pairs
      - **Base Data**: Built upon CC3M (2.6M) and CC12M (12M) datasets
      - **Data Type**: Each positive sample paired with one carefully constructed negative sample
  - **Training Strategy**:
      - **Fair Computational Budget**: Maintains same training compute as baseline methods
      - **Modality-Specific Ablations**: Separately validate contributions of hard negative captions and images
      - **Concept Coverage Analysis**: Evaluate performance across different concept diversity levels
  - **Experimental Results**:
      - **Compositional Understanding Benchmarks**:
        - **SugarCrepe**: +9.4% (CC3M) and +10.9% (CC12M) over LaCLIP
        - **SugarCrepe**: +6.3% (CC3M) and +6.5% (CC12M) over NegCLIP
        - **All Sub-categories**: Comprehensive improvements across object/attribute replace, swap, add tasks
      - **Zero-Shot Tasks**:
        - **Image-Text Retrieval**: Significant R@5 improvements (CC3M: +11.1%, CC12M: +16.1%)
        - **ImageNet Classification**: Top-1 accuracy gains (CC3M: +3.5%, CC12M: +7.0%)
        - **VTAB Benchmark**: Maintains competitiveness on visual task adaptation
      - **Ablation Study Findings**:
        - **Negative Captions Alone**: +7.6% over LaCLIP on SugarCrepe
        - **Negative Images Alone**: +2.2% over LaCLIP on SugarCrepe
        - **Combined**: Achieves best performance +9.4%
  - **Key Findings**:
      - **Dual-Modal Hard Negatives Effect**: Negative captions + negative images more effective than either alone
      - **Data Efficiency**: Using half positive + half negative samples outperforms full positive baseline
      - **LLM Generation Quality**: LLM-generated negative captions significantly superior to rule-based replacement
      - **Concept Coverage Independence**: Maintains performance advantages even at lower concept coverage levels
  - **Publication**: arXiv November 2024 | Arizona State University & University of Maryland, Baltimore County
  - **Open Source**: ✅ Code, Models, TripletData Dataset - [tripletclip.github.io](https://tripletclip.github.io)
  - **Significance**:
      - **CLIP Compositional Understanding Breakthrough**: First method to simultaneously leverage hard negative images and text for CLIP training
      - **Scalability**: Provides general triplet contrastive learning framework applicable to other VLMs
      - **Practicality**: Achieves significant performance gains under equal computational budget with favorable efficiency-effectiveness trade-off
  

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

  - **Focus**: **Enhancing VLM compositional understanding through multimodal synthetic data with subtle variations**
  - **Data Synthesis Method** - **Real Image Feature Injection into Fast T2I Model + Adaptive Margin Loss**:
      - **Core Innovation**: Generates positive/negative caption pairs with **visually grounded images** to train VLMs on fine-grained compositional distinctions
      - **3-Stage Pipeline**:
        1. **Caption Pair Generation (LLM-based)**:
           - Use **LLM** (e.g., GPT-4) to generate positive/negative caption pairs with subtle compositional variations
           - **Positive Caption**: Accurately describes image content
           - **Negative Caption**: Introduces compositional errors while maintaining semantic similarity
           - **Variation Types**:
             - **Attribute Binding**: "red apple and green banana" → "green apple and red banana"
             - **Object Counting**: "three dogs" → "two dogs"
             - **Spatial Relationships**: "cat on the left of dog" → "dog on the left of cat"
             - **Action Attribution**: "woman holding umbrella" → "man holding umbrella"
        2. **Image Synthesis with Real Feature Injection**:
           - **Challenge**: Pure text-to-image models struggle with precise compositional control
           - **Solution**: Inject **real image features** into fast T2I model (e.g., SDXL-Turbo)
           - **Method**:
             - Extract features from **real reference images** (e.g., COCO, Visual Genome)
             - **Feature Injection**: Condition T2I generation on both text caption + real image features
             - Ensures generated images faithfully reflect compositional details in captions
           - **Speed**: SDXL-Turbo enables rapid generation (4-8 steps vs. 50+ for standard diffusion)
        3. **Style Transfer for Domain Alignment**:
           - Apply **style transfer** to synthetic images to match distribution of real images
           - Reduces domain gap between synthetic training data and real-world test images
           - Uses neural style transfer or lightweight style adapters
      - **Adaptive Margin Loss**:
        - **Problem**: Fixed margin in contrastive learning treats all negative samples equally
        - **Solution**: **Adaptive margin** based on caption similarity
        - **Formula**: Margin inversely proportional to text similarity between positive/negative captions
        - **Effect**: Harder negatives (more similar captions) get smaller margins → model learns finer distinctions
  - **Data Scale**:
      - **SPARCL Dataset**: Large-scale synthetic compositional data (exact scale not specified, likely 100K-1M pairs)
      - **Caption Pairs**: Each image associated with positive caption + multiple negative variants
      - **Compositional Categories**: Covers 4+ major compositional reasoning types
  - **Training Strategy**:
      - **Efficient Fine-Tuning**: Use **LoRA adapters** for parameter-efficient training
      - **Contrastive Learning**: Train VLM to distinguish positive vs. negative caption-image pairs
      - **Adaptive Margin**: Dynamically adjust margin based on caption similarity
  - **Experimental Results**:
      - **Compositional Benchmarks**: Significant improvements on Winoground, ARO, CREPE, SugarCrepe
        - **Winoground**: +12.3% over CLIP baseline
        - **ARO (attribute binding)**: +8.7%
        - **SugarCrepe (hard negatives)**: +10.1%
      - **Generalization**: Maintains strong performance on standard VQA tasks (no degradation)
      - **Data Efficiency**: Achieves gains with moderate synthetic data (no need for billion-scale datasets)
  - **Key Findings**:
      - **Real Feature Injection Critical**: Pure T2I generation fails on fine-grained compositional control
      - **Adaptive Margin Effectiveness**: Outperforms fixed-margin contrastive learning by **+4.2%**
      - **Synthetic Data Sufficiency**: Targeted synthetic data more effective than scaling up real data
  - **Publication**: CVPR 2025 | arXiv March 2025 (v2: March 2025)
  - **Institution**: Not explicitly stated (academic research)
  - **Open Source**: ✅ Code, Synthetic Data, LoRA Adapters - Release details in paper
  - **Significance**:
      - **Addresses VLM Weakness**: Targets known compositional understanding limitations
      - **Efficient Synthesis**: Fast T2I + LoRA enables scalable, cost-effective data generation
      - **Methodological Innovation**: Real feature injection + adaptive margin provide blueprint for compositional data synthesis
  

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

  - **Focus**: **Generative Data Pipeline for Generative Multi-Concept Composition** - Semi-automated dataset creation pipeline Gen4Gen for multi-concept personalization using cascaded AI foundation models
  - **Data Synthesis Method** - **Semi-Automated Multi-Stage Composition Pipeline**:
      - **Core Innovation**: Leverages recent advancements in image foreground extraction, LLMs, MLLMs, and inpainting to compose personalized concepts into realistic scenes with densely corresponding text descriptions
      - **Three Design Principles**:
        1. **Detailed Text-Image Pairing**: Text must be well-aligned with corresponding image, providing information for both foreground and background objects
        2. **Reasonable Object Layout and Background Generation**: Objects only co-exist when possible in real-life, and their positions in image make sense
        3. **High Resolution**: Ensures dataset caters to end goal of generating high-quality, multi-concept personalized images
      - **Gen4Gen Pipeline** (three main stages):
        1. **Object Association and Foreground Segmentation**:
           - **Input**: Set of k objects O = {o_i}^k, where each object o_i is represented by set of n images X_oi = {x_j}^n
           - **Source Data**: DreamBooth, Custom Diffusion, online copyright-free sources
           - **Object Combination Selection**: Find subset of object combinations O' = {o_a, o_b, ...} that are intuitively likely to co-exist (e.g., dog, cat, houseplant)
           - **Foreground Segmentation**: Apply DIS (category-agnostic saliency object detector) to segment foreground given objects within composition O'
           - **Output**: Segmented foreground images D(X') and corresponding masks M(D(X'))
        2. **LLM-Guided Object Composition**:
           - **Bounding Box Generation**: Exploit LLM's zero-shot capability, inquire ChatGPT to provide probable set of bounding boxes given object combinations O'
           - **Template-Based**: Show few samples to ChatGPT explaining task of providing bounding box points given object bounding boxes in COCO dataset
           - **Scale Enhancement**: Utilize GPT-4 for logical enhancements, request scales for each bounding box to be realistic (solves scaling problem where some objects are unrealistically bigger)
           - **Composition**: Place individual images within D(X') following bounding box location and given size to obtain foreground image I_fg and mask M(I_fg)
           - **Background Prompt Generation**: Obtain set of prompts P describing possible scenes I_fg may be placed in by verifying validity against same LLM model
        3. **Background Repainting and Image Recaptioning**:
           - **Background Retrieval**: Find starting background image I_bg from copyright-free sources (Unsplash) with prompt p ∈ P
           - **Inpainting**: Use text-to-image diffusion inpainting model f (Stable-Diffusion-XL) to repaint I_fg by embedding it within background image I_bg
           - **Mask Smoothing**: Utilize smoothed soft mask (average smoothing on M(I_fg) with 5×5 window) to enhance integration of foreground object into background
           - **Output**: Final image I_O' = f(I_fg, M(I_fg), I_bg)
           - **Recaptioning**: Inquire MLLM (LLaVA-1.5) to provide detailed caption describing I_O' to subset of all combinations (word limit: 30, constrained by CLIP's context constraints of 77 tokens max)
      - **Training-Time Prompt Engineering Strategies**:
        - **Global Composition Token**: Adapt DreamBooth concept to complex compositions, introduce global token alongside individual tokens for each object to enhance capabilities in describing detailed scene arrangements
        - **Repeat Concept Token Prompts During Training**: Employ strategy of repeating concept token prompts during training to encourage model to ensure presence of each specified concept in generated images
        - **Incorporating Background Prompts**: Make sure background is stated within training prompt to disentangle background and concept compositions
      - **Key Techniques**:
        - **DIS Segmentation**: Category-free saliency object detector, agnostic to set of objects being used
        - **LLM-Guided Composition**: Leverages LLM's zero-shot capability for realistic object layout
        - **Scale Enhancement**: GPT-4 logical enhancements ensure realistic object proportions
        - **Diffusion Inpainting**: Stable-Diffusion-XL for high-quality background integration
        - **MLLM Recaptioning**: LLaVA-1.5 for detailed caption generation maintaining alignment
      - **MyCanvas Dataset**:
        - **Scale**: 150 objects (some with single image, others with multiple), 41 probable compositions, over 10K images filtered manually down to **2,684 images** of best quality
        - **Caption Statistics**: Average word length 17.7, approximately 30% of lengths extending beyond 20 words
        - **Object Diversity**: Wide range of objects, surpassing both CustomConcept101 and DreamBooth datasets
        - **Recaptioning Coverage**: Applied to 10 object combinations O' within MyCanvas dataset
      - **Comprehensive Evaluation Metrics**:
        - **CP-CLIP (Composition-Personalization-CLIP)**: Assesses accuracy of composition and personalization
          - **Composition Accuracy**: Is each personalized concept mentioned in text reflected during image generation?
          - **Fidelity**: Does generated personalized concepts look similar to their source counterparts?
        - **TI-CLIP (Text-Image Alignment CLIP)**: Serves as indicator of potential overfitting by evaluating model's generalization quality across various textual backgrounds
      - **Experimental Results**:
        - **Multi-Concept Personalization**: Previous methods (Custom Diffusion) with enhanced dataset (MyCanvas) and prompting strategy can gain significant improvements in generating realistic multi-concept images with varying backgrounds while sticking to identity of personalized concepts
        - **Improvements**: More apparent under very complex compositions, challenging guidance (relative positions), and multiple semantically similar concepts (e.g., two dog identities in same image)
        - **Baseline**: Simple baseline built on top of Custom Diffusion with empirical prompting strategies for future researchers to evaluate on MyCanvas
      - **Publication**: CVPR 2024 | arXiv February 2024
  - **Institution**: UC Berkeley, University of Oxford, Harvard University, CMU, HKU, UC Davis
  - **Open Source**: ✅ [Project](https://danielchyeh.github.io/Gen4Gen/) | [GitHub](https://github.com/danielchyeh/Gen4Gen) - Code, MyCanvas Dataset (2,684 images), Benchmark Metrics
  - **Significance**:
      - **Integrating AI Foundation Models**: Semi-automated dataset creation pipeline introduces possibilities of using cascaded AI-foundation models for generating high-quality datasets
      - **Dataset Quality Matters**: Proof-of-concept MyCanvas dataset reflects that simply composing well-aligned image and text description pairs would significantly improve task of multi-concept personalization
      - **Benchmark for Multi-Concept Personalization**: Holistic evaluation benchmark considers personalization accuracy, composition correctness, and text-image alignment in task of multi-concept personalization
      - **Chaining Foundation Models**: Demonstrates chaining strong foundation models could be promising direction for generating high-quality datasets targeting variety of challenging tasks
  

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

  - **Focus**: **Generating Multi-Image Synthetic Data for Text-to-Image Customization** - Simple approach to address challenges in text-to-image customization by creating Synthetic Customization Dataset (SynCD) consisting of multiple images of same object under different lighting, poses, and backgrounds
  - **Data Synthesis Method** - **Masked Shared Attention + 3D Consistency + Dataset Filtering**:
      - **Core Innovation**: Leverages existing text-to-image models and 3D assets to create high-quality synthetic dataset of multiple images of same object in different contexts, maintaining object identity while generating multiple images with varying contexts
      - **SynCD Dataset Generation Pipeline** (three main steps):
        1. **LLM-Assisted Prompt Generation**:
           - **Object Description**: Design each prompt to have detailed description of both object and background
           - **Rigid Objects**: Use Cap3D descriptions for Objaverse assets (e.g., "a large metal drum with blue and pink stripes")
           - **Deformable Objects**: Instruct LLM to generate descriptive captions (e.g., "The Russian blue cat has a thick, plush coat in a steel blue color, with green eyes")
           - **Background Prompt Generation**: Instruct LLM (Instruction-tuned Llama3) to generate plausible background scene descriptions based on object description
           - **Combination**: Combine one object description with multiple background descriptions and input to image generation step
        2. **Multi-Image Consistent-Object Generation**:
           - **Base Model**: Use DiT-based FLUX model to generate images with consistent object
           - **Masked Shared Attention (MSA) Mechanism**:
             - **Method**: Modify attention block of diffusion model such that each image attends to itself as well as foreground object regions of other images
             - **Formula**: MSA({q_i, k_i, v_i}^N) ≡ Softmax(q_i [k_1 ... k_N]^T / √d' + M_i) [v_1 ... v_N]
             - **Mask M_i**: Initialized so that text tokens of one image do not attend to other image tokens, and i-th image feature only attends to object region of other images, ignoring their background
             - **Effect**: Enables generation of objects with similar visual features among all images
           - **Rigid Object Generation with 3D Consistency**:
             - **Depth Guidance**: For rigid objects with available 3D datasets (Objaverse), render asset from N varying camera poses and feed rendered depth map and captions to depth-conditioned FLUX model
             - **Depth Guidance**: Ensures 3D shape consistency of object across images
             - **Feature Warping**: For representative example of generating two images with same object, given latent features f_i ∈ R^(h×w)×d, i ∈ {1,2}, warping is calculated as:
               - f̂_2(u,v) = α f_1(u+Δu, v+Δv) + (1-α) f_2(u,v)
               - Where (u+Δu, v+Δv) denotes corresponding location in first image, α is binary scalar denoting if that location is visible in first image
             - **Application**: Apply warping for all pairs with appropriate masks and only during early diffusion timesteps
             - **Effect**: Increases multi-view consistency without introducing warping artifacts and allows flexibility for lighting variations
        3. **Dataset Filtering**:
           - **Aesthetic Score Filtering**: Reject images with aesthetic score below 6
           - **Object Identity Similarity**: Use DINOv2 to measure object identity similarity, remove images with average pairwise feature similarity below 0.7 within their set
           - **Final Dataset**: Contains ~95,000 objects with 2-3 images per object, uniformly distributed among rigid and deformable categories
      - **Encoder-Based Model Training**:
        - **Architecture**: Fine-tune existing text-to-image diffusion or flow-based model using SynCD dataset
        - **Training Setup**: Given N images of object, consider one as target and rest as references
        - **Shared Attention Mechanism**: For conditioning generation on real reference images, employ Shared Attention similar to dataset generation pipeline
          - Concatenate reference image features with target image features along sequence dimension in each attention block
          - Query features of target image are subsequently updated by attending to both itself and reference images' features
        - **Training Objective**: Adopt velocity or flow prediction objective for diffusion and flow-based models respectively
      - **Inference Method**:
        - **Normalized Guidance Vectors**: Directly combining text and image guidance using previous work often leads to over-exposure issues in generated image, especially at high image guidance
        - **Proposed Solution**: Normalize image and text guidance vectors
          - Formula: ε_θ(x_t, {x_i}^K, ∅) + λ_I ||g||/||g_I|| · g_I + λ_c ||g||/||g_c|| · g_c
          - Where g_I = ε_θ(x_t, {x_i}^K, ∅) - ε_θ(x_t, ∅, ∅), g_c = ε_θ(x_t, {x_i}^K, c) - ε_θ(x_t, {x_i}^K, ∅), ||g|| = min(||g_I||, ||g_c||)
        - **Effect**: Helps achieve better image alignment with reference object while still following text prompt
        - **Flexibility**: Number of reference images can vary from training since attention-based conditioning is agnostic to sequence length
      - **Key Techniques**:
        - **Masked Shared Attention**: Enables consistent object generation across multiple images
        - **3D Consistency for Rigid Objects**: Depth guidance and feature warping ensure multi-view consistency
        - **Shared Attention in Training**: Allows model to learn from multiple reference images
        - **Normalized Guidance Inference**: Mitigates over-exposure issues while maintaining text and image alignment
      - **Data Scale**:
        - **SynCD Dataset**: ~95,000 objects with 2-3 images per object
          - **Rigid Objects**: 75,000 rigid category assets from Objaverse
          - **Deformable Objects**: 16 deformable super-categories of animals with approximately 100 different subspecies
        - **Uniform Distribution**: Uniformly distributed among rigid and deformable categories
      - **Experimental Results**:
        - **Quantitative Comparison** (3 input reference images):
          - **Ours(1B)**: MDINOv2-I 0.806, CLIPScore 0.773, TIFA 0.303, GeometricScore 0.801
          - **Ours(3B)**: MDINOv2-I 0.822, CLIPScore 0.789, TIFA 0.313, GeometricScore 0.838
          - **Ours(12B)**: MDINOv2-I 0.778, CLIPScore 0.771, TIFA 0.306, GeometricScore 0.780
          - All variants perform better or on par with other baselines on overall GeometricScore metric
        - **Human Evaluation**:
          - **Ours(1B) vs JeDi**: 69.51% text alignment, 63.05% image alignment, 80.89% photorealism, 68.19% overall preference
          - **Ours(3B) vs Emu-2**: 70.49% text alignment, 66.88% image alignment, 64.66% photorealism, 66.74% overall preference
          - **Ours(12B) vs OminiControl**: 56.27% text alignment, 58.30% image alignment, 54.47% photorealism, 58.02% overall preference
        - **Ablation Studies**:
          - **SynCD Dataset Contribution**: Simply fine-tuning with SynCD dataset already improves performance
          - **Shared Attention Effectiveness**: Adding reference condition via shared attention further boosts performance
          - **Multiple Reference Images**: Allows use of multiple reference images during inference, improving performance as number of reference images increases to three
          - **Normalized Guidance**: Outperforms guidance rescale in mitigating over-exposure issues
      - **Model Variants**:
        - **Ours(12B)**: Fine-tuned FLUX model, only fine-tune attention layers with LoRA
        - **Ours(1B/3B)**: Latent Diffusion Models initialized with IP-Adapter, fine-tune LoRA layers in self-attention block and key-value projection matrices in image cross-attention layers
      - **Publication**: CVPR 2025 | arXiv February 2025
  - **Institution**: Carnegie Mellon University, Meta
  - **Open Source**: ✅ Code and data available at project website
  - **Significance**:
      - **Addresses Data Shortage**: Creating such dataset through internal feature sharing and external 3D guidance is far more scalable than collecting real-world data of multiple images with same object
      - **Cost-Effective Customization**: Generates consistent object identities using internal feature sharing and external 3D guidance, more tractable than task of model customization with real images
      - **Multi-Image Supervision**: Training encoder-based models on multi-image datasets with shared attention improves customization quality
      - **Inference Innovation**: Normalized guidance vectors help achieve better image alignment while following text prompt
  

</details>
---

### 🧪 Interleaved Image-Text · Coherence & Consistency

This category focuses on **high-quality interleaved image-text data construction** with emphasis on **coherence (logical flow), consistency (factual accuracy), and alignment (image-text relevance)**. Unlike simple image-text pairs, these methods curate or synthesize multi-image documents with narrative coherence, making them suitable for training models on long-context multimodal understanding and generation.

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2506.09427">📄 InterSyn</a></b><br>
<code>arXiv 2506.09427</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Interleaved Image-Text Generation Dataset & Evaluation** - First fully automatic, large-scale, multi-turn instruction-following interleaved image-text QA dataset with dedicated evaluation model SynJudge
  - **Data Synthesis Method** - **SEIR (Self-Evaluation with Iterative Refinement)**:
      - **Core Innovation**: Three-stage iterative refinement pipeline embedding self-checking and feedback loops, ensuring semantic completeness, cross-modal synergy, and contextual relevance
      - **Preparation Phase** (5 steps):
        1. **Question Collection**: 25 participants each contribute 40 questions from natural conversation scenarios (1000 total)
        2. **Question Screening & Benchmarking**: LLM + expert review, curate 500 high-quality questions for benchmark
        3. **Question Template Extraction**: Extract generalized templates from high-quality questions
        4. **Base Topic Hierarchy**: AI-assisted topic extraction + human organization, build logically clear topic hierarchy
        5. **Topic Hierarchy Expansion**: AI suggestions + expert curation, expand to 8 domains, 65 categories, 3500 fine-grained topics
      - **SEIR Three-Stage Refinement** (executed per dialogue turn, K=3 iterations):
        - **Stage 1: Question Refinement (QR)**:
          - Initialization: Generate initial question q₀ from template τ and topic z
          - Iterative refinement: LLM generates refinement suggestions → optimize question based on suggestions
          - Effect: Quality improves **32%** after 3 iterations
        - **Stage 2: Answer Refinement (AR)**:
          - Initialization: Generate initial answer a₀ and temporary caption γ₀
          - Iterative refinement: LLM evaluates answer and caption → generates suggestions → optimization
          - Effect: TCC **+15%**, ICC **+11%**, ITS **+19%**
        - **Stage 3: Image Refinement (IR)**:
          - Generate initial image using temporary caption → VLM evaluation → optimize caption → regenerate image
          - Effect: Further improves ICC and ITS
      - **Key Techniques**:
        - **Markov Property**: Each iteration depends only on previous state
        - **Cross-Turn Coherence**: Maintains topic consistency via history context H
        - **Multi-Model Ensemble**: Qwen/InternLM/GPT + QwenVL/InternVL/LLaVA + FLUX
  - **SynJudge Evaluation Model**:
      - **Training Data**: 38,400 human-annotated samples
      - **Base Model**: QwenVL2.5 / InternVL2.5
      - **Four-Dimensional Evaluation**:
        1. **TCC (Text Content Completeness)**: Text content completeness
        2. **ICC (Image Content Completeness)**: Image content completeness
        3. **IQ (Image Quality)**: Image quality
        4. **ITS (Image-Text Synergy)**: Image-text synergy (rewards complementary alignment, penalizes redundancy)
      - **vs. Human Evaluation**: RMSE only 5% deviation (vs. 13% for other models)
  - **Data Scale**:
      - **InterSyn**: 1.8M single-turn samples + 50K multi-turn dialogues
      - **Benchmark**: 500 high-quality questions
      - **Topic Coverage**: 8 domains, 65 categories, 3500 fine-grained topics
  - **Experimental Results** - **Model Fine-tuning Significantly Improves**:
      - **Anole Fine-tuning** (50K InterSyn): TCC +14%, ICC +7.6%, IQ +6.2%, ITS **+30%**
      - **VILA-U Fine-tuning**: TCC **+29.7%**, ITS **+52.1%**
      - **vs. Existing Models**: InterSyn-generated samples surpass GPT-4o+DALL-E3 across all dimensions (+0.34~0.66)
  - **Open Source**: ✅ [GitHub](https://github.com/xxx/InterSyn) (specific link TBD)
  - **Institution**: Nankai University + Shanghai Innovation Institute + Wuhan University + USTC + Shanghai AI Lab
  - **Publication**: arXiv June 2025
  - **Significance**:
      - **First Large-Scale Interleaved Image-Text Instruction Data**: Fills instruction-following interleaved data gap
      - **Fully Automatic Pipeline**: SEIR significantly reduces human labor cost
      - **Four-Dimensional Evaluation System**: SynJudge provides fine-grained, interpretable evaluation
      - **Cross-Modal Synergy**: Emphasizes ITS metric, surpasses traditional consistency evaluation
  

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

  - **Focus**: **Coherent interleaved image-text dataset** with multi-perspective quality filtering and novel evaluation tasks
  - **Data Curation Method** - **Multi-Perspective Filter Strategy + Quality Assessment Framework**:
      - **Core Innovation**: Not pure synthesis, but **systematic curation and quality enhancement** of web-scraped interleaved data using **multi-model filtering** across three dimensions
      - **3-Perspective Filtering Pipeline**:
        1. **Text Sequence Filtering (Coherence)**:
           - **Goal**: Ensure logical flow and narrative coherence in text sequences
           - **Method**:
             - Use **LLM-based coherence scoring** (e.g., GPT-3.5/4) to evaluate text readability and logical progression
             - Detect and remove documents with:
               - Abrupt topic shifts
               - Disconnected sentences
               - Poor grammatical structure
           - **Thresholds**: Calibrated coherence score ≥ 0.75 (on 0-1 scale)
        2. **Image Sequence Filtering (Consistency)**:
           - **Goal**: Maintain visual consistency and relevance across image sequences in same document
           - **Method**:
             - **CLIP-based image similarity**: Measure visual coherence between consecutive images
             - **Object/Scene Consistency**: Use detection models (YOLO, DINO) to verify consistent entities across images
             - **Aesthetic Quality**: Filter low-quality, blurry, or heavily watermarked images
           - **Criteria**: Remove sequences with:
             - Extremely low inter-image similarity (< 0.3 CLIP score)
             - Drastic style/domain shifts within single document
             - Majority of images failing quality checks
        3. **Image-Text Alignment Filtering (Relevance)**:
           - **Goal**: Ensure tight alignment between images and surrounding text
           - **Method**:
             - **Cross-Modal Retrieval Verification**: For each image, verify it ranks highly when retrieving against surrounding text paragraphs
             - **CLIP-based Image-Text Matching**: Compute alignment scores between images and adjacent text
             - **Captioning Consistency Check**: Generate captions for images using VLM (e.g., BLIP-2), verify semantic match with document text
           - **Filtering**: Remove image-text pairs with alignment score < 0.5
      - **Multi-Model Consensus**:
        - Combine scores from multiple models (CLIP, BLIP-2, GPT-4, custom classifiers)
        - Require agreement across models to avoid single-model biases
        - **Ensemble Strategy**: Weighted averaging with calibrated thresholds
      - **Source Data**:
        - **Web Crawling**: CommonCrawl, Wikipedia, educational websites
        - **Initial Scale**: ~2M raw documents before filtering
        - **Post-Filtering Scale**: 227K high-quality coherent documents
  - **Data Scale**:
      - **CoMM Dataset**: 227K documents, 2.28M images, 139M text tokens
      - **Average Document Length**: ~611 tokens, ~10 images per document
      - **Domains**: News articles, tutorials, educational content, story narratives
  - **Novel Evaluation Tasks (4 Tasks Proposed)**:
      1. **Coherent Image Generation**: Generate coherent image sequences given text outline
      2. **Coherent Text Generation**: Generate narrative text given image sequence
      3. **Coherence Evaluation**: Assess coherence quality of interleaved documents
      4. **Cross-Modal Retrieval in Long Context**: Retrieve relevant images/text in multi-image documents
  - **Benchmark Construction**:
      - **Test Set**: 5K high-quality held-out documents
      - **Human Annotations**: Expert ratings on coherence, consistency, alignment (3-point scale)
      - **Automatic Metrics**: CLIP-based, LLM-based, and custom coherence metrics
  - **Experimental Results**:
      - **Pre-training with CoMM**: Models trained on CoMM show **+8.3%** improvement on interleaved understanding tasks vs. models trained on non-filtered data
      - **Coherence Metrics**: CoMM-filtered data scores **0.82 coherence** vs. **0.61** for raw web data
      - **Alignment Quality**: **87.5%** image-text alignment accuracy vs. **62.3%** for unfiltered data
      - **Generalization**: Strong transfer to downstream tasks (long-form VQA, multi-image reasoning)
  - **Ablation Studies**:
      - **Each Filter Contribution**:
        - Text filtering: +3.1% coherence
        - Image filtering: +2.7% consistency
        - Alignment filtering: +4.2% relevance
      - **Multi-Model Consensus**: Outperforms single-model filtering by **+5.8%**
  - **Publication**: CVPR 2025 | arXiv June 2024 (v3: June 2024)
  - **Institution**: Not explicitly stated (academic research)
  - **Open Source**: ✅ CoMM Dataset (227K documents), Evaluation Benchmark (5K test set), Filtering Code, Evaluation Metrics - Release details in paper
  - **Cross-Reference**: See also [Notable Multimodal Datasets](#-notable-multimodal-datasets) for dataset details
  - **Significance**:
      - **Quality Over Quantity**: Demonstrates rigorous filtering > raw scale for interleaved data
      - **Multi-Dimensional Quality**: First to systematically address coherence, consistency, AND alignment simultaneously
      - **Methodological Contribution**: Multi-perspective filtering framework applicable to other web-scale curation tasks
      - **Benchmark Innovation**: Proposes new tasks specifically for evaluating interleaved data quality
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2501.03675">📄 SMIR</a></b><br>
<code>arXiv 2501.03675</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Efficient Synthetic Data Pipeline for Multi-Image Reasoning** - Synthetic data generation pipeline for multi-image reasoning with high-quality dataset and evaluation benchmark
  - **Data Synthesis Method** - **Multimodal Embedding + Random Sampling with Iteration**:
      - **Core Innovation**: Efficiently identifies correlated images using multimodal embeddings, applying cluster sampling and graph iteration sampling to ensure diversity and robustness in instruction tuning
      - **Stage 1: Multimodal Embedding Construction**:
        - **Method**: Combines SigLIP or CLIP image embeddings with corresponding caption embeddings
        - **Formula**: E_multimodal = E_image + c·E_caption (where c = 0.2 for ShareGPT4V dataset)
        - **Purpose**: Captures both visual and textual relationships for better identification and clustering of correlated images
        - **Dimensionality Reduction**: Applies UMAP for dimensionality reduction, preserving essential data structures
      - **Stage 2: Random Sampling with Iteration**:
        - **Algorithm**: Iteratively selects semantically related images using probability distribution based on cumulative distance
        - **Probability Distribution**: p(x_j) ∝ 1/(Σ∥x_j - x_u∥^k + ε), where k (default: 12) controls proximity emphasis
        - **Purpose**: Balances semantic coherence and diversity, allowing meaningful multi-image relationships while introducing randomness
        - **Advantage**: Effectively clusters related images while avoiding disconnected groupings
      - **Stage 3: Synthetic Data Generation**:
        - **LLM**: Uses Meta Llama 3.1 70B Instruct Turbo (open-source LLM)
        - **Cost Efficiency**: Up to **50× cheaper** and **10× faster** than GPT-4
        - **Two Types of System Prompts**:
          1. **LLaVA-style Prompt**: Focuses on shorter visual questions, often requiring OCR-based understanding
          2. **Long-form Reasoning Prompt**: Designed for multi-step inference and deeper contextual understanding
        - **Data Source**: ShareGPT4V (1.2M image-caption pairs)
        - **Batch Processing**: Each batch consists of 20,000 images and generates 5,000 synthetic conversations
      - **Key Techniques**:
        - **Multimodal Embedding**: Integrates visual and descriptive information for better correlation identification
        - **Iterative Sampling**: Ensures diversity while preserving coherence
        - **Open-Source LLM**: Reduces costs significantly compared to closed-source alternatives
        - **Modular Design**: Easy adaptation to new datasets and applications
  - **SMIR-BENCH Evaluation Benchmark**:
      - **Scale**: 200 diverse examples across seven complex reasoning tasks
      - **Task Categories**:
        1. **Bird**: Identifying species and reasoning over distinguishing features
        2. **Matching**: Pairing photos based on visual similarities
        3. **OCR**: Reading and reasoning about academic texts
        4. **Pattern**: Recognizing visual patterns in structured tasks
        5. **Ranking**: Ordering objects based on contextual preferences
        6. **Storytelling**: Narrating events from image sequences
        7. **Visual**: Establishing meaningful connections between images
      - **Evaluation Methodology**:
        - **Multi-turn**: Supports multi-turn interactions
        - **Free-form Responses**: Assesses models via free-form responses and reasoning justifications
        - **Judge Model**: Uses GPT-4o as judge for pairwise comparisons
        - **Framework**: Extends Auto-Hard-Auto v0.1 framework to multimodal evaluation
  - **Data Scale**:
      - **SMIR Dataset**: 160,000 synthetic training samples
      - **Source Images**: 640,000 image-caption pairs used to produce 160,000 synthetic conversations
      - **Average Statistics**:
        - Maximum turns: 24, Minimum turns: 2, Average turns: 9.65
        - Average images per conversation: 4.65
        - Average user tokens: 25.51, Average assistant tokens: 124.32
  - **Experimental Results**:
      - **Model Fine-tuning**: Models fine-tuned on SMIR achieve up to **8% improvement** over base versions on SMIR-BENCH
      - **SMIR-8B-SIGLIP-LLAMA3**: 58.1 score (+8.1% vs Mantis-8B-siglip-llama3 baseline)
      - **SMIR-8B-IDEFICS2**: 58.0 score (+8.0% vs Mantis-8B-Idefics2 baseline)
      - **vs. Closed-Source Models**: SMIR-trained models significantly outperform MANTIS-tuned counterparts despite smaller dataset size
  - **Publication**: arXiv January 2025
  - **Institution**: TogetherAI, UC Berkeley, Stanford University, Caltech
  - **Open Source**: ✅ [GitHub](https://github.com/togethercomputer/SMiR) - Code, SMIR Dataset (160K samples), SMIR-BENCH (200 examples)
  - **Significance**:
      - **Addresses Multi-Image Reasoning Gap**: Targets known weakness in open-source VLMs for multi-image tasks
      - **Cost-Effective Synthesis**: Open-source LLM reduces costs by 50× and increases speed by 10×
      - **Correlated Image Focus**: Ensures image correlation, advancing complex multi-image reasoning
      - **Comprehensive Benchmark**: SMIR-BENCH provides rigorous evaluation with multi-turn, free-form responses
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2501.00958">📄 2.5 Years in Class</a></b><br>
<code>arXiv 2501.00958</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-Zhejiang_University_+_Alibaba_DAMO_Academy-red?style=flat-square"/>
</summary>

  - **Focus**: **Instructional Video-to-Multimodal Textbook** - Constructing high-quality interleaved image-text "textbook" corpus from online instructional videos to improve VLM pretraining
  - **Data Synthesis Method** - **Video-to-Textbook Multi-Level Pipeline**:
      - **Core Innovation**: First systematic method to construct interleaved image-text datasets from instructional videos through multi-level extraction (Video→ASR→Keyframes→OCR) generating textbook-quality data
      - **Problem Identification**:
        - Existing interleaved datasets (MMC4, OBELICS) crawled from webpages suffer from **low knowledge density, loose image-text relations, poor logical coherence between images**
        - Online instructional videos (e.g., geometry courses) contain rich foundational knowledge but remain underexplored in VLM training
      - **Three-Stage Data Construction Pipeline**:
        1. **Instructional Video Collection**:
           - **Knowledge Taxonomy Construction**: Use GPT-4o to build taxonomy with 3,915 knowledge points covering 6 subjects (Math, Physics, Chemistry, Earth Science, Engineering, Computer Science)
           - **Video Retrieval**: Automatically retrieve instructional videos from YouTube and other platforms based on knowledge taxonomy
           - **Metadata Filtering**: Use LLM to review video metadata (title, description, comments), filtering non-instructional content
           - **Scale**: Collect 159,565 instructional videos, retain 75,000 high-quality videos after filtering (22,697 class hours, avg 18 min/video)
        2. **Video-Level Extraction & Filtering**:
           - **Audio Transcription (ASR)**: Use Whisper-large-v3 to convert audio to text, preserving timestamps
           - **ASR Refinement**: Use Qwen2-72B-Instruct to refine colloquial ASR text, improving grammar and coherence
           - **Quality Scoring**: Use DeepSeek-V2 and Llama3-70B to score ASR text quality, filtering low-quality videos
        3. **Clip-Level Extraction (Long Video→Short Clips)**:
           - **Video Segmentation**: Split long videos into short clips based on ASR timestamps (each clip corresponds to complete semantic unit)
           - **ASR Segment Merging**: Merge incomplete ASR segments into semantically coherent paragraphs
           - **Quality Filtering**:
             - Use VideoLlama2-7B to generate caption for each clip
             - Calculate similarity between clip caption and ASR (GTE-Qwen2-7B-Instruct)
             - Filter clips where visual content mismatches ASR
           - **Scale**: Generate 4M video clips
        4. **Keyframe-Level Extraction**:
           - **Keyframe Detection**: Use SSIM (Structural Similarity Index) algorithm to detect inter-frame changes, extracting keyframes
           - **OCR Extraction**: Use InternVL2 to extract text, symbols, formulas from keyframes
           - **OCR Filtering**:
             - Remove OCR unrelated to ASR (e.g., only showing speaker)
             - Remove OCR identical to previous frame
             - Discard keyframes lacking useful information
           - **Scale**: Extract 6.5M keyframes, generate 0.75B text tokens (ASR + OCR)
        5. **Textbook Sample Construction**:
           - Concatenate multiple `<keyframe, OCR, ASR>` fragments into single sample
           - Each sample contains average 10.7 keyframes and 1,297 text tokens
           - **Final Scale**: 610K interleaved image-text samples
      - **Advantages vs. Existing Datasets**:
        - **In-sample Image Similarity**: 0.686 (vs. MMC4 0.319, OBELICS 0.345), indicating more coherent frame sequences from instructional videos
        - **Average Images per Sample**: 10.7 (vs. MMC4 5.7, OBELICS 2.5), richer content
        - **Average Text Tokens per Sample**: 1,297 (vs. MMC4 417, OBELICS 816), higher knowledge density
  - **Data Statistics**:
      - **Video Scale**: 75K instructional videos, 22,697 class hours (2.5 years)
      - **Keyframes**: 6.5M
      - **Text**: 259M ASR tokens + 500M OCR tokens
      - **Final Samples**: 610K interleaved image-text samples
      - **Subject Distribution**: Math (21.7K videos), Physics (11K), Chemistry (4.5K), Earth Science (12K), Engineering (13K), Computer Science (12.8K)
  - **Experimental Results** - **Significantly improves knowledge & reasoning-intensive benchmarks**:
      - **Pretraining LLaVA-1.5-7B** (continual pretraining on 610K textbook data):
        - **MathVista**: 1-shot 43.4% (vs. MMC4 30.0%, OBELICS 28.5%, **+13.4%~14.9%**)
        - **ScienceQA**: 1-shot 29.4% (vs. MMC4 1.6%, OBELICS 2.8%, **+26.6%~27.8%**)
        - **MathVision**: 1-shot 25.6% (vs. MMC4 21.3%, OBELICS 20.1%, **+4.3%~5.5%**)
        - **Average Improvement**: Average **+11.5%** across 7 VQA benchmarks (vs. OBELICS)
      - **Pretraining Idefics2-8B**:
        - **MathVista**: 8-shot 29.7% (vs. MMC4 27.8%, OBELICS 27.6%)
        - **Continual Pretraining**: From Idefics2-8B-base continual pretraining, improvements across all benchmarks
      - **In-Context Learning Enhancement**:
        - Textbook data significantly improves model's ability to leverage few-shot context
        - In "1-shot Cheat" experiment (test sample directly in context), textbook-trained model achieves 94.1% accuracy (MathVista), far surpassing MMC4 (72.6%) and OBELICS (67.7%)
      - **SFT Stage Transfer**: Pretraining gains transfer to instruction fine-tuning stage, further improving downstream task performance
  - **Ablation Study Key Findings**:
      - **ASR Refinement Crucial**: Removing ASR refinement increases perplexity from 13.92 to 16.86, accuracy drops 4.9%
      - **OCR Importance**: Removing OCR drops accuracy by 2.3%, greater impact on math-related tasks
      - **SSIM Superior to Other Keyframe Extraction Methods**: Pixel-level extractor produces 18M keyframes (too redundant), CLIP-based only 1.7M (missing critical frames), SSIM's 6.5M optimal
      - **Image Order Matters**: Shuffling image order drops accuracy from 31.1% to 22.1% (-9%), proving temporal coherence of video frames critical for learning
  - **Institution**: Zhejiang University, Alibaba DAMO Academy
  - **Authors**: Wenqi Zhang, Hang Zhang, Xin Li, Jiashuo Sun, Yongliang Shen, Weiming Lu, Deli Zhao, Yueting Zhuang, Lidong Bing
  - **Publication**: arXiv January 2025 (v4)
  - **Paper Link**: [arXiv:2501.00958](https://arxiv.org/abs/2501.00958)
  - **Project Page**: https://multimodal-interleaved-textbook.github.io/
  - **Significance**:
      - **Data Source Innovation**: First systematic construction of VLM pretraining data from instructional videos, filling "textbook-quality" multimodal data gap
      - **High Knowledge Density**: Compared to webpage-crawled data, instructional videos are more structured, higher knowledge density, tighter image-text relations
      - **In-Context Learning Enhancement**: Significantly enhances VLM's context awareness, models more effectively leverage few-shot examples
      - **Scalability**: Fully automated pipeline, easily extensible to more subjects and languages
  

</details>
---

### Image-Invariant Text Enhancement

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

  - **Focus**: **Automatic Synthesis of High-Quality Triplet Data for Composed Image Retrieval** - Automatically generating large-scale high-quality triplet training data for Composed Image Retrieval (CIR) tasks
  - **Data Synthesis Method** - **LLM + T2I + MLLM Three-Stage Pipeline**: First complete pipeline using generative models to automatically construct high-quality CIR triplets (reference image, target image, relative caption). **Three-Stage Pipeline**: (1) **Diversified Quadruple Generation**: LLM (Qwen2.5-32B) generates text quadruples (C_Ir, C_It, C_r→t, C_t→r) with 6 predefined instruction sets covering objects, editing operations, and styles. (2) **Consistent Image Pair Synthesis**: Key insight - independent generation causes uncontrollable visual discrepancies. Strategy: Merge C_Ir and C_It into single prompt using Flux.1-dev to generate image with two semantically related sub-images, then crop into I_r and I_t. Ensures high consistency and shared semantic entities. (3) **Data Filtering**: MLLM (Qwen2.5-VL-32B) scores triplets on three dimensions (image quality, image-caption fidelity, CIR task alignment), discards bottom 15%, resulting in 534K high-quality triplets from 594K raw.
  - **CIRHS Dataset**: 534K high-quality triplets covering diverse scenes, objects, and editing operations (object/scene change, quantity variation, viewpoint shift, attribute modification) with photorealistic images and precise editing descriptions.
  - **Experimental Results - SOTA in Both Supervised and Zero-Shot Settings**: **Supervised CIR (trained on CIRHS)**: CIRR R@5 **83.81%**, R_s@1 **80.87%**, Avg **82.34%** (surpasses SPRC +1.69/+0.22/+0.95); FashionIQ Avg@10 **54.92%**, Avg@50 **75.55%** (+0.20/+0.58). **Zero-shot CIR**: CIRR R@1 **41.17%**, Avg **71.17%**; FashionIQ Avg@10 **39.11%**; CIRCO mAP@10 **25.29%** (best among all zero-shot methods). **Dataset Comparison (100K triplets)**: CIRHS significantly outperforms ST18M (CompoDiff) +11.18% R@5, WebVid-CoVR +3.90% R@5, even surpassing real-world dataset.
  - **Institution**: Beijing University of Posts and Telecommunications, SenseTime
  - **Authors**: Haiwen Li, Delong Liu, Zhaohui Hou, Zhicheng Zhao, Fei Su
  - **Publication**: arXiv July 2025 (v3)
  - **Significance**: First fully automated high-quality CIR triplet generation pipeline without human annotation. Innovative merged-prompt strategy ensures image pair semantic consistency. Synthetic data quality surpasses multiple real and synthetic datasets. Achieves SOTA performance in both supervised and zero-shot CIR.
  

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
<img src="https://img.shields.io/badge/Institution-Tencent_AI_Lab-red?style=flat-square"/>
</summary>

  - **Focus**: **Large-Scale Chart Understanding Instruction Tuning** - Creating a large-scale multi-task instruction dataset for chart image understanding tasks, significantly improving LMM performance on chart comprehension
  - **Data Synthesis Method** - **GPT-4-Driven Multi-Task Chart Instruction Generation Pipeline**:
      - **Core Innovation**: First large-scale (600K) multi-task chart understanding instruction dataset, covering 9 different task types, with high-quality instruction-answer pairs generated through GPT-4
      - **Problem Identification**:
        - Existing open-source LMMs perform poorly on chart understanding due to the vast difference between chart images and natural scene images
        - Existing chart QA datasets are small-scale, single-task, and rely on template generation or fixed vocabulary answers
        - Lack of comprehensive chart understanding evaluation benchmarks
      - **Four-Stage Data Construction Pipeline**:
        1. **Chart-Text Alignment Data Collection (210K)**:
           - **Data Sources**: Collect 210K chart-caption pairs for vision-text alignment training
           - **Sources**: Existing public datasets (FigureQA, DVQA, PlotQA, ChartQA, SciGraphQA, etc.)
           - **Format Conversion**: Unify annotations from different datasets into standard format
           - **Purpose**: Help models learn basic visual-language alignment for charts
        2. **Chart Information Extraction & Reasoning Task Generation**:
           - **Image Sources**: High-quality charts from ChartQA and Statista.com
           - **GPT-4 Generation**: Based on chart descriptions (title, axes, data range, etc.), use GPT-4 to generate diverse question-answer pairs
           - **Task Types**:
             - **Chart Information Extraction**: Extract detailed information like title, coordinate values, range, data patterns
             - **Chart Reasoning**: Reasoning questions about trends, data patterns, and analytical insights
           - **Prompt Design**: Request generation of 3 different questions, each answer less than 20 words, ensuring diversity
           - **Scale**: 330 information extraction samples, 256 reasoning samples
        3. **Scientific Chart Understanding Task Generation**:
           - **Data Sources**: Charts from arXiv scientific papers
           - **Multi-turn Dialogue Construction**: Use GPT-4 to generate multi-turn chart-related dialogues
           - **Task Types**:
             - **Contextual Chart Understanding**: Understanding the role and significance of charts in scientific literature
             - **Multiple Chart Understanding**: Understanding relationships between multiple related charts in the same document
           - **Quality Control**: Use heuristic rules to remove non-chart-related questions, ensuring focus on chart content
           - **Scale**: 56 contextual understanding samples, 52 multi-chart understanding samples
        4. **Structured Tasks & Classification Task Generation**:
           - **Chart-to-DataTable/JSON**:
             - Use real data tables from VisText dataset
             - Convert to JSON format (GPT-4 assisted)
             - Task: Convert visual information in charts to structured data formats
             - Scale: 400 data table samples, 96 JSON samples
           - **Chart Type/Topic Classification**:
             - Diverse charts crawled from the web
             - Use ground truth labels as answers
             - Scale: 360 type classification samples, 536 topic classification samples
           - **Stock Chart Analysis**:
             - Use Google Bard and source articles to generate analysis questions
             - Scale: 40 samples
      - **Human Quality Control**:
        - Filter samples with answers longer than 20 words
        - Remove samples mentioning "given caption", "existing descriptions", etc.
        - Chart-to-Json task: Remove samples not mentioning "title" as a key
        - Random sample 500 instances for human evaluation to ensure quality
      - **Key Technical Advantages**:
        - **Multi-Task Coverage**: 9 different task types, comprehensive evaluation of chart understanding capabilities
        - **High-Quality Generation**: GPT-4 generated instruction-answer pairs are natural and fluent, aligned with human cognition
        - **Open-Ended Answers**: Average answer length 23.7 words, far exceeding existing datasets' 1-2 word fixed answers
        - **Real Charts**: Use real web charts and scientific paper charts, not synthetic data
        - **Scalability**: Pipeline can be applied to any chart dataset
  - **MMC-Instruction Dataset**:
      - **Total Scale**: 600K chart instruction data
      - **Task Distribution** (9 tasks):
        1. **Chart Information Extraction**: 330 samples (extracting title, coordinates, range, etc.)
        2. **Chart Reasoning**: 256 samples (trend analysis, data pattern recognition)
        3. **Contextual Chart Understanding**: 56 samples (role of charts in scientific literature)
        4. **Multiple Chart Understanding**: 52 samples (understanding multi-chart relationships)
        5. **Chart Type Classification**: 360 samples (identifying bar, line, pie charts, etc.)
        6. **Chart Topic Classification**: 536 samples (identifying business, health, travel themes, etc.)
        7. **Chart-to-DataTable**: 400 samples (converting charts to table format)
        8. **Chart-to-JSON**: 96 samples (converting charts to JSON format)
        9. **Stock Chart Analysis**: 40 samples (analyzing stock chart trends)
      - **Data Characteristics**:
        - **Diverse Chart Types**: Bar charts, histograms, line plots, scatter plots, heatmaps, etc.
        - **Rich Topics**: Business, health, biology, engineering, sports, travel, etc.
        - **Open-Ended Answers**: Average 23.7 words, free-form responses
        - **Image Sources**: Statista.com, arXiv, VisText, web crawling
  - **MMC-Benchmark Evaluation Benchmark**:
      - **Scale**: 2,126 high-quality test samples
      - **Image Count**: 1,063 unique images
      - **Question Types**:
        - **Multiple-Choice Questions (MQA)**: 1,275 questions
        - **Free-Form Questions**: 851 questions
      - **Average Question Length**: 15.6 words
      - **Evaluation Methods**:
        1. **Generation Ability Evaluation**: Use GPT-4 to assess free-form answer accuracy (0.90 Cohen's kappa human agreement)
        2. **Understanding Ability Evaluation**: Use multiple-choice questions to directly calculate accuracy, no GPT-4 needed
      - **Data Sources**: Statista.com, arXiv scientific papers, VisText, web crawling
      - **Human Verification**: All samples underwent human quality checks
  - **MMCA Model (MultiModal Chart Assistant)**:
      - **Architecture**:
        - Vision Encoder: ViT-L (0.3B parameters)
        - Language Model: Vicuna-7B (fine-tuned with LoRA)
        - Visual Abstractor: Learnable query tokens
      - **Two-Stage Training**:
        - **Stage 1**: Chart-text alignment (freeze LLM, train visual abstractor)
        - **Stage 2**: Chart instruction tuning (LoRA fine-tune LLM, train on MMC-Instruction for 3 epochs)
      - **Training Setup**: Tesla V100 GPUs
  - **Experimental Results** - **Achieves Open-Source SOTA on Chart Understanding Tasks**:
      - **MMC-Benchmark Performance** (Generation Ability Evaluation, GPT-4 scoring):
        - **MMCA**: Overall accuracy **26%**, surpassing all open-source models
        - **LLaVA-1.5**: 24% (second place)
        - **MiniGPT-v2**: 21%
        - **mPLUG-Owl**: 20%
        - **GPT-4V**: **51%** (far exceeds open-source models, but still challenged by Chart-to-Datatable and Chart-to-Json tasks)
      - **MMC-Benchmark Performance** (Understanding Ability Evaluation, MQA accuracy):
        - **MMCA**: Overall accuracy **56%**, surpassing all open-source models
        - **LLaVA-1.5**: 51%
        - **Chart-to-DataTable**: MMCA **64%** vs other models ≤57%
        - **Chart-to-JSON**: MMCA **59%** vs other models ≤51%
      - **Existing Benchmark Performance**:
        - **ChartQA**: **57.4%** (surpasses LLaVA-1.5's 51.4%)
        - **DocVQA**: **72.5%** (comparable to LLaVA-1.5's 72.8%)
        - **TextVQA**: **59.6%** (surpasses LLaVA-1.5's 58.2%)
      - **Ablation Studies**:
        - MMCA without fine-tuning vision encoder shows significant performance drop (ChartQA: 54.2% vs 57.4%)
        - Proves fine-tuning vision encoder is crucial for chart understanding
  - **Error Analysis** (100 GPT-4V error samples):
      - **Language Bias (35%)**: Strong language priors mislead the model, ignoring visual input
      - **Vision Perception Errors (29.6%)**: Existing vision encoders (CLIP) have weak chart understanding ability, as CLIP is mainly trained on natural images
      - **Reasoning Errors (18.9%)**: Failures on complex reasoning tasks
      - **Not Following Instructions (16.5%)**: Most open-source models cannot follow human instructions well
  - **Institution**: University of Maryland College Park, Tencent AI Lab Bellevue
  - **Authors**: Fuxiao Liu, Xiaoyang Wang, Wenlin Yao, Jianshu Chen, Kaiqiang Song, Sangwoo Cho, Yaser Yacoob, Dong Yu
  - **Publication**: arXiv November 2023 (v2)
  - **Paper Link**: [arXiv:2311.10774](https://arxiv.org/abs/2311.10774)
  - **Significance**:
      - **Data Contribution**: First large-scale (600K) multi-task chart understanding instruction dataset, filling the gap in chart understanding training data
      - **Evaluation Benchmark**: Provides comprehensive chart understanding evaluation benchmark (MMC-Benchmark) covering 9 task types
      - **Open-Source Model Improvement**: Demonstrates that open-source models can significantly improve chart understanding through high-quality instruction data
      - **Error Insights**: Systematically analyzes error types of open-source and closed-source models on chart understanding, pointing direction for future improvements
      - **Scalability**: Pipeline can be applied to other domain-specific image understanding tasks
  

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

  - **Focus**: **Domain-Adaptive Post-Training Data Synthesis** - Using only open-source models to generate diverse visual instruction tasks from domain-specific image-caption pairs for MLLM domain adaptation
  - **Data Synthesis Method** - **Open-Source MLLM-Driven Generate-then-Filter Pipeline**:
      - **Core Innovation**: First domain-adaptive instruction synthesis method relying solely on open-source models, avoiding expert annotation through consistency-based filtering, outperforming rule-based methods and closed-source models
      - **Problem Identification**:
        - Domain-specific MLLM training data is scarce, especially in professional domains like medicine, food, and remote sensing
        - Existing methods rely on manual rules or expensive closed-source models (GPT-4/GPT-4V)
        - Traditional two-stage training (image-caption alignment → visual instruction tuning) reduces task diversity in domain-specific scenarios
      - **Two-Stage Data Construction Pipeline**:
        1. **Visual Instruction Synthesizer Fine-tuning (Stage A)**:
           - **Seed Data Construction**:
             - Aggregate existing multi-domain datasets covering various image domains and task types
             - Include: object recognition, domain classification, step-by-step guidance, text detection & OCR, task-oriented recognition, etc.
             - No additional expert annotation required
           - **Task Triplet Format**:
             - **Instruction**: Task description based on image-caption pair
             - **Informative Response**: Detailed answer with reasoning process
             - **Precise Response**: Concise final answer
           - **Fine-tuning Strategy**:
             - Base Model: LLaVA-v1.6-Llama3-8B (or other open-source MLLMs)
             - Input: Image + caption → Output: Task triplet
             - **Modality Balancing Strategy**: Replace 10% images with blank ones to encourage leveraging textual captions, avoiding over-reliance on visual inputs
             - Calculate loss only on conversational turns related to task triplets
        2. **Target Domain Task Synthesis (Stage B)**:
           - **Task Generation**: Use fine-tuned synthesizer to generate task triplets for target domain image-caption pairs
           - **Consistency-Based Filter (Key Innovation)**:
             - **Core Idea**: Instead of directly verifying response accuracy (requiring expert knowledge), check consistency between precise and informative responses
             - **Verification Tool**: Use Llama-3-8B to evaluate consistency
             - **Judgment Criteria**: Yes (consistent) / No (inconsistent) / Open (open-ended questions allowing multiple interpretations)
             - **Advantage**: Significantly reduces need for expert annotation, accuracy improves from 60-77% to 75-84% after filtering
           - **Quality Assurance**: ~30% of task triplets retained after filtering
      - **Single-Stage Post-Training (Innovative Training Strategy)**:
        - **Problem**: Traditional two-stage training (image-caption alignment first, then visual instruction tuning) reduces task diversity in domain-specific training
        - **Solution**: Merge into single-stage training, each sample contains two tasks:
          - **Image Captioning Task**: Use original caption as ground-truth
          - **Synthetic Visual Instruction Task**: Use filtered task triplets
        - **Advantage**: In most cases, single-stage training outperforms two-stage training
      - **Key Technical Advantages**:
        - **No Closed-Source Models**: Only uses open-source MLLMs, no need for GPT-4/GPT-4V
        - **Reduced Expert Annotation**: Consistency filter avoids per-task expert verification
        - **Task Diversity**: Synthesized instructions cover 12 major task types
        - **Domain Knowledge Utilization**: Effectively extracts domain expertise from image-caption pairs
        - **Scalability**: Pipeline applicable to any domain and any open-source MLLM
  - **Synthetic Data Scale** (based on different domain image-caption sources):
      - **Biomedicine**:
        - PMCRaw: 150K instruction-response pairs (from PMC-OA raw captions)
        - PMCRefined: 144K instruction-response pairs (from LLAVA-Med refined captions)
      - **Food Domain**:
        - Recipe1M: 32K instruction-response pairs (from Recipe1M dataset)
      - **Remote Sensing Domain**:
        - Remote Sensing: 15K instruction-response pairs (from multiple remote sensing datasets)
  - **AdaMLLM Models**:
      - **Supported Base Models**: LLaVA-v1.6-8B, Qwen2-VL-2B, Llama-3.2-11B
      - **Training Method**: Single-stage post-training (image captioning + synthetic instruction tasks)
      - **Training Time**: 13 hours (8×A100-80GB GPUs)
  - **Experimental Results** - **Significantly outperforms baselines and specialized models across all domains**:
      - **Biomedicine Domain** (AdaMLLM-8B from PMCRefined):
        - **SLAKE**: 58.0% (Open) / 73.3% (Closed), surpassing LLaVA-Med (43.4%/50.2%) and PubMedVision (50.0%/68.3%)
        - **PathVQA**: 22.9% (Open) / 78.6% (Closed), surpassing all baselines
        - **VQA-RAD**: 59.8% (Open) / 81.3% (Closed)
        - **PMC-VQA**: 47.9%, surpassing LLaVA-Med (37.1%)
      - **Food Domain** (AdaMLLM-8B):
        - **Recipe1M**: 24.8 Rouge-L (vs. LLaVA-Chef 23.1)
        - **Nutrition5K**: 36.1 Recall (vs. LLaVA-Chef 29.1)
        - **Food101**: 65.3% Acc (vs. LLaVA-1.6 47.9%)
        - **FoodSeg**: 42.0 F1 (vs. LLaVA-Chef 14.5)
      - **Remote Sensing Domain** (AdaMLLM-8B):
        - **CLRS**: 66.9% Acc (vs. LLaVA-1.6 54.3%)
        - **UCMerced**: 72.1% Acc (vs. LLaVA-1.6 64.9%)
        - **NWPU**: 47.1 Rouge-L (vs. LLaVA-1.6 26.1)
      - **Cross-Model Generalization**: Equally effective on Qwen2-VL-2B and Llama-3.2-11B
  - **Synthetic Data Quality Comparison** - **Surpasses rule-based methods and closed-source models**:
      - **vs. Rule-Based Methods**:
        - Task Diversity: 68.0 vs. 52.5 (+29.6%)
        - Domain Knowledge Utilization: 95.0 vs. 72.5 (+31.0%)
        - Task Complexity: 77.9 vs. 43.8 (+77.9%)
      - **vs. GPT-4 (Text-only)**:
        - Task Diversity: 81.0 vs. 75.2
        - Complexity: 80.0 vs. 75.3
      - **vs. GPT-4V (Vision+Text)**:
        - Task Diversity: 85.5 vs. 83.2 (comparable)
        - Accuracy (PMCRefined): 79.6 vs. 87.5 (slightly lower but acceptable)
  - **Ablation Study Key Findings**:
      - **Consistency Filter is Crucial**: Removing it drops accuracy from 58.3% to 54.2% (biomedicine)
      - **Single-Stage Training Outperforms Two-Stage**: Average 3-5% improvement on 8B and 11B models
      - **Modality Balancing Strategy is Effective**: Replacing 10% with blank images improves robustness
      - **Task Diversity Matters**: Using only synthetic tasks (without image captioning) significantly degrades performance
  - **Task Type Distribution** (synthetic data covers 12 major task types):
      - Task-Oriented Image Recognition
      - Attribute and Context Recognition
      - Object Recognition
      - Data Representation and Visualization
      - Step-by-Step Guidance
      - Anomaly Detection
      - Image-Text Matching
      - Caption Generation
      - Text Detection and OCR
      - Scene Classification
      - Domain Classification
      - Pose and Activity Recognition
  - **Institution**: BIGAI, BUAA, THU, BIT, RUC
  - **Authors**: Daixuan Cheng, Shaohan Huang, Ziyu Zhu, Xintong Zhang, Wayne Xin Zhao, Zhongzhi Luan, Bo Dai, Zhenliang Zhang
  - **Publication**: arXiv November 2024 (v4)
  - **Paper Link**: [arXiv:2411.19930](https://arxiv.org/abs/2411.19930)
  - **Open Source**: ✅ [HuggingFace](https://huggingface.co/AdaptLLM)
  - **Significance**:
      - **Open-Source Alternative**: Proves open-source models can replace expensive closed-source models (GPT-4V) for domain-adaptive data synthesis
      - **Consistency Filter Innovation**: Checking response consistency instead of directly verifying accuracy avoids massive expert annotation
      - **Single-Stage Training**: Proposes more efficient training strategy maintaining task diversity
      - **Domain Generalization**: Achieves SOTA across biomedicine, food, and remote sensing domains, proving method universality
      - **Reproducibility**: Fully open-sources models, code, and data, lowering domain adaptation barriers
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2403.00231">📄 Multimodal ArXiv</a></b><br>
<code>arXiv 2403.00231</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-The_University_of_Hong_Kong-red?style=flat-square"/>
</summary>

  - **Focus**: **Scientific Figure Understanding Dataset** - Extracting large-scale image-caption pairs from ArXiv papers and using GPT-4V to generate scientific figure QA data, improving MLLM scientific comprehension
  - **Data Synthesis Method** - **GPT-4V-Driven Scientific Figure QA Generation Pipeline**:
      - **Core Innovation**: First large-scale open-domain scientific figure understanding dataset covering multiple scientific domains, using GPT-4V to generate multiple-choice QA pairs from images
      - **Problem Identification**:
        - Existing MLLMs struggle with abstract figures (geometric shapes, scientific plots) compared to concrete images from everyday scenes
        - Scientific domain training data is scarce
        - Existing scientific figure datasets are small-scale, single-task, or limited to computer science domain only
      - **Two-Stage Data Construction Pipeline**:
        1. **ArXivCap Dataset Construction (Image-Caption Pairs)**:
           - **Data Source**: ArXiv paper source files before June 2023
           - **Paper Filtering**:
             - Retrieve paper metadata from Semantic Scholar
             - Only keep published papers (Journal Article, Conference, Review)
             - Filter low-quality papers to ensure dataset quality
           - **Image-Caption Extraction**:
             - Extract images and corresponding captions from LaTeX source files
             - **Two Image Types**:
               - **Single-Figure Pairs**: One image with one caption
               - **Multiple-Figure Pairs**: Multiple sub-figures, each with sub-caption, plus overall main caption
           - **Caption Cleaning**:
             - Remove chunks with captions shorter than 5 words
             - Use pylatexenc to convert LaTeX expressions to text
             - Preserve LaTeX formulas, convert citations to `<cit.>`, references to `<ref>`
             - Ensure caption quality and readability
           - **Scale**: 6.4M images + 3.9M captions (from 572K papers)
           - **Domain Coverage**: Mathematics, physics, computer science, biomedicine, astrophysics, condensed matter, statistics, etc.
        2. **ArXivQA Dataset Construction (GPT-4V Generated QA)**:
           - **Data Source**: Select high-quality images from ArXivCap
           - **GPT-4V QA Generation**:
             - Input: Scientific image + caption
             - Output: Multiple-choice question (question, 4 options, correct answer, rationale)
             - Prompt Design: Request generating challenging, college-level reasoning questions
             - Task Diversity: Covers figure understanding, data interpretation, scientific reasoning, etc.
           - **Quality Control**:
             - Filter invalid samples (answer not in options, formatting errors, etc.)
             - Human sampling validation (100 samples, human accuracy 80%)
             - Ensure question answerability and difficulty
           - **Scale**: 32K QA pairs (from 16.6K images)
           - **Question Characteristics**:
             - Average question length: 16.98 words
             - Average 4.20 options per question
             - Average option length: 7.59 words
      - **Key Technical Advantages**:
        - **Large-Scale Real Data**: Uses real scientific paper images, not synthetic data
        - **Open-Domain Coverage**: Covers multiple scientific domains, not limited to single discipline
        - **High-Quality QA**: GPT-4V generated questions are challenging and scientific
        - **Multimodal Alignment**: Image-caption pairs and QA pairs combined to enhance multimodal understanding
  - **ArXivCap Dataset**:
      - **Total Scale**: 6.4M images + 3.9M captions (572K papers)
      - **Image Type Distribution**:
        - Single-figure pairs: ~5.4M
        - Multiple-figure pairs: ~1M (including sub-captions)
      - **Caption Statistics**:
        - Average main caption length: 47.6 words (median 35 words)
        - Average sub-caption length: 4.8 words (median 3 words)
        - Chunk caption (merged) average length: 48.8 words
      - **Domain Distribution**: Math, computer science, physics, astrophysics, condensed matter, statistics, etc.
  - **ArXivQA Dataset**:
      - **Total Scale**: 32K multiple-choice QA pairs
      - **Image Count**: 16.6K unique images
      - **Question Types**: Figure QA, geometry problem solving, math word problems, textbook QA, visual QA, etc.
      - **Difficulty**: Requires college-level reasoning ability
  - **Experimental Results** - **ArXivQA significantly improves mathematical reasoning**:
      - **Baseline Model Evaluation** (1000-sample test set):
        - LLaVA-1.5-7B: 44.2% (second place)
        - Qwen-VL-Chat: 46.6%
        - InstructBLIP-Vicuna7B: 7.0%
        - OpenFlamingo-9B: 9.9%
        - Human Performance: 80.0% (100-sample subset)
      - **MathVista Improvement** (fine-tuning Qwen-VL-Chat-7B):
        - **Overall Accuracy**: 50.4% (vs. baseline 40.0%, +10.4% absolute improvement)
        - **Geometry Problem Solving**: 34.0% (vs. baseline 19.1%, +14.9%)
        - **Textbook QA**: 70.0% (vs. baseline 46.7%, +23.3%)
        - **Visual QA**: 64.1% (vs. baseline 57.6%, +6.5%)
        - **Surpasses Commercial Models**: 50.4% vs. Bard 50.0%
      - **ArXivCap Single-Figure Captioning** (fine-tuning Qwen-VL-Chat-7B):
        - BLEU-2: 8.9 (vs. baseline 4.4, +102%)
        - ROUGE-L: 15.8 (vs. baseline 11.1, +42%)
        - BERT-Score: 83.3 (vs. baseline 81.8)
        - Surpasses all open-source baseline models
      - **New Task Benchmarks** (defined on ArXivCap):
        - Multiple-Figure Captioning
        - Contextualized Captioning (in-context learning)
        - Title Generation (inferring paper title from figure-caption pairs)
  - **Domain-Specific Performance Analysis**:
      - Different scientific domain QA data improves different tasks differently
      - Astrophysics domain data enhances geometry problem-solving ability
      - Condensed matter domain data improves math word problem performance
      - Most domain data negatively affects FigureQA task (indicating synthetic FigureQA may not be best benchmark)
  - **Error Analysis** (human analysis of 100 samples):
      - **Language Bias**: Strong language priors mislead model (ignoring visual input)
      - **Visual Perception Errors**: CLIP and other vision encoders have weak figure understanding ability
      - **Reasoning Errors**: Complex reasoning task failures
      - **Not Following Instructions**: Open-source models cannot follow instructions well
  - **Institution**: The University of Hong Kong, Peking University
  - **Authors**: Lei Li, Yuqi Wang, Runxin Xu, Peiyi Wang, Xiachong Feng, Lingpeng Kong, Qi Liu
  - **Publication**: arXiv March 2024 (v3)
  - **Paper Link**: [arXiv:2403.00231](https://arxiv.org/abs/2403.00231)
  - **Open Source**: ✅ Dataset and code
  - **Significance**:
      - **Data Scale**: Largest real paper image-caption dataset (6.4M images)
      - **Open-Domain Coverage**: First large-scale QA dataset covering multiple scientific domains
      - **Scientific Understanding Improvement**: Significantly improves MLLM mathematical reasoning and scientific figure understanding
      - **Evaluation Benchmarks**: Provides four new task benchmarks for comprehensive scientific figure understanding evaluation
      - **GPT-4V Application**: Proves GPT-4V can effectively generate high-quality scientific QA data
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2412.07012">📄 PROVISION</a></b><br>
<code>arXiv 2412.07012</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Programmatically Scaling Vision-centric Instruction Data** - Using scene graphs as symbolic representations of images and human-written programs to systematically synthesize vision-centric instruction data, ensuring interpretability and controllability of the data generation process
  - **Data Synthesis Method** - **Scene Graph-Driven Programmatic Instruction Generation Pipeline**:
      - **Core Innovation**: First programmatic approach using scene graphs to systematically generate vision-centric instruction data, ensuring hallucination-free and scalable generation through human-written programs
      - **Augmented Scene Graph Definition**:
        - **Standard Scene Graph**: Objects as nodes, attributes assigned to nodes, object relationships/interactions as directed edges
        - **Augmented Features**: Add depth annotations (DepthAnyThing V2) and segmentation annotations (SAM-2), forming augmented scene graphs
        - **Scene Graph Sources**:
          - **Manual Annotation**: Visual Genome dataset (human-annotated scene graphs)
          - **Auto-Generated**: DataComp dataset (auto-generated using scene graph generation pipeline)
      - **Programmatic Instruction Generation System**:
        - **24 Single-Image Instruction Generators**: Transform augmented scene graphs into thousands of high-level perceptual question-answer pairs
          - **Six Instruction Dimensions**: Object QA, Attribute QA, Depth QA, Segmentation QA, Relation QA, Object+Depth QA
          - **Each Generator Uses Hundreds of Pre-defined Templates**: Systematically integrate annotations to generate diverse instruction data
          - **Coverage Capabilities**: Compare, retrieve, and reason about basic visual concepts (objects, attributes, relations)
        - **14 Multi-Image Instruction Generators**: Process multiple scene graphs to generate cross-image question-answer pairs
          - **Three Multi-Image Task Types**: Selection, Comparison, Aggregation
          - **Examples**: "Which image contains more red objects?", "What are the objects common in these images?", "How many red objects in total in these images?"
      - **Scene Graph Generation Pipeline** (for unlabeled images):
        - **Object Detection**: YOLO-world detects bounding boxes and labels for all objects
        - **Image Segmentation**: SAM-2 generates pixel-wise segmentation based on bounding boxes
        - **Attribute Detection**: Fine-tuned LLaVA-1.5-13B as attribute detection model (trained on LSA dataset, 90% precision)
        - **Relation Detection**: Fine-tuned Osprey model detects relationships between object pairs
        - **Depth Estimation**: DepthAnyThing V2 generates pixel-wise depth annotations
        - **Key Advantage**: Applicable to any image, not limited to datasets with scene graph annotations
      - **Key Technical Advantages**:
        - **Interpretability**: Scene graphs + human-written programs introduce transparency and interpretability, eliminating uncertainty of end-to-end models
        - **Hallucination-Free Guarantee**: As long as scene graphs are accurate, program-generated instructions are hallucination-free, based on explicit information in scene graphs rather than LLM probabilistic outputs
        - **Scalability**: Shift from powerful LLMs to programmatic generation, enabling scalable and cost-effective data creation
        - **No License Constraints**: Scene graphs and custom programs don't involve proprietary model outputs, avoiding license restrictions
        - **Controllability**: Human-written programs allow precise control and customization of output generation
      - **PROVISION-10M Dataset**:
        - **Total Scale**: Over 10 million unique instruction data points
        - **Data Sources**:
          - **VG-S**: 1.5M single-image instructions (Visual Genome, manually annotated scene graphs)
          - **VG-M**: 4.2M multi-image instructions (Visual Genome)
          - **DC-S**: 2.3M single-image instructions (DataComp, auto-generated scene graphs)
          - **DC-M**: 4.2M multi-image instructions (DataComp)
        - **Data Format**: Each instruction provided in both multiple-choice and short-answer versions for flexibility
      - **Experimental Results**:
        - **Single-Image Instruction Fine-tuning** (LLaVA-1.5-7B, VG-S data):
          - **CVBench 2D**: 58.0% → 65.0% (+7.0%, 50% Half-Half format)
          - **CVBench 3D**: 61.0% → 69.0% (+8.0%, 50% Half-Half format)
          - **QBench2**: 46.4% → 50.2% (+3.8%, 50% Short Answer format)
          - **RealWorldQA**: 54.2% → 58.2% (+4.0%, 50% Multiple Choice format)
          - **MMMU**: 36.2% → 39.1% (+2.9%, 20% Half-Half format)
          - **Key Findings**:
            - Multiple-choice format performs better in replacement settings (20% replacement rate optimal)
            - Short-answer format performs better in augmentation settings (50% augmentation rate optimal)
            - Half-Half format (mixed format) achieves best performance across multiple settings
        - **Multi-Image Instruction Fine-tuning** (Mantis-SigLIP-8B, VG-M data):
          - **Mantis-Eval**: 54.4% → 62.7% (+8.3%, 20% Replacement Short Answer format)
          - **MMT**: 52.9% → 58.6% (+5.7%, 20% Augmentation Half-Half format)
          - **Single-Image Benchmarks**: Average improvement of 1.95% (SEED +0.5%, MMBench +0.1%, MME +2.0%, etc.)
        - **Pre-training vs Instruction Fine-tuning** (xGen-MM-4B):
          - **Pre-training Only**: Average improvement +1.1% (DC-S) and +1.2% (VG-S)
          - **Instruction Fine-tuning Only**: Average improvement +0.4% (DC-S) and +0.9% (VG-S)
          - **Both Combined**: Average improvement +1.2% (DC-S) and +1.6% (VG-S), demonstrating synergistic effects
          - **Data Scale Impact**: Increasing from 0.75M to 1.5M samples in pre-training stage improves average performance from 59.1% to 60.1%
        - **Manual vs Auto-Generated Scene Graph Comparison**:
          - **Single-Image Tasks**: DC-S underperforms at lower data scales, but achieves comparable performance to VG-S as data scale increases to 50%
          - **Multi-Image Tasks**: DC-M consistently underperforms VG-M, possibly due to edge effects triggered by larger-scale generated scene graphs in multi-image settings
          - **Conclusion**: Manually annotated scene graphs are generally better, but auto-generated scene graphs can also improve model performance
      - **Key Findings**:
        - **Data Format Importance**: Multiple-choice and short-answer formats perform differently across settings, mixed format generally achieves best performance
        - **Data Scale Impact**: Performance improves with increasing data scale, but requires balancing data quality and quantity
        - **Scene Graph Quality**: Manually annotated scene graphs generally outperform auto-generated ones, but auto-generated scene graphs can also effectively improve performance
        - **Pre-training + Fine-tuning Synergy**: Adding data in both pre-training and instruction fine-tuning stages performs better than adding in a single stage only
      - **Institution**: University of Washington, Salesforce Research, University of Southern California
      - **Authors**: Jieyu Zhang, Le Xue, Linxin Song, Jun Wang, Weikai Huang, Manli Shu, An Yan, Zixian Ma, Juan Carlos Niebles, Silvio Savarese, Caiming Xiong, Zeyuan Chen, Ranjay Krishna, Ran Xu
      - **Publication**: arXiv December 2024 (v3)
      - **Open Source**: ✅ [Code](https://github.com/JieyuZ2/ProVision) | [Dataset](https://huggingface.co/datasets/Salesforce/ProVision-10M)
      - **Significance**:
        - **Method Innovation**: First programmatic approach using scene graphs to systematically generate vision-centric instruction data, providing interpretable and controllable data generation process
        - **Scalability**: Through scene graph generation pipeline, applicable to any image, enabling large-scale data generation
        - **Data Contribution**: Provides over 10 million high-quality vision-centric instruction data points (PROVISION-10M)
        - **Practical Value**: Significantly improves model performance across multiple benchmarks, demonstrating effectiveness of programmatic data generation
  

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

  - **Focus**: **Enhancing Cognition and Explainability of Multimodal Foundation Models with Self-Synthesized Data** - Improving LMM's fine-grained visual reasoning capabilities through visual rejection sampling framework, enabling identification of domain-specific objectives and providing verifiable explanations
  - **Data Synthesis Method** - **Information Bottleneck Concept Selection + Reward Model-Free Rejection Sampling**:
      - **Core Innovation**: First method using Information Bottleneck principle to select image-level visual concepts, generating interpretable answers through iterative rejection sampling and fine-tuning process without requiring image-specific annotations
      - **Problem Identification**: LMMs perform poorly on fine-grained visual classification tasks (e.g., LLaVA-1.5 only 12.2% on Stanford Dogs), failing to utilize key visual features for reasoning and provide verifiable explanations
      - **Two-Stage Self-Synthesis Framework**:
        1. **Image-Level Visual Concept Selection Stage**:
           - **Goal**: Select subset Z* most relevant to image X from expert-defined concept set Z
           - **Information Bottleneck Principle**: Maximize I(X;Z*) while minimizing I(Z*;Z), balancing relevance and redundancy
           - **Image Description Approximation**:
             - Use base LLaVA-1.5 to generate multiple image descriptions D = {d₁, d₂, ..., dₙ}
             - **Theoretical Guarantee**: As n→∞, I(D;Z) converges to I(X;Z) (Theorem 1)
             - Approximate true image content distribution by increasing number of descriptions n
           - **InfoNCE Scoring**: Calculate InfoNCE score sⱼ for each concept zⱼ, measuring concept relevance to image descriptions
           - **Concept Selection Criterion**: Z* = {zⱼ ∈ Z | sⱼ > μ + β̂σ}, where μ and σ are mean and standard deviation of InfoNCE scores
           - **Interpretable Answer Generation**: Use selected concepts Z* to prompt base LMM to generate interpretable answers
        2. **Reward Model-Free Rejection Sampling Stage**:
           - **Goal**: Select best answer from multiple answer candidates generated by fine-tuned model
           - **Rejection Sampling Process**:
             - Use fine-tuned model f_θ^T to generate m answer candidates Y = {y₁, y₂, ..., yₘ} for each image
             - Calculate InfoNCE score s'ᵢ for each answer yᵢ with selected concepts Z*
             - Select answer with highest score: y* = argmax s'ᵢ
           - **Additional Constraint**: Selected answer must contain correct label c, otherwise discarded
           - **Key Advantage**: No need for separate reward model, uses concept alignment as quality metric
      - **Iterative Fine-tuning Process**:
        - **Initial Fine-tuning**: Use interpretable answers generated in first stage for initial fine-tuning
        - **Iterative Improvement**:
          - Round 1: Use initial fine-tuned model to generate new answers, select best through rejection sampling
          - Round 2-N: Repeat above process, gradually improving model performance
          - Maximum 4 rounds of iteration
      - **Key Technical Advantages**:
        - **No Image-Specific Annotations**: Only requires images and class labels, no detailed image-specific feature annotations needed
        - **Information-Theoretic Foundation**: Based on Information Bottleneck principle, providing theoretical guarantees
        - **No Reward Model**: No need to train or use external reward models, uses concept alignment as quality metric
        - **Explainability**: Generated answers contain human-verifiable visual features, providing interpretable explanations
        - **Domain Adaptability**: Applicable to various domains (fine-grained classification, medical images, etc.)
      - **Experimental Results**:
        - **Fine-Grained Classification Datasets**:
          - **CUB-200**: 2.69% → 85.02% (+82.33%, 4 rounds)
          - **Stanford Dogs**: 12.2% → 86.91% (+74.71%, 4 rounds)
          - **FGVC-Aircraft**: 3.00% → 91.99% (+88.99%, 4 rounds)
          - **PLD**: 0.00% → 97.16% (+97.16%, 4 rounds)
        - **Medical Datasets**:
          - **HAM10000**: 1.62% → 85.06% (+83.44%, 4 rounds)
          - **Chest X-Ray**: 62.50% → 98.72% (+36.22%, 4 rounds, using LLaVA-Med)
        - **Explanation Quality Evaluation**:
          - **Explanation Existence (EE)**: 1.00 (all datasets), indicating always generating explanations
          - **Cognition Score (CS)**: 0.79-0.87 (all datasets), indicating good alignment with expert knowledge
          - **Fluency Score (FS)**: 6.53-9.01, indicating natural and fluent explanations
        - **vs Baseline Methods**:
          - **Naive Label (NL)**: Training only with labels, cannot generate explanations (EE=0.00), accuracy generally lower than our method
          - **Label + General Explanations (L+GE)**: Using labels and general explanations, but lower explanation quality (lower CS), poor performance on some datasets (e.g., HAM10000 only 8.45%)
        - **Concept Selection Precision**:
          - With 25 descriptions, concept selection precision reaches 72.89%
          - Outperforms GPT-4o (63.95%), LLaVA (~55%), and CLIP (~55%)
        - **Filtering Strategy Effectiveness**:
          - Without filtering: Accuracy 70.45% (CUB-200), CS 0.71
          - With filtering: Accuracy 85.02% (CUB-200), CS 0.82
          - Proves importance of rejection sampling filtering
      - **Key Findings**:
        - **Iterative Improvement**: As iteration rounds increase, accuracy and explanation quality continuously improve
        - **Concept Selection Importance**: Image-level concept selection more effective than using all label-level features
        - **Rejection Sampling Effectiveness**: Filtering strategy significantly improves model performance and explanation quality
        - **Avoid Shortcut Learning**: Using image-specific features rather than only labels avoids model learning spurious correlations
        - **Cross-Dataset Generalization**: Model trained on CUB-200 only improves 4.4% on Stanford Dogs, indicating importance of domain-specific fine-tuning
      - **Institution**: University of Georgia, Massachusetts General Hospital, Harvard Medical School
      - **Authors**: Yucheng Shi, Quanzheng Li, Jin Sun, Xiang Li, Ninghao Liu
      - **Publication**: ICLR 2025 | arXiv February 2025 (v2)
      - **Open Source**: ✅ [Code](https://github.com/sycny/SelfSynthX)
      - **Significance**:
        - **Method Innovation**: First method using Information Bottleneck principle to select image-level visual concepts without image-specific annotations
        - **Explainability Enhancement**: Generated answers contain human-verifiable visual features, providing interpretable explanations
        - **Practical Value**: Significantly improves accuracy and explanation quality across multiple fine-grained classification and medical datasets
        - **Theoretical Contribution**: Provides information-theoretic analysis proving method effectiveness
  

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

  - **Focus**: **Self-Training on Image Comprehension for Large Vision Language Models** - Enhancing LVLM's image comprehension capabilities through two-stage self-training approach, self-constructing preference datasets using unlabeled images without relying on GPT-4V or human annotation
  - **Data Synthesis Method** - **Two-Stage Image Comprehension Self-Training Framework**:
      - **Core Innovation**: First self-training approach specifically for image comprehension, significantly improving LVLM's visual perception and reasoning capabilities through self-constructed image description preference datasets and description-infused fine-tuning
      - **Problem Identification**: LVLMs require high-quality vision-language data for fine-tuning, but acquisition is costly, and existing methods rely on GPT-4V for data generation, which is still expensive
      - **STIC Two-Stage Framework**:
        - **Stage 1: Image Comprehension Self-Training**:
          - **Self-Constructed Preference Dataset**: Use base LVLM (e.g., LLaVA-v1.6) to generate preference data pairs for unlabeled images
            - **Preferred Response**: Generate detailed image descriptions through well-designed step-by-step prompts (e.g., "Please provide a detailed description of the image, focusing on the following aspects: Identify the main subjects...")
            - **Dispreferred Response**: Generated through two methods
              - **Method 1**: Use "bad prompts" (e.g., "Describe imaginative objects that may exist in the image") to elicit hallucinated descriptions
              - **Method 2**: Use normal prompts but input corrupted images (color jittering or lower resolution)
          - **DPO Alignment Fine-tuning**: Use Direct Preference Optimization (DPO) loss with additional regularization term emphasizing preferred response
            - **Loss Function**: L(θ,θ_ref) = E[ℓ(λlog(p_θ(y_w|x)/p_θ_ref(y_w|x)) - λlog(p_θ(y_l|x)/p_θ_ref(y_l|x))) - αlog p_θ(y_w|x)]
            - **Regularization Term**: -αlog p_θ(y_w|x) further emphasizes preferred response, enhancing model's ability to distinguish high-quality and low-quality responses
          - **Prompt Design**:
            - **Good Prompts**: Use GPT-4 to generate multiple initial prompts, refined through human filtering and MSCOCO sample testing
            - **Bad Prompts**: Sampled from GPT-4 generated prompts, designed to elicit inaccurate descriptions (describing objects that could logically exist)
        - **Stage 2: Description-Infused Fine-tuning**:
          - **Goal**: Further fine-tune self-trained LVLM to leverage self-generated image descriptions for instruction-following tasks
          - **Data Construction**:
            - Randomly select small subset of data (5K samples) from model's previously used instruction fine-tuning dataset
            - Generate model description for each image (using simple prompts like "Explain what is depicted in the photograph")
            - Infuse generated description into original instruction: `Image description: {model description} <original instruction>`
            - Keep original ground-truth completions unchanged
          - **Fine-tuning**: Fine-tune for one epoch on description-infused dataset
        - **Optional: Describe and Respond (DaR)**:
          - At inference, optionally let model describe image first, then concatenate description with original question to generate more informed answer
          - **Format**: First prompt model to describe image, then use description+original question as new prompt
      - **Key Technical Advantages**:
        - **No External Models**: No need for GPT-4V or other external models, only uses base LVLM itself
        - **Cost Efficiency**: Uses GPT-4-turbo instead of GPT-4V, significantly reducing costs
        - **Scalability**: Applicable to large amounts of unlabeled images, enabling large-scale data generation
        - **Goal-Oriented**: Goal-oriented nature of preference data construction ensures quality of generated data
        - **Iterative**: Improved models can be used to generate better datasets, enabling continuous improvement
      - **Experimental Results**:
        - **Main Results** (LLaVA-v1.6-7B):
          - **ScienceQA**: 68.9% → 75.3% (+6.4%)
          - **TextVQA**: 60.3% → 65.2% (+4.9%)
          - **ChartQA**: 36.4% → 41.5% (+5.1%)
          - **LLaVA-Bench**: 77.3% → 79.2% (+1.9%)
          - **MMBench**: 63.7% → 67.8% (+4.1%)
          - **MM-Vet**: 42.2% → 45.0% (+2.8%)
          - **MathVista**: 34.6% → 37.0% (+2.4%)
          - **Average Improvement**: +4.0%
        - **LLaVA-v1.5-7B Comparison**:
          - **ScienceQA**: 66.8% → 69.5% (+2.7%)
          - **TextVQA**: 58.2% → 61.4% (+3.2%)
          - **ChartQA**: 6.3% → 6.6% (+0.3%)
          - **LLaVA-Bench**: 65.4% → 68.9% (+3.5%)
          - **MMBench**: 64.3% → 65.3% (+1.0%)
          - **MM-Vet**: 31.1% → 32.6% (+1.5%)
          - **MathVista**: 25.1% → 27.2% (+2.1%)
          - **Average Improvement**: +1.7%
        - **Ablation Studies**:
          - **Describe and Respond (DaR) Effectiveness**:
            - **DaR Only (No Fine-tuning)**: Average drop 2.3% (some datasets improve, some degrade)
            - **STIC + DaR**: Average improvement 1.1%, ScienceQA improvement 2.8%
            - **Conclusion**: DaR has synergistic effect with fine-tuning process
          - **Stage Progression**:
            - **Base**: 68.9% (ScienceQA)
            - **Stage 1**: 72.5% (+3.6%)
            - **Stage 2**: 74.0% (+1.5%)
            - **Stage 2 + DaR**: 75.3% (+1.3%)
          - **Role of Dispreferred Samples**:
            - **Positive Samples Only SFT**: LLaVA-Bench 76.7% (vs Base 77.3%), drop 0.6%
            - **STIC (Preference Data)**: LLaVA-Bench 79.2%, improvement 1.9%
            - **Conclusion**: Negative samples play crucial role in preference alignment
          - **Scaling Law**:
            - **6K Preference Data**: LLaVA-Bench improvement 1.9%
            - **12K Preference Data**: LLaVA-Bench improvement 3.1%
            - **Conclusion**: Performance improves with increasing data scale, no plateau reached
          - **Image Distribution Correlation**:
            - **ScienceQA**: Large overlap with MSCOCO distribution, improvement 6.4% (highest)
            - **TextVQA**: Large overlap with MSCOCO distribution, improvement 4.9%
            - **MathVista**: Small overlap with MSCOCO distribution, improvement 2.4% (lower)
            - **ChartQA**: Small overlap with MSCOCO distribution, but improvement 5.1% (improved image comprehension plays fundamental role)
        - **Different Data Source Experiments**:
          - **MSCOCO**: Average improvement 4.0%
          - **Vision Flan**: Average improvement 4.3% (broader range of image types)
          - **Conclusion**: Using more diverse image data can further improve performance
        - **Scalability** (LLaVA-v1.6-13B):
          - **LLaVA-Bench**: 84.5% → 85.6% (+1.1%)
          - **MM-Vet**: 48.9% → 50.5% (+1.6%)
          - **MMBench**: 70.6% → 72.3% (+1.7%)
          - **Conclusion**: STIC effective across different model sizes
      - **Key Findings**:
        - **Self-Training Effectiveness**: Current LVLM's image comprehension capabilities enable generation of useful preference data, providing foundation for scalable data generation
        - **Two-Stage Synergy**: Stage 1 improves image comprehension, Stage 2 improves reasoning based on comprehension, combination achieves best results
        - **Negative Sample Importance**: Dispreferred samples play crucial role in preference alignment, using only positive samples cannot achieve same effect
        - **Data Scale Impact**: Performance improves with increasing data scale, demonstrating potential to leverage vast amounts of unlabeled images
        - **Image Distribution Correlation**: Greater overlap between training images and evaluation task distributions leads to more significant performance improvements
      - **Institution**: University of California, Los Angeles, University of California, Berkeley, Stanford University
      - **Authors**: Yihe Deng, Pan Lu, Fan Yin, Ziniu Hu, Sheng Shen, Quanquan Gu, James Zou, Kai-Wei Chang, Wei Wang
      - **Publication**: NeurIPS 2024 | arXiv May 2024
      - **Open Source**: ✅ [Code and Data](https://stic-lvlm.github.io/)
      - **Significance**:
        - **Method Innovation**: First self-training approach specifically for image comprehension, improving LVLM performance through self-constructed preference datasets
        - **Cost Efficiency**: Uses 70% less supervised fine-tuning data while achieving average 4.0% performance improvement
        - **Scalability**: Applicable to large amounts of unlabeled images, demonstrating potential to leverage large-scale unlabeled data
        - **Practical Value**: Consistent and significant performance improvements across 7 different benchmarks, demonstrating method effectiveness
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2312.06731">📄 Genixer</a></b><br>
<code>arXiv 2312.06731</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Empowering Multimodal Large Language Models as Powerful Data Generators** - Exploring the potential of current MLLMs to independently generate visual instruction tuning data without relying on GPT-4V
  - **Data Synthesis Method** - **Four-Stage Automated Data Generation Pipeline**:
      - **Core Innovation**: First systematic exploration of current MLLMs' capability as data generators, demonstrating that MLLMs can independently generate high-quality visual instruction data, even surpassing GPT-4V on some complex tasks
      - **Genixer Pipeline (Four Key Steps)**:
        1. **Instruction Data Collection**:
           - **Task Selection**: Carefully selected 9 representative VL tasks, divided into two main categories
           - **Generic Tasks**: Common VQA, Adversarial VQA, Multi-choice VQA, Multi-turn Dialogue
           - **Grounding Tasks**: REC (Referring Expression Comprehension), REG (Referring Expression Generation), PointQA, Q→CBoxA, Referential Dialogue
           - **Data Sources**: VQAv2, GQA, Counting110K, POPE, A-OKVQA, LLaVA-Conv-58K, VG, RefCOCO, PointQALocal, Visual7W, etc.
           - **Total Training Data**: ~2M samples for training data generators
        2. **Instruction Template Design**:
           - **Two-Level Instruction System**: Enables both task-agnostic and task-specific generation modes
           - **Generic Instructions**: 58 handwritten instruction templates, e.g., "Please provide a clear and direct question and answer after examining the image"
           - **Specific Instructions**: Explicitly specify task type, e.g., "This is a Common VQA task"
           - **Control Constant τ**: Controls ratio of samples using only generic instructions during training (different values 0.2-0.5 for different task types)
           - **Inference Flexibility**: Can switch modes during inference by adding or omitting specific instructions
        3. **Empowering MLLMs**:
           - **Two Data Generators**:
             - **Genixer-L**: Trained on LLaVA1.5, focused on generic task data generation
               - **Training Tasks**: Common VQA, Adv VQA, MC VQA, MD
               - **Training Settings**: AdamW optimizer, learning rate 1×10⁻⁵, batch size 128, 1 epoch training (~14 hours)
             - **Genixer-S**: Trained on Shikra, focused on grounding task data generation
               - **Two-Phase Training**: Phase 1 focuses on REC and REG, Phase 2 adds PointQA, Q→CBoxA, RD
               - **Training Settings**: Phase 1 learning rate 3×10⁻⁵, batch 128; Phase 2 learning rate 1×10⁻⁵, batch 64
           - **Training Objective**: Autoregressive generation of question-answer pairs, formula: max log p(Xₒ|X_G, X_S, X_I)
        4. **Data Generation and Filtering**:
           - **Image Sources**: 1.4M images (558K from LAION/CC3M/SBU mix, 830K from SBU)
           - **Generic Task Data Generation**:
             - **Generation**: Use Genixer-L to generate 1.4M raw VQA triplets on 1.4M images
             - **Fuyu-Driven Filtering Framework**:
               - **Verification Prompt**: "Here is a question-answer pair. Is {Q:X_q \nA:X_a} true for this image?\nPlease answer this question with Yes or No.\n"
               - **Probability Calculation**: Calculate probability of predicting "Yes": P(Y_r|X_I, X_q, X_a)
               - **Threshold Filtering**: λ=0.7, retain high-quality samples
               - **Result**: Filter from 1.4M to 915K, named **Genixer-915K**
           - **Grounding Task Data Generation**:
             - **Generation**: Use Genixer-S to generate 1.4M raw REC data on 1.4M images
             - **CLIP-Driven Filtering Framework**:
               - **Three-Step Filtering**: (1) Format validation (regex extraction of coordinates and text); (2) Bounding box size filtering (width/height ≥ 50); (3) CLIP similarity filtering (OpenCLIP-L, threshold 0.6)
               - **Result**: Filter from 1.4M to 350K, named **Genixer-350K**
      - **Key Technical Advantages**:
        - **No GPT-4V Required**: Fully based on open-source MLLMs, eliminating high API costs
        - **Complex Task Superiority**: Generation quality surpasses GPT-4V on complex tasks like REC (as shown in Fig. 1)
        - **Controllable Generation**: Two-level instruction system enables flexible task control
        - **Automatic Filtering**: Dual filtering mechanisms ensure data quality
      - **Data Scale**:
        - **Genixer-915K**: 915K VQA-like synthetic data
          - **Question Length**: Significant long-tail distribution, contains more long sentences than VQAv2
          - **Vocabulary Diversity**: Rich noun and verb distributions
          - **Quality Verification**: Fuyu-8B evaluation shows 82-88% accuracy, average probability 0.82-0.87
        - **Genixer-350K**: 350K REC-like synthetic data
          - **Expression Length**: Average 6.67 words (vs. RefCOCOg's 8.43)
          - **Region Coverage**: 447.8K objects, covering diverse scenarios
          - **Quality Verification**: CLIP similarity filtering ensures text-region alignment
      - **Experimental Results**:
        - **Generic Task Evaluation** (LLaVA1.5 + Genixer-915K):
          - **12 Benchmarks**: Improvements on 10 benchmarks
          - **Significant Improvements**: VizWiz +3.8%, ScienceQA +2.9%, MME +37.7 points
          - **Other Gains**: VQAv2 +0.6%, GQA +1.1%, TextVQA +0.8%, POPE +1.4%
        - **Grounding Task Evaluation** (Shikra + Genixer-350K):
          - **8 REC Datasets**: Improvements on 7 datasets
          - **Average Gain**: +0.6% (non-trivial improvement)
          - **Best Performance**: RefCOCO test-A +0.53%, RefCOCO+ test-B +1.02%
        - **Data Generator Performance**:
          - **Genixer-L**: On 6 benchmarks, zero-shot setting shows partial task improvements (VQAv2 +1.2%, VizWiz +0.8%)
          - **Mixed Training**: After combining with original fine-tuning data, all benchmarks show significant improvements (VQAv2 +1.7%, VizWiz +4.1%)
        - **Ablation Studies**:
          - **Data Scale Effect**: 300K→610K→915K, performance continuously improves
          - **Filtering Threshold**: λ=0.7 outperforms 0.5 and 0, proving quality > quantity
        - **Human Evaluation**:
          - **100 Sample Analysis**: 7 question type distributions (Action, Color, Counting, Object Type, Relative Position, Yes/No, Others)
          - **Accuracy**: held-in (COCO) 75-92%, held-out (Flickr30K) 65-100%
          - **User Preference Study**: 13 valid surveys show Genixer-generated data preferred on REC tasks (vs. GPT-4V)
      - **Key Findings**:
        - **MLLMs as Data Generators**: Current MLLMs can independently generate high-quality visual instruction data without GPT-4V assistance
        - **Complex Task Advantage**: On complex tasks like REC, MLLMs after training generate higher quality than GPT-4V
        - **Performance Enhancement**: Synthetic datasets significantly enhance MLLM performance on multiple multimodal benchmarks and help mitigate model hallucinations
        - **Cost Efficiency**: Eliminates GPT-4V API costs while providing more flexible generation control
      - **Institution**: Show Lab, National University of Singapore; Singapore Management University
      - **Authors**: Henry Hengyuan Zhao, Pan Zhou, Mike Zheng Shou
      - **Publication**: arXiv December 2023 (v6: 2024)
      - **Open Source**: ✅ [Code, Data, and Models](https://github.com/zhaohengyuan1/Genixer)
      - **Significance**:
        - **Paradigm Innovation**: First systematic proof that MLLMs can serve as independent data generators without relying on commercial APIs
        - **Cost Reduction**: Provides economically viable alternative for large-scale data generation
        - **Quality Assurance**: Dual filtering mechanisms ensure synthetic data quality
        - **Task Coverage**: Simultaneously supports generic and grounding tasks, providing comprehensive data generation solution
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2502.08468">📄 mmE5</a></b><br>
<code>arXiv 2502.08468</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Improving Multimodal Multilingual Embeddings via High-quality Synthetic Data** - Develop high-quality synthetic data generation framework for multimodal multilingual embeddings covering diverse tasks, modality combinations, and languages
  - **Data Synthesis Method** - **MLLM-Guided Single-Pass Multi-Aspect Generation Pipeline**:
      - **Core Innovation**: First systematic approach identifying three key criteria for high-quality synthetic multimodal data (broad scope, robust cross-modal alignment, high fidelity) and implementing comprehensive generation framework covering 93 languages and 7 modality combinations
      - **Three Quality Criteria Framework**:
        1. **Broad Scope**: Ensure generated data covers diverse tasks (classification, VQA, retrieval) and modality combinations, making it applicable to various downstream scenarios
        2. **Robust Cross-modal Alignment**: Make different modalities semantically consistent through deep thinking process and comprehensive interpretation
        3. **High Fidelity**: Maintain realistic details in synthetic data through self-evaluation and refinement mechanisms
      - **Single-Pass Generation Process**:
        - **Visual Interpretation**: Multi-aspect analysis from four perspectives (general description, object-level details, contextual features, task-specific brainstorming)
        - **Data Synthesis**: Generate task-specific data samples based on comprehensive visual understanding
        - **Self-Evaluation**: Assess data quality across relevance, plausibility, clarity, and diversity dimensions
        - **Refinement**: Produce revised versions based on evaluation feedback for improved quality
      - **Comprehensive Task & Modality Coverage**:
        - **3 Tasks**: Classification (genre/theme identification), VQA (visual question answering), Retrieval (cross-modal search)
        - **7 Modality Combinations**: I→T, IT→T, T→IT, T→I, I→I, IT→I, IT→IT (comprehensive coverage vs. prior works' 1-2 combinations)
        - **93 Languages**: English, Arabic, Spanish, Chinese, French, German, Dutch, Portuguese, Russian, Polish, Japanese, Italian, Indonesian, Persian + 75 low-resource languages
      - **Multi-Aspect Visual Analysis**:
        - **General Description**: Overall summary including primary objects, scene, notable features
        - **Object-Level Details**: Individual objects, attributes (color, size, position), relationships
        - **Contextual Features**: Scene environment, background details, lighting, actions
        - **Task-Specific Brainstorming**: Analysis of how image relates to specific task requirements
      - **Quality Assurance Mechanisms**:
        - **Deep Thinking Process**: Comprehensive pre-generation analysis ensuring robust cross-modal alignment
        - **Self-Evaluation Metrics**: Automated assessment across multiple quality dimensions
        - **Hard Negative Mining**: Generate challenging negative samples for contrastive learning
        - **Multilingual Consistency**: Ensure quality maintenance across all 93 supported languages
  - **Technical Implementation**:
      - **Base Images**: Sampled from LAION-400M for diversity and scale
      - **MLLM Integration**: Single-pass generation using LLaMA-3-Vision to avoid information loss
      - **Training Strategy**: Contrastive learning with LoRA fine-tuning (rank 8) on multimodal embedding models
      - **Language Distribution**: Balanced coverage with 23% English, equal distribution across other languages
  - **Data Scale**:
      - **Total Synthetic Data**: **560K high-quality samples** across all tasks and modality combinations
      - **Task Distribution**: Classification (140K), VQA (140K), Retrieval (280K) ensuring balanced coverage
      - **Multilingual Coverage**: Comprehensive support for 93 languages including low-resource languages
      - **Quality Filtering**: Rigorous self-evaluation and refinement ensuring high synthetic data fidelity
  - **Evaluation & Results**:
      - **MMEB Benchmark**: Achieves SOTA performance (69.8% avg.) significantly outperforming previous methods (VLM2Vec: 62.9%, MMRet: 64.1%)
      - **Multilingual Performance**: Superior results on XTD benchmark across all 7 languages (95.3% avg. vs. GME: 94.1%)
      - **Zero-Shot Capability**: Strong performance with synthetic data only (58.6% vs. previous best 44.0% on MMEB)
      - **Scaling Effect**: Linear-log relationship between performance and data size, demonstrating high synthetic data quality
  - **Key Technical Contributions**:
      - **Quality Criteria Framework**: First systematic identification of three key criteria for synthetic multimodal data quality
      - **Single-Pass Generation**: Avoids information loss through comprehensive one-pass MLLM generation
      - **Comprehensive Coverage**: Unprecedented breadth across tasks, modalities, and languages in single framework
      - **Multilingual Excellence**: Demonstrates superior multilingual embedding capabilities across diverse language families
  - **Institution**: Renmin University of China, Microsoft Corporation
  - **Open Source**: ✅ [Code, Data, and Model](https://github.com/haon-chen/mmE5)
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2409.20424">📄 World to Code (W2C)</a></b><br>
<code>arXiv 2409.20424</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Multi-modal Data Generation via Self-Instructed Compositional Captioning and Filtering** - Generate structured Python code representations of visual scenes through VLM self-instruction, reducing dependency on specialist models and human annotation
  - **Data Synthesis Method** - **Self-Instructed Compositional Pipeline with Code Formatting**:
      - **Core Innovation**: First framework using VLMs themselves to extract cross-modal information via different prompts and filter generated outputs through consistency strategies, organizing final outputs in Python code format for enhanced structural representation
      - **Four-Stage Construction Pipeline**:
        1. **Visual Concepts Extraction**:
           - **Global Caption Generation**: Simple sentence describing the image accurately
           - **Detail Caption Generation**: Comprehensive description of all visual concepts (≤120 words)
           - **Concept Extraction**: Use NLTK to extract noun phrases from captions, post-process with WordNet to remove duplicates
           - **Grounding**: Map visual concepts to bounding boxes using Grounding DINO
        2. **Self-Instructed Information Extraction**:
           - **Region-Level Captioning**: Generate compositional captions for each detected visual concept using cropped image regions
           - **OCR Information Extraction**: Guide VLMs to extract text information via instructed prompts (better than traditional OCR tools for complex scenarios)
           - **Prompt Templates**: Predefined universal templates ensuring better instruction compliance
        3. **Information Filtering via Self-Consistency**:
           - **Counting Consistency Filtering**: Verify existence of grouped visual concepts through VLM validation
           - **Caption Re-ranking**: Score and rank caption quality using VLM self-assessment
           - **Rule-based Filtering**: Remove counting-inconsistent samples using structured rules
        4. **Structured Code Formatting**:
           - **Python Class Organization**: Structure visual information as Python classes with object attributes
           - **Rich Annotations**: Include description, bounding boxes, OCR text for each visual element
           - **Hierarchical Grouping**: Group similar concepts (e.g., elephant_group, people_group) for better organization
      - **Self-Consistency Strategy**:
        - **Generator-Validator Approach**: VLM acts as both generator and validator to ensure consistency
        - **Multi-Round Verification**: Iterative validation of extracted concepts and descriptions
        - **Scoring Mechanism**: Manual scoring system for caption quality assessment
      - **Quality Assurance**:
        - **Beam Search**: Encourage VLMs to provide as many visual concepts as possible
        - **Concept Validation**: Check existence and counting accuracy of each extracted concept
        - **Consistency Scoring**: Use VLM-based scoring to rank and filter high-quality samples
  - **Technical Implementation**:
      - **Base Dataset**: ShareGPT4V images (after deduplication) for fair comparison
      - **VLM Integration**: Compatible with LLaVA-1.5 and LLaVA-NeXT architectures
      - **Processing Tools**: NLTK for concept extraction, WordNet for deduplication, Grounding DINO for spatial grounding
      - **Code Structure**: Natural environment classes with grouped objects and detailed attributes
  - **Data Scale**:
      - **Generated Samples**: 34K (LLaVA-1.5-7B), 33K (LLaVA-1.5-13B), 37K (LLaVA-NeXT-7B), 29K (LLaVA-NeXT-13B)
      - **Processing Time**: 1-1.5 days on 32 A100s (LLaVA-1.5), 2-3 days on 48 A100s (LLaVA-NeXT)
      - **Consistency Filtering**: Significant data elimination during filtering ensures high quality
  - **Evaluation & Results**:
      - **VQA Benchmarks**: Superior performance on 7/9 benchmarks (LLaVA-NeXT-7B), 6/9 benchmarks (LLaVA-NeXT-13B)
      - **Visual Grounding**: Average 1.5/1.6 IoU improvement (LLaVA-1.5 7B/13B), 3.5/1.3 IoU improvement (LLaVA-NeXT 7B/13B)
      - **Few-Shot Learning**: 5% accuracy gain on GQA 2-shot evaluation, demonstrating improved code parsing ability
      - **Code vs. Caption**: Python code format consistently outperforms single/multi-round conversation formats
  - **Key Technical Contributions**:
      - **Self-Sufficiency**: Eliminates need for multiple specialist models through VLM self-instruction
      - **Code Representation**: Novel Python code formatting for structured multimodal data organization
      - **Consistency Filtering**: Robust self-consistency strategies for quality assurance without human annotation
      - **Scalability**: Fully automated pipeline enabling large-scale structured data generation
  - **Institution**: University of Chinese Academy of Sciences, ByteDance Inc.
  - **Open Source**: ✅ Pipeline code and data construction methodology
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2406.19593">📄 SK-VQA</a></b><br>
<code>arXiv 2406.19593</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Synthetic Knowledge Generation at Scale for Context-Augmented Multimodal LLMs** - Generate large-scale synthetic context documents and knowledge-based VQA pairs for training multimodal retrieval-augmented generation (RAG) systems
  - **Data Synthesis Method** - **GPT-4 Guided Context Document & QA Generation Pipeline**:
      - **Core Innovation**: First large-scale approach using GPT-4 to automatically generate both context documents and knowledge-requiring QA pairs for arbitrary images, enabling context-augmented multimodal learning beyond Wikipedia-linked images
      - **Multi-Source Image Integration**:
        - **LAION Images**: 908K QA pairs with GPT-4 generated contexts for diverse web images
        - **Wikipedia Images**: 702K QA pairs with synthetic contexts + 182K with real Wikipedia contexts
        - **COCO-Counterfactuals**: 214K QA pairs enabling controlled evaluation scenarios
        - **Broader Coverage**: Supports arbitrary image sources vs. existing datasets limited to Wikipedia-linkable images
      - **GPT-4 Context Generation Process**:
        - **Context Document Creation**: Generate Wikipedia-style articles related to images without directly referencing them
        - **8-Condition QA Generation**: Strict criteria ensuring questions require both image and context reasoning:
          1. Questions must refer to the image
          2. Avoid mentioning object names directly
          3. Answers must require reasoning over context document
          4. Natural and concise question formulation
          5. Extractive answers from context documents
          6. Answers cannot be objects visible in image
          7. Single word/phrase answers with comma separation for multiple correct answers
          8. No conjunctions ('and'/'or') in answers
      - **Quality Assurance Pipeline**:
        - **Multi-Stage Filtering**: IR (Image Retrieval) + IR+CAP (Image Retrieval + Caption) filtering strategies
        - **Grammar Validation**: LanguageTool assessment shows 93.31% grammar accuracy on 10K sample context documents
        - **Human Evaluation**: 77% accuracy on full dataset, 87% on filtered subsets (comparable to other VQA datasets)
        - **Bias & Toxicity Detection**: State-of-the-art models used to screen generated content
        - **Factuality Verification**: 86% of randomly sampled QA pairs verified as factual using online sources
  - **Technical Implementation**:
      - **Context Diversity**: Topics span 40+ categories from sports to science, arts to geography
      - **Question Uniqueness**: 96% of 2M+ questions are unique (11× more unique questions than Encyclopedic-VQA)
      - **Vocabulary Richness**: 926K unique POS sequences, 138K vocabulary size, 12.7 average question length
      - **Filtering Effectiveness**: Post-filtering retains 984K highest-quality QA pairs while maintaining diversity
  - **Data Scale**:
      - **Total Dataset**: **2.006M QA pairs** (largest knowledge-based VQA dataset to date)
      - **Filtered Subsets**: SK-VQA IR (1.530M), SK-VQA IR+CAP (984K)
      - **Context Documents**: Each QA pair associated with rich context document containing necessary reasoning information
      - **Image Sources**: 4 diverse sources ensuring domain coverage and evaluation robustness
  - **Evaluation & Impact**:
      - **Challenge Level**: More challenging than existing datasets - state-of-the-art MLLMs achieve 38-50% accuracy vs 47-84% on ViQuAE
      - **Generalization Boost**: Fine-tuning on SK-VQA consistently improves out-of-domain performance across model sizes on InfoSeek, Enc-VQA, ViQuAE
      - **RAG System Training**: Enables training of context-augmented multimodal models for real-world RAG scenarios
      - **Benchmark Stability**: Provides more consistent evaluation across model scales compared to existing datasets
  - **Key Technical Contributions**:
      - **Scalable Synthetic Generation**: Demonstrates viability of fully automated context+QA generation at million-scale
      - **Multi-Modal RAG Training**: First dataset specifically designed for training multimodal RAG systems
      - **Quality-Quantity Balance**: Achieves both scale (2M+ samples) and quality (high human evaluation scores)
      - **Domain Generalization**: Multi-source approach ensures robust performance across diverse image types and knowledge domains
  - **Institution**: Multiple collaborating institutions
  - **Open Source**: ✅ [Dataset & Generation Code](https://arxiv.org/abs/2406.19593)
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2308.08428">📄 ALIP</a></b><br>
<code>arXiv 2308.08428</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-August_2023-red?style=flat-square"/>
</summary>

  - **Focus**: **Adaptive Language-Image Pre-training with Synthetic Caption** - Using synthetic captions to reduce web data noise, optimizing contrastive learning through adaptive weighting mechanisms
  - **Data Synthesis Method** - **OFA Model Generated Synthetic Captions + Adaptive Weight Gating Mechanisms**:
      - **Core Innovation**: Addresses image-text mismatch in web data by using large multimodal models to generate high-quality synthetic captions, designing adaptive weighting systems to dynamically balance contributions of raw text and synthetic captions
      - **Problem Identification**: Web-crawled data contains intrinsic noise and mismatched image-text pairs
        - **Content Mismatch**: Raw text too abstract (e.g., "Leisure Sunday") doesn't match concrete visual signals
        - **Information Insufficiency**: Web text lacks detailed descriptions of image content
        - **Noise Impact**: Mismatched data affects representation learning performance
      - **Synthetic Caption Generation**:
        - **Generation Model**: Use **OFA (One For All)** model to generate synthetic captions
        - **Guiding Prompt**: "What does the image describe?" guides generation of image content descriptions
        - **Quality Advantages**: Synthetic captions provide more accurate, detailed image content descriptions
          - Example: "A woman sitting on a step reading a book" vs "Leisure Sunday"
          - Contains specific object information (book, woman, steps) and action information (sitting, reading)
      - **Bi-Path Architecture**:
        - **Raw Path**: Process image-raw text pairs (x, t)
        - **Synthetic Path**: Process image-synthetic caption pairs (x, c)
        - **Triplet Input**: (image x, raw text t, synthetic caption c) as complete training unit
      - **Adaptive Weight Gating System**:
        1. **Language Consistency Gate (LCG)**:
           - **Function**: Predict sample weight Ws based on similarity between raw text and synthetic caption
           - **Computation**: Ws = sigmoid(MLP(|t-c|, t⊙c, t, c)), where ⊙ denotes element-wise multiplication
           - **Role**: Identify high-quality samples (consistent text-caption) vs low-quality samples (mismatched text-caption)
        2. **Description Consistency Gate (DCG)**:
           - **Function**: Compute image-text pair weight Wt and image-caption pair weight Wc
           - **Based on Historical Similarity**: Use historical average similarities Hxt and Hxc as thresholds
           - **Weight Formulas**:
             - Wt = exp((Sxt - Hxt) × γp) when Ws < 1
             - Wc = exp((Sxc - Hxc) × γp) when Ws < 1
           - **Adaptive Adjustment**: Mine high-quality image-text/image-caption pairs from low-quality samples
      - **Adaptive Contrastive Loss**:
        - **Traditional InfoNCE Limitations**: Uniformly weights all training samples, ignoring data quality differences
        - **Improvement Strategy**: Integrate sample weights Ws and pair weights (Wt, Wc) into InfoNCE loss
        - **Loss Functions**:
          - Lxt = -Σ WsWt × log(softmax(image-text similarity))
          - Lxc = -Σ WsWc × log(softmax(image-caption similarity))
        - **Dynamic Adjustment**: Weights adapt based on data quality during training
  - **Data Scale**:
      - **Base Dataset**: YFCC15M (15M image-text pairs)
      - **Synthetic Captions**: Generate one high-quality synthetic caption per image
      - **Computational Efficiency**: Synthetic captions can be pre-computed and stored, no online generation needed
  - **Training Strategy**:
      - **Dual Encoder Architecture**: Follow CLIP architecture (image encoder + text encoder)
      - **Joint Optimization**: Train both contrastive losses Lxt + Lxc simultaneously
      - **Weight Scheduling**: Use historical similarity statistics to dynamically adjust weight parameters
      - **Hyperparameters**: γs=2 (sample weight), γp=2 (pair weight), temperature parameter τ optimized during training
  - **Experimental Results**:
      - **Zero-shot Image-Text Retrieval**:
        - **Flickr30K**: Text→Image R@1 reaches 70.5% (vs CLIP 34.9%, +35.6%)
        - **MSCOCO**: Image→Text R@1 reaches 48.9% (vs CLIP 23.4%, +25.5%)
        - **Significant Improvements**: Achieves new SOTA performance on all retrieval metrics
      - **Linear Probing**:
        - **10 downstream datasets**: Average accuracy 72.2% (vs CLIP 63.0%, +9.2%)
        - **Zero-shot Classification**: 11 datasets average accuracy 41.7% (vs CLIP 31.8%, +9.9%)
      - **Large-scale Validation**: Validates method robustness and scalability on LAION-10M and LAION-30M
  - **Ablation Study Findings**:
      - **Weight Component Contributions**: Ws, Wt, Wc each contribute significantly, combination works best
      - **Synthetic Caption Quality**: OFA-generated captions have higher image-text similarity and more compact distribution compared to raw text
      - **Caption Length**: Synthetic caption token count concentrated in 10-15 range, significantly lower than raw text
      - **Different Capacity Models**: OFA-base and OFA-large generate captions with comparable effectiveness
  - **Key Findings**:
      - **Synthetic Caption Advantages**: Synthetic captions more accurately describe image content than raw web text, but raw text still valuable for zero-shot classification tasks
      - **Weight Mechanism Effectiveness**: Adaptive weighting system effectively identifies and utilizes high-quality data while suppressing noise impact
      - **Computational Efficiency**: Pre-computed synthetic captions more efficient than online filtering methods (avoiding extra computational overhead during training)
      - **Data Utilization Maximization**: Through adaptive weighting rather than direct filtering, fully utilizes all training data
  - **Publication**: arXiv August 2023 | DeepGlint & Huawei UK R&D & InsightFace & University of Sydney
  - **Open Source**: ✅ Code and model weights - Paper promises open source release
  - **Significance**:
      - **Web Data Noise Solution**: Provides effective framework for handling large-scale web data noise
      - **Synthetic Caption Paradigm**: Establishes standard method for using multimodal models to generate high-quality captions
      - **Adaptive Learning**: Pioneering introduction of adaptive weighting mechanisms into multimodal contrastive learning
      - **Strong Practicality**: Simple and effective method, easy to integrate into existing CLIP training pipelines
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2410.13523">📄 Medical VLP</a></b><br>
<code>arXiv 2410.13523</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-October_2024-red?style=flat-square"/>
</summary>

  - **Focus**: **Can Medical Vision-Language Pre-training Succeed with Purely Synthetic Data?** - Exploring the feasibility of medical VLP based entirely on synthetic data to address paired data scarcity in medical domain
  - **Data Synthesis Method** - **Entity-Driven Synthetic Report Generation + Specialized CXR Image Generation**:
      - **Core Innovation**: First systematic validation of purely synthetic data effectiveness in medical VLP, proposing automated pipeline to generate high-quality, distribution-balanced synthetic medical image-text pairs
      - **Problem Identification**: Real medical datasets like MIMIC-CXR have serious defects
        - **Low-Quality Images**: Blurry, poor contrast, artifact issues
        - **Unpaired Samples**: Image and text mismatches
        - **Long-Tail Distribution**: Severe imbalance in medical entity distribution affecting model learning
        - **Data Scarcity**: Difficult and expensive to obtain high-quality paired medical data
      - **Real Data Quality Assessment**:
        - **Multimodal Filtering**: Use InternVL2-26B with 6 designed queries to assess CXR image quality
        - **Query Types**: Frontal view detection, image quality assessment, artifact detection, contrast evaluation, clarity detection, diagnostic suitability
        - **Similarity Filtering**: Use RAD-DINO to extract features, filter images similar to low-quality samples
        - **Results**: Filtered out 1,448 low-quality samples from MIMIC-CXR's 213,384 pairs
      - **Entity Distribution Analysis**:
        - **NER Extraction**: Use RaTE model to extract 154,049 unique medical entities from reports
        - **Five Categories**: Abnormality (55,047), Non-Abnormality (36,365), Disease (23,017), Non-Disease (22,103), Anatomy (40,517)
        - **Long-Tail Problem**: All categories exhibit severe long-tail distribution affecting learning of rare entities
      - **Synthetic Report Generation**:
        - **Entity Sampling Strategy**:
          - Sample entity combinations from S1 (Abnormality+Disease, k=9) and S2 (Non-Abnormality+Non-Disease+Anatomy, m=3)
          - Set frequency threshold τmax=15 to ensure balanced entity distribution
          - Dynamic resampling to avoid over-representation of high-frequency entities
        - **LLM Generation**: Use Llama 3.1-70B to generate synthetic radiology reports based on sampled entities
        - **Structured Output**: Generate complete reports containing both FINDINGS and IMPRESSION sections
        - **Quality Control**: Use RaTE to verify generated reports actually contain specified entities, regenerate if mismatched
      - **Synthetic Image Generation**:
        - **Specialized Model**: Use RoentGen (clinically validated CXR-specific T2I model) to generate paired CXR images
        - **Conditional Generation**: Generate corresponding CXR images based on IMPRESSION section of synthetic reports
        - **Quality Assurance**: Only use clinically expert-validated generation models to ensure medical accuracy
      - **Data Balancing Strategy**:
        - **Distribution Control**: Actively balance synthetic data distribution through entity sampling and frequency limiting
        - **Diversity Guarantee**: Ensure reasonable representation of both rare and common diseases
        - **Pairing Guarantee**: Each synthetic report has corresponding synthetic image, avoiding unpaired issues
  - **Data Scale**:
      - **SynCXR Dataset**: 200,000 synthetic CXR image-report pairs
      - **No Manual Checking**: Fully automated generation without manual quality checks
      - **Entity Coverage**: Generated from balanced sampling of 154,049 medical entities
  - **Training Strategy**:
      - **Baseline Models**: Use ConVIRT and GLoRIA two classic MedVLP methods
      - **Training Setup**: Strictly control model and training configurations, focus on data perspective impact assessment
      - **Comparative Experiments**: Pure real data vs pure synthetic data vs mixed data three settings
  - **Experimental Results** - **Pure Synthetic Data Significantly Outperforms Real Data**:
      - **Zero-shot Classification** (Seen Diseases):
        - **ConVIRT**: Average AUC improvement +4.7%, F1 improvement +4.53%
        - **GLoRIA**: Consistently outperforms real data training on all 5 datasets
        - **Mixed Data**: AUC improvement +10.08%, F1 improvement +7.62%
      - **Zero-shot Classification** (Unseen Diseases):
        - Significantly enhanced generalization to unseen diseases
        - Improved performance on Covid-19, PadChest unseen/rare disease detection
      - **Zero-shot Grounding**:
        - Average IoU improvement +1.42%, Dice score improvement +0.97%
        - Mixed data further improvement: IoU +4.06%, Dice +2.92%
      - **Fine-tuning Tasks**:
        - Synthetic data pre-trained models consistently outperform real data on classification and segmentation tasks
        - Proves synthetic data benefits not only cross-modal learning but also single-modal visual understanding
  - **Ablation Study Findings**:
      - **Entity Balanced Sampling**: Using more entity types (25%→75%) significantly improves performance
      - **LLM Choice**: Llama 3.1-70B outperforms other LLMs and medical-specific LLMs
      - **Image Generation Model**: RoentGen (clinically validated) significantly outperforms general T2I models
      - **Data Cleaning Value**: Cleaned MIMIC-CXR performance still inferior to pure synthetic data
  - **Key Findings**:
      - **Pure Synthetic Data Feasibility**: First proof that medical VLP can be successfully trained entirely on synthetic data
      - **Synthetic Superior to Real**: Pure synthetic data training outperforms real data across multiple tasks
      - **Distribution Balance Importance**: Balanced entity distribution more critical than data authenticity
      - **Quality Over Quantity**: High-quality synthetic data more effective than large-scale noisy real data
  - **Publication**: arXiv October 2024 | Imperial College London & AstraZeneca & Ohio State University et al.
  - **Open Source**: ✅ SynCXR Dataset (200K image-text pairs) + Data Generation Pipeline + Evaluation Code
  - **Significance**:
      - **Medical AI Breakthrough**: Provides revolutionary solution to data scarcity problem in medical domain
      - **Synthetic Data Paradigm**: Proves synthetic data can completely replace real data for medical VLP
      - **Data Quality Redefinition**: Reveals distribution balance and quality control more important than data authenticity
      - **Clinical Application Prospects**: Provides new pathway for rapid medical AI system construction and privacy-sensitive data handling
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2507.22431">📄 HQ-CLIP</a></b><br>
<code>arXiv 2507.22431</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-July_2025-red?style=flat-square"/>
</summary>

  - **Focus**: **Leveraging Large Vision-Language Models to Create High-Quality Image-Text Datasets and CLIP Models** - Enhancing existing image caption quality through LVLMs to build large-scale high-quality image-text datasets
  - **Data Synthesis Method** - **Cost-Efficient LVLM-Driven Data Refinement Pipeline + Multi-Granularity Text Generation**:
      - **Core Innovation**: Proposes scalable LVLM-driven data refinement paradigm, fine-tuning open-source LVLMs with small GPT-4o samples to achieve large-scale high-quality image-text data generation
      - **Cost Efficiency Solution**:
        - **Problem**: Direct use of top-tier LVLMs like GPT-4o, Gemini too expensive for large-scale data processing
        - **Solution**: Three-step cost optimization strategy
          1. Use GPT-4o to curate 10,000 high-quality recaption samples as seed data
          2. Perform supervised fine-tuning (SFT) on lightweight open-source LVLM (Qwen2-VL-7B) to align with GPT-4o on specific task
          3. Deploy fine-tuned lightweight LVLM for efficient large-scale data processing
        - **Efficiency Validation**: SFT-enhanced Qwen2-VL-7B achieves comparable performance to 72B version while requiring only 1/9 computing resources
      - **Multi-Granularity Text Synthesis Strategy**:
        - **Four Complementary Text Types**:
          1. **Detailed Positive Description (d+)**: Long detailed image content descriptions, 4× longer than original captions on average
          2. **Short Positive Tags (t+)**: Key semantic tags extracted from detailed descriptions
          3. **Detailed Negative Description (d-)**: Semantically similar but content-mismatched detailed negative descriptions
          4. **Short Negative Tags (t-)**: Negative semantic tags mismatched with image content
        - **Prompt Engineering Optimization**:
          - Design specialized prompt templates to guide LVLM generation of high-quality, structured multi-level descriptions
          - Complete workflow including positive/negative description generation and tag extraction
        - **Quality Control**: Ensure generated text quality through multi-round iteration and automatic evaluation
      - **Data Processing Pipeline**:
        1. **Raw Data Collection**: Start from large-scale datasets like DFN-Large
        2. **LVLM Enhancement**: Use fine-tuned Qwen2-VL-7B to generate four complementary texts for each image
        3. **Quality Filtering**: Filter based on image-text similarity and generation quality
        4. **Final Integration**: Build multi-granularity dataset containing original + enhanced texts
  - **HQ-CLIP Training Framework**:
      - **Hard Negative Identification (HNI)**:
        - Utilize detailed negative descriptions and negative tags for fine-grained understanding training
        - Enhance model sensitivity to semantic nuances
        - Loss Function: L_HNI = -log(exp(sim(x,t+)/τ) / (exp(sim(x,t+)/τ) + exp(sim(x,t-)/τ)))
      - **Short-Tag Classification (STC)**:
        - Use extracted semantic tags for classification training
        - Improve model categorical semantic recognition capability
        - Loss Function: L_STC based on tag classification cross-entropy
      - **Mixed Training Strategy**:
        - Combine original captions and enhanced texts for training
        - Optimal mixing ratio: 75% enhanced text + 25% original captions
        - Dynamic weight adjustment: α=0.2 (HNI weight), β=100 (STC weight)
  - **Data Scale**:
      - **VLM-150M Dataset**: 150 million high-quality image-text pairs
      - **Base Data**: Filtered and enhanced based on DFN-Large (1.47B original data)
      - **Text Enhancement**: Each image equipped with 4 complementary text descriptions
      - **Processing Efficiency**: Using fine-tuned LVLM reduces cost by 90%+ compared to GPT-4o
  - **Experimental Results** - **Three Orders of Magnitude Validation (1M to 150M)**:
      - **Small Scale (1.4M)**:
        - ImageNet Accuracy: 8.7% (vs DFN 5.8%, +2.9%)
        - Average 38 datasets performance: 20.0% (vs DFN 17.1%, +2.9%)
      - **Medium Scale (14.7M)**:
        - ImageNet Accuracy: 40.5% (vs DFN 37.6%, +2.9%)
        - Retrieval Tasks: 38.4% (vs DFN 28.6%, +9.8%)
        - Average 38 datasets performance: 41.1% (vs DFN 36.8%, +4.3%)
      - **Large Scale (147M)**:
        - ImageNet Accuracy: 70.6% (vs DFN 68.7%, +1.9%)
        - ImageNet-V2: 63.1% (vs DFN 60.0%, +3.1%)
        - Retrieval Average: 60.9% (vs DFN 54.5%, +6.4%)
        - **SOTA Performance**: Achieves 58.6% average across 38 benchmarks
      - **Extra Large Scale (1.4B)**:
        - Continues performance improvements, validating method scalability
  - **Ablation Study Findings**:
      - **LVLM Selection**: Qwen2-VL performs best among multiple open-source LVLMs
      - **SFT Effectiveness**: GPT-4o fine-tuning significantly improves data quality and downstream performance
      - **Text Type Contributions**:
        - Detailed descriptions contribute most (+3.4% performance gain)
        - Hard negative training (+0.8% performance gain)
        - Short tag classification (+0.4% performance gain)
      - **Mixing Ratios**: 75% enhanced text is optimal ratio
  - **Quality Assessment**:
      - **Image-Text Similarity**: OpenAI CLIP-Large evaluation shows enhanced data has higher similarity
      - **GPT-4o Scoring**: Synthetic caption quality scores significantly superior to original captions
      - **Downstream Task Validation**: CLIP models trained on enhanced data perform best
  - **Key Findings**:
      - **Cost Efficiency**: Lightweight LVLMs after SFT can match large model performance with 9× cost reduction
      - **Multi-Granularity Text Value**: Combination of detailed descriptions + short tags + negative samples most effective
      - **Scalability**: Method excels from 1M to 1.5B scale
      - **Quality Enhancement**: Significantly outperforms existing methods at same data scale
  - **Publication**: arXiv July 2025 | University of Science and Technology of China & Tencent WeChat Vision
  - **Open Source**: ✅ VLM-150M Dataset (150M image-text pairs) + HQ-CLIP Models + Data Refinement Pipeline
  - **Significance**:
      - **New CLIP Data Quality Standard**: Establishes new paradigm for LVLM-based large-scale data enhancement
      - **Cost Efficiency Breakthrough**: Proves lightweight models with proper fine-tuning can replace expensive large models
      - **Multi-Granularity Text Framework**: Proposes complete text enhancement framework combining positive/negative samples and long/short texts
      - **Scalable Solution**: Provides practical path for building larger-scale, higher-quality vision-language datasets
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2511.02046">📄 Text-VQA Aug</a></b><br>
<code>arXiv 2511.02046</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Automated QA synthesis for Text-VQA** — A training-free, scalable pipeline that synthesizes high-quality question-answer pairs from scene-text images for Text-VQA pretraining
  - **Data Synthesis Method** - **OCR + Grounding + Crop Caption + Answer Selection + Question Generation + Validation**:
      1) **Text-Spotting (OCR detect+recognize)**: GLASS extracts scene text + boxes
      2) **Local Context via Grounding**: Kosmos-2 generates ROI crops (foreground/background) and aligns with OCR
      3) **Crop Captioning**: Feed crops+OCR to LLaVA-R for local captions; concatenate to global image description
      4) **OCR Answer Selection Algorithm**: From global description, find sequential OCR token groups as candidate answers (pseudo-code provided)
      5) **Question Generation (LLM)**: Intel Neural Chat 7B generates concise questions conditioned on description + chosen OCR answer
      6) **QA Validation & Length Filtering**: Same LLM judges "Right/Wrong"; filter too short/long questions to reduce noise
  - **Data Scale**:
      - **Text-VQAaug Dataset**: 44,581 images, 72,490 QA (≈1.6 questions/image)
      - Compared to Text-VQA: Questions are more specific (median length ≈14 words); some questions omit OCR tokens while answers still come from OCR
  - **Key Advantages**:
      - **Training-free & Scalable**: Leverages pretrained LMM/OCR/grounding; easy to extend to new domains
      - **Answer-first Conditioning**: Selects answer before generating question, improving controllability and consistency
      - **Quality Control**: LLM Right/Wrong validation + length constraints reduce hallucinations/noise
  - **Applications**: Accessibility (reading assistance), retail visual search, educational content, healthcare device/label reading, traffic security (license plates)
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2504.11257">📄 UI-E2I-Synth</a></b><br>
<code>arXiv 2504.11257</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **GUI instruction grounding data synthesis and benchmark** — Proposes a large-scale instruction synthesis pipeline (UI-E2I-Synth) and a comprehensive benchmark (UI-I2E-Bench) for realistic high-resolution GUI scenarios across Web/Windows/Android
  - **Data Synthesis Method** - **Three-stage divide-and-conquer (Element Parsing → Referring Expressions → Instruction Synthesis)**:
      1) **Raw Data & Parsing**: Collect screenshot+metadata from multiple platforms; heuristically parse three attributes (type/content/bbox); resample to balance element types and element-to-screen ratios
      2) **Referring Expression (RE) Generation**: In Set-of-Marks context, use element attributes + GPT-4o to generate explicit/implicit RE to reduce hallucination from image-only prompting
      3) **Parameterized User Instruction Synthesis**: Combine RE with (action type/content/target) to let GPT-4o produce first-person, concise, and faithful user instructions
  - **Data & Benchmark**:
      - **Training (UI-E2I-Synth)**: 1,635,594 screenshots, 9,899,581 instructions (Web 1.54M/9.10M; Desktop 14K/334K; AndroidControl 40K/109K; plus MOTIF, WidgetCaption)
      - **Evaluation (UI-I2E-Bench)**: 1,477 samples with fine-grained annotations (element type, element-to-screen ratio, implicitness; implicit ≥63%)
  - **Results**:
      - On ScreenSpot, ScreenSpot-Pro, and UI-I2E-Bench, UI-I2E-VLM-7B outperforms prior SOTA (e.g., OS-Atlas-7B) with ~+9.7% relative average gain; strong on implicit instructions and long-tail elements (Icon/Input)
      - With 500K web instructions, models trained on UI-E2I-Synth data surpass those trained on OS-Atlas-Web; removing instruction synthesis or attribute-enhancement notably degrades performance (ablation)
  - **Key Advantages**:
      - **Realistic element-to-screen ratio** for 1080p/1440p desktop scenarios, emphasizing small targets at high resolution
      - **Implicit instruction coverage & balanced element types**: boosts generalization to long-tail categories
      - **Parameterized instruction synthesis**: mirrors authentic user expressions grounded in actions
  - **Applications**: Integrates with GPT-4o planner for OSWorld tasks, improving real desktop agent usability
  

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
<b><b><a href="https://arxiv.org/abs/2410.02713">📄 LLaVA‑Video: Video Instruction Tuning with Synthetic Data</a></b><br>
<code>arXiv 2410.02713</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Synthetic video instruction‑following data + models** — Builds the LLaVA‑Video‑178K dataset and LLaVA‑Video models; dense frame sampling and recurrent 3‑level captioning; covers detailed captioning, open‑ended QA, and multi‑choice QA
  - **Data Synthesis**:
      - **Dynamic untrimmed sources (10)**; select most dynamic clips; avoid over‑trimmed static videos
      - **Dense sampling (1 FPS)** + **recurrent 3‑level descriptions** (10‑sec clip, 30‑sec summary, full‑video); GPT‑4o generates captions and 16‑type QA; de‑dup and non‑answerable filtering
  - **Scale**:
      - 178,510 videos → 1.3M instruction samples: 178K captions, 960K open‑ended QA, 196K multi‑choice QA
  - **Findings**:
      - More frames ⇒ better results; proposes a SlowFast‑style token budget to include up to 3× frames under the same context limit
      - Strong zero‑shot across 11 video benchmarks; open‑weight 72B comparable to commercial baselines in several tasks
  - **Significance**:
      - Establishes a high‑quality synthetic dataset and effective video tokenization strategy; plans to release data, code, and checkpoints
  
  #### 🔀 Cross-Modal Representation Transfer (No Real Images Required)
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2503.22655">📄 Unicorn</a></b><br>
<code>arXiv 2503.22655</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Text-Only Multimodal Data Synthesis** - Synthesizes VLM training data purely from text without relying on real or generated images
  - **Data Synthesis Method** - **Cross-Integrated Three-Stage Text-to-Image-Representation Pipeline**:
      - **Core Innovation**: Leverages geometric structure of cross-modal representation space (modality gap theory) to generate synthetic image representations from text representations, **completely bypassing image generation**
      - **Stage 1: Diverse Caption Data Synthesis**:
        - **Input**: 1.2M sparse caption seeds (sampled from multiple sources)
          - **Open-Domain**: MS-COCO, Flickr30K, CC3M, CC-YFCC, etc.
          - **Domain-Specific**: Conceptual Captions, Chart2Text, PlotQA, etc.
        - **Method**: Use LLM (Qwen2.5-72B-Instruction) to add detailed information to sparse captions
        - **Prompt Design**: "Add more details (object attributes, spatial relationships, background info, etc.) while preserving original semantics"
        - **Output**: 1.2M semantically rich, diverse detailed captions
        - **Quality Assurance**: Multi-round iterative optimization ensuring caption detail and accuracy
      - **Stage 2: Instruction-Tuning Data Generation**:
        - **Input**: Sample 471K captions from Stage 1
        - **Method**: Use Qwen2.5-72B-Instruction to generate three task types
        - **Three Task Types**:
          1. **Multiple-Choice**:
             - Generate questions and 4 options based on caption content
             - Test detail understanding and reasoning abilities
          2. **Question-Answering**:
             - Generate open-ended questions and detailed answers
             - Cover descriptive, factual, and reasoning questions
          3. **Complex Reasoning**:
             - Complex questions requiring multi-step reasoning
             - Combine visual understanding and logical reasoning
        - **Output**: 471K multi-task instruction-tuning data
      - **Stage 3: Modality Representation Transfer (Key Innovation)**:
        - **Theoretical Foundation - Modality Gap Geometric Structure**:
          - For paired image-text (x_img, x_text), their representations satisfy: **e_x - e_y = c + ε**
          - **c**: Constant orthogonal vector (modality gap)
          - **ε**: Alignment noise (approximated by Gaussian distribution)
        - **Transfer Process - Mean Shift**:
          1. Use text encoder (LLM2CLIP) to encode Stage 1/2 captions as text representations e_text
          2. Calculate modality gap vector c (statistically derived from small paired data)
          3. Apply mean shift: **e_synthetic_img = e_text + c**
          4. Obtain synthetic image representations without generating real images
        - **Key Techniques**:
          - Use **LLM2CLIP** (specially optimized text encoder) to ensure text representation quality
          - **Training-Free**: No additional training needed, purely exploits geometric structure
          - **Scalable**: Applicable to arbitrary scale text data
        - **Advantages**:
          - **No Images Needed**: Completely skips image generation/storage, saving API costs, time, storage space
          - **Efficient**: Reduces API cost by **44×**, time by **4×**, storage by **27×**
          - **Quality**: Synthetic representations consistent with real image representation distribution in shared space
      - **Key Technical Advantages**:
        - **Extremely Low Cost**: Drastically reduces costs vs traditional methods (API: $6.84 vs $12, Storage: 4GB vs 109GB)
        - **No Hallucination Risk**: No dependence on visual generation models, avoids image generation hallucinations
        - **Strong Scalability**: Text data abundant and cheap, easy to scale
        - **Privacy-Friendly**: No need to collect/store real images
  - **Data Scale**:
      - **Unicorn-1.2M** (pretraining dataset): 1.2M detailed captions + corresponding synthetic image representations
      - **Unicorn-471K-Instruction** (instruction-tuning dataset): 471K multi-task instruction data + corresponding synthetic image representations
      - **Caption Source Diversity**:
        - Open-domain: MS-COCO, Flickr30K, CC3M, CC-YFCC, etc.
        - Domain-specific: Conceptual Captions, Chart2Text, PlotQA, FigureQA, DVQA, etc.
  - **Model**: **Unicorn-8B VLM**
      - **Architecture**: Based on mainstream VLM architecture (vision encoder + projection layer + LLM)
      - **Training Strategy**:
        - **Pretraining**: Use Unicorn-1.2M for modality alignment
        - **Instruction-Tuning**: Use Unicorn-471K-Instruction for fine-tuning
      - **Feature**: Trained completely without real images
  - **Experimental Results** - **Comparable Performance to Real Image-Based Methods**:
      - **Multimodal Benchmark Evaluation**: Achieves competitive performance across multiple VLM benchmarks
      - **Cost-Effectiveness**: Significantly reduces training cost while maintaining performance
      - **Ablation Studies**:
        - **Stage 1 Diversity**: Detailed captions significantly improve model performance
        - **Stage 2 Task Types**: Multi-task mixed training outperforms single-task
        - **Stage 3 Representation Transfer**: Mean shift method effectively bridges modality gap
  - **Cost Comparison** (vs traditional image-text synthesis methods):
      - **API Cost**: $6.84 vs $12 (44% reduction)
      - **Synthesis Time**: 0.3 days vs 4 days (92.5% reduction)
      - **Storage**: 4GB vs 109GB (96.3% reduction)
  - **Publication**: arXiv March 2025
  - **Institution**: Xreal, Westlake University, Zhejiang University, Shanghai AI Lab, Nanyang Technological University, Beihang University, Great Bay University
  - **Authors**: Xiaomin Yu, Pengxiang Ding, Wenjie Zhang, et al.
  - **Open Source**: ✅ **Fully Open-Source** - Code, datasets
  - **Code Repository**: [github.com/Yu-xm/Unicorn](https://github.com/Yu-xm/Unicorn)
  - **Significance**:
      - **Paradigm Breakthrough**: First framework to synthesize multimodal data completely without real/generated images
      - **Theoretical Innovation**: Systematically applies modality gap theory to large-scale data synthesis
      - **Cost Revolution**: Drastically reduces cost, time, and storage overhead for multimodal data synthesis
      - **Scalability**: Leverages abundant text resources, easily scalable to larger scale
      - **Practical Value**: Provides viable solution for VLM training in resource-constrained scenarios
  
  #### 🔬 Large Model-based Text Generation
  
  > **Core Idea**: Use powerful VLMs (e.g., GPT-4V) or LLMs (e.g., GPT-4) to generate higher quality captions/dialogue data for images
  

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

  - **Focus**: **Interleaved Multi-Image Instruction Tuning** - First multi-image instruction-tuning dataset MANTIS-INSTRUCT containing 721K multi-image instruction data to train multi-image LMMs with academic-level resources
  - **Data Construction Method** - **Multi-Source Dataset Curation + Instruction Formatting**:
      - **Core Innovation**: Builds strong multi-image LMMs via instruction tuning with academic-level resources, avoiding massive pre-training on hundreds of millions of noisy interleaved image-text data
      - **MANTIS-INSTRUCT Dataset Construction**:
        - **Total Scale**: 721K multi-image instruction instances across 14 subsets
        - **Four Multi-Image Skills Coverage**:
          1. **Co-reference**: Understanding references like "second image" and grounding them to referred images
             - **LLaVA-665k-multi** (313K): Concatenates multiple single-image conversations into multi-image sequences
             - **LRV-multi** (8K): Includes natural language references like "For the second image"
          2. **Comparison**: Capturing nuances and commonalities between several images
             - **CoInstruct** (151K): Image quality, visual similarity, difference description
             - **Dreamsim** (16K), **Spot-the-Diff** (8K), **Birds-to-Words** (3K)
          3. **Reasoning**: Capturing information across multiple images and reasoning over multiple pieces
             - **NLVR2** (86K): Logical reasoning across image contents
             - **IconQA** (64K): Counting, image matching, image retrieval
             - **Contrast-Caption** (36K): Reformatting captioning datasets
             - **ImageCoDe** (17K): Free-form multi-image QA
             - **Multi-VQA** (5K): Self-collected multi-image QA
          4. **Temporal Understanding**: Observing multiple frames to understand temporal information
             - **VIST** (7K): Storytelling from image sequences
             - **NExT-QA** (4K), **STAR** (3K): Video understanding tasks
        - **Single-Image Datasets** (268K): DVQA (200K), DocVQA (39K), ChartQA (28K) for balancing multi-image and single-image abilities
        - **Newly Curated Subsets** (4 new datasets):
          - **LLaVA-665k-multi**: Multi-image version of LLaVA-665k
          - **LRV-multi**: Multi-image version of LRV
          - **Contrast-Caption**: Reformatting captioning datasets for multi-image reasoning
          - **Multi-VQA**: Self-collected multi-image QA dataset
      - **Text-Image Interleaving Format**:
        - **Format**: "(image {i}: <BOI><image><EOI>)", where <BOI> and <EOI> are image delimiters
        - **Design Principles**: (1) Mark boundaries between images clearly, (2) Denote serial number of images
        - **Implementation**: Uses <Image> and </Image> as delimiters
        - **Image Context Length**:
          - **LLaVA architecture**: 576 image tokens per image, max 14 images (8K context)
          - **Idefics2 architecture**: 64 tokens per image, max 128 images (8K context)
      - **Key Techniques**:
        - **Instruction Tuning Focus**: Low-cost instruction tuning on 721K high-quality data vs. massive pre-training
        - **Multi-Skill Coverage**: Systematically covers all four multi-image skills
        - **Academic-Level Resources**: Achieves strong performance without massive computational resources
        - **Format Standardization**: Consistent text-image interleaving format across all datasets
  - **MANTIS Model Family**:
      - **Architecture Variants**:
        - **Mantis-CLIP**: CLIP encoder + LLaMA-3-8B, pre-trained on CC3M subset (0.56M)
        - **Mantis-SigLIP**: SigLIP encoder + LLaMA-3-8B, pre-trained on CC3M subset (0.56M)
        - **Mantis-Flamingo**: CLIP encoder + MPT-7B, initialized from OpenFlamingo (pre-trained on 2.4B data)
        - **Mantis-Idefics2**: SigLIP encoder + Mistral-7B-v0.1, initialized from Idefics2 (pre-trained on 143M data)
      - **Training**: Fine-tuned on MANTIS-INSTRUCT (721K) + 268K single-image data
      - **Training Resources**: 16×A100-40G for 36 hours
  - **Mantis-Eval Benchmark**:
      - **Scale**: 217 multi-image reasoning examples covering different topics
      - **Coverage**: Size perceptions, weight comparisons, etc.
      - **Construction**: Carefully curated by annotators, images acquired via Google Search
      - **Format**: Contains both multiple-choice and short-answer questions
  - **Data Scale**:
      - **MANTIS-INSTRUCT**: 721K multi-image instruction instances
        - **Average Images per Example**: 4.7
        - **Maximum Images per Example**: 50
        - **Average Turns**: 14.4
        - **Average Text Token Length**: 555
        - **Average Text+Image Token Length**: 3,584
      - **Single-Image Datasets**: 268K instances for balancing
  - **Experimental Results** - **SOTA on All Multi-Image Benchmarks**:
      - **Multi-Image Benchmarks** (5 benchmarks):
        - **NLVR2**: Mantis-Idefics2 achieves **89.71** (vs. Idefics2-8B 86.87, +2.84)
        - **Q-Bench**: Mantis-Idefics2 achieves **75.20** (vs. Idefics2-8B 57.00, +18.20)
        - **Mantis-Eval**: Mantis-SigLIP achieves **59.45** (vs. Idefics2-8B 48.85, +10.60)
        - **BLINK**: Mantis-Idefics2 achieves **49.05** (vs. Idefics2-8B 45.18, +3.87)
        - **MVBench**: Mantis-SigLIP achieves **50.15** (vs. Idefics2-8B 29.68, +20.47)
        - **Average**: Mantis-SigLIP achieves **62.7** (vs. Idefics2-8B 53.5, +9.2), Mantis-Idefics2 achieves **64.5** (vs. Idefics2-8B 53.5, +11.0)
      - **vs. GPT-4V**: Mantis-Idefics2 matches GPT-4V performance (64.5 vs 64.5 average)
      - **vs. Idefics2-8B**: Mantis beats Idefics2-8B by average of **11 absolute points** despite Idefics2-8B being pre-trained on 140M interleaved multi-image data (200× larger than MANTIS-INSTRUCT)
      - **Generalization**: Held-in and held-out results are equivalently strong, showing strong generalization ability
      - **Single-Image Performance**: Mantis maintains strong single-image performance on par with CogVLM and Emu2
  - **Publication**: arXiv May 2024
  - **Institution**: University of Waterloo, Tsinghua University, Sea AI Lab
  - **Open Source**: ✅ [GitHub](https://github.com/tiger-ai-lab/Mantis) - Code, MANTIS-INSTRUCT Dataset (721K), Models
  - **Significance**:
      - **First Multi-Image Instruction-Tuning Dataset**: MANTIS-INSTRUCT provides essential baseline for future studies
      - **Academic-Level Resources**: Achieves SOTA without massive pre-training, demonstrating efficiency of instruction tuning
      - **Multi-Skill Coverage**: Systematically covers co-reference, comparison, reasoning, and temporal understanding
      - **Cost-Effective**: Low-cost instruction tuning (721K data) outperforms models pre-trained on 200× larger datasets
      - **Generalization**: Strong performance on both held-in and held-out benchmarks
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2406.11833">📄 MMDU</a></b><br>
<code>arXiv 2406.11833</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-NeurIPS_2024-red?style=flat-square"/>
</summary>

  - **Focus**: **Multi-Turn Multi-Image Dialog Understanding Benchmark and Instruction-Tuning Dataset** - Comprehensive benchmark and large-scale instruction tuning dataset designed to evaluate and improve LVLMs' abilities in multi-turn and multi-image conversations
  - **Data Construction Method** - **Clustering-Based Image Selection + GPT-4o Generation + Human Annotation**:
      - **Core Innovation**: Employs clustering algorithm to find relevant images and textual descriptions from open-source Wikipedia, constructs question-answer pairs by human annotators with GPT-4o assistance
      - **MMDU Benchmark Construction**:
        - **Data Collection**:
          1. **Image and Text Selection**:
             - **Source**: Open-source Wikipedia entries
             - **Method**: Clustering algorithm to identify relevant Wikipedia entities
             - **Process**: Encodes relevant tags of entries using sentence transformer, clusters entries using obtained embeddings
             - **Image Matching**: Matches entries using image captions to obtain highly relevant entries and image sets
             - **Selection**: Within each cluster, selects multiple images and associated textual information to create combinations of image-text pairs (ranging from 2 to 20 images)
          2. **Question-Answer Generation**:
             - **GPT-4o Generation**: Uses carefully crafted prompts to guide GPT-4o in generating corresponding questions and answers based on available images and text information
             - **Multi-turn Construction**:
               - Initially constructs multi-turn Q&A pairs for each single image and its associated text
               - Then inputs combinations of multiple images into GPT-4o to generate multi-turn Q&A pairs based on multiple images
               - Combines multi-turn Q&A pairs for multiple images with those for each individual image, creating dialogues that include both single-image and multi-image questions
             - **Text-Image Interleaving Format**: Uses tags like <image-1>, <image-2>, etc., to refer to different images
          3. **Quality Control**:
             - **Human Annotation**: Expert annotators meticulously review generated dialogues
             - **Selection**: Selects 110 high-quality multi-turn, multi-image dialogues for benchmark
             - **Editing**: Carefully edits samples to eliminate hallucinations and errors in GPT-4o's responses
             - **Quality Assurance**:
               - Combined automated and manual screening methods
               - Multi-round manual review mechanism (at least two rounds: preliminary checks by regular reviewers, in-depth examination by experts)
               - Specialized web UI for quick browsing and modification of data content
        - **MMDU-45K Dataset Construction**:
          - **Same Process**: Uses same process employed in building MMDU
          - **Difference**: Random sampling of human verification instead of exhaustive human evaluation used in MMDU
          - **Scale**: 45K high-quality instruction tuning data
      - **Key Techniques**:
        - **Clustering-Based Selection**: Ensures logical coherence and rich content by selecting relevant images
        - **GPT-4o Assistance**: Leverages GPT-4o for question-answer generation while maintaining human oversight
        - **Multi-turn Design**: Supports both single-image and multi-image questions in same dialogue
        - **Scalable Format**: Flexible format allows concatenating multiple dialogues, theoretically supporting unlimited length
  - **MMDU Benchmark Features**:
      - **Multi-turn and Multi-image**: Maximum of 20 images and 27 turns, at least 5× longer than previous benchmarks
      - **Long Context**: Maximum of 18K image+text tokens, evaluating LVLMs' capacity to process and comprehend extended contextual information
      - **Open-ended Evaluation**: Adopts free-form multi-turn outputs, assessing LVLMs' performance through GPT-4o as judge
      - **Evaluation Dimensions** (6 dimensions):
        1. **Creativity**: Originality and innovation in responses
        2. **Richness**: Detail and depth of information
        3. **Visual Perception**: Accuracy in identifying visual elements
        4. **Logical Coherence**: Logical structure and flow
        5. **Answer Accuracy**: Correctness of factual information
        6. **Image Relationship Understanding**: Understanding relationships between images
        - **Overall Score**: Comprehensive assessment (aggregated from the 6 dimensions)
  - **Data Scale**:
      - **MMDU Benchmark**: 110 high-quality multi-turn, multi-image dialogues with more than 1,600 questions
        - **Images per Dialogue**: 2 to 20 images
        - **Average Image & Text Token Length**: 8.2K tokens
        - **Maximum Image & Text Length**: 18K tokens
        - **Average Turns**: 15 rounds of Q&A
      - **MMDU-45K Dataset**: 45K high-quality instruction tuning data
        - **Average Text Tokens**: 6.4K
        - **Images per Sample**: 2-20 images
        - **Average 15 rounds of Q&A**
  - **Experimental Results**:
      - **Benchmark Evaluation** (15 LVLMs evaluated):
        - **Open-source vs. Proprietary Gap**: Best open-source model scores 42.8%, far behind proprietary GPT-4o at 70.2%
        - **Performance Gap**: Significant performance disparity between proprietary and open-source LVLMs
      - **Fine-tuning Results** (InternLM-XC2):
        - **MMDU**: +14.5% improvement
        - **MMStar**: +1.1% improvement
        - **MathVista**: +1.5% improvement
        - **ChartQA**: +1.2% improvement
      - **Model Improvements**:
        - **Longer Conversations**: Fine-tuning on MMDU-45K generates longer and more accurate conversations
        - **Multi-turn Performance**: Significant improvements on multi-turn, multi-image scenarios
        - **Generalization**: Improvements on both MMDU and existing benchmarks
  - **Publication**: NeurIPS 2024 (Datasets and Benchmarks Track)
  - **Institution**: Shanghai Jiao Tong University, Shanghai AI Laboratory, CUHK, CPII under InnoHK, MThreads, Inc.
  - **Open Source**: ✅ [GitHub](https://github.com/Liuziyu77/MMDU) - Code, MMDU Benchmark (110 dialogues), MMDU-45K Dataset (45K samples)
  - **Significance**:
      - **Comprehensive Benchmark**: First benchmark specifically designed for multi-turn, multi-image dialog understanding
      - **Long Context Evaluation**: Evaluates LVLMs' capacity to process extended contextual information (up to 18K tokens)
      - **Open-ended Assessment**: Adopts free-form multi-turn outputs with GPT-4o as judge, more realistic than traditional multiple-choice formats
      - **Scalable Dataset**: MMDU-45K provides large-scale instruction tuning data for improving multi-turn, multi-image capabilities
      - **Bridging Performance Gap**: Demonstrates that fine-tuning on MMDU-45K significantly addresses gap between open-source and proprietary LVLMs
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2403.09028">📄 ChartInstruct</a></b><br>
<code>arXiv 2403.09028</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Instruction Tuning Data for Chart Comprehension** - Builds large-scale, diverse chart instruction dataset for training general chart understanding models
  - **Data Synthesis Method** - **LLM-Driven Multi-Task Instruction Generation**:
      - **Core Innovation**: Leverages GPT-3.5/GPT-4 to generate instruction data covering broad chart understanding tasks, supporting instruction tuning
      - **Data Collection**:
        - **Chart Corpus**: Collects real charts from multiple online sources, covering diverse visual styles
          - **UniChart Dataset**: 611K charts (sources: Pew, Statista, OECD, OWID)
          - **WebCharts (New Contribution)**: 41K charts (web-crawled, data tables extracted using Gemini Pro Vision)
        - **Final for instruction generation**: 70,882 unique charts
      - **Instruction Generation Pipeline**:
        - **Task Selection**: Defines 6 major task categories
          1. **Chart Summarization**: Generates chart captions capturing key insights (trends, patterns)
          2. **Open-ended QA**: Generates explanatory Q&A (requiring detailed answers)
          3. **Fact Checking**: Given claim, generates verdict (accept/refute) + explanation
          4. **Chain-of-Thought (CoT) Reasoning**:
             - **Variable Dependent**: Uses tools (inspired by ToolFormer) to compute statistics
             - **Variable Independent**: Retrieval, comparison, basic math analysis
          5. **Code Generation**: Generates executable Python scripts to answer queries (inspired by PAL)
          6. **Novel Tasks**: LLM proposes new tasks (future value prediction, pattern detection, etc.)
        - **Prompt Design**:
          - Each task has dedicated prompt template
          - Input: Chart data table + metadata (title)
          - Output: Instruction-response pairs
        - **Generation Strategy**:
          - **GPT-4**: For complex reasoning tasks (CoT, Novel tasks)
          - **GPT-3.5 Turbo**: For moderate complexity tasks
          - Multiple samples generated per call to increase diversity and reduce cost
      - **Key Technical Advantages**:
        - **Task Diversity**: Covers 6 major categories, multiple sub-tasks, avoids task-specific overfitting
        - **Real Charts**: Based on real online charts, not synthetic data
        - **Automated Pipeline**: Fully automated LLM-driven pipeline, scalable
  - **Data Scale**:
      - **ChartInstruct Dataset**: 191K instructions corresponding to 70,882 charts
      - **Distribution**:
        - Chart Summarization: 53,876 (28.24%)
        - Open-ended QA: 42,470 (22.26%)
        - CoT Reasoning: 27,271 (14.3%)
        - Fact Checking: 24,175 (12.67%)
        - Code Generation: 19,572 (10.26%)
        - Novel Tasks: 23,410 (12.27%)
      - **Charts Source Distribution** (unique charts count):
        - WebCharts: 41,742 (58.9%)
        - OECD/OWID: 10,949 (15.4%)
        - Statista: 9,992 (14.1%)
        - PlotQA: 8,199 (11.6%)
      - **Instructions Distribution**: WebCharts contributes 157,190 instructions, 67.5% of total
  - **Models**: Two system designs
      1. **End-to-end**: UniChart vision encoder + LLM (Llama2-7B / Flan-T5-XL-3B)
      2. **Pipeline**: Chart-to-table model (DEPLOT) → LLM
  - **Experimental Results** - **SOTA on 4 Benchmarks**:
      - **ChartQA**: Surpasses previous SOTA
      - **Chart2Text**: SOTA on summarization task
      - **OpenCQA**: SOTA on open-ended QA
      - **ChartFC**: SOTA on fact-checking
      - **Human evaluation**: Excellent performance in real chart understanding scenarios
  - **Data Quality**:
      - **Expert Evaluation**: Manual annotation of 100 random samples
        - 87% instructions describe valid tasks
        - 86% inputs match task descriptions
        - 61% outputs fully correct, 8% partially correct
      - **Diversity**: Verb-noun pair analysis shows broad spectrum of comprehension and reasoning tasks
  - **Publication**: arXiv March 2024
  - **Institution**: York University (Canada), Qatar Computing Research Institute, Salesforce Research, NTU Singapore
  - **Authors**: Ahmed Masry, Mehrad Shahmohammadi, Md Rizwan Parvez, Enamul Hoque, Shafiq Joty
  - **Open Source**: ✅ [Code and Data](https://github.com/vis-nlp/ChartInstruct)
  - **Significance**:
      - **First Large-Scale Chart Instruction Dataset**: Establishes foundation for instruction tuning in chart domain
      - **Task Comprehensiveness**: Covers multiple aspects of chart comprehension, avoids narrow task focus
      - **Real Data**: Based on real online charts, closer to real-world applications
      - **Open Contribution**: Fully open-source data and code, advancing chart comprehension research
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2412.05243">📄 CompCap</a></b><br>
<code>arXiv 2412.05243</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Caption Generation for Composite Images** - Generates high-quality captions for composite images (collages, charts, tables, code, diagrams, etc.)
  - **Problem Background**:
      - **Composite Images (CI)**: Synthetic visual content combining multiple elements (photos, text, graphics, etc.)
      - **Current Status**: Existing MLLM training data primarily focuses on natural image (NI) captions, CI captions are scarce
      - **Impact**: MLLMs perform poorly on CIs, captioning and VQA accuracy significantly lower than NIs
  - **Data Synthesis Method** - **CompCap Framework: Metadata-Driven CI-Caption Synthesis**:
      - **Core Innovation**: Leverages metadata (image-caption pairs, layouts, tabular data, text) + LLMs + automated tools to synthesize CIs with detailed captions
      - **CompCap Framework (General)**:
        - **Input**: Metadata (raw data + configuration/customization)
        - **Image Synthesis**: Uses various tools (rendering libraries, code) to generate CIs based on metadata
        - **Caption Generation**: LLM generates accurate, detailed captions based on metadata
        - **Flexibility**: Customizable pipelines for different CI types
      - **6 CI Type Implementations**:
        1. **Collage**:
           - **Raw Data**: Image-caption pair datasets
           - **Configuration**: Randomly generated layouts (row-column structure)
           - **Image Synthesis**: Arranges images according to layout
           - **Caption Generation**: LLM generates overall caption based on individual image captions + layout info
           - **Retrieval Strategies**: Random retrieval, similarity-based retrieval, entity-based retrieval (3 types)
        2. **Image-Text**:
           - Overlays text on images
           - LLM generates captions describing both image content and text
        3. **Chart**:
           - **Raw Data**: Tabular data
           - **Image Synthesis**: Renders charts using Matplotlib/Plotly
           - **Caption Generation**: LLM generates chart descriptions based on tabular data (data analysis, trends)
        4. **Diagram**:
           - Uses tools like Mermaid to generate flowcharts, architecture diagrams
        5. **Code**:
           - **Raw Data**: Code snippets
           - **Image Synthesis**: Renders code as images (syntax highlighting)
           - **Caption Generation**: Describes code functionality, structure
        6. **Table**:
           - Renders tabular data as images
           - LLM generates table content descriptions
      - **Caption Quality Standards**:
        - **Accuracy**: Faithfully represents image content without misleading information
        - **Detailedness**: Provides specific insights beyond basic descriptions
      - **Key Technical Advantages**:
        - **Metadata-Driven**: Ensures caption accuracy (based on structured data rather than visual speculation)
        - **Modular**: Easy to extend to new CI types
        - **Scalable**: Leverages abundant raw data (image datasets, tables, etc.)
  - **Data Scale**:
      - **CompCap-118K**: 118K CI-caption pairs
      - **Composition**:
        - Collage: 42.3%
        - Image-Text: 31.4%
        - Chart: 18.7%
        - Table: 3.4%
        - Diagram: 2.5%
        - Code: 1.7%
  - **Experimental Results** - **Significant Improvements on CI Understanding Benchmarks**:
      - **Training**: SFT on xGen-MM-inst.-4B, LLaVA-NeXT-Vicuna-7B/13B
      - **Average gains across 11 benchmarks**:
        - xGen-MM-4B: +1.7%
        - LLaVA-NeXT-7B: +2.0%
        - LLaVA-NeXT-13B: +2.9%
      - **Significant improvements on CI-specific benchmarks**:
        - ChartQA: +8.0% (LLaVA-13B)
        - DocVQA: +6.2%
        - InfoVQA: +4.5%
        - TextVQA: +3.8%
      - **Maintains performance on NI benchmarks**: No degradation on natural image tasks
  - **Ablation Studies**:
      - **Caption vs VQA data**: Caption data more effective for CI understanding
      - **Data volume**: Performance improves with increasing CompCap data
      - **CI types**: Chart and Image-Text types contribute most
  - **Publication**: arXiv December 2024
  - **Institution**: Meta, Tufts University, Georgia Tech
  - **Authors**: Xiaohui Chen, Satya Narayan Shukla, Mahmoud Azab, et al.
  - **Open Source**: To be confirmed
  - **Significance**:
      - **Fills CI Data Gap**: First systematic approach to generate high-quality captions for CIs
      - **General Framework**: CompCap framework applicable to multiple CI types
      - **Practical Impact**: Significantly improves MLLMs' understanding of real-world composite images
      - **Data Efficiency**: 118K data brings significant improvements
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2410.18558">📄 Infinity-MM</a></b><br>
<code>arXiv 2410.18558</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Large-Scale Multimodal Instruction Data Construction** - Collects, integrates, and synthesizes 40M+ multimodal instruction data with tagging system-based synthesis method
  - **Core Contributions**: Data scale + synthesis method innovation
      - **Data Scale**: 44.8M multimodal instruction data (among largest open-source)
      - **Synthesis Method**: Tagging system-based data synthesis supporting continuous expansion
  - **Data Construction Method**:
      - **Stage 1: Data Collection**:
        - **Unified Preprocessing**: Collects available multimodal instruction datasets with format standardization
        - **Quality Filtering**: Deduplication, quality checks
        - **Sources**: Integrates multiple public datasets (LLaVA series, ShareGPT4V, Cambrian, etc.)
      - **Stage 2: Data Synthesis (Innovation)**:
        - **Tagging System Design**:
          - **Image Tagging**: Uses RAM++ model to extract image tags (objects, actions, scenes)
          - **Instruction Tagging**: Three-layer instruction tag system
            - **Layer 1**: 6 major categories (Coarse Perception, Fine-grained Perception-single, Fine-grained Perception-cross, Relation Reasoning, Attribute Reasoning, Logic Reasoning)
            - **Layer 2**: Refined task features
            - **Layer 3**: Detailed classification based on specific task needs, totaling 199 sub-tasks
        - **Image-Instruction Mapping**:
          - Calculates co-occurrence frequency of image tags and instruction tags in seed data
          - Computes TF-IDF values to establish image tag → instruction type mapping
          - **Purpose**: Guides what instruction types should be generated for new images
        - **Instruction Synthesis Pipeline**:
          1. **Question Generation**:
             - Input: Image + target instruction type + few-shot examples
             - Model: MiniCPM-V2.6 (open-source VLM)
             - Output: Questions matching target type
          2. **Answer Generation**:
             - Uses different prompts to generate diverse answer formats
             - Ensures answer accuracy and format diversity
          3. **Quality Filtering**:
             - Re-inputs image+question to VLM to evaluate relevance
             - Filters low-quality questions
      - **Key Technical Advantages**:
        - **Tagging System**: Systematic instruction classification ensures data diversity
        - **Image-Instruction Correspondence**: Automatically identifies which image types suit which instruction types
        - **Open-Source VLM Synthesis**: Uses MiniCPM-V2.6 instead of GPT-4, low cost and reproducible
        - **Continuous Expansion**: Framework supports continuous data addition
  - **Data Scale**:
      - **Infinity-MM**: 44.8M samples
      - **Composition** (by data category):
        - **Image Caption Data**: 10M
        - **Comprehensive Visual Instruction Data**: 25.8M
          - General Instruction: 7.1M
          - OCR Data: 2.6M
          - Doc/Chart/Screen: 5.8M
          - Math/Reasoning: 1.3M
          - Text Instruction: 9M
        - **Selective Visual Instruction Data**: 6M
          - General Instruction: 1.3M
          - OCR Data: 0.3M
          - Doc/Chart/Screen: 1.9M
          - Math/Reasoning: 0.7M
          - Text Instruction: 1.8M
        - **GPT4 & Synthetic Data**: 3M
          - General Instruction: 1M
          - OCR Data: 0.5M
          - Doc/Chart/Screen: 0.1M
          - Math/Reasoning: 0.3M
          - Text Instruction: 0.3M
          - Newly Synthesized Data (using open-source VLM): 0.8M
  - **Model**: **Aquila-VL-2B**
      - **Architecture**: 2B parameter VLM
      - **Training**: Based on Infinity-MM
  - **Experimental Results** - **2B Model SOTA**:
      - **Average Score**: Outperforms similar-scale models on multiple benchmarks
      - **Surpasses Other Open-Source Data Trained Models**:
        - Outperforms OneVision-SI trained models
        - Surpasses some closed-source data trained models (see Figure 1)
      - **Key Finding**: Large-scale high-quality data + proper mixing ratio = SOTA performance
  - **Ablation Studies**:
      - **Data Scale**: Performance improves with data volume
      - **Data Type Mixing**: Optimal mixing ratios for different task types
      - **Tagging System**: Validates effectiveness of image-instruction mapping
  - **Publication**: arXiv October 2024 (v2: January 2025)
  - **Institution**: BAAI (Beijing Academy of Artificial Intelligence), BJTU, BUPT, ICT/CAS, HKUST(GZ), PKU, DLUT
  - **Authors**: Shuhao Gu, Jialing Zhang, Siyuan Zhou, Kevin Yu, et al. (large team)
  - **Open Source**: ✅ [Dataset](https://huggingface.co/datasets/BAAI/Infinity-MM)
  - **Significance**:
      - **Scale Breakthrough**: 44.8M samples, among largest open-source datasets
      - **Synthesis Method Innovation**: Tagging system provides systematic guidance for data synthesis
      - **Open-Source VLM Synthesis**: First use of open-source VLM for large-scale high-quality synthesis
      - **Continuous Expansion**: Framework supports continuous data expansion, not one-time dataset
  

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

  - **Focus**: **LLaMA-3 Driven Billion-Scale Image Re-captioning** - Uses LLaMA-3-powered LLaVA to re-caption DataComp-1B (1.3B images) at full scale, generating detailed, aligned captions
  - **Data Synthesis Method** - **Train Captioner + Large-Scale Recaptioning**:
      - **Core Innovation**: First work to use open-source LLaMA-3 for high-quality re-captioning at **billion scale**, filling community gap
      - **Stage 1: Train High-Performance Captioner**:
        - **Model Architecture**: LLaVA-1.5 framework + **LLaMA-3-8B** (replaces original 7B/13B) + CLIP ViT-L/14 (frozen)
        - **Training Process** (2 stages):
          1. **Pre-training Stage**: 558K image-text pairs (LAION/CC/SBU) train 2-layer MLP projection
          2. **Instruction Tuning Stage**: 665K instruction data (LLaVA-1.5) + **HQ-Edit dataset** fine-tune MLP and LLM
        - **Model Performance**:
          - MMMU: 45.2 (vs. LLaVA-1.5-7B's 33.6, +11.6)
          - MM-Vet: 37.8 (vs. LLaVA-1.5-7B's 33.9, +3.9)
          - Surpasses LLaVA-1.5-13B, demonstrates strong visual understanding capability
      - **Stage 2: Large-Scale Recaptioning**:
        - **Data Source**: DataComp-1B (~1.3B web-crawled image-text pairs, already safety-checked, deduplicated, CLIP-filtered)
        - **Generation Prompt**: "Please generate a detailed caption of this image. Please be as descriptive as possible."
        - **Generation Strategy**: Greedy decoding, max 128 tokens, autoregressive generation
        - **Output**: **Recap-DataComp-1B** (1.3B re-captioned image-text pairs)
      - **Quality Analysis**:
        - **Length**: Average 49.43 tokens (vs. original 10.22, +4.8x)
        - **Vocabulary Richness**: Covers 82.86% of vocabulary, more diverse nouns and adjectives
        - **Semantic Alignment**:
          - **LongCLIP Score**: 89.91 (vs. original 10.09, **~9x improvement**)
          - Standard CLIP Score: 49.57 vs. 50.43 (comparable, since CLIP trained on short captions)
        - **Human Quality Assessment (GPT-4V scoring)**:
          - Average score: 4.14/5 (vs. original 3.71, +0.43)
          - Evaluation dimensions: Fluency, accuracy, alignment
  - **Experimental Results** - **Significant Improvements for CLIP and DiT Models**:
      - **CLIP Models** (mixing ratio p=0.8, 80% original + 20% re-captioned):
        - **Zero-Shot Retrieval** (COCO I→T): 61.5% (vs. original 57.3%, +4.2%)
        - **Zero-Shot Retrieval** (Flickr30K T→I): 66.9% (vs. original 63.0%, +3.9%)
        - **Urban-1K Long-Text Retrieval**: 85.0% I→T (vs. original 53.2%, **+31.8%**)
        - **VG-Attribution**: 66.4% (vs. original 57.1%, +9.3%)
      - **Text-to-Image DiT Models** (mixing ratio p=0.0, 100% re-captioned):
        - **FID**: 27.8 (vs. original 36.2, **-8.4**)
        - **CLIP Score**: 32.5% (vs. original 29.3%, +3.2%)
        - **Recap-CLIP Score**: 28.3% (vs. original 19.9%, +8.4%)
        - **GPT-4V Score**: 2.53 (vs. original 1.40, +1.1)
      - **Key Findings**:
        - **Mixing Strategy Optimal**: Original + re-captioned mixed training works best (prevents overfitting)
        - **Larger Text Encoder**: With re-captioned data, expanding CLIP text encoder further improves performance
        - **Long-Text Understanding**: Re-captioning significantly improves CLIP's understanding of long, complex text
  - **Data Scale**:
      - **Recap-DataComp-1B**: 1.3B re-captioned image-text pairs
      - **Average Caption Length**: 49.43 tokens (vs. original 10.22)
  - **Open Source**: ✅ [Project Page](https://www.haqtu.me/Recap-Datacomp-1B/)
  - **Institution**: UC Santa Cruz + University of Edinburgh + JHU + Adobe + UT Austin
  - **Publication**: arXiv June 2024
  - **Significance**:
      - **Open-Source Billion-Scale Re-captioning**: First open-source billion-scale high-quality re-captioning dataset, lowers community barrier
      - **LLaMA-3 Application**: Demonstrates open-source LLM (LLaMA-3) can achieve GPT-4V-level annotation quality
      - **Cross-Task Generalization**: Simultaneously improves discriminative (CLIP) and generative (DiT) model performance
      - **Long-Text Understanding**: Proves critical role of detailed captions for long-text retrieval and attribute understanding
      - **Mixed Strategy Inspiration**: Provides best practices for original + synthetic data mixed training to community
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2504.13123">📄 Hunyuan-Recap100M</a></b><br>
<code>arXiv 2504.13123</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Scale-100M-orange?style=flat-square"/>
<img src="https://img.shields.io/badge/Institution-Industrial_Report-red?style=flat-square"/>
</summary>

  - **Focus**: **Low-Hallucination, Knowledge-Intensive Re-captioning** - Tencent Hunyuan team's 100M-scale re-captioning work with hallucination mitigation and knowledge enrichment
  - **Data Synthesis Method** - **Three-Stage SFT + CDPO Pipeline**:
      - **Core Innovation**: First large-scale re-captioning work systematically addressing **hallucination** and **knowledge enrichment**, three-stage training (SFT + DPO + CDPO) dramatically improves caption quality
      - **Stage 1: Knowledge-Enriching Supervised Fine-Tuning (SFT)**:
        - **Model**: Qwen2.5-VL-3B (base model)
        - **Training Data**: 43K high-quality image-caption pairs
          - **Sources**: Selected from ShareGPT4V, LLaVA-OneVision, high-quality captions
          - **Characteristics**: Rich knowledge, detailed descriptions, low hallucination
        - **Training Objective**: Standard next-token prediction loss
        - **Effect**: Model learns generating knowledge-rich, detailed captions, but still contains hallucinations
      - **Stage 2: Direct Preference Optimization (DPO)**:
        - **Data Construction**: Use trained SFT model to generate multiple caption candidates for each image
          - **Preference Annotation**: Human annotators compare candidates, mark preferred/dispreferred pairs
          - **Focus**: Penalize hallucinations, reward accuracy and detail
        - **Training Data**: 218K preference pairs
        - **DPO Objective**: Maximize log-probability ratio of preferred vs. dispreferred captions
        - **Effect**: Significantly reduces hallucinations, but model may gradually saturate, requiring further optimization
      - **Stage 3: Continuous DPO (CDPO)**:
        - **Innovation**: Modified standard DPO algorithm—when performance plateaus, iteratively update reference model (e.g., using current policy), resample preference data using updated policy, yielding new implicit reward signal, resume optimization
        - **Sequence-Length Balancing**: During CDPO training, apply sequence-length balancing operation to preference pairs to prevent sample length from acting as unintended learning signal (e.g., if longer completions more likely to contain hallucinations)
        - **Training Data**: 139K preference pairs (after filtering and balancing)
        - **Effect**: Further reduces hallucinations, improves overall caption quality
      - **Quality Screening & Filtering**:
        - **Preliminary Annotation**: Use trained captioner to generate captions for large-scale image corpus
        - **Hallucination Detection**: Use POPE benchmark and other hallucination detection tools to filter high-hallucination captions
        - **Knowledge Verification**: Use external knowledge bases (Wikipedia, encyclopedias) to verify factual correctness
        - **Human Review**: Random sampling for human review to ensure final dataset quality
  - **Data Scale**:
      - **Hunyuan-Recap100M**: 100M re-captioned image-text pairs
      - **Average Caption Length**: 103.15 tokens (significantly longer than traditional captions)
      - **Hallucination-Free Rate**: 77.9% (vs. baseline 48.3%, **+29.6%**)
      - **Knowledge-Intensive**: Average 8.1 knowledge entities per caption
  - **Experimental Results** - **State-of-the-Art Performance on Multiple Benchmarks**:
      - **Hallucination Metrics**:
        - **Non-Hallucination Rate**: 77.86% (CDPO) vs. 74.47% (DPO) vs. 73.75% (SFT)
        - **Low-Hallucination Rate**: 96.85% (CDPO) vs. 96.64% (DPO) vs. 97% (baseline)
      - **Vision-Language Pre-training**: Models pre-trained on Hunyuan-Recap100M significantly outperform baseline on 15+ VLM benchmarks
      - **Knowledge-Intensive Tasks**: Particularly excels on tasks requiring world knowledge (e.g., VQAv2, OK-VQA)
      - **Generalization**: Strong generalization to different model architectures (CLIP, DiT, VLMs)
  - **Ablation Studies**:
      - **SFT vs. DPO vs. CDPO**: CDPO best reduces hallucinations while maintaining caption detail
      - **Data Scale**: Performance scales with data volume, 100M achieves optimal cost-performance balance
      - **Knowledge Enrichment**: Knowledge-enriched captions significantly improve downstream task performance
  - **Open Source**: ✅ **Will Release** - Hunyuan-Recap100M dataset (100M image-text pairs)
  - **Institution**: Tencent Hunyuan Team
  - **Publication**: arXiv April 2025
  - **Significance**:
      - **Industrial-Scale Hallucination Mitigation**: First systematic solution to hallucination problem in large-scale re-captioning
      - **Three-Stage Training**: SFT + DPO + CDPO provides reusable paradigm for high-quality caption generation
      - **Knowledge Enrichment**: Demonstrates importance of incorporating external knowledge into multimodal data
      - **Open-Source Contribution**: 100M-scale dataset significantly enriches community resources
      - **Generalization**: Methods and data broadly applicable to various VLM pre-training scenarios
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2507.18616">📄 SynC</a></b><br>
<code>arXiv 2507.18616</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
</summary>

  - **Focus**: **Synthetic Dataset Refinement for Zero-shot Image Captioning** - Refine synthetic image-caption datasets through one-to-many mapping, reassigning captions to best-aligned synthetic images
  - **Data Synthesis Method** - **One-to-Many Mapping + Cycle-Consistency Alignment Scoring**:
      - **Core Innovation**: Unlike traditional pruning or regeneration, SynC focuses on **reassigning captions to pre-existing best-matched synthetic images from the image pool**
      - **Problem Definition**:
        - **Traditional One-to-One**: Φ_One(C_i) = {I_i^syn}, each caption corresponds only to directly generated image
        - **Challenge**: T2I models frequently generate misalignment images (missing objects, incorrect attributes), while captions remain well-formed
        - **Gap vs. Web Data Pruning**: Web data is "noisy text + clean image"; synthetic data is "clean caption + noisy image"
      - **One-to-Many Selection Strategy (Φ_T2I)**:
        - **Input**: Caption C_i, pre-generated synthetic image pool I^syn
        - **T2I Retrieval**: Use VLM (SigLIP ViT-B/16) text encoder E_T and image encoder E_I
        - **Retrieve Top-K Candidates**: Φ_i = Top-K_j {⟨E_I(I_j^syn), E_T(C_i)⟩}, K=15
        - **Output**: Candidate set {I_r^syn}_r∈R_i, broader than just I_i^syn
        - **Rationale**: Search across caption corpus for best image matches, rather than being limited to misaligned pairs
      - **Cycle-Consistency Alignment Scoring (f_ret)**:
        - **Standard CLIP Score Limitation**: Global semantic similarity, lacks fine-grained detail verification
        - **Cycle-Consistency Inspiration**: T2I retrieval (selection) + I2T retrieval (verification)
        - **I2T Retrieval Scoring**:
          1. For candidate image I^syn, perform I2T retrieval to find top-K_r captions from caption corpus C
          2. Use SBERT (Sentence Transformer) to compute text similarity between retrieved captions and original caption C
          3. Formula: f_ret(I^syn, C) = max_r∈Φ(I^syn) ⟨E_S(C_r), E_S(C)⟩
        - **Verification Logic**: If I^syn matches C, then captions related to I^syn should be similar to C
        - **Final Selection**: I_i^*syn = argmax_{I^syn∈S(C_i)} f_ret(I^syn, C_i)
      - **Filtering**: Sort by alignment score, keep top τ% pairs, τ ∈ [0,1]
  - **Implementation Details**:
      - **Baseline Model**: PCM-Net (ECCV 2024)
      - **T2I Model**: Stable Diffusion v1.4 (512×512, 20 sampling steps)
      - **Retrieval VLM**: SigLIP ViT-B/16@256
      - **Text Encoder**: SBERT (unimodal text similarity)
      - **Data Sources**: CC3M, SS1M (~200K synthetic pairs)
  - **Experimental Results** - **Consistent Improvements Across Captioning Benchmarks**:
      - **COCO Captioning** (ViT-B/32):
        - BLEU@4: 31.5 → 33.6 (+2.1)
        - CIDEr: 103.8 → 112.0 (+8.2)
      - **Flickr30k**:
        - BLEU@4: 26.9 → 28.2 (+1.3)
        - CIDEr: 61.3 → 65.8 (+4.5)
      - **Cross-Domain** (COCO→Flickr30k):
        - CIDEr: 45.5 → 49.5 (+4.0)
      - **NoCaps** (out-of-domain): Entire CIDEr 70.5 → 72.7 (+2.2)
      - **Consistency**: Improvements across all settings (in-domain, cross-domain, out-of-domain)
  - **Ablation Studies**:
      - **vs. Traditional Pruning Methods**: SynC surpasses filtering-only methods (avoids computational cost and fairness issues)
      - **K Value Impact**: K=15 achieves optimal balance
      - **τ Threshold**: Keeping top 80-90% pairs most effective
  - **Open Source**: ✅ [GitHub](https://github.com/boreng0817/SynC)
  - **Institution**: Hanyang University + CJ Group
  - **Publication**: arXiv July 2025
  - **Significance**:
      - **Novel Synthetic Data Refinement**: First method specifically designed for "clean caption + noisy image" scenario
      - **Leverages Pre-existing Resources**: Reassigns from image pool, avoiding regeneration cost
      - **Cycle-Consistency**: Bidirectional retrieval ensures fine-grained alignment
      - **Strong Generalization**: Simple, model-agnostic, broadly applicable
      - **Practical Impact**: Efficient, effective approach readily integrated into existing ZIC pipelines
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2510.27164">📄 High-Res Captioning</a></b><br>
<code>arXiv 2510.27164</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
</summary>

  - **Focus**: **High-Resolution Image Accurate and Detailed Caption Generation** - Training-free pipeline combining VLM + LLM + object detection systems to overcome VLM low-resolution pre-training detail loss
  - **Data Synthesis Method** - **Four-Stage Caption Refinement Pipeline**:
      - **Core Innovation**: Through "progressive visual zoom-in" strategy and multi-stage verification, generates more detailed, reliable high-resolution image captions while reducing hallucinations
      - **Stage 1: Initial Caption Generation**:
        - **VLM Generation**: Use VLM (InstructBLIP/LLaVA-v1.5/Qwen2-VL) to generate initial caption
        - **Prompt**: "Describe this image in detail."
        - **Problem**: VLMs typically pre-trained at low resolution (224×224, 336×336), losing fine details when downsampling high-resolution images
        - **LLM Keyword Extraction**: Use GPT-4o to extract keyword list from initial caption
      - **Stage 2: Identify Potentially Missing Objects**:
        - **LLM Reasoning**: Based on keywords, LLM infers using world knowledge potentially co-occurring but missed objects
        - **Example**: If keywords include "table, chair", LLM infers potential "lamp, books, cup"
        - **Output**: Expanded candidate object list (original + inferred)
      - **Stage 3: Object Detection Ensemble Verification**:
        - **Detector Ensemble**: GroundingDINO + YOLO-World + OWLv2
        - **Verification Process**:
          - Each object checked: If detected by any model (confidence ≥0.5, IoU ≥0.7) considered same object
          - Object undetected: Any detector fails to detect → remove from initial caption (eliminates hallucinations)
        - **Output**: Verified object list + high-confidence bounding boxes
      - **Stage 4: Final Caption Generation**:
        - **Re-prompt VLM**: Use detected object list + bounding boxes to re-prompt VLM
        - **GPT-4o Integration**: Integrate (1) initial caption, (2) verified object list with spatial coordinates, (3) new detailed descriptions
        - **Final Output**: Single, coherent, contextually rich enhanced caption
      - **Key Technical Advantages**:
        - **Training-Free**: No VLM retraining required, flexible VLM model choice
        - **Multi-Stage Verification**: LLM reasoning + detector ensemble ensures accuracy
        - **Hallucination Reduction**: Detection verification effectively removes false objects
        - **High-Resolution Applicable**: Maintains detail recognition in 4K+ images
  - **Data Scale & Experimental Setup**:
      - **Image Source**: Filter 4K resolution (3840×2160 pixels) images from Objects365 dataset
      - **Evaluation Benchmarks**: CHAIR (hallucination), POPE (hallucination), GPT-4o scoring (quality)
  - **Experimental Results** - **Significant Improvements in Caption Quality and Hallucination Reduction**:
      - **CHAIR Metric** (Caption Quality):
        - InstructBLIP: 0.6333 → 0.6952 (+9.59%)
        - LLaVA-v1.5: 0.6785 → 0.7304 (+7.66%)
        - Qwen2-VL: 0.8260 → 0.8398 (+1.68%)
      - **POPE Benchmark** (Hallucination Evaluation):
        - **Random Sampling** (InstructBLIP): F1 Score 0.1484 → 0.2153 (+45.10%)
        - **Popular Sampling** (InstructBLIP): F1 Score 0.1732 → 0.2229 (+28.85%)
        - **Adversarial Sampling** (InstructBLIP): F1 Score 0.1662 → 0.2141 (+28.82%)
      - **GPT-4o Quality Scoring**: Substantial improvements in detail richness and factual accuracy
  - **Ablation Studies**:
      - **Impact of Each Stage**: Each refinement stage contributes incremental quality improvements
      - **Detector Ensemble vs. Single Detector**: Ensemble consistently outperforms single detector by 5-8%
      - **LLM Reasoning Contribution**: Identifying missing objects increases recall by 12-15%
  - **Open Source**: ⚠️ Code/model release status not explicitly mentioned in paper
  - **Institution**: Not explicitly stated (academic research)
  - **Publication**: arXiv October 2025
  - **Significance**:
      - **Training-Free Solution**: Practical approach requiring no model retraining
      - **Multi-Stage Verification**: Systematic pipeline ensuring caption accuracy
      - **Hallucination Mitigation**: Significant reduction in false object mentions
      - **High-Resolution Focus**: Addresses critical gap in VLM caption quality for high-res images
      - **Modular Design**: Each component replaceable, allowing flexible implementation
  
  
  
  #### 🤖 VLM/LLM-based Synthetic Text Generation
  
  > Following papers explicitly describe how to use large models to generate synthetic captions/dialogues for images
  

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
<img src="https://img.shields.io/badge/Institution-Fudan_University-red?style=flat-square"/>
</summary>

  - **Focus**: **Any-to-Any Multimodal Language Model** - Unified processing and generation across speech, text, images, and music using discrete representations
  - **Data Synthesis Method** - **Two-Stage Fully Synthetic Any-to-Any Multimodal Dialogue Pipeline**:
      - **Core Innovation**: First any-to-any multimodal LLM using discrete representations, with fully synthetic multimodal dialogue data (AnyInstruct-108k) without needing paired multimodal data
      - **Problem Identification**:
        - Existing multimodal models typically support only specific modality combinations (e.g., image+text), lacking unified any-to-any capabilities
        - Difficult to obtain large-scale paired multimodal dialogue data covering all modality combinations
        - Complex model architectures requiring modality-specific encoders/decoders limit scalability
      - **Discrete Representation Approach**:
        - **Speech**: Pre-trained SpeechTokenizer converts speech to discrete tokens
        - **Images**: Pre-trained SEED tokenizer converts images to discrete tokens
        - **Music**: Pre-trained Encodec converts music to discrete tokens
        - **Text**: Standard text tokenization
        - **Advantage**: All modalities represented as discrete token sequences, enabling LLM to process and generate any modality uniformly
      - **Two-Stage Data Construction Pipeline**:
        1. **Multimodal Alignment Pre-training**:
           - **Data Collection**: Collect text-centric multimodal data from internet (images, audio, music paired with text descriptions)
           - **Format Conversion**: Convert all modalities to discrete tokens, interleave with text
           - **Scale**: Large-scale alignment data for basic multimodal understanding
           - **Purpose**: Enable LLM to understand correlations between different modality tokens
        2. **Any-to-Any Multimodal Instruction Tuning - AnyInstruct-108k**:
           - **Fully Synthetic Data Generation (Key Innovation)**:
             - **Step 1: Text-based Conversation Generation**:
               - Use GPT-4 to generate text-only multi-turn conversations covering various scenarios
               - Conversations include placeholders for multimodal elements (e.g., "[IMAGE]", "[MUSIC]", "[SPEECH]")
               - Topics cover: daily dialogue, creative scenarios, educational content, entertainment, etc.
             - **Step 2: Modality Content Generation**:
               - For IMAGE placeholders: Use SDXL (Stable Diffusion XL) to generate images based on GPT-4 descriptions
               - For MUSIC placeholders: Use MusicGen to generate music based on GPT-4 descriptions
               - For SPEECH placeholders: Use Azure TTS to synthesize speech from text
             - **Step 3: Convert to Discrete Tokens**:
               - Convert all generated images, music, speech to discrete tokens
               - Replace placeholders in conversations with actual discrete token sequences
             - **Step 4: Quality Filtering**:
               - Remove conversations with generation failures
               - Ensure all modality contents match conversation context
               - Verify conversation coherence and naturalness
           - **Data Characteristics**:
             - **108K samples**: 108K multi-turn multimodal conversations
             - **Multi-turn**: Average 3-5 turns per conversation
             - **Any-to-Any**: Covers all possible input-output modality combinations
             - **Modality Interleaving**: Each conversation can contain multiple modality switchings
             - **Task Diversity**: Question answering, content generation, modality conversion, creative tasks, etc.
      - **Key Technical Advantages**:
        - **Unified Architecture**: No need for modality-specific encoders/decoders, only requires discrete tokenizers
        - **Fully Synthetic**: No need for expensive paired multimodal data collection
        - **Flexible Scalability**: New modalities can be easily integrated by adding new tokenizers
        - **Any-to-Any Capability**: Supports arbitrary input-output modality combinations
        - **Standard LLM Training**: Uses standard language model training without architectural modifications
  - **AnyGPT Model**:
      - **Base Model**: Vicuna-7B or Vicuna-13B
      - **Training Stages**:
        - Stage 1: Multimodal alignment pre-training
        - Stage 2: AnyInstruct-108k instruction tuning
      - **Inference**: Auto-regressive generation of discrete tokens, then convert back to corresponding modalities
  - **Experimental Results** - **Achieves comparable performance to specialized models across all modalities**:
      - **Text Understanding**: Comparable to LLaMA-based models
      - **Image Understanding**: Comparable to BLIP-2, LLaVA on image captioning and VQA
      - **Speech Recognition**: Comparable to Whisper on ASR tasks
      - **Music Understanding**: Novel capability, no direct comparison
      - **Any-to-Any Tasks**: Demonstrates flexible modality conversion capabilities (e.g., image-to-music, speech-to-image)
      - **Multi-turn Dialogue**: Supports coherent multi-turn multimodal conversations
  - **Key Innovation Analysis**:
      - **Discrete Representation Advantage**: Unifies all modalities within single LLM, avoiding complex fusion modules
      - **Synthetic Data Pipeline**: Fully automated data generation reduces manual annotation costs
      - **Scalability**: Framework easily extensible to new modalities (e.g., video, 3D)
      - **Training Efficiency**: Reuses existing LLM training infrastructure without architectural changes
  - **Limitations**:
      - **Token Sequence Length**: Discrete representation significantly increases token sequence length, limiting long-context handling
      - **Generation Quality**: Quality of generated non-text modalities depends on quality of discrete tokenizers
      - **Computational Cost**: Processing multiple modalities requires substantial computational resources
  - **Institution**: Fudan University
  - **Authors**: Jun Zhan, Junqi Dai, Jiasheng Ye, Yunhua Zhou, Dong Zhang, Zhigeng Liu, Xin Zhang, Ruibin Yuan, Ge Zhang, Linyang Li, Hang Yan, Jie Fu, Tao Gui, Tianxiang Sun, Yugang Jiang, Xipeng Qiu
  - **Publication**: arXiv February 2024 (v2)
  - **Paper Link**: [arXiv:2402.12226](https://arxiv.org/abs/2402.12226)
  - **Open Source**: ✅ [GitHub](https://github.com/OpenMOSS/AnyGPT)
  - **Dataset**: AnyInstruct-108k
  - **Significance**:
      - **Any-to-Any Pioneer**: First work demonstrating truly unified any-to-any multimodal LLM using only discrete representations
      - **Synthetic Data Innovation**: Proves fully synthetic multimodal dialogue data can effectively train any-to-any models
      - **Simplified Architecture**: Shows complex multimodal fusion modules unnecessary when using appropriate discrete representations
      - **Research Inspiration**: Opens new research direction for unified multimodal models
  

</details>
---

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2403.03194">📄 MAGID</a></b><br>
<code>arXiv 2403.03194</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Automatic Multimodal Dialogue Data Generation** - Automatically augments text-only dialogues into multimodal dialogues (text + images)
  - **Problem Background**:
      - **Existing Method Limitations**: Retrieval-based methods (retrieve from fixed image libraries) lead to limited image diversity and low matching quality
      - **Data Scarcity**: Multimodal dialogue data difficult to obtain, with serious privacy and quality issues
      - **Single-Image Limitation**: Existing datasets typically contain only one image per dialogue
  - **Data Synthesis Method** - **Generative Multimodal Dialogue Pipeline + Quality Assurance Module**:
      - **Core Innovation**: Starting from text-only dialogues, uses LLM to identify utterances requiring images, uses diffusion models to generate images, with feedback loop ensuring quality
      - **Three Core Modules**:
        1. **LLM-based Scanner**:
           - **Task**: Identifies utterances in dialogues requiring images and generates image descriptions
           - **Input**: Text-only dialogue
           - **Output**: Selected utterances + corresponding image descriptions
           - **Prompt Engineering**: Tests three strategies
             - **Zero-shot**: Provides only format and problem description
             - **Few-shot**: Provides input-output examples
             - **Chain-of-Thought (CoT)**: Provides reasoning steps (optimal choice)
           - **Output Format Control**: Uses HTML-like tags (`<result>` and `<reason>`) for structured output
           - **Key Point**: CoT provides debuggable reasoning paths, avoids context inconsistencies (e.g., "give it a look" generating meaningless images)
        2. **Diffusion-based Image Generator**:
           - **Model Selection**: Stable Diffusion XL 1.0 (SDXL)
           - **Advantages**: Trained on billions of images, generates diverse, high-quality images
           - **Input**: LLM-generated image descriptions
           - **Output**: Synthetic images
           - **Key Point**: Transcends diversity bottleneck of retrieval-based methods
        3. **Quality Assurance Module**:
           - **Three Evaluation Dimensions**:
             a) **Image-Text Matching**:
                - Uses CLIP score to verify image-utterance matching quality
                - Low scores trigger regeneration (up to 2 times)
             b) **Image Quality**:
                - Uses aesthetic score (CLIP embedding + MLP based)
                - Detects diffusion model artifacts
                - Threshold: 0.51 (effectively detects most artifacts)
             c) **Image Safety**:
                - NSFW content detection
                - Dataset finds very few unsafe images, validating pipeline reliability
           - **Feedback Loop**: If image fails to meet standards, returns to LLM to regenerate image description
      - **Key Technical Advantages**:
        - **Generative not Retrieval-based**: Image diversity not limited by library size
        - **Automated**: Fully automated pipeline, no manual annotation required
        - **Quality Assurance**: Multi-dimensional quality control ensures data usability
        - **Multi-Image Support**: No limit to one image per dialogue
        - **Privacy-Friendly**: Does not rely on real user data
  - **Data Scale**:
      - **MAGID Dataset**: Medium-sized dataset (paper as proof-of-concept)
      - **Source**: Text-only dialogue datasets (e.g., DailyDialog, etc.)
  - **Experimental Results** - **Automated and Human Evaluation**:
      - **Quantitative Evaluation**:
        - Compares with SOTA baselines on 3 dialogue datasets
        - Uses automatic metrics (CLIP score, FID, etc.)
      - **Human Evaluation**:
        - MAGID significantly outperforms retrieval-based baselines (especially with small image libraries)
        - High image-dialogue consistency scores
        - High scores for image quality and diversity
      - **Ablation Studies**:
        - CoT prompting outperforms zero-shot and few-shot
        - Quality assurance module critical for final data quality
        - Feedback loop effectively improves image-text alignment
  - **Publication**: arXiv March 2024
  - **Institution**: AWS AI Labs, University of Waterloo
  - **Authors**: Hossein Aboutalebi, Hwanjun Song, Yusheng Xie, Arshit Gupta, et al.
  - **Open Source**: ✅ [Code](https://github.com/amazon-science/MAGID)
  - **Significance**:
      - **Paradigm Shift**: From retrieval-based to generative multimodal dialogue data construction
      - **Quality Assurance Design**: Systematic design of multi-dimensional quality control + feedback loop
      - **Addresses Practical Challenges**: Tackles three major challenges of privacy, diversity, and quality
      - **Scalability**: Automated pipeline easy to scale to large scale
      - **Multi-Image Dialogues**: Supports multiple images per conversation, closer to real scenarios
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2412.14475">📄 MegaPairs</a></b><br>
<code>arXiv 2412.14475</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Large-Scale Data Synthesis for Universal Multimodal Retrieval** - Scalable multimodal retrieval training data construction via heterogeneous KNN triplets and open-ended instruction generation
  - **Data Synthesis Method** - **Heterogeneous Similarity Mining + MLLM/LLM Annotation Pipeline**:
      - **Core Innovation**: Uses **multiple similarity models** to mine diverse image pairs from open-domain image corpora, paired with MLLM/LLM generated open-ended retrieval instructions
      - **Two-Stage Pipeline**:
        1. **Heterogeneous Image Pair Mining** (diversity key):
           - **Three Types of Similarity Models in Parallel**:
             - a) **Visual-Semantic Correlation** (EVA-CLIP image encoder): Captures semantic correlation regardless of visual similarity (e.g., different views of same car)
             - b) **Visual-Pattern Correlation** (DINOv2): Captures visual similarity regardless of semantic correlation (e.g., different cars in similar backgrounds)
             - c) **Caption Correlation** (EVA-CLIP text encoder): Based on textual similarity between image captions
           - **Similarity Filtering**: Keeps pairs with scores in (0.8, 0.96) range, eliminates weak associations and near-duplicates
           - **Hard Negatives**: Automatically introduces hard negative samples from retrieval set (other retrieved non-target images)
           - **Scale**: Mines relationships from 20M image subset of RecapDataComp-1B
        2. **Open-Ended Instruction Generation** (based on MLLM/LLM):
           - **Relationship Description Generation** (InternVL2-26B):
             - Takes image pair (Iq, Iti) as input
             - MLLM generates detailed description Di explaining commonalities and differences between images
             - Captures visual and semantic relationships
           - **Instruction Synthesis** (LLaMA3-8B):
             - LLM generates diverse textual instructions Tq→ti based on description Di
             - At least 3 different instructions per image pair
             - Instructions designed as open-ended search queries (e.g., "show interior of this car")
           - **Final Triplets**: (Iq, Tq→ti, Iti) + 5 hard negatives
      - **Key Advantages**:
        - **Scalability**: Leverages general image corpora (not reliant on multi-image webpages), infinitely scalable
        - **Quality Assurance**: Similarity filtering + MLLM/LLM annotation ensures high quality
        - **Diversity**: Three types of heterogeneous similarity introduce different image relationship types
        - **Low Cost**: Uses open-source MLLM/LLM (InternVL2-26B, LLaMA3-8B)
  - **Data Scale**:
      - **MegaPairs**: 26.235M image pairs
      - **Source Corpus**: 20M image subset from RecapDataComp-1B
      - **Instruction Diversity**: At least 3 instructions per pair
      - **Hard Negatives**: 5 hard negatives per query
  - **Models**: **MMRet Series** - Universal multimodal retrievers trained on MegaPairs
      - **MMRet-Base**: CLIP-B architecture (149M parameters)
      - **MMRet-Large**: CLIP-L architecture (428M parameters)
      - **MMRet-MLLM**: LLaVA-1.6 Mistral 7B architecture (7.57B parameters)
  - **Experimental Results** - **SOTA Zero-Shot Performance**:
      - **Composed Image Retrieval (CIR) Benchmarks** (4 mainstream benchmarks):
        - **CIRCO** (main benchmark):
          - MMRet-MLLM: **42.2% mAP@5** (surpasses previous SOTA CoCa-based MagicLens-L 34.1%, **+8.1%**)
          - MMRet-Large: **39.2% mAP@5** (CLIP-L scale SOTA)
          - MMRet-Base: **34.3% mAP@5** (outperforms most larger models)
        - **CIRR Test Set**:
          - MMRet-MLLM: **46.7% R@1, 75.4% Rs@1** (surpasses SOTA **+7.4% R@1, +4.5% Rs@1**)
          - MMRet-Large: **38.0% R@1** (CLIP-L scale SOTA)
        - **FashionIQ**: MMRet-MLLM **35.6% R@10**
        - **GeneCIS**: MMRet-MLLM **21.1% Rs@1** (surpasses SOTA **+3.7%**)
      - **MMEB Benchmark** (36 datasets, 4 meta-tasks):
        - **Zero-Shot Overall**: MMRet-MLLM **44.0%** (SOTA, surpasses UniIR 42.8%)
        - **Classification**: 47.2%
        - **VQA**: 18.4%
        - **Retrieval**: 56.5% (significantly better than other methods)
        - **Visual Grounding**: 62.2%
      - **Supervised Fine-Tuning Performance** (MMEB):
        - **Overall**: **64.1%** (surpasses VLM2Vec Phi-3.5-V 60.1%)
        - **IND Datasets**: 68.0%
        - **OOD Datasets**: 59.1% (strong generalization, surpasses VLM2Vec LLaVA-1.6 **+7.1%**)
  - **Data Quality Validation**:
      - **Data Efficiency**: Just **500K MegaPairs samples** outperform MagicLens trained on **36.7M data** (**1/70 data size**)
      - **Scalability**: Performance continues to improve with data scale (from 128K to 26M)
      - **Heterogeneous Strategy Effect**: Using all three similarity types outperforms single strategy (ablation study validated)
      - **Hard Negative Importance**: Including hard negatives significantly improves performance (+5-10% across benchmarks)
  - **Publication**: arXiv December 2024
  - **Institution**: Beijing University of Posts and Telecommunications, Beijing Academy of Artificial Intelligence, USTC, Shanghai Jiao Tong University, Hong Kong Polytechnic University
  - **Authors**: Junjie Zhou, Zheng Liu, Ze Liu, Shitao Xiao, et al.
  - **Open Source**: ✅ **Fully Open-Source** - Dataset, models, and data synthesis pipeline will all be publicly available
  - **Significance**:
      - **Breakthrough Data Bottleneck**: First to achieve large-scale multimodal retrieval data synthesis from general image corpora
      - **Quality Over Scale**: Demonstrates high-quality synthetic data is more effective than large-scale low-quality data
      - **Heterogeneous Similarity Innovation**: Multi-type similarity mining introduces diverse image relationships
      - **Open-Source Ecosystem Contribution**: Complete open-sourcing of data, models, pipeline to advance the field
      - **Universal Retrieval Capability**: Achieves SOTA on both CIR and broad multimodal tasks
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2410.11963">📄 CtrlSynth</a></b><br>
<code>arXiv 2410.11963</code>
<img src="https://img.shields.io/badge/Method-✓-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Focus**: **Controllable Image-Text Synthesis Pipeline** - Fine-grained controllable multimodal data generation via visual tag decomposition-recomposition
  - **Data Synthesis Method** - **Decompose-Recompose Paradigm for Controllable Data Synthesis**:
      - **Core Innovation**: Decompose image semantics into basic elements (objects, attributes, relations), manipulate via user-defined control policies, then recompose to generate synthetic data
      - **Three Core Components**:
        1. **Vision Tagging Model (VTM)**:
           - Extracts basic visual elements from images (**visual tags**)
           - **Objects & Attributes**: Multi-label classifier (CatLIP-Huge) + top-20 classes via sigmoid prediction
           - **Relations**: Multimodal captioning model (Florence-large) generates detailed descriptions + LLM (Qwen2-7B) extracts relations
           - **Hybrid Approach**: Combines CatLIP object/attribute predictions with Florence+LLM relation extraction for comprehensive visual tag set
        2. **Text Controller**:
           - Takes visual tags + user policy + optional original text
           - Generates text synthesis instructions to guide LLM
           - **Three Predefined Policy Types**:
             - a) **Edit Visual Tags** (remove, add, replace) for fine-grained content control
             - b) **Constrain Semantic Meaning** to improve fidelity of noisy captions
             - c) **Stylize Output** (e.g., JSON format) for enhanced downstream usability
           - **10 text control policies** for caption synthesis (see paper Appendix A.1)
        3. **Image Controller**:
           - Takes text prompts + user policy
           - Outputs image synthesis instructions to guide diffusion models
           - **Two Policy Types**:
             - Tag weighting adjustments (emphasize specific objects/attributes)
             - Style prompts (cinematic, realistic, artistic)
      - **Flexible Synthesis Paths** (supports 4 main paths):
        - **SP(1) Image→Text**: Original image → VTM → visual tags → text controller → LLM → synthetic text
        - **SP(2) Image+Original Text→Improved Text**: Includes original caption as constraint, generates faithful improved text
        - **SP(3) Image→Text+Image**: Generate text → image controller → diffusion model → synthetic image+text pair
        - **SP(4) Text→Image**: Original text → image controller → diffusion model → synthetic image
      - **Closed-Loop Self-Filtering**:
        - **Quality Validation**: Checks if synthetic text contains at least pf fraction of visual tags (default 20%)
        - **Image Validation**: Synthetic images re-processed through VTM to extract tags, verified against source text alignment
        - **Advantage**: Automatic filtering of low-quality samples without manual rules
      - **Key Technical Advantages**:
        - **Fine-grained Controllability**: Precise data synthesis via tag-level manipulation
        - **Training-Free**: Fully leverages pretrained models (LLM, diffusion models) without additional training
        - **Modular**: Easy to swap LLM, diffusion model, or VTM components
        - **Closed-Loop Design**: Automatic quality verification and filtering capabilities
  - **Data Scale**:
      - **CC3M Synthetic Data**:
        - CtrlSynth-cap: 2.6M captions (filtered from 2.8M original)
        - CtrlSynth-img: 2.4M images
        - CtrlSynth-mix: 5.1M image-text pairs (mixing cap+capimg)
      - **CC12M Synthetic Data**:
        - CtrlSynth-cap: 10.2M captions (from 11.3M original)
        - CtrlSynth-img: 9.5M images
        - CtrlSynth-mix: 19.7M image-text pairs
  - **Experimental Results** - **Comprehensive Evaluation on CLIP Pretraining**:
      - **Zero-Shot Classification** (31 datasets):
        - CC3M training: Average accuracy from 19.4% to **27.1% (+7.7%)**
        - CC12M training: From 33.9% to **36.6% (+2.5%)**
        - ImageNet variants: From 11.3% to **20.7% (+9.4%)** [CC3M]
      - **Image-Text Retrieval** (COCO, Flickr30k):
        - CC3M training: recall@1 from 13.7% to **37.1% (+23.4%)**
        - Flickr I2T: From 21.3% to **57.3% (+36%)**
        - CC12M training: recall@1 from 45.4% to **54.4% (+9.0%)**
      - **Compositional Reasoning** (SugarCrepe benchmark):
        - CC3M training: From 64.0% to **68.5% (+4.5%)**
        - CC12M training: From 72.3% to **75.3% (+3.0%)**
        - **Notable Gains**: REPLACE relation +4.3%, SWAP attribute +14.8%
      - **Long-Tail Task Performance**:
        - **ImageNet-LT**: Tail class accuracy +21.3%, overall +5.4%
        - **Places-LT**: Tail class accuracy +16.2%, overall +3.7%
      - **Comparison with Prior Work**:
        - Outperforms **VeCLIP**: +4.8% average on VTAB, +7.9% on ImageNet 1K
        - Outperforms **LaCLIP**: +3.4% average on 15 datasets, +2.3% on ImageNet 1K
  - **Ablation Study Key Findings**:
      - **Importance of Visual Relations**: Including relation tags improves compositional reasoning by 4% over objects/attributes only
      - **LLM Comparison**: Mistral-NeMo outperforms Qwen2-7B (+3% SugarCrepe)
      - **Filtering Threshold**: 20% achieves optimal performance balance (stable in 10%-30% range)
      - **Mixing Ratio**: 50% synthetic data reaches best gains, diminishing returns at higher ratios
      - **Data Efficiency**: Synthetic data improves CLIP training efficiency by 40% (iterations needed to reach 20% accuracy)
  - **Synthetic Quality Analysis**:
      - **Text Length**: Synthetic captions average 60 words vs original 8 words
      - **Information Density**: Contains richer visual details and relationship descriptions
      - **Diversity**: Control policies generate diverse phrasings
  - **Publication**: arXiv October 2024
  - **Institution**: Apple, Meta
  - **Authors**: Qingqing Cao, Mahyar Najibi, Sachin Mehta
  - **Open Source**: ⚠️ Paper does not explicitly mention dataset/code release status
  - **Significance**:
      - **First Controllable Image-Text Synthesis System**: Provides fine-grained control vs black-box generation
      - **Decompose-Recompose Paradigm**: Innovative visual semantics manipulation approach
      - **Closed-Loop Self-Verification**: No manual filtering rule design needed
      - **Cross-Task Generalization**: Comprehensive improvements across classification, retrieval, compositional reasoning, and long-tail tasks
      - **Data Efficiency**: Demonstrates sample efficiency of synthetic data over pure real data scaling
  

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

  - **Focus**: **Hyper-Detailed Image Descriptions** - Human-in-the-loop framework combining VLM generation with sequential human enhancement and active learning to produce hyper-detailed image descriptions
  - **Data Synthesis Method** - **Seeded Annotation + Sequential Augmentation + Active Learning**:
      - **Core Innovation**: Combines **VLM-generated meta-elements** with **human annotator iterative refinement**, producing hyper-detailed image descriptions through sequential augmentation and active learning loops
      - **Annotation Framework**:
        1. **Task 1: Object-Level (Fine-grained element annotation)**:
           - **Input**: Image + Object Detection (OD) model-generated (label, bbox)
           - **VLM Seeding**: Use PaLI-35B to generate short caption for each bbox
           - **Human Enhancement**: Annotators add, delete, merge, and refine annotations on panels
           - **Output**: (label, bbox, detailed description) triplets, describing objects thoroughly
        2. **Task 2: Image-Level (Full-image descriptions)**:
           - **Input**: Task 1 multi-element output + VLM-generated full-image caption + optional domain-specific metadata (e.g., art style)
           - **Sequential Augmentation**: Annotators iteratively enhance and improve descriptions (typically 3 rounds)
           - **Active Learning**: Every 1K samples collected, use accumulated data to fine-tune PaLI-35B for better seed generation
           - **Output**: 217.2 tokens average length hyper-detailed descriptions
      - **Sequential Augmentation Benefits** (Fig. 2):
        - **Efficiency Gains**: 3 sequential annotators vs unordered
          - **Token Count**: +20% token count growth (170→204 words)
          - **Time Saving**: -30% time (from 800→560 sec/annotator)
          - **Inter-Annotator Agreement**: Jaccard similarity from 0.2 rises to 0.65 (round 1-2 and round 2-3)
        - **Implicit Learning Loop**: Annotators learn from each other's perspectives across rounds
      - **Active Learning Loop**:
        - **Initial PaLI**: Average ~15 word captions
        - **After 3K Samples**: Generates 150+ word captions
        - **Key Mechanism**: Gradually reduces human annotation burden
      - **Annotation Guidelines** (detailed in Appendix A):
        - **TLDR Principle**: Start with newspaper article-style brief summary
        - **Importance Order**: Describe by importance order, not left-to-right order
        - **Visual Precision**: Focus on visually determinable details, avoid speculation
        - **Comprehensive Coverage**: Include background, colors, textures, angles, text, rendering style
        - **Special Focus**: Describe people's clothing, brand logos, specific attributes, etc.
      - **Key Technical Advantages**:
        - **Seeded Annotation**: Lower annotation cost and time by starting from VLM baseline
        - **Sequential Augmentation**: More efficient than parallel annotation while achieving consistency
        - **Active Learning**: Continuously improves VLM to approach human annotation quality
        - **Quality Verification**: Token count + n-gram Jaccard similarity ensure consistency
  - **Data Scale**:
      - **IIW Dataset**: 9,018 images (Train: 8,573, Test: 445)
      - **Average Statistics**:
        - **Tokens**: 217.2 (vs DOCCI 135.7, DCI 148.0)
        - **Sentences**: 9.8
        - **Nouns**: 52.5 (vs DOCCI 34.0, DCI 35.3)
        - **Adjectives**: 28.0 (vs DOCCI 16.6, DCI 16.3)
        - **Verbs**: 19.1 (vs DOCCI 9.6, DCI 10.5)
      - **Image Source**: WebLI-like dataset crawl
      - **Annotators**: 20+ domain experts (creative writing, art history, photography, etc.)
  - **Experimental Results** - **Human SxS and Downstream Application Validation**:
      - **IIW Human Annotations vs Prior Datasets** (Table 2):
        - **vs DCI (112 samples)**:
          - Comprehensiveness: +61%
          - Specificity: +80%
          - Hallucinations: -42%
          - TLDR Quality: +91%
          - Human-Likeness: +82%
        - **vs DOCCI (100 samples)**:
          - Comprehensiveness: +42%
          - Specificity: +82%
          - Hallucinations: -35%
          - TLDR Quality: +79%
          - Human-Likeness: +68%
        - **Average Win**: +66% (average across 5 metrics vs prior datasets)
      - **IIW Human Annotations vs GPT-4V** (Table 3 right):
        - **100 Sample Comparison**:
          - Comprehensiveness: +35%
          - Specificity: +53%
          - Hallucinations: -59%
          - TLDR Quality: +70%
          - Human-Likeness: +21%
        - **Average Win**: +48%
      - **IIW Model (fine-tuned PaLI-35B) vs Prior Dataset Models** (Table 3 left):
        - **vs DCI Model**: +42% Comprehensiveness, +54% Specificity, +51% TLDR
        - **vs DOCCI Model**: +4% Comprehensiveness, +37% Specificity, +57% TLDR
        - **Average Win**: +31% (average across 5 metrics vs prior dataset-trained models)
  - **Downstream Applications**:
      - **Text-to-Image Reconstruction** (Table 4, 240 LocNar images):
        - Use Imagen model, human evaluation on generated candidates (S1, S1-2, S1-3...)
        - **Mean Rank**: IIW 1.63 vs DOCCI 1.74 vs DCI 2.05 (**rank 1**)
        - **CLIP Similarity**: IIW 0.861 vs DOCCI 0.853 vs DCI 0.844 (**highest**)
        - **Key Finding**: Even using only 1 sentence, IIW still outperforms prior datasets
      - **Compositional Reasoning** (Table 5, LLM-only setting):
        - Replace images in ARO/SVO-Probes/Winoground with IIW descriptions for LLM judgment
        - **ARO VG-Attribution**: 90.37% (vs InstructBLIP 83.99%, LLaVA 84.80%, **+6%**)
        - **ARO VG-Relation**: 66.19% (vs InstructBLIP 62.73%, LLaVA 63.71%, **+2-3%**)
        - **Winoground**: 69.38% (vs InstructBLIP 65.25%, LLaVA 63.38%, **+4-6%**)
  - **IIW-Eval Benchmark** (Table 6):
      - **2,612 Images** + **1,899 object-level annotations** + **2,712 image-level annotations**
      - **412 Human SxS Labels** (IIW vs DCI, IIW vs DOCCI)
      - **IIW-400**: 400 quality sample set + DCI subset (112) + DOCCI subset (100)
      - **Model-Enriched Datasets**: LocNar (1,000) + XM3600 (1,000) re-annotated using IIW model
  - **Ablation Study Key Findings**:
      - **Seeded Annotation Importance** (Table 7): Seeded vs from-scratch = +54% Comprehensiveness, +48% Specificity
      - **IIW Human vs IIW Model** (Table 8, 100 samples): Human still better (+78% Compr., +91% Spec.)
      - **Sequential Rounds**: 3 rounds reach 0.8 similarity threshold, far superior to prior datasets
  - **Publication**: ECCV 2024 | arXiv May 2024 (v2: October 2024)
  - **Institution**: Google DeepMind, Google Research, University of Washington
  - **Authors**: Roopal Garg, Andrea Burns, Burcu Karagol Ayan, Yonatan Bitton, et al.
  - **Open Source**: ✅ **Fully Open-Source** - IIW-Eval benchmark (2.6K images), Human SxS labels, Model-enriched LocNar+XM3600 data
  - **Project Page**: [github.com/google/imageinwords](https://github.com/google/imageinwords)
  - **Significance**:
      - **Pioneering Human-AI Collaboration**: First systematic combination of VLM generation with human iteration for hyper-detailed description generation framework
      - **Sequential Augmentation Breakthrough**: Proves sequential annotation achieves efficiency + quality dual win
      - **Active Learning Loop**: Demonstrates continuous collection data improves model in feedback loop
      - **TLDR Principle**: Introduces newspaper lead-sentence summarization as new paradigm for long descriptions
      - **Comprehensive Benchmark**: IIW-Eval provides multi-dimensional evaluation metrics driving future research
      - **Downstream Validation**: T2I reconstruction and compositional reasoning prove practical value
      - **Quality Leadership**: Surpasses prior datasets in comprehensiveness, specificity, reduced hallucinations across board SOTA
  
  #### 🧠 Spatial Reasoning Enhancement
  

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
  
  #### 🔄 Continual Learning & Catastrophic Forgetting Mitigation
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2503.04229">📄 GIFT</a></b><br>
<code>arXiv 2503.04229</code>
</summary>

  - **Data Synthesis Method** - **Stable Diffusion-based Synthetic Data for VLM Continual Learning**:
      - **Core Innovation**: First framework using diffusion-generated synthetic data to mitigate catastrophic forgetting in Vision-Language Models during continual fine-tuning
      - **Dual Forgetting Challenge**: Addresses both downstream task forgetting AND pre-training knowledge degradation in VLMs - a unique multi-modal CL challenge
      - **Synthetic Data Recreation**: Uses Stable Diffusion to recreate both pre-training approximations (ImageNet class names) and historical downstream task data without storage/privacy issues
      - **Data Scale**: 1K synthetic images per task achieves superior performance vs. 100K real ImageNet images, demonstrating synthetic data efficiency
  - **Key Technical Components**:
      - **Class Buffer Pool Strategy**: Maintains P = ∪C_i storing all encountered class names; samples from diverse pool to generate approximated pre-training + downstream data
      - **Contrastive Distillation Loss**: Aligns current model θ_t with previous model θ_{t-1} on synthetic image-text pairs using image-text matching objective consistent with CLIP pre-training
      - **Image-Text Alignment Constraint**: Corrects teacher model errors by enforcing KL divergence between identity matrix and contrastive similarity matrix as hard target
      - **Adaptive Weight Consolidation (AWC)**: Dynamic Fisher information calculation from synthetic data during training (not static like EWC), enabling real-time parameter importance adjustment
  - **Experimental Framework**:
      - **MTIL Benchmark**: 11 datasets (Aircraft, Caltech101, CIFAR100, DTD, EuroSAT, Flowers, Food, MNIST, OxfordPet, StanfordCars, SUN397) with 1,201 classes across diverse domains
      - **Two Task Orders**: Alphabetical (Order I) and random (Order II) arrangements introducing different domain shift challenges
      - **Comprehensive Metrics**: Transfer (zero-shot capability preservation), Last (downstream task retention), Avg. (stability-plasticity balance)
  - **Experimental Results**:
      - **MTIL Order I**: Transfer 69.3% (+8.3% vs l2 baseline), Avg. 77.3% (+14.6%), Last 86.0% (+10.1%) - achieves new SOTA across all metrics
      - **MTIL Order II**: Transfer 65.9% (+5.3%), Avg. 75.7% (+6.9%), Last 85.3% (+8.1%) - maintains strong performance under high domain shift
      - **CIL Benchmarks**: CIFAR100 (10/20/50 steps) and TinyImageNet (5/10/20 steps) - consistent improvements over traditional CL methods
      - **Synthetic vs Real Data**: 1K synthetic images outperform 1K real ImageNet images in Avg./Last metrics while maintaining comparable Transfer scores
  - **Ablation Studies**:
      - **Contrastive > Other Losses**: Contrastive distillation (85.0% Last) >> feature distance (80.5%) > image-only (84.1%) > text-only (81.8%)
      - **Teacher Model Choice**: Last CLIP model optimal vs. initial CLIP (higher Transfer but lower Last) vs. WiSE interpolation (suboptimal balance)
      - **ITA Scale Analysis**: β=0.25 provides optimal soft-hard target balance; higher β causes synthetic data overfitting
      - **AWC vs EWC**: Adaptive Fisher information (86.0% Last) significantly outperforms static EWC variants (≤86.2% with 256 samples)
  - **Synthetic Data Analysis**:
      - **Generation Quality**: High-quality diverse images across domains; 50→25 denoising steps minimal performance impact (fast generation)
      - **Guidance Scale Robustness**: Consistent performance across CFG scales (4.5-10.5) due to inter-class diversity focus over intra-class variation
      - **Domain-Specific Impact**: Eliminating synthetic data for specific tasks (Aircraft, StanfordCars) significantly exacerbates forgetting of those tasks
      - **Distribution Coverage**: Synthetic pre-training data (ImageNet classes) + downstream classes provides comprehensive feature space anchoring
  - **Computational Efficiency**:
      - **Storage-Free**: Generated images discarded after each task; regenerated before next task ensuring diversity
      - **Privacy-Preserving**: No historical data storage required; synthetic recreation eliminates privacy concerns
      - **Cost-Effective**: 1K images per task via Stable Diffusion vs. storing/accessing massive real datasets
  - **Institution**: Wuhan University, Chinese Academy of Sciences, Wuhan AI Research
  - **Authors**: Bin Wu, Wuxuan Shi, Jinqiao Wang, Mang Ye
  - **Open Source**: ✅ [Code](https://github.com/Luo-Jiaming/GIFT_CL)
  - **Significance**:
      - **Multi-Modal CL Breakthrough**: First successful application of diffusion-generated synthetic data to VLM continual learning
      - **Dual Knowledge Preservation**: Simultaneously maintains pre-training generalization AND downstream task performance - critical for practical VLM deployment
      - **Synthetic Data Paradigm**: Demonstrates synthetic data superiority over real data replay for CL when properly designed
      - **Practical Impact**: Enables efficient VLM updates in production without catastrophic forgetting, storage overhead, or privacy issues
  
  #### 🎭 VLM Personalization & Concept Learning
  

</details>
<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2503.12999">📄 Concept-as-Tree (CaT)</a></b><br>
<code>arXiv 2503.12999</code>
</summary>

  - **Data Synthesis Method** - **Hierarchical Concept Tree Framework for Controllable Synthetic Data Generation**:
      - **Core Innovation**: First controllable synthetic data pipeline for VLM personalization using tree-structured concept representation to generate positive/negative samples with varying difficulty and diversity
      - **Three-Layer Tree Structure**: Root node (concept category: "cat", "dog"), Dimensions (attribute aspects: "appearance", "behavior", "location"), Attributes (specific features: "sitting", "lying", "climbing")
      - **Automated Tree Construction**: VLM description → Batch summarization → Self-refinement with multi-round voting mechanism for orthogonality and completeness
      - **Data Scale**: Works with 1-3 user-provided images, generates controllable positive/negative samples for personalization fine-tuning
  - **Key Technical Components**:
      - **Tree Editing Operations**: (1) Add Dimension - increases diversity and conversational capabilities, (2) Remove Dimension - decreases diversity for focused learning, (3) Modify Dimension - balanced diversity control
      - **Controllable Sample Generation**: Positive samples via fine-tuned diffusion on user images + root node; Easy negatives via root category replacement; Hard negatives via dimension modification while preserving root
      - **PCS Score Filtering**: Perturbation-based Concept-Specific score distinguishes concept-specific (CS) vs concept-agnostic (CA) information through patch shuffling and CLIP similarity difference
      - **Multi-Type Sample Strategy**: Easy negatives boost recognition; Hard negatives enhance VQA/conversation; Combined approach achieves optimal performance across tasks
  - **Experimental Framework**:
      - **Systematic Analysis**: Studies positive/negative sample impact and diversity requirements across recognition, VQA, captioning, and choice tasks
      - **Cross-Model Validation**: MyVLM, Yo'LLaVA, MC-LLaVA baselines show consistent improvements with synthetic data integration
      - **Diversity Optimization**: Identifies optimal diversity levels - excessive diversity introduces noise, insufficient diversity limits generalization
  - **Experimental Results**:
      - **MyVLM Enhancement**: Recognition +3.4%, VQA +4.5%, Caption +2.6% (Real+Syn+Plus setting)
      - **Yo'LLaVA Enhancement**: Recognition +2.2%, VQA +3.9%, Caption +5.3% achieving near GPT-4o performance in certain scenarios
      - **MC-LLaVA Enhancement**: Recognition +3.0%, VQA +4.2%, Caption +5.3% with stable cross-dataset improvements
      - **Quality Validation**: Human evaluation shows synthetic positive samples comparable to originals, synthetic hard negatives significantly outperform retrieved negatives
  - **Data Quality Insights**:
      - **PCS Score Effectiveness**: High PCS scores (>0.3 for positives, >0.1 for hard negatives) correlate with concept-specific information content
      - **Synthetic vs Retrieved**: Synthetic negative samples show lower proportion of low-quality samples compared to retrieval-based negatives
      - **Tree Operation Analysis**: Add operations increase diversity most, Remove operations decrease it, Modify provides balanced control
  - **Practical Guidelines**:
      - **Minimal Data Requirements**: 1-3 concept images sufficient for effective personalization (vs. traditional 10+ images)
      - **Controllable Generation**: Tree editing frequency and type directly control synthetic data diversity and task-specific improvements
      - **Quality Assurance**: PCS score filtering more effective than cosine similarity alone for concept-centric data selection
      - **Mixed Training**: Combination of original + synthetic data achieves best performance, pure synthetic data shows distribution shift challenges
  - **Institution**: Peking University, Intel Labs China, CUHK MMLab
  - **Authors**: Ruichuan An, Kai Zeng, Ming Lu, Sihan Yang, Renrui Zhang, et al.
  - **Open Source**: ✅ [Code](https://github.com/zengkaiya/CaT)
  - **Significance**:
      - **Personalization Breakthrough**: First systematic framework for VLM personalization with minimal user data requirements
      - **Controllable Synthesis**: Enables precise control over synthetic data characteristics through interpretable tree operations
      - **Quality Assessment Innovation**: PCS score provides novel method for evaluating concept-specific information in synthetic images
      - **Practical Impact**: Makes VLM personalization accessible for real-world deployment with limited user-provided examples
  

</details>
---

#### 🛠️ Tool-Assisted Annotation Generation (For Data Synthesis)

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
<img src="https://img.shields.io/badge/Institution-ICLR_2025_--_Kuaishou_Technology-red?style=flat-square"/>
</summary>

  - **Focus**: **Large-Scale Task Type Expansion** - Constructing multimodal instruction fine-tuning dataset with 19,227 hierarchical task types and 413K samples, significantly improving task diversity through automated pipeline
  - **Data Synthesis Method** - **GPT-4o-Driven Hierarchical Task Type Expansion + Multi-Referee Filtering Pipeline**:
      - **Core Innovation**: First dataset with tens of thousands of task types, automatically expanding task taxonomy via GPT-4o, combined with CLIP filtering and multi-open-source-model scoring to ensure quality
      - **Problem Identification**:
        - Existing instruction fine-tuning datasets have limited task types (e.g., Vision-Flan only 196 types), limiting model generalization
        - Manual task type annotation is costly and time-consuming, difficult to scale
        - Low task type-image matching quality leads to poor training data quality
      - **Five-Step Automated Generation Pipeline**:
        1. **Hierarchical Task Type Generation**:
           - **Seed Task Definition**: Manually define small set of level-1 task types (e.g., OCR, Image Description, Logical Reasoning)
           - **GPT-4o Iterative Expansion**:
             - **Level-1 Tasks**: Expand from seed tasks to 115 level-1 task types
             - **Level-2 Tasks**: Generate 2,796 level-2 subtasks for each level-1 task
             - **Level-3 Tasks**: Further subdivide into 14,370 level-3 tasks
           - **Prompt Design**: Design specialized prompts for different levels to ensure systematic and complete expansion
           - **Final Scale**: 19,227 hierarchical task types (1:2:3 ratio = 115:2,796:14,370)
        2. **Image Data Collection**:
           - **Multi-Source Images**: Collect images from ALLaVA, Visual Genome, LAION, DocVQA, CLEVR-Math and other public datasets
           - **Preserve Original Resolution**: No additional preprocessing
           - **Support Diverse Image Types**: Natural scenes, documents, charts, artwork, watermarked images, etc.
        3. **Task Type-Image Matching (CLIP Filtering)**:
           - **Text-Image Similarity Computation**: Use CLIP to compute similarity between task type text and images
           - **Initial Screening**: Match most relevant task types for each image
           - **Issue**: CLIP matching performance limited, may produce mismatches
        4. **Question-Answer Generation (GPT-4o)**:
           - **Input**: Image + matched task type text
           - **Output**: Question-answer pairs (JSON format)
           - **Prompt Design**: Request generating complex questions with detailed answers
           - **Diversity**: Generate multiple different questions for each task type-image pair
        5. **Multi-Referee Scoring Filtering (Referee Screening)**:
           - **Three-Model Consensus Mechanism**: Use three high-performance open-source multimodal models (InternVL, Qwen-VL, other MLLMs) as referees
           - **Scoring Criteria**: Each model scores task type, question-image matching (0 or 1)
           - **Filtering Rule**: Only retain samples with cumulative score ≥2 (at least two of three models agree)
           - **Advantage**: Improves task type, question-image alignment accuracy, reduces closed-source API costs
           - **Balance Strategy**: To maintain task type balance, randomly select 1-55 samples per task type
      - **Key Technical Advantages**:
        - **Fully Automated**: Except for small number of seed tasks, entire pipeline requires no human intervention
        - **Task Type Quantity**: 19,227 task types, 98× more than Vision-Flan
        - **Quality Control**: Multi-referee mechanism ensures data quality, avoids single-model bias
        - **Scalability**: Pipeline adaptable to new image types and task types
  - **TaskGalaxy Dataset**:
      - **Total Scale**: 413,648 high-quality question-answer pairs
      - **Task Types**: 19,227 hierarchical task types
      - **Sample Distribution**: 1-55 samples per task type
        - 1-10 samples: 50.1% of task types
        - 11-20 samples: 11.1%
        - 21-40 samples: 10.21%
        - 41-55 samples: 27.99%
      - **Hierarchical Distribution**: Level-1:Level-2:Level-3 = 1:2:3 (115:2,796:14,370)
  - **Experimental Results** - **Improvements across all 16 benchmarks**:
      - **LLaVA-v1.5-7B** (fine-tuned with TaskGalaxy):
        - MME: 1506→1533, MMBench: 64.69%→68.04%, ScienceQA: 69.51%→71.26%
        - MathVista: 26.7%→31.4% (+4.7%), ChartQA: 14.72%→20.20% (+5.48%)
        - AI2D: 25.32%→38.26% (+12.94%), HalluBench: 50.05%→51.74%
        - **Average Improvement**: 44.46%→48.96% (+4.5%, excluding MME)
      - **LLaVA-v1.5-13B** (fine-tuned with TaskGalaxy):
        - MME: 1532→1600, MMBench: 68.47%→69.85%, MathVista: 28.1%→33.3% (+5.2%)
        - ChartQA: 15.56%→23.44% (+7.88%), AI2D: 21.13%→41.19% (+20.06%)
        - **Average Improvement**: 45.21%→49.04% (+3.83%)
      - **InternVL-Chat-v1.0-7B** (fine-tuned with TaskGalaxy):
        - MMBench: 65.29%→67.10%, ScienceQA: 66.4%→70.93%, MathVista: 27.7%→30.8%
        - MMMU: 27.0%→34.9% (+7.9%), AI2D: 35.96%→38.57%
        - **Average Improvement**: 47.79%→50.79% (+3.0%)
      - **InternVL-Chat-v1.0-13B** (fine-tuned with TaskGalaxy):
        - MMBench: 65.64%→69.50%, ScienceQA: 70.12%→72.72%, MathVista: 28.7%→30.5%
        - AI2D: 38.55%→52.60% (+14.05%), Q-Bench: 56.13%→58.60%
        - **Average Improvement**: 49.90%→53.17% (+3.27%)
  - **Ablation Study Key Findings**:
      - **Task Type Quantity Critical**:
        - Fixed 100K samples, task types from 2K to 19K, performance continuously improves
        - Proves task diversity more important than data volume
      - **Sample Quantity Impact**:
        - Fixed 19,227 task types, samples from 76K to 413K, performance gradually improves
        - But optimal sample size exists for some benchmarks (e.g., LLaVA-in-the-wild at 281K)
      - **vs. Rule-Based Methods and Closed-Source Models**: TaskGalaxy's task coverage and quality superior to manual rule construction and closed-source model generation
  - **Task Type Examples** (showing task hierarchy):
      - **Level-1**: OCR, Image Description, Logical Reasoning, Suggestions, Storytelling
      - **Level-2**: OCR→webpage OCR / handwritten OCR, Image Description→location-based / historical context
      - **Level-3**: webpage OCR→extract links / recognize style, location-based→describe cityscapes / identify landmarks
  - **Institution**: Kuaishou Technology
  - **Authors**: Jiankang Chen, Tianke Zhang, Changyi Liu, Haojie Ding, Yaya Shi, Feng Cheng, Huihui Xiao, Bin Wen, Fan Yang, Tingting Gao, Di Zhang
  - **Publication**: ICLR 2025, arXiv February 2025
  - **Paper Link**: [arXiv:2502.09925](https://arxiv.org/abs/2502.09925)
  - **Open Source**: ✅ [GitHub](https://github.com/Kwai-YuanQi/TaskGalaxy)
  - **Significance**:
      - **Task Type Breakthrough**: First to achieve tens of thousands of task type coverage, 100× existing datasets
      - **Automated Pipeline**: Dramatically reduces task type expansion costs, improves scalability
      - **Task Diversity Value**: Empirically proves task diversity importance for model generalization exceeds data volume
      - **Multi-Referee Mechanism**: Innovative quality control method balancing cost and quality
      - **Practicality**: Significant improvements across 16 mainstream benchmarks, proving method universality
  

</details>
---

## 🎯 VLM Self-Improvement & Reinforcement Learning

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

  - **Focus**: **Vision-Language Model Dialog Games for Self-Improvement** - Through two VLM agents engaged in goal-oriented reference game self-play, automatically filtering successful game interactions to generate high-quality interleaved image-text data for fine-tuning
  - **Data Synthesis Method** - **Goal-Oriented Self-Play Framework + Automatic Success Detection**:
      - **Core Innovation**: First dialog game-based VLM self-improvement framework, generating high-quality synthetic data through goal-oriented self-play without human annotation or external models
      - **VLM Dialog Game Mechanism**:
        - **Game Setup**: Construct reference game variant using unlabeled images
          - **Describer**: Sees single target image, instructed to answer questions about it faithfully
          - **Guesser**: Sees N images (including target and multiple distractors), identifies target image by asking questions
        - **Game Flow**:
          - Guesser poses clarifying questions (e.g., "How many objects are in the image?")
          - Describer answers questions (e.g., "There are 9 objects")
          - Guesser makes guess based on accumulated information (e.g., "I know the answer, it is image 4")
          - If Guesser correctly identifies target image, game succeeds
        - **Game Difficulty Control**:
          - **Number of Distractors**: Increasing N directly increases difficulty (N=2 to 8)
          - **Image Similarity**: Random image selection creates easier games, while grouping visually or semantically similar images increases challenge
          - **Optimal Setting**: N=4 achieves best balance in study
      - **Self-Improvement Workflow**:
        1. **Game Setup**: Configure dialog game with designated unlabeled image dataset (OpenImages, DOCCI, or domain-specific datasets like robotics video frames)
        2. **Dialog Generation**: Generate dialogs via self-play between VLM agents
          - **Describer Examples**: Input=single image+question, Output=corresponding answer
          - **Guesser Examples**: Input=N images+target image description summary, Output=clarifying question or guess
          - Each successful VLM Dialog Game generates multiple training examples of both types
        3. **Dialog Filtering**: Filter generated dialogs based on success criteria
          - **Success Detection**: If Guesser's final selection matches target image, dialog considered successful
          - **Validation Step**: To avoid correct guesses by chance, rerun dialog with same images but permuted order, verify correct target identification in all permutations
          - **Computational Efficiency**: Limit tested permutations to N, ensuring target image appears at each possible position (1 to N), distractor order can remain fixed
        4. **Model Improvement**: Fine-tune VLM using filtered successful dialog game data
          - **Standard Supervised Fine-tuning**: Use filtered dialog data
          - **Iterative Improvement**: Improved model can be used to generate new, higher-quality dataset for further improvement (round 1, round 2, etc.)
      - **Key Technical Advantages**:
        - **Goal-Oriented**: Goal-oriented nature of game ensures quality of generated data, success detection provides automatic quality control
        - **Self-Play**: Leverages VLM's instruction-following capabilities for scalable data collection approach
        - **No External Models**: No need for GPT-4V or other external models, only uses base VLM itself
        - **Domain Adaptability**: Can adapt to specific domains (e.g., robotics) by designing games using images from that domain
        - **Iterative**: Improved models can be used to generate better datasets, enabling continuous improvement
      - **Experimental Results**:
        - **General Image Experiments** (DOCCI and OpenImages datasets):
          - **Game Success Rate**: Gemini 1.5 Flash 20.3% → VLM Dialog Games (DOCCI) 24.4% (+4.1%)
          - **VQA Performance** (VQAv2):
            - **Yes/No Questions**: 73.0% → 79.8% (+6.8%, DOCCI) and 83.4% (+10.4%, OpenImages)
            - **Counting Questions**: 56% → 58.3% (+2.3%, DOCCI) and 56% (+0.0%, OpenImages)
          - **Cross-Dataset Generalization**: Model trained on DOCCI performs better on OpenImages games (21.9% vs 18.4%), and vice versa
        - **Robotics Domain Experiments** (ALOHA dataset):
          - **Game Success Rate**: Gemini 1.5 Flash 14.39% → Round 1 40.15% (+25.76%) → Round 2 53.74% (+39.35%)
          - **Success Detection Accuracy**: 56.5% → Round 1 69.5% (+13.0%) → Round 2 73.0% (+16.5%)
          - **Iterative Improvement**: Round 2 further improves both game success rate and success detection accuracy
          - **vs Baselines**:
            - **SFT-Description**: 65.0% (+8.5%) - Direct fine-tuning on image-task description pairs
            - **Self-QA**: 67.0% (+10.5%) - Question-answering based self-improvement approach
            - **VLM Dialog Games (answers only)**: 68% (+12.5%) - Using only Describer answers, but low game success rate (17.92%), unable to achieve further iterative improvement
        - **Ablation Studies**:
          - **Impact of Number of Images** (N value):
            - **N=2**: Game success rate 83.7%, but game simple, less informative data, VQA accuracy 81.3% (+8.3%)
            - **N=4**: Game success rate 18.4%, VQA accuracy 83.4% (+10.4%) - **Optimal**
            - **N=8**: Game success rate 0.24%, game too difficult, very few dialog data generated, VQA accuracy 77.1% (+4.1%)
          - **Image Grouping Strategy**:
            - **Similar Image Grouping**: Game success rate 18.4%, VQA accuracy 83.4% (+10.4%)
            - **Random Image Grouping**: Game success rate 24.7%, VQA accuracy 82.6% (+9.6%)
            - **Conclusion**: Both strategies significantly improve, similar image grouping slightly better, but random grouping also works effectively
      - **Key Findings**:
        - **Self-Play Effectiveness**: Current VLM's instruction-following capabilities enable non-zero success rate in dialog games, providing foundation for scalable data generation
        - **Goal-Oriented Advantage**: Goal-oriented nature of game ensures quality of generated data, success detection provides automatic quality control
        - **Iterative Improvement Capability**: Improved models can be used to generate better datasets, enabling continuous improvement (Round 1 → Round 2)
        - **Domain Adaptability**: Method can adapt to specific domains (e.g., robotics), particularly effective in domains where high-quality data is scarce
        - **Importance of Guesser Questions**: Using only Describer answers can improve success detection but cannot improve game success rate, limiting further iterative improvement
      - **Institution**: Google DeepMind
      - **Authors**: Ksenia Konyushkova, Christos Kaplanis, Serkan Cabi, Misha Denil
      - **Publication**: arXiv February 2025 (v1)
      - **Open Source**: ⚠️ Code/data availability not explicitly stated in paper
      - **Significance**:
        - **Method Innovation**: First dialog game-based VLM self-improvement framework, generating high-quality data through goal-oriented self-play
        - **Scalability**: Leverages VLM's own capabilities, no external models or human annotation required, enabling scalable data generation
        - **Domain Adaptability**: Can adapt to specific domains (e.g., robotics), particularly effective in domains where high-quality data is scarce
        - **Practical Value**: Significantly improves performance on general VQA and robotics success detection tasks, demonstrating method effectiveness
  

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

  - **Focus**: **Calibrated Self-Rewarding Vision Language Models** - Improving modality alignment in LVLMs by incorporating visual constraints into the calibrated self-rewarding process, reducing hallucinations and enhancing performance
  - **Data Synthesis Method** - **Iterative Preference Optimization Framework + Calibrated Reward Model**:
      - **Core Innovation**: First method to integrate visual constraints into the self-rewarding paradigm, addressing modality alignment issues in LVLMs during both response generation and preference modeling stages
      - **Problem Identification**: LVLMs suffer from modality misalignment, where models tend to prioritize textual information over visual input, leading to hallucination phenomena
      - **CSR Framework (Two Alternating Stages)**:
        1. **Candidate Response Generation Stage**:
           - **Sentence-Level Beam Search**: Uses sentence-level beam search to generate fine-grained candidate responses for each input prompt
           - **Reward Calculation Process**:
             - **Initial Reward**: Language decoder determines initial reward R_T(s) for each generated sentence (sentence-level cumulative probability)
             - **Image-Response Relevance Score**: Calculates R_I(s) = max(100×cos(F_I(x_v), F_T(s)), 0) using CLIP-score
             - **Calibrated Reward**: R(s) = λ·R_I(s) + (1-λ)·R_T(s), where λ=0.9 (emphasizing visual calibration)
           - **Iterative Generation**: Selects top-k and bottom-k sentences based on calibrated reward scores, continues to next round of beam search
           - **Cumulative Reward**: Cumulative reward for response y: R(y) = Σ R(s_i)
        2. **Preference Curation and Fine-tuning Stage**:
           - **Preference Data Construction**: Selects responses with highest and lowest cumulative calibrated rewards as preferred and dispreferred responses
           - **DPO Optimization**: Uses Direct Preference Optimization (DPO) for fine-tuning
           - **Reference Model**: Each iteration uses the model from previous round as reference model
           - **Loss Function**: L_t = -E log σ(α log(π_θ(y_w,t|x)/π_θt-1(y_w,t|x)) - α log(π_θ(y_l,t|x)/π_θt-1(y_l,t|x)))
      - **Key Technical Advantages**:
        - **Vision-Constrained Reward**: Addresses LVLM's tendency to overlook visual input when generating preferences by incorporating image-response relevance information
        - **Step-Wise Reward**: Sentence-level rewards provide finer-grained guidance and stronger robustness
        - **Self-Rewarding Paradigm**: No external models or human annotations required, leverages model itself to generate preference data
        - **Iterative Improvement**: Continuously enhances model performance and modality alignment through multiple iterations
      - **Training Settings**:
        - **Base Models**: LLaVA-1.5 7B and 13B
        - **Training Data**: Randomly sampled ~13,000 samples from detailed description and complex reasoning subclasses of LLaVA150k dataset
        - **Fine-tuning Method**: LoRA fine-tuning
        - **Iterations**: 3 rounds (~3.5-5 hours per round, 1×A100 80GB)
        - **Hyperparameters**: λ=0.9 (CLIP score weight), α=0.1 (language score weight)
      - **Experimental Results**:
        - **Comprehensive Benchmarks** (MME, SEED, LLaVAW, MMBench, MM-Vet):
          - **LLaVA-1.5-7B + CSR**: Average improvement of 7.62% (3 iterations)
          - **LLaVA-1.5-13B + CSR**: Average improvement of 5.25% (3 iterations)
          - **Significant Improvements**: LLaVAW +8.9%, CHAIR +49.50%
        - **General VQA** (ScienceQA, VizWiz, GQA):
          - **7B Model**: ScienceQA +2.9%, VizWiz +4.1%, GQA +0.3%
          - **13B Model**: ScienceQA +3.5%, VizWiz +3.2%, GQA +0.4%
        - **Hallucination Benchmarks** (POPE, CHAIR):
          - **POPE**: 7B model 85.90%→87.01% (+1.11%), 13B model 85.90%→87.30% (+1.40%)
          - **CHAIR_S**: 7B model 48.8%→21.0% (-27.8%, lower is better), 13B model 48.3%→28.0% (-20.3%)
          - **CHAIR_I**: 7B model 14.9%→6.0% (-8.9%), 13B model 14.1%→7.3% (-6.8%)
        - **vs. Competitive Methods**:
          - **Outperforms Self-Rewarding Baseline**: Average improvement of 2.43%
          - **Outperforms External Preference Methods**: Better than POVID, RLHF-V, Silkie that rely on GPT-4 or human annotations
          - **vs. SOTA Open-Source VLMs**: Outperforms InstructBLIP, Qwen-VL-Chat, mPLUG-Owl2 on 9 out of 10 benchmarks
        - **Iterative Improvement Analysis**:
          - **Reward Score Changes**: Preferred response rewards improve from 0.4885 (iteration 1) to 0.5066 (iteration 5)
          - **Image-Response Relevance**: Both preferred and dispreferred responses show improved image relevance scores, with gap gradually narrowing
          - **Attention Analysis**: CSR enhances attention to visual tokens, reduces over-reliance on textual context
        - **Compatibility Validation** (Vila 7B):
          - **Overall Improvement**: Average improvement of 3.37% after 3 iterations
          - **Significant Improvements**: VizWiz +8.48%, MM-Vet +14.0%
      - **Ablation Studies**:
        - **Only R_T (Language Score)**: 68.46% (7B), 68.12% (13B)
        - **Only R_I (Image Score)**: 67.49% (7B), 69.23% (13B)
        - **CSR (Combined)**: 72.39% (7B), 71.95% (13B)
        - **Conclusion**: Combined use of both scores achieves best results
        - **λ Value Analysis**: λ=0.9 outperforms 0.5 and 0.1, proving importance of visual calibration
      - **Theoretical Analysis**:
        - **Theorem 5.1**: Under mild assumptions, incorporating image-response relevance scores can calibrate the self-rewarding process and improve generation accuracy
        - **Key Condition**: When model tends to prioritize textual information over visual input (∥β*^T V_1*∥ ≪ ∥β*^T V_2*∥), visual constraints (λ<1) can increase attention to image signals
      - **Key Findings**:
        - **Self-Rewarding Effectiveness**: Self-generated preference data is more effective than external model (e.g., GPT-4) generated preferences, as it better captures target LVLM's inherent preferences
        - **Visual Constraint Necessity**: Directly applying self-rewarding to LVLMs cannot address modality alignment issues, visual constraints are required
        - **Iterative Improvement Capability**: CSR can continuously improve performance through iterative fine-tuning, gradually converging
        - **Cross-Model Compatibility**: Method applicable to different LVLM architectures (LLaVA-1.5, Vila)
      - **Institution**: UNC-Chapel Hill, University of Chicago, University of Maryland, Rutgers University, HKUST, PolyU, NTU, NUS
      - **Authors**: Yiyang Zhou, Zhiyuan Fan, Dongjie Cheng, Sihan Yang, Zhaorun Chen, Chenhang Cui, Xiyao Wang, Yun Li, Linjun Zhang, Huaxiu Yao
      - **Publication**: arXiv May 2024 (v4) | NeurIPS 2024
      - **Open Source**: ✅ [Code and Data](https://github.com/YiyangZhou/CSR)
      - **Significance**:
        - **Paradigm Innovation**: First to integrate visual constraints into self-rewarding paradigm, addressing LVLM-specific modality alignment issues
        - **Cost Reduction**: No external models or human annotations required, uses model itself for self-improvement
        - **Performance Enhancement**: Significant improvements across multiple benchmarks and hallucination reduction, average improvement of 7.62%
        - **Theoretical Support**: Provides rigorous theoretical analysis validating method effectiveness
        - **Practical Value**: Provides scalable and cost-effective solution for LVLM self-improvement
  

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

## 🧠 Cross-Domain Methodology Insights

> **Note**: This section includes influential works from adjacent domains (e.g., LLM reasoning, mathematical data curation) whose **data curation and quality assessment methodologies** provide valuable frameworks transferable to multimodal settings. While not directly VLM papers, their systematic approaches to data quality evaluation, mixture optimization, and efficient filtering pipelines offer important insights for multimodal data practitioners.

### 📚 Foundation Model Mid-training & Data Curation

<details>
<summary><b>OctoThinker: Mid-training Incentivizes Reinforcement Learning Scaling</b> - Systematic Data Curation, Quality Assessment & Mixture Optimization</summary>

**Paper**: [OctoThinker: Mid-training Incentivizes Reinforcement Learning Scaling](https://arxiv.org/abs/2506.20512)

**Institution**: GAIR Lab, Shanghai Jiao Tong University (Wang et al.)

**Publication**: arXiv June 2025

**Domain**: Mathematical reasoning / LLM mid-training

**🔬 Why Relevant to VLM Data Curation?**

**Core Contribution**: This paper is **NOT about data synthesis/generation**, but rather about **systematic data quality assessment, large-scale filtering/curation, and mixture optimization**. While focused on mathematical reasoning in the text domain, OctoThinker provides a rigorous experimental framework for evaluating and selecting high-quality data from existing corpora—methods highly transferable to multimodal scenarios where practitioners need to curate billion-scale datasets from noisy web sources.

---

**📊 Key Transferable Insights**:

**1. Two-Stage Quality Assessment Pipeline**
- **Method**: LLM annotation (0-5 scale) → Train efficient classifier (FastText) → Large-scale filtering (threshold 0.4) → Optional LLM refinement
- **Key Finding**: Preprocessing critical for recall; threshold 0.4 balances quality-quantity (vs 0.9 in prior work)
- **Result**: MegaMath-Web-Pro-Max (73.8B tokens, 5.5× larger than MegaMath-Web-Pro's 13B)
- **VLM Transfer**: Construct multimodal annotation schema addressing vision-language alignment quality, information density, and compositional reasoning complexity; train lightweight cross-modal discriminators with frozen vision encoders to enable cost-effective billion-scale curation while preserving high-fidelity filtering

**2. Systematic Data Mixture Optimization**
- **Rigorous Testing**: 10%, 20%, 30%, 40% ratios across multiple dimensions
- **Optimal Finding**: 30% QA data (diminishing returns beyond due to redundancy)
- **Critical Insight**: *"Distribution gap between training data and downstream tasks notably affects performance"*
- **VLM Transfer**: Establish controlled experimental frameworks varying caption granularity (entity-level vs scene-level vs reasoning-level), data provenance (web-scraped vs human-annotated vs model-synthesized), and cross-modal interaction patterns; employ grid search with rigorous downstream evaluation rather than heuristic mixing

**3. Distribution Alignment > Data Scale**
- **Observation**: Structured QA datasets (OpenR1, OMI2) outperform web-sourced QA (MegaMath-QA) for competition-style benchmarks due to distributional alignment, not data volume
- **Principle**: Match pre-training distribution to downstream task format, not just domain
- **VLM Transfer**: Prioritize distribution-aware data curation over volume maximization—document understanding benefits from text-dense layouts with diverse typography rather than natural images; visual reasoning requires multi-hop relational annotations over descriptive captions; domain-specific applications demand modality-consistent and structurally-aligned pre-training corpora

**4. Small "Stabilizer" Data Has Outsized Impact**
- **Finding**: Small amounts (1-10%) of high-quality instruction data unlock potential of other data types
- **Effect**: Stabilizes training, reduces instability from long-format data, enables successful RL scaling
- **VLM Transfer**: Introduce small-proportion high-quality vision-language alignment data (1-10%) to regularize training dynamics, particularly when scaling to dense long-form captions or complex multi-image reasoning scenarios; acts as distributional anchor preventing mode collapse and representation drift

---

**🎯 Summary: Key Takeaways for VLM Data Practitioners**

| # | Principle | OctoThinker Method | VLM Application |
|---|-----------|-------------------|-----------------|
| 1 | **Quality over Quantity** | Filtered MegaMath-Web-Pro-Max >> Raw corpus | Curated high-precision pairs demonstrate superior downstream transfer over raw web-scale noisy corpora |
| 2 | **Efficient Filtering** | LLM annotation → FastText classifier → Scale | Scalable two-stage pipeline enabling billion-scale curation with computational efficiency |
| 3 | **Systematic Experimentation** | Test 10%, 20%, 30%, 40% ratios | Grid search over data mixture hyperspace with rigorous ablation studies |
| 4 | **Diminishing Returns** | Beyond 30% QA, redundancy hurts | Identify saturation points where marginal utility diminishes due to distributional redundancy |
| 5 | **Distribution Alignment** | Match downstream task format | Data format alignment with tasks outweighs domain similarity |
| 6 | **Stabilizer Data** | 1-10% instruction data unlocks QA potential | Small-proportion regularization data prevents training instability and enables scaling |
| 7 | **Format Awareness** | Long-CoT = high capability + instability | High-capacity dense outputs require stabilization mechanisms to prevent mode collapse |
| 8 | **Two-Stage Philosophy** | Foundation (90%) → Specialization (10%) | Broad distributional coverage followed by targeted capability specialization |
| 9 | **Preprocessing Matters** | Critical for classifier performance | Systematic normalization and artifact removal critical for discriminator generalization |
| 10 | **Empirical Validation** | Threshold validated on downstream tasks | Hyperparameter selection guided by downstream task performance rather than proxy metrics |

---

**📈 Scale & Resources**:
- **Base Model**: Llama-3.2-1B/3B/8B
- **Mid-training Budget**: Up to 200B tokens (Stable) + 20B tokens (Decay)
- **Final Corpus**: MegaMath-Web-Pro-Max (73.8B tokens, 5.5× larger than MegaMath-Web-Pro)
- **Ablation Studies**: Systematic controlled experiments across data quality, mixture ratios, QA sources, and format characteristics
- **Performance Gain**: 10-20% improvement over base model, matches Qwen2.5 after RL

**🔗 Resources**:
- ✅ **Paper**: [arXiv:2506.20512](https://arxiv.org/abs/2506.20512)
- ✅ **Code**: [GitHub - GAIR-NLP/OctoThinker](https://github.com/GAIR-NLP/OctoThinker)
- ✅ **Models**: [HuggingFace - OctoThinker](https://huggingface.co/OctoThinker)
- ✅ **Dataset**: MegaMath-Web-Pro-Max (70B+ tokens, open-source promised)
- ✅ **Full Disclosure**: All prompts and methods detailed in paper appendix

**💡 Potential VLM Follow-up Works**:
- Systematic vision-language data mixture optimization
- Efficient multimodal quality classifiers
- Distribution-aligned synthetic caption generation for specific domains
- Two-stage VLM pre-training with specialized branches

</details>

### 🔄 Multi-Modal Model Collapse & Synthetic Data Robustness

<details>
<summary>
<b><b><a href="https://arxiv.org/abs/2505.08803">📄 Multi-modal Synthetic Data Training and Model Collapse</a></b><br>
<code>arXiv 2505.08803</code>
<img src="https://img.shields.io/badge/Data-✓-blue?style=flat-square"/>
</summary>

  - **Domain**: Multi-modal generative systems (VLMs + Diffusion Models)
  - **Core Contribution**: First comprehensive study of model collapse in multi-modal vision-language generative systems, expanding beyond single-modality investigations to multi-agent recursive training scenarios
  - **Key Research Questions**:
      1. How does recursive synthetic data training impact multi-modal generative systems?
      2. What properties characterize multi-modal model collapse vs. single-modal collapse?
      3. Do model interactions make collapse better or worse?
      4. How can we improve generative synthetic data to mitigate model collapse?
  - **Experimental Framework**:
      - **Three Training Settings**: (1) Single-model recursive fine-tuning, (2) Two-model with frozen relabeling, (3) Joint recursive fine-tuning
      - **Model Architectures**: BLIP-2 (VLM) + Stable Diffusion 1.5 (text-to-image)
      - **Evaluation Dataset**: MS-COCO subset (1K samples) with comprehensive metrics across modalities
      - **Recursive Training**: Models generate synthetic data → fine-tune on generated data → repeat for multiple generations
  - **Key Findings**:
      - **VLM Collapse Differs from LLMs**: Variance increases (not decreases) in VLM image captioning due to cross-modal interactions bridging modality gaps
      - **Improved Vision-Language Alignment**: Model collapse paradoxically improves CLIP alignment scores through reduced variance, though with quality degradation
      - **Bias-Variance Trade-off Critical**: Balanced bias-variance (not just increased variance) key for collapse mitigation
      - **Decoding Budget Correlation**: Higher decoding budgets (50+ diffusion steps) generate more robust synthetic datasets resistant to collapse
  - **Multi-Modal Collapse Characteristics**:
      - **Diffusion Models**: 4× faster CLIP variance drop, improved caption-image alignment, saturation-driven gender bias shifts
      - **VLMs**: Vocabulary explosion (200+ more tokens), perplexity increase, improved semantic alignment but reduced grammatical coherence
      - **Distinct from Single-Modal**: Multi-modal systems show alignment improvements absent in unimodal collapse patterns
  - **Mitigation Strategies**:
      - **Model Diversity**: Both hyperparameter diversity (different CFG/temperatures) and architectural diversity (multiple model variants) reduce collapse
      - **Frozen Relabeling**: Using frozen models from different paradigms to relabel synthetic data significantly slows collapse (223.1 vs 253.2 FID)
      - **Joint Training Warning**: Simultaneous training of both models accelerates collapse (312.5 FID) - requires frozen anchoring models
      - **Statistical Quality Correlation**: Common metrics (FID for images, BLEU-4 for captions) reliably predict synthetic data robustness
  - **Practical Guidelines**:
      - **Decoding Optimization**: Increase generation steps for diffusion models to improve collapse resistance
      - **Multi-Agent Setup**: Maintain at least one frozen model trained on human-authored data to prevent co-degradation
      - **Quality Monitoring**: Use standard quality metrics as early warning indicators for model collapse onset
      - **Distribution Anchoring**: Avoid completely self-contained recursive loops without external reference points
  - **Institution**: University of Southern California
  - **Authors**: Zizhao Hu, Mohammad Rostami, Jesse Thomason
  - **Open Source**: ⚠️ Code availability not specified in paper
  - **Significance**:
      - **Multi-Modal Extension**: First rigorous investigation of model collapse beyond single-modality systems
      - **Practical Framework**: Provides concrete guidelines for safe deployment of recursive synthetic data training in multi-agent AI systems
      - **Quality Assurance**: Establishes correlation between standard metrics and collapse resistance for practical monitoring
      - **Self-Improving Systems**: Critical insights for developing stable autonomous multi-modal AI agents that train on self-generated data
  

</details>
---

## 📦 Notable Multimodal Datasets

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

## 📊 Benchmark Datasets

### 🎯 Instruction-Following Benchmarks

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

## 🎓 Resources

### 💡 Influential Inspirational Work

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

## 📝 Contributing

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

## ⭐ Star History

If this project helps you, please give us a Star ⭐️!

[![Star History Chart](https://api.star-history.com/svg?repos=opendatalab-raiser/awesome-multimodal-data-recipe&type=Date)](https://star-history.com/#opendatalab-raiser/awesome-multimodal-data-recipe&Date)

---

## 📄 License

This project is licensed under [MIT License](LICENSE).

---

## 🙏 Acknowledgments

Thanks to all researchers and engineers who have contributed to the field of multimodal data synthesis!

Special thanks to the following projects for inspiration:
- [awesome-data-llm](https://github.com/weAIDB/awesome-data-llm)
- [Awesome-Scientific-Datasets-and-LLMs](https://github.com/open-sciencelab/Awesome-Scientific-Datasets-and-LLMs)

---

<p align="center">
  Made with ❤️ by the multimodal research community
</p>

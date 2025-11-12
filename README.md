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

- **Total Papers:** 60+ (data synthesis/construction methods)
- **Industrial Reports:** 9 (Baidu, Microsoft, Alibaba, ByteDance, Tencent, Hunyuan, etc.)
- **Data Synthesis Methods:** 
  - Image Generation - Synthesizing New Visual Content (10): Geometric/mathematical reasoning + document/text-dense scenes + scene text detection + multimodal dialogue + text-driven image synthesis
  - Image Editing (4): Non-rigid motion, unified editing, referring expression-guided editing
  - Compositionality / Preference-Guided Synthesis (3): Enhancing compositional understanding + multi-concept composition + multi-image customization
  - Interleaved Image-Text · Coherence & Consistency (4): Multi-perspective quality filtering + iterative refinement + multimodal embedding-based correlation
  - Think with Image (1): Interleaved multimodal reasoning with image manipulation
  - Image-Invariant - Text Enhancement (29): Fixed images, enriched text only
  - Video - Instruction Tuning (Synthetic Data) (1): Synthetic video instruction-following data (captions + QA)
- **Notable Datasets:** 
  - 4 interleaved image-text datasets (OmniCorpus, OBELICS, MMC4, CoMM)
  - 2 domain-specific datasets (MMM-RS, MESED)
  - 4 image editing datasets (ByteMorph-6M, ImgEdit, RefEdit, RefCOCO-Edit)
  - 4 large-scale general training datasets
  - 4 chart reasoning datasets (ChartInstruct, Synthesize Step-by-Step, ECD, ChartGen)
  - 1 multimodal dialogue dataset (MAGID)
- **Open Source Datasets:** 28+ datasets fully open-sourced

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

- **📄 SynthVLM** [(ACM MM 2025, arXiv 2407.20756)](https://arxiv.org/abs/2407.20756) 🏷️ **[Method + Data]** - **ACM Multimedia 2025**
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

---

#### 📐 Geometric & Mathematical Reasoning

- **📄 R-CoT** [(OpenReview ICLR 2025)](https://openreview.net/pdf?id=iwVkB9zaVb)
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

- **📄 MAVIS** [(arxiv 2407.08739)](https://arxiv.org/abs/2407.08739)
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

- **📄 ShareGPT-4o-Image** [(arxiv 2506.18095)](https://arxiv.org/abs/2506.18095) *[Also includes Image Editing]*
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

- **📄 CoSyn** [(arXiv 2502.14846)](https://arxiv.org/abs/2502.14846) 🏷️ **[Method + Data]**
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

- **📄 TextSSR** [(arXiv 2412.01137)](https://arxiv.org/abs/2412.01137) 🏷️ **[Method + Data]** - **ICCV 2025**
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

- **📄 Synthetic Text Localisation** [(arXiv 1604.06646)](https://arxiv.org/abs/1604.06646) 🏷️ **[Method + Data]**
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

#### 🔄 Contrastive Learning & Image Difference

- **📄 Img-Diff** [(CVPR 2025)](https://github.com/modelscope/data-juicer/tree/ImgDiff) 🏷️ **[Method + Data]**
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

- **📄 ChartGen** [(arXiv 2507.19492)](https://arxiv.org/abs/2507.19492) 🏷️ **[Method + Data]**
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

- **📄 Effective Chart Dataset (ECD)** [(arXiv 2508.06492)](https://arxiv.org/abs/2508.06492) 🏷️ **[Method + Data]**
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

---

### 💭 Think with Image

This emerging category constructs **image-text interleaved reasoning traces** where images are actively **edited and manipulated** during the reasoning process. Unlike traditional text-only approaches, these methods treat text and images as **complementary modalities** that jointly advance problem-solving through progressive visual modifications (e.g., highlighting, overlaying, zooming, inpainting).

- **📄 ThinkMorph** [(arxiv 2510.27492)](https://arxiv.org/abs/2510.27492) 🏷️ **[Think with Image]**
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

---

### ✂️ Image Editing (Method + Data)

This category focuses on **instruction-guided image editing** where models learn to transform images based on natural language instructions. These works typically combine **method innovation** (novel editing pipelines, architectures) with **large-scale data synthesis** (automated data engines, quality benchmarks), making them distinct from pure dataset construction efforts.

- **📄 ByteMorph** [(arXiv 2506.03107)](https://arxiv.org/abs/2506.03107) 🏷️ **[Method + Data + Benchmark]**
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

- **📄 ImgEdit** [(arXiv 2505.20275)](https://arxiv.org/abs/2505.20275) 🏷️ **[Method + Data + Benchmark]**
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

- **📄 RefEdit** [(arXiv 2506.03481)](https://arxiv.org/abs/2506.03481) 🏷️ **[Method + Benchmark + Data]**
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

- **📄 Referring Image Editing / RefCOCO-Edit** [(CVPR 2024 Paper)](https://openaccess.thecvf.com/content/CVPR2024/html/Liu_Referring_Image_Editing_Object-level_Image_Editing_via_Referring_Expressions_CVPR_2024_paper.html) 🏷️ **[Task Definition + Method + Early Benchmark]** - **CVPR 2024**
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

---

### 🧩 Compositionality / Preference-Guided Synthesis

This category focuses on **synthetic data generation for enhancing compositional understanding** in Vision-Language Models. These methods use controlled data synthesis to improve models' ability to understand complex compositional relationships (e.g., attribute binding, spatial relationships, counting) and align with human preferences.

- **📄 SPARCL** [(arXiv 2503.01167)](https://arxiv.org/abs/2503.01167) 🏷️ **[Method + Synthetic Data]** - **CVPR 2025**
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

---

- **📄 Gen4Gen** [(arXiv 2402.15504)](https://arxiv.org/abs/2402.15504) 🏷️ **[Method + Data + Benchmark]** - **CVPR 2024**
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

---

- **📄 SynCD** [(arXiv 2502.01720)](https://arxiv.org/abs/2502.01720) 🏷️ **[Method + Data]** - **CVPR 2025**
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

---

### 🧪 Interleaved Image-Text · Coherence & Consistency

This category focuses on **high-quality interleaved image-text data construction** with emphasis on **coherence (logical flow), consistency (factual accuracy), and alignment (image-text relevance)**. Unlike simple image-text pairs, these methods curate or synthesize multi-image documents with narrative coherence, making them suitable for training models on long-context multimodal understanding and generation.

- **📄 InterSyn** [(arXiv 2506.09427)](https://arxiv.org/abs/2506.09427) 🏷️ **[Method + Data + Evaluation]**
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

---

- **📄 CoMM** [(arXiv 2406.10462)](https://arxiv.org/abs/2406.10462) 🏷️ **[Method + Data + Benchmark]** - **CVPR 2025**
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

---

- **📄 SMIR** [(arXiv 2501.03675)](https://arxiv.org/abs/2501.03675) 🏷️ **[Method + Data + Benchmark]**
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

---

### Image-Invariant Text Enhancement

This category of methods keeps original images fixed while enriching and improving paired text quality through various techniques. **This is currently the most mainstream multimodal data synthesis paradigm.**

> **Note**: Only includes papers that explicitly describe data synthesis/generation methods, with specific synthesis components annotated.

- **📄 Text-VQA Aug** [(arXiv 2511.02046)](https://arxiv.org/abs/2511.02046) 🏷️ **[Method + Data]**
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

- **📄 UI-E2I-Synth** [(arXiv 2504.11257)](https://arxiv.org/abs/2504.11257) 🏷️ **[Method + Data]**
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

- **📄 SK‑VQA** [(ICML 2025)](https://huggingface.co/datasets) 🏷️ **[Method + Data]**
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

- **📄 LLaVA‑Video: Video Instruction Tuning with Synthetic Data** [(arXiv 2410.02713)](https://arxiv.org/abs/2410.02713) 🏷️ **[Method + Data]**
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

- **📄 Unicorn** [(arXiv 2503.22655)](https://arxiv.org/abs/2503.22655) 🏷️ **[Method + Data]**
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

- **📄 Synthesize Step-by-Step** [(CVPR 2024)](https://openaccess.thecvf.com/content/CVPR2024/papers/Li_Synthesize_Step-by-Step_Tools_Templates_and_LLMs_as_Data_Generators_for_CVPR_2024_paper.pdf) 🏷️ **[Method + Data]** - **CVPR 2024**
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

- **📄 MANTIS** [(arXiv 2405.01483)](https://arxiv.org/abs/2405.01483) 🏷️ **[Method + Data + Evaluation]**
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

- **📄 MMDU** [(arXiv 2406.11833)](https://arxiv.org/abs/2406.11833) 🏷️ **[Method + Data + Benchmark]** - **NeurIPS 2024**
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

- **📄 ChartInstruct** [(arXiv 2403.09028)](https://arxiv.org/abs/2403.09028) 🏷️ **[Method + Data]**
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

- **📄 CompCap** [(arXiv 2412.05243)](https://arxiv.org/abs/2412.05243) 🏷️ **[Method + Data]**
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

- **📄 Infinity-MM** [(arXiv 2410.18558)](https://arxiv.org/abs/2410.18558) 🏷️ **[Method + Data]**
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

- **📄 ShareGPT4V** [(arxiv 2311.12793)](https://arxiv.org/abs/2311.12793)
  - **Data Synthesis Method** (Section 3.1):
    - Uses **GPT-4V** to generate high-quality captions for 100K images
    - Prompt design: Requires detailed descriptions (3-5 times more detailed than original captions)
    - Image sources: Curated images from COCO, SAM, LAION, etc.
  - **Data Scale**: 100K high-quality captions
  - **Open Source**: ✅ [Dataset](https://huggingface.co/datasets/Lin-Chen/ShareGPT4V) | [Code](https://github.com/InternLM/InternLM-XComposer/tree/main/projects/ShareGPT4V)

- **📄 SVIT** [(arxiv 2307.04087)](https://arxiv.org/abs/2307.04087)
  - **Data Synthesis Method** (Section 3.2):
    - Uses **GPT-4** to generate large-scale visual instruction data
    - 4.2M dialogues + 1.6M complex reasoning
    - Based on captions from multiple datasets (COCO, VG, CC3M, etc.)
  - **Data Scale**: 5.8M instruction data
  - **Open Source**: ✅ [Dataset](https://huggingface.co/datasets/BAAI/SVIT)

- **📄 CapsFusion** [(arxiv 2310.20550)](https://arxiv.org/abs/2310.20550)
  - **Data Synthesis Method** (Section 3):
    - **Fuses outputs from multiple captioning models** (BLIP-2, CoCa, GPT-4V, etc.)
    - Uses weighted fusion strategy, combining strengths of different models
    - Re-generates captions for DataComp-1B
  - **Data Scale**: Billion-scale recaptioning
  - **Open Source**: ✅ [Code](https://github.com/baaivision/CapsFusion)

- **📄 Image Textualization** [(arxiv 2406.07502)](https://arxiv.org/abs/2406.07502)
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

---

- **📄 Recap-DataComp-1B** [(arXiv 2406.08478)](https://arxiv.org/abs/2406.08478) 🏷️ **[Method + Data]**
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

---

- **📄 Hunyuan-Recap100M** [(arXiv 2504.13123)](https://arxiv.org/abs/2504.13123) 🏷️ **[Method + Data]** - **Industrial Report**
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

---

- **📄 SynC** [(arXiv 2507.18616)](https://arxiv.org/abs/2507.18616) 🏷️ **[Method]**
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

---

- **📄 High-Res Captioning** [(arXiv 2510.27164)](https://arxiv.org/abs/2510.27164) 🏷️ **[Method]**
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

- **📄 LLaVAR** [(arxiv 2306.17107)](https://arxiv.org/abs/2306.17107)
  - **Data Synthesis Method** (Section 3.2):
    - Targets text-rich images (documents, posters, charts, etc.)
    - Uses **GPT-4** to generate instruction Q&A pairs based on OCR results
    - Generates "understanding + reasoning" type questions (not just reading text)
  - **Data Scale**: 422K instruction data
  - **Open Source**: ✅ [Code](https://github.com/SALT-NLP/LLaVAR)

- **📄 ALLaVA** [(arxiv 2402.11684)](https://arxiv.org/abs/2402.11684)
  - **Data Synthesis Method** (Abstract explicitly describes):
    - **Captioning-then-QA paradigm**: Two-stage data generation
    - Uses **GPT-4V** to generate two types of data:
      a) **Fine-grained image annotations** for vision-language alignment
      b) **Complex reasoning visual QA pairs** for visual instruction fine-tuning
    - Complete data generation pipeline, utilizing powerful proprietary models to synthesize high-quality data
  - **Data Scale**: 1.3M samples
  - **Experimental Results**: Achieves competitive performance among 4B models, even on par with 7B/13B models on various benchmarks
  - **Open Source**: ✅ Dataset open-sourced (mentioned in paper)

- **📄 COGS** [(arxiv 2510.15040)](https://arxiv.org/abs/2510.15040)
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

- **📄 MAGID** [(arXiv 2403.03194)](https://arxiv.org/abs/2403.03194) 🏷️ **[Method + Data]**
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

- **📄 MegaPairs** [(arXiv 2412.14475)](https://arxiv.org/abs/2412.14475) 🏷️ **[Method + Data]**
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

- **📄 CtrlSynth** [(arXiv 2410.11963)](https://arxiv.org/abs/2410.11963) 🏷️ **[Method + Data]**
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

---

- **📄 ImageInWords** [(arXiv 2405.02793)](https://arxiv.org/abs/2405.02793) 🏷️ **[Method + Data]** - **ECCV 2024**
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

---

#### 🛠️ Tool-Assisted Annotation Generation (For Data Synthesis)

> Following tools are commonly used in data synthesis pipelines

- **📄 All-Seeing Project** [(arxiv 2308.01907)](https://arxiv.org/abs/2308.01907)
  - **Data Synthesis Method** (Section 3):
    - Uses SAM, RAM, Tag2Text and other tools to automatically generate multi-level annotations
    - Pipeline: Image → Segmentation+Tags → Region Description → Instruction Data
    - Builds AS-1B dataset (1.2B region-text pairs)
  - **This is true data synthesis**: Uses tool combination to generate new annotations
  - **Open Source**: ✅ [Dataset](https://huggingface.co/datasets/OpenGVLab/AS-V2) | [Code](https://github.com/OpenGVLab/all-seeing)


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

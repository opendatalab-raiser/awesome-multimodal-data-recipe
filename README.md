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

- **Total Papers:** 30+ (data synthesis/construction methods)
- **Industrial Reports:** 9 (Baidu, Microsoft, Alibaba, ByteDance, Tencent, etc.)
- **Data Synthesis Methods:** 
  - Image Generation - Synthesizing New Visual Content (4): Geometric/mathematical + document/text-dense scenes
  - Image Editing (4): Non-rigid motion, unified editing, referring expression-guided editing
  - Compositionality / Preference-Guided Synthesis (1): Enhancing compositional understanding
  - Interleaved Image-Text · Coherence & Consistency (1): Multi-perspective quality filtering
  - Think with Image (1): Interleaved multimodal reasoning with image manipulation
  - Image-Invariant - Text Enhancement (16): Fixed images, enriched text only
- **Notable Datasets:** 
  - 4 interleaved image-text datasets (OmniCorpus, OBELICS, MMC4, CoMM)
  - 2 domain-specific datasets (MMM-RS, MESED)
  - 4 image editing datasets (ByteMorph-6M, ImgEdit, RefEdit, RefCOCO-Edit)
  - 4 large-scale general training datasets
- **Open Source Datasets:** 25+ datasets fully open-sourced

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

### 🧪 Interleaved Image-Text · Coherence & Consistency

This category focuses on **high-quality interleaved image-text data construction** with emphasis on **coherence (logical flow), consistency (factual accuracy), and alignment (image-text relevance)**. Unlike simple image-text pairs, these methods curate or synthesize multi-image documents with narrative coherence, making them suitable for training models on long-context multimodal understanding and generation.

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

### Image-Invariant Text Enhancement

This category of methods keeps original images fixed while enriching and improving paired text quality through various techniques. **This is currently the most mainstream multimodal data synthesis paradigm.**

> **Note**: Only includes papers that explicitly describe data synthesis/generation methods, with specific synthesis components annotated.

#### 🔬 Large Model-based Text Generation

> **Core Idea**: Use powerful VLMs (e.g., GPT-4V) or LLMs (e.g., GPT-4) to generate higher quality captions/dialogue data for images

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

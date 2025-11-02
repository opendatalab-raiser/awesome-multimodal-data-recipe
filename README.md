# Awesome Multimodal Data Recipe [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

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
  <b>A curated list of multimodal data synthesis methods, tools, and resources for Vision-Language Models</b>
</p>

---

## 📊 Statistics

- **Total Papers:** 12 (data synthesis methods)
- **Industrial Reports:** 6 (Baidu, Microsoft, Alibaba, ByteDance)
- **Data Synthesis Methods:** Image-Invariant (12)
- **Open Source Datasets:** 11 datasets fully open-sourced

---

## 📋 Table of Contents

- [Introduction](#-introduction)
- [Industrial & Open-Source Data Synthesis](#-industrial--open-source-data-synthesis)
- [Methods by Image Processing Type](#-methods-by-image-processing-type)
  - [Image-Invariant Text Enhancement](#image-invariant-text-enhancement)
- [Tools & Frameworks](#-tools--frameworks)
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
  - **Open Source**: ✅ [Dataset](https://huggingface.co/datasets/OpenGVLab/all-seeing) | [Code](https://github.com/OpenGVLab/all-seeing)


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

## 🛠️ Tools & Frameworks

### 📦 Data Synthesis Tools

| Tool | Description | Link |
|------|-------------|------|
| GPT-4V API | Industry standard for high-quality caption/instruction generation | [Official Docs](https://platform.openai.com/docs/guides/vision) |
| LLaVA Toolkit | Complete instruction data generation pipeline | [GitHub](https://github.com/haotian-liu/LLaVA) |
| SAM (Segment Anything) | For automatic segmentation annotation | [Website](https://segment-anything.com/) |
| RAM/Tag2Text | For automatic image tagging | [GitHub](https://github.com/xinyu1205/recognize-anything) |

### 🔧 Data Processing Frameworks

| Framework | Description | Link |
|-----------|-------------|------|
| MMEval | Multimodal model evaluation framework | [GitHub](https://github.com/open-compass/MMEval) |
| LLaVA-NeXT | Next-generation vision-language assistant | [Website](https://llava-vl.github.io/) |

---

## 📊 Benchmark Datasets

### 🎯 Instruction-Following Benchmarks

| Benchmark | Description | Link |
|-----------|-------------|------|
| MMBench | Comprehensive multimodal capability evaluation | [GitHub](https://github.com/open-compass/MMBench) |
| SEED-Bench | Hierarchical multimodal understanding evaluation | [GitHub](https://github.com/AILab-CVC/SEED-Bench) |
| LLaVA-Bench | In-the-wild instruction-following evaluation | [GitHub](https://github.com/haotian-liu/LLaVA) |

### 📝 Task-Specific Benchmarks

| Benchmark | Description | Link |
|-----------|-------------|------|
| VQAv2 | Visual question answering | [Website](https://visualqa.org/) |
| GQA | Compositional reasoning evaluation | [Website](https://cs.stanford.edu/people/dorarad/gqa/) |
| MMMU | Multimodal multi-task understanding | [Website](https://mmmu-benchmark.github.io/) |

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

[![Star History Chart](https://api.star-history.com/svg?repos=opendatalab-raiser/Awesome-Multimodal-Data-Recipe&type=Date)](https://star-history.com/#opendatalab-raiser/Awesome-Multimodal-Data-Recipe&Date)

---

## 📄 License

This project is licensed under [CC0-1.0 License](LICENSE).

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

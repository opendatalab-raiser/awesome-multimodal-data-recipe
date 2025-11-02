# Assets Directory

This directory contains all images, figures, and logos used in the Awesome Multimodal Data Recipe repository.

## 📁 Directory Structure

```
assets/
├── images/          # Paper figures and diagrams
├── figures/         # Custom illustrations and charts
└── logos/           # Project and organization logos
```

## 📸 Image Categories

### `images/` - Paper Figures

Contains figures extracted from research papers.

**Naming Convention:**
```
paper-[first-author-last-name]-[year]-fig[number].[ext]
```

**Examples:**
- `paper-radford-2021-fig1.png` - Figure 1 from Radford et al. 2021 (CLIP paper)
- `paper-liu-2024-fig2.jpg` - Figure 2 from Liu et al. 2024 (LLaVA paper)
- `paper-gan-2023-architecture.png` - Architecture diagram from Gan et al. 2023

**Guidelines:**
- ✅ Extract key figures that illustrate data synthesis methods
- ✅ Prefer vector formats (SVG, PDF) when available
- ✅ Use PNG for screenshots and raster images
- ✅ Keep file sizes under 500KB
- ✅ Always credit original authors in captions

### `figures/` - Custom Illustrations

Contains custom-created diagrams, charts, and illustrations.

**Naming Convention:**
```
custom-[description]-[date].[ext]
```

**Examples:**
- `custom-taxonomy-diagram-2025-01.svg` - Custom taxonomy visualization
- `custom-comparison-chart-2025-01.png` - Comparison chart
- `custom-workflow-diagram.svg` - Workflow illustration

**Guidelines:**
- ✅ Use vector formats (SVG) for diagrams when possible
- ✅ Include source files (e.g., .ai, .sketch) if available
- ✅ Maintain consistent visual style
- ✅ Use clear, readable fonts and colors
- ✅ Optimize for both light and dark backgrounds

### `logos/` - Project Logos

Contains logos for the project and referenced organizations.

**Naming Convention:**
```
[organization-name]-logo.[ext]
```

**Examples:**
- `awesome-logo.svg` - Main project logo
- `openai-logo.png` - OpenAI logo
- `microsoft-logo.svg` - Microsoft logo

**Guidelines:**
- ✅ Use official logos from organization websites
- ✅ Prefer SVG format for scalability
- ✅ Include both light and dark versions if available
- ✅ Respect copyright and usage guidelines
- ✅ Keep file sizes minimal

## 📐 Technical Guidelines

### File Formats

| Format | Use Case | Pros | Cons |
|--------|----------|------|------|
| **SVG** | Diagrams, logos, charts | Scalable, small file size, editable | Not ideal for photos |
| **PNG** | Screenshots, complex images | Lossless, transparent background | Larger file size |
| **JPG** | Photos, photographs | Small file size | Lossy compression, no transparency |
| **WebP** | Modern images | Best compression | Limited browser support (older) |

**Recommendation:** Use SVG for diagrams and logos, PNG for screenshots, JPG for photos.

### Image Optimization

Before adding images, optimize them to reduce file size:

```bash
# For PNG files
pngquant input.png --output output.png --quality 80-95

# For JPG files
jpegoptim --max=85 input.jpg

# For SVG files
svgo input.svg -o output.svg
```

**Online tools:**
- [TinyPNG](https://tinypng.com/) - PNG/JPG compression
- [SVGOMG](https://jakearchibald.github.io/svgomg/) - SVG optimization
- [Squoosh](https://squoosh.app/) - Modern image compression

### Size Guidelines

- **Maximum file size:** 500KB per image
- **Recommended width:** 800-1200px for full-width images
- **Thumbnail width:** 200-400px for thumbnails
- **DPI for screenshots:** 72-96 DPI (screen resolution)

## 📝 Usage in Markdown

### Basic Image

```markdown
![Description](assets/images/paper-radford-2021-fig1.png)
```

### Image with Caption

```markdown
<figure>
  <img src="assets/images/paper-radford-2021-fig1.png" alt="CLIP Architecture">
  <figcaption>Figure 1: CLIP architecture from Radford et al. (2021)</figcaption>
</figure>
```

### Responsive Image

```markdown
<img src="assets/images/paper-radford-2021-fig1.png" 
     alt="CLIP Architecture" 
     width="800">
```

### Image in Details/Summary

```markdown
<details>
    <summary>Key Figures</summary>
    
    ![Architecture Diagram](assets/images/paper-radford-2021-fig1.png)
    
    **Figure 1**: CLIP architecture showing the dual-encoder design.
</details>
```

## ⚖️ Copyright and Attribution

### Fair Use Guidelines

When including images from papers:

1. **✅ Always attribute**: Credit the original authors and paper
2. **✅ Link to source**: Provide a link to the original paper
3. **✅ Educational purpose**: Use only for educational/reference purposes
4. **✅ Fair use**: Follow fair use guidelines for academic work
5. **❌ No commercial use**: Don't use for commercial purposes without permission

### Attribution Template

```markdown
![Description](assets/images/paper-author-year-fig1.png)

**Figure from**: [Paper Title](paper_link) by Author et al. (Year)
```

### Example

```markdown
![CLIP Architecture](assets/images/paper-radford-2021-fig1.png)

**Figure 1**: CLIP architecture from [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) by Radford et al. (2021)
```

## 🔍 Finding Images

### From arXiv Papers

1. **HTML version** (easiest):
   - Visit `https://arxiv.org/html/[arxiv-id]`
   - Right-click images and "Save image as..."

2. **PDF version**:
   - Download PDF from `https://arxiv.org/pdf/[arxiv-id].pdf`
   - Use tools like [PDF Image Extractor](https://www.ilovepdf.com/extract_images_pdf)
   - Or take screenshots of figures

3. **LaTeX source**:
   - Download source files from arXiv
   - Find original image files in the source package

### From Papers with Project Pages

Many papers provide high-quality figures on their project pages:
- Check paper websites (often linked in arXiv abstract)
- Look for "Resources" or "Media" sections
- Download official figures when available

## 🛠️ Recommended Tools

### Image Editing

- **[GIMP](https://www.gimp.org/)** - Free Photoshop alternative
- **[Inkscape](https://inkscape.org/)** - Free vector graphics editor
- **[Figma](https://www.figma.com/)** - Online design tool

### Screenshot Tools

- **Windows**: Snipping Tool, Snip & Sketch
- **macOS**: Screenshot app (Cmd+Shift+4)
- **Linux**: GNOME Screenshot, Spectacle

### Batch Processing

- **[ImageMagick](https://imagemagick.org/)** - Command-line image manipulation
- **[XnConvert](https://www.xnview.com/en/xnconvert/)** - Batch image converter

## 📋 Checklist Before Adding Images

- [ ] Image is relevant to the content
- [ ] File name follows naming convention
- [ ] File size is under 500KB
- [ ] Image is optimized for web
- [ ] Proper attribution is included
- [ ] Image is placed in correct subdirectory
- [ ] Image is referenced in README.md or README_zh.md
- [ ] Alternative text (alt text) is provided

## 🚫 What NOT to Include

- ❌ Low-quality or blurry images
- ❌ Images with unclear copyright status
- ❌ Unnecessarily large files (>500KB)
- ❌ Images unrelated to multimodal data synthesis
- ❌ Copyrighted logos without permission
- ❌ Personal photos or identifiable information

## 📧 Questions?

If you have questions about using images:
- Open an issue in the repository
- Check the [CONTRIBUTING.md](../CONTRIBUTING.md) guide
- Refer to fair use guidelines for academic work

---

<p align="center">
  Made with ❤️ for the Awesome Multimodal Data Recipe community
</p>


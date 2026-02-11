# Dataset Card: AI Detector Arena Benchmark

## Dataset Description

**Homepage:** [aidetectorarena.com](https://aidetectorarena.com)

**Repository:** [github.com/AI-Detect-Arena/benchmark-dataset](https://github.com/AI-Detect-Arena/benchmark-dataset)

**Leaderboard:** [aidetectorarena.com](https://aidetectorarena.com)

**Methodology:** [aidetectorarena.com/methodology](https://aidetectorarena.com/methodology)

### Dataset Summary

AI Detector Arena Benchmark is a curated dataset for evaluating AI-generated image detection tools. It contains approximately 2,050 images split evenly between AI-generated content and real photographs.

The dataset is designed to provide:
- **Balanced evaluation** — Equal representation of AI and real images
- **Generator diversity** — 17 state-of-the-art AI image generators
- **Category coverage** — 6 content categories (Portrait, Landscape, Art, Food, Animal, Product)
- **Reproducibility** — Versioned releases with consistent metadata

### Supported Tasks

- **Binary Classification**: AI-generated vs Real photograph detection
- **AI Generator Identification**: Determining which AI model created an image
- **Detector Benchmarking**: Comparing accuracy of AI detection tools

### Languages

Metadata and documentation are in English.

---

## Dataset Structure

### Data Instances

Each image in the dataset has an associated metadata record:

```json
{
  "id": "ai_flux_2_flex_portrait_01",
  "filename": "ai_flux_2_flex_portrait_01.png",
  "is_ai": true,
  "generator": "flux_2_flex",
  "category": "portrait"
}
```

### Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier for the image |
| `filename` | string | Image filename |
| `is_ai` | boolean | True if AI-generated, False if real photograph |
| `generator` | string | AI model name (empty for real images) |
| `category` | string | Content category (portrait, landscape, art, food, animal, product) |

### Data Splits

| Split | Count | Description |
|-------|-------|-------------|
| AI-Generated | ~1,018 | Images from 17 AI generators |
| Real Photos | ~1,032 | Photographs from Unsplash |

---

## Dataset Creation

### Curation Rationale

Existing AI detection benchmarks often suffer from:
- Class imbalance (too few real images)
- Limited generator diversity
- Outdated AI models
- Lack of versioning

This dataset addresses these issues by maintaining balance, including modern generators (late 2024 - early 2025), and using semantic versioning.

### Source Data

#### AI-Generated Images

Images were generated using official APIs with category-specific prompts:

| Generator | Vendor | Images |
|-----------|--------|--------|
| Flux Pro v1.1 | Black Forest Labs | 60 |
| Flux 2 Flex | Black Forest Labs | 60 |
| Flux Schnell | Black Forest Labs | 60 |
| GPT Image 1.5 | OpenAI | 60 |
| Gemini 3 Pro | Google | 60 |
| Grok Aurora | xAI | 60 |
| Stable Diffusion 3.5 Large | Stability AI | 60 |
| Ideogram v3 | Ideogram | 60 |
| Leonardo Phoenix | Leonardo AI | 60 |
| Recraft v3 | Recraft | 60 |
| Hunyuan v3 | Tencent | 60 |
| Seedream v3 | ByteDance | 60 |
| Seedream v4 | ByteDance | 60 |
| Qwen 2512 | Alibaba | 60 |
| GLM Image | Zhipu AI | 60 |
| Wan v2.6 | Alibaba | 60 |
| Z Image | — | 59 |

#### Real Photographs

Real images are sourced from the [Unsplash Lite Dataset](https://unsplash.com/data), consisting of professional photographs under the Unsplash License.

### Annotations

Ground truth labels are derived from the source:
- AI images: Known to be generated (API provenance)
- Real images: Known to be photographs (Unsplash source)

No human annotation was required for binary classification.

---

## Considerations for Using the Data

### Social Impact

This dataset supports the development of AI detection tools, which have applications in:
- Content moderation
- Academic integrity
- Journalism verification
- Copyright protection

### Discussion of Biases

**Known biases:**
- Real images are professional photographs (Unsplash), not casual snapshots
- AI images use standard API settings, not adversarial prompts
- Limited to 6 categories; specialized domains may differ
- No social media compression artifacts

### Limitations

This benchmark does **not** cover:
- AI-edited or inpainted images
- Video or audio deepfakes
- Images with social media compression
- Adversarial attacks on detectors
- Generators released after January 2025

See [methodology.md](methodology.md) for full limitations.

---

## Additional Information

### Dataset Curators

AI Detector Arena team.

### Licensing

- **Code**: MIT License
- **Metadata & Documentation**: CC-BY-4.0
- **AI Images**: Generated via official APIs for research
- **Real Images**: Unsplash License

### Citation

```bibtex
@misc{aidetectorarena2025,
  title={AI Detector Arena Benchmark Dataset},
  author={AI Detector Arena},
  year={2025},
  url={https://aidetectorarena.com/benchmark-dataset},
  note={Dataset Version 0.1}
}
```

### Contact

- Website: [aidetectorarena.com](https://aidetectorarena.com)
- GitHub: [github.com/AI-Detect-Arena](https://github.com/AI-Detect-Arena)

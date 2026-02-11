# Benchmark Methodology

This document describes the evaluation methodology used by AI Detector Arena to benchmark AI image detection tools.

## 1. Dataset Composition

### Balance
The dataset maintains a near-equal split between AI-generated and real images to ensure unbiased evaluation.

| Class | Count | Percentage |
|-------|-------|------------|
| AI-Generated | ~1,018 | ~50% |
| Real Photos | ~1,032 | ~50% |

### Diversity

**AI Generators (17 total):**
- Flux Pro v1.1, Flux 2 Flex, Flux Schnell (Black Forest Labs)
- GPT Image 1.5 (OpenAI)
- Gemini 3 Pro (Google)
- Grok Aurora (xAI)
- Stable Diffusion 3.5 Large (Stability AI)
- Ideogram v3 (Ideogram)
- Leonardo Phoenix (Leonardo AI)
- Recraft v3 (Recraft)
- Hunyuan v3 (Tencent)
- Seedream v3, Seedream v4 (ByteDance)
- Qwen 2512, Wan v2.6 (Alibaba)
- GLM Image (Zhipu AI)
- Z Image

**Content Categories (6):**
- Portrait, Landscape, Art, Food, Animal, Product

**Real Image Sources:**
- Unsplash Lite Dataset (professional photography)

## 2. Evaluation Protocol

### Image Submission
Each image from the dataset is submitted to every detector being evaluated. Images are sent in their original format without preprocessing.

### Response Collection
For each image, we collect:
- **Binary classification:** AI or Real
- **Confidence score:** 0-100% (when available)
- **Response time:** API latency

### Metrics

**Primary Metric: Accuracy**
```
Accuracy = (True Positives + True Negatives) / Total Images
```

**Secondary Metrics:**
- **Precision:** TP / (TP + FP)
- **Recall:** TP / (TP + FN)
- **F1 Score:** 2 × (Precision × Recall) / (Precision + Recall)

Where:
- TP = AI image correctly identified as AI
- TN = Real image correctly identified as Real
- FP = Real image incorrectly identified as AI
- FN = AI image incorrectly identified as Real

## 3. Ranking Rules

### Combined Score
Detectors are ranked by their accuracy on the benchmark dataset.

### Minimum Test Threshold
Detectors must be tested on at least **50 images** to appear in rankings. This ensures statistical significance.

### Provisional Status
Detectors with **50-199 tests** are marked as "Provisional" to indicate preliminary results.

### Dataset Version
Rankings always display the dataset version used. Results from different versions are not directly comparable.

## 4. Limitations

### Known Limitations

1. **Dataset Size:** ~2,000 images may not capture all edge cases
2. **Generator Coverage:** New AI generators may not be represented
3. **Temporal Bias:** Dataset reflects AI capabilities at time of creation
4. **Format Bias:** Original quality images; no social media compression
5. **Content Scope:** Limited to 6 categories; may miss specialized domains

### What This Benchmark Does NOT Measure

- Detection of AI-edited (partially modified) images
- Video or audio deepfake detection
- Text-to-image prompt recovery
- Watermark detection
- Performance on heavily compressed images

## 5. Dataset Versioning

Each dataset version is preserved to ensure reproducibility:

| Version | Images | Release | Notes |
|---------|--------|---------|-------|
| 0.1 | ~2,050 | Feb 2025 | Initial release |

Future versions will add:
- JPEG compression variants
- Additional generators
- Expanded content categories

## 6. Reproducibility

To reproduce benchmark results:

1. Download the dataset from this repository
2. Use the `images_metadata.csv` for ground truth labels
3. Submit images to detectors using their official APIs
4. Calculate metrics using the same formulas above

## References

- Website: [aidetectarena.com](https://aidetectarena.com)
- Dataset: [aidetectarena.com/benchmark-dataset](https://aidetectarena.com/benchmark-dataset)
- Leaderboard: [aidetectarena.com](https://aidetectarena.com)

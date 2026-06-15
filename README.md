# Sovereign AI Hardware & LLM Sizing Calculator

An interactive, single-file web tool for architects, engineers, and AI practitioners to determine whether a target LLM fits on a given hardware profile — and how fast it will run.

## Overview

Local model execution is almost entirely **memory-bandwidth bound**, not compute bound. This calculator audits your hardware across four dimensions: VRAM capacity, memory bandwidth, KV cache size, and CPU offload headroom.

## Running Locally

```bash
python3 launch.py
```

Opens `http://localhost:8080` in your browser automatically. No install required.

## The Math

### VRAM Capacity

$$M_{total} = (P \times \frac{Q}{8} \times 1.2) + M_{kv}$$

| Symbol | Meaning |
|--------|---------|
| $P$ | Total parameters (billions) |
| $Q$ | Quantization bit-width |
| $1.2$ | 20% overhead for activations & framework buffers |
| $M_{kv}$ | KV cache size (scaled by KV quantization factor) |

### Token Generation Speed

$$\text{tok/s} = \frac{\text{Bandwidth (GB/s)} \times \eta}{\text{Active Weight Size (GB)}}$$

For MoE models, **active parameters** drive bandwidth cost — not total parameters. For CPU offload, speed is the harmonic mean of GPU and CPU bandwidth weighted by the layer split percentage.

$$\text{tok/s}_{hybrid} = \frac{1}{\frac{f_{GPU}}{\text{tok/s}_{GPU}} + \frac{f_{CPU}}{\text{tok/s}_{CPU}}}$$

---

## Features

### Hardware
- **VRAM / Unified Memory** — total GPU or Apple Silicon memory
- **GPU Memory Bandwidth** — the primary speed constraint (e.g. RTX 4090 = 1008 GB/s, M3 Max = 300 GB/s)
- **CPU Offload (llama.cpp / Ollama)** — toggle to enable layer splitting between GPU and CPU with an adjustable slider; speed uses harmonic mean of both bandwidths

### Model
- **Architecture** — Dense (all params active per token) or MoE with separate total/active parameter fields
- **Quantization** — FP16 · INT8 · Q6 · Q5 · Q4 · Q3 · Q2
- **MoE sparsity readout** — shows active % and bandwidth cost relative to an equivalent dense model

### KV Cache
- **Context window** — scales cache size linearly
- **KV Cache Quantization** — FP16 / INT8 / Q4, matching llama.cpp `--cache-type-k/v` flags

### Results
- Required VRAM vs. available (color-coded pass/fail)
- Estimated decode speed in tok/s and ms/token
- Visual memory breakdown bar (weights · overhead · KV cache)
- Hybrid speed breakdown when CPU offload is enabled

---

## Deployment

Single-file, zero-build. Requires internet for CDN assets (Alpine.js, Tailwind CSS, IBM Plex Mono font).

1. Clone the repo
2. Run `python3 launch.py` for local use, or
3. Deploy `index.html` via [GitHub Pages](https://pages.github.com/) or [Vercel](https://vercel.com/)

---

## Sovereign AI Focus

Built for organizations running private models on their own hardware — no cloud API dependency, no telemetry.

*"If you don't own the hardware, you don't own the intelligence."*

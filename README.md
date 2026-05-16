# Sovereign AI Hardware & LLM Sizing Calculator

An interactive, web-based utility for architects, engineers, and AI practitioners to determine the maximum Large Language Model (LLM) size a specific hardware profile can support without compromising on latency.

## 🚀 Overview

In the generative era, local model execution speed is rarely limited by the number of compute cores (TFLOPS). Instead, it is almost entirely **memory-bandwidth bound**. This calculator provides a mathematical audit of your hardware to ensure your model fits entirely within VRAM and calculates the expected tokens-per-second based on your memory bus width.

## 📐 The Mathematics of Latency

This tool utilizes two primary formulas to determine model feasibility and performance.

### 1. VRAM Capacity Formula
To avoid "swapping" to system RAM (which causes a ~95% drop in speed), the model and its operational buffers must fit within available Video RAM.

$$M_{total} = (P \times \frac{Q}{8} \times 1.2) + M_{context}$$

* **$P$ (Parameters):** Total count of model weights (in Billions).
* **$Q$ (Quantization):** Bit-precision (e.g., 4-bit, 8-bit). Dividing by 8 converts bits to bytes.
* **1.2:** A 20% multiplier for framework overhead and activation buffers.
* **$M_{context}$:** The memory required for the **KV (Key-Value) Cache**, which grows with the length of the conversation history.

### 2. Token Generation Latency
Because LLM generation is sequential, every parameter must be read from memory to compute a single token. Therefore, your **Memory Bandwidth** is the speed limit.

$$\text{Tokens Per Second} = \frac{\text{Memory Bandwidth (GB/s)} \times \eta}{\text{Model Size (GB)}}$$

* **$\eta$ (Efficiency Factor):** Real-world utilization of the memory bus (typically 80-85%).
* **Model Size:** The raw weight size ($P \times \frac{Q}{8}$).

---

## 🛠️ Features

- **Interactive Sizing:** Real-time calculation of VRAM requirements.
- **Latency Estimation:** Predicts tokens per second and milliseconds per token.
- **Safety Alerts:** Visual warnings when model requirements exceed hardware capacity.
- **Educational Tooltips:** Hover-over explanations for technical terms like *Quantization*, *KV Cache*, and *Memory Bandwidth*.

## 📦 Deployment

This is a single-file solution using **Tailwind CSS** for styling and **Alpine.js** for reactivity. 

1.  Save the provided `index.html` to your local machine.
2.  Host it for free via [GitHub Pages](https://pages.github.com/) or [Vercel](https://vercel.com/).
3.  Share the link in your internal Slack channels or LinkedIn posts to help others audit their AI infrastructure.

---

## 🛡️ Sovereign AI Focus

This calculator is designed for the **Sovereign AI** movement—enabling organizations to run private models on their own "Big Iron" or edge hardware without relying on third-party API providers.

*“If you don't own the hardware, you don't own the intelligence.”*

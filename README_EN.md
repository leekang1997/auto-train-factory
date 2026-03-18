# Auto-Train-Factory

[中文](./README.md) | [English](./README_EN.md)

`Auto-Train-Factory` is an automation toolkit built around the LLaMA-Factory workflow. Its goal is to connect dataset registration, config generation, training orchestration, evaluation, and LoRA export into a single Python-based pipeline.

## Project Positioning

Many fine-tuning workflows run into the same issues:

- dataset registration requires manual edits
- training YAML files are copied and patched repeatedly
- experiment naming becomes messy over time
- training, evaluation, and export live in separate scripts
- shell-based workflows become hard to maintain and reproduce

This project turns those repeated steps into reusable code.

## Current Capabilities

- automatically updates `dataset_info.json`
- automatically generates training YAML files
- prepares training workflows for `llamafactory-cli train`
- supports evaluation output generation through an OpenAI-compatible endpoint
- generates export YAML files for LoRA merge workflows

## What Is Already Included In This Repo

- `auto_train_factory/dataset.py`
  - dataset registration logic
- `auto_train_factory/trainer.py`
  - training YAML generation
- `auto_train_factory/evaluator.py`
  - evaluation result export via OpenAI-compatible APIs
- `auto_train_factory/exporter.py`
  - export YAML generation for LoRA merge workflows
- `configs/*.example.yaml`
  - example configs for training, evaluation, and export
- `examples/`
  - minimal usage examples

## Source Origin

- derived from internal Python prototypes for SFT training, evaluation, and LoRA export
- representative scripts:
  - `2_自动化训练脚本_3b_sft_lora copy.py`
  - `3_测评大模型.py`
  - `merge_lora.py`

## Good Technical Highlights

- automated LLaMA-Factory training orchestration
- dataset and config registration
- cleaner experiment naming
- vLLM-based evaluation flow
- LoRA export automation for downstream delivery

## One-Line Resume Version

Built an automated LLaMA-Factory fine-tuning pipeline that supports dataset registration, YAML generation, training orchestration, vLLM-based evaluation, and LoRA export, turning LLM tuning workflows into code-driven infrastructure.

## Remaining Cleanup Work

- remove business-specific hard-coded paths
- move script-top constants into config files
- expose training, evaluation, and export as separate commands
- add retry behavior and logging conventions
- add dependency metadata, license, and example data notes

## Recommended Initial Repo Structure

```text
auto-train-factory/
├── README.md
├── README_EN.md
├── LICENSE
├── requirements.txt
├── configs/
│   ├── train.example.yaml
│   ├── eval.example.yaml
│   └── export.example.yaml
├── auto_train_factory/
│   ├── __init__.py
│   ├── dataset.py
│   ├── trainer.py
│   ├── evaluator.py
│   └── exporter.py
└── examples/
    ├── register_and_build_train_yaml.py
    └── build_export_yaml.py
```

## Quick Start

```bash
pip install -r requirements.txt
python examples/register_and_build_train_yaml.py
python examples/build_export_yaml.py
```

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

## Why This Project Exists

In many LLM fine-tuning workflows, the most time-consuming part is not training itself, but the surrounding repetitive engineering work.

- every new dataset requires manual registration changes
- every new experiment starts from copying and editing another YAML file
- evaluation and export are often handled by separate ad hoc scripts
- output folders, logs, and run names become messy across repeated experiments

This project exists to turn those scattered steps into one reusable Python workflow so that fine-tuning becomes easier to reproduce, easier to hand over, and easier to maintain in a team setting.

## How To Use It

A typical usage flow looks like this:

1. Prepare your training data, for example in `jsonl` format.
2. Define a `TrainJobConfig` with model path, dataset name, output directory, and training hyperparameters.
3. Call `register_dataset` to update `dataset_info.json`.
4. Call `build_train_yaml` to generate the LLaMA-Factory training config.
5. After training, use the evaluation module to export inference results.
6. Use the export module to build the LoRA merge config for delivery or deployment.

It is especially useful for:

- personal research with frequent experiment iteration
- labs where multiple people share one training workflow
- small teams that want a cleaner fine-tuning pipeline
- projects that need a trackable train-eval-export lifecycle

## How The Project Works

The current repository organizes the workflow into four understandable modules:

- `dataset.py`
  - registers datasets into the metadata file expected by LLaMA-Factory
- `trainer.py`
  - turns training parameters into standard YAML configs
- `evaluator.py`
  - sends test prompts to an OpenAI-compatible endpoint and saves normalized outputs
- `exporter.py`
  - builds the config needed for LoRA merge and export

In other words, the goal is not to replace the training framework itself, but to add a reusable automation layer around it.

## How It Helps Others

- helps researchers spend less time on repetitive configuration work
- helps teams keep training runs, outputs, and experiment versions organized
- helps new contributors understand the workflow faster
- helps projects connect training, evaluation, and export into one stable pipeline

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

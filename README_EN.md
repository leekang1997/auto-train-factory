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

## Prerequisites

This repository is not a standalone replacement for `LLaMA-Factory`. It is an automation layer built on top of the `LLaMA-Factory` training workflow.

Before using this project, you should:

1. install `LLaMA-Factory` first
2. make sure `llamafactory-cli train` already works on your machine
3. know where your local `LLaMA-Factory` installation lives
4. point this project's config paths to your local `LLaMA-Factory` directory and data files

Without a working `LLaMA-Factory` installation, this repository can help generate configs and organize workflow steps, but it cannot run the actual training by itself.

## Why This Project Exists

In many LLM fine-tuning workflows, the most time-consuming part is not training itself, but the surrounding repetitive engineering work.

- every new dataset requires manual registration changes
- every new experiment starts from copying and editing another YAML file
- evaluation and export are often handled by separate ad hoc scripts
- output folders, logs, and run names become messy across repeated experiments

This project exists to turn those scattered steps into one reusable Python workflow so that fine-tuning becomes easier to reproduce, easier to hand over, and easier to maintain in a team setting.

## How To Use It

A typical usage flow looks like this:

1. Install and validate `LLaMA-Factory` first.
2. Prepare your training data, for example in `jsonl` format.
3. Locate the `data/dataset_info.json` file inside your local `LLaMA-Factory` installation.
4. Define a `TrainJobConfig` with model path, dataset name, output directory, training hyperparameters, and `dataset_info_path`.
5. Call `register_dataset` to update the `dataset_info.json` used by `LLaMA-Factory`.
6. Call `build_train_yaml` to generate the training YAML.
7. Pass that YAML to `llamafactory-cli train` to run the actual fine-tuning job.
8. After training, use the evaluation module to export inference results.
9. Use the export module to build the LoRA merge config for delivery or deployment.

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

## What Paths Need To Be Configured

At minimum, you need to align the following path types with your own environment:

- `LLaMA-Factory` installation directory
  - this determines where training commands run and where `dataset_info.json` actually lives
- `dataset_info_path`
  - this should usually point to `LLaMA-Factory/data/dataset_info.json`
- `model_path`
  - the base model you want to fine-tune
- `dataset_file`
  - your training dataset file
- `output_dir`
  - where training artifacts should be written
- `yaml_output_path`
  - where the generated training YAML should be saved

The key idea is:

- this repository is responsible for generating configs and organizing workflow steps
- `LLaMA-Factory` is still responsible for executing the actual training

So if your paths do not point to the correct local `LLaMA-Factory` installation, the workflow will break.

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
git clone https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
# follow the official LLaMA-Factory installation guide

cd /path/to/auto-train-factory
pip install -r requirements.txt
python examples/register_and_build_train_yaml.py
python examples/build_export_yaml.py
```

## A More Accurate Mental Model

It is best to think about this project as:

- an automation layer on top of `LLaMA-Factory`
- not a fully independent training framework

So the practical sequence is:

- install `LLaMA-Factory` first
- then use this repository to reduce the repetitive engineering work around it

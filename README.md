# Auto-Train-Factory

[中文](./README.md) | [English](./README_EN.md)

`Auto-Train-Factory` 是一个面向 LLaMA-Factory 工作流的自动化训练工具链，目标是把数据注册、配置生成、训练调度、评测和 LoRA 合并串成统一的 Python 流程。

## 项目定位

在大模型微调过程中，很多团队都会遇到这些问题：

- 数据集注册需要手工改配置
- 训练 YAML 容易反复复制粘贴
- 多次实验命名混乱
- 训练、评测、导出分散在不同脚本里
- 大量 Shell 脚本难维护、难复现

这个项目希望把这些步骤变成代码化、模板化、可复用的流水线。

## 当前能力

- 自动写入 `dataset_info.json`
- 自动生成训练 YAML
- 自动启动 `llamafactory-cli train`
- 自动记录训练日志
- 自动拉起 vLLM 进行评测
- 自动执行 LoRA 权重合并导出

## 当前仓库已包含

- `auto_train_factory/dataset.py`
  - 训练数据集注册逻辑
- `auto_train_factory/trainer.py`
  - 训练 YAML 生成逻辑
- `auto_train_factory/evaluator.py`
  - 基于 OpenAI 兼容接口的评测结果导出逻辑
- `auto_train_factory/exporter.py`
  - LoRA 合并导出 YAML 生成逻辑
- `configs/*.example.yaml`
  - 训练、评测、导出配置示例
- `examples/`
  - 最小可运行的示例脚本

## 对应源码原型

- Python 自动化 SFT 训练、评测与 LoRA 导出脚本原型
- 关键脚本：
  - `2_自动化训练脚本_3b_sft_lora copy.py`
  - `3_测评大模型.py`
  - `merge_lora.py`

## 适合展示的技术点

- LLaMA-Factory 自动训练调度
- 数据集与配置自动注册
- 训练实验命名规范化
- vLLM 自动评测
- LoRA 导出与模型交付流程自动化

## 适合写进简历的一句话

面向 LLaMA-Factory 构建自动化训练流水线，支持数据集注册、YAML 生成、训练调度、vLLM 自动评测与 LoRA 合并导出，实现大模型微调工作流代码化。

## 当前需要清洗的内容

- 抽离业务写死目录
- 用统一配置文件替代脚本顶部硬编码
- 把训练、评测、合并拆成子命令
- 补充失败重试和日志目录约定
- 补依赖文件、许可证和示例数据说明

## 推荐的仓库初始结构

```text
auto-train-factory/
├── README.md
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
    ├── run_train.py
    ├── run_eval.py
    └── run_export.py
```

## 快速开始

```bash
pip install -r requirements.txt
python examples/register_and_build_train_yaml.py
python examples/build_export_yaml.py
```

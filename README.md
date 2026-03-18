# Auto-Train-Factory

[中文](./README.md) | [English](./README_EN.md)

`Auto-Train-Factory` 是一个面向 LLaMA-Factory 工作流的自动化训练工具链，目标是把数据注册、配置生成、训练调度、评测和 LoRA 合并串成统一的 Python 流程。

## 一眼看懂

- 项目类型：`LLaMA-Factory` 的自动化增强层
- 核心目标：减少微调实验中重复、零散、难复现的工程劳动
- 适合人群：做 SFT / LoRA 微调的研究者、实验室和小团队
- 依赖前提：必须先安装并跑通 `LLaMA-Factory`
- 当前阶段：开源初版，重点展示流程抽象与工程组织思路

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

## 使用前提

这个仓库不是独立替代 `LLaMA-Factory` 的训练框架，而是构建在 `LLaMA-Factory` 之上的自动化工具层。

这意味着你在使用它之前，必须先完成下面几件事：

1. 先单独安装好 `LLaMA-Factory`
2. 确保本地已经能正常执行 `llamafactory-cli train`
3. 确定你的 `LLaMA-Factory` 安装目录
4. 在本项目配置中，把相关路径指向你本地的 `LLaMA-Factory` 目录和数据目录

如果没有先装好 `LLaMA-Factory`，这个仓库只能帮你生成配置和组织流程，不能真正完成训练。

## 这个项目是为了解决什么

如果你经常做大模型微调，很容易遇到一个问题：真正耗时间的往往不是“训练本身”，而是训练前后那些重复又容易出错的工程动作。

- 每次换数据集都要手工改注册配置
- 每次新实验都要复制一份 YAML 再改参数
- 训练完之后还要单独写评测脚本、导出脚本
- 做多轮实验时，日志、输出目录和版本名容易混乱

这个项目的目标，就是把这些散落在不同脚本里的重复劳动统一收束到一条 Python 工作流里，让训练实验更容易复现、更容易交接、也更适合团队协作。

## 如何使用这个项目

一个典型使用流程是这样的：

1. 先安装并验证 `LLaMA-Factory`。
2. 准备好训练数据文件，例如 `jsonl` 格式的 SFT 数据。
3. 找到你本地 `LLaMA-Factory` 里的 `data/dataset_info.json` 路径。
4. 用 `TrainJobConfig` 描述模型路径、数据集名称、输出目录、训练超参数，以及 `dataset_info_path`。
5. 调用 `register_dataset` 把数据集写入 `LLaMA-Factory` 使用的 `dataset_info.json`。
6. 调用 `build_train_yaml` 生成训练 YAML。
7. 把生成出来的 YAML 交给 `llamafactory-cli train` 去真正执行训练。
8. 训练完成后，再用评测模块生成推理评测结果。
9. 最后用导出模块生成 LoRA 合并配置，进入模型交付流程。

它适合下面这些场景：

- 个人研究中的频繁试参
- 实验室里多同学共享训练流程
- 小团队内部统一微调工作流
- 需要保留训练、评测、导出全流程痕迹的项目

## 这个项目大概是怎么工作的

这个仓库当前的思路是把训练链路拆成 4 个可以独立理解的模块：

- `dataset.py`
  - 负责把数据集信息注册到 LLaMA-Factory 所需的数据索引文件里
- `trainer.py`
  - 负责把训练参数整理成标准 YAML，减少反复手写配置的成本
- `evaluator.py`
  - 负责把测试数据送到 OpenAI 兼容接口，并保存统一格式的评测结果
- `exporter.py`
  - 负责生成 LoRA 合并导出所需的配置，方便进入部署或共享环节

也就是说，它不是重新发明训练框架，而是在现有训练框架外面补了一层更适合实验组织和工程复用的自动化壳。

## 你需要配置哪些路径

当前这套代码至少要和下面几类路径对齐：

- `LLaMA-Factory` 安装目录
  - 用来确定训练命令运行位置，以及 `dataset_info.json` 的实际位置
- `dataset_info_path`
  - 通常应当指向 `LLaMA-Factory/data/dataset_info.json`
- `model_path`
  - 你要微调的基座模型路径
- `dataset_file`
  - 你的训练数据文件路径
- `output_dir`
  - 训练输出目录
- `yaml_output_path`
  - 自动生成的训练 YAML 保存位置

最关键的一点是：

- 这个项目负责“生成配置、组织流程、连接训练前后步骤”
- `LLaMA-Factory` 负责“真正执行训练”

所以如果路径没有正确指向你本地的 `LLaMA-Factory` 安装位置，流程就会断掉。

## 它能给大家带来什么帮助

- 帮研究者减少大量重复配置工作，把时间留给数据和实验设计
- 帮团队把“谁训练的、怎么训练的、结果放哪了”这件事整理清楚
- 帮新成员更快接手微调流程，不必从一堆零散脚本开始摸索
- 帮项目把训练、评测、导出串成一个更稳定的可复用链路

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
git clone https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
# 按 LLaMA-Factory 官方文档完成安装

cd /path/to/auto-train-factory
pip install -r requirements.txt
python examples/register_and_build_train_yaml.py
python examples/build_export_yaml.py
```

## 一个更准确的上手思路

你可以把这个项目理解成：

- 先安装 `LLaMA-Factory`
- 再用本仓库帮你减少围绕 `LLaMA-Factory` 的重复工程劳动

也就是说，它更像：

- `LLaMA-Factory` 的自动化增强层
- 而不是一个完全独立的新训练框架

from dataclasses import dataclass, field


@dataclass(slots=True)
class TrainJobConfig:
    model_path: str
    dataset_name: str
    dataset_file: str
    dataset_info_path: str
    output_dir: str
    yaml_output_path: str
    stage: str = "sft"
    finetuning_type: str = "lora"
    lora_target: str = "all"
    template_name: str = "qwen"
    cutoff_len: int = 8192
    train_batch_size: int = 1
    gradient_accumulation_steps: int = 4
    learning_rate: float = 1e-4
    num_train_epochs: float = 3.0
    logging_steps: int = 10
    save_steps: int = 200
    overwrite_output_dir: bool = True
    bf16: bool = True
    flash_attn: str = "fa2"
    columns_prompt: str = "prompt"
    columns_query: str = "input"
    columns_response: str = "output"


@dataclass(slots=True)
class EvalTarget:
    model_path: str
    test_json: str
    port: int
    served_model_name: str = "mymodel"


@dataclass(slots=True)
class EvalJobConfig:
    output_dir: str
    gpu_devices: list[str] = field(default_factory=lambda: ["0"])
    host: str = "127.0.0.1"
    timeout_seconds: int = 300
    vllm_python_executable: str = "python3"
    activation_command: str | None = None


@dataclass(slots=True)
class ExportJobConfig:
    model_path: str
    adapter_path: str
    export_dir: str
    export_yaml_path: str
    template_name: str = "qwen"
    export_size: int = 2
    export_device: str = "cpu"
    export_legacy_format: bool = False

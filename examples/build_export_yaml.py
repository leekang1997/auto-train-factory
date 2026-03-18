from auto_train_factory import ExportJobConfig, build_export_yaml


config = ExportJobConfig(
    model_path="/path/to/base-model",
    adapter_path="/path/to/lora-adapter",
    export_dir="./outputs/exported-model",
    export_yaml_path="./outputs/export.yaml",
)

print(build_export_yaml(config))

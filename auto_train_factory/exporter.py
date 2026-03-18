from pathlib import Path

from .config import ExportJobConfig


EXPORT_TEMPLATE = """### Note: DO NOT use quantized model or quantization_bit when merging lora adapters

### model
model_name_or_path: {model_path}
adapter_name_or_path: {adapter_path}
template: {template_name}
finetuning_type: lora

### export
export_dir: {export_dir}
export_size: {export_size}
export_device: {export_device}
export_legacy_format: {export_legacy_format}
"""


def build_export_yaml(config: ExportJobConfig) -> str:
    yaml_content = EXPORT_TEMPLATE.format(
        model_path=config.model_path,
        adapter_path=config.adapter_path,
        template_name=config.template_name,
        export_dir=config.export_dir,
        export_size=config.export_size,
        export_device=config.export_device,
        export_legacy_format=str(config.export_legacy_format).lower(),
    )
    output_path = Path(config.export_yaml_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(yaml_content, encoding="utf-8")
    return yaml_content

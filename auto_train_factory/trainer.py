from pathlib import Path

from .config import TrainJobConfig


TRAIN_TEMPLATE = """### model
model_name_or_path: {model_path}

### method
stage: {stage}
do_train: true
finetuning_type: {finetuning_type}
lora_target: {lora_target}

### dataset
dataset: {dataset_name}
template: {template_name}
cutoff_len: {cutoff_len}

### output
output_dir: {output_dir}
logging_steps: {logging_steps}
save_steps: {save_steps}
overwrite_output_dir: {overwrite_output_dir}

### train
per_device_train_batch_size: {train_batch_size}
gradient_accumulation_steps: {gradient_accumulation_steps}
learning_rate: {learning_rate}
num_train_epochs: {num_train_epochs}
bf16: {bf16}
flash_attn: {flash_attn}
"""


def build_train_yaml(config: TrainJobConfig) -> str:
    yaml_content = TRAIN_TEMPLATE.format(
        model_path=config.model_path,
        stage=config.stage,
        finetuning_type=config.finetuning_type,
        lora_target=config.lora_target,
        dataset_name=config.dataset_name,
        template_name=config.template_name,
        cutoff_len=config.cutoff_len,
        output_dir=config.output_dir,
        logging_steps=config.logging_steps,
        save_steps=config.save_steps,
        overwrite_output_dir=str(config.overwrite_output_dir).lower(),
        train_batch_size=config.train_batch_size,
        gradient_accumulation_steps=config.gradient_accumulation_steps,
        learning_rate=config.learning_rate,
        num_train_epochs=config.num_train_epochs,
        bf16=str(config.bf16).lower(),
        flash_attn=config.flash_attn,
    )
    output_path = Path(config.yaml_output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(yaml_content, encoding="utf-8")
    return yaml_content

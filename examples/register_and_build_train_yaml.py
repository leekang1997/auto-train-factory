from auto_train_factory import TrainJobConfig, build_train_yaml, register_dataset


config = TrainJobConfig(
    model_path="/path/to/model",
    dataset_name="demo-sft",
    dataset_file="/path/to/data.jsonl",
    dataset_info_path="./outputs/dataset_info.json",
    output_dir="./outputs/demo-sft",
    yaml_output_path="./outputs/demo-sft/train.yaml",
)

register_dataset(config)
print(build_train_yaml(config))

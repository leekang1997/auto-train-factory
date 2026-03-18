import json
from pathlib import Path

from .config import TrainJobConfig


def register_dataset(config: TrainJobConfig) -> str:
    dataset_info_path = Path(config.dataset_info_path)
    dataset_info_path.parent.mkdir(parents=True, exist_ok=True)
    if dataset_info_path.exists():
        data = json.loads(dataset_info_path.read_text(encoding="utf-8"))
    else:
        data = {}

    data[config.dataset_name] = {
        "file_name": config.dataset_file,
        "columns": {
            "prompt": config.columns_prompt,
            "query": config.columns_query,
            "response": config.columns_response,
        },
    }
    dataset_info_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return config.dataset_name

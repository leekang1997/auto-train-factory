import json
from pathlib import Path
from typing import Any

import requests


def evaluate_chat_dataset(
    *,
    api_url: str,
    served_model_name: str,
    test_json_path: str,
    output_file_path: str,
    timeout_seconds: int = 300,
) -> list[dict[str, Any]]:
    test_data = json.loads(Path(test_json_path).read_text(encoding="utf-8"))
    results: list[dict[str, Any]] = []
    headers = {"Content-Type": "application/json"}

    for item in test_data:
        prompt = f"{item['prompt']}\n{item['input']}"
        payload = {
            "model": served_model_name,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.0,
        }
        try:
            response = requests.post(api_url, headers=headers, json=payload, timeout=timeout_seconds)
            response.raise_for_status()
            response_data = response.json()
            predicted_output = response_data["choices"][0]["message"]["content"].strip()
        except Exception as exc:
            predicted_output = f"ERROR: {exc}"

        results.append(
            {
                "prompt": prompt,
                "predicted_output": predicted_output,
                "true_output": item["output"].strip(),
            }
        )

    output_path = Path(output_file_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    return results

import torch
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig
)

MODEL_NAME = "Qwen2.5-Coder-32B-Instruct"
MODEL_PATH = f"/home/ai_admin/dp_models/coding_models/{MODEL_NAME}"

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH,
    trust_remote_code=True
)

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    quantization_config=bnb_config,
    device_map="sequential",
    trust_remote_code=True
)

model.eval()

with open("system_prompt_body.txt", "r", encoding="utf-8") as f:
    system_body = f.read().strip()

tasks = [
    "Write a single code out of a series of codes. The objective is Order a pizza from a nearby restaurant",
    "download the current weather for new york using a public api and print the temperature",
    "scrape the top 5 trending repositories from github and display their names",
    "count the number of lines in all .py files in the current directory"
]

for idx, task_description in enumerate(tasks, start=1):

    print("\n" + "=" * 120)
    print(f"TASK {idx}")
    print(task_description)
    print("=" * 120)

    system_prompt = (
        system_body
        + "\n\n"
        + "task description: "
        + task_description
    )

    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    print("\nPROMPT\n")
    print(prompt)

    inputs = tokenizer(
        prompt,
        return_tensors="pt"
    ).to("cuda")

    with torch.no_grad():

        outputs = model.generate(
            **inputs,
            max_new_tokens=1024,
            temperature=0.4,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )

    generated_tokens = outputs[0][inputs["input_ids"].shape[-1]:]

    content = tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True
    )

    print("\nRAW OUTPUT")
    print("-" * 120)
    print(content)
    print("-" * 120)

    print("\nREPR OUTPUT")
    print("-" * 120)
    print(repr(content))
    print("-" * 120)

    print("\nSTART CHECKS")
    print("startswith ```python :", content.strip().startswith("```python"))
    print("startswith ```bash   :", content.strip().startswith("```bash"))
    print("startswith ```sh     :", content.strip().startswith("```sh"))

    if len(content.strip()) > 100:
        print("\nFIRST 100 CHARS")
        print(repr(content.strip()[:100]))

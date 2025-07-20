from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load model and tokenizer once
tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
model = AutoModelForCausalLM.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
device = torch.device("cpu")
model.to(device)

# Injected business knowledge
SYSTEM_PROMPT = (
    "TorkeHub is a white-label CRM used for business automation. "
    "It helps streamline client communication and sales workflows."
)

# ✅ Fast-access Knowledge Base (add more if needed)
knowledge_base = {
    "what is torkehub": "TorkeHub is a white-label CRM used to automate business workflows, manage clients, and streamline communication.",
    "who built torkehub": "TorkeHub was developed by a team of passionate full stack engineers during a cutting-edge AI internship.",
    "what is tinyllama": "TinyLlama is a small, open-source language model designed to run fast on CPU while giving intelligent replies."
}

def generate_answer(user_question):
    q_lower = user_question.strip().lower()

    # ⚡ Check if question exists in knowledge base
    if q_lower in knowledge_base:
        return knowledge_base[q_lower]

    # 🧠 Else, use TinyLlama model
    full_prompt = (
        f"<|system|>\n{SYSTEM_PROMPT}</s>\n"
        f"<|user|>\n{user_question}</s>\n"
        f"<|assistant|>\n"
    )

    inputs = tokenizer(full_prompt, return_tensors="pt").to(device)

    with torch.inference_mode():
        outputs = model.generate(
            **inputs,
            max_new_tokens=40,
            do_sample=True,
            top_k=50,
            top_p=0.95
        )

    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded.split("<|assistant|>")[-1].strip()

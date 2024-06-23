import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from utils import reorder_sentences

model_id = "meta-llama/Meta-Llama-3-8B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

def generate_new_report_Llama3(report, reorder=False):

    if reorder == True:
        report = reorder_sentences(report)

    messages = [
        {"role": "system", "content": "Imagine you are an expert radiologist specializing in chest imaging. You receive various reports that your students have prepared. Your task is to improve these reports by changing all the words while preserving the pathology terms and the same meaning."},
        
        {"role": "user", "content": "Enhance the following report by changing the words, and sentence order. Returns only the new report, without saying Here is the enhanced report nor introduce it: " + report},
    ]

    input_ids = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        return_tensors="pt"
    ).to(model.device)

    terminators = [
        tokenizer.eos_token_id,
        tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]

    outputs = model.generate(
        input_ids,
        pad_token_id=tokenizer.eos_token_id,
        max_new_tokens=512,
        eos_token_id=terminators,
        do_sample=True,
        temperature=1.2, # 0.6
        top_p=0.9,
    )
    response = outputs[0][input_ids.shape[-1]:]
    new_report = tokenizer.decode(response, skip_special_tokens=True)

    return new_report

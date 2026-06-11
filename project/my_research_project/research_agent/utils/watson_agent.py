import os
from ibm_watsonx_ai.foundation_models import ModelInference

def get_granite_client():
    """Initializes the connection to IBM watsonx.ai using Granite 4.1."""
    credentials = {
        "url": "https://us-south.ml.cloud.ibm.com", # Change region if needed
        "apikey": os.getenv("e4jdglZuuzjXj7xEcJBgMNcmaB92Bp2w-qoKFC8NOFW")
    }
    
    project_id = os.getenv("3ebc9a77-1f61-4e2a-b145-b75533950de3")
    model_id = "ibm/granite-4-1-8b-instruct"  # High performance enterprise model
    
    # Lite limits can be managed through tweakable generation parameters
    gen_params = {
        "decoding_method": "greedy",
        "max_new_tokens": 1024,
        "temperature": 0.3
    }
    
    return ModelInference(
        model_id=model_id,
        credentials=credentials,
        params=gen_params,
        project_id=project_id
    )

def query_research_agent(prompt_text, system_instruction):
    """Executes a research prompt against the IBM Granite LLM."""
    client = get_granite_client()
    formatted_prompt = f"<|system|>\n{system_instruction}\n<|user|>\n{prompt_text}\n<|assistant|>\n"
    
    response = client.generate_text(prompt=formatted_prompt)
    return response
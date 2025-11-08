def model_return(model):
    #One of the best free-tier models for structured Q&A. Use text-generation
    mistralInstruct='mistralai/Mistral-7B-Instruct-v0.2'

    #supports long contexts.
    mixtral='mistralai/Mixtral-8x7B-Instruct-v0.1'

    #exellent quality
    llama3Instruct='meta-llama/Meta-Llama-3-8B-Instruct'

    # a lot chaotic and creative ,requires tightened constraints as system prompts
    zephyr='HuggingFaceH4/zephyr-7b-beta'




    repo_id=vars()[model]
    return repo_id

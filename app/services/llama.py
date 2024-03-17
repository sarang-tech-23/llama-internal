# from  langchain_community.llms import LlamaCpp

# class Llama27bModel():
#     def __init__(self):
#         self.model_path="llama-2-7b-chat.Q2_K.gguf"
#         self.n_ctx=4096
#         self.n_gpu_layers=32
#         self.n_batch=1024
#         self.f16_kv=True
#         self.verbose=False
#         self.llm = LlamaCpp(
#             model_path=self.model_path,
#             n_ctx=self.n_ctx,
#             n_gpu_layers=self.n_gpu_layers,
#             n_batch=self.n_batch,
#             f16_kv=self.f16_kv,
#             verbose=self.verbose,
#         )
    
#     def get_output(self, question):
#         output = self.llm(
#             question,
#             max_tokens=4096,
#             temperature=0.2,
#             # nucleus sampling (mass probability index)
#             # controls the cumulative probability of the generated tokens
#             # the higher top_p the more diversity in the output
#             top_p=0.1
#         )
#         return output


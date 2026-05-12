from vllm import LLM

llm = LLM(model="gpt-oss-20b", trust_remote_code=True)

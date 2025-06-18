# 调用GPTAPI 分析模块

import openai

def analyze(services: str) -> str:
    openai.api_key = "你的GPT-4密钥"
    prompt = f"以下是nmap扫描结果，请分析服务漏洞可能性并写出简洁报告：\n{services}"
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
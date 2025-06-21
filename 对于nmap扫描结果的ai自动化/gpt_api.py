from openai import OpenAI
from config import API_KEY  # 从 config.py 中读取你的密钥

client = OpenAI(api_key=API_KEY)

def analyze(services: str) -> str:
    try:
        prompt = f"""
我正在做网络渗透测试，以下是nmap扫描出来的服务信息，请你作为资深红队成员执行以下任务：

1. 对每个服务分析其潜在风险，并分为【高危】【中危】【低危】；
2. 指出每个服务可能存在的**攻击方式**（如：爆破、命令注入、文件上传、匿名访问等）；
3. 判断是否存在**已知公开漏洞**（如 CVE 编号或 Exploit DB 链接）；
4. 用 Markdown 输出格式组织报告，结构如下：

---

## 高危服务
- `IP:Port` - 服务名称/版本
  - **风险**：简述风险点
  - **攻击方式**：列出可能的攻击方式
  - **公开漏洞**：列出 CVE 或 Exploit 信息（如有）

## 中危服务
...

## 低危服务
...

---

服务信息如下：

{services}
"""
        completion = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {"role": "system", "content": "你是资深渗透测试专家，擅长分析nmap结果并生成专业报告"},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"调用GPT失败：{e}"

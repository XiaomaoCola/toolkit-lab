# 这个用于控制所有模块

from scanner import scan
from parser import extract_services
from gpt_api import analyze

target = "192.168.50.201"
xml_path = scan(target)  # 返回 XML 的完整路径
services = extract_services(xml_path)
report = analyze(services)

# 生成报告名与扫描结果对应
report_path = xml_path.replace("scan_", "report_").replace(".xml", ".md")
with open(report_path, "w", encoding="utf-8") as f:
    f.write(report)

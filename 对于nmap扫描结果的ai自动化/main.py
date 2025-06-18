# 这个用于控制所有模块

from scanner import scan
from parser import extract_services
from gpt_api import analyze

target = "192.168.50.0/24"
scan(target)
services = extract_services("scan_result.xml")
report = analyze(services)

with open("report.md", "w") as f:
    f.write(report)
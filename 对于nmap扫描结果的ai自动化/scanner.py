# nmap自动扫描模块
import subprocess
import os
from datetime import datetime

def scan(target_ip, output_dir="scans"):
    # 确保输出文件夹存在
    os.makedirs(output_dir, exist_ok=True)

    # 格式化时间字符串
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    # 文件名示例：scan_192.168.50.0-24_20250620-221530.xml
    safe_ip = target_ip.replace("/", "-").replace(".", "_")  # 适配文件名
    output_file = os.path.join(output_dir, f"scan_{safe_ip}_{timestamp}.xml")

    # 构造 nmap 命令
    cmd = f"nmap -sV -T4 -oX {output_file} {target_ip}"
    subprocess.run(cmd, shell=True)

    # 返回文件路径，供主程序使用
    return output_file

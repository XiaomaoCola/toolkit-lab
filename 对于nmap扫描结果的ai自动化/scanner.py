# nmap自动扫描模块

import subprocess

def scan(target_ip, output_file="scan_result.xml"):
    cmd = f"nmap -sV -T4 -oX {output_file} {target_ip}"
    subprocess.run(cmd, shell=True)
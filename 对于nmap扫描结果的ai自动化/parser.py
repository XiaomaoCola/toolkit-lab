# XML结果解析模块

# 让nmap生成XML格式的理由
# 1.“机器”更容易读懂这个格式的文件
# 2.兼容性高，最通用，可以 feed 给其他工具（如 AI 模型、数据库、可视化平台）

import xml.etree.ElementTree as ET

def extract_services(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    result = []
    for host in root.findall('host'):
        ip = host.find('address').attrib['addr']
        for port in host.find('ports').findall('port'):
            portid = port.attrib['portid']
            service = port.find('service')
            name = service.attrib.get('name', 'unknown')
            product = service.attrib.get('product', '')
            version = service.attrib.get('version', '')
            result.append(f"{ip}:{portid} - {name} {product} {version}")
    return "\n".join(result)
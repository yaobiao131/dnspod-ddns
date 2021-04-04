import json
import re
import logging
import socket
from urllib import request, error, parse

# 匹配合法 IP 地址
regex_ip = re.compile(
    r"\D*("
    + r"(?:1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\."
    + r"(?:1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\."
    + r"(?:1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\."
    + r"(?:1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)"
    + r")\D*")


# 增强鲁棒性，用多种方式获取 IP
def get_ip():
    return (get_ip_by_myip()
            or get_ip_by_httpbin()
            or get_ip_by_icanhazip()
            or get_ip_by_ipify())


# 这几个函数会在 DNS 遭受污染时失效
def get_ip_by_myip():
    url = 'https://api.my-ip.io/ip'
    try:
        resp = request.urlopen(url=url, timeout=10).read()
        return resp.decode("utf-8")
    except Exception as e:
        logging.warning("get_ip_by_ipip FAILED, error: %s", str(e))
        return None


def get_ip_by_httpbin():
    url = 'http://www.httpbin.org/ip'
    try:
        resp = request.urlopen(url=url, timeout=10).read()
        return regex_ip.match(resp.decode("utf-8")).group(1)
    except Exception as e:
        logging.warning("get_ip_by_httpbin FAILED, error: %s", str(e))
        return None


def get_ip_by_ipify():
    url = 'https://api.ipify.org?format=json'
    try:
        resp = request.urlopen(url=url, timeout=10).read()
        return json.loads(resp.decode('utf-8'))['ip']
    except Exception as e:
        logging.warning("get_ip_by_ipify FAILED, error: %s", str(e))
        return None


def get_ip_by_icanhazip():
    url = 'https://icanhazip.com'
    try:
        resp = request.urlopen(url=url, timeout=10).read()
        return resp.decode('utf-8')
    except Exception as e:
        logging.warning("get_ip_by_ipify FAILED, error: %s", str(e))
        return None


# 测试
if __name__ == '__main__':
    print(get_ip())
    print(get_ip_by_myip())
    print(get_ip_by_httpbin())

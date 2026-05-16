#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import argparse
import urllib.parse
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 兼容新老版本的模块导入
try:
    from ddgs import DDGS
except ImportError:
    from duckduckgo_search import DDGS

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def print_banner():
    # 前面加了字母 'r'，代表 Raw String，彻底消灭那个烦人的 SyntaxWarning
    banner = r"""
    ===============================================================
       ____  _____ _____ _   _ _____   _   _             _            
      / __ \/ ____|_   _| \ | |_   _| | | | |           | |           
     | |  | \ (___   | | |  \| | | |  | |_| |_   _ _ __ | |_ ___ _ __ 
     | |  | |\___ \  | | | . ` | | |  |  _  | | | | '_ \| __/ _ \ '__|
     | |__| |____) |_| |_| |\  |_| |_ | | | | |_| | | | | ||  __/ |   
      \____/|_____/|_____|_| \_|_____||_| |_|\__,_|_| |_|\__\___|_|   
                                                        
                [ PRO VERSION 2.0 - BYPASS ENGINES ]
    ===============================================================
    """
    print(banner)

def get_clean_filename(url, file_type, index):
    try:
        parsed_url = urllib.parse.urlparse(url)
        filename = os.path.basename(parsed_url.path)
        filename = urllib.parse.unquote(filename)
        if not filename.lower().endswith(f".{file_type.lower()}"):
            filename = f"document_{index}.{file_type}"
        for char in '<>:"/\\|?*':
            filename = filename.replace(char, '_')
        return filename
    except Exception:
        return f"document_{index}.{file_type}"

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="现代化 OSINT 文档猎手 v2.0")
    parser.add_argument("-d", "--domain", required=True, help="目标域名")
    parser.add_argument("-t", "--type", default="pdf", help="搜集的文件类型 (默认: pdf)")
    parser.add_argument("-l", "--limit", type=int, default=20, help="最大搜索量")
    parser.add_argument("-o", "--output", default="./downloads", help="保存目录")
    args = parser.parse_args()

    domain = args.domain.strip()
    file_type = args.type.strip().lower()
    save_dir = args.output

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    query = f"site:{domain} filetype:{file_type}"
    print(f"[*] 正在接通最新版 DDGS 引擎...")
    print(f"[*] 侦察语法: [{query}]")

    found_urls = []
    try:
        with DDGS() as ddgs:
            # 使用最新的 text 接口
            results = ddgs.text(query, max_results=args.limit)
            if results:
                for res in results:
                    if 'href' in res:
                        found_urls.append(res['href'])
    except Exception as e:
        print(f"[-] 引擎请求失败: {e}")
        sys.exit(1)

    if not found_urls:
        print(f"\n[-] 引擎未返回结果。")
        print(f"[-] 军师提示：如果多次尝试依然为0，说明云服务器IP已被所有搜索引擎拉黑。建议在本地电脑运行此脚本！")
        sys.exit(0)

    print(f"[+] 成功定位 {len(found_urls)} 个目标，开始下载...\n")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'
    }

    success_count = 0
    for index, url in enumerate(found_urls, start=1):
        print(f"[{index}/{len(found_urls)}] 正在获取: {url}")
        filename = get_clean_filename(url, file_type, index)
        save_path = os.path.join(save_dir, filename)

        try:
            response = requests.get(url, headers=headers, stream=True, timeout=15, verify=False)
            if response.status_code == 200:
                with open(save_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print(f"    ✅ [成功] -> {filename}")
                success_count += 1
            else:
                print(f"    ❌ [失败] 状态码: {response.status_code}")
        except Exception:
            print(f"    ⚠️ [错误] 网络连接异常")
        time.sleep(1.5)

    print(f"\n[*] 任务结束！成功下载: {success_count} 个文件\n")

if __name__ == "__main__":
    main()

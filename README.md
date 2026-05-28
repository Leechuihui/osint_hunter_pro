 OSINT-Hunter Pro

<p align="center">
  <strong>A Modern OSINT Document Hunter Powered by DuckDuckGo (Bypass Google CAPTCHA)</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

---

**OSINT-Hunter Pro** is a lightweight, modern Open Source Intelligence (OSINT) document harvesting tool. It is designed specifically to solve a common frustration with traditional tools (like `metagoofil`): getting constantly blocked or hitting CAPTCHAs when running from cloud server IPs (such as AWS, Vultr, or DigitalOcean). By leveraging the `ddgs` engine under the hood, it covertly and rapidly extracts and batch-downloads publicly exposed sensitive documents from any target domain.

**OSINT-Hunter Pro** 是一款轻量、现代化的开源情报（OSINT）文档搜集工具。它完美解决了传统工具（如 metagoofil）在云服务器 IP 下频繁被 Google 人机验证（CAPTCHA）拦截的痛点。通过底层对接 `ddgs` 引擎，它能隐蔽、快速地从目标域名中批量提取并下载公开暴露的敏感文档。

---

🚀 Features | 核心特性

- **Bypass Google**: Completely abandons Google Search in favor of the DuckDuckGo engine, making it perfectly suited for cloud servers and low-reputation IP environments. (完全弃用 Google Search，完美适应云服务器等低信誉 IP 环境)
- **Anti-Ban Mechanism**: Features built-in randomized User-Agent rotation and tactical request throttling (0.5s sleep delay) to drastically minimize the risk of IP blocking. (内置拟人化 User-Agent 轮询与 0.5s 战术性休眠)
- **Smart Sanitization**: Automatically handles URL-encoded gibberish to create clean, readable filenames, and automatically appends missing file extensions. (自动清洗 URL 编码导致的乱码文件名，智能补全缺失后缀)
- **Ultra-Lightweight**: Built with clean Python 3 using `requests` stream-loading (`stream=True`), ensuring smooth performance even on low-spec machines. (流式下载，轻量无依赖地狱)

---

🛠️ Installation | 安装指南

Ensure your system has Python 3.7+ installed. Run the following commands in your terminal (compatible with Ubuntu, Debian, Kali, etc.):


1. Clone the repository and navigate into the directory
```bash
  git clone https://github.com/Leechuihui/osint_hunter_pro.git

  cd osint_hunter_pro
```
2. Install the core dependencies
```bash
    pip install ddgs requests
```
📖 Usage & Options | 使用说明
    Syntax | 命令格式
    
  python osint_hunter_pro.py [-d domain] [-t type] [-l limit] [-o output_dir]
    
Options | 参数说明
  
 FlagDefaultDescription -d(Required) Target domain to harvest from target ip -tpdfFile type to search for (pdf, docx, xlsx, pptx)filetype-l20Maximum number of results to fetch最大返回结果数-o./downloadsOutput directory where files will be saved文件保存路径Quick Examples | 快速示例Basic Search (Downloads default PDF files from github.com):

```Bash

python osint_hunter_pro.py -d github.com

```
High-Volume Gathering (Grabs up to 100 DOCX documents from a government domain):
```Bash

python osint_hunter_pro.py -d usa.gov -t docx -l 100

```
Custom Export (Searches for spreadsheets and saves them to a custom folder):

```Bash
python osint_hunter_pro.py -d example.com -t xlsx -o ./xfiles

```
⚙️ How It Works & Tips | 工作原理与提示
Automated Retrieval: The script automatically constructs advanced search queries using the site:domain 
filetype:type syntax to quietly query DuckDuckGo. (自动构造高阶语法静默查询)

Structured Output: Downloaded files are normalized and neatly organized into your target folder. 
Falls back to incremental naming (document_{n}.{ext}) if the original filename cannot be parsed. (下载文件规范化命名，无法解析时自动递增编号)

Plaintext
downloads/
├── annual_report.pdf
├── spreadsheet_42.xlsx
└── document_15.pdf 

Proxy Support: If your cloud server IP is heavily throttled and returns 0 results, you can route your traffic through a proxy by setting your system environment variables before running the script: (若遭遇云 IP 封锁，可配置环境变量走代理下载)

```Bash
export HTTP_PROXY="http://your-proxy-ip:port"

export HTTPS_PROXY="http://your-proxy-ip:port"
```
⚠️ Disclaimer | 免责声明
For Educational and Authorized Testing Purposes Only. This tool is strictly intended to locate files that have already been publicly exposed to the internet. 
Users must comply with all local and international laws. The author assumes no liability and is not responsible for any misuse, data theft, malicious attacks, 
or damages caused by this program.

仅供授权的安全测试与学术研究使用。 本工具仅用于搜集互联网上已经公开暴露的文件。使用者需遵守当地法律法规，严禁用于任何非法的信息窃取或恶意网络攻击。
因使用本工具造成的任何直接或间接后果，作者不承担任何责任。

📄 License | 开源协议
This project is licensed under the MIT License.

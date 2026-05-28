OSINT-Hunter Pro
A Modern OSINT Document Hunter Powered by DuckDuckGo (Bypass Google CAPTCHA)OSINT-Hunter Pro 是一款轻量、现代化的开源情报（OSINT）文档搜集工具。它完美解决了传统工具（如 metagoofil）在云服务器 IP（如 AWS, Vultr）下频繁被 Google 人机验证（CAPTCHA）拦截的痛点。
通过底层对接 ddgs 引擎，它能隐蔽、快速地从目标域名中批量提取并下载公开暴露的敏感文档（PDF, DOCX, XLSX, PPTX 等）。

🚀 核心特性 (Features)Bypass Google：完全弃用 Google Search，改用 DuckDuckGo 引擎，完美适应云服务器等低信誉 IP 环境。Anti-Ban 机制：内置拟人化 User-Agent 轮询与战术性请求休眠（0.5s 延迟），极大降低被封锁概率。

智能清洗：自动处理 URL 编码导致的乱码文件名，并智能补全缺失的文件后缀。极度轻量：无依赖地狱，使用 requests 流式下载（stream=True），低配机器也能流畅运行。

🛠️ 安装指南 (Installation)确保系统已安装 Python 3.7+。
在 Ubuntu / Debian 

环境下运行以下命令完成安装：Bash# 

1. 克隆仓库并进入目录
git clone https://github.com/Leechuihui/osint_hunter_pro.git
cd osint_hunter_pro

#2. 安装核心依赖
pip install ddgs requests

📖 使用指南 (Usage & Options)命令格式Bashpython osint_hunter_pro.py [-d domain] [-t type] [-l limit] [-o output_dir]

参数说明 (Options)FlagDefaultDescription-d(Required)目标域名 (Target domain)-tpdf搜寻的文件类型 (File type: pdf, docx, xlsx, pptx 等)-l20最大返回结果数 (Max results to return)-o./downloads文件保存路径 (Output directory)快速示例 (Quick Examples)基础搜索

（默认下载 github.com 的 PDF 文件）：Bashpython osint_hunter_pro.py -d github.com
高强度搜集（从政府网站下载 100 个 DOCX 文档）：Bashpython osint_hunter_pro.py -d usa.gov -t docx -l 100
自定义导出（下载表格并保存到指定文件夹）：Bashpython osint_hunter_pro.py -d example.com -t xlsx -o ./xfiles
⚙️ 工作原理与提示 (How It Works & Tips)
自动化检索：脚本自动构造 site:domain filetype:type 
语法静默查询 DuckDuckGo。
结构化输出：下载的文件规范化命名并整齐存放在目标目录：Plaintextdownloads/

├── annual_report.pdf
├── spreadsheet_42.xlsx
└── document_15.pdf (无法解析原文件名时自动递增命名)
网络提示：如果遭遇云 IP 封锁导致返回结果为 0，工具会弹出提示。
你可以通过设置系统环境变量 HTTP_PROXY / HTTPS_PROXY 来让工具走代理下载。
⚠️ 免责声明 (Disclaimer)本工具仅供授权的安全测试与学术研究使用 (For Educational and Authorized Testing Purposes Only)。
本工具仅用于搜集互联网上已经公开暴露的文件。使用者需遵守当地法律法规，严禁用于任何非法的信息窃取或恶意网络攻击。
因使用本工具造成的任何直接或间接后果，作者不承担任何责任。
📄 开源协议 (License)MIT


Here is the fully polished, pure English version of your README document, optimized for GitHub:OSINT-Hunter ProA Modern OSINT Document Hunter Powered by DuckDuckGo (Bypass Google CAPTCHA)OSINT-Hunter Pro is a lightweight, modern Open Source Intelligence (OSINT) document harvesting tool. It is designed specifically to solve a common frustration with traditional tools (like metagoofil): getting constantly blocked or hitting CAPTCHAs when running from cloud server IPs (such as AWS, Vultr, or DigitalOcean).By leveraging the ddgs engine under the hood, it covertly and rapidly extracts and batch-downloads publicly exposed sensitive documents (PDF, DOCX, XLSX, PPTX, etc.) from any target domain.🚀 FeaturesBypass Google: Completely abandons Google Search in favor of the DuckDuckGo engine, making it perfectly suited for cloud servers and low-reputation IP environments.Anti-Ban Mechanism: Features built-in randomized User-Agent rotation and tactical request throttling (0.5s sleep delay) to drastically minimize the risk of IP blocking.Smart Sanitization: Automatically handles URL-encoded gibberish to create clean, readable filenames, and automatically appends missing file extensions.Ultra-Lightweight: No dependency hell. Built with clean Python 3 using requests stream-loading (stream=True), ensuring smooth performance even on low-spec, single-core machines.🛠️ InstallationEnsure your system has Python 3.7+ installed. Run the following commands in your terminal (compatible with Ubuntu, Debian, Kali, and other Linux distributions):Bash# 1. Clone the repository and navigate into the directory
git clone https://github.com/Leechuihui/osint_hunter_pro.git
cd osint_hunter_pro

# 2. Install the core dependencies
pip install ddgs requests
📖 Usage & OptionsSyntaxBashpython osint_hunter_pro.py [-d domain] [-t type] [-l limit] [-o output_dir]
OptionsFlagDefaultDescription-d(Required)Target domain to harvest from-tpdfFile type to search for (e.g., pdf, docx, xlsx, pptx)-l20Maximum number of results to fetch-o./downloadsOutput directory where files will be savedQuick ExamplesBasic Search (Downloads default PDF files from github.com):Bashpython osint_hunter_pro.py -d github.com
High-Volume Gathering (Grabs up to 100 DOCX documents from a government domain):Bashpython osint_hunter_pro.py -d usa.gov -t docx -l 100
Custom Export (Searches for spreadsheets and saves them to a custom folder):Bashpython osint_hunter_pro.py -d example.com -t xlsx -o ./xfiles
⚙️ How It Works & TipsAutomated Retrieval: The script automatically constructs advanced search queries using the site:domain filetype:type syntax to quietly query DuckDuckGo.Structured Output: Downloaded files are normalized and neatly organized into your target folder:Plaintextdownloads/
├── annual_report.pdf
├── spreadsheet_42.xlsx
└── document_15.pdf (Falls back to incremental naming if the original filename cannot be parsed)
Proxy Support: If your cloud server IP is heavily throttled and returns 0 results, the tool will alert you. You can route your traffic through a proxy by setting your system environment variables before running the script:Bashexport HTTP_PROXY="http://your-proxy-ip:port"
export HTTPS_PROXY="http://your-proxy-ip:port"
⚠️ DisclaimerFor Educational and Authorized Testing Purposes Only. This tool is strictly intended to locate files that have already been publicly exposed to the internet. Users must comply with all local and international laws. The author assumes no liability and is not responsible for any misuse, data theft, malicious attacks, or damages caused by this program.📄 LicenseThis project is licensed under the MIT License.

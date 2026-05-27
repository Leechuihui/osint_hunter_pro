```bash（ubuntu)
 1. 克隆本仓库
git clone [https://github.com/你的用户名/OSINT-Hunter-Pro.git](https://github.com/你的用户名/OSINT-Hunter-Pro.git)
cd OSINT-Hunter-Pro

 2. 安装核心依赖包
pip install ddgs requests


OSINT-Hunter Pro

A lightweight document hunter for OSINT. Queries DuckDuckGo to find and download public documents (PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX, etc.) from any domain — without getting stuck in Google CAPTCHAs.

#Why This Exists

Traditional OSINT tools like metagoofil work well, but they hit Google constantly. Cloud server IPs (AWS, Vultr, etc.) get flagged for CAPTCHAs and the whole pipeline grinds to a halt. OSINT-Hunter Pro swaps Google for DuckDuckGo, so it flies on cloud IPs.

Plus, it runs smoothly on low-end machines. No heavy dependencies.
 
 
 
  OSINT-Hunter Pro

A Modern OSINT Document Hunter Powered by DuckDuckGo (Bypass Google Captcha)**

OSINT-Hunter Pro 是一款现代化的开源情报（OSINT）文档搜集工具。它旨在解决传统爬虫工具（如 metagoofil）在云服务器 IP 下频繁被 Google 人机验证（CAPTCHA）拦截的痛点。

本项目底层基于 `ddgs` 引擎，通过高度拟人化的请求和智能容错机制，隐蔽、快速地从目标域名中提取并下载特定后缀的公开文档（如 PDF, DOCX, XLSX 等）。

---

  核心特性 (Features)

- Bypass Google：完全弃用 Google Search API，依托 DuckDuckGo 引擎，完美适应 AWS/云服务器等低信誉 IP 环境。
- Anti-Ban 机制：内置拟人化 User-Agent 轮询与战术性请求休眠（Sleep机制），极大降低被目标服务器封锁的概率。
-  智能清洗：自动处理由于 URL 编码导致的乱码文件名，并自动修正缺少后缀的文件。
- 无依赖地狱：极其轻量，仅依赖 `requests` 和 `ddgs`，告别复杂的环境配置。
- 
仅供授权的安全测试与学术研究使用 (For Educational and Authorized Testing Purposes Only). 本工具仅用于搜集互联网上已经公开暴露的文件。
使用者需遵守当地法律法规，严禁用于任何非法的信息窃取或恶意网络攻击。因使用本工具造成的任何直接或间接后果，作者不承担任何责任。
---

 安装指南 (Installation)

确保你的系统已安装 Python 3.7+。建议在虚拟环境中运行：



 Installation

```
git clone https://github.com/Leechuihui/osint_hunter_pro.git
cd osint_hunter_pro
pip install ddgs requests
```

Done. That's all you need.

 Usage

```
python osint_hunter_pro.py -d target.com
```

This runs a `site:target.com filetype:pdf` query, downloads matching files to `./downloads/`, and prints progress as it goes.

 Options

```
python osint_hunter_pro.py [-d domain] [-t type] [-l limit] [-o output_dir]
```

| Flag   | Default        | Description                       |
|--------|----------------|-----------------------------------|
| -d     | _(required)_   | Target domain                     |
| -t     | `pdf`          | File type to search               |
| -l     | `20`           | Max results to return             |
| -o     | `./downloads`  | Where to save files               |

### Quick Examples

Search for PDFs on a domain:
```
python osint_hunter_pro.py -d github.com
```

Grab 100 DOCX files from a government domain:
```
python osint_hunter_pro.py -d usa.gov -t docx -l 100
```

Save results to a custom folder:
```
python osint_hunter_pro.py -d example.com -t xlsx -o ./xfiles
```

The tool works with any file extension that DuckDuckGo can find — `pdf`, `doc`, `docx`, `xls`, `xlsx`, `ppt`, `pptx`. Just run a separate command for each type.

 How It Works

The script does four things:

1. Queries DuckDuckGo in text mode using a `site:domain filetype:type` search.
2. Collects up to `--limit` matching URLs. If no results, it suggests you might be on a throttled cloud IP.
3. Downloads every file, cleaning filenames along the way (URL-decoding, fixing missing extensions).
4. Waits half a second between requests so you don't get flagged.

 Output

Files land in `./downloads` by default, named to be readable:

```
downloads/
  annual_report.pdf
  presentation.doc
  slide_deck.pptx
  spreadsheet_42.xlsx
  document_15.pdf
```

If the URL doesn't contain a recognizable extension, the tool assigns names like `document_{n}.{ext}`.

 Tips

- Cloud IP and getting few results? Try from a local machine first.
- Set `HTTP_PROXY` / `HTTPS_PROXY` to route downloads through a proxy.
- If DuckDuckGo returns zero results, the tool tells you and suggests running from a local machine.
- The script uses `requests` with `stream=True` so it's memory-efficient even with larger files.

 Disclaimer

This is an educational / authorized testing tool. It only collects publicly exposed internet files. Use it responsibly. The author is not responsible for any downstream consequences.

 License

MIT




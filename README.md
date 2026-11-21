**English** | [简体中文](README.zh-CN.md)

# OSINT-Hunter Pro

<p align="center">
  <strong>A Modern OSINT Document Hunter Powered by DuckDuckGo (Bypass Google CAPTCHA)</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

---

**OSINT-Hunter Pro** is a lightweight, modern Open Source Intelligence (OSINT) document harvesting tool. It is designed specifically to solve a common frustration with traditional tools (like `metagoofil`): getting constantly blocked or hitting CAPTCHAs when running from cloud server IPs (such as AWS, Vultr, or DigitalOcean). By leveraging the `ddgs` engine under the hood, it covertly and rapidly extracts and batch-downloads publicly exposed sensitive documents from any target domain.

---

## 🚀 Features

- **Bypass Google**: Completely abandons Google Search in favor of the DuckDuckGo engine, making it perfectly suited for cloud servers and low-reputation IP environments.
- **Anti-Ban Mechanism**: Features built-in randomized User-Agent rotation and tactical request throttling (0.5s sleep delay) to drastically minimize the risk of IP blocking.
- **Smart Sanitization**: Automatically handles URL-encoded gibberish to create clean, readable filenames, and automatically appends missing file extensions.
- **Ultra-Lightweight**: Built with clean Python 3 using `requests` stream-loading (`stream=True`), ensuring smooth performance even on low-spec machines.

---

## 🛠️ Installation

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

---

## 📖 Usage & Options

### Syntax

```
python osint_hunter_pro.py [-d domain] [-t type] [-l limit] [-o output_dir]
```

### Options

| Flag | Default | Description |
|------|---------|-------------|
| `-d` | (Required) | Target domain to harvest from |
| `-t` | pdf | File type to search for (pdf, docx, xlsx, pptx) |
| `-l` | 20 | Maximum number of results to fetch |
| `-o` | ./downloads | Output directory where files will be saved |

### Quick Examples

Basic Search (Downloads default PDF files from github.com):

```bash
python osint_hunter_pro.py -d github.com
```

High-Volume Gathering (Grabs up to 100 DOCX documents from a government domain):

```bash
python osint_hunter_pro.py -d usa.gov -t docx -l 100
```

Custom Export (Searches for spreadsheets and saves them to a custom folder):

```bash
python osint_hunter_pro.py -d example.com -t xlsx -o ./xfiles
```

---

## ⚙️ How It Works & Tips

**Automated Retrieval**: The script automatically constructs advanced search queries using the `site:domain filetype:type` syntax to quietly query DuckDuckGo.

**Structured Output**: Downloaded files are normalized and neatly organized into your target folder. Falls back to incremental naming (`document_{n}.{ext}`) if the original filename cannot be parsed.

```
downloads/
├── annual_report.pdf
├── spreadsheet_42.xlsx
└── document_15.pdf
```

**Proxy Support**: If your cloud server IP is heavily throttled and returns 0 results, you can route your traffic through a proxy by setting your system environment variables before running the script:

```bash
export HTTP_PROXY="http://your-proxy-ip:port"
export HTTPS_PROXY="http://your-proxy-ip:port"
```

---

## ⚠️ Disclaimer

For Educational and Authorized Testing Purposes Only. This tool is strictly intended to locate files that have already been publicly exposed to the internet. Users must comply with all local and international laws. The author assumes no liability and is not responsible for any misuse, data theft, malicious attacks, or damages caused by this program.

---

## 📄 License

This project is licensed under the MIT License.

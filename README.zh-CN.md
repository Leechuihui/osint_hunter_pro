[English](README.md) | **简体中文**

# OSINT-Hunter Pro

<p align="center">
  <strong>基于 DuckDuckGo 的现代化 OSINT 文档搜集工具（绕过 Google 人机验证）</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

---

**OSINT-Hunter Pro** 是一款轻量、现代化的开源情报（OSINT）文档搜集工具。它完美解决了传统工具（如 metagoofil）在云服务器 IP 下频繁被 Google 人机验证（CAPTCHA）拦截的痛点。通过底层对接 `ddgs` 引擎，它能隐蔽、快速地从目标域名中批量提取并下载公开暴露的敏感文档。

---

## 🚀 核心特性

- **绕过 Google**：完全弃用 Google Search，改用 DuckDuckGo 引擎，完美适应云服务器等低信誉 IP 环境。
- **防封禁机制**：内置拟人化 User-Agent 轮询与 0.5s 战术性休眠，最大限度降低 IP 被封风险。
- **智能文件名清洗**：自动处理 URL 编码导致的乱码文件名，生成干净可读的文件名，并智能补全缺失后缀。
- **极致轻量**：纯 Python 3 实现，使用 `requests` 流式下载（`stream=True`），低配机器也能流畅运行。

---

## 🛠️ 安装指南

确保系统已安装 Python 3.7+。在终端中运行以下命令（兼容 Ubuntu、Debian、Kali 等）：

1. 克隆仓库并进入目录

```bash
git clone https://github.com/Leechuihui/osint_hunter_pro.git
cd osint_hunter_pro
```

2. 安装核心依赖

```bash
pip install ddgs requests
```

---

## 📖 使用说明

### 命令格式

```
python osint_hunter_pro.py [-d domain] [-t type] [-l limit] [-o output_dir]
```

### 参数说明

| 参数 | 默认 | 说明 |
|------|---------|-------------|
| `-d` | （必填） | 要搜集的目标域名 |
| `-t` | pdf | 要搜索的文件类型（pdf、docx、xlsx、pptx） |
| `-l` | 20 | 最大返回结果数 |
| `-o` | ./downloads | 文件保存路径 |

### 快速示例

基础搜索（从 github.com 下载默认的 PDF 文件）：

```bash
python osint_hunter_pro.py -d github.com
```

大批量搜集（从政府域名抓取最多 100 个 DOCX 文档）：

```bash
python osint_hunter_pro.py -d usa.gov -t docx -l 100
```

自定义导出（搜索电子表格并保存到自定义目录）：

```bash
python osint_hunter_pro.py -d example.com -t xlsx -o ./xfiles
```

---

## ⚙️ 工作原理与提示

**自动检索**：脚本自动使用 `site:domain filetype:type` 高阶语法静默查询 DuckDuckGo。

**结构化输出**：下载的文件会被规范化命名并整齐地整理到目标文件夹。当原始文件名无法解析时，自动回退为递增编号（`document_{n}.{ext}`）。

```
downloads/
├── annual_report.pdf
├── spreadsheet_42.xlsx
└── document_15.pdf
```

**代理支持**：如果云服务器 IP 被严重限流、返回 0 结果，可在运行脚本前设置系统环境变量，让流量走代理：

```bash
export HTTP_PROXY="http://your-proxy-ip:port"
export HTTPS_PROXY="http://your-proxy-ip:port"
```

---

## ⚠️ 免责声明

仅供授权的安全测试与学术研究使用。本工具仅用于搜集互联网上已经公开暴露的文件。使用者需遵守当地法律法规，严禁用于任何非法的信息窃取或恶意网络攻击。因使用本工具造成的任何直接或间接后果，作者不承担任何责任。

---

## 📄 开源协议

本项目基于 MIT License 开源。

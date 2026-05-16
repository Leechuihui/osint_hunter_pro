 🎯 OSINT-Hunter Pro

A Modern OSINT Document Hunter Powered by DuckDuckGo (Bypass Google Captcha)**

OSINT-Hunter Pro 是一款现代化的开源情报（OSINT）文档搜集工具。它旨在解决传统爬虫工具（如 metagoofil）在云服务器 IP 下频繁被 Google 人机验证（CAPTCHA）拦截的痛点。

本项目底层基于 `ddgs` 引擎，通过高度拟人化的请求和智能容错机制，隐蔽、快速地从目标域名中提取并下载特定后缀的公开文档（如 PDF, DOCX, XLSX 等）。

---

 ✨ 核心特性 (Features)

- 🛡️ **Bypass Google**：完全弃用 Google Search API，依托 DuckDuckGo 引擎，完美适应 AWS/云服务器等低信誉 IP 环境。
- 🤖 **Anti-Ban 机制**：内置拟人化 User-Agent 轮询与战术性请求休眠（Sleep机制），极大降低被目标服务器封锁的概率。
- 🧹 **智能清洗**：自动处理由于 URL 编码导致的乱码文件名，并自动修正缺少后缀的文件。
- ⚡ **无依赖地狱**：极其轻量，仅依赖 `requests` 和 `ddgs`，告别复杂的环境配置。

---

 🛠️ 安装指南 (Installation)

确保你的系统已安装 Python 3.7+。建议在虚拟环境中运行：

```bash
# 1. 克隆本仓库
git clone [https://github.com/你的用户名/OSINT-Hunter-Pro.git](https://github.com/你的用户名/OSINT-Hunter-Pro.git)
cd OSINT-Hunter-Pro

# 2. 安装核心依赖包
pip install ddgs requests

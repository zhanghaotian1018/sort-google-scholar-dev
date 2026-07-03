# sort-google-scholar

A Python tool to rank Google Scholar publications by citations.

---

## English

### Overview

This tool searches Google Scholar for academic publications based on keywords, extracts bibliographic metadata (author, title, citations, year, venue, publisher, abstract, PDF link), sorts results by citation count (or citations per year), and exports the data to CSV/Excel.

### Features

- Search Google Scholar by keyword with configurable result count
- Extract rich metadata: author, title, citations, year, venue, publisher, abstract, PDF link
- Sort by total citations or citations per year
- Filter by publication year range and language
- Export results to CSV and/or Excel (with styled formatting)
- Visualize citation distribution with a rank-vs-citations plot
- Selenium fallback for anti-bot protection (CAPTCHA)
- Debug mode using Web Archive snapshots

### Installation

```bash
pip install .
```

Or from source:

```bash
pip install -r requirements.txt
```

**Dependencies:** requests, beautifulsoup4, pandas, matplotlib, selenium, openpyxl (optional, for Excel export)

### Usage

Basic search:

```bash
python -m sortgs "machine learning"
```

Advanced usage:

```bash
python -m sortgs "cultural heritage CT imaging" \
    --nresults 200 \
    --sortby "Citations" \
    --startyear 2018 \
    --endyear 2024 \
    --langfilter en \
    --plotresults \
    --csvpath ./output
```

### Command-line Arguments

| Argument | Description | Default |
|---|---|---|
| `kw` | Keyword(s) to search | `"machine learning"` |
| `--sortby` | Column to sort by (`Citations` or `cit/year`) | `Citations` |
| `--nresults` | Number of results to fetch | `100` |
| `--startyear` | Start year for filtering | `None` |
| `--endyear` | End year for filtering | Current year |
| `--langfilter` | Language filter (e.g. `en`, `zh-CN`, `fr`) | `All` |
| `--csvpath` | Output directory for CSV/Excel | Current directory |
| `--notsavecsv` | Skip saving results to file | `False` |
| `--plotresults` | Show citation rank plot | `False` |
| `--debug` | Use Web Archive for testing | `False` |
| `--xlsx-only` | Export only Excel, skip CSV | `False` |

### Output Columns

| Column | Description |
|---|---|
| Rank | Sorted position |
| Author | Paper author(s) |
| Title | Paper title |
| Citations | Total citation count |
| Year | Publication year |
| Publisher | Publishing house / platform |
| Venue | Journal / conference name |
| Content | Abstract / snippet |
| Source | Original Google Scholar URL |
| PDF | Direct PDF download link |
| cit/year | Citations per year (normalized) |

---

## 中文

### 概述

本工具根据关键词在 Google Scholar 上搜索学术论文，提取元数据（作者、标题、引用次数、年份、会议/期刊、出版社、摘要、PDF链接），按引用量（或年均引用量）排序，并导出为 CSV/Excel 文件。

### 功能特性

- 按关键词搜索 Google Scholar，可自定义结果数量
- 提取丰富元数据：作者、标题、引用次数、年份、会议/期刊、出版社、摘要、PDF链接
- 支持按总引用数或年均引用数排序
- 支持按出版年份范围和语言过滤
- 导出结果为 CSV 和/或 Excel（带格式美化）
- 可视化引用分布（排名 vs 引用数折线图）
- Selenium 反爬回退机制（遇 CAPTCHA 暂停等待人工处理）
- Debug 模式：使用 Web Archive 快照进行测试

### 安装

```bash
pip install .
```

或从源码安装：

```bash
pip install -r requirements.txt
```

**依赖：** requests, beautifulsoup4, pandas, matplotlib, selenium, openpyxl（可选，用于 Excel 导出）

### 使用方法

基础搜索：

```bash
python -m sortgs "machine learning"
```

高级用法：

```bash
python -m sortgs "cultural heritage CT imaging" \
    --nresults 200 \
    --sortby "Citations" \
    --startyear 2018 \
    --endyear 2024 \
    --langfilter en \
    --plotresults \
    --csvpath ./output
```

### 命令行参数

| 参数 | 描述 | 默认值 |
|---|---|---|
| `kw` | 搜索关键词 | `"machine learning"` |
| `--sortby` | 排序列（`Citations` 或 `cit/year`） | `Citations` |
| `--nresults` | 获取结果数量 | `100` |
| `--startyear` | 起始年份 | `None` |
| `--endyear` | 结束年份 | 当前年份 |
| `--langfilter` | 语言过滤（如 `en`、`zh-CN`、`fr`） | `All` |
| `--csvpath` | 输出目录 | 当前目录 |
| `--notsavecsv` | 不保存结果到文件 | `False` |
| `--plotresults` | 显示引用排名图 | `False` |
| `--debug` | 使用 Web Archive 测试 | `False` |
| `--xlsx-only` | 仅导出 Excel，跳过 CSV | `False` |

### 输出字段说明

| 字段 | 描述 |
|---|---|
| Rank | 排序位置 |
| Author | 论文作者 |
| Title | 论文标题 |
| Citations | 总引用次数 |
| Year | 发表年份 |
| Publisher | 出版社/平台 |
| Venue | 期刊/会议名称 |
| Content | 摘要/片段 |
| Source | Google Scholar 原始链接 |
| PDF | PDF 下载直链 |
| cit/year | 年均引用数（归一化） |

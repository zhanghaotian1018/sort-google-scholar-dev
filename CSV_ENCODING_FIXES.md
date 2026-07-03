# CSV 文件格式和乱码问题修复说明

## 问题诊断
你的脚本在保存CSV文件时出现格式混乱和乱码的问题，主要原因有以下几个：

1. **编码不一致**：使用了ISO-8859-1解码但用utf-8解析，导致字符转换错误
2. **特殊字符处理不完整**：HTML中包含的特殊空格字符（如`\xa0`非换行空格）没有彻底清理
3. **CSV编码选项不优化**：使用纯utf-8而没有BOM标记，在Windows/Excel中容易显示问题
4. **文本未规范化**：提取的文本中包含换行符、多余空格等会导致CSV格式混乱

## 实施的改进

### 1. 修复网页编码处理（第323-335行）
```python
# 之前
page = session.get(url)
c = page.content
if any(kw in c.decode("ISO-8859-1") for kw in ROBOT_KW):
    # ...
soup = BeautifulSoup(c, "html.parser", from_encoding="utf-8")

# 改进后
page = session.get(url)
page.encoding = 'utf-8'  # 从一开始就设置正确编码
c = page.content
if any(kw in c.decode("utf-8", errors="ignore") for kw in ROBOT_KW):
    # ...
soup = BeautifulSoup(c, "html.parser")  # 使用更简洁的API
```

### 2. 添加文本清理函数（第207-217行）
```python
def clean_text(text: str) -> str:
    """清理和规范化提取的文本"""
    if not text:
        return ""
    # 替换特殊空格和换行符
    text = text.replace("\xa0", " ").replace("\u200b", "").replace("\r", " ").replace("\n", " ")
    # 移除多余空格
    text = " ".join(text.split())
    return text.strip()
```

这个函数处理以下问题：
- `\xa0`：非换行空格（HTML中常见）
- `\u200b`：零宽度空格
- `\r`和`\n`：换行符，会破坏CSV格式
- 多余空格被合并为单个空格

### 3. 在所有数据提取处应用清理函数
- **标题**（第347行）：`clean_text(div.find("h3").find("a").text)`
- **作者**（第354行）：`clean_text(get_author(...))`
- **出版社**（第362行）：`clean_text(publisher_text)`
- **会议地点**（第369行）：`clean_text(venue_text)`
- **摘要内容**（第377行）：`clean_text(content_div.text)`
- **PDF链接**（第382行）：`clean_text(get_pdf_link(div) or ...)`

### 4. 优化CSV保存方式（第484-487行）
```python
# 之前
data_ranked.to_csv(csv_path, encoding="utf-8")

# 改进后
data_ranked.to_csv(csv_path, encoding="utf-8-sig", index=True, quoting=1)
```

改进说明：
- **utf-8-sig**：添加BOM（字节顺序标记），在Windows和Excel中有更好的兼容性
- **quoting=1**：即`csv.QUOTE_ALL`，确保所有字段都被引号包围，防止特殊字符导致的解析错误

## 效果
这些改进将：
✓ 消除编码导致的乱码问题
✓ 确保CSV文件在Windows和Excel中正确显示
✓ 防止文本中的特殊字符破坏CSV格式
✓ 清理HTML中的非可见字符
✓ 规范化输出格式

## 测试建议
修改后，你可以运行：
```bash
python -m sortgs.sortgs "machine learning" --nresults 10
```

然后检查生成的CSV文件是否：
1. 能正常在Excel中打开
2. 没有乱码
3. 格式整齐，列对齐
4. 没有多余的换行或空格

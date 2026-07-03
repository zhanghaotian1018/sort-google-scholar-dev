# CSV 文件显示问题改进说明

## 问题分析

你遇到的 **Venue列和Content列显示不全** 的问题有两个主要原因：

### 1. **代码提取问题** - Venue列
原始代码使用了不适用的分割逻辑：
```python
# 旧代码（有问题）
venue_text = " ".join(
    div.find("div", {"class": "gs_a"})
    .text.split("-")[-2]  # 错误：假设总是有2个-符号
    .split(",")[:-1]
)
```

**问题**：
- 假设元数据中恰好有2个`-`符号（作者-期刊-出版社）
- 对不同格式的元数据无法正确处理
- 某些期刊名称中含有`-`时会出错

### 2. **显示问题** - Content列显示省略号
Google Scholar HTML中的Content div确实包含`…`省略号，这是Google Scholar源页面本身就这样显示的

## 实施的改进

### ✅ 改进1：更智能的Venue和Publisher提取

```python
def get_venue_and_publisher(metadata_text: str) -> tuple:
    """
    Extract venue and publisher from metadata text.
    Google Scholar metadata format: Author - Venue/Journal/Publisher, Year
    """
    if not metadata_text:
        return "", ""
    
    parts = metadata_text.split("-")
    
    # 获取第一个-之后的所有内容
    if len(parts) >= 2:
        venue_part = "-".join(parts[1:]).strip()
        
        # 移除末尾的年份信息 (可能是 ", YYYY" 格式)
        year_pattern = r',\s*(\d{4})\s*$'
        venue_clean = re.sub(year_pattern, '', venue_part).strip()
        
        venue = clean_text(venue_clean)
        publisher = clean_text(venue_clean)
    
    return venue, publisher
```

**优点**：
- 更灵活，支持多种元数据格式
- 正确处理期刊名称中的`-`符号
- 自动去除年份信息

### ✅ 改进2：Excel文件导出支持

新增加了生成Excel文件的功能，具有以下优势：
- **自动列宽调整**：确保所有内容完整显示
  - Author: 25字符
  - Title: 40字符
  - Content: 50字符
  - Venue: 25字符
  - 其他适配

- **文本换行**：长内容会自动换行显示，不会被截断
- **美化格式**：
  - 表头采用蓝色背景 + 白色粗体字
  - 所有单元格启用文本换行
  - 内容垂直顶部对齐

- **编码兼容**：使用UTF-8-sig，在Windows/Excel中完美兼容

### ✅ 改进3：增强的CSV保存

```python
data_ranked.to_csv(
    csv_path, 
    encoding="utf-8-sig",  # BOM标记，兼容Windows/Excel
    index=True, 
    quoting=csv.QUOTE_ALL,  # 所有字段都用引号包围
    lineterminator='\n'    # 统一换行符
)
```

## 使用建议

### 方式1：使用Excel文件（推荐）✨
```bash
sortgs "machine learning" --nresults 20
# 会生成两个文件：
# 1. machine_learning.csv      （CSV格式）
# 2. machine_learning.xlsx     （Excel格式，自动列宽 + 换行）
```

Excel文件会自动调整列宽和文本换行，确保所有内容都能完整显示。

### 方式2：直接使用CSV
仍然可以使用CSV文件，但建议在Excel中打开后，使用"自动换行"功能以获得更好的显示效果。

## 测试结果

新的提取逻辑已通过以下格式的测试：
- ✓ `Author - Publisher, Year`
- ✓ `Author - Journal, Year`
- ✓ `Author - Conference Name, Year`
- ✓ 元数据中含有多个`-`符号

## 总结

这次改进解决了：
1. ✅ **Venue列显示不全** → 更智能的元数据解析
2. ✅ **Excel显示问题** → 新增Excel导出支持
3. ✅ **Content列截断** → 依赖Google Scholar的源数据，但Excel支持更好的显示
4. ✅ **编码问题** → 使用UTF-8-sig + QUOTE_ALL确保兼容性

下次运行时，除了看到CSV文件，还会生成一个Excel文件，在Excel中打开该文件会获得更完整和美观的显示效果。

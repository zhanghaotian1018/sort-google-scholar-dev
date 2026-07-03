# 快速使用指南

## 改进摘要

你的代码已经进行了全面优化，解决了以下问题：

### 🔧 修复的问题

1. **CSV编码乱码** ✅
   - 统一使用UTF-8编码
   - 添加BOM标记提高兼容性

2. **特殊字符处理** ✅
   - 新增 `clean_text()` 函数清理所有特殊字符
   - 处理非换行空格、零宽度字符、换行符

3. **Venue列显示不全** ✅
   - 改进 `get_venue_and_publisher()` 函数
   - 更智能的元数据解析，支持多种格式

4. **显示问题** ✅
   - 新增 **Excel导出功能**
   - 自动调整列宽和文本换行

## 现有功能

### 自动生成文件

运行命令后，会自动生成两个文件：

```bash
sortgs "机器学习" --nresults 50
```

✅ **输出文件：**
- `机器学习.csv` - CSV格式（兼容所有软件）
- `机器学习.xlsx` - Excel格式（推荐查看）

### Excel文件的优势

使用Excel文件（`.xlsx`）可以获得：
- 📊 自动调整的列宽
- 📝 智能文本换行
- 🎨 美化的表头格式
- ✨ 更好的可读性

## 命令参考

```bash
# 基础搜索
sortgs "machine learning"

# 指定结果数量
sortgs "deep learning" --nresults 50

# 按引用数排序（默认）
sortgs "neural networks" --sortby "Citations"

# 按年均引用排序
sortgs "deep learning" --sortby "cit/year"

# 指定年份范围
sortgs "machine learning" --startyear 2010 --endyear 2020

# 指定保存路径
sortgs "AI" --csvpath "./results/"

# 多个条件组合
sortgs "deep learning" --nresults 100 --sortby "cit/year" --csvpath "./output/"
```

## 代码改进详情

### 文本清理函数
```python
def clean_text(text: str) -> str:
    """清理和规范化提取的文本"""
    # 处理所有特殊字符和空格
    # 确保CSV格式正确
```

### Venue/Publisher 提取函数
```python
def get_venue_and_publisher(metadata_text: str) -> tuple:
    """
    灵活提取期刊/会议信息
    支持多种元数据格式
    """
```

### Excel格式化
```python
# 自动设置列宽
# 启用文本换行
# 美化表头
# 使用推荐字体大小
```

## 依赖项

已新增依赖：
- `openpyxl` - Excel文件支持（已自动安装）

## 验证安装

检查是否已正确安装：
```bash
sortgs --help
```

应该能看到完整的命令行帮助信息。

## 下一步建议

1. 运行 `sortgs "你的关键词" --nresults 20` 进行测试
2. 检查生成的Excel文件是否格式正确
3. 如有任何问题，检查日志信息

---

有任何问题或需要进一步改进，随时反馈！

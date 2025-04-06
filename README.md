# 📚 Books to Scrape 自动化测试项目

本项目使用 **Selenium + Pytest** 完成对开源图书电商模拟站点 [Books to Scrape](http://books.toscrape.com/) 的功能测试，包括首页加载、分类筛选、图书点击和分页翻转功能。

---

## 🧠 技术栏

- Python 3.12
- Selenium WebDriver
- Pytest
- Pytest-HTML (HTML 测试报告)

---

## 🗂️ 项目结构

```
book_test/
├── pages/              # 页面对象封装
│   └── book_page.py
├── tests/              # 测试脚本
│   └── test_books.py
├── conftest.py         # Pytest fixture 配置
├── requirements.txt    # 依赖包
├── pytest.ini          # 配置文件
└── report.html         # 自动生成的测试报告
```

---

## ✅ 已实现功能

| 测试编号 | 功能测试项 | 说明 |
|--------------|------------------|--------------------------|
| TC01         | 首页加载           | 校验标题包含 "Books to Scrape" |
| TC02         | 点击第一本图书     | 是否成功进入图书详情页         |
| TC03         | 分类筛选             | 点击 "Science" 分类后显示关联内容     |
| TC04         | 图书价格格式校验 | 所有价格应以 "￡" 开头        |
| TC05         | 分页功能             | 点击 "next" 切换页面，内容变化     |

---

## 🚀 运行方法

### 步骤 1：安装依赖
```
pip install -r requirements.txt
```

### 步骤 2：启动测试 + 生成报告
```
pytest tests/ --html=report.html
```

> 运行后在项目根目录下生成 `report.html`，可以用浏览器打开查看统计和进程。

---

## 💬 作者

该项目由 **许泽辰 (Zechen Xu)** 经手编写，作为自动化测试技术培训项目，应用于简历、面试和实战经验积累。

若您喜欢，欢迎优化或扩展更多测试场景 🚀


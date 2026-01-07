# 📚 Automated Vocabulary Builder (基于Python的外刊生词本生成器)

### Project Overview (项目简介)
This project is a Python-based tool designed for Chinese English learners. It automatically extracts advanced vocabulary from English articles (e.g., The Economist), filters out basic words using the Oxford 3000 list, translates them into Chinese, and exports a study-ready Excel file.

本项目旨在辅助中国英语学习者进行深度阅读。它能自动清洗英文文本，过滤掉简单的初高中词汇，提取高阶生词并调用 API 获取中文释义，最终生成 Excel 生词本。

### 🛠 Dependencies (依赖库)
*   Python 3.13
*   pandas
*   openpyxl
*   deep-translator

### 🚀 How to Run (如何运行)
1. Install dependencies:
   ```bash
   pip install -r requirements.txt

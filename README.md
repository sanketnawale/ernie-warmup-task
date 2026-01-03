# ERNIE Warmup Task - z/OS TSO/E Command Reference Web Page

## 🌐 Live Demo
**[View Generated Webpage](https://sanketnawale.github.io/ernie-warmup-task/)**


## 📝 Project Overview
Automated conversion of IBM z/OS TSO/E Command Reference PDF to a modern, responsive web page using:
- **PaddleOCR-VL** for intelligent document parsing
- **ERNIE 4.0** for AI-powered HTML generation
- **GitHub Pages** for hosting

## ✨ Features
- Extracts 1M+ characters from 448-page technical PDF
- Converts to clean, structured format
- Generates beautiful, responsive HTML with modern CSS
- Fully automated pipeline
- IBM-themed professional design

## 🛠️ Technologies
- PaddleOCR-VL (via Baidu AI Studio)
- ERNIE 4.0 LLM
- PyPDF2 (fallback text extraction)
- Python 3.x
- GitHub Pages

## 📦 Installation
Create virtual environment
python3 -m venv venv
source venv/bin/activate

Install dependencies
pip install requests erniebot PyPDF2


## 🚀 Usage
Step 1: Extract PDF
python step1_extract_pdf_v2.py

Step 2: Generate webpage
python step2_generate_webpage.py



## 📊 Project Stats
- **Source PDF**: z/OS V2R4 TSO/E Command Reference (448 pages)
- **Extracted Content**: 1,031,508 characters
- **Generated HTML**: 15,253 characters
- **Processing Time**: ~2 minutes


## 👨‍💻 Author
Sanket Nawale - IBM Z Student Developer  
Specializing in DevOps, Mainframe Systems, and AI Integration

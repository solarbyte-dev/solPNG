# ❄️ SolPNG

A simple **CLI tool** to add, read, and erase custom **PNG metadata**.
Built with Python and [Pillow](https://pillow.readthedocs.io/)

---

## Features
- Write custom metadata (`key: value`) into PNG files
- Read all metadata from PNGs
- **Erase all metadata from PNGs**
- Works on single files or entire folders (recursively)
- Supports **multiple key:value pairs** in one command

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/solarbyte-dev/solpng.git
cd solpng
source solpng/bin/activate
```
---

## Usage

Run with Python 3:

### ➕ Add Metadata
```bash
python3 solpng.py -w "Author: Solar, License: MIT, Tool: SolPNG" image.png
```

### 📖 Read Metadata
```bash
python3 solpng.py -r image.png
```

### 🧹 Erase Metadata
```bash
python3 solpng.py -e image.png
```

### 📂 Process a Folder
```bash
python3 solpng.py -w "Batch: True" ./images/
python3 solpng.py -r ./images/
python3 solpng.py -e ./images/
```
---

## ⚠️ Notes

    1. If your metadata contains !, wrap the string in single quotes (') instead of double quotes (").
    
       ```py 
       python3 solpng.py -w 'Text: Hello! This is a sample PNG!' image.png
       ```
       
    3. Overwriting metadata will preserve existing entries unless erased with -e.

##📜 License

MIT License © 2025 — Made with ❤️ by Solar

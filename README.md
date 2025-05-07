# 💰 kapital - **WIP**

> A terminal-based personal finance tracker powered by [Rich](https://github.com/Textualize/rich) and [Polars](https://www.pola.rs/).  
> Fast, minimal, and a little nostalgic — built for the command line, not the cloud.

---

## ✨ Features

- 📈 Add, view, and export personal transactions in your terminal
- 📊 Beautiful `rich` tables for reports and summaries
- ⚡ Fast performance using `polars` for all data handling
- 📝 Export reports to Excel or Markdown (`.xlsx`, `.md`)
- 🗃️ Data stored locally in `.parquet` or `.db` format — no cloud, no tracking

---

## 🧱 Project Structure

kapital/
├── db/ # Local database
├── reports/ #  Generated reports (Excel/Markdown)
├── main.py # Entry point
├── tracker.py # Core logic
├── exporter.py # Report creation
├── ui.py # Rich prompt/input and styled output
└── requirements.txt # Project dependencies

---

## 🚀 Getting Started

```bash
git clone https://github.com/LeothDev/kapital.git
cd kapital
```

# Setup virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

# Install dependencies
```bash
pip install -r requirements.txt
```

# Run the app
```bash
python main.py
```

---

## 📦 Dependencies

- rich — Terminal UI framework
- polars — Fast dataframe engine
- fastexcel — write .xlsx files
> 📎All declared in requirements.txt

---

## 📘 Example Usage

---

## 🛠️ Made With
- 🐍 Python
- 🎨 Rich
- 🧠 Polars
- ❤️ Terminal Love

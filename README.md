# 🌍 Multilingual Virtual Assistant

A **Streamlit-based multilingual virtual assistant** that allows users to **translate text into multiple languages** and optionally convert translated text into **speech (audio playback + download)**.  
This project dynamically loads supported languages from an external Excel file (`language.xlsx`), ensuring flexibility and easy updates.

---

## ✨ Features
- 📖 **Dynamic Language Loading** – Reads supported languages from `data/language.xlsx`.
- 🌐 **Text Translation** – Translate input text into any supported language.
- 🔊 **Text-to-Speech (TTS)** – Convert translated text into speech using **gTTS** (if supported).
- 🎵 **Audio Playback & Download** – Play the generated audio in-app and download as `.mp3`.
- 🖥 **Streamlit UI** – Simple and interactive interface for seamless translation and speech synthesis.

---

## 📂 Project Structure
multilingual_virtual_asst/
│── data/
│ └── language.xlsx # Contains supported languages and ISO codes
│── app.py # Main Streamlit application
│── requirements.txt # Python dependencies
│── README.md # Project documentation



---

## ⚙️ Installation

### 1️⃣ Clone the repository

git clone https://github.com/your-username/multilingual_virtual_asst.git
cd multilingual_virtual_asst

### INSTALL DEPENDENCIES

pip install -r requirements.txt

📊 Input & Output

Input: Enter text in any language into the input text area.

Output:

Translated text will appear in the TRANSLATED TEXT section.

If TTS is supported, audio playback and a Download Audio File link will be provided.

📑 Dependencies

Streamlit
 – Web app framework

mtranslate
 – Translation API

pandas
 – Excel reading and manipulation

gTTS
 – Text-to-Speech conversion

openpyxl
 – Excel file support

base64
 – File encoding for downloads

Install them manually if needed:

pip install streamlit mtranslate pandas gTTS openpyxl



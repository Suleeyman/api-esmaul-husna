# 🌙 Esmaul Husna API

Free and Open Source API for the 99 names of Allah (الأسماء الحسنى)

This repository provides a structured and multilingual dataset for the 99 Names of Allah, also known as Asma'ul Husna. Each entry includes translations, transliterations, explanations, and audio support—making it ideal for educational, spiritual, or app development purposes.

---

## 📘 Overview

This project includes:

- 🕋 The 99 Names of Allah in Arabic with and without diacritics
- 🌍 Translations and transliterations in multiple languages
- 📝 Short and long explanations of each name
- 🔊 Audio pronunciation files
- 🖼️ Image placeholders for future use

Everything is bundled in a clean JSON format (*ressources/esmaul-husna.json*) and served through an open API (to be optionally self-hosted or integrated).

### 📦 Example Entry

Here’s an example object from the dataset:

```json
{
  "id": "3525c865-3cb7-11f0-b9b7-6045cb6ed61f",
  "name": {
    "ar": "الغفور",
    "ar-enhanced": "ٱلْغَفُورُ",
    "fr": "Le Tout-Pardon",
    "en": "",
    "tr": "Bütün günahları bağışlayan"
  },
  "explanation": {
    "short": {
      "fr": "Le Tout-Pardon, Le Pardonneur, Celui qui pardonne beaucoup.",
      "en": "",
      "tr": ""
    },
    "long": {
      "fr": "Allah est Al-Ghafoor, Il est Celui qui pardonne complètement nos péchés et nos fautes. Son pardon est illimité, et Il est tout à fait compatissant. Il est très haut, son pardon s'étend à tous ceux qui se tournent vers lui en toute humilité et cherchent à se repentir.",
      "en": "",
      "tr": ""
    }
  },
  "transliteration": {
    "fr": "Al-Ghafoor",
    "en": "",
    "tr": "El-Gafûr"
  },
  "audio": "/audio/al-ghafur.mp3",
  "image": {
    "png": {
      "64x64": "",
      "128x128": "",
      "256x256": ""
    },
    "svg": ""
  }
}
```

### 🧾 Field Descriptions

- `id`: A unique identifier in UUID format (e.g., `"3525c865-3cb7-11f0-b9b7-6045cb6ed61f"`).
- `name` (*object*): The name of Allah in different languages:
  - `ar`: Arabic
  - `ar-enhanced`: Arabic with proper diacritics (tashkeel)
  - `fr`, `en`, `tr: French, English, and Turkish translations
- `explanation` (*object*): Descriptions of the meaning of the name:
  - `short`: Concise description per language
  - `long`: Extended explanation per language
- `tranliteration` (*object*): Phonetic transcription of the Arabic name for pronunciation help:
  - `fr`, `en`, `tr`: Per-language transliterations
- `audio`: URL or path to the .mp3 pronunciation file
- `image`: Name-related icons or representations:
  - `png`: Paths for 64x64, 128x128, and 256x256 images
  - `svg`: SVG file path

## 🤝 Contributing

We welcome all kinds of contributions! Here's how you can help:

**✅ Improve the Dataset**

If you notice:
- Missing or inaccurate translations
- Absent explanations in certain languages
- Missing audio or images

Please feel free to update the JSON file and submit a pull request.

**🧩 Add New Fields**

If you'd like to propose a new field, open an issue first to explain your idea before creating a pull request.

---

## 📂 File Structure

```text
ressources/
├── esmaul-husna.json     # Main JSON file with the 99 names
├── audio/                # Optional folder for audio files
└── images/               # Optional folder for PNG/SVG icons
```

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/license/mit).

## 💬 Feedback

Have suggestions, feedback, or need support? Open an issue or start a discussion — we’d love to hear from you.
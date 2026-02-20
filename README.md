[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-FF5E5B?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/ysuleyman)
[![Swagger](https://img.shields.io/badge/OpenAPI-Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)](https://www.esmaulhusna.org/docs)
[![ReDoc](https://img.shields.io/badge/OpenAPI-ReDoc-8A2BE2?style=for-the-badge&logo=redoc&logoColor=white)](https://www.esmaulhusna.org/redoc)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

# 🌙 Esmaul Husna API

Free and Open Source API for the 99 names of Allah (الأسماء الحسنى) also known as Esma'ul Husna. This repository provides a structured and multilingual dataset and ach entry includes translations, transliterations, explanations, images and audio support—making it ideal for educational, spiritual, or app development purposes.

The API is available here : [esmaulhusna.org/](https://esmaulhusna.org/)

**Quick summary**

Open-source FastAPI REST API for structured access to:

- The 99 Names of Allah (Esmaul Husna)
- Related Surah data
- Language-aware responses
- Static media assets for each _esmaul husna_ (audio and images)

## Features

- FastAPI-based REST API
- OpenAPI docs (`/docs`) and ReDoc (`/redoc`)
- TinyDB-backed local data store
- Pagination support for list endpoints
- Optional language filtering
- Static file serving for `/audio` and `/images`

## 📘 Overview

This project includes:

- 🕋 The 99 Names of Allah in Arabic with and without diacritics
- 🌍 Translations and transliterations in multiple languages
- 📝 Short and long explanations of each name
- 🔊 Audio pronunciation files
- 🖼️ Image placeholders for future use

Everything is bundled in a clean JSON format and served through an open API (to be optionally self-hosted or integrated).

### 📦 Example Entry

Here’s an example object from the dataset:

```json
{
    "slug": "ar-rahman",
    "id": 1,
    "ar": "الرحمن",
    "ar-enhanced": "الرَّحْمنُ",
    "name": {
      "fr": "Le Tout-Miséricordieux",
      "en": "The Most Merciful",
      "tr": "Çok rahmet sahibi"
    },
    "explanation": {
      "short": {
        // Multi language short explanation
      },
      "long": {
        // Multi language long explanation
      }
    },
    "transliteration": {
      "iso": "Ar-Raḥmān",
      "popular": {
        // Multi language popular transliteration
      }
    },
    "ipa": "/ar.raħˈmaːn/",
    "audio": "/audio/ar-rahman.mp3",
    "image": {
      "png": {
        "64x64": "/images/rahman/rahman-64x64.png",
        "128x128": "/images/rahman/rahman-128x128.png",
        "256x256": "/images/rahman/rahman-256x256.png"
      },
      "svg": "/images/rahman/rahman.svg"
    },
    "verse": {
      "1": [2],
      [...]
    }
  }
```

### 🧾 Field Descriptions

- `slug`: A unique text identifier in lowercase, typically used in URLs or as a technical key (e.g., "ar-rahman").
- `id`: A unique numeric identifier in a very simple format (int starting from 1).
- `ar`: The name written in standard Arabic script.
- `ar-enhanced`: The name written in Arabic with full diacritical marks (tashkīl) to ensure correct pronunciation.
- `name` (_object_): An object containing the translated name in multiple languages.
- `explanation` (_object_): An object containing explanations of the name.
  - `short` (_object_): A short and concise description in multiple languages.
  - `long` (_object_): A longer and more detailed description in multiple languages.
- `transliteration` (_object_): An object containing different transliteration formats of the Arabic name.
  - `iso`: Academic transliteration following an international standard (including diacritical marks).
  - `popular` (_object_): Common simplified transliterations in multiple languages.
- `ipa`: The International Phonetic Alphabet (IPA) transcription representing the precise pronunciation.
- `audio`: The file path to the audio pronunciation.
- `image` (_object_): An object containing visual resources associated with the name.
  - `png` (_object_): Path for PNG image versions in different sizes.
    - `64x64`: Small size (icon).
    - `128x128`: Medium size.
    - `256x256`: Large size.
  - `svg`: Vector version of the image (SVG format).
- `verse` (_object_): An object listing the occurrences of the name in the Qur’an.
  - Each key (e.g., "1", "2", "7", etc.) represents a Surah (chapter) number.
  - Each value is an array containing the verse numbers where the name appears in that Surah.
  - Example: "55": [1] means the name appears in Surah 55, verse 1.

## About the surah al-Fatiha

Although there is a consensus that Surah al-Fatiha contains seven verses, whether the basmala is one of them remains a subject of debate. According to the Qur’anic recitation scholars of Medina, Basra, and Damascus, the basmala is not part of al-Fatiha. In this case, the first verse is:

```
الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ
```

and the last verse is:

```
غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ
```

This is also the view held by the **Hanafi** and **Maliki** schools. On the other hand, according to the recitation scholars of Mecca and Kufa, the first verse is the _basmala_, and the final verse is:

```
صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ
```

The **Shafi‘i** and **Hanbali** schools follow this opinion as well.

Our choice was to follow the Hanafi school. That's why the esma "rahman" and "rahim" in our JSON don't include the first verse (basmala) of the surah al-Fatiha.

## API

### Endpoints

#### Root

- `GET /` - API metadata and docs links

#### Esmas

- `GET /esmas/` - List all esmas (supports `page`, `limit`, `lg`)
- `GET /esmas/{esma_id}` - Get one esma by ID (supports `lg`)
- `GET /esmas/name/{esma_slug}` - Get one esma by slug (supports `lg`)

#### Surah

- `GET /surah/` - List all surahs (supports `page`, `limit`, `lg`)
- `GET /surah/{number}` - Get one surah by number (supports `lg`)

### Query Parameters

- `lg`: language selector (for localized fields)
- `page`: page number for pagination
- `limit`: page size for pagination

## Quick Start

### Requirements

- Python `>=3.12`
- `uv` package manager

### Install

```bash
uv sync
```

### Run (development)

```bash
uv run fastapi run app/main.py --reload
```

### Run tests

```bash
uv run pytest tests -v --durations=0 --cov --cov-report=term-missing
```

## Project Structure

```text
app/
  main.py
  database.py
  core/
  esma/
  surah/
assets/
  esmaul-husna.json
  surah.json
  static/
    audio/
    images/
tests/
```

## Notes

- Data is seeded during app startup.
- Static media is mounted at:
  - `/audio` -> `assets/static/audio`
  - `/images` -> `assets/static/images`

## 📜 License

This project is licensed under the MIT License. See `LICENSE`.

## 💬 Feedback

Have suggestions, feedback, or need support? Open an issue or start a discussion — we’d love to hear from you.

## 🤝 Contributing

We welcome all kinds of contributions! Here's how you can help:

**✅ Improve the Dataset**

If you notice:

- Missing or inaccurate translations
- Absent explanations in certain languages

Please feel free to update the JSON file and submit a pull request.

**🧩 Add New Fields**

If you'd like to propose a new field, open an issue first to explain your idea before creating a pull request.

**♥️ Financial support**

Currently the API costs me 90.90€ per year :

- 72.00€ per year for the host on CleverCloud
- 18.90€ per year for the domain name [esmaulhusna.org](https://esmaulhusna.org)

If you want to support me financially you can [buy me a coffee](https://ko-fi.com/ysuleyman) it will certainly motivate me on continously improving the REST API.

**📬 A quick thank-you**

If this project helped you, you can send me a message (a comment) on Ko-fi.  
You don’t have to donate — even a simple message of support or a quick “thank you” means a lot and keeps me motivated to continue improving this project.

👉 Write a comment [here](https://ko-fi.com/post/Supporting-the-Esmaul-Husna-REST-API-Z8Z01MKPMF) at the very bottom of the article.

Your encouragement truly makes a difference 🙌
Feel free to send a message — your encouragement keeps this project alive!

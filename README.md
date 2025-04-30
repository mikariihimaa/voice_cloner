# Voice Cloner Web UI (XTTS v2)

Tämä projekti tarjoaa yksinkertaisen www-pohjaisen käyttöliittymän **äänen kloonaamiseen (voice cloning)** englanninkielisellä puhesynteesillä. Käyttäjä voi ladata oman puheääninäytteen (`.wav`), syöttää haluamansa tekstin, ja järjestelmä tuottaa puhesynteesin kloonatulla äänellä käyttäen Coqui TTS -kirjaston XTTS v2 -mallia.

## 🔍 Mitä tämä tekee?

- Käyttää `tts_models/multilingual/multi-dataset/xtts_v2` -mallia tekstin muuntamiseen puheeksi
- Tukee **oman äänen** käyttöä referenssinä (`speaker_wav`)
- Luo ladattavan `.wav`-tiedoston selaimessa
- Toimii Docker-kontissa, joten ei sotke järjestelmäasennusta

## 📦 Projektin rakenne

```
voice-cloner/
├── Dockerfile
├── app.py
├── templates/
│   └── index.html
└── README.md
```

## 🧱 Asennusohjeet (Linux)

### 🔧 Esivaatimukset

- Docker asennettuna

### 🏗 Rakenna ja aja

```bash
docker build -t voice-cloner-image .
docker run -dit -p 5002:5002 --name voice-cloner voice-cloner-image
```

Avaa selaimessa: [http://localhost:5002](http://localhost:5002)

## 🧪 Käyttö

1. Avaa selain ja siirry osoitteeseen `http://localhost:5002`
2. Syötä haluamasi teksti (englanniksi)
3. Lataa oma ääninäyte (`.wav`)
4. Paina **Generate**
5. Lataa valmis kloonattu puhetiedosto (.wav)

## 🔒 Huomautuksia

- Malli ei tue tällä hetkellä suomenkielistä äänen kloonausta.
- Ääninäytteen tulee olla selkeä ja mieluiten 1–10 sekunnin mittainen.

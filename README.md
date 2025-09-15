# leads_to_raags

Analyze Western melodies and map them to Indian raags (Hindustani + Carnatic).
Given a lead sheet or melody, the tool suggests possible raags and gives hints on how to adapt the melody to sound more "raag-like."

---

## 🚀 Quickstart

### 1. Clone & Setup
```bash
git clone https://github.com/yourname/leads_to_raags.git
cd leads_to_raags
uv sync --dev

## 2. Run uv run test
uv run pytest

## 3. Run uv run test
uv run python main.py

---

## 🛠️ Development Workflow
Prepare input
Start with MusicXML or MIDI of a melody (e.g., Stella by Starlight).
PDFs will need OCR → MusicXML conversion (future step).
Melody extraction (core classes)
MelodyExtractor: load MusicXML/MIDI → extract pitch sequence.
MelodyAnalyzer: normalize to scale degrees, build pitch sets.
Raag database
Structured JSON/YAML dataset of Hindustani + Carnatic raags:
Scale (aroha/avarohana).
Thaat/melakarta parent.
Vadi/samvadi (primary/secondary tones).
Pakad (signature phrases).
Matching engine
Compare melody pitch set vs. raag pitch sets.
Rank by overlap and phrase similarity.
Output candidate raags with match scores.
Adaptation suggestions
Suggest characteristic ornaments (gamakas, meends).
Suggest phrasing (pakad).
Optionally generate MIDI/MusicXML with adapted notes.
Web application (later)
Minimal FastAPI app: file upload → JSON of candidate raags.
Frontend:
Staff rendering (VexFlow / ABC.js).
Audio playback of original vs. adapted melody.
Stretch goals
Support user libraries (store analyses).
Add AI/ML component: learn style of raag phrases beyond static pitch sets.
Interactive teaching mode (e.g. highlight "wrong" notes against chosen raag).🛠️ Development Workflow
Prepare input
Start with MusicXML or MIDI of a melody (e.g., Stella by Starlight).
PDFs will need OCR → MusicXML conversion (future step).
Melody extraction (core classes)
MelodyExtractor: load MusicXML/MIDI → extract pitch sequence.
MelodyAnalyzer: normalize to scale degrees, build pitch sets.
Raag database
Structured JSON/YAML dataset of Hindustani + Carnatic raags:
Scale (aroha/avarohana).
Thaat/melakarta parent.
Vadi/samvadi (primary/secondary tones).
Pakad (signature phrases).
Matching engine
Compare melody pitch set vs. raag pitch sets.
Rank by overlap and phrase similarity.
Output candidate raags with match scores.
Adaptation suggestions
Suggest characteristic ornaments (gamakas, meends).
Suggest phrasing (pakad).
Optionally generate MIDI/MusicXML with adapted notes.
Web application (later)
Minimal FastAPI app: file upload → JSON of candidate raags.
Frontend:
Staff rendering (VexFlow / ABC.js).
Audio playback of original vs. adapted melody.
Stretch goals
Support user libraries (store analyses).
Add AI/ML component: learn style of raag phrases beyond static pitch sets.
Interactive teaching mode (e.g. highlight "wrong" notes against chosen raag).
--

Hindustani Raags
Raag Data JSON (Python repo): sanskrit-coders/raaga
JSON files of aroha/avarohana + notes.
https://github.com/sanskrit-coders/raaga

SwarClassicalMusic Raag DB: swarclassicalmusic/raaga-database
300+ raags, structured data with vadi/samvadi, aroha/avarohana.
https://github.com/swarclassicalmusic/raaga-database

Carnatic Raags
Carnatic Music Database (CMDB): carnatic/carnatic-music-database
Machine-readable data on all 72 melakarta ragas + janya ragas.
https://github.com/carnatic/carnatic-music-database
Karnatik.com data (unofficial): Large table of ragas with arohanam/avarohanam (scrapable, but license check needed).
Karnatik.com data

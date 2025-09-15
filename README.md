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

### Project: Leads to Raags 🎶

This project aims to create a web application that analyzes a piece of Western sheet music or a lead sheet and suggests corresponding raags from both the Carnatic and Hindustani traditions. It also provides guidance on how to adapt the melody to an Indian classical feel.

***

### Project Plan

This is a large-scale music information retrieval (MIR) and machine learning project that can be broken down into the following stages:

- **1. Data Ingestion & Pre-processing:** The system will accept digital input, such as MIDI or machine-readable notation files. This data will be loaded and structured for a distributed computing environment.
- **2. Feature Engineering:** This is the most crucial part of the pipeline. The raw musical data will be converted into a numerical format. This process will go beyond simple note identification to capture the unique elements of Indian classical music.
    - **Pitch & Rhythm:** Extracting pitch contours, note durations, and rhythmic patterns.
    - **Ornamentation:** Identifying subtle slides and graces (**gamakas**) that are a hallmark of Indian classical music. This will likely require advanced signal processing techniques.
- **3. Raga Identification Model:** A machine learning model, likely a deep neural network, will be trained on a large dataset of raags and their features. The model will then predict the most probable raags for a given piece of music.
- **4. Suggestion Engine:** A rule-based or generative model will use the identified raag to offer adaptation suggestions, such as:
    - Which notes to emphasize (**vadi** and **samvadi**).
    - Characteristic melodic phrases to incorporate (**chalan**).
    - Possible rhythmic changes (e.g., to a different **tala**).

***

### Technology Stack

The project will be built with a focus on scalability to handle large datasets.

- **PySpark:** Ideal for processing and analyzing large-scale musical data. PySpark's MLlib library provides powerful, distributed machine learning algorithms, which are essential for training the raga identification model.
- **Music Information Retrieval (MIR) Libraries:**
    - [**Librosa**](https://librosa.org/doc/latest/index.html): A Python library for audio analysis that can extract crucial features like pitch, rhythm, and MFCCs.
    - **Essentia:** An open-source C++ library with Python bindings for audio analysis and MIR.
    - **Muda:** A Python library for musical data augmentation, which can help create a more robust training dataset.

***

### Possible Data Sources

Finding well-structured, machine-readable datasets for Indian classical music is a key challenge. Here are some excellent sources for your model:

- **Academic Datasets:**
    - **CompMusic & Saraga:** These academic projects provide high-quality, annotated datasets of Carnatic and Hindustani music, including musical theoretical concepts like **gamakas** and other stylistic annotations.
    - **"Raga Database":** A project from the University of Pennsylvania that offers a structured database of Hindustani raags with details on their scales and characteristic phrases.

- **Symbolic and Audio Data:**
    - **MIDI Files:** While not always rich enough to capture all the nuances of Indian classical music, MIDI files can be a good starting point for symbolic analysis.
    - **Publicly Available Recordings:** While not pre-annotated, a large corpus of recordings from archives and online platforms can be used for feature extraction. This would require a significant effort to label the data.

***

### Roadmap

1.  **Phase 1: Research & Data Collection:**
    - Download and explore existing academic datasets.
    - Set up a PySpark environment.
    - Develop scripts for data ingestion and cleaning.

2.  **Phase 2: Feature Engineering & Prototyping:**
    - Use MIR libraries to extract features from the datasets.
    - Build a prototype machine learning model to test initial classification accuracy.

3.  **Phase 3: Model Development & Refinement:**
    - Train a scalable deep learning model on the full dataset using PySpark.
    - Evaluate and fine-tune the model to improve raga identification accuracy.

4.  **Phase 4: Application Development:**
    - Develop the front-end user interface.
    - Integrate the machine learning model to provide real-time predictions.
    - Build the rule-based suggestion engine.

    ### Project: Leads to Raags 🎶

    This project aims to create a web application that analyzes a piece of Western sheet music or a lead sheet and suggests corresponding raags from both the Carnatic and Hindustani traditions. It also provides guidance on how to adapt the melody to an Indian classical feel.

    ***

    ### Project Plan

    This is a large-scale music information retrieval (MIR) and machine learning project that can be broken down into the following stages:

    - **1. Data Ingestion & Pre-processing:** The system will accept digital input, such as MIDI or machine-readable notation files. This data will be loaded and structured for a distributed computing environment.
    - **2. Feature Engineering:** This is the most crucial part of the pipeline. The raw musical data will be converted into a numerical format. This process will go beyond simple note identification to capture the unique elements of Indian classical music.
        - **Pitch & Rhythm:** Extracting pitch contours, note durations, and rhythmic patterns.
        - **Ornamentation:** Identifying subtle slides and graces (**gamakas**) that are a hallmark of Indian classical music. This will likely require advanced signal processing techniques.
    - **3. Raga Identification Model:** A machine learning model, likely a deep neural network, will be trained on a large dataset of raags and their features. The model will then predict the most probable raags for a given piece of music.
    - **4. Suggestion Engine:** A rule-based or generative model will use the identified raag to offer adaptation suggestions, such as:
        - Which notes to emphasize (**vadi** and **samvadi**).
        - Characteristic melodic phrases to incorporate (**chalan**).
        - Possible rhythmic changes (e.g., to a different **tala**).

    ***

    ### Technology Stack

    The project will be built with a focus on scalability to handle large datasets.

    - **PySpark:** Ideal for processing and analyzing large-scale musical data. PySpark's MLlib library provides powerful, distributed machine learning algorithms, which are essential for training the raga identification model.
    - **Music Information Retrieval (MIR) Libraries:**
        - [**Librosa**](https://librosa.org/doc/latest/index.html): A Python library for audio analysis that can extract crucial features like pitch, rhythm, and MFCCs.
        - **Essentia:** An open-source C++ library with Python bindings for audio analysis and MIR.
        - **Muda:** A Python library for musical data augmentation, which can help create a more robust training dataset.

    ***

    ### Possible Data Sources

    Finding well-structured, machine-readable datasets for Indian classical music is a key challenge. Here are some excellent sources for your model:

    - **Academic Datasets:**
        - **CompMusic & Saraga:** These academic projects provide high-quality, annotated datasets of Carnatic and Hindustani music, including musical theoretical concepts like **gamakas** and other stylistic annotations.
        - **"Raga Database":** A project from the University of Pennsylvania that offers a structured database of Hindustani raags with details on their scales and characteristic phrases.

    - **Symbolic and Audio Data:**
        - **MIDI Files:** While not always rich enough to capture all the nuances of Indian classical music, MIDI files can be a good starting point for symbolic analysis.
        - **Publicly Available Recordings:** While not pre-annotated, a large corpus of recordings from archives and online platforms can be used for feature extraction. This would require a significant effort to label the data.

    ***

    ### Roadmap

    1.  **Phase 1: Research & Data Collection:**
        - Download and explore existing academic datasets.
        - Set up a PySpark environment.
        - Develop scripts for data ingestion and cleaning.

    2.  **Phase 2: Feature Engineering & Prototyping:**
        - Use MIR libraries to extract features from the datasets.
        - Build a prototype machine learning model to test initial classification accuracy.

    3.  **Phase 3: Model Development & Refinement:**
        - Train a scalable deep learning model on the full dataset using PySpark.
        - Evaluate and fine-tune the model to improve raga identification accuracy.

    4.  **Phase 4: Application Development:**
        - Develop the front-end user interface.
        - Integrate the machine learning model to provide real-time predictions.
        - Build the rule-based suggestion engine.

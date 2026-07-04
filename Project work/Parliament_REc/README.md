# 🇮🇳 ParliamentAI
### An Intelligent Search, Analysis & Recommendation System for Indian Lok Sabha Questions

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green)
![NLP](https://img.shields.io/badge/NLP-TFIDF-orange)
![Sentence Transformers](https://img.shields.io/badge/Sentence-Transformers-red)
![FAISS](https://img.shields.io/badge/FAISS-VectorSearch-purple)
![Gradio](https://img.shields.io/badge/Gradio-WebApp-yellow)

---

## 📌 Project Overview

ParliamentAI is an AI-powered information retrieval and recommendation system built using Indian Lok Sabha parliamentary questions.

The project combines **Natural Language Processing (NLP)**, **Machine Learning**, **Semantic Search**, and **Recommendation Systems** to help users explore parliamentary data intelligently.

Instead of traditional keyword matching, ParliamentAI understands the **semantic meaning** of a user's query and retrieves the most relevant parliamentary questions.

---

## 🎯 Objectives

- Analyze parliamentary question data using Exploratory Data Analysis (EDA)
- Predict the responsible ministry from the subject of a parliamentary question
- Perform semantic search using sentence embeddings
- Recommend similar parliamentary questions
- Build an interactive AI application using Gradio

---

# 📂 Dataset

The project uses publicly available Lok Sabha datasets containing parliamentary questions.

### Features

- Question Number
- Subject
- Member of Parliament
- Ministry
- Lok Sabha Number
- Session Number
- Question Type
- Date
- Supplementary Question Indicator
- Year

Dataset Size:

- **37,000+ Parliamentary Questions**

---

# 🚀 Project Pipeline

```
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Text Preprocessing
      │
      ▼
TF-IDF Feature Engineering
      │
      ▼
Ministry Classification
      │
      ▼
Sentence Embeddings
      │
      ▼
Semantic Search (FAISS)
      │
      ▼
Recommendation Engine
      │
      ▼
Gradio Interface
```

---

# 📊 Exploratory Data Analysis

Performed comprehensive analysis including:

- Questions per year
- Questions per Lok Sabha
- Questions per session
- Ministry-wise distribution
- Member-wise distribution
- Question type analysis
- Subject frequency analysis
- Word Cloud visualization
- Time trend analysis

---

# 🧠 NLP Pipeline

The following preprocessing techniques were applied:

- Lowercasing
- Tokenization
- Stopword Removal
- Lemmatization
- TF-IDF Vectorization

---

# 🤖 Machine Learning

### Problem Statement

Predict the responsible ministry based on the parliamentary question subject.

### Feature

- Subject

### Target

- Ministry

### Models Evaluated

- Logistic Regression
- Multinomial Naive Bayes
- Linear SVM
- Random Forest

### Best Model

**Logistic Regression**

### Accuracy

**85%**

---

# 🔍 Semantic Search

Semantic search was implemented using:

- Sentence Transformers
- all-MiniLM-L6-v2
- FAISS Vector Database

Instead of keyword matching, the system retrieves semantically similar parliamentary questions.

Example:

Input

```
solar energy subsidy
```

Returns

- Rooftop Solar Scheme
- Renewable Energy Projects
- Solar Power Generation
- National Solar Mission

---

# 💡 Recommendation Engine

The recommendation engine suggests parliamentary questions related to the user's search by leveraging semantic similarity.

---

# 🖥️ Application

A Gradio interface was developed that allows users to:

- Predict Ministry
- Search Parliamentary Questions
- View Similar Questions
- Get Recommendations

---

# 📁 Project Structure

```
ParliamentAI/

│
├── notebooks/
│   ├── questions_EDA.ipynb
│   ├── debates_EDA.ipynb
│   ├── NLP.ipynb
│   ├── classifier.ipynb
│   ├── semantic_search.ipynb
│   ├── recommender.ipynb
│   └── app.ipynb
│
├── models/
│
├── data/
│
├── requirements.txt
│
└── README.md
```

---

# 🛠️ Technologies Used

### Programming

- Python

### Data Analysis

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn
- WordCloud

### Machine Learning

- Scikit-learn

### NLP

- NLTK
- Sentence Transformers

### Vector Search

- FAISS

### Web Application

- Gradio

---

# 📈 Results

| Task | Result |
|------|---------|
| Ministry Classification | **85% Accuracy** |
| Semantic Search | Successfully retrieves contextually similar parliamentary questions |
| Recommendation System | Generates relevant parliamentary question recommendations |
| Interactive Interface | Developed using Gradio |

---

# 🔮 Future Improvements

- Retrieval-Augmented Generation (RAG)
- Debate Summarization using Large Language Models
- Question Answering over Parliamentary Records
- Interactive Analytics Dashboard
- Named Entity Recognition (NER)
- Topic Modeling
- Knowledge Graph Construction
- Multilingual Support

---

# 📚 Key Concepts Demonstrated

- Exploratory Data Analysis
- Natural Language Processing
- TF-IDF Feature Engineering
- Multi-class Classification
- Semantic Search
- Sentence Embeddings
- Vector Databases
- Recommendation Systems
- Information Retrieval
- Interactive AI Applications

---

# 💼 Resume Highlights

- Developed an AI-powered semantic search system for 37,000+ Indian parliamentary questions.
- Built a multi-class NLP classifier achieving **85% accuracy** for ministry prediction.
- Implemented semantic retrieval using Sentence Transformers and FAISS.
- Designed a recommendation engine for contextually similar parliamentary questions.
- Built an interactive Gradio-based AI application for intelligent parliamentary search.

---

# 👨‍💻 Author

**Aatif Khan**


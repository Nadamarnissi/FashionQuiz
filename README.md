# FashionQuiz Backend

Backend API développé avec FastAPI pour l'application mobile FashionQuiz.

## Technologies utilisées

- FastAPI
- Firebase
- PostgreSQL
- Ollama
- Phi-3
- Uvicorn

---

## Fonctionnalités

- Authentification utilisateur
- Gestion des quiz
- Gestion des scores
- Chatbot IA
- Feedback IA
- API REST

---

## Installation

### Créer et activer le virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## Lancer le backend

```bash
uvicorn app.main:app --reload
```

---

## URL locale

```text
http://127.0.0.1:8000
```

---

## IA utilisée

Le chatbot utilise :

- Ollama
- Modèle Phi-3

Lancer Ollama :

```bash
ollama serve
```

---
# Demo Video

[Watch FashionQuiz Demo](./demo/fashionquiz-demo.mp4)

## Auteur

Nada Marnissi

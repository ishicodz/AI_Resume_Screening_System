# AI Resume Screening System

An AI-powered Resume Screening System built using **Python**, **Streamlit**, and **Scikit-learn** that automatically ranks resumes based on their similarity to a given job description.

## Overview

Recruiters often receive hundreds of resumes for a single job opening, making the initial screening process time-consuming. This project simplifies that process by allowing users to upload multiple resumes in PDF format and compare them against a job description.

The system extracts text from each resume, converts both the resumes and the job description into numerical vectors, and computes the **Cosine Similarity** score to rank candidates based on how closely their resumes match the job requirements.

## Features

* Upload multiple PDF resumes.
* Paste any job description.
* Automatic text extraction from resumes.
* Resume ranking based on similarity score.
* Percentage match for each candidate.
* Simple and interactive Streamlit web interface.

## Tech Stack

* **Python**
* **Streamlit**
* **Scikit-learn**
* **PyPDF2 / PyMuPDF**
* **TF-IDF Vectorizer**
* **Cosine Similarity**

## How It Works

1. The user pastes a job description into the application.
2. One or more resumes are uploaded in PDF format.
3. The application extracts text from each resume.
4. TF-IDF converts the job description and resumes into numerical feature vectors.
5. Cosine Similarity measures how closely each resume matches the job description.
6. The resumes are ranked from the highest to the lowest match percentage.

## Learning Outcomes

This project demonstrates:

* Natural Language Processing (NLP)
* Information Retrieval
* Text Vectorization (TF-IDF)
* Cosine Similarity
* PDF Text Processing
* Machine Learning fundamentals
* Streamlit web application development


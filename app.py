import streamlit as st
import fitz  
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(uploaded_file):
    """Extract text from a PDF using PyMuPDF."""
    text = ""

    try:
        pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

        for page in pdf:
            text += page.get_text()

        pdf.close()

    except Exception as e:
        st.error(f"Error reading {uploaded_file.name}: {e}")

    return text.strip()


st.set_page_config(page_title="AI Resume Screening", layout="wide")

st.title("📄 AI Resume Screening System")

st.write(
    "Upload multiple resumes and compare them against a Job Description."
)

job_description = st.text_area(
    "Paste Job Description",
    height=200
)

uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Rank Resumes"):

    if not job_description.strip():
        st.warning("Please enter a Job Description.")
        st.stop()

    if not uploaded_files:
        st.warning("Please upload at least one resume.")
        st.stop()

    documents = [job_description]
    resume_names = []

    with st.spinner("Analyzing resumes..."):

        for file in uploaded_files:

            resume_text = extract_text_from_pdf(file)

            if resume_text:
                documents.append(resume_text)
                resume_names.append(file.name)

        if len(documents) == 1:
            st.error("No readable text found in the uploaded resumes.")
            st.stop()

        vectorizer = TfidfVectorizer(stop_words="english")

        vectors = vectorizer.fit_transform(documents)

        similarity_scores = cosine_similarity(
            vectors[0:1],
            vectors[1:]
        ).flatten()

        results = list(zip(resume_names, similarity_scores))

        results.sort(key=lambda x: x[1], reverse=True)

    st.success("Analysis Complete!")

    st.subheader("Resume Rankings")

    for i, (name, score) in enumerate(results, start=1):

        st.write(f"### {i}. {name}")

        st.progress(float(score))

        st.write(f"Match Score: **{score*100:.2f}%**")

        st.divider()
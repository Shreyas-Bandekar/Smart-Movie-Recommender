# Movie Recommendation System

Small two-part app for movie discovery and recommendations.

## Structure

- `main.py` - FastAPI backend that serves movie details, TMDB search, and recommendation endpoints.
- `app.py` - Streamlit frontend that consumes the API and renders the UI.
- `data/` - raw dataset inputs, currently `movies_metadata.csv`.
- `models/` - serialized artifacts used by the backend: `df.pkl`, `indices.pkl`, `tfidf.pkl`, `tfidf_matrix.pkl`.
- `notebook/` - training and experimentation notebook, currently `moveis.ipynb`.

## Run Locally

1. Set `TMDB_API_KEY` in a local `.env` file.
2. Start the API:

```bash
uvicorn main:app --reload
```

3. Start the Streamlit app in a second terminal:

```bash
streamlit run app.py
```

If you want to force a specific backend, set `API_BASE` before launching Streamlit. Otherwise the app will try the configured URL, then localhost, then the deployed API.

## Notes

- The backend now prefers the `models/` folder and still falls back to the project root for older artifact layouts.
- The notebook filename is still `moveis.ipynb`; it looks like a typo, but I left it unchanged to avoid breaking references.

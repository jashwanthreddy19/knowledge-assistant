import logging, os
import streamlit as st
from agent import run_agent

# ─── Setup & WIDE LAYOUT ─────────────────────────────────────────────────
logging.getLogger("streamlit.watcher.local_sources_watcher").setLevel(logging.ERROR)
UPLOAD_DIR = "data"
os.makedirs(UPLOAD_DIR, exist_ok=True)

st.set_page_config(page_title="RAG Agent", layout="wide")

# ─── TIGHTER CSS ─────────────────────────────────────────────────────────
# remove the large default top-padding in the block container and columns
st.markdown(
    """
    <style>
      /* remove top padding around the whole page */
      .block-container {
        padding-top: 0rem;
      }
      /* remove the little gutter above each column area */
      .css-1lcbmhc {  /* this is the "row" container in wide mode */
        margin-top: 0rem !important;
      }
    </style>
    """,
    unsafe_allow_html=True
)

# ─── HEADER (full-width, centered) ───────────────────────────────────────
st.markdown("<div style='text-align:center; margin-top:1rem;'>", unsafe_allow_html=True)
st.title("🧠 Intelligent Q&A Agent")
st.info("ℹ️ The model will answer questions **only based on the uploaded text documents**. Please upload `.txt` files below.")
st.markdown("</div>", unsafe_allow_html=True)

# ─── MAIN ROW: 3 COLUMNS ─────────────────────────────────────────────────
col_left, col_mid, col_right = st.columns([1, 2, 1], gap="medium")

# ← Left sidebar: docs upload & delete, starts at very top
with col_left:
    st.subheader("📄 Uploaded Documents")
    files = sorted(os.listdir(UPLOAD_DIR))
    if files:
        for fname in files:
            path = os.path.join(UPLOAD_DIR, fname)
            st.markdown(f"• `{fname}`")
            if st.button(f"🗑 Delete '{fname}'", key=f"del_{fname}"):
                os.remove(path)
                st.rerun()
    else:
        st.info("No documents uploaded yet.")
    st.markdown("---")
    st.subheader("📤 Upload `.txt` Files")
    uploaded = st.file_uploader("", type="txt", accept_multiple_files=True, key="uploader")
    if uploaded:
        for f in uploaded:
            dest = os.path.join(UPLOAD_DIR, f.name)
            with open(dest, "wb") as out:
                out.write(f.getbuffer())
        st.success("✅ Uploaded!")
        st.rerun()

# → Center: big query box (also top-aligned by default)
with col_mid:
    st.markdown("<div style='padding-top:1rem;'>", unsafe_allow_html=True)
    query = st.text_input("💬 Ask me anything based on the documents:")
    if query:
        with st.spinner("🤖 Thinking..."):
            try:
                answer = run_agent(query)
            except Exception as e:
                answer = f"⚠️ Error:\n```\n{e}\n```"
        st.subheader("Answer")
        st.write(answer)
    st.markdown("</div>", unsafe_allow_html=True)

# → Right sidebar: logs, also starting at very top
with col_right:
    st.markdown("## LOGGING information…")
    log_file = "logs/app.log"
    if os.path.exists(log_file):
        logs = open(log_file, encoding="utf-8").read().strip().splitlines()
        logs.reverse()  # Newest logs first
        st.text_area("", "\n".join(logs), height=600)
    else:
        st.write("_No logs available._")


import os
import streamlit as st

from data_generator import generate_dataset
from dirty_data import make_dataset_dirty
from llm_helper import get_domain_context
from solution_generator import generate_cleaning_solution

os.makedirs(
    "outputs",
    exist_ok=True
)

st.set_page_config(
    page_title="Synthetic Data Generator",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Synthetic Data Generator")

st.write(
    "Generate messy fake datasets and learn data cleaning."
)

# ----------------------------------
# SESSION STATE
# ----------------------------------

if "dataset_generated" not in st.session_state:
    st.session_state.dataset_generated = False

if "df" not in st.session_state:
    st.session_state.df = None

if "issues" not in st.session_state:
    st.session_state.issues = []

if "domain" not in st.session_state:
    st.session_state.domain = ""

# ----------------------------------
# SIDEBAR
# ----------------------------------

st.sidebar.header("Dataset Settings")

domain = st.sidebar.text_input(
    "Dataset Domain",
    placeholder="Students"
)

columns = st.sidebar.text_area(
    "Columns",
    placeholder="""
Student_Name,
Email,
Division,
Marks
"""
)

rows = st.sidebar.selectbox(
    "Rows",
    [10, 25, 50, 100, 250, 500]
)

difficulty = st.sidebar.selectbox(
    "Messiness Level",
    [
        "Easy",
        "Medium",
        "Hard"
    ]
)

generate_button = st.sidebar.button(
    "Generate Dataset"
)

# ----------------------------------
# GENERATE DATASET
# ----------------------------------

if generate_button:

    if not domain or not columns:

        st.error(
            "Please provide all inputs."
        )

    else:

        with st.spinner(
            "Generating dataset..."
        ):

            context = get_domain_context(
                domain
            )

            df = generate_dataset(
                columns,
                rows
            )

            df, issues = make_dataset_dirty(
                df,
                difficulty
            )

            st.session_state.df = df
            st.session_state.issues = issues
            st.session_state.domain = domain
            st.session_state.context = context
            st.session_state.dataset_generated = True

            df.to_csv(
                "outputs/generated_dataset.csv",
                index=False
            )

# ----------------------------------
# DISPLAY DATASET
# ----------------------------------

if st.session_state.dataset_generated:

    df = st.session_state.df
    issues = st.session_state.issues

    st.info(
        f"Dataset Context: {st.session_state.context}"
    )

    st.success(
        "Dataset Generated Successfully!"
    )

    st.subheader(
        "Dataset Preview"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.subheader(
        "Detected Issues"
    )

    for issue in issues:

        st.write(
            f"✅ {issue}"
        )

    csv = df.to_csv(
        index=False
    ).encode(
        "utf-8"
    )

    st.download_button(
        label="⬇ Download Dataset",
        data=csv,
        file_name=f"{st.session_state.domain}_dataset.csv",
        mime="text/csv"
    )

    st.markdown("---")

    # ----------------------------------
    # SOLUTION SECTION
    # ----------------------------------

    st.subheader(
        "🧹 Generate Cleaning Solution"
    )

    language = st.radio(
        "Choose Language",
        [
            "Python",
            "SQL"
        ]
    )

    if st.button(
        "Generate Solution"
    ):

        profile = f"""
Columns:
{list(df.columns)}

Rows:
{len(df)}

Missing Values:
{df.isnull().sum()}

Duplicates:
{df.duplicated().sum()}

Sample Data:
{df.head(15).to_string()}
"""

        with st.spinner(
            "Generating Cleaning Solution..."
        ):

            solution = (
                generate_cleaning_solution(
                    profile,
                    language,
                    issues
                )
            )

        st.success(
            f"{language} solution generated."
        )

        st.code(
            solution,
            language=(
                "python"
                if language == "Python"
                else "sql"
            )
        )

        st.download_button(
            label=f"⬇ Download {language} Solution",
            data=solution,
            file_name=f"{language.lower()}_cleaning_solution.txt"
        )
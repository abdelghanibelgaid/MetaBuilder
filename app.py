import streamlit as st
import pandas as pd
from transformers import pipeline

# Load a GPT model (example using Hugging Face transformers with GPT-J or GPT-Neo)
@st.cache(allow_output_mutation=True)
def load_model():
    model = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")
    return model

# Helper function to generate full code
def generate_code(metadata_df, frontend, backend, database, data_fetch, interface_type, model):
    metadata_columns = "\n".join([f"- {col}" for col in metadata_df['Column Name']])
    
    prompt = f"""
    Generate full stack code for a {interface_type} interface with {frontend}, {backend}, and {database}.
    Metadata columns: {metadata_columns}
    Backend setup: {backend} with {database}
    Frontend setup: {frontend}
    Data fetching method: {data_fetch}
    """
    
    # Generate full code using the model
    generated_code = model(prompt, max_length=1000)[0]['generated_text']
    return generated_code

def main():
    st.title("Full-Stack Code Generator")

    st.write("Upload metadata, select your tech stack, and generate full-stack code.")

    # Upload the metadata file (Excel)
    uploaded_file = st.file_uploader("Upload Metadata (Excel)", type=["xlsx", "xls"])

    if uploaded_file is not None:
        # Read the uploaded Excel file
        metadata_df = pd.read_excel(uploaded_file)
        
        if 'Column Name' not in metadata_df.columns:
            st.error("The uploaded file must contain a 'Column Name' column.")
            return
        
        # Display metadata preview
        st.subheader("Metadata Preview")
        st.dataframe(metadata_df)

        # Select frontend, backend, database, and data fetch method
        frontends = ['ReactJS', 'Angular', 'VueJS']
        backends = ['NodeJS', 'Django', 'Flask']
        databases = ['MySQL', 'PostgreSQL', 'MongoDB', 'SQLite']
        data_fetch_methods = ['REST API', 'GraphQL', 'WebSockets']
        interfaces = ['Display Data', 'Enter Data', 'Display and Enter Data']

        frontend = st.selectbox("Pick a Frontend Framework", frontends)
        backend = st.selectbox("Pick a Backend Framework", backends)
        database = st.selectbox("Pick a Database", databases)
        data_fetch = st.selectbox("Pick a Data Fetch Method", data_fetch_methods)
        interface_type = st.selectbox("Select the Interface Type", interfaces)

        # Load the LLM model
        model = load_model()

        # Generate the code
        if st.button("Generate Code"):
            generated_code = generate_code(metadata_df, frontend, backend, database, data_fetch, interface_type, model)
            st.subheader("Generated Full-Stack Code")
            st.code(generated_code, language='javascript')

            # Provide an option to download the generated code
            st.download_button(
                label="Download Generated Code",
                data=generated_code,
                file_name='fullstack_code.js',
                mime='text/plain'
            )

if __name__ == "__main__":
    main()

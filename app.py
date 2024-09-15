import streamlit as st
import pandas as pd
import openai

# Function to generate full-stack code using OpenAI API (chat-based)
def generate_code_with_openai(metadata_df, frontend, backend, database, data_fetch, interface_type, api_key):
    metadata_columns = "\n".join([f"- {col}" for col in metadata_df['Column Name']])
    
    prompt = f"""
    You are an AI developer assistant. Generate full-stack code for a {interface_type} interface with {frontend}, {backend}, and {database}.
    The following are the metadata columns: {metadata_columns}.
    Backend setup should use {backend} with {database}.
    Frontend setup should use {frontend}.
    The data fetching method should be {data_fetch}.
    """

    # Use OpenAI API to generate code
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for generating code."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        temperature=0.5,
    )
    
    generated_code = response['choices'][0]['message']['content'].strip()
    return generated_code

def main():
    st.title("Full-Stack Code Generator")

    st.write("Upload metadata, select your tech stack, and generate full-stack code using OpenAI's API.")

    # User enters OpenAI API Key
    api_key = st.text_input("Enter your OpenAI API Key", type="password")

    # Upload the metadata file (Excel)
    uploaded_file = st.file_uploader("Upload Metadata (Excel)", type=["xlsx", "xls"])

    if uploaded_file is not None and api_key:
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

        # Generate the code
        if st.button("Generate Code"):
            generated_code = generate_code_with_openai(metadata_df, frontend, backend, database, data_fetch, interface_type, api_key)
            
            # Display the generated code
            st.subheader("Generated Full-Stack Code")
            st.code(generated_code, language='javascript')

            # Option to download the generated code
            st.download_button(
                label="Download Generated Code",
                data=generated_code,
                file_name='fullstack_code.js',
                mime='text/plain'
            )

if __name__ == "__main__":
    main()

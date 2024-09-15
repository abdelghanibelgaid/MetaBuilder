import streamlit as st
import pandas as pd

# Supported options for frontend, backend, database, and data fetch methods
frontends = ['ReactJS', 'Angular', 'VueJS']
backends = ['NodeJS', 'Django', 'Flask']
databases = ['MySQL', 'PostgreSQL', 'MongoDB', 'SQLite']
data_fetch_methods = ['REST API', 'GraphQL', 'WebSockets']

# Interface types
interfaces = ['Display Data', 'Enter Data', 'Display and Enter Data']

# Function to generate interface based on user selections
def generate_code(metadata_df, frontend, backend, database, data_fetch, interface_type):
    code = f"# Generated code for {interface_type} interface with {frontend}, {backend}, and {database}\n"
    
    code += f"\n# Metadata columns:\n"
    for column in metadata_df['Column Name']:
        code += f"# - {column}\n"
    
    code += f"\n# Backend setup ({backend} with {database})\n"
    if backend == "NodeJS":
        code += f"const express = require('express');\nconst app = express();\n// Add routes and database integration ({database}) here...\n"
    elif backend == "Django":
        code += "import django\n# Setup Django views, models, and database connections here...\n"
    elif backend == "Flask":
        code += "from flask import Flask\napp = Flask(__name__)\n# Add Flask routes and database integration here...\n"

    code += f"\n# Frontend setup ({frontend})\n"
    if frontend == "ReactJS":
        code += "import React from 'react';\n// Add React components and pages here...\n"
    elif frontend == "Angular":
        code += "import { Component } from '@angular/core';\n// Add Angular components and pages here...\n"
    elif frontend == "VueJS":
        code += "import Vue from 'vue';\n// Add Vue components and pages here...\n"
    
    code += f"\n# Data fetching method: {data_fetch}\n"
    if data_fetch == "REST API":
        code += "fetch('/api/data').then(response => response.json()).then(data => console.log(data));\n"
    elif data_fetch == "GraphQL":
        code += "fetch('/graphql', { method: 'POST', body: JSON.stringify({ query: '{ allData { id name } }' }) });\n"
    elif data_fetch == "WebSockets":
        code += "const socket = new WebSocket('ws://localhost:8080');\nsocket.onmessage = (event) => { console.log(event.data); };\n"

    if interface_type == "Display Data":
        code += "\n# Display data interface (Frontend) - Use the frontend library to display data here.\n"
    elif interface_type == "Enter Data":
        code += "\n# Enter data interface (Frontend) - Use the frontend library to create forms for data entry.\n"
    elif interface_type == "Display and Enter Data":
        code += "\n# Display and Enter Data - Combine data display and forms for entry here.\n"

    return code

def main():
    st.title("Automated Interface Generator")

    st.write("""
    Upload metadata and select your stack to automatically generate a frontend, backend, and database interface.
    """)

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
        frontend = st.selectbox("Pick a Frontend Framework", frontends)
        backend = st.selectbox("Pick a Backend Framework", backends)
        database = st.selectbox("Pick a Database", databases)
        data_fetch = st.selectbox("Pick a Data Fetch Method", data_fetch_methods)

        # Select the type of interface
        interface_type = st.selectbox("Select the Interface Type", interfaces)

        # Generate and display the code
        if st.button("Generate Interface"):
            generated_code = generate_code(metadata_df, frontend, backend, database, data_fetch, interface_type)
            
            # Display the template within the app
            st.subheader("Generated Interface Template")
            st.code(generated_code, language='python')
            
            # Optionally allow user to download the template (you can implement file download here)
            st.download_button(
                label="Download Generated Code",
                data=generated_code,
                file_name='generated_interface_template.py',
                mime='text/plain'
            )

if __name__ == "__main__":
    main()

# MetaBuilder

**MetaBuilder** is a Streamlit-based tool that allows you to generate full-stack code templates from your database metadata. By selecting your preferred tech stack (frontend, backend, and database), the app uses the OpenAI API to generate a complete interface with options for displaying or entering data.

## Features

- **Upload Metadata**: Upload an Excel file containing metadata columns (e.g., table name, column name, description).
- **Choose Tech Stack**: Select from popular frontend, backend, and database technologies (e.g., ReactJS, NodeJS, MySQL).
- **Generate Full-Stack Code**: Automatically generate code templates using OpenAI's API (version 0.28.0).
- **Download Code**: Download the generated code directly from the app for further use.

---

## How to Use the App

### 1. Installation

#### Prerequisites:
- **Python 3.7+**
- **OpenAI API Key** (version `0.28.0` of the OpenAI library)

#### Step-by-Step Installation:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/MetaBuilder.git
   cd MetaBuilder
   ```

2. **Install Dependencies**:
   Run the following command to install the required dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**:
   Start the Streamlit app with the following command:
   ```bash
   streamlit run app.py
   ```

   The app will open in your default browser.

---

### 2. Using the App

1. **Enter OpenAI API Key**:
   - Upon opening the app, you’ll be prompted to enter your OpenAI API key. You can obtain an API key by signing up at [OpenAI](https://beta.openai.com/signup/).

2. **Upload Metadata File**:
   - Upload an Excel file that contains the metadata of your database. A sample file (`transaction_metadata.xlsx`) is provided for testing purposes. The file should contain columns like `Column Name`, `Table Name`, and `Description`.

3. **Select Tech Stack**:
   - Select the frontend framework (e.g., ReactJS), backend framework (e.g., NodeJS), and the database technology (e.g., MySQL).
   - Choose the data fetching method (e.g., REST API, GraphQL) and the interface type (e.g., Display Data, Enter Data, or both).

4. **Generate Code**:
   - Once you've selected the tech stack and uploaded the metadata, click the "Generate Code" button.
   - The app will use the OpenAI API to generate the code for your chosen stack. The generated code will be displayed within the app.

5. **Download the Code**:
   - After reviewing the generated code, you can download it by clicking the "Download Generated Code" button. The code will be saved as a `.js` file, which you can use in your project.

---

## Example Workflow

1. **Upload**: Upload the `transaction_metadata.xlsx` file (or your own metadata file).
2. **Select Stack**: Choose a frontend (ReactJS), backend (NodeJS), and database (MySQL).
3. **Generate**: Click "Generate Code" to get a full-stack code template.
4. **Download**: Download the generated code and integrate it into your project.

---

## Sample Data: Transaction Excel File

The **transaction_metadata.xlsx** file contains metadata information that the app can process. Here's what the sample file looks like:

| Table Name  | Column Name        | Description                                                      |
|-------------|--------------------|------------------------------------------------------------------|
| transaction | Transaction_ID     | Unique identifier for each transaction.                          |
| transaction | Customer_Name      | Name of the customer involved in the trade.                      |
| transaction | Product_Code       | Code of the product being traded.                                |
| transaction | Trade_Value        | Total value of the trade in USD.                                 |
| transaction | Trade_Date         | Date of the trade.                                               |
| transaction | Country_Origin     | Country where the trade originated.                              |
| transaction | Payment_Term       | Payment terms agreed upon (e.g., Net 30).                        |
| transaction | Shipment_Method    | Method used for shipping the goods (e.g., Air, Sea).             |
| transaction | Transaction_Status | Status of the transaction (e.g., Completed, Pending).            |
| transaction | Currency_Used      | Currency used for the trade.                                     |

You can use this file to test the app's functionality by uploading it during the code generation process.

---

## Project Structure

```plaintext
MetaBuilder/
│
├── app.py                      # Main Streamlit app code
├── requirements.txt             # List of required dependencies
├── transaction_metadata.xlsx    # Sample metadata Excel file for testing
├── README.md                    # Project documentation (this file)
└── .gitignore                   # Files to be ignored by Git
```
---

## Known Issues

If you encounter issues with the OpenAI API, make sure:
- You are using version `0.28.0` of the OpenAI library.
- You have entered a valid OpenAI API key.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions or suggestions, please open an issue or contact me.

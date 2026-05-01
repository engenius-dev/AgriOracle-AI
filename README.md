# 🌱 AgriOracle-AI

> A precision agriculture decision engine utilizing Python and **Explainable AI (XAI)** to predict optimal crop selection based on soil and climate data. Built for the Jacob.ai challenge, it transforms complex environmental metrics into transparent, profitable recommendations for modern, sustainable farming.

---

## 🚀 Features

*   **High-Fidelity Predictive Modeling:** Utilizes a Random Forest Classifier trained on 7,000 diverse agricultural data points to ensure high accuracy.
*   **Explainable AI (XAI) Integration:** Bridges the gap between raw data and actionable intelligence. A Generative AI layer translates the mathematical outputs of the ML model into natural language, explaining *why* a crop is recommended based on specific environmental and market factors.
*   **Dynamic Interactive Dashboard:** Built with Streamlit to allow users (farmers, planners, or stakeholders) to adjust environmental parameters in real-time and instantly visualize outcomes.
*   **Hyper-Localized Inputs:** Makes decisions based on four critical environmental pillars: Temperature, Humidity, Soil pH, and Rainfall.

---

## 🛠️ Tech Stack

*   **Frontend / UI:** Streamlit
*   **Machine Learning Core:** Scikit-Learn (Random Forest)
*   **Explainable AI Engine:** Google Gemini (Generative AI)
*   **Data Processing:** Pandas, OpenPyXL
*   **Environment Management:** Python `dotenv`

---

## ⚙️ Local Setup & Installation

Follow these steps to run the decision engine on your local machine.

1. **Clone the Repository**
   ```sh
   git clone https://github.com/engenius-dev/AgriOracle-AI.git
   cd AgriOracle-AI

2. **Set Up the Virtual Environment**

   It is recommended to use a virtual environment to manage dependencies.

   ```sh
   python -m venv venv
   
   # On Windows:
   .\venv\Scripts\activate

   # On macOS/Linux:
   source venv/bin/activate

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt

4. **Configure Environment Variables**

   This project requires a Gemini API key for the Explainable AI features.

   1. Create a file named .env in the root directory.
   2. Add your API key in the following format (refer to .env.example):

   ```sh
   GEMINI_API_KEY=your_actual_api_key_here

5. **Train the Model & Launch**

   Before launching the app, ensure the ML model is compiled from the dataset.

   ```sh
   # Train the ML model (generates crop_model.pkl)
   python train_model.py

   # Launch the Streamlit dashboard
   streamlit run app.py

   The application will automatically open in your default web browser at http://localhost:8501

## 📂 Project Structure

1. **app.py:** The main Streamlit application and UI logic.
2. **train_model.py:** Script to process the dataset and train the Random Forest model.
3. **Crop Recommendation Dataset.xlsx:** The core dataset containing 7,000 environmental data points.
4. **requirements.txt:** Project dependencies.
5. **.env.example** Template for API key configuration.

---
*Built for the Jacob.ai 2027 YOP Placement Challenge.*
## Customer Churn Prediction System

This project outlines an end-to-end machine learning application designed to predict customer churn risk for a SaaS product. It leverages customer usage, engagement, and billing data to provide real-time predictions. 

---

### Application Functionality

The system offers the following core features:

*   **Customer Attribute Input:** Accepts customer-specific data through a user interface.
*   **Churn Probability Prediction:** Calculates the likelihood of a customer churning.
*   **Risk Classification:** Categorizes customers into **Low**, **Mild**, or **High** churn risk.
*   **Prediction Confidence Display:** Shows the confidence level of the generated predictions.

---

### Model Selection

Both Logistic Regression and Random Forest models were trained and fine-tuned using cross-validation.

**Random Forest** was ultimately selected as the final model due to its superior ability to capture nonlinear relationships in customer behavior and its higher overall performance on ROC-AUC. Despite being slightly more resource-intensive than linear models, its inference time remains sufficiently fast for a lightweight API.

---

### Technical Stack

The project utilizes a focused tech stack for efficiency and deployability:

*   **Scikit-learn**: For model training and development.
*   **FastAPI**: Powers the inference service, providing a robust API.
*   **HTML / CSS / JavaScript**: Used to build a minimal yet functional user interface.
*   **Joblib**: Employed for efficient model serialization and deserialization.

---

### Running Locally

To set up and run the application locally, follow these steps:

1.  **Create a virtual environment and install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Start the API service:**
    ```bash
    uvicorn api.main:app --reload
    ```

3.   **Access Swagger API documentation:**
    ```
    /docs
    ```


**Important Note:** The model was trained using `scikit-learn==1.6.1`. Using a different version may lead to model loading issues due to serialization incompatibilities. And change the `const RENDER_APP_URL = "https://churn-predictor-ful0.onrender.com"` in index.html to `const RENDER_APP_URL = "http://127.0.0.1"` while using in the local system.

---

### Project Structure

```
api/        → FastAPI backend
model/      → Serialized Random Forest pipeline
training/   → Jupyter notebook used for experimentation
index.html  → Interface for Web deployment
```

---

### Web Deployment

Open `https://skeswarsudhan.github.io/Churn_Predictor/` to check wen deployment.


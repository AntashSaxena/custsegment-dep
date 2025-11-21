# Customer Segmentation Application

This project is a customer segmentation application built using Python and Streamlit. It allows users to input customer details and predict customer segments using a pre-trained KMeans model.

## Project Structure

```
customer-segmentation-app
├── app
│   └── segmentation.py       # Main application logic using Streamlit
├── models
│   ├── kmeans_model.pkl      # Pre-trained KMeans model
│   └── scaler.pkl            # Scaler model for input data standardization
├── Dockerfile                 # Instructions to build the Docker image
├── requirements.txt           # Python dependencies
├── .dockerignore              # Files to ignore when building the Docker image
├── .gitignore                 # Files to ignore in Git
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd customer-segmentation-app
   ```

2. **Install dependencies:**
   You can install the required Python packages using pip:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   You can run the application locally using Streamlit:
   ```
   streamlit run app/segmentation.py
   ```

## Docker Instructions

To build and run the application using Docker, follow these steps:

1. **Build the Docker image:**
   ```
   docker build -t customer-segmentation-app .
   ```

2. **Run the Docker container:**
   ```
   docker run -p 8501:8501 customer-segmentation-app
   ```

3. **Access the application:**
   Open your web browser and go to `http://localhost:8501` to access the customer segmentation application.

## Usage

- Enter customer details such as age, income, total spending, number of web purchases, number of store purchases, number of web visits per month, and recency days since the last purchase.
- Click on the "Predict Segment" button to get the predicted customer segment.

## License

This project is licensed under the MIT License.
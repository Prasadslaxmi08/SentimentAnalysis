# SentimentAnalysis
Sentiment Analysis of review of famous movies
# Sentiment Analysis using Support Vector Machines (SVM)

This project demonstrates sentiment analysis using Support Vector Machines (SVM) on the IMDb movie reviews dataset. It predicts the sentiment of a given input text as either positive or negative.

## Requirements

To run the code in this repository, you need the following dependencies:

- Python 3.x
- pandas
- scikit-learn (sklearn)
- joblib
- streamlit

You can install these dependencies using the following command:
bash
pip install pandas scikit-learn joblib streamlit


## Dataset

The dataset used in this project is the IMDb movie reviews dataset. The dataset is loaded from the `datasetIMDB.csv` file, which contains two columns: 'text' for movie reviews and 'sentiment' for the corresponding sentiment labels ('positive' or 'negative').

## Getting Started

1. Clone this repository to your local machine.

2. Install the required dependencies as mentioned in the Requirements section.

3. Run the `sentiment_analysis.py` script to train the SVM model and set up a Streamlit web application.

## Running the Code

To train the SVM model and use the Streamlit web application, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the project directory.

3. Run the following command:
bash
streamlit run sentiment_analysis.py


4. A Streamlit web application will be launched in your browser.

5. Enter a text message in the provided text input.

6. Click on the 'Predict' button to see the sentiment prediction (either 'positive' or 'negative') for the input message.

7. The accuracy score of the model on the test data will also be displayed on the page.

## Saving and Loading the Model

The trained SVM model is saved using the `joblib` library and stored as 'sentiment_analysis.joblib'. The saved model can be loaded and used for prediction as shown in the code.

python
import joblib

# Load the model
model = joblib.load('sentiment_analysis.joblib')

# Use the model for prediction
op = model.predict([input_text])


## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The IMDb movie reviews dataset used in this project is available at [Kaggle](https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews).

- This project is inspired by various Sentiment Analysis tutorials and examples available online.

Feel free to contribute to this project by creating pull requests or reporting issues. Happy sentiment analyzing!

*Note*: Make sure to replace `<your_username>` in the repository URL with your actual GitHub username when uploading the code to your GitHub account.

Please let me know if you need any further assistance or have any other questions!

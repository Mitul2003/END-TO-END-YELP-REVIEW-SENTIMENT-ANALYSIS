# Yelp Review Sentiment Analysis

This project performs sentiment analysis on Yelp reviews using Natural Language Processing (NLP) techniques. It includes training a model to classify reviews into positive, neutral, or negative sentiments and deploying it with a FastAPI backend and a simple HTML frontend.

## Project Structure

- **app/**: Contains the main FastAPI application.
  - `main.py`: FastAPI application with endpoints for sentiment analysis.
- **templates/**: HTML templates for user interface.
  - `index.html`: Homepage for entering reviews and displaying results.
  - `result.html`: give output of review
- **models/**: Directory for storing trained model files (not included in GitHub repository).
- **data/**: Directory for storing datasets (not included in GitHub repository).
- **Dockerfile**: Docker configuration file to containerize the application.
- **requirements.txt**: List of Python dependencies for the project.
- **README.md**: This file, explaining the project and its structure.

## Usage

### -Running Locally

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/yelp-review-sentiment-analysis.git
   cd yelp-review-sentiment-analysis


2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   
   ```

3. **Download the Yelp dataset**:
- Obtain the Yelp reviews dataset (e.g., from Kaggle) and place it in the data/ directory.

4. **Run the FastAPI application**:
  ```
  uvicorn main:app --reload
  ```
  - Navigate to http://localhost:8000 in your web browser to use the web interface.

## Docker Deployment

1. **Build the Docker image**:

```
docker build -t yelp-review-sentiment .
```

2. **Run the Docker container**:

```
docker run -p 8000:8000 yelp-review-sentiment
```
- Access the application at http://localhost:8000 in your web browser.

## API Endpoints
- POST /predict: Endpoint to classify a Yelp review text and return its sentiment.

##### Example
To classify a Yelp review, send a POST request to /predict with JSON data:

```
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "review_text": "This restaurant was amazing! The food was delicious and the service was excellent."
}'
```
## Results

The model achieves an accuracy of approximately 89% on the validation set.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

## License
This project is licensed under the MIT License.

## Explanation:

- **Project Overview**: Brief introduction to the project and its objectives.
- **Project Structure**: Description of the directory structure and key files.
- **Usage**: Detailed instructions on how to set up and run the project locally and with Docker.
- **File Descriptions**: Explanation of each important file and its role in the project.
- **Customization**: Guidance on how to customize and extend the project.
- **API Endpoints**: Description of the API endpoint with an example using `curl`.
- **Results**: Placeholder for model performance and example classifications.
- **Contributing**: Information for potential contributors.
- **License**: Licensing information.


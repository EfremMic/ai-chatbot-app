# AI Chatbot Application with Google OAuth

This is a Flask-based AI chatbot application that integrates with OpenAI's GPT-3.5 API. It includes Google OAuth for user authentication and is designed to be deployed on Heroku. The chatbot can handle user inputs and generate responses using the GPT-3.5 model.

## Features

- **AI Chatbot**: Leverages OpenAI's GPT-3.5 API for generating responses to user queries.
- **Google OAuth**: Secure login using Google OAuth 2.0.
- **Asynchronous Requests**: Non-blocking API requests for faster responses.
- **Heroku Deployment**: Ready to be deployed on Heroku with minimal setup.
- **Environment-based Configuration**: All sensitive information is stored in environment variables using a `.env` file.

## Prerequisites

- **Python 3.7+**
- **Heroku CLI** (for deployment)
- **OpenAI API Key**
- **Google OAuth Client ID & Secret**

## Getting Started

Follow these steps to get the project up and running locally or on Heroku.

### 1. Clone the repository

```bash
git clone https://github.com//EfremMic/ai-chatbot-app.git
cd ai-chatbot-app
```

### 2. Set up a virtual environment

It's recommended to use a virtual environment to manage your dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate a `SECRET_KEY`

Run the provided script to generate a `SECRET_KEY` for your Flask application:

```bash
python generate_secret_key.py
```

This will append a `SECRET_KEY` to your `.env` file. The `.env` file stores sensitive information and should **never** be pushed to version control.

### 5. Set up environment variables

Create a `.env` file in the project root with the following content:

```bash
# .env
SECRET_KEY=your_generated_secret_key
OPENAI_API_KEY=your_openai_api_key
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
```

### 6. Run the application locally

```bash
flask run
```

You can now access the application at `http://127.0.0.1:5000/`.

### 7. Deploy to Heroku

If you want to deploy the app to Heroku, follow these steps:

#### 7.1. Create a Heroku app

```bash
heroku create your-app-name
```

#### 7.2. Set environment variables on Heroku

Set your environment variables on Heroku:

```bash
heroku config:set SECRET_KEY=your_secret_key
heroku config:set OPENAI_API_KEY=your_openai_api_key
heroku config:set GOOGLE_CLIENT_ID=your_google_client_id
heroku config:set GOOGLE_CLIENT_SECRET=your_google_client_secret
```

#### 7.3. Push the code to Heroku

```bash
git add .
git commit -m "Initial commit"
git push heroku master
```

#### 7.4. Open the app

```bash
heroku open
```

Your application should now be live on Heroku!

## Project Structure

## Technologies Used

- **Flask**: A micro-framework for Python web development.
- **OpenAI API**: For generating AI-based responses.
- **Authlib**: For integrating Google OAuth 2.0.
- **Gunicorn**: A production-grade WSGI server for serving the Flask app on Heroku.

## License

This project is licensed under the MIT License - see https://github.com/EfremMic/ai-chatbot-app/blob/main/LICENSE for details.

## Contributing

Feel free to submit issues or pull requests to enhance the application. Contributions are welcome!

---

## Troubleshooting

If you run into issues, here are a few steps you can take:

- Make sure your `.env` file contains the correct keys.
- Check that you have set up Google OAuth correctly by creating OAuth credentials in your Google Cloud Console.
- For deployment issues, ensure that you have the correct environment variables set up on Heroku using the `heroku config` command.

---

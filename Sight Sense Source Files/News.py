import requests
import pyttsx3

# Function to fetch news headlines from News API
def get_news():
    # Replace 'YOUR_API_KEY' with your actual News API key
    api_key = '12fa853930eb4491877e907e5cc76a2c'
    url = f'http://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    
    try:
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'ok':
            articles = data['articles']
            headlines = [article['title'] for article in articles]
            return headlines
        else:
            print("Failed to fetch news:", data['message'])
            return []
    except Exception as e:
        print("Error fetching news:", e)
        return []

# Function to speak out the news headlines
def speak_news(headlines):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust the speaking rate
    engine.setProperty('volume', 0.9)  # Adjust the speaking volume
    engine.say("Here are the top news headlines for today:")
    for headline in headlines:
        engine.say(headline)
    engine.runAndWait()

# Main function
if __name__ == "__main__":
    headlines = get_news()
    if headlines:
        speak_news(headlines)
    else:
        print("No news available.")

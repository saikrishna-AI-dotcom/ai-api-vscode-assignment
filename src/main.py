from utils import format_topic, get_sample_topics
from api_client import fetch_post

def main():
  print("Welcome to the AI Learning App!")
  print("-" * 50)

  topics = get_sample_topics()
  print('Topics in the Project:')

  for topic in topics:
    print(format_topic(topic))

  print('Making a small API call')
  result= fetch_post()
  
  print('API Response:')
  print(result)

if __name__=="__main__":
   main()
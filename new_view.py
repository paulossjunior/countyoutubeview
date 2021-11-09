#https://www.thepythoncode.com/article/get-youtube-data-python
from requests_html import HTMLSession 
from bs4 import BeautifulSoup as bs # importing BeautifulSoup


videos = ["https://www.youtube.com/watch?v=tkvJQ5x-eEY&list=PLq1I6GEIwH6fdea1RoWbPwME0Bzjt8pnH",
          "https://www.youtube.com/watch?v=OKMoxMSCFng",
          "https://www.youtube.com/watch?v=GgWQFLble_I",
          "https://www.youtube.com/watch?v=RNHrIirvYow",
          "https://www.youtube.com/watch?v=jD92I5jHs9U",
          "https://www.youtube.com/watch?v=70BBCSy1cL4",
          "https://www.youtube.com/watch?v=3qxCcZmctqI",
          "https://www.youtube.com/watch?v=39ExyhtP6no&feature=youtu.be"]

# init an HTML Session
session = HTMLSession()
print ("Iniciando a busca")
for video_url in videos:
	
	# get the html content
	response = session.get(video_url)
	# execute Java-script
	response.html.render(sleep=2, timeout=60)
	# create bs object to parse HTML
	soup = bs(response.html.html, "html.parser")
	result = {}
	result["title"] = soup.find("meta", itemprop="name")['content']
	result["views"] = 0
 	
	interaction = soup.find("meta", itemprop="interactionCount")
	if  interaction:
		result["views"] = interaction['content']
	
	print (result['title']+" : "+result['views']+ " views")
 
print ("Fim")
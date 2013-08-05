import httplib2
import json
from .model import Article, Comment
from sqlalchemy.exc import IntegrityError
import traceback
from extensions import db
topics=[
'changemyview',
'debate',
'debateachristian',
'atheism',
'sustainability',
'climate',
'PoliticalDiscussion',
'debatefascism',
'debateacommunist',
'corporatism',
'fascism',
'gunsarecool',
'gunpolitics',
'progun',
'liberal',
'progressive',
'newright',
'occupywallstreet',
'politics',
'ask_politics'
]

users=[
'Decamun'
]
def extract_reddit_from_url(url,after=None):
	h = httplib2.Http(".cache")
	formed_url = url
	if after:
		formed_url = "%s?after=%s"%(url,after)
	print "processing url: %s"%formed_url
	resp, content = h.request(formed_url, "GET")
	print "response: %s"%resp
	if resp['status'] in ['200','304']:
		content = json.loads(content)
		reddits = content['data']['children']
		for reddit in reddits:
			article = Article()
			print "saving reddit of kind: %s"%reddit['kind']
			article.kind = reddit['kind']
			article.id = reddit['data']['id']
			if "permalink" in reddit['data']:
				comment_url = "http://reddit.com%s.json"%reddit['data']['permalink']
			else:
				comment_url = "http://reddit.com/r/%s/comments/%s/.json"%(reddit['data']['subreddit'],(reddit['data']['link_id']).split('_')[1])
			article.data = json.dumps(reddit['data'])
			try:
				article.save()
				db.session.commit()
				getcomments(comment_url,article.id)
			except IntegrityError:
				db.session.rollback()
				print "reddit already exists"
		if content['data']['after']:
			extract_reddit_from_url(url,content['data']['after'])
	else:
		print "malfuctioning url"

def get_reddits():
	for topic in topics:
		url = "http://reddit.com/r/%s/.json"%topic
		extract_reddit_from_url(url)

def getcomments(url,id):
	h = httplib2.Http(".cache")
	print "processing comments url: %s"%url
	resp, content = h.request(url, "GET")
	if resp['status'] in ['200','304']:
		content = json.loads(content)
		if len(content) > 1:
			comments = content[1]['data']['children']
			for comment in comments:
				_comment = Comment()
				_comment.id = comment['data']['id']+"_"+id
				_comment.kind = comment['kind']
				_comment.data = json.dumps(comment['data'])
				_comment.reddit_id = id
				try:
					_comment.save()
					db.session.commit()
				except IntegrityError:
					# print traceback.format_exc()
					db.session.rollback()
					print "comment already exists"

	

def get_reddits_of_user():
	for user in users:
		url = "http://www.reddit.com/user/%s/.json"%user
		extract_reddit_from_url(url)


	
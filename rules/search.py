import random
import requests
from .rule import Rule

class SearchRule(Rule):
    def match_expr(self):
        return (
            r'我?[要想](找|問|知道)(關於|什麼是)?(?P<keyword>\S+)(是什麼)?',
        )

    def run(self, message, keyword, **kwargs):
        try:
            response = requests.get('https://www.jrf.org.tw/api/articles', params={'query': keyword}).json()
            if response['status'] != 'success' or response['count'] < 1:
                return '嗚呃，找不到你要問什麼！你可以試試看對我說「我要問{}」～'.format(random.choice([
                    '司法改革', '大法官', '冤獄平反', '邱和順', '徐自強', '蘇建和', '司法陽光', '檢察官', '麵包'
                ]))
            else:
                article = random.choice(response['articles'])
                author, _, occupation = article.get('author', '秘密人物').replace('文／', '').partition('／')
                url = 'https://www.jrf.org.tw/articles/{}'.format(article['id'])
                text = '推薦一篇好文章〈{}〉，是由{}{}主筆的哦！\n{}'.format(article['title'], occupation, author, url)
                result = {
                    "text": text,
                    "attachment": {
                          "type": "template",
                          "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": article['title'],
                                    "item_url": url,
                                    "buttons": [
                                    {
                                        "type":"web_url",
                                        "url": url,
                                        "title":"看文章"
                                    }]
                                }
                            ]
                        }
                    }
                }
                if article['image']:
                    result["attachment"]["payload"]["elements"][0]["image_url"] = article['image']
            return result
        except:
            return '嗚呃，網站在維修！'

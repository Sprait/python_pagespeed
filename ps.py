
import requests
import json
import fire
from config import api_key
from pprint import pprint

'''
25,000 requests / day.
1,000 requests per 100 seconds.
60 requests per 100 seconds.
'''




class PageSpeed():
    '''
    Return pagespeed score for your site.
    Default returned perfomance score.

    Example:
    ~/python ps.py --url=http://mysite.ru [performance|accessibility|best-practices|pwa|seo]
    ~/python ps.py --url=http://mysite.ru
    ~/python ps.py --url=http://mysite.ru seo
    
    :param url(str): the url of the site
    '''
    def __init__(self, url, api_key=api_key):
        self.site = url
        self.api_key = api_key
        self.pd_url = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&fields=lighthouseResult&strategy=desktop&category=performance&category=pwa&category=best-practices&category=accessibility&category=seo&key={self.api_key}'
        self._data = {}
        self.analyse()


    def analyse(self):
        json_data = requests.get(self.pd_url).json()
        for category in json_data['lighthouseResult']['categories']:
            self._data[category] = str(round(json_data['lighthouseResult']['categories'][category]['score']*100))
    
    @property
    def performance(self):
        return self._data['performance']
    
    @property
    def accessibility(self):
        return self._data['accessibility']
    
    @property
    def best_practices(self):
        return self._data['best-practices']
    
    @property
    def pwa(self):
        return self._data['pwa']
    
    @property
    def seo(self):
        return self._data['seo']
        
    def __str__(self):
        return f"""
        performance: {self._data['performance']} 
        accessibility: {self._data['accessibility']}
        best-practices: {self._data['best-practices']}
        pwa: {self._data['pwa']}
        seo: {self._data['seo']}
        """
    
def main():
    fire.Fire(PageSpeed)

if __name__ == '__main__':
    main()   


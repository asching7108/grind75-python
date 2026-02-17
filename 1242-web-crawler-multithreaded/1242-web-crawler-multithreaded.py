# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock


class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = '/'.join(startUrl.split('/', 3)[:3])
        seen = set([startUrl])
        lock = Lock()

        def process(url):
            result = []

            for u in htmlParser.getUrls(url):
                if not u.startswith(hostname):
                    continue

                with lock:
                    if u in seen:
                        continue
                    seen.add(u)
                result.append(u)

            return result

        with ThreadPoolExecutor(max_workers=16) as executor:
            futures = {executor.submit(process, startUrl)}

            while futures:
                for future in as_completed(futures):
                    futures.remove(future)
                    for url in future.result():
                        futures.add(executor.submit(process, url))

        return list(seen)

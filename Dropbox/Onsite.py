import threading
import queue

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        ret = set()
        ret_lock = threading.Lock()
        
        q = queue.Queue()
        
        ret.add(startUrl)
        
        hostname = startUrl.split('/')[2]
        
        def worker():
            while True:
                p = q.get()
                
                urls = htmlParser.getUrls(p)
                for url in urls:
                    if url.split('/')[2] == hostname:
                        with ret_lock:
                            if url not in ret:
                                ret.add(url)
                                q.put(url)
                
                q.task_done()
                
        for _ in range(4):
            threading.Thread(target=worker, daemon=True).start()
            
        q.put(startUrl)
        q.join()
        
        return list(ret)

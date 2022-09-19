from django.shortcuts import render
from googlesearch import search
from usp.tree import sitemap_tree_for_homepage
import threading


class ThreadResult(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None):
        def function():
            self.result = target(*args, **kwargs)

        super().__init__(group=group, target=function, name=name, daemon=daemon)


def index(request):
    return render(request, 'index.html')


def search_(request):
    """
        we are first searching keyword from google and getting all the domains with the keyword user searched.
        Then we are just filtering all the links of each domain and searching for contact and contact us pages.
    """
    thread = ThreadResult(target=find_links, args=(request.GET.get("keyword"), 3))
    thread.start()
    thread.join()
    return render(request, 'index.html', context={"links": thread.result})


def find_links(keyword, pages):
    all_domains = []
    for s in search(keyword, num_results=int(pages), lang='en'):
        all_domains.append(s)
    links = []

    print("Going to find contact page for these search websites")
    print(all_domains)

    for domain in all_domains:
        tree = sitemap_tree_for_homepage(domain)
        """
            we will search contact and contact us page keyword from url
        """
        for page in tree.all_pages():
            if 'contact' in page.url:
                links.append(page.url)
                print("CONTACT PAGE ADDED")
                print(page.url)
                break

    return links

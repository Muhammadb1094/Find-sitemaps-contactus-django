from usp.tree import sitemap_tree_for_homepage

tree = sitemap_tree_for_homepage('https://arcticplumbingandheating.com/')

for page in tree.all_pages():
    print(page.url)


# query = "plumbers in alaska"
# from googlesearch import search
# data = search("plumbers in alaska", num_results=100, lang="en")
# print(data)
# for j in search(query, num_results=10, lang='en'):
#     print(j)


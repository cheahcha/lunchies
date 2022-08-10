from bs4 import BeautifulSoup
import requests


def main():
    base_url = 'https://danielfooddiary.com/category/food/'
    res = requests.get(base_url)
    soup = BeautifulSoup(res.content, 'html5lib')
    page_string = soup.find('a', attrs={'class': 'last'})
    num_pages = int(page_string.contents[0])

    for i in range(num_pages):
        url = base_url + 'page/' + str(i)
        links = extract_page_links(url)
        print(links)
        for link in links:
            try:
                extract_food_and_location(link)
            except:
                print("Error in " + link)


def extract_food_and_location(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html5lib')
    post_body = soup.find_all('strong')

    print(list(filter(lambda x: x.find('br'), post_body)))


def filter_by_break(item):
    return item.find('br') is not None


def extract_page_links(url):
    links = []
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html5lib')
    for row in soup.findAll('div', attrs={'class': 'td-block-span6'}):
        link = row.a['href']
        links.append(link)

    return links


if __name__ == '__main__':
    main()

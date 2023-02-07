# Name: Md Toufique Hasan
# Email: hasan.mdtoufique@gmail.com
####################################

import sys
from urllib.parse import urlsplit
import requests
from bs4 import BeautifulSoup


def extract_url_parts(url):
    url_parts = urlsplit(url)
    tld = url_parts.hostname.split(".")[-1]
    domain = ".".join(url_parts.hostname.split(".")[-2:])
    hostname = url_parts.hostname
    path = url_parts.path
    return tld, domain, hostname, path


def extract_links(url):
    same_hostname = []
    same_domain = []
    different_domain = []
    tld, domain, hostname, path = extract_url_parts(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.find_all("a")
    for link in links:
        link_url = link.get("href")
        link_tld, link_domain, link_hostname, link_path = extract_url_parts(link_url)
        if link_hostname == hostname:
            same_hostname.append(link_url)
        elif link_domain == domain:
            same_domain.append(link_url)
        else:
            different_domain.append(link_url)
    return same_hostname, same_domain, different_domain


def main(url):
    tld, domain, hostname, path = extract_url_parts(url)
    print("TLD:", tld)
    print("DOMAIN:", domain)
    print("HOSTNAME:", hostname)
    print("PATH:", path)
    same_hostname, same_domain, different_domain = extract_links(url)
    print("LINKS:")
    print("Same hostname:")
    for link in same_hostname:
        print(link)
    print("Same domain:")
    for link in same_domain:
        print(link)
    print("Different domain:")
    for link in different_domain:
        print(link)


if __name__ == "__main__":
    url = sys.argv[1]
    main(url)

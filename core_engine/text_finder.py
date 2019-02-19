from bs4 import BeautifulSoup as bs
import time


def read_url(soup, count=0):
    if count>3:
        print('\033[1;31;40m Too many tries \033[0m', end=' ')
        return ''
    tags = soup.find_all('p')
    if not tags:
        print('\033[1;31;40m Can\'t read text \033[0m', end=' ')
        count += 1
        return read_url(soup, count)
    text = bs(str(tags), 'html.parser').text
    return text


# with open("links1.txt", 'r') as file:
#     urls = file.read().split('\n')
# print('Writing', end='')
# with open("test.txt", 'a') as file:
#     for i in range(len(urls)):
#         file.write(read_url(urls[i]))
#         print('.', end='')


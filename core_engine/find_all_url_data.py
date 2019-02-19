import sys
from bs4 import BeautifulSoup
import requests
from text_finder import read_url
import time
import sys

sys.setrecursionlimit(100000)


def get_all_data_from_url(url, links=[], count=0):
    try:
        """Handle multiple repeating of exception"""
        print("Link...", end=' ')
        if count > 20:
            return 0
        """Reading html page and extract tags with texts"""
        response = requests.get(url).text
        soup = BeautifulSoup(response, 'html.parser')
        th_tags = soup.find_all('th')

        """Check whether list of texts is empty and handle error 503"""
        if not th_tags:
            print('\033[1;31;40m Empty list. Wait a bit... \033[0m', end=' ')
            time.sleep(2)
            count += 1
            return get_all_data_from_url(url, links, count)

        """Search for text and add it into a file"""
        with open("training_data.txt", 'ab') as file:
            print('Read text', end=' ')
            file.write(read_url(soup).encode('cp1251', errors='ignore'))
            print("\033[1;33;40m Text was added \033[0m  ", end=' ')

        find_new_url(th_tags, links)

    except UnicodeEncodeError as e:
        print("Exception {} is occurred!".format(e))
        print(th_tags[-1])
        find_new_url(th_tags, links)
    except Exception as e:
        print("Exception \'{0}\' at line {1} is occurred!".format(e, sys.exc_info()[-1].tb_lineno))
    finally:
        return 0


def find_new_url(th_tags, links):
        """Search for tag that points to next page. If absent - break since it was the last one."""
        if str(th_tags[-1]['class'])[2:-2] == 'pagenav_next':
            a = th_tags[-1].find('a')
        else:
            print("Book is finished")
            time.sleep(5)
            return 0

        """Make a list with urls"""
        new_url = a.get('href')
        if new_url not in links:
            links.append(new_url)
            print('New link', end=' ')

        """Add every 10 links into a file"""
        if len(links) % 10 == 0:
            with open("links.txt", 'a') as file:
                file.write('\n'.join(links[-1:-11:-1]))
                file.write('\n')
                print('\n', '-'*150, '\nIt was added {} links!\n'.format(len(links)), '-'*150, '\n')
        print("\033[1;34;40m Finish \033[0m  \n ", '-' * 150)

        get_all_data_from_url(new_url, links)


print('Loading', end='')
books = 0
start = time.time()
blogUrl = 'https://pidruchniki.com/81900/menedzhment/upravlinnya_lyudskimi_resursami'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/158407207846/menedzhment/upravlinnya_lyudskimi_resursami'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/1584072033571/menedzhment/situatsiyniy_menedzhment'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/82005/menedzhment/rozvitok_personalu'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/1584072032566/menedzhment/priynyattya_upravlinskih_rishen'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/2015082666224/menedzhment/ofisniy_menedzhment'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/1410072650947/menedzhment/osnovi_menedzhmentu'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/15281113/menedzhment/organizatsiya_pratsi_menedzhera'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/1990042141958/menedzhment/organizatsiya_biznesu'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/10760803/menedzhment/operatsiyniy_menedzhment'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/1554042253489/menedzhment/operatsiyniy_menedzhment'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/1048030461712/menedzhment/menedzhment_fermerskih_gospodarstv'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/19640805/menedzhment/menedzhment_u_sferi_poslug'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/1584072016050/menedzhment/menedzhment_pidpriyemstva'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/1584072016751/menedzhment/menedzhment_personalu'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/67898/menedzhment/menedzhment_organizatsiy'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/86515/menedzhment/menedzhment_vischoyi_osviti'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/19991130/menedzhment/menedzhment'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/12861203/menedzhment/liderstvo_ta_stil_roboti_menedzhera'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/19871030/menedzhment/kultura_dilovogo_spilkuvannya_menedzhera'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/1584072028851/menedzhment/korporativne_upravlinnya'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/1045011752401/menedzhment/korporativne_upravlinnya'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/2015080265798/menedzhment/komunikativna_pidgotovka_spivrobitnikiv_pravoohoronnih_organiv'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/1584072019034/menedzhment/innovatsiyniy_menedzhment'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/19991130/menedzhment/etika_dilovogo_spilkuvannya'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/1584072025747/menedzhment/dilova_karyera'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/88196/menedzhment/diagnostika_v_sistemi_upravlinnya'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/2015060964853/menedzhment/virobnichiy_menedzhment'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/1800022461253/menedzhment/antikrizoviy_menedzhment'
get_all_data_from_url(blogUrl)
books+=1
blogUrl = 'https://pidruchniki.com/91602/menedzhment/upravlinnya_trudovim_potentsialom'
get_all_data_from_url(blogUrl)
books+=1

end = time.time()
print('{0} books were copied for {1} minutes'.format(books, (end-start)/60))


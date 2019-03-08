import requests
import subprocess

def ping(host):
    status, result = subprocess.getstatusoutput("ping -n 1 " + host)
    result_string = [res for res in result.split('\n')[:6] if res != '']
    print(result_string)


def ping_requests(host):
    r = requests.get(host)
    if r.status_code == 200:
        print('Success connection')
    else:
        print('Resource not response')


if __name__ == '__main__':
    ping_requests('https://www.yandex.ru')
    ping_requests('https://www.youtube.com')

    ping('www.yandex.ru')
    ping('www.youtube.com')
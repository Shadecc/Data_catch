# coding=gbk
import io
import requests
from bs4 import BeautifulSoup
import sys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030') #�ı��׼�����Ĭ�ϱ���
browser = webdriver.Firefox()
wait = WebDriverWait(browser, 10)


def get_total_page():
    url = 'http://www.fairso.com/43/28224/'
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html')
    dd = soup.find_all('dd')
    #  browser.close()
    pages = len(dd)
    return pages


def index_page(i):
    """
    ���س�С˵��ÿһ������
    :param i: С˵�ĵ� i ��
    """
    if i == 1:
        # С˵��һ�µ� Url ��ַ
        url = "http://www.fairso.com/28/28224/19087870.html"
        browser.get(url)
    # �ȴ� Content �ڵ���س���
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content')))
    # ���� get_info() ������ҳ����н���
    get_info()
    # Ѱ����һ�µ���Ľڵ�
    next_p = browser.find_elements(By.XPATH, ('//div[@class="bottem2"]/a'))[
        2]  # //*[@id="wrapper"]/div[4]/div/div[6]/a[3]
    # �ҵ���ͣ�� 30 ��
    time.sleep(4)
    # �����ť
    next_p.click()


def main():
    """
    ����С˵ȫ���½�
    :return:
    """
    total_page = get_total_page()
    print(total_page)
    for i in range(1, total_page + 1):
        index_page(i)


def get_info():
    """
    ��ȡÿһ��С˵�����½���������
    #wrapper > div.content_read > div > div.bookname > h1
    :return:
    """
    # �ҵ��½ڵ�����
    name = browser.find_element_by_css_selector('#wrapper > div.content_read > div > div.bookname > h1').text
    print(name)
    # �ҵ�С˵����
    content = browser.find_element_by_id('content').text
    print(content)
    # ���õ���С˵���Ͷ�Ӧ����������д�� txt �ļ���
    with open('1234.txt', 'a', encoding="utf-8") as f:
        # '\n'.join([name, content]) ת��Ϊ�ַ���
        f.write('\n'.join([name, content]))
        # ������
        f.write('\n\n')


if __name__ == '__main__':
    main()
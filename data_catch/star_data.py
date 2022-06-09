# coding=gbk
import io
import sys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030') #�ı��׼�����Ĭ�ϱ���
browser = webdriver.Firefox()
wait = WebDriverWait(browser, 10)


def index_page(i):
    """
    ����ÿһҳ����
    :param i: ҳ��ĵ� i ҳ
    """
    if i == 1:
        url = "http://star.iecity.com/all/0"
        browser.get(url)
        print('��', i, 'ҳ')
    # �ȴ� Main �ڵ���س���
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#Main')))

    # ���� get_info() ������ҳ����н���
    get_info()
    # Ѱ����һҳ����Ľڵ�
    next_p = browser.find_element(By.XPATH, ('//*[@id="Main"]/div[4]/div/span[12]'))
    # //*[@id="wrapper"]/div[4]/div/div[6]/a[3]
    # �ҵ���ͣ�� 30 ��
    time.sleep(4)
    # �����ť
    next_p.click()


def main():
    """
    ����ҳ��
    :return:
    """
    for i in range(1, 2):
        index_page(i)


def get_info():
    """
    ��ȡÿҳ����
    #
    :return:
    """
    # �ҵ��½ڵ�����
    content = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[4]/ul').text
    print(content)
    # ���õ�������д�� txt �ļ���
    with open('111.txt', 'a', encoding="utf-8") as f:
        # '\n'.join([name, content]) ת��Ϊ�ַ���
        f.write('\n'.join([content, content]))
        # ������
        f.write('\n\n')


if __name__ == '__main__':
    main()
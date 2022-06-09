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

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030') #改变标准输出的默认编码
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
    加载出小说的每一章内容
    :param i: 小说的第 i 章
    """
    if i == 1:
        # 小说第一章的 Url 地址
        url = "http://www.fairso.com/28/28224/19087870.html"
        browser.get(url)
    # 等待 Content 节点加载出来
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content')))
    # 调用 get_info() 方法对页面进行解析
    get_info()
    # 寻找下一章点击的节点
    next_p = browser.find_elements(By.XPATH, ('//div[@class="bottem2"]/a'))[
        2]  # //*[@id="wrapper"]/div[4]/div/div[6]/a[3]
    # 找到后停顿 30 秒
    time.sleep(4)
    # 点击按钮
    next_p.click()


def main():
    """
    遍历小说全部章节
    :return:
    """
    total_page = get_total_page()
    print(total_page)
    for i in range(1, total_page + 1):
        index_page(i)


def get_info():
    """
    提取每一章小说的章章节名及正文
    #wrapper > div.content_read > div > div.bookname > h1
    :return:
    """
    # 找到章节的名字
    name = browser.find_element_by_css_selector('#wrapper > div.content_read > div > div.bookname > h1').text
    print(name)
    # 找到小说正文
    content = browser.find_element_by_id('content').text
    print(content)
    # 将拿到的小说名和对应的正文内容写入 txt 文件中
    with open('1234.txt', 'a', encoding="utf-8") as f:
        # '\n'.join([name, content]) 转化为字符串
        f.write('\n'.join([name, content]))
        # 换两行
        f.write('\n\n')


if __name__ == '__main__':
    main()
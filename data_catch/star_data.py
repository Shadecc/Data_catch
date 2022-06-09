# coding=gbk
import io
import sys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030') #改变标准输出的默认编码
browser = webdriver.Firefox()
wait = WebDriverWait(browser, 10)


def index_page(i):
    """
    加载每一页内容
    :param i: 页面的第 i 页
    """
    if i == 1:
        url = "http://star.iecity.com/all/0"
        browser.get(url)
        print('第', i, '页')
    # 等待 Main 节点加载出来
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#Main')))

    # 调用 get_info() 方法对页面进行解析
    get_info()
    # 寻找下一页点击的节点
    next_p = browser.find_element(By.XPATH, ('//*[@id="Main"]/div[4]/div/span[12]'))
    # //*[@id="wrapper"]/div[4]/div/div[6]/a[3]
    # 找到后停顿 30 秒
    time.sleep(4)
    # 点击按钮
    next_p.click()


def main():
    """
    遍历页数
    :return:
    """
    for i in range(1, 2):
        index_page(i)


def get_info():
    """
    提取每页正文
    #
    :return:
    """
    # 找到章节的名字
    content = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[4]/ul').text
    print(content)
    # 将拿到的内容写入 txt 文件中
    with open('111.txt', 'a', encoding="utf-8") as f:
        # '\n'.join([name, content]) 转化为字符串
        f.write('\n'.join([content, content]))
        # 换两行
        f.write('\n\n')


if __name__ == '__main__':
    main()
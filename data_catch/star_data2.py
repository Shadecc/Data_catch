# coding=gbk
import io
import sys
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# aim_row行，aim_col列
aim_col = 2
aim_row = 1
file_name = 'data.xlsx'
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

    # 等待 Main 节点加载出来
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#Main')))

    # 调用 get_info() 方法对页面进行解析
    get_info()
    # 寻找下一页点击的节点
    next_p = browser.find_element(By.XPATH, ('//*[@id="Main"]/div[4]/div/span[12]'))
    # 找到后停顿 30 秒
    time.sleep(4)
    # 点击按钮
    next_p.click()


def main():
    """
    遍历页数
    :return:
    """
    for i in range(1, 354):
        index_page(i)


def get_info():
    """
    提取每页正文
    #
    :return:
    """
    # 找到章节的名字
    content = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[4]/ul')
    li_list = content.find_elements_by_tag_name('li')
    global aim_row
    for li in li_list:
        li_content = li.text
        aim_row += 1
        # 根据实际aim_row行，aim_col列修改数据即可
        # 加载已存在的wookbook对象
        wb = load_workbook(file_name)
        wb1 = wb.active  # 激活sheet
        # 往sheet中写入数据
        wb1.cell(aim_row, 1, aim_row-1)
        wb1.cell(aim_row, aim_col, li_content)
        # 保存
        wb.save(file_name)


if __name__ == '__main__':
    main()
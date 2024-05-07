from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas

# 初始化Chrome Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
# 打开网页


def get_rearch_page_info(page_element):
    # 抓取页面上的信息
    # 获取research组
    ul_element = page_element.find_element(By.XPATH, '//*[@id="research-index"]/div/div[3]/form/div[3]/ul')
    # 获取每条research数据
    li_elements = ul_element.find_elements(By.TAG_NAME, 'li')
    rearch_infos = []
    for li in li_elements:
        date = li.find_element(By.XPATH, "div[2]/div[1]/span[1]").text
        title = li.find_element(By.XPATH, "div[2]/div[2]/a/span/span").text
        openai_link = li.find_element(By.XPATH, "div[2]/div[2]/a").get_attribute('href')
        catergorys = []
        for catergory_ele in li.find_elements(By.XPATH, "div[2]/div[3]/div/span/a"):
            catergorys.append(catergory_ele.text)
        
        pdf_elements = li.find_elements(By.XPATH, "div[2]/div[3]/a")
        
        pdf_link = ""
        if pdf_elements:
            pdf_link = pdf_elements[0].get_attribute('href')
        rearch_infos.append([date, title, openai_link, catergorys, pdf_link])
    return rearch_infos



if __name__ == "__main__":
    
    all_public_research = []
    for i in range(1, 10):
        driver.get(f"https://openai.com/research?page={i}")
        # 页面等待，确保内容加载完成
        driver.implicitly_wait(5)
        research_infos = get_rearch_page_info(driver)
        all_public_research.extend(research_infos)
    
    # 关闭浏览器
    driver.quit()

    pandas.DataFrame(all_public_research).to_excel("openai_research.xlsx")
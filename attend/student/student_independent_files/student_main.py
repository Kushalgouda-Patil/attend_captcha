import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

def main(usn,dd,mm,yyyy):
    options = webdriver.ChromeOptions()
    headers = {
    "Host": "student.kletech.ac.in",
    "User-Agent": "PostmanRuntime/7.362",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
    }
    headers_str = ""
    for key, value in headers.items():
        headers_str += f"{key}: {value}\n"
    options.add_argument("--disable-blink-features=HeadersOverride")
    options.add_argument(f"--user-agent={headers['User-Agent']}")
    # options.add_argument(f"--host-rules={headers['Host']}=127.0.0.1")
    options.add_argument(f"--user-data-dir={headers_str}")
    options.add_argument("--start-maximized") 
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    try:
        # driver = webdriver.Chrome()
        url="https://student.kletech.ac.in/"
        driver.get(url)
        print("driver got url")
        iframe_id = "ifrm"
        wait = WebDriverWait(driver, 10)
        iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, iframe_id)))
        usn_element = wait.until(EC.presence_of_element_located((By.ID, "username")))
        dd_element = wait.until(EC.presence_of_element_located((By.ID, "dd")))
        mm_element = wait.until(EC.presence_of_element_located((By.ID, "mm")))
        yyyy_element = wait.until(EC.presence_of_element_located((By.ID, "yyyy")))
        usn_element.send_keys(usn)
        dd_element.send_keys(dd)
        mm_element.send_keys(mm)
        yyyy_element.send_keys(yyyy)
        submit_button = wait.until(EC.element_to_be_clickable((By.NAME, "submit")))
        submit_button.click()
        
        driver.get("https://student.kletech.ac.in/odd2023/index.php?option=com_studentdashboard&controller=studentdashboard&task=dashboard")
        soup=BeautifulSoup(driver.page_source,features="html.parser")
        name=soup.find_all('div',class_="tname2")[0].text.strip()
        semester=soup.find_all('div',class_="tname2")[2].text.strip().split()[1]
        courses=soup.find_all('div',class_="coursename")
        attendence=soup.find_all('a',title="Attendence")
        marks=soup.find_all('div',class_='cie')
        print(name,semester)
        marks_list=list()
        course_list=list()
        attendence_list=list()
        for i in range(len(courses)):
            course_list.append(courses[i].text)
            attendence_list.append(attendence[i*2].text)
            marks_list.append(marks[i].text.strip('\nInternal Assessment'))
        # df=pd.DataFrame({'Course':course_list,'Attendence':attendence_list,'Marks':marks_list})
        # df.to_json(f'{usn}.json')
        # print(df)
        dict_val={
            'Name':name,
            'Sem':semester,
            'Course':course_list,
            'Attendence':attendence_list,
            'Marks':marks_list
        }

        # element = driver.find_element(By.XPATH, '//a[contains(@href, "javascript:document.log.submit()")]')
        driver.execute_script('javascript:document.log.submit()')
        
        driver.quit()
        return dict_val
    except IndexError:
        driver.quit()
        return {'error':'Invalid credentials'}
    except Exception as e:
        driver.quit()
        return {'error':e}
    

if __name__ == '__main__':
    print(main('01fe21bci051',26,'Jul',2003))
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import urllib.request
import os


class InstaScrap:
    def __init__(self, track_name):
        self.url = 'https://www.instagram.com/'
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.track_name = track_name
        self.action = ActionChains(self.driver)

    def login(self, user_name, password):
        # username
        user_name_field = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
        user_name_field.click()
        user_name_field.send_keys(user_name)
        # password
        password_field = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_field.click()
        password_field.send_keys(password)
        # log in
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
        self.acc_name()

    def acc_name(self):
        name = self.track_name
        search = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div/span[2]')))
        search.click()
        search_2 = self.driver.find_element_by_xpath('// *[ @ id = "react-root"] / section / nav / div[2] / div / div / div[2] / input')
        search_2.send_keys(name)
        time.sleep(3)
        user_acc = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]/div/div[2]/div/span')))
        insta_name = user_acc.get_attribute('innerHTML')
        if insta_name == name:
            user_acc.click()
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h2.rkEop')))
                print("Follow this acc to scrap images")
            except:
                print("You can scrap this account")
        else:
            raise Exception("No such account")

    def followers(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.k9GMp')))
        follower = self.driver.find_elements_by_css_selector('span.g47SY')
        follower_text = follower[1].get_attribute('title')
        followers = ''
        for char in follower_text:
            if char != ',':
                followers += char

        return int(followers)

    def following(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.k9GMp')))
        following = self.driver.find_elements_by_css_selector('span.g47SY')
        following_text = following[2].get_attribute('innerHTML')
        following = ''
        for char in following_text:
            if char != ',':
                following += char

        return int(following)

    def post(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.k9GMp')))
        post_text = self.driver.find_elements_by_css_selector('span.g47SY')
        post_text = post_text[0].text
        post = ''
        for i in post_text:
            if i != ',':
                post += i

        return int(post)

    def followers_list(self, loc=None):
        if loc == 'cwd':
            loc = os.getcwd()
        if self.followers() != 0:
            time.sleep(5)
            follower_click = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')))
            follower_click.click()
            time.sleep(5)
            scroll_follow = self.followers()
            # version--1 Handling follow menu scroll
            for i in range(2):
                self.action.send_keys(Keys.TAB)
            for i in range(20):
                self.action.send_keys(Keys.ARROW_DOWN).perform()
            for i in range(2):
                self.action.send_keys(Keys.TAB).perform()
            action2 = ActionChains(self.driver)
            time.sleep(5)
            for i in range(scroll_follow//3):
                action2.send_keys(Keys.ARROW_DOWN).perform()
                time.sleep(0.1)
            html = self.driver.page_source
            html_soup = BeautifulSoup(html, 'lxml')
            names = html_soup.find_all('div', class_='d7ByH')
            follower_list = []
            for name in names:
                name_str = name.span.a.text
                follower_list.append(name_str)
            if loc is not None:
                with open(f'{loc}\\followers{self.track_name}.txt', 'w') as f:
                    count = 1
                    for name in names:
                        name_str = name.span.a.text
                        name_str = f'{count}.{name_str}'
                        f.write(name_str+'\n')
                        count += 1
            close = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button')
            close.click()
        else:
            if loc is not None:
                with open(f'{loc}\\followers{self.track_name}.txt', 'w') as f:
                    f.write("NO FOLLOWERS")
            follower_list = []
        return follower_list

    def following_list(self, loc=None):
        if loc == 'cwd':
            loc = os.getcwd()
        if self.following() != 0:
            time.sleep(5)
            following_click = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')))
            following_click.click()
            time.sleep(2)
            scroll_follow = self.following()

            # Handling follow menu scroll
            for i in range(2):
                self.action.send_keys(Keys.TAB)
            for i in range(20):
                self.action.send_keys(Keys.ARROW_DOWN).perform()
            for i in range(2):
                self.action.send_keys(Keys.TAB).perform()
            action2 = ActionChains(self.driver)
            time.sleep(5)
            for i in range(scroll_follow//3):
                action2.send_keys(Keys.ARROW_DOWN).perform()
                time.sleep(0.1)
            html = self.driver.page_source
            html_soup = BeautifulSoup(html, 'lxml')
            names = html_soup.find_all('div', class_='d7ByH')
            following_list = []
            for name in names:
                name_str = name.span.a.text
                following_list.append(name_str)
            if loc is not None:
                with open(f'{loc}\\following{self.track_name}.txt', 'w') as f:
                    count = 1
                    for name in names:
                        name_str = name.span.a.text
                        name_str = f'{count}.{name_str}'
                        f.write(name_str+'\n')
                        count += 1
            close = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button')
            close.click()
        else:
            if loc is not None:
                with open(f'{loc}\\following{self.track_name}.txt', 'w') as f:
                    f.write("NOT FOLLOWING ANYONE")
            following_list = []
        return following_list

    def images(self, loc=None, profile=False):
        if loc is None:
            loc = os.getcwd()
        if profile:
            try:
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/div/div/span/img')))
                dp_link = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/div/div/span/img')
                dp_link = dp_link.get_attribute('src')
                path_dir = f'{loc}\\ProfilePic{self.track_name}'
                boo = os.path.isdir(path_dir)

                if not boo:
                    os.mkdir(path_dir)
                dp_path = f'{path_dir}\\profilePIC.jpg'
                urllib.request.urlretrieve(dp_link, dp_path)
            except:
                print("No Profile pic")
        time.sleep(5)
        img_link_list = []
        while True:
            scroll_height_new = self.driver.execute_script('return document.body.scrollHeight')
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(5)
            html = self.driver.page_source
            soup = BeautifulSoup(html, 'lxml')

            images = soup.find_all('img')
            for image in images:
                img_link = image['src']
                img_link_list.append(img_link)

            scroll_height = self.driver.execute_script('return document.body.scrollHeight')

            if scroll_height == scroll_height_new:
                break
        count = 0
        img_link_list_1 = []
        for i in img_link_list:
            if i not in img_link_list_1:
                img_link_list_1.append(i)
        path = f'{loc}\\post{self.track_name}'
        boo = os.path.isdir(path)
        if not boo:
            os.mkdir(path)
        for link in img_link_list_1:
            count += 1
            path_dwnld = f'{path}\\post({count}).jpg'
            try:
                urllib.request.urlretrieve(link, path_dwnld)
            except:
                pass

    def bio(self, loc=None):
        if loc == 'cwd':
            loc = os.getcwd()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/div[2]')))
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        bio_sec = soup.find('div', class_='-vDIg')
        bio = []
        for i in bio_sec.children:
            try:
                bio_part = str(i.get_text())
                bio.append(bio_part)
            except:
                bio_part = str(i)
                bio.append(bio_part)
        if loc:
            with open(f'{self.track_name}_BIO.txt', 'w', encoding="utf-8") as f:
                for bio_parts in bio:
                    f.write(f'{bio_parts}\n')
        # bio = bio_sec.get_text()
        return bio






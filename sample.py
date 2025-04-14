from seleniumbase import Driver
from bs4 import BeautifulSoup

def test_main_content_titles():
    # Initialize the Driver with headless mode
    driver = Driver(headless=True,uc=True)  # You can set `headed=True` if you want a GUI

    # Open bol.com
    driver.get("https://musescore.com/user/58619206")

    page_source = driver.get_page_source()
    print(page_source)
    
    soup = BeautifulSoup(page_source,'html.parser')
    # Find all elements with the class 'main_cntent_title'

    name_tag = soup.select_one('[property="og:title"]')
    if name_tag:
        print("Extracted Name:", name_tag['content'])
    else:
        print("❌ og:title tag not found!")
        
    # Close the browser
    driver.quit()

if __name__ == "__main__":
    test_main_content_titles() 

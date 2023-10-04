from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
        headers=headers)
    print("Searching......\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    
    # Check if elements were found before accessing them
    location_elements = soup.select('.BNeawe iBp4i AP7Wnd')
    if location_elements:
        location = location_elements[0].getText().strip()
        print(location)
    else:
        print("Location not found on the page.")

    time_elements = soup.select('.BNeawe tAd8D AP7Wnd')
    if time_elements:
        time = time_elements[0].getText().strip()
        print(time)
    else:
        print("Time not found on the page.")

    info_elements = soup.select('.BNeawe tAd8D AP7Wnd')
    if info_elements:
        info = info_elements[1].getText().strip()
        print(info)
    else:
        print("Weather information not found on the page.")

    weather_elements = soup.select('.BNeawe iBp4i AP7Wnd')
    if weather_elements:
        weather = weather_elements[2].getText().strip()
        print(weather)
    else:
        print("Temperature not found on the page.")

city=input("Enter the Name of Any City >>  ")
city=city+" weather"
weather(city)


import requests

if __name__ == '__main__':
    print('Message: "wave" (HTTP GET)')
    wave_get_response = requests.get('http://localhost:5000/echo/wave')
    print(f'Content: "{wave_get_response.content.decode()}"')

    print('Message: "wave" (HTTP POST)')
    wave_post_response = requests.post('http://localhost:5000/echo/wave')
    print(wave_post_response)

    for i in range(5):
        print(f'Feeling lucky: {i}')
        lucky_dip_response = requests.get('http://localhost:5000/lucky')
        print(f'Response code: {lucky_dip_response.status_code}')
        print(f'Content: {lucky_dip_response.json()}')

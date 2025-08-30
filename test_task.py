import requests
def main():
    try:
        response = requests.get('https://catfact.ninja/facts', timeout=30)
        response.raise_for_status()

        data = response.json()
        total, per_page = data['total'], data['per_page']
        last_page = (total + per_page - 1) // per_page

        last_response = requests.get(f'https://catfact.ninja/facts?page={last_page}', timeout=30)
        last_response.raise_for_status()
        last_data = last_response.json()

        shortest = min(last_data['data'], key=lambda x: len(x['fact']))

        print(f"\"{shortest['fact']}\"")
    except Exception as e:
        print(f"Ошибка {e}")

if __name__ == "__main__":
    main()
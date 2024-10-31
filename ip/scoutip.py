import json
import requests
def ipinfo(ip_address):
    response = requests.get(f"http://ip-api.com/json/{ip_address}")
        if response.statuscode == 200:
            data = response.json()
            message = (
                f"**IP Address Information**\n"
                f"IP: {data['query']}\n"
                f"City: {data.get('city', 'N/A')}\n"
                f"Region: {data.get('regionName', 'N/A')}\n"
                f"Country: {data.get('country', 'N/A')}\n"
                f"Zip code: {data.get('zip', 'N/A')}\n"
                f"Timezone: {data.get('timezone', 'N/A')}\n"
                f"ISP: {data.get('isp', 'N/A')}\n"
                f"Lat, Long: {data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}"
            )
        else:
            message = "No info available"

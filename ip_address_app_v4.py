import requests
import json
import tkinter as tk

def get_ip_info():
    """
    Get the public IP addressing information using ipapi.co API.
    """
    response = requests.get('https://ipapi.co/json/')
    return response.json()

def main():
    """
    Display and format the computer's current public IP addressing information, geolocation, ISP, and ASN.
    """
    ip_info = get_ip_info()
    ipv4_address = ip_info['ip']
    ipv6_address = ip_info.get('ipv6', 'N/A') if 'ipv6' in ip_info else 'N/A'
    city = ip_info['city']
    region = ip_info['region']
    country = ip_info['country_name']
    isp = ip_info['org']
    asn = ip_info['asn']
    timezone = ip_info['timezone']
    currency = ip_info['currency']

    # Create GUI window
    root = tk.Tk()
    root.title("IP Address Information")

    # Display IP information using labels
    tk.Label(root, text=f"IPv4 Address: {ipv4_address}").pack()
    tk.Label(root, text=f"IPv6 Address: {ipv6_address}").pack()
    tk.Label(root, text=f"City: {city}, Region: {region}, Country: {country}").pack()
    tk.Label(root, text=f"ISP: {isp}").pack()
    tk.Label(root, text=f"ASN: {asn}").pack()
    tk.Label(root, text=f"Timezone: {timezone}").pack()
    tk.Label(root, text=f"Currency: {currency}").pack()

    root.mainloop()

if __name__ == "__main__":
    main()

import requests
import json

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
    formatted_ip4 = f"IPv4 Address: {ipv4_address}"
    formatted_ip6 = f"IPv6 Address: {ipv6_address}" if ipv6_address else "IPv6 Address: N/A"
    formatted_location = f"City: {city}, Region: {region}, Country: {country}"
    formatted_isp = f"ISP: {isp}"
    formatted_asn = f"ASN: {asn}"
    print(formatted_ip4)
    print(formatted_ip6)
    print(formatted_location)
    print(formatted_isp)
    print(formatted_asn)

if __name__ == "__main__":
    main()

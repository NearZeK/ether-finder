
import hashlib
import random
import sys
import time
import requests
from colorama import Fore
print("Compiling modules, wait...") 

def generate_eth_address():
    private_key = ''.join(random.choice('0123456789abcdef') for i in range(64))
    keccak = hashlib.sha3_256()
    keccak.update(private_key.encode())
    keccak_digest = keccak.hexdigest()
    eth_address = "0x" + keccak_digest[-40:]
    return private_key, eth_address
while True:
    eth_private_key, eth_address = generate_eth_address()
    api_key = 'WXWU1HKNC5VTA3R2C2GSXSFA9X28G1I7M2'
    url = f'https://api.etherscan.io/api?module=account&action=balance&address={eth_address}&tag=latest&apikey={api_key}'
    print(Fore.GREEN + f"Private Key: {eth_private_key}")
    print(Fore.WHITE + f"Address: {eth_address}")
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Check if the response contains the balance
        if data['status'] == '1':
            balance_ether = float(data['result']) / 10 ** 18
            print(Fore.RED + f"Balance {eth_address}: {balance_ether} ETH")
            if balance_ether > 0.000000000001:
                file = open("data.txt", "w")
                file.write(eth_address)
                file.write(eth_private_key)
                file.write(balance_ether)
                file.close()
                sys.exit()
            else:
                pass
        else:
            print(f"Error: {data['message']}")
    else:
        print("Error: Failed to retrieve data from Etherscan API")
    time.sleep(0.4)
    #

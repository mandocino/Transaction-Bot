from web3 import Web3
import time
import asyncio
import telegram
import time
import requests
from datetime import datetime
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

uniswap_0kn = "0x2947dC50cc24cc55AFBf22807a49cC302d65568C"
#WETH_ADDRESS = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
Lp_address = "0x2947dC50cc24cc55AFBf22807a49cC302d65568C"
weth_address = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
contract_address = '0x4594CFfbFc09BC5e7eCF1C2e1C1e24F0f7D29036' 
coingecko_url= "CG-KAYiT6sGZ2dDF2fKTgcnFaJB"
api_url = "https://api.coingecko.com/api/v3"

BOT_TOKEN = ""
CHAT_ID = ""
ETHERSCAN_API_TOKEN="QHFKN1F91QA1PU7BJASTU15TJVK9DYXQYM"
bot = telegram.Bot(token=BOT_TOKEN)

def get_days_and_hours_apart(timestamp1, timestamp2):
    start_timestamp, end_timestamp = min(timestamp1, timestamp2), max(timestamp1, timestamp2)
    time_difference_seconds = end_timestamp - start_timestamp
    days = time_difference_seconds // (24 * 3600)
    remaining_seconds = time_difference_seconds % (24 * 3600)
    hours = remaining_seconds // 3600

    return days, hours

def get_eth_price_in_currency(currency='usd'):
    api_url = f'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies={currency}'
    
    try:
        response = requests.get(api_url)
        data = response.json()
        eth_price = data['ethereum'][currency]
        return eth_price
    except (requests.RequestException, KeyError) as e:
        print(f"Error retrieving ETH price: {e}")
        return None

def wait_for_new_block(web3):
    current_block = web3.eth.block_number

    while True:
        new_block = web3.eth.block_number

        if new_block > current_block:
            return new_block

        time.sleep(1)

def get_eth_price_at_block(block_number):
    block_info = w3.eth.get_block(block_number)

    if block_info:
        timestamp = block_info['timestamp']
    
    lower_timestamp = timestamp - 1000
    upper_timestamp = timestamp + 3000
    data = cg.get_coin_market_chart_range_by_id(id='ethereum',vs_currency='usd',from_timestamp=lower_timestamp,to_timestamp=upper_timestamp)
    return (data['prices'][0][1])

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/e23b710c0f4b49dfb7d1c48fc92882e0'))

contract_abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"ReentrancyGuardReentrantCall","type":"error"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"Status","type":"bool"}],"name":"DistributionStatus","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"bool","name":"isExcluded","type":"bool"}],"name":"ExcludeFromFees","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"bool","name":"isExcluded","type":"bool"}],"name":"ExcludeFromMaxHolding","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"Status","type":"bool"}],"name":"FeeStatus","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"FeeUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"newAmount","type":"uint256"}],"name":"NewSwapAmount","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"newWallet","type":"address"},{"indexed":true,"internalType":"address","name":"oldWallet","type":"address"}],"name":"OKNTreasuryWalletUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"tokensSwapped","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"ethReceived","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"tokensIntoLiqudity","type":"uint256"}],"name":"SwapAndLiquify","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TransferForeignToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"newAmount","type":"uint256"}],"name":"UpdatedMaxWalletAmount","type":"event"},{"inputs":[],"name":"Marketing","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"NodeOperatorRewards","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"OKNTreasuryFeeOnBuy","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"OKNTreasuryFeeOnSell","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"OKNTreasuryWallet","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"Seed","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"Team","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"dexPair","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"dexRouter","outputs":[{"internalType":"contract IDexRouter","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"distributeAndLiquifyStatus","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool","name":"_value","type":"bool"}],"name":"enableOrDisableFees","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"feesStatus","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"bool","name":"value","type":"bool"}],"name":"includeOrExcludeFromFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"bool","name":"value","type":"bool"}],"name":"includeOrExcludeFromMaxHolding","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"isExcludedFromFee","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"isExcludedFromMaxHolding","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxHoldLimit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minTokenToSwap","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"percentDivider","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_OKNTreasuryFee","type":"uint256"}],"name":"setBuyFeePercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_value","type":"bool"}],"name":"setDistributionStatus","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"setMaxHoldLimit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"setMinTokenToSwap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_OKNTreasuryFee","type":"uint256"}],"name":"setSellFeePercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"totalBuyFeePerTx","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"totalSellFeePerTx","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOKNTreasuryWallet","type":"address"}],"name":"updateOKNTreasuryWallet","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdrawETH","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'  # replace with your contract's ABI
WETH_ABI = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"guy","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Withdrawal","type":"event"}]'

okn_contract = w3.eth.contract(address=contract_address, abi=contract_abi)
weth_contract = w3.eth.contract(address=weth_address, abi=WETH_ABI)
#transfer_filter = weth_contract.events.Transfer().createFilter(fromBlock='latest')
message = "Starting mandobot script."
asyncio.run(bot.send_message(chat_id=CHAT_ID, text=message))
while True:
    try:
        new_block_number = wait_for_new_block(w3)
        logs = okn_contract.events.Transfer().get_logs(fromBlock=new_block_number)
        total_supply = w3.from_wei(okn_contract.functions.totalSupply().call(block_identifier=new_block_number),'ether')

        for log in logs:
            txType = 0
            lastMessage = ""
            message=""
            address_to_check = ""
            print(f"Transfer of {w3.from_wei(log.args.value, 'ether'):,} 0kn from {log.args['from']} to {log.args.to}")
            if (log.args['from'].lower() == uniswap_0kn.lower()):
                txType = 1
                address_to_check = log.args['to']
                message += "<b>0kn Buy Alert!</b>🚀💵🚀\n"
                total0kn = w3.from_wei(okn_contract.functions.balanceOf(address_to_check).call(),'ether')
                message += f"<b>New Holdings: </b>{total0kn:,.2f} 0kn\n"
                if (total0kn >= 40000000):
                    message += "🐳🐳🐳🐳🐳🐳\n"
                elif (total0kn >= 15000000):
                    message += "🐋🐋🐋🐋🐋\n"
                elif (total0kn >= 6500000):
                    message += "🦈🦈🦈🦈\n"
                elif (total0kn >= 1000000):
                    message += "🐠🐠🐠\n"
                elif (total0kn >= 500000):
                    message += "🦐🦐\n"
                else:
                    message += "🍤\n"

                bought0kn = w3.from_wei(log.args.value, 'ether')
                message+=f"<b>Bought:</b> {bought0kn:,.2f} 0kn\n"

                boughtPercentage = float(bought0kn) / float(total0kn-bought0kn) * 100 
                if (boughtPercentage != 100.0):
                    message += f"<b>Trade % vs Prev. Holdings:</b> Increased {boughtPercentage:.2f}%\n"
                elif (boughtPercentage == 100.0):
                    message += f"<b>New Wallet Holder!</b>🍾🥂\n"
                weth_amount = w3.from_wei(weth_contract.functions.balanceOf("0x2947dC50cc24cc55AFBf22807a49cC302d65568C").call(),'ether')
                token1_amount = w3.from_wei(okn_contract.functions.balanceOf("0x2947dC50cc24cc55AFBf22807a49cC302d65568C").call(),'ether')
                eth_price = float(2248.89)#get_eth_price_in_currency('usd')

                if eth_price is not None:
                    print(f"The current price of ETH in {'usd'.upper()}: {eth_price}")
                else:
                    print("Failed to retrieve ETH price.")

                price_token1_in_weth = float(weth_amount) / float(token1_amount)
                price_token1_in_usd = price_token1_in_weth * eth_price
                message += f"<b>Price:</b> ${price_token1_in_usd:.7f}\n"
                totalSpentDollars = float(price_token1_in_weth) * float(bought0kn) * float(eth_price)
                totalEthSpent = float(price_token1_in_weth) * float(bought0kn)
                message += f"<b>Spent:</b> ${totalSpentDollars:,.2f} USD ({totalEthSpent:,.2f} Weth) \n"
                circulating_MCap = float(total_supply) * float(.7) * float(price_token1_in_weth) * float(eth_price)
                fdv_MCap = float(total_supply) * float(price_token1_in_weth) * float(eth_price)
                message += f"<b>Circulating MCap:</b> ${circulating_MCap:,.2f}\n"
                message += f"<b>FDV MCap:</b> ${fdv_MCap:,.2f}\n"
                lastMessage = [bought0kn, price_token1_in_usd]

            elif (log.args['to'].lower() == uniswap_0kn.lower()):

                txType = 2
                address_to_check = log.args['from']
                message += "<b>0kn Sell Alert!!</b>🔻⚠️🔻\n"
                sold0kn = w3.from_wei(log.args.value, 'ether')
                message+=f"{sold0kn:,.2f} <b>0kn SOLD.</b>\n"
                remaining0kn = w3.from_wei(okn_contract.functions.balanceOf(address_to_check).call(),'ether')
                total0kn = remaining0kn + sold0kn
                message += f"<b>Remaining Holdings:</b> {remaining0kn:,.2f}0kn\n"
                if (total0kn >= 40000000):
                    message += "🐳🐳🐳🐳🐳🐳\n"
                elif (total0kn >= 15000000):
                    message += "🐋🐋🐋🐋🐋\n"
                elif (total0kn >= 6500000):
                    message += "🦈🦈🦈🦈\n"
                elif (total0kn >= 1000000):
                    message += "🐠🐠🐠\n"
                elif (total0kn >= 500000):
                    message += "🦐🦐\n"
                else:
                    message += "🍤\n"

                soldPercentage = float(sold0kn) / float(total0kn) * 100 
                if (soldPercentage != 100.0):
                    message += f"<b>Trade % vs Holdings: </b>{soldPercentage:.2f}%\n"
                elif (soldPercentage == 100.0):
                    message += f"<b>Wallet Completely Sold</b>\n"

                weth_amount = w3.from_wei(weth_contract.functions.balanceOf("0x2947dC50cc24cc55AFBf22807a49cC302d65568C").call(),'ether')
                token1_amount = w3.from_wei(okn_contract.functions.balanceOf("0x2947dC50cc24cc55AFBf22807a49cC302d65568C").call(),'ether')

                eth_price = float(2248.89)#get_eth_price_in_currency('usd')

                if eth_price is not None:
                    print(f"The current price of ETH in {'usd'.upper()}: {eth_price}")
                else:
                    print("Failed to retrieve ETH price.")

                price_token1_in_weth = float(weth_amount) / float(token1_amount)
                price_token1_in_usd = price_token1_in_weth * eth_price
                message += f"<b>Price:</b> ${price_token1_in_usd:.7f}\n"
                totalSoldDollars = float(price_token1_in_weth) * float(sold0kn) * float(eth_price)
                totalEthSold = float(price_token1_in_weth) * float(sold0kn)
                message += f"<b>Total USD Sold:</b> ${totalSoldDollars:,.2f} ({totalEthSold:.2f} Eth)\n"
                circulating_MCap = float(total_supply) * float(.7) * float(price_token1_in_weth) * float(eth_price)
                fdv_MCap = float(total_supply) * float(price_token1_in_weth) * float(eth_price)
                message += f"<b>Circulating MCap:</b> ${circulating_MCap:,.2f}\n"
                message += f"<b>FDV MCap:</b> ${fdv_MCap:,.2f}\n"
                lastMessage = [sold0kn, price_token1_in_usd]
                
            averageBuyPrice = 0
            totalOwned = 0
            totalSpent = 0
            totalReturn = 0
            buyCount = 0
            sellCount = 0
            sendCount = 0
            totalBuyQty = 0
            totalSendQty = 0
            totalSellQty = 0
            transaction_hash = log['transactionHash'].hex()
            chart_URL = f"<a href='https://www.dextools.io/app/en/ether/pair-explorer/{Lp_address}'>Chart</a>"
            txHash_URL = f"<a href='https://etherscan.io/tx/{transaction_hash}'>TxHash</a>"
            walletHolder_URL = f"<a href='https://etherscan.io/address/{address_to_check}'>Wallet</a>"

            url = f"https://api.etherscan.io/api?module=account&action=tokentx&contractaddress={contract_address}&address={address_to_check}&page=1&offset=100&startblock=0&endblock=27025780&sort=asc&apikey={ETHERSCAN_API_TOKEN}"
            response = requests.get(url)

            allTrades = []

            if response.status_code == 200:
                data = response.json()
                for result in data['result']:
                    allTrades.append(result)
            else:
                print(f"Error: {response.status_code}")
                print(response.text)

            message += f"{txHash_URL} | {walletHolder_URL} | {chart_URL}\n\n"
            lastTxUnix = ""
            for tx in allTrades:
                if (tx['from']== uniswap_0kn.lower()):
                    buyCount +=1
                    id = int(tx['blockNumber'])
                    weth_balance = w3.from_wei(weth_contract.functions.balanceOf("0x2947dC50cc24cc55AFBf22807a49cC302d65568C").call(block_identifier=id),'ether')
                    okn_balance = w3.from_wei(okn_contract.functions.balanceOf("0x2947dC50cc24cc55AFBf22807a49cC302d65568C").call(block_identifier=id),'ether')
                    okn_balance_wallet = w3.from_wei(okn_contract.functions.balanceOf(address_to_check).call(block_identifier=id),'ether')
                    eth_price = float(2248.89)#get_eth_price_at_block(id)
                    price_token1_in_weth_old = float(weth_balance) / float(okn_balance)
                    price_token1_in_usd_old = float(price_token1_in_weth_old) * float(eth_price)
                    buyQty = w3.from_wei(int(tx['value']), 'ether')
                    totalBuyQty += buyQty
                    totalOwned = float(totalOwned)
                    totalOwned += float(buyQty)
                    totalSpent += float(buyQty) * float(price_token1_in_usd_old)
                    averageBuyPrice = float(totalSpent) / float(totalOwned)
                    pnlPercentage = ((float(price_token1_in_usd_old)-float(averageBuyPrice))/float(averageBuyPrice))*100
                    lastTxUnix = tx['timeStamp']
                    current_timestamp = int(time.time())
                    dt_object = int(lastTxUnix)
                    days_apart, hours_apart = get_days_and_hours_apart(dt_object, current_timestamp)                    
                    firstBuyPrice = 0
                    if (buyCount==1):
                        firstBuyPrice = price_token1_in_usd_old
                    if (price_token1_in_usd_old > averageBuyPrice):
                        message += f"<u>Buy #{buyCount}</u>: <b>Bought {buyQty:,.2f}</b> at <b>${price_token1_in_usd_old:.6f}</b> above Holding average\n" 
                    elif (price_token1_in_usd_old < averageBuyPrice):
                        message += f"<u>Buy #{buyCount}</u>: <b>Bought {buyQty:,.2f}</b> at <b>${price_token1_in_usd_old:.6f}</b> below Holding average\n"
                    elif (price_token1_in_usd_old == averageBuyPrice):
                        message += f"<u>Buy #{buyCount}</u>: <b>Bought {buyQty:,.2f}</b> at <b>${price_token1_in_usd_old:.6f}</b> at Holding average\n"
                    message += f"Holding Avg: {averageBuyPrice:.7f} | PnL %: {pnlPercentage:.2f} | Total 0kn: {okn_balance_wallet:,.2f} {days_apart} days, {hours_apart} hours ago\n"
                    
                if (tx['to']== uniswap_0kn.lower()):
                    sellCount+=1
                    id = int(tx['blockNumber'])
                    weth_balance = w3.from_wei(weth_contract.functions.balanceOf("0x2947dC50cc24cc55AFBf22807a49cC302d65568C").call(block_identifier=id),'ether')
                    okn_balance = w3.from_wei(okn_contract.functions.balanceOf("0x2947dC50cc24cc55AFBf22807a49cC302d65568C").call(block_identifier=id),'ether')
                    okn_balance_wallet = w3.from_wei(okn_contract.functions.balanceOf(address_to_check).call(block_identifier=id),'ether')
                    eth_price = float(2248.89)#get_eth_price_at_block(id)
                    price_token1_in_weth_old = float(weth_balance) / float(okn_balance)
                    price_token1_in_usd_old = float(price_token1_in_weth_old) * float(eth_price)
                    sellQty = w3.from_wei(int(tx['value']), 'ether')
                    totalSellQty += sellQty
                    sellQty = float(sellQty) + (float(sellQty) * float(.09))
                    totalOwned = float(totalOwned)
                    totalOwned -= float(sellQty)
                    totalSpent -= float(sellQty) * float(averageBuyPrice)
                    averageSellPrice = float(totalSpent) / float(totalOwned)
                    pnlPercentage = ((float(price_token1_in_usd)-float(averageSellPrice))/float(averageSellPrice))*100
                    lastTxUnix = tx['timeStamp']
                    current_timestamp = int(time.time())
                    dt_object = int(lastTxUnix)
                    days_apart, hours_apart = get_days_and_hours_apart(dt_object, current_timestamp)
                    firstBuyPrice = 0
                    if (price_token1_in_usd_old > averageSellPrice):
                        message += f"<u>Sell #{sellCount}</u>: <b>Sold {sellQty:,.2f}</b> at <b>${price_token1_in_usd_old:.6f}</b> above Holding average\n" 
                    elif (price_token1_in_usd_old < averageSellPrice):
                        message += f"<u>Sell #{sellCount}</u>: <b>Sold {sellQty:,.2f}</b> at <b>${price_token1_in_usd_old:.6f}</b> below Holding average\n"
                    elif (price_token1_in_usd_old == averageSellPrice):
                        message += f"<u>Sell #{sellCount}</u>: <b>Sold {sellQty:,.2f}</b>  at <b>${price_token1_in_usd_old:.6f}</b> at Holding average\n"
                    message += f"Holding Avg: {averageSellPrice:.7f} | PnL %: {pnlPercentage:.2f} | Total 0kn: {okn_balance_wallet:,.2f} {days_apart} days, {hours_apart} hours ago\n"
                
                if (tx['from'].lower() == address_to_check.lower() and tx['to'].lower() != uniswap_0kn.lower()):
                    sendCount += 1
                    sendQty = w3.from_wei(int(tx['value']), 'ether')
                    totalSendQty += sendQty
                    if (tx['to'].lower() == "0x4594CFfbFc09BC5e7eCF1C2e1C1e24F0f7D29036".lower()):
                        devWallet_address = tx['to'].lower()
                        devWallet_URL = f"<a href='https://etherscan.io/address/{devWallet_address}'>Dev Wallet</a>"
                        message += f"<u>Send #{sendCount}</u>: <b>Sent {sendQty:,.2f}</b> to the {devWallet_URL} from the sale.\n"
                    else:
                        randomWallet_address = tx['to'].lower()
                        randomWallet_URL = f"<a href='https://etherscan.io/address/{randomWallet_address}'>Random Wallet</a>"
                        splice_address = last_four_characters = randomWallet_address[-4:]
                        message += f"<u>Send #{sendCount}</u>: <b>Sent {sendQty:,.2f}</b> to another {randomWallet_URL} (0x{splice_address})\n"

            if (txType == 1):
                    buyCount += 1
                    if (lastMessage[1] > averageBuyPrice):
                        message += f"<u>Buy #{buyCount}</u>: <b>Bought {lastMessage[0]:,.2f}</b> at <b>${price_token1_in_usd_old:.6f}</b> above Holding average\n" 
                    elif (price_token1_in_usd_old < averageBuyPrice):
                        message += f"<u>Buy #{buyCount}</u>: <b>Bought {lastMessage[0]:,.2f}</b> at <b>${price_token1_in_usd_old:.6f}</b> below Holding average\n"
                    elif (price_token1_in_usd_old == averageBuyPrice):
                        message += f"<u>Buy #{buyCount}</u>: <b>Bought {lastMessage[0]:,.2f}</b> at <b>${price_token1_in_usd_old:.6f}</b> at Holding average\n"
                    message += f"Holding Avg: {averageBuyPrice:.7f} | PnL %: {pnlPercentage:.2f} | Total 0kn: {okn_balance_wallet:,.2f} {days_apart} days, {hours_apart} hours ago\n"
            elif (txType == 2):
                    sellCount += 1
                    if (lastMessage[1] > averageSellPrice):
                        message += f"<u>Sell #{sellCount}</u>: <b>Sold {lastMessage[0]:,.2f}</b> at <b>${price_token1_in_usd_old:.6f}</b> above Holding average\n" 
                    elif (price_token1_in_usd_old < averageSellPrice):
                        message += f"<u>Sell #{sellCount}</u>: <b>Sold {lastMessage[0]:,.2f}</b> at <b>${price_token1_in_usd_old:.6f}</b> below Holding average\n"
                    elif (price_token1_in_usd_old == averageSellPrice):
                        message += f"<u>Sell #{sellCount}</u>: <b>Sold {lastMessage[0]:,.2f}</b>  at <b>${price_token1_in_usd_old:.6f}</b> at Holding average\n"
                    message += f"Holding Avg: {averageSellPrice:.7f} | PnL %: {pnlPercentage:.2f} | Total 0kn: {okn_balance_wallet:,.2f} {days_apart} days, {hours_apart} hours ago\n"
            message += f"<b>Buys:</b> {buyCount} | <b>Sells:</b> {sellCount} | <b>Transfers:</b> {sendCount}\n"
            message += f"<b>Buy Qty:</b>{totalBuyQty:,.2f} | <b>Sell Qty:</b>{totalSellQty:,.2f} | <b>Transfer Qty:</b>{totalSendQty:,.2f}\n"

            asyncio.run(bot.send_message(chat_id=CHAT_ID, text=message, parse_mode='HTML',disable_web_page_preview=True))

    except Exception as e:
        print("An unexpected error occurred:", e)
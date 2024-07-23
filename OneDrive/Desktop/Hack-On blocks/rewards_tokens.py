from web3 import Web3

# Connect to blockchain
w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# Load smart contract
contract_address = '0xYourContractAddress'
abi = [...]  # ABI of the smart contract
contract = w3.eth.contract(address=contract_address, abi=abi)

# Reward tokens
def reward_user(address, amount):
    tx = contract.functions.rewardTokens(address, amount).buildTransaction({
        'chainId': 3,  # Ropsten
        'gas': 70000,
        'gasPrice': w3.toWei('1', 'gwei'),
        'nonce': w3.eth.getTransactionCount(w3.eth.defaultAccount),
    })
    signed_tx = w3.eth.account.signTransaction(tx, private_key='YourPrivateKey')
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return tx_hash.hex()


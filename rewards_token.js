async function rewardUser(address, amount) {
    const contractAddress = '0xYourContractAddress';
    const abi = [...] // ABI of the smart contract

    if (typeof window.ethereum !== 'undefined') {
        const web3 = new Web3(window.ethereum);
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        const accounts = await web3.eth.getAccounts();
        const contract = new web3.eth.Contract(abi, contractAddress);

        contract.methods.rewardTokens(address, amount).send({ from: accounts[0] })
            .on('receipt', function(receipt){
                console.log('Tokens rewarded: ', receipt);
            });
    }
}
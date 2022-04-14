from brownie import accounts, config, network, interface


def main():
    """
    Runs the get_weth function to get WETH
    """
    """
    print(f"Active network is {network.show_active()}")
    if network.show_active() == "mainnet-fork":
        account = accounts[0]
    if network.show_active() == "kovan":
        account = accounts.add(config["wallets"]["from_key"])
    else:
        account = accounts.load("testing")
    """
    get_weth(accounts[0])


def get_weth(account=None):
    """
    Mints WETH by depositing ETH.
    """
    account = (
        account if account else accounts.add(config["wallets"]["from_key"])
    )  # add your keystore ID as an argument to this call
    weth = interface.WethInterface(
        config["networks"][network.show_active()]["weth_token"]
    )
    tx = weth.deposit({"from": account, "value": 0.01 * 1e18})
    tx.wait(1)
    print("Received 0.01 WETH")
    return tx

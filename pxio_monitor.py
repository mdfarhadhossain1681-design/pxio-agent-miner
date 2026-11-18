"""PXIO mining state checker (read-only).

Reads the PxioMiningV2 state for a wallet via a public BSC RPC and reports
pending mined $PXIO, total claimed, storage usage vs. the cap, and the
estimated hours until storage fills. Never signs or sends a transaction.
"""
import json
import urllib.request

RPC_URLS = [
    "https://bsc-dataseed.binance.org",
    "https://bsc-dataseed1.binance.org",
    "https://bsc-dataseed2.binance.org",
]
MINING_CONTRACT = "0xaf86f162299916Da344ef536Fc50f40cBa2bF703"
WALLET = "0x03484EC26021896398cA8E7434831b9a47A5470f"
STATE_SELECTOR = "0x31e658a5"  # state(address)


def rpc(method, params):
    payload = json.dumps(
        {"jsonrpc": "2.0", "id": 1, "method": method, "params": params}
    ).encode()
    for url in RPC_URLS:
        try:
            req = urllib.request.Request(
                url, data=payload, headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=15) as r:
                res = json.load(r)
            if res.get("result") is not None:
                return res["result"]
        except Exception:
            continue
    return None


def main():
    data = STATE_SELECTOR + "000000000000000000000000" + WALLET[2:].lower()
    res = rpc("eth_call", [{"to": MINING_CONTRACT, "data": data}, "latest"])
    if not res:
        print("RPC read failed")
        return
    h = res[2:]
    w = [int(h[i:i + 64], 16) for i in range(0, len(h), 64)]
    started, pending, rate, cap, claimed = w[0], w[2] / 1e18, w[3], w[4], w[7] / 1e18
    print(f"mining active : {bool(started)}")
    print(f"pending       : {pending:.2f} PXIO")
    print(f"total claimed : {claimed:.2f} PXIO")
    print(f"storage       : {pending:.2f} / {cap} PXIO")
    if rate:
        print(f"fills in      : ~{(cap - pending) / (rate / 1e18 if rate > 1000 else rate):.1f} hours")


if __name__ == "__main__":
    main()

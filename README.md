# PXIO Agent Miner

An AI agent powered by the **Binance Agentic Wallet** and the user's **Agent ID
(mfarhad.ai)** that autonomously manages on-chain PXIO mining on BNB Smart Chain —
with strict, permission-first safety rules.

## The problem

On-chain mining rewards are easy to lose track of: mining storage fills up,
rewards stop accruing, and users must constantly check and claim by hand.
Most users simply forget — and their mining sits paused at a full storage cap.

## What the agent does

- **Free mint** — Minted PXIO Miner NFT #6725 for free (0 BNB, gas only),
  unlocked by holding a `.ai` Agent ID.
- **Mining management** — Started mining on PxioMiningV2 (10 $PXIO/hour,
  150 $PXIO storage cap).
- **Hourly monitoring** — Reads the mining state on-chain every hour and
  reports: pending rewards, growth, storage vs. cap, and time until full.
- **Price watch** — Checks the $PXIO price every 15 minutes and alerts the
  user at $0.001, $0.80, and $1.00 (alert-only; selling is always the user's
  own decision).
- **Permission-first claims** — Rewards were claimed twice (225.21 $PXIO
  total). At the storage cap, the agent may auto-claim **only** because the
  user explicitly authorized that single action in advance.
- **Safety rules** — The agent never transfers, swaps, sells, or mints
  anything paid without the user's explicit permission for that specific
  transaction. Every transaction is previewed (contract, amount, risks)
  before execution.

## How Agent ID is used

The Agent ID `mfarhad.ai` is the agent's verified on-chain identity:
it was the eligibility key for the free Miner mint, and it binds the agent
to a single wallet identity in the Binance Agentic Wallet for all
monitoring, alerts, and permission-scoped claims.

## On-chain proof (BNB Smart Chain)

| Item | Address / Tx |
| --- | --- |
| Agent wallet | `0x03484EC26021896398cA8E7434831b9a47A5470f` |
| PxioMiningV2 | `0xaf86f162299916Da344ef536Fc50f40cBa2bF703` |
| PXIO Miners NFT | `0x58e8f1b34B60687B36BCdc78e02a2fd443De71Ab` |
| $PXIO token | `0x870aD5f304871eC0c63BE1e976406e0b095A32CD` |
| Agent ID NFT (Space ID) | `0x60B9262456dE011F7d15a54CdD8c48bAaa8B022F` |
| Miner mint tx | `0xb7d1cdc0dfcc054b8f7d6f18665ad3a7861826022316c3283a3bebcccdb2076c` |
| Claim #1 tx (+108.50 PXIO) | `0x3a078046e5e7768724f81de490d496ae657a2a1eaa26c2ed6a2736b7d5ffa1e9` |
| Claim #2 tx (+116.71 PXIO) | `0x467511a6712561b5a82501f2abef849e0377d24d998f3fdc486d1a88a7f1d579` |

## Tech stack

Binance Agentic Wallet · Agent ID (Space ID) · BNB Smart Chain ·
PxioMiningV2 · public BSC RPC (`eth_call`) · Dexscreener price API

## Code

- `pxio_monitor.py` — read-only mining state checker (the same logic the
  agent runs hourly): pending rewards, storage vs. cap, hours until full.
- `pxio_price_watch.py` — read-only $PXIO price checker against the alert
  levels ($0.001 / $0.80 / $1.00).

Both scripts are read-only and never sign or send transactions.

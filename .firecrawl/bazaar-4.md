https://cp0x.com/blog/wheres-the-money-in-x402-an-analysis-of-coinbases-bazaar-catalog

[Go to cp0x home page](https://cp0x.com/)

[Deals](https://cp0x.com/) [Loyalty](https://cp0x.com/loyalty) [For Projects](https://cp0x.com/forprojects) [Reports](https://cp0x.com/reports) [Permissionless Interfaces](https://pi.cp0x.com/) [Delegations](https://cp0x.com/delegations) [Staking](https://cp0x.com/staking)

More

[Docs](https://cp0x.com/docs) [Blog](https://cp0x.com/blog) [Vaults](https://cp0x.com/vaults) [Journey](https://cp0x.com/about) [Media Kit](https://cp0x.com/about#media-kit) [Mint free domain](https://gwei.cp0x.com/) [cp0x vs AI](https://cp0x.com/cp0xvsAI)

EN

Connect

EN

![](https://cp0x.com/uploads/blog/1784120342_x402_bazaar_market_state_cp0x.png)

The x402 Bazaar catalog is a rare chance to look at the "agent economy" through data rather than tweets. I downloaded the entire Coinbase CDP discovery catalog — all 25k+ resources sold to AI agents over the x402 protocol — and worked out who actually pays for what.

Spoiler: the market is hundreds of times smaller than it looks, the popularity metric is more than half fake, and the most interesting money is no longer in data.

The Coinbase facilitator settles payments and indexes every resource they pass through into a catalog — the **x402 Bazaar**. Every listing carries a `quality` block: how many unique wallets paid over the trailing 30 days (`l30DaysUniquePayers`), how many paid calls it received in total (`l30DaysTotalCalls`), and when the last one happened. The catalog is served publicly, paginated, no keys required:

```
GET https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources?limit=1000&offset=0
```

I pulled every page (snapshot dated July 11, 2026 — 25,443 resources, verified against `pagination.total`) and broke them down by network, price, domain, category, and traffic quality. Here is what is actually going on in there.

## The market on paper and the market in reality

The first number sounds impressive: 25 thousand paid resources for agents. Then the sobering-up begins.

**39% of the catalog is a single spam domain.**`lowpaymentfee.com` holds 10,028 listings with an identical 18-character description ("Premium API Access"), no service name, and zero traffic across every position. One participant dumped ten thousand blanks into the index — and the catalog swallowed it.

Remove that domain and 15,415 listings remain — and their picture is unexpected: **95% received at least one paid call in the past month**. That sounds like prosperity, but the cause is technical: the Bazaar has no self-registration; a listing is _created_ by the first payment that passes through the facilitator. One payment to yourself — and you are in the index. So the only honest measure is not "is there traffic" but how many _distinct_ wallets paid:

| Unique payers over 30 days | Resources |
| --- | --- |
| ≥ 1 | 14,609 |
| ≥ 2 | 6,282 |
| ≥ 5 | 962 |
| ≥ 10 | 257 |
| ≥ 21 | 112 |
| ≥ 100 | 37 |

Out of 25 thousand listings, only ~1k have any repeat demand at all, ~100 have meaningful demand, and a few dozen make up practically the entire market. **The top 10 domains collect 70% of all paid calls in the catalog.**

All in, over 30 days the whole market is **262 thousand paid calls** and roughly **$26 thousand in confirmed volume**. Revenue is computed as the sum of "endpoint price × its calls," and here the semantics of the `amount` field in x402 matter: in the `exact` scheme (25,432 listings, 99.96% of the catalog) it is the exact payment amount one-to-one, while in the `upto` scheme (11 listings) it is only the permitted maximum — the actual amount is not visible from outside. The breakdown comes out like this:

- **~$7.3 thousand — fees for API calls** (exact listings under $10; median call price $0.01);
- **~$19 thousand — one-off large purchases** under the exact scheme: tokenized gold at $1,000 per payment, goods, premium reports — real payments at full size;
- as a separate line — **Bitrefill**: 62 paid invoices under the upto scheme with a $1,000 ceiling — actual amounts are not visible, upper bound $62 thousand.

The API side of the "agent economy" on the largest facilitator currently earns about as much as a single coffee shop — but commerce has already overtaken it.

## What agents actually buy

I categorized the active segment — 1,328 resources with ≥5 payers or ≥20 calls. Important: this is a slice of _recurring_ demand specifically, so the sums in the table are smaller than the overall figures above. The active segment accounts for $4.6k of the $7.3k in API fees (the remaining ~$2.8k is smeared across a tail of thousands of barely-active listings), and the large one-off purchases ($19k) do not land in it at all — they have 1–11 payments each:

| Category | Resources | Calls, 30d | Revenue, 30d |
| --- | --- | --- | --- |
| Web/social search and scraping | 210 | **124,800** | **$2,378** |
| Crypto/DeFi data | 424 | 37,730 | $637 |
| Email and communications | 10 | 6,572 | $17 |
| AI inference and generation | 57 | 5,895 | $33 |
| Trading signals and analytics | 164 | 5,309 | $374 |
| Commerce: goods and payments | 16 | 4,242 | $327\* |
| News | 51 | 1,632 | $141 |
| People and company enrichment | 12 | 1,389 | $137 |
| Utilities (weather, geo, conversion) | 71 | 1,406 | $6 |
| Identity and compliance | 48 | 791 | $39 |

\\* Exact payments in the active segment only. Beyond this, commerce also includes Bitrefill's upto-scheme invoices (ceiling $62k) and those ~$19k of one-off purchases outside the segment (gold, goods, premium reports). The table also excludes the "Other" ($438) and "Content/media" ($23) categories.

Three observations on top of the table.

**Agents mostly buy "eyes on the internet."** Search and scraping is 48% of all paid calls and roughly a third of the API segment's fee revenue. The killer app of the entire protocol is Twitter/X data: one provider (`x402.twit.sh`) collects 64 thousand calls a month, 55 thousand of them on a single endpoint, `/tweets/search`, which 34 clients hit an average of 1,600 times each. This is selling what an agent finds hard to obtain on its own — and clients come back with thousands of calls. Next to it is managed web search: Tavily (20 thousand calls, 197 payers) and Exa, which sells over x402 directly.

**Crypto data brings volume, but not money.** 424 active resources, the second-largest category by calls — and $637 in revenue, because almost everything costs $0.001–0.01. Commodity token-price data and RPC wrappers are the most oversaturated segment of the catalog.

**The money is in premium resale and, unexpectedly, in commerce.** The revenue leader among "pure APIs" is `stableenrich.dev` (~$940/mo): a family of domains that simply proxies well-known paid APIs (Exa, People Data Labs, Firecrawl, Whitepages) through x402. Zero proprietary data; the product is _access_ itself: USDC per call, no account, no key. Person-profile enrichment at $0.28 is the highest willingness to pay in the catalog. That is the best proof that x402's value today is friction removal, not data exclusivity.

## The popularity metric can't be trusted

Ranking in the Bazaar is effectively determined by the number of unique payers over 30 days. The problem is that this metric can be gamed almost for free: a provider pays itself from fresh wallets and loses only gas on Base — fractions of a cent per "payer."

Telling a farm from a live service is simple: I look at the ratio of calls to payers. A real client that has wired the service into an agent loop makes hundreds of calls. A wallet farm makes exactly one call per wallet:

- organic leaders have calls/payers = **×15…×1,600** (Tavily ×101, Twitter search ×1,630);
- farms have **1.0…1.5**.

By this filter, **20 domains hold 24,185 "unique payers" — 58% of the catalog's entire metric**. The flagship of the genre is `api.onesource.io`: 9,362 "payers" across 9,595 calls, spread over 25 identical Ethereum RPC wrappers (balance, nonce, gas, transaction by hash — everything any node hands out for free). Those 25 endpoints occupy almost the entire top 30 by payers. The catalog's only resource with "more than 500 payers" is a mail endpoint with 873 payers across 881 calls. No comment needed.

There is a subtler genre too — **width bootstrap farms**: `clonecho.builda.company` set up 993 endpoints, each with exactly 1 payer and 1 call — a minimal self-payment to get into the index. Other providers likewise set up 500–1,400 micro-endpoints (collectible card entries, converters, reference lookups) betting on agents' semantic search: each listing is a separate lure for embeddings.

## The rails: x402 is USDC on Base

- **98% of listings** accept payment on Base mainnet; the asset is almost monopolistically USDC. Solana as the primary network is ~150 listings; everything else is statistical noise.
- At the same time, **multi-rail is becoming the default for new providers**: nearly 5 thousand listings accept Base+Solana, and another ~1.5 thousand accept combinations with Polygon, Arbitrum, Worldchain, Stellar, and Cosmos/Noble. The logic is simple: accept USDC everywhere it exists.
- The protocol is migrating from x402 v1 (55% of listings) to v2 (45%).
- The median price of an active listing is **$0.01**; the popular points are $0.001, $0.01, $0.05, $0.1. Everything above $1 per call is 286 listings, and it is almost always enrichment, managed research, or not an API at all but goods.

## The most interesting part: agents have started paying for actions, not data

Looking only at volumes, x402 is a data market. But the catalog's most telling listings are the ones where an agent's payment _does something_:

**Real commerce.** Bitrefill — a large gift card and eSIM seller — has put up a full x402 storefront: search across 10,000+ brands in 180+ countries, a price-locked invoice, payment under the upto scheme with a $1,000 ceiling in USDC, and redemption-code retrieval via the payer wallet's signature. Over a month: 62 paid invoices. This is a ready-made template for agent purchasing: search → detail → invoice → pay → redeem, without a single account. Next to it is jamton: 11 purchases of tokenized gold at $1,000 under the exact scheme — that is **$11 thousand in real payments, one and a half times more than the fees of the catalog's entire API segment over the same month**.

**Execution of on-chain operations.**`hibra.app/api/swap/execute` — the agent pays not for a quote but for execution of a swap along the best route on Base. 161 unique payers in a month — one of the catalog's highest organic figures, with almost no competitors.

**Orchestration.**`agents.chain.link` — execution of a Chainlink workflow by name: 22 thousand paid calls from literally a couple of clients. Infrastructure consumption at industrial volume, paid per call.

**Agent-to-agent payments.**`api.molty.cash` — "Tip or hire @0xmesuthere": 2,785 payments at $0.11 for hiring/tipping a specific agent. Agent-to-agent payment as a service.

**Renting compute.** Browserbase sells prepaid browser sessions for automation over x402 — clients come back an average of 50 times.

**Attestable data.** 169 listings are already tagged `attested` — signed responses (prices, volatility indices) that an agent can verify and pass along without trusting the transport. For agent-to-agent deals this is an obvious building block, and supply here still lags well behind the logic of demand.

This is a qualitative shift. "USDC for JSON data" is an understandable but cramped niche: data always has free substitutes. An _action_ — a purchase, a swap, a hire, a rental — has no substitute, and that is exactly where payment stops being a replacement for an API key and becomes the transaction itself.

## Where the catalog is empty

Matching demand (what gets searched and called) against supply, I see several clearly underserved niches:

- **Agent commerce beyond gift cards.** Bitrefill created the category single-handedly; the pattern carries over to tickets, hosting, domains, physical goods.
- **DeFi operation execution** — swaps, limit orders, bridges. One notable player in the whole catalog.
- **DeFi analytics** — health factor, liquidation candidates, vault risk. Six dozen listings mention these words in their keyword tails (providers are clearly betting on such queries), but almost nobody has built a product underneath them: live offerings number in the single digits, with single-digit payers.
- **Compliance primitives** — sanctions and AML screening of wallets: steady demand, almost no competition.
- **Portfolio analytics for an arbitrary wallet** — open PnL/tracking for any address is practically absent.
- **The mid price segment, $0.01–0.05** — the market is split between commodity at $0.001 and premium at $0.2+; composed, "ready-to-act" answers (screeners, rankings, risk passports) are nearly nonexistent in between.

Conversely, going now into micro-utilities like unit converters (kg↔pounds, degrees↔radians — one provider stamped out hundreds of such endpoints for semantic search), basic token prices, RPC wrappers, and "crypto news for $0.001" means competing with thousands of listings for zero demand.

## The sellers arrived before the buyers

Put the marketplace's two sides side by side and its main structural defect shows through. The selling side: ~15 thousand honest listings and nearly 1,500 domains. The buying side — after subtracting the farms — is not much bigger, and the regular buyers among them number in the hundreds: even the most popular organic service has just 261 unique payers a month. That works out to **roughly ten seller domains per real buyer**. This is an inverted marketplace: a listing costs one self-payment, while a buyer needs a wallet, a USDC budget, and a client integration — supply got there first and is waiting.

Through this lens, almost all the catalog's "diseases" turn out to be symptoms of a buyer shortage rather than problems in their own right:

- **Gaming the metric is only profitable in a thin market.** When the leaders have hundreds of organic payers, 500 fake wallets flip the ranking almost for free. Were there 10–100× more buyers, a farm would drown in the organic signal and lose its economic point.
- **The dead long tail** is not a verdict on the services: there physically aren't enough buyers for 15 thousand listings.
- **The empty mid price segment** — composed answers at $0.02–0.05 require mature demand, which doesn't exist yet: the market pays only for commodity and pinpoint premium.

Where the buyer shortage comes from: first, agents have no wallet and no budget by default — not one major agent framework ships an x402 client out of the box, and a human has to explicitly allocate funds. Second, there is no trust mechanism before payment: the catalog's metrics are gamed, and SLAs, refunds, and arbitration do not exist. Third, wherever price matters more than friction, x402 has no advantage: cheap data an agent will get for free, and expensive data a corporation will buy on contract with an invoice. The protocol wins exactly where friction costs more than money — which is why premium-API resellers, Twitter data, and managed search are the ones that live.

The strategic implication: the main growth lever for this market is not new sellers but everything that _creates buyers_: payment SDKs inside agent frameworks, default agent budgets, honest ranking you can trust. Whoever brings the buying side — the facilitator, a framework, or a marketplace — takes a disproportionate share of the market.

## The bottom line

1. **The x402 market is real, but tiny:** ~260 thousand paid calls, ~$7 thousand in API-call fees, and ~$19 thousand in agent purchases of goods per month on the largest facilitator. A 25-thousand-position catalog reduces to ~a hundred resources with meaningful demand and ~15 domains with a real business.
2. **Demand #1 is access to real-time information:** Twitter data and managed web search account for half of all calls. Willingness to pay peaks for people enrichment and managed research, not for crypto data.
3. **Half the catalog's metrics are fictional.** 58% of "unique payers" are wallet farms; a listing is created by a self-payment. The only public authenticity filter is the calls/payers ratio.
4. **The business models that work today:** hard-to-get data with high reuse, premium-API resale with friction removal (USDC instead of registration and a key), and — newly — a storefront for real goods.
5. **The direction of travel is visible to the naked eye:** from paying for data to paying for actions — purchases, transaction execution, hiring agents, renting compute. That is where x402 stops being "an API key without registration" and becomes the payment rail of the agent economy.
6. **The market is constrained by the buying side, not by supply:** ~10 seller domains per real buyer. Gamed metrics, the dead tail, and the empty mid price segment are symptoms of a buyer shortage; growing the buying side 10–100× would clear most of these problems automatically.

The market is early enough that entering the catalog's top 100 today costs a few dozen real clients a month. The window of opportunity is open — but, judging by the pace, not for long.

* * *

_Methodology: a full snapshot of the Coinbase CDP discovery catalog dated July 11, 2026 — 25,443 resources, which I pulled with paginated requests and verified against `pagination.total`. I assessed popularity by the `quality` block (unique payers and calls over a trailing 30 days), and revenue as the sum of "endpoint price × its calls," accounting for the payment scheme: in `exact` (99.96% of listings) the `amount` field is the exact payment amount and is taken at face value; in `upto` (11 listings, including Bitrefill invoice payments) it is only a maximum, so for those only an upper bound is given. For dynamically quoted exact endpoints the catalog stores the last indexed price, so their contribution is an approximation. Categorization I did by automated keyword tagging with manual verification of the top 100 listings._
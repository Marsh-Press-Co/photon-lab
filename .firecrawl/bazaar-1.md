https://medium.com/@heimlabs/ship-a-402-powered-api-bazaar-with-x402-from-discovery-to-paid-response-in-one-script-cf08f3853b05

[Sitemap](https://medium.com/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40heimlabs%2Fship-a-402-powered-api-bazaar-with-x402-from-discovery-to-paid-response-in-one-script-cf08f3853b05&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40heimlabs%2Fship-a-402-powered-api-bazaar-with-x402-from-discovery-to-paid-response-in-one-script-cf08f3853b05&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

[![HeimLabs](https://miro.medium.com/v2/resize:fill:40:40/0*dZpIe7R2Jv-mImzY)](https://medium.com/@heimlabs?source=post_page---post_author_sidebar--cf08f3853b05-----------------973d3738f84b----------------------)

## HeimLabs

Follow writer

Web3

Coinbase

X402

Api Marketplaces

Typescript

# Ship an x402-Powered API with Bazaar. From Discovery to Paid Response in One Script

[![HeimLabs](https://miro.medium.com/v2/da:true/resize:fill:32:32/0*dZpIe7R2Jv-mImzY)](https://medium.com/@heimlabs?source=post_page---byline--cf08f3853b05---------------------------------------)

[HeimLabs](https://medium.com/@heimlabs?source=post_page---byline--cf08f3853b05---------------------------------------)

Follow

7 min read

·

Oct 27, 2025

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dcf08f3853b05&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40heimlabs%2Fship-a-402-powered-api-bazaar-with-x402-from-discovery-to-paid-response-in-one-script-cf08f3853b05&source=---header_actions--cf08f3853b05---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*1EMbIVPXccpgncC6SpXtXw.png)

## Introduction

Most API marketplaces still assume a human is in the loop, create an account, add a card, mint keys, manage usage. That’s friction your **AI agent** can’t handle.

**Bazaar + x402** flips that model. Your agent discovers services, **gets an HTTP 402 (payment required) response with payment details**, pays (typically **USDC on Base**), retries the same request with proof, and the API responds — **no accounts, no subscriptions**.

By the end of this post, you’ll have a runnable demo that shows the end-to-end loop: **list → discover → 402 → pay → retry → use**.

## What You’ll Build

- 🧭 Publish a minimal **Bazaar**-style listing your agent can discover
- 💳 Simulate **x402** payment flow (HTTP 402 → facilitator settle → proof)
- 🔁 Retry the same request with proof to get the **paid** response
- 🧪 Do it all in **one Node.js script** you can run locally

(Watch the full video here)

## System Architecture

```
Agent (buyer) ──> Bazaar catalog ──> Service endpoint
    │                                   │
    │ (Request)                          │ If unpaid:
    │──────────────────────────────────> │  returns HTTP 402 + payment details
    │                                    │
    │ --pay via Facilitator------------> Facilitator (verifies/settles, returns proof)
    │                                    │
    │ (Retry + proof header)            │
    └──────────────────────────────────> │ Returns the result
```

**Components (quick tour)**

- **Bazaar**: Simple discovery layer returning listings with name, price, asset, network.
- **Service**: Your API endpoint that _requires pay-per-request_. If unpaid, it answers with **HTTP 402** and payment details.
- **x402 Facilitator**: Verifies/settles the client’s payment and issues a **proof** your service can trust.
- **Agent**: A tiny buyer script that discovers a service, calls it, handles 402, pays via facilitator, retries with proof, and prints the result.

## Implementation phase

The code will be split into two parts: **Seller** and **Buyer**.

## Project setup

```
mkdir x402-baazar
cd x402-baazar

npm init -y
```

## Install dependencies

```
npm i @coinbase/cdp-sdk @coinbase/x402 dotenv express viem x402-express x402-fetch
```

We’ll start by building a simple **Rock–Paper–Scissors** endpoint. Then, we’ll integrate it with **x402** so each request is payable, and provide the necessary config to list the service in **Baazar**. Create a file called index.js

## Setting up our endpoint with express

```
import express from “express”;

const moves = ["rock", "paper", "scissors"];
function getOutcome(player, server) {
 if (player === server) return "draw";
 if (
 (player === "rock" && server === "scissors") ||
 (player === "paper" && server === "rock") ||
 (player === "scissors" && server === "paper")
 ) {
 return "win";
 }
 return "lose";
}

const app = express();
app.use(express.json());

app.post("/rps/play", (req, res) => {
 try {
 const { move } = req.body;
 if(!move || !moves.includes(move)){
 res.status(400).send({ error: "Move must be rock, paper, or scissors" });
 return;
 }

const serverMove = moves[Math.floor(Math.random() * moves.length)];
const outcome = getOutcome(move, serverMove);

app.listen(4021, () => {
 console.log(`Server listening at http://localhost:4021`);
})
```

Now to set up x402 and the configs required for Baazar for the above endpoint

```
// … exisiting imports
import { paymentMiddleware } from “x402-express”;
import { facilitator } from “@coinbase/x402”;

// after `app.use(express.json())`

app.use(
 paymentMiddleware(
 "0xB1De43C2Ca1195258FEE160adAcB1820c3776B7D",
 {
 "POST /rps/play": {
 price: "$0.001", // USDC testnet price
 network: "base",
 config: {
 name: "Rock-Paper-Scissors",
 description: "Pay to play a simple game of Rock-Paper-Scissors.",
 discoverable: true, //
 inputSchema: {
 type: "object",
 properties: {
 move: {
 type: "string",
 enum: ["rock", "paper", "scissors"],
 description: "Your move",
 },
 },
 required: ["move"],
 },
 outputSchema: {
 type: "object",
 properties: {
 playerMove: { type: "string" },
 serverMove: { type: "string" },
 outcome: { type: "string" },
 },
 },
 },
 },
 },
 {
 facilitator
 }
 )
)

// before `app.post("/rps/play"…`
```

- The paymentMiddleware integrates **x402** into this project as an Express middleware (learn more about Express middlewares [here](https://expressjs.com/en/guide/using-middleware.html)).
- It takes two parameters:

1. **Recipient address** — the wallet where payments to this endpoint will be sent.
2. **Baazar config** — metadata that describes your service in the Baazar catalog, making it discoverable for AI agents.

- The discoverable flag in the config is set to true, which ensures your API is automatically listed in the Baazar catalog.

Note: To make your API indexable by Baazar, you must deploy it to a public cloud (e.g., [Railway](https://railway.app/), AWS, etc.) and ensure it’s accessible publicly

## Get HeimLabs’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

Remember me for faster sign in

Next, let’s create a simple function that simulates a **buyer**

- It queries the Baazar catalog to list available services.
- Selects our rock-paper-scissors service.
- Plays the game while paying **USDC** for each request.

Now create another file called buyer.js, and start with listing the catalog

```
const listCatalog = async () => {
const response = await fetch("https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources")
const res = await response.json()
console.log(res)

}

const run = async () => {
const catalog = await listCatalog();
}

run()
```

This will return an array of objects

```
{
 “items”: […]
}
```

Now that we have the service list, let’s set up a few prerequisites before making a call:

1. **Wallet setup** — We need a wallet to pay for the service. The quickest option is to use a **CDP wallet**, which abstracts all the complexities into just two lines of code. Alternatively, you can bring your own wallet, but then you’ll need to handle the full viem configuration yourself.
2. **Making the API call** — There are two approaches:

- Manually: call the API with fetch or axios, receive the 402 Payment Required response, make the payment, and then retry.
- Automatically: use the **CDP wrappers** for fetch or axios, which handle the entire payment flow for you.

For this walkthrough, we’ll wrap fetch with **x402-fetch**.

```
import { CdpClient } from “@coinbase/cdp-sdk”;
import dotenv from “dotenv”;
import { wrapFetchWithPayment, decodeXPaymentResponse } from “x402-fetch”;

dotenv.config()

// Setup CDP account or bring your own wallet
const cdp = new CdpClient();
const cdpAccount = await cdp.evm.getAccount({ name: “buyer-account”});

// feel free to enable this in testnet, perks for using CDP 😅
// await cdp.evm.requestFaucet({
// address: cdpAccount.address,
// network: “base-sepolia”,
// token: “usdc”
// });

// providing x402 super power to our good old `fetch`
const fetchWithPayment = wrapFetchWithPayment(fetch, cdpAccount);

// … previous listCatalog function

const run = async () => {
 try {
 const catalog = await listCatalog();

 // choosing a service, assuming that it’s our RPS API
 const service = catalog.items[0]
 const response = await fetchWithPayment(service.resource, {
 method: “POST”,
 headers: {
 “Content-Type”: “application/json”,
 },
 body: JSON.stringify({ move }),
 });

 const result = await response.json();
 console.log(“Game result:”, result);
 const paymentResponse = decodeXPaymentResponse(response.headers.get(“x-payment-response”));
 console.log(paymentResponse)
 } catch (error) {
 console.log(error);
 }
}

run()
```

Using **fetchWithPayment** ensures that whenever the API responds with a 402 Payment Required, the payment is handled automatically and the request is retried — so you get the result without needing to manage the payment flow yourself.

## Run the app

Seller

```
node index.ts
```

Buyer

```
node buyer.js
```

You’ll see:

1. The server start
2. The buyer discovering the service
3. The first call returning HTTP 402 with payment details
4. The testnet facilitator issuing a receipt
5. Then retry with X-PAYMENT header
6. The server responds back with a valid response

## Map the Demo to the Real Thing

- **Bazaar UI & Catalog**: In production, this is a hosted catalog with ratings, pricing, latency, and networks. Your agent chooses providers that match **budget + policy constraints**.
- **x402**: The pattern stays identical — **service answers unpaid with 402**, agent **settles** via a **facilitator**, then **retries** the exact same HTTP request with a **proof** header.
- **Facilitator**: In production you’d use **Coinbase’s default facilitator** for **USDC on Base** (or run your own / pick a community one). Its job: verify payment and issue a proof your service trusts.
- **Service**: Your API should treat 402 like a **contract**: be explicit about **amount, asset, network, seller, and facilitator URL**, then verify the facilitator’s proof on retry before returning data.

## Hardening & Extensions

- **Replay protection:** Bind proofs to `paymentRequestId` \+ method + path + query and expire quickly. Note: CDP facilitators are, by default, designed to handle this—providing a 60-second window to pay and retry
- **Tiered responses**: Offer free previews, charge for high-res/long runs.
- **Dynamic pricing**: Quote by **input size** (e.g., seconds of audio, tokens) inside the 402 body.
- **Provider switching**: Your agent can compare **rating/price/latency**, swap providers mid-workflow, and keep moving.
- **Onchain receipts**: Include tx hashes and facilitator attestations to anchor off-chain work to on-chain payments.

## **Recap**

You just ran a full, agent-friendly **Bazaar + x402** loop: **discover**, call and get **402 payment required status**, **pay** via a facilitator, **retry with proof**, and receive the **paid** result — no accounts, no subscriptions, **per-request**.

## **Next Steps**

- Swap the mock facilitator for **Coinbase’s default facilitator** on **Base USDC**.
- Add signature verification using your facilitator’s real public keys.
- Turn the catalog into a UI with ratings, price filters, and network badges.

## **CTA**

- Explore **Coinbase Developer Platform docs** for Bazaar/x402 and wallets.
- Follow **HeimLabs** for upcoming agent demos that chain providers (translate → analyze → summarize → TTS) with **pay-per-step** execution.

## Resources & Links

**Coinbase Developer Docs**:

[**Coinbase Developer Docs - Coinbase Developer Documentation** \\
\\
**Explore our API & SDK references, demos, and guides for building onchain apps.**\\
\\
docs.cdp.coinbase.com](https://docs.cdp.coinbase.com/?source=post_page-----cf08f3853b05---------------------------------------)

**x402:**

[**x402.org** \\
\\
**An open standard for internet-native payments**\\
\\
www.x402.org](https://www.x402.org/?source=post_page-----cf08f3853b05---------------------------------------)

**HeimLabs:**

[**HeimLabs \| Trusted Blockchain Solutions Provider** \\
\\
**Revolutionize your business with HeimLabs' blockchain development solutions. Our expert team offers end-to-end services…**\\
\\
www.heimlabs.com](https://www.heimlabs.com/?source=post_page-----cf08f3853b05---------------------------------------)

**Clap if this saved you hours, and share what you’re building with the CDP stack!**

**Follow HeimLabs** for unapologetically practical Web3 dev content.

[Twitter](https://x.com/heimlabs), [LinkedIn](https://www.linkedin.com/company/heimlabs).

Happy Building 🚀

Web3

Coinbase

X402

Api Marketplaces

Typescript

[![HeimLabs](https://miro.medium.com/v2/resize:fill:48:48/0*dZpIe7R2Jv-mImzY)](https://medium.com/@heimlabs?source=post_page---post_author_info--cf08f3853b05---------------------------------------)

[![HeimLabs](https://miro.medium.com/v2/resize:fill:64:64/0*dZpIe7R2Jv-mImzY)](https://medium.com/@heimlabs?source=post_page---post_author_info--cf08f3853b05---------------------------------------)

Follow

[**Written by HeimLabs**](https://medium.com/@heimlabs?source=post_page---post_author_info--cf08f3853b05---------------------------------------)

[21 followers](https://medium.com/@heimlabs/followers?source=post_page---post_author_info--cf08f3853b05---------------------------------------)

· [1 following](https://medium.com/@heimlabs/following?source=post_page---post_author_info--cf08f3853b05---------------------------------------)

Follow

[Help](https://help.medium.com/hc/en-us?source=post_page-----cf08f3853b05---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----cf08f3853b05---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----cf08f3853b05---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----cf08f3853b05---------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----cf08f3853b05---------------------------------------)

[Store](https://medium.com/store)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----cf08f3853b05---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----cf08f3853b05---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----cf08f3853b05---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----cf08f3853b05---------------------------------------)
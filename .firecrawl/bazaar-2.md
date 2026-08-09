https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-connect-bazaar.html

## Select your cookie preferences

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies.

If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

AcceptDeclineCustomize

## Customize cookie preferences

We use cookies and similar tools (collectively, "cookies") for the following purposes.

### Essential

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Allowed

### Performance

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Allowed

### Functional

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Allowed

### Advertising

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Allowed

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

CancelSave preferences

## Your privacy choices

We and our advertising partners (“we”) may use information we collect from or about you to show you ads on other websites and online services. Under certain laws, this activity is referred to as “cross-context behavioral advertising” or “targeted advertising.”

To opt out of our use of cookies or similar technologies to engage in these activities, select “Opt out of cross-context behavioral ads” and “Save preferences” below. If you clear your browser cookies or visit this site from a different device or browser, you will need to make your selection again. For more information about cookies and how we use them, read our [Cookie Notice](https://aws.amazon.com/legal/cookies/).

Allow cross-context behavioral adsOpt out of cross-context behavioral ads

To opt out of the use of other identifiers, such as contact information, for these activities, fill out the form [here](https://pulse.aws/application/ZRPLWLL6?p=0).

For more information about how AWS handles your information, read the [AWS Privacy Notice](https://aws.amazon.com/privacy/).

CancelSave preferences

## Unable to save cookie preferences

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

Dismiss

# Coinbase Bazaar via AgentCore Gateway

[PDF](https://docs.aws.amazon.com/pdfs/bedrock-agentcore/latest/devguide/bedrock-agentcore-dg.pdf#payments-connect-bazaar)

[RSS](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/bedrock-agentcore-dg.rss)

[Markdown](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-connect-bazaar.md "Download Markdown")

Focus mode

Coinbase Bazaar via AgentCore Gateway - Amazon Bedrock AgentCore

[Open PDF](https://docs.aws.amazon.com/pdfs/bedrock-agentcore/latest/devguide/bedrock-agentcore-dg.pdf#payments-connect-bazaar "Open PDF")

[Add Coinbase x402 Bazaar MCP server to a Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-connect-bazaar.html#_add_coinbase_x402_bazaar_mcp_server_to_a_gateway)

AgentCore Gateway lets you connect to paid MCP servers and API endpoints. You can add the Coinbase x402 Bazaar MCP server as a target in a Gateway to discover 10,000+ existing paid MCP tools that support x402 microtransactions.

- Server URL — `https://api.cdp.coinbase.com/platform/v2/x402/discovery/mcp`

- Outbound authentication types accepted — No Authorization (default)


## Add Coinbase x402 Bazaar MCP server to a Gateway

###### Example

Console

1. Navigate to the **Target** section.

2. (Optional) Change the generated **Target name**.

3. (Optional) Provide a **Target description**.

4. For **Target type**, choose **Integrations**.

5. Select **Coinbase x402 Bazaar**.

6. Skip **Outbound Auth configurations**. "No Authorization" is the only supported option and is selected by default.


AgentCore CLI

```

agentcore add gateway-target \
  --name CoinbaseTarget \
  --type mcp-server \
  --endpoint https://api.cdp.coinbase.com/platform/v2/x402/discovery/mcp \
  --gateway MyGateway

agentcore deploy
```

AWS SDK

```

import boto3

agentcore_client = boto3.client('bedrock-agentcore-control')

target = agentcore_client.create_gateway_target(
    gatewayIdentifier="your-gateway-id",
    name="Coinbasex402BazaarTarget",
    description="Coinbase x402 Bazaar MCP server for paid API discovery",
    targetConfiguration={
        "mcp": {
            "mcpServer": {
                "endpoint": "https://api.cdp.coinbase.com/platform/v2/x402/discovery/mcp"
            }
        }
    }
)
```

Strands SDK

Use the Coinbase x402 Bazaar Gateway Target with your agent:

```

from strands import Agent
from strands.models import BedrockModel
from strands.tools.mcp.mcp_client import MCPClient
from mcp.client.streamable_http import streamablehttp_client
from bedrock_agentcore.payments.integrations.config import AgentCorePaymentsPluginConfig
from bedrock_agentcore.payments.integrations.strands.plugin import AgentCorePaymentsPlugin

GATEWAY_URL = "https://<your-gateway-id>.gateway.bedrock-agentcore.<region>.amazonaws.com/mcp"
ACCESS_TOKEN = "<your-inbound-auth-token>"

mcp_client = MCPClient(
    lambda: streamablehttp_client(GATEWAY_URL, headers={"Authorization": f"Bearer {ACCESS_TOKEN}"})
)

# Configure the Payment plugin
config = AgentCorePaymentsPluginConfig(
    payment_manager_arn="arn:aws:bedrock-agentcore:us-west-2:123456789012:payment-manager/pm-abc123",
    user_id="test-user-123",
    payment_instrument_id="payment-instrument-XJU4RSQP9VO0ler",
    payment_session_id="payment-session-xuzrnUCd7RT725G",
    region="us-west-2",
)

# Create the plugin
plugin = AgentCorePaymentsPlugin(config=config)

with mcp_client:
    tools = mcp_client.list_tools_sync()
    agent = Agent(
        model=BedrockModel(inference_profile_id="us.anthropic.claude-sonnet-4-20250514-v1:0", streaming=True),
        tools=tools,
        plugins=[plugin],  # enables automatic payments
    )
    response = agent("Search for available x402 paid APIs related to weather data")
    print(response)
```

LangGraph

Use the Coinbase x402 Bazaar Gateway Target with your LangGraph agent:

```

import asyncio
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from bedrock_agentcore.payments.integrations.langgraph import (
    AgentCorePaymentsConfig,
    AgentCorePaymentsMiddleware,
)

GATEWAY_URL = "https://<your-gateway-id>.gateway.bedrock-agentcore.<region>.amazonaws.com/mcp"
ACCESS_TOKEN = "<your-inbound-auth-token>"

async def main():
    client = MultiServerMCPClient({
        "bazaar": {
            "transport": "streamable_http",
            "url": GATEWAY_URL,
            "headers": {"Authorization": f"Bearer {ACCESS_TOKEN}"},
        }
    })
    mcp_tools = await client.get_tools()

    config = AgentCorePaymentsConfig(
        payment_manager_arn="arn:aws:bedrock-agentcore:us-west-2:123456789012:payment-manager/pm-abc123",
        user_id="test-user-123",
        payment_instrument_id="payment-instrument-XJU4RSQP9VO0ler",
        region="us-west-2",
        auto_session=True,
    )

    payments = AgentCorePaymentsMiddleware(config)

    agent = create_agent(
        model=ChatOpenAI(model="gpt-4o-mini"),
        tools=mcp_tools,
        middleware=[payments],
    )

    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "Search for available x402 paid APIs related to weather data"}]}
    )
    print(result["messages"][-1].content)

asyncio.run(main())
```

anchoranchoranchoranchoranchor

- Console

- AgentCore CLI

- AWS SDK

- Strands SDK

- LangGraph


1. Navigate to the **Target** section.

2. (Optional) Change the generated **Target name**.

3. (Optional) Provide a **Target description**.

4. For **Target type**, choose **Integrations**.

5. Select **Coinbase x402 Bazaar**.

6. Skip **Outbound Auth configurations**. "No Authorization" is the only supported option and is selected by default.


Once the Bazaar target is configured, your agents can discover and call paid x402 endpoints through the Gateway. When an endpoint returns HTTP 402, AgentCore payments handles the payment flow automatically if you have configured a payments plugin (Strands) or middleware (LangGraph) in your agent. To learn more, see [Framework integrations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-framework-integrations.html).

To set up the Payment Manager and Connector required for processing payments, see [Create a Payment Manager and Connector](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-create-manager.html).

[Document Conventions](https://docs.aws.amazon.com/general/latest/gr/docconventions.html)

Create a session

Process Payment

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

- ### On this page

- Did this page help you?








Yes



No













[Provide feedback](https://docs.aws.amazon.com/feedback/doc-feedback.html?hidden_service_name=bedrock-agentcore&topic_url=https%3A%2F%2Fdocs.aws.amazon.com%2Fbedrock-agentcore%2Flatest%2Fdevguide%2Fpayments-connect-bazaar.html)


#### Next topic:

[Process Payment](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-process-payment.html)

#### Previous topic:

[Create a session](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-create-session.html)
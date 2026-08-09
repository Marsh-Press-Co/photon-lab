> ## Documentation Index
>
> Fetch the complete documentation index at: [/llms.txt](https://docs.cdp.coinbase.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](https://docs.cdp.coinbase.com/api-reference/v2/rest-api/x402-facilitator/list-x402-resources#content-area)

[Coinbase Developer Documentation home page![light logo](https://mintcdn.com/coinbase-prod/B68gj-lD9xkJGij4/logos/wordmark-light.svg?fit=max&auto=format&n=B68gj-lD9xkJGij4&q=85&s=0eb5640aeec58541851e1cba9c6ccc8b)![dark logo](https://mintcdn.com/coinbase-prod/B68gj-lD9xkJGij4/logos/wordmark-dark.svg?fit=max&auto=format&n=B68gj-lD9xkJGij4&q=85&s=53721303b967eaae0304eee4d72b76a4)](https://docs.cdp.coinbase.com/)

Search...

Ctrl KAsk Assistant

- [Get help](https://discord.com/invite/cdp)
- [Dev portal](https://portal.cdp.coinbase.com/)
- [Dev portal](https://portal.cdp.coinbase.com/)

Search...

Navigation

x402 Facilitator

List x402 resources

[Docs](https://docs.cdp.coinbase.com/) [API Reference](https://docs.cdp.coinbase.com/api-reference/v2/introduction) [SDKs](https://docs.cdp.coinbase.com/sdks) [Recipes](https://docs.cdp.coinbase.com/get-started/demo-apps/learn) [Changelogs](https://docs.cdp.coinbase.com/get-started/changelog)

![](https://mintlify-assets.b-cdn.net/developerSDKNavigation-0.svg)

CDP API

### CDP API

- [Overview](https://docs.cdp.coinbase.com/api-reference/v2/introduction)
- [Authentication](https://docs.cdp.coinbase.com/api-reference/v2/authentication)
- [Conventions](https://docs.cdp.coinbase.com/api-reference/v2/conventions)
- [Pagination](https://docs.cdp.coinbase.com/api-reference/v2/pagination)
- [Idempotency](https://docs.cdp.coinbase.com/api-reference/v2/idempotency)
- [Rate Limits](https://docs.cdp.coinbase.com/api-reference/v2/rate-limits)
- [Errors](https://docs.cdp.coinbase.com/api-reference/v2/errors)
- [OpenAPI Spec](https://docs.cdp.coinbase.com/api-reference/v2/cdp-api-v2.yaml)
- [Troubleshooting](https://docs.cdp.coinbase.com/api-reference/v2/troubleshooting)

### REST API

- Wallets

- Payments



  - Acceptance

  - Deposit DestinationsBeta

  - Payment MethodsBeta

  - TransfersBeta

  - Onramp

  - x402 FacilitatorBeta



    - [Overview](https://docs.cdp.coinbase.com/api-reference/v2/rest-api/x402-facilitator/x402-facilitator)
    - [GET\\
      \\
      Get supported payment schemes and networks](https://docs.cdp.coinbase.com/api-reference/v2/rest-api/x402-facilitator/get-supported-payment-schemes-and-networks)
    - [GET\\
      \\
      List merchant discovery info](https://docs.cdp.coinbase.com/api-reference/v2/rest-api/x402-facilitator/list-merchant-discovery-info)
    - [GET\\
      \\
      List x402 resources](https://docs.cdp.coinbase.com/api-reference/v2/rest-api/x402-facilitator/list-x402-resources)
    - [GET\\
      \\
      Search x402 resources](https://docs.cdp.coinbase.com/api-reference/v2/rest-api/x402-facilitator/search-x402-resources)
    - [POST\\
      \\
      Handle MCP JSON-RPC request](https://docs.cdp.coinbase.com/api-reference/v2/rest-api/x402-facilitator/handle-mcp-json-rpc-request)
    - [POST\\
      \\
      Settle payment](https://docs.cdp.coinbase.com/api-reference/v2/rest-api/x402-facilitator/settle-payment)
    - [POST\\
      \\
      Validate x402 endpoint](https://docs.cdp.coinbase.com/api-reference/v2/rest-api/x402-facilitator/validate-x402-endpoint)
    - [POST\\
      \\
      Verify payment](https://docs.cdp.coinbase.com/api-reference/v2/rest-api/x402-facilitator/verify-payment)
- Trading

- Onchain Tools

- CustomersBeta

- Webhooks


List x402 resources

cURL

```
curl --request GET \
  --url 'https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources?limit=100' \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources?limit=100"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources?limit=100', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [\
  CURLOPT_URL => "https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources?limit=100",\
  CURLOPT_RETURNTRANSFER => true,\
  CURLOPT_ENCODING => "",\
  CURLOPT_MAXREDIRS => 10,\
  CURLOPT_TIMEOUT => 30,\
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,\
  CURLOPT_CUSTOMREQUEST => "GET",\
  CURLOPT_HTTPHEADER => [\
    "Authorization: Bearer <token>"\
  ],\
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```

```
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources?limit=100"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources?limit=100")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources?limit=100")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

200

400

500

502

503

```
{
  "x402Version": 2,
  "items": [\
    {\
      "resource": "https://api.example.com/weather/forecast",\
      "description": "Real-time weather forecast data.",\
      "type": "http",\
      "x402Version": 2,\
      "lastUpdated": "2024-01-15T10:30:00Z",\
      "accepts": [\
        {\
          "scheme": "exact",\
          "network": "eip155:8453",\
          "amount": "1000000",\
          "payTo": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",\
          "asset": "0x036CbD53842c5426634e7929541eC2318f3dCF7e",\
          "maxTimeoutSeconds": 60\
        }\
      ],\
      "extensions": {\
        "bazaar": {\
          "info": {\
            "input": {\
              "type": "http",\
              "method": "GET"\
            }\
          },\
          "schema": {}\
        }\
      },\
      "quality": {\
        "l30DaysTotalCalls": 42,\
        "l30DaysUniquePayers": 15,\
        "lastCalledAt": "2024-01-15T10:30:00Z"\
      },\
      "serviceName": "Weather API",\
      "tags": [\
        "weather",\
        "data"\
      ],\
      "iconUrl": "https://res.cloudinary.com/bdb-prod/image/upload/...",\
      "curated": true,\
      "skillUrl": "https://skills.cdp.coinbase.com/weather-api/SKILL.md"\
    }\
  ],
  "pagination": {
    "limit": 100,
    "offset": 0,
    "total": 1000
  }
}
```

```
{
  "errorType": "invalid_request",
  "errorMessage": "Invalid request. Please check the request parameters."
}
```

```
{
  "errorType": "internal_server_error",
  "errorMessage": "An internal server error occurred. Please try again later."
}
```

```
{
  "errorType": "bad_gateway",
  "errorMessage": "Bad gateway. Please try again later."
}
```

```
{
  "errorType": "service_unavailable",
  "errorMessage": "Service unavailable. Please try again later."
}
```

x402 Facilitator

# List x402 resources

Copy pageCopy page

Lists all active discovered x402 resources.
This endpoint returns resources that have been discovered and cached by the x402 facilitator, including their payment requirements and metadata.
The response is paginated, and by default, returns 100 items per page.

Copy pageCopy page

GET

/

v2

/

x402

/

discovery

/

resources

Try it

List x402 resources

cURL

```
curl --request GET \
  --url 'https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources?limit=100' \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources?limit=100"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources?limit=100', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [\
  CURLOPT_URL => "https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources?limit=100",\
  CURLOPT_RETURNTRANSFER => true,\
  CURLOPT_ENCODING => "",\
  CURLOPT_MAXREDIRS => 10,\
  CURLOPT_TIMEOUT => 30,\
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,\
  CURLOPT_CUSTOMREQUEST => "GET",\
  CURLOPT_HTTPHEADER => [\
    "Authorization: Bearer <token>"\
  ],\
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```

```
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources?limit=100"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources?limit=100")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources?limit=100")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

200

400

500

502

503

```
{
  "x402Version": 2,
  "items": [\
    {\
      "resource": "https://api.example.com/weather/forecast",\
      "description": "Real-time weather forecast data.",\
      "type": "http",\
      "x402Version": 2,\
      "lastUpdated": "2024-01-15T10:30:00Z",\
      "accepts": [\
        {\
          "scheme": "exact",\
          "network": "eip155:8453",\
          "amount": "1000000",\
          "payTo": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",\
          "asset": "0x036CbD53842c5426634e7929541eC2318f3dCF7e",\
          "maxTimeoutSeconds": 60\
        }\
      ],\
      "extensions": {\
        "bazaar": {\
          "info": {\
            "input": {\
              "type": "http",\
              "method": "GET"\
            }\
          },\
          "schema": {}\
        }\
      },\
      "quality": {\
        "l30DaysTotalCalls": 42,\
        "l30DaysUniquePayers": 15,\
        "lastCalledAt": "2024-01-15T10:30:00Z"\
      },\
      "serviceName": "Weather API",\
      "tags": [\
        "weather",\
        "data"\
      ],\
      "iconUrl": "https://res.cloudinary.com/bdb-prod/image/upload/...",\
      "curated": true,\
      "skillUrl": "https://skills.cdp.coinbase.com/weather-api/SKILL.md"\
    }\
  ],
  "pagination": {
    "limit": 100,
    "offset": 0,
    "total": 1000
  }
}
```

```
{
  "errorType": "invalid_request",
  "errorMessage": "Invalid request. Please check the request parameters."
}
```

```
{
  "errorType": "internal_server_error",
  "errorMessage": "An internal server error occurred. Please try again later."
}
```

```
{
  "errorType": "bad_gateway",
  "errorMessage": "Bad gateway. Please try again later."
}
```

```
{
  "errorType": "service_unavailable",
  "errorMessage": "Service unavailable. Please try again later."
}
```

#### Query Parameters

[​](https://docs.cdp.coinbase.com/api-reference/v2/rest-api/x402-facilitator/list-x402-resources#parameter-type)

type

string

Filter by protocol type (e.g., "http", "mcp").
Currently, the only supported protocol type is "http".

Example:

`"http"`

[​](https://docs.cdp.coinbase.com/api-reference/v2/rest-api/x402-facilitator/list-x402-resources#parameter-limit)

limit

integer

default:100

The number of discovered x402 resources to return per page.

[​](https://docs.cdp.coinbase.com/api-reference/v2/rest-api/x402-facilitator/list-x402-resources#parameter-offset)

offset

integer

default:0

The offset of the first discovered x402 resource to return.

#### Response

200

application/json

Successfully retrieved discovery list.

Response containing discovered x402 resources.

[​](https://docs.cdp.coinbase.com/api-reference/v2/rest-api/x402-facilitator/list-x402-resources#response-x402-version)

x402Version

enum<integer>

required

The version of the x402 protocol.

Available options:

`1`,

`2`

Example:

`2`

[​](https://docs.cdp.coinbase.com/api-reference/v2/rest-api/x402-facilitator/list-x402-resources#response-items)

items

object\[\]

required

List of discovered x402 resources.

Showchild attributes

Example:

```
[\
  {\
    "resource": "https://api.example.com/weather/forecast",\
    "description": "Real-time weather forecast data.",\
    "type": "http",\
    "x402Version": 2,\
    "lastUpdated": "2024-01-15T10:30:00Z",\
    "accepts": [\
      {\
        "scheme": "exact",\
        "network": "eip155:8453",\
        "amount": "1000000",\
        "payTo": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",\
        "asset": "0x036CbD53842c5426634e7929541eC2318f3dCF7e",\
        "maxTimeoutSeconds": 60\
      }\
    ],\
    "extensions": {\
      "bazaar": {\
        "info": {\
          "input": { "type": "http", "method": "GET" }\
        },\
        "schema": {}\
      }\
    },\
    "quality": {\
      "l30DaysTotalCalls": 42,\
      "l30DaysUniquePayers": 15,\
      "lastCalledAt": "2024-01-15T10:30:00Z"\
    },\
    "serviceName": "Weather API",\
    "tags": ["weather", "data"],\
    "iconUrl": "https://res.cloudinary.com/bdb-prod/image/upload/...",\
    "curated": true,\
    "skillUrl": "https://skills.cdp.coinbase.com/weather-api/SKILL.md"\
  }\
]
```

[​](https://docs.cdp.coinbase.com/api-reference/v2/rest-api/x402-facilitator/list-x402-resources#response-pagination)

pagination

object

required

Pagination information for the response.

Showchild attributes

Example:

```
{ "limit": 100, "offset": 0, "total": 1000 }
```

Was this page helpful?

YesNo

[List merchant discovery info\\
\\
Previous](https://docs.cdp.coinbase.com/api-reference/v2/rest-api/x402-facilitator/list-merchant-discovery-info) [Search x402 resources\\
\\
Next](https://docs.cdp.coinbase.com/api-reference/v2/rest-api/x402-facilitator/search-x402-resources)

Ctrl+I

[Coinbase Developer Documentation home page![light logo](https://mintcdn.com/coinbase-prod/B68gj-lD9xkJGij4/logos/wordmark-light.svg?fit=max&auto=format&n=B68gj-lD9xkJGij4&q=85&s=0eb5640aeec58541851e1cba9c6ccc8b)![dark logo](https://mintcdn.com/coinbase-prod/B68gj-lD9xkJGij4/logos/wordmark-dark.svg?fit=max&auto=format&n=B68gj-lD9xkJGij4&q=85&s=53721303b967eaae0304eee4d72b76a4)](https://docs.cdp.coinbase.com/)

[x](https://x.com/coinbasedev) [github](https://github.com/coinbase) [linkedin](https://www.linkedin.com/company/coinbasedeveloperplatform)

[Join CDP Discord](https://discord.com/invite/cdp) [Status](https://cdpstatus.coinbase.com/) [Privacy Policy](https://www.coinbase.com/legal/privacy)

[x](https://x.com/coinbasedev) [github](https://github.com/coinbase) [linkedin](https://www.linkedin.com/company/coinbasedeveloperplatform)

[x](https://x.com/coinbasedev) [github](https://github.com/coinbase) [linkedin](https://www.linkedin.com/company/coinbasedeveloperplatform)

Assistant

This is an AI generated summary and may contain mistakes. It is not intended to give advice, including legal, financial or tax advice. It does not have access to your account information. By using this AI-assistant, you agree to the [CDP ToS](https://www.coinbase.com/legal/developer-platform/terms-of-service).
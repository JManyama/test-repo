---
title: SAP Concur Authentication v0.1
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2
generator: widdershins v4.0.1

---

<h1 id="sap-concur-authentication">SAP Concur Authentication v0.1</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

This specification describes how the OAuth2/token endpoints are
implemented by the SAP Concur service provider.

The endpoint in this specification is derived from a number of RFCs and
external documents:

  * The OAuth2 framework - [RFC 6749][rfc6749]
  * Proof of Key Code Exchange extension for OAuth2 - [RFC 7636][rfc7636]

The US production APIs can be found at `https://us.api.concursolutions.com/oauth2/token`.

[rfc6749]: https://tools.ietf.org/html/rfc6749
[rfc7636]: https://tools.ietf.org/html/rfc7636

Base URLs:

* <a href="https://www.concursolutions.com/oauth2/token">https://www.concursolutions.com/oauth2/token</a>

# Authentication

- oAuth2 authentication. To use this API, you need to get OAuth client credentials (client ID, secret, and geolocation) from SAP Concur, and be authorized to use the relevant scope. Refer to the <a href="https://developer.concur.com/api-reference/authentication/getting-started.html">full authentication information</a> for more information.

    - Flow: clientCredentials

    - Token URL = [https://us.api.concursolutions.com/oauth2/v0](https://us.api.concursolutions.com/oauth2/v0)

<h1 id="sap-concur-authentication-token-management">Token Management</h1>

Get access tokens and refresh tokens.

## oauth2Token

<a id="opIdoauth2Token"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://www.concursolutions.com/oauth2/token/token \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```http
POST https://www.concursolutions.com/oauth2/token/token HTTP/1.1
Host: www.concursolutions.com
Content-Type: application/x-www-form-urlencoded
Accept: application/json

```

```javascript
const inputBody = '{
  "body": "string"
}';
const headers = {
  'Content-Type':'application/x-www-form-urlencoded',
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('https://www.concursolutions.com/oauth2/token/token',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/x-www-form-urlencoded',
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.post 'https://www.concursolutions.com/oauth2/token/token',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://www.concursolutions.com/oauth2/token/token', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/x-www-form-urlencoded',
    'Accept' => 'application/json',
    'Authorization' => 'Bearer {access-token}',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://www.concursolutions.com/oauth2/token/token', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("https://www.concursolutions.com/oauth2/token/token");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/x-www-form-urlencoded"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://www.concursolutions.com/oauth2/token/token", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /token`

*Request a new access token.*

The token endpoint, as described in [RFC 6749 Â§3.2], used in four cases:
 * [Password Grant][RFC 6749 Â§4.3]
   * The Password grant can be used when there is a trust relationship between the user and the application. There are two credential types allowed with Password Grant:
     * <b>Password:</b> with this credential type, the application either already has the user’s credentials or can obtain the user’s credentials by directly interacting with the user.
     * <b>AuthToken:</b> This credential type is used for connections from the App Center. For App Center partners and TripLink suppliers, please refer to the [certification documentation][Cert Docs] for more information.
    * Properties:
      * <b>client_id:</b> (Required) <i>String</i> - The client_id of the application.
      * <b>client_secret:</b> (Required) <i>String</i> - The client_secret of the application.
      * <b>grant_type:</b> (Required) <i>String</i> - The credential types allowed with Password Grant.
      * <b>username:</b> (Required) <i>String</i> - The username of the user being authenticated.
      * <b>password:</b> (Required) <i>String</i> - The password of the user being authenticated.
      * <b>cred_type:</b> <i>String</i> - The credential set being submitted in the request, either <i>authtoken</i> or <i>password</i>. For password requests, use <i>password</i>. For connections with the App Center, use <i>authtoken</i>. If omitted, the default is <i>password</i>.
      * <b>scope:</b> <i>String</i> - The scope of the requested access token. This can be used to restrict the new access token to a subset of the scope allowed to the client and token type.
 * [Client Credentials Grant][RFC 6749 Â§4.4]
   * The Client Credentials grant enables an application to get an access token allowing only app-specific operations.
   * Properties:
      * <b>client_id:</b> (Required) <i>String</i> - The client_id of the application.
      * <b>client_secret:</b> (Required) <i>String</i> - The client_secret of the application.
      * <b>grant_type:</b> (Required) <i>String</i> - The credential types allowed with Password Grant.
 * [Token Refresh Grant][RFC 6749 Â§6]
   * The refresh grant is used to refresh an access_token that has expired. This grant can be used anytime a refresh_token is returned in the response of another grant request. No user interaction is required.
   * Properties:
      * <b>client_id:</b> (Required) <i>String</i> - The client_id of the application.
      * <b>client_secret:</b> (Required) <i>String</i> - The client_secret of the application.
      * <b>grant_type:</b> (Required) <i>String</i> - The credential types allowed with Password Grant.
      * <b>refresh_token:</b> (Required) <i>String</i> - An existing valid refresh token to be used to request a new access token.
      * <b>scope:</b> <i>String</i> - The scope of the requested access token. This can be used to restrict the new access token to a subset of the scope allowed to the client and token type.
 * [One Time Password Grant][RFC 6749 Â§4.1]
   * The One-time Password grant type leverages email, phone (text messaging), instant messaging and similar systems to provide per user access tokens to client applications. This grant type requires the following steps:
     * The calling application calls the OAuth2 service specifying the otp grant type along with required parameters.
     * The OAuth2 service generates a one time token which it sends through the messaging mechanism chosen by the application.
     * The user retrieves the token and presents it to the application. The means of having this presented to the application is the responsibility of the application.
     * The application presents this one-time token to the OAuth2 service via the token endpoint.  <b>It is only this step that is covered by this documentation.</b>
    * Properties:
      * <b>client_id:</b> (Required) <i>String</i> - The client_id of the application.
      * <b>client_secret:</b> (Required) <i>String</i> - The client_secret of the application.
      * <b>grant_type:</b> (Required) <i>String</i> - The credential types allowed with Password Grant.
      * <b>channel_handle:</b> (Required) <i>String</i> - The location (email address, phone number) where the one time token should be sent.  Currently only email addresses are allowed.
      * <b>channel_type:</b> (Required) <i>String</i> - The type of messaging system to use. Currently only <i>email</i> is allowed.
      * <b>otp:</b> (Required) <i>String</i> - The one-time token.
      * <b>scope:</b> <i>String</i> - The scope of the requested access token. This can be used to restrict the new access token to a subset of the scope allowed to the client and token type.

Access Tokens have a one hour lifetime.  If the access token expires, the client application must use a Refresh Grant to obtain a new access token.

Refresh Tokens have a six month lifetime. If the refresh token expires, the client application must reinitiate the authorization process. When a refresh token is used to request a new access token, both a new access token as well as a new refresh token are returned in the response. This token can change even if most of the time, this value is the same. Client applications should treat all returned refresh tokens as new tokens and overwrite the stored tokens with the new token from the response.

 [RFC 6749 Â§3.2]: https://tools.ietf.org/html/rfc6749#section-3.2
 [RFC 6749 Â§4.1]: https://tools.ietf.org/html/rfc6749#section-4.1
 [RFC 6749 Â§4.3]: https://tools.ietf.org/html/rfc6749#section-4.3
 [RFC 6749 Â§4.4]: https://tools.ietf.org/html/rfc6749#section-4.4
 [RFC 7636 Â§4.5]: https://tools.ietf.org/html/rfc7636#section-4.3
 [RFC 6749 Â§6]: https://tools.ietf.org/html/rfc6749#section-6
 [Cert Docs]: https://developer.concur.com/manage-apps/app-certification.html

> Body parameter

```yaml
body: string

```

<h3 id="oauth2token-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» body|body|string|true|* <b>Password Grant Example:</b>|

#### Detailed descriptions

**» body**: * <b>Password Grant Example:</b>
client_id=000000000000000000000000000000000000&client_secret=111111111111111111111111111111111111&grant_type=password&username={name of user}&password={password of user}&credtype=password
* <b>Client Credentials Grant Example:</b>
client_id=000000000000000000000000000000000000&client_secret=111111111111111111111111111111111111&grant_type=client_credentials
* <b>Token Refresh Example:</b>
client_id=000000000000000000000000000000000000&client_secret=111111111111111111111111111111111111&grant_type=refresh_token&refresh_token=333333333333333333333333333333333333
* <b>One Time Password Grant Example:</b>
client_id=000000000000000000000000000000000000&client_secret=111111111111111111111111111111111111&grant_type=otp&otp=222222222222222222222222222222222222&channel_handle={email address of user}&channel_type=email

> Example responses

> 200 Response

```json
{
  "access_token": "string",
  "token_type": "bearer",
  "expires_in": "3600",
  "refresh_token": "string",
  "scope": "string",
  "idtoken": "string",
  "geolocation": "https://us.api.concursolutions.com"
}
```

<h3 id="oauth2token-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|New access token generated successfully|[TokenResponse](#schematokenresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|[TokenErrorResponse](#schematokenerrorresponse)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[TokenErrorResponse](#schematokenerrorresponse)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[TokenErrorResponse](#schematokenerrorresponse)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[TokenErrorResponse](#schematokenerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2
</aside>

# Schemas

<h2 id="tocS_TokenResponse">TokenResponse</h2>

<a id="schematokenresponse"></a>
<a id="schema_TokenResponse"></a>
<a id="tocStokenresponse"></a>
<a id="tocstokenresponse"></a>

```json
{
  "access_token": "string",
  "token_type": "bearer",
  "expires_in": "3600",
  "refresh_token": "string",
  "scope": "string",
  "idtoken": "string",
  "geolocation": "https://us.api.concursolutions.com"
}

```

TokenResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|access_token|string|false|none|The newly-obtained access token.|
|token_type|[TokenType](#schematokentype)|false|none|The type of the token. Currently only bearer tokens are emitted.|
|expires_in|string|false|none|The lifetime of the access token, in seconds.|
|refresh_token|string|false|none|The refresh token to use, for a refresh token request.|
|scope|string|false|none|The effective scope of the newly-obtained token.|
|idtoken|string|false|none|The id token associated with the access token.  This is a parsable JSON document that includes the id-related fields of the access token.|
|geolocation|string|false|none|The base URL for where the user profile lives. The token’s geolocation should be stored along with the token. The application should make subsequent calls using the token and the correct end points based on the token’s geolocation.|

<h2 id="tocS_TokenErrorResponse">TokenErrorResponse</h2>

<a id="schematokenerrorresponse"></a>
<a id="schema_TokenErrorResponse"></a>
<a id="tocStokenerrorresponse"></a>
<a id="tocstokenerrorresponse"></a>

```json
{
  "code": 16,
  "error": "invalid_request",
  "error_description": "user lives elsewhere",
  "geolocation": "https://us.api.concursolutions.com"
}

```

TokenErrorResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|number|false|none|A machine-readable number that more specifically identifies the error.|
|error|[Error](#schemaerror)|true|none|A machine-readable category for the error, as in<br />[RFC 6749, Â§4.1.2.1](https://tools.ietf.org/html/rfc6749#section-4.1.2.1).|
|error_description|string|false|none|A human-readable error message that gives details about the error.|
|geolocation|string|false|none|The base URL for where the user profile lives. The token’s geolocation should be stored along with the token. The application should make subsequent calls using the token and the correct end points based on the token’s geolocation.|

<h2 id="tocS_Error">Error</h2>

<a id="schemaerror"></a>
<a id="schema_Error"></a>
<a id="tocSerror"></a>
<a id="tocserror"></a>

```json
"invalid_request"

```

Error

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Error|string|false|none|A machine-readable category for the error, as in<br />[RFC 6749, Â§4.1.2.1](https://tools.ietf.org/html/rfc6749#section-4.1.2.1).|

#### Enumerated Values

|Property|Value|
|---|---|
|Error|invalid_request|
|Error|invalid_client|
|Error|invalid_grant|
|Error|access_denied|
|Error|invalid_scope|

<h2 id="tocS_TokenType">TokenType</h2>

<a id="schematokentype"></a>
<a id="schema_TokenType"></a>
<a id="tocStokentype"></a>
<a id="tocstokentype"></a>

```json
"bearer"

```

TokenType

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|TokenType|string|false|none|The type of the token. Currently only bearer tokens are emitted.|

#### Enumerated Values

|Property|Value|
|---|---|
|TokenType|bearer|


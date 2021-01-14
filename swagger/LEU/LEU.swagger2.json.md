---
title: Launch External URL v0.1
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

<h1 id="launch-external-url">Launch External URL v0.1</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

Rest API for Launch External URL Service

Base URLs:

* <a href="//launchexternalurl-prod.seapr1.uscom.cnqr.delivery/">//launchexternalurl-prod.seapr1.uscom.cnqr.delivery/</a>

<a href="http://www.concur.com">Terms of service</a>
Email: <a href="mailto:martian@concur.com">Team Martian</a> 
License: <a href="http://www.concur.com">Concur</a>

# Authentication

* API Key (Authorization)
    - Parameter Name: **Authorization**, in: header. 

<h1 id="launch-external-url-launch-external-url-api">Launch External URL API</h1>

Launch External Url Controller

## createLeuConfigUsingPOST

<a id="opIdcreateLeuConfigUsingPOST"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /launchexternalurl-prod.seapr1.uscom.cnqr.delivery/launchexternalurl/v4/leuconfig \
  -H 'Content-Type: application/json' \
  -H 'Accept: */*' \
  -H 'company-uid: string' \
  -H 'concur-correlationid: string' \
  -H 'concur-uid: string' \
  -H 'Authorization: API_KEY'

```

```http
POST /launchexternalurl-prod.seapr1.uscom.cnqr.delivery/launchexternalurl/v4/leuconfig HTTP/1.1

Content-Type: application/json
Accept: */*
company-uid: string
concur-correlationid: string
concur-uid: string

```

```javascript
const inputBody = '{
  "allocation_id": "string",
  "context_type": "string",
  "expense_ids": [
    "string"
  ],
  "form_field_id": "string",
  "is_mobile": true,
  "logged_in_user_id": "string",
  "logged_in_user_login_id": "string",
  "report_id": "string",
  "report_owner_user_id": "string",
  "rpe_key": "string",
  "rpt_key": "string",
  "source": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'*/*',
  'company-uid':'string',
  'concur-correlationid':'string',
  'concur-uid':'string',
  'Authorization':'API_KEY'
};

fetch('/launchexternalurl-prod.seapr1.uscom.cnqr.delivery/launchexternalurl/v4/leuconfig',
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
  'Content-Type' => 'application/json',
  'Accept' => '*/*',
  'company-uid' => 'string',
  'concur-correlationid' => 'string',
  'concur-uid' => 'string',
  'Authorization' => 'API_KEY'
}

result = RestClient.post '/launchexternalurl-prod.seapr1.uscom.cnqr.delivery/launchexternalurl/v4/leuconfig',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': '*/*',
  'company-uid': 'string',
  'concur-correlationid': 'string',
  'concur-uid': 'string',
  'Authorization': 'API_KEY'
}

r = requests.post('/launchexternalurl-prod.seapr1.uscom.cnqr.delivery/launchexternalurl/v4/leuconfig', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => '*/*',
    'company-uid' => 'string',
    'concur-correlationid' => 'string',
    'concur-uid' => 'string',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/launchexternalurl-prod.seapr1.uscom.cnqr.delivery/launchexternalurl/v4/leuconfig', array(
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
URL obj = new URL("/launchexternalurl-prod.seapr1.uscom.cnqr.delivery/launchexternalurl/v4/leuconfig");
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
        "Content-Type": []string{"application/json"},
        "Accept": []string{"*/*"},
        "company-uid": []string{"string"},
        "concur-correlationid": []string{"string"},
        "concur-uid": []string{"string"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/launchexternalurl-prod.seapr1.uscom.cnqr.delivery/launchexternalurl/v4/leuconfig", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /launchexternalurl/v4/leuconfig`

*Launch external url configuration*

returns the launch external url configuration for the form field

> Body parameter

```json
{
  "allocation_id": "string",
  "context_type": "string",
  "expense_ids": [
    "string"
  ],
  "form_field_id": "string",
  "is_mobile": true,
  "logged_in_user_id": "string",
  "logged_in_user_login_id": "string",
  "report_id": "string",
  "report_owner_user_id": "string",
  "rpe_key": "string",
  "rpt_key": "string",
  "source": "string"
}
```

<h3 id="createleuconfigusingpost-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|company-uid|header|string|true|The unique identifier of the company in question|
|concur-correlationid|header|string|true|The unique identifier of the consumer making the API calls. Minimum length: 6 characters|
|concur-uid|header|string|false|The unique identifier of the logged in user (required when using user jwt)|
|body|body|[LeuConfigRequest](#schemaleuconfigrequest)|true|leuConfigRequest|

> Example responses

> 200 Response

<h3 id="createleuconfigusingpost-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully retrieved launch external url config|[LeuConfigResponse](#schemaleuconfigresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request - Your request is missing parameters. Please verify and resubmit.|[ErrorMessage](#schemaerrormessage)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Full authentication is required to access this resource.|[ErrorMessage](#schemaerrormessage)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Unable to find resource requested|[ErrorMessage](#schemaerrormessage)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error, please contact the administrator.|[ErrorMessage](#schemaerrormessage)|
|503|[Service Unavailable](https://tools.ietf.org/html/rfc7231#section-6.6.4)|The service is unavailable either due to being offline or refusing the connection|[ErrorMessage](#schemaerrormessage)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Authorization ( Scopes: global ), None ( Scopes: global )
</aside>

## getLeuVersionUsingGET

<a id="opIdgetLeuVersionUsingGET"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /launchexternalurl-prod.seapr1.uscom.cnqr.delivery/launchexternalurl/v4/leuversion/{formFieldId} \
  -H 'Accept: */*' \
  -H 'company-uid: string' \
  -H 'concur-correlationid: string' \
  -H 'concur-uid: string' \
  -H 'Authorization: API_KEY'

```

```http
GET /launchexternalurl-prod.seapr1.uscom.cnqr.delivery/launchexternalurl/v4/leuversion/{formFieldId} HTTP/1.1

Accept: */*
company-uid: string
concur-correlationid: string
concur-uid: string

```

```javascript

const headers = {
  'Accept':'*/*',
  'company-uid':'string',
  'concur-correlationid':'string',
  'concur-uid':'string',
  'Authorization':'API_KEY'
};

fetch('/launchexternalurl-prod.seapr1.uscom.cnqr.delivery/launchexternalurl/v4/leuversion/{formFieldId}',
{
  method: 'GET',

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
  'Accept' => '*/*',
  'company-uid' => 'string',
  'concur-correlationid' => 'string',
  'concur-uid' => 'string',
  'Authorization' => 'API_KEY'
}

result = RestClient.get '/launchexternalurl-prod.seapr1.uscom.cnqr.delivery/launchexternalurl/v4/leuversion/{formFieldId}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': '*/*',
  'company-uid': 'string',
  'concur-correlationid': 'string',
  'concur-uid': 'string',
  'Authorization': 'API_KEY'
}

r = requests.get('/launchexternalurl-prod.seapr1.uscom.cnqr.delivery/launchexternalurl/v4/leuversion/{formFieldId}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => '*/*',
    'company-uid' => 'string',
    'concur-correlationid' => 'string',
    'concur-uid' => 'string',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/launchexternalurl-prod.seapr1.uscom.cnqr.delivery/launchexternalurl/v4/leuversion/{formFieldId}', array(
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
URL obj = new URL("/launchexternalurl-prod.seapr1.uscom.cnqr.delivery/launchexternalurl/v4/leuversion/{formFieldId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
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
        "Accept": []string{"*/*"},
        "company-uid": []string{"string"},
        "concur-correlationid": []string{"string"},
        "concur-uid": []string{"string"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/launchexternalurl-prod.seapr1.uscom.cnqr.delivery/launchexternalurl/v4/leuversion/{formFieldId}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /launchexternalurl/v4/leuversion/{formFieldId}`

*Launch external url version*

returns Launch external url version configured for the form field

<h3 id="getleuversionusingget-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|company-uid|header|string|true|The unique identifier of the company in question|
|concur-correlationid|header|string|true|The unique identifier of the consumer making the API calls. Minimum length: 6 characters|
|concur-uid|header|string|false|The unique identifier of the logged in user (required when using user jwt)|
|formFieldId|path|string|true|Form field id|

> Example responses

> 200 Response

<h3 id="getleuversionusingget-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully retrieved launch external url version|[LeuVersionResponse](#schemaleuversionresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request - Your request is missing parameters. Please verify and resubmit.|[ErrorMessage](#schemaerrormessage)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Full authentication is required to access this resource.|[ErrorMessage](#schemaerrormessage)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Unable to find resource requested|[ErrorMessage](#schemaerrormessage)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error, please contact the administrator.|[ErrorMessage](#schemaerrormessage)|
|503|[Service Unavailable](https://tools.ietf.org/html/rfc7231#section-6.6.4)|The service is unavailable either due to being offline or refusing the connection|[ErrorMessage](#schemaerrormessage)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Authorization ( Scopes: global ), None ( Scopes: global )
</aside>

<h1 id="launch-external-url-mgmt-controller">mgmt-controller</h1>

Mgmt Controller

## versionUsingGET

<a id="opIdversionUsingGET"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /launchexternalurl-prod.seapr1.uscom.cnqr.delivery/mgmt/version \
  -H 'Accept: */*' \
  -H 'company-uid: string' \
  -H 'concur-correlationid: string' \
  -H 'concur-uid: string' \
  -H 'Authorization: API_KEY'

```

```http
GET /launchexternalurl-prod.seapr1.uscom.cnqr.delivery/mgmt/version HTTP/1.1

Accept: */*
company-uid: string
concur-correlationid: string
concur-uid: string

```

```javascript

const headers = {
  'Accept':'*/*',
  'company-uid':'string',
  'concur-correlationid':'string',
  'concur-uid':'string',
  'Authorization':'API_KEY'
};

fetch('/launchexternalurl-prod.seapr1.uscom.cnqr.delivery/mgmt/version',
{
  method: 'GET',

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
  'Accept' => '*/*',
  'company-uid' => 'string',
  'concur-correlationid' => 'string',
  'concur-uid' => 'string',
  'Authorization' => 'API_KEY'
}

result = RestClient.get '/launchexternalurl-prod.seapr1.uscom.cnqr.delivery/mgmt/version',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': '*/*',
  'company-uid': 'string',
  'concur-correlationid': 'string',
  'concur-uid': 'string',
  'Authorization': 'API_KEY'
}

r = requests.get('/launchexternalurl-prod.seapr1.uscom.cnqr.delivery/mgmt/version', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => '*/*',
    'company-uid' => 'string',
    'concur-correlationid' => 'string',
    'concur-uid' => 'string',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/launchexternalurl-prod.seapr1.uscom.cnqr.delivery/mgmt/version', array(
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
URL obj = new URL("/launchexternalurl-prod.seapr1.uscom.cnqr.delivery/mgmt/version");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
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
        "Accept": []string{"*/*"},
        "company-uid": []string{"string"},
        "concur-correlationid": []string{"string"},
        "concur-uid": []string{"string"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/launchexternalurl-prod.seapr1.uscom.cnqr.delivery/mgmt/version", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /mgmt/version`

*Get current server time and git commit sha of deployed LEU*

/api based path requires authentication

<h3 id="versionusingget-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|company-uid|header|string|true|The unique identifier of the company in question|
|concur-correlationid|header|string|true|The unique identifier of the consumer making the API calls. Minimum length: 6 characters|
|concur-uid|header|string|false|The unique identifier of the logged in user (required when using user jwt)|

> Example responses

> 200 Response

<h3 id="versionusingget-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|string|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request - Your request is missing parameters. Please verify and resubmit.|[ErrorMessage](#schemaerrormessage)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Full authentication is required to access this resource.|[ErrorMessage](#schemaerrormessage)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Unable to find resource requested.|[ErrorMessage](#schemaerrormessage)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error, please contact the administrator.|[ErrorMessage](#schemaerrormessage)|
|503|[Service Unavailable](https://tools.ietf.org/html/rfc7231#section-6.6.4)|Service Unavailable.|[ErrorMessage](#schemaerrormessage)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Authorization ( Scopes: global ), None ( Scopes: global )
</aside>

# Schemas

<h2 id="tocS_ErrorMessage">ErrorMessage</h2>

<a id="schemaerrormessage"></a>
<a id="schema_ErrorMessage"></a>
<a id="tocSerrormessage"></a>
<a id="tocserrormessage"></a>

```json
{
  "errorId": "string",
  "errorMessage": "string",
  "httpStatus": "string",
  "path": "string",
  "timestamp": "2016-10-04T00:53:25.931+0000",
  "validationErrors": [
    {
      "message": "string",
      "source": "string"
    }
  ]
}

```

ErrorMessage

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|errorId|string|false|none|The unique identifier of the error associated with the response or is it error response itself|
|errorMessage|string|true|none|The detailed error message|
|httpStatus|string|true|none|The http response code and phrase for the response|
|path|string|true|none|The URI of the attempted request|
|timestamp|string(date-time)|true|none|The time when the error was captured|
|validationErrors|[[ValidationError](#schemavalidationerror)]|false|none|The validation error messages|

<h2 id="tocS_LeuConfigRequest">LeuConfigRequest</h2>

<a id="schemaleuconfigrequest"></a>
<a id="schema_LeuConfigRequest"></a>
<a id="tocSleuconfigrequest"></a>
<a id="tocsleuconfigrequest"></a>

```json
{
  "allocation_id": "string",
  "context_type": "string",
  "expense_ids": [
    "string"
  ],
  "form_field_id": "string",
  "is_mobile": true,
  "logged_in_user_id": "string",
  "logged_in_user_login_id": "string",
  "report_id": "string",
  "report_owner_user_id": "string",
  "rpe_key": "string",
  "rpt_key": "string",
  "source": "string"
}

```

LeuConfigRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|allocation_id|string|false|none|The allocation ID is required for report allocation|
|context_type|string|true|none|The context type would most likely be TRAVELER, and that is dependent on the JWT conversation|
|expense_ids|[string]|false|none|A list of expense IDs is required for report entry and allocation|
|form_field_id|string|true|none|The form field ID is required to call EMT for the popup window height and width.|
|is_mobile|boolean|false|none|A boolean (set to false as default) to know if the request is coming from Mobile|
|logged_in_user_id|string|true|none|UUID of the user, can also be the expense delegate instead of report owner|
|logged_in_user_login_id|string|false|none|The SAP Concur user ID of the logged-in user|
|report_id|string|true|none|The report ID is required for report entry, allocation, and header|
|report_owner_user_id|string|true|none|UUID of the report owner|
|rpe_key|string|false|none|The report entry key is required for v1 only|
|rpt_key|string|false|none|The report header key is required for v1 only|
|source|string|true|none|The source of the report|

<h2 id="tocS_LeuConfigResponse">LeuConfigResponse</h2>

<a id="schemaleuconfigresponse"></a>
<a id="schema_LeuConfigResponse"></a>
<a id="tocSleuconfigresponse"></a>
<a id="tocsleuconfigresponse"></a>

```json
{
  "client_url": "string",
  "leu_version": "string",
  "popup_height": 0,
  "popup_width": 0
}

```

LeuConfigResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|client_url|string|false|none|value = Client popup url along with data as query parameter, needed by client to update report using Concur callback url|
|leu_version|string|false|none|value = Launch external url version configured for the field / connector|
|popup_height|integer(int32)|false|none|value = Display specifics for popup window|
|popup_width|integer(int32)|false|none|value = Display specifics for popup window|

<h2 id="tocS_LeuVersionResponse">LeuVersionResponse</h2>

<a id="schemaleuversionresponse"></a>
<a id="schema_LeuVersionResponse"></a>
<a id="tocSleuversionresponse"></a>
<a id="tocsleuversionresponse"></a>

```json
{
  "leu_version": "string"
}

```

LeuVersionResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|leu_version|string|false|none|value = Launch external url version configured for the field / connector|

<h2 id="tocS_ValidationError">ValidationError</h2>

<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "message": "string",
  "source": "string"
}

```

ValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|message|string|false|none|The detailed message of the validation error|
|source|string|false|none|The type of validation which failed|


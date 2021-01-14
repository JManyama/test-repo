---
title: GET Users Bulk API v3.1.0
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers:
  - <a
    href="https://developer.concur.com/api-reference/authentication/get-users31.html">Documentation</a>
includes: []
search: true
highlight_theme: darkula
headingLevel: 2
generator: widdershins v4.0.1

---

<h1 id="get-users-bulk-api">GET Users Bulk API v3.1.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

This API takes a company level token, and returns a list of users that match the search criteria

Base URLs:

* <a href="https://us.api.concursolutions.com">https://us.api.concursolutions.com</a>

# Authentication

* API Key (ApiKeyAuth)
    - Parameter Name: **Authorization**, in: header. 

<h1 id="get-users-bulk-api-default">Default</h1>

## get__users_

> Code samples

```shell
# You can also use wget
curl -X GET https://us.api.concursolutions.com/users/ \
  -H 'Accept: */*' \
  -H 'Authorization: string'

```

```http
GET https://us.api.concursolutions.com/users/ HTTP/1.1
Host: us.api.concursolutions.com
Accept: */*
Authorization: string

```

```javascript

const headers = {
  'Accept':'*/*',
  'Authorization':'string'
};

fetch('https://us.api.concursolutions.com/users/',
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
  'Authorization' => 'string'
}

result = RestClient.get 'https://us.api.concursolutions.com/users/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': '*/*',
  'Authorization': 'string'
}

r = requests.get('https://us.api.concursolutions.com/users/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => '*/*',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://us.api.concursolutions.com/users/', array(
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
URL obj = new URL("https://us.api.concursolutions.com/users/");
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
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://us.api.concursolutions.com/users/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /users/`

<h3 id="get__users_-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|false|Company level access Bearer token|
|offset|query|integer|false|The number of items to skip before returning result set|
|limit|query|integer|false|The numbers of items to return.|
|isactive|query|string|false|Whether the user is active|
|loginid|query|string|false|login_id of the user|
|lastname|query|string|false|last name of the user|
|employeeid|query|string|false|Employee Id of the user|
|primaryemail|query|string|false|Primary email of the user|
|countrycode|query|string|false|Country Code of the user|
|id|query|string|false|Id of the user|

> Example responses

> 200 Response

<h3 id="get__users_-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[Response](#schemaresponse)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Authorization Required|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Resoource not found|None|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_User">User</h2>

<a id="schemauser"></a>
<a id="schema_User"></a>
<a id="tocSuser"></a>
<a id="tocsuser"></a>

```json
{
  "ID": "99BFFFC3-C0BE-44FF-A441-AE1FFFFFF75B8",
  "Active": true,
  "CountryCode": "US",
  "CellPhoneNumber": "425-555-1111",
  "PrimaryEmail": "johndoe@gmail.com",
  "EmployeeID": "johndoe@gmail.com",
  "OrganizationUnit": "IT",
  "FirstName": "John",
  "MiddleName": "",
  "LastName": "Doe",
  "LoginID": "johndoe@gmail.com",
  "Emails": [
    "johndoe@gmail.com"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ID|string|false|none|none|
|Active|boolean|false|none|none|
|CountryCode|string|false|none|none|
|CellPhoneNumber|string|false|none|none|
|PrimaryEmail|string|false|none|none|
|EmployeeID|string|false|none|none|
|OrganizationUnit|string|false|none|none|
|FirstName|string|false|none|none|
|MiddleName|string|false|none|none|
|LastName|string|false|none|none|
|LoginID|string|false|none|none|
|Emails|[string]|false|none|none|

<h2 id="tocS_Response">Response</h2>

<a id="schemaresponse"></a>
<a id="schema_Response"></a>
<a id="tocSresponse"></a>
<a id="tocsresponse"></a>

```json
{
  "total": 10,
  "offset": 1,
  "limit": 10,
  "company": {
    "name": "Company Name LLC",
    "address": "601 108th ave NE",
    "city": "Bellevue",
    "state": "WA",
    "zip": "98004",
    "country": "US"
  },
  "Items": [
    {
      "ID": "99BFFFC3-C0BE-44FF-A441-AE1FFFFFF75B8",
      "Active": true,
      "CountryCode": "US",
      "CellPhoneNumber": "425-555-1111",
      "PrimaryEmail": "johndoe@gmail.com",
      "EmployeeID": "johndoe@gmail.com",
      "OrganizationUnit": "IT",
      "FirstName": "John",
      "MiddleName": "",
      "LastName": "Doe",
      "LoginID": "johndoe@gmail.com",
      "Emails": [
        "johndoe@gmail.com"
      ]
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|total|integer|false|none|none|
|offset|integer|false|none|none|
|limit|integer|false|none|none|
|company|object|false|none|none|
|» name|string|false|none|none|
|» address|string|false|none|none|
|» city|string|false|none|none|
|» state|string|false|none|none|
|» zip|string|false|none|none|
|» country|string|false|none|none|
|Items|[[User](#schemauser)]|false|none|none|


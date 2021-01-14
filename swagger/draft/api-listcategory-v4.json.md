---
title: List Category v4.0
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

<h1 id="list-category">List Category v4.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

Provides an automated solution to clients who would like to manage list categories. This API provides methods to view, add, update or delete list categories.

Base URLs:

* <a href="https://www.concursolutions.com/api/v4.0">https://www.concursolutions.com/api/v4.0</a>

# Authentication

* API Key (JWT_Token)
    - Parameter Name: **Authorization**, in: header. 

<h1 id="list-category-list-category-api">List Category API</h1>

List Category Controller

## getAllCategoriesUsingGET

<a id="opIdgetAllCategoriesUsingGET"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://www.concursolutions.com/api/v4.0/list/v4/categories \
  -H 'Accept: application/json' \
  -H 'Accept-Language: en' \
  -H 'company-uuid: string' \
  -H 'concur-correlationid: string' \
  -H 'concur-uid: string' \
  -H 'Authorization: API_KEY'

```

```http
GET https://www.concursolutions.com/api/v4.0/list/v4/categories HTTP/1.1
Host: www.concursolutions.com
Accept: application/json
Accept-Language: en
company-uuid: string
concur-correlationid: string
concur-uid: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Accept-Language':'en',
  'company-uuid':'string',
  'concur-correlationid':'string',
  'concur-uid':'string',
  'Authorization':'API_KEY'
};

fetch('https://www.concursolutions.com/api/v4.0/list/v4/categories',
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
  'Accept' => 'application/json',
  'Accept-Language' => 'en',
  'company-uuid' => 'string',
  'concur-correlationid' => 'string',
  'concur-uid' => 'string',
  'Authorization' => 'API_KEY'
}

result = RestClient.get 'https://www.concursolutions.com/api/v4.0/list/v4/categories',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Accept-Language': 'en',
  'company-uuid': 'string',
  'concur-correlationid': 'string',
  'concur-uid': 'string',
  'Authorization': 'API_KEY'
}

r = requests.get('https://www.concursolutions.com/api/v4.0/list/v4/categories', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Accept-Language' => 'en',
    'company-uuid' => 'string',
    'concur-correlationid' => 'string',
    'concur-uid' => 'string',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://www.concursolutions.com/api/v4.0/list/v4/categories', array(
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
URL obj = new URL("https://www.concursolutions.com/api/v4.0/list/v4/categories");
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
        "Accept": []string{"application/json"},
        "Accept-Language": []string{"en"},
        "company-uuid": []string{"string"},
        "concur-correlationid": []string{"string"},
        "concur-uid": []string{"string"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://www.concursolutions.com/api/v4.0/list/v4/categories", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /list/v4/categories`

*Gets all categories for the given company.*

Returns all categories

<h3 id="getallcategoriesusingget-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Accept-Language|header|string|false|Language code|
|company-uuid|header|string|false|Company UUID of the user (Used for x509 authorization)|
|concur-correlationid|header|string|false|The unique identifier of the consumer making the API calls. Minimum length: 6 characters|
|concur-uid|header|string|false|Concur Employee UUID of the caller (Used for x509 authorization)|
|page|query|integer(int32)|false|Page number starting from 1|
|type|query|string|false|Filter capabilities for List Category type|

> Example responses

> 200 Response

```json
{
  "content": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "value": "string",
      "type": "string",
      "isSystemRecord": true,
      "isDeleted": true,
      "isReadOnly": true
    }
  ],
  "links": [
    {
      "deprecation": "string",
      "href": "string",
      "hreflang": "string",
      "media": "string",
      "rel": "string",
      "templated": true,
      "title": "string",
      "type": "string"
    }
  ],
  "page": {
    "number": 0,
    "size": 0,
    "totalElements": 0,
    "totalPages": 0
  }
}
```

<h3 id="getallcategoriesusingget-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully get all categories|[PagedResourcesCategoryResponse](#schemapagedresourcescategoryresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Entity does not exist|[ErrorMessage](#schemaerrormessage)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access Denied|[ErrorMessage](#schemaerrormessage)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|List category not found|[ErrorMessage](#schemaerrormessage)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|[ErrorMessage](#schemaerrormessage)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
JWT_Token
</aside>

## createCategoryUsingPOST

<a id="opIdcreateCategoryUsingPOST"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://www.concursolutions.com/api/v4.0/list/v4/categories \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'company-uuid: string' \
  -H 'concur-correlationid: string' \
  -H 'concur-uid: string' \
  -H 'Authorization: API_KEY'

```

```http
POST https://www.concursolutions.com/api/v4.0/list/v4/categories HTTP/1.1
Host: www.concursolutions.com
Content-Type: application/json
Accept: application/json
company-uuid: string
concur-correlationid: string
concur-uid: string

```

```javascript
const inputBody = '{
  "value": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'company-uuid':'string',
  'concur-correlationid':'string',
  'concur-uid':'string',
  'Authorization':'API_KEY'
};

fetch('https://www.concursolutions.com/api/v4.0/list/v4/categories',
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
  'Accept' => 'application/json',
  'company-uuid' => 'string',
  'concur-correlationid' => 'string',
  'concur-uid' => 'string',
  'Authorization' => 'API_KEY'
}

result = RestClient.post 'https://www.concursolutions.com/api/v4.0/list/v4/categories',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'company-uuid': 'string',
  'concur-correlationid': 'string',
  'concur-uid': 'string',
  'Authorization': 'API_KEY'
}

r = requests.post('https://www.concursolutions.com/api/v4.0/list/v4/categories', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'company-uuid' => 'string',
    'concur-correlationid' => 'string',
    'concur-uid' => 'string',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://www.concursolutions.com/api/v4.0/list/v4/categories', array(
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
URL obj = new URL("https://www.concursolutions.com/api/v4.0/list/v4/categories");
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
        "Accept": []string{"application/json"},
        "company-uuid": []string{"string"},
        "concur-correlationid": []string{"string"},
        "concur-uid": []string{"string"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://www.concursolutions.com/api/v4.0/list/v4/categories", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /list/v4/categories`

*Create a category with provided request body*

Returns a new category

> Body parameter

```json
{
  "value": "string"
}
```

<h3 id="createcategoryusingpost-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|company-uuid|header|string|false|Company UUID of the user (Used for x509 authorization)|
|concur-correlationid|header|string|false|The unique identifier of the consumer making the API calls. Minimum length: 6 characters|
|concur-uid|header|string|false|Concur Employee UUID of the caller (Used for x509 authorization)|
|body|body|[CategoryRequest](#schemacategoryrequest)|true|List Category that is created for the company|

> Example responses

> 201 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "value": "string",
  "type": "string",
  "isSystemRecord": true,
  "isDeleted": true,
  "isReadOnly": true
}
```

<h3 id="createcategoryusingpost-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successfully created a category|[CategoryResponse](#schemacategoryresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Entity does not exist|[ErrorMessage](#schemaerrormessage)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access Denied|[ErrorMessage](#schemaerrormessage)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ErrorMessage](#schemaerrormessage)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|The specified media type is not supported|[ErrorMessage](#schemaerrormessage)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|The list category could not be created|[ErrorMessage](#schemaerrormessage)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
JWT_Token
</aside>

## getListCategoryUsingGET

<a id="opIdgetListCategoryUsingGET"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId} \
  -H 'Accept: application/json' \
  -H 'Accept-Language: en' \
  -H 'company-uuid: string' \
  -H 'concur-correlationid: string' \
  -H 'concur-uid: string' \
  -H 'Authorization: API_KEY'

```

```http
GET https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId} HTTP/1.1
Host: www.concursolutions.com
Accept: application/json
Accept-Language: en
company-uuid: string
concur-correlationid: string
concur-uid: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Accept-Language':'en',
  'company-uuid':'string',
  'concur-correlationid':'string',
  'concur-uid':'string',
  'Authorization':'API_KEY'
};

fetch('https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId}',
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
  'Accept' => 'application/json',
  'Accept-Language' => 'en',
  'company-uuid' => 'string',
  'concur-correlationid' => 'string',
  'concur-uid' => 'string',
  'Authorization' => 'API_KEY'
}

result = RestClient.get 'https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Accept-Language': 'en',
  'company-uuid': 'string',
  'concur-correlationid': 'string',
  'concur-uid': 'string',
  'Authorization': 'API_KEY'
}

r = requests.get('https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Accept-Language' => 'en',
    'company-uuid' => 'string',
    'concur-correlationid' => 'string',
    'concur-uid' => 'string',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId}', array(
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
URL obj = new URL("https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId}");
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
        "Accept": []string{"application/json"},
        "Accept-Language": []string{"en"},
        "company-uuid": []string{"string"},
        "concur-correlationid": []string{"string"},
        "concur-uid": []string{"string"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /list/v4/categories/{categoryId}`

*Get a list category with provided id*

Returns an existing category

<h3 id="getlistcategoryusingget-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Accept-Language|header|string|false|Language code|
|categoryId|path|string(uuid)|true|The unique identifier of the category|
|company-uuid|header|string|false|Company UUID of the user (Used for x509 authorization)|
|concur-correlationid|header|string|false|The unique identifier of the consumer making the API calls. Minimum length: 6 characters|
|concur-uid|header|string|false|Concur Employee UUID of the caller (Used for x509 authorization)|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "value": "string",
  "type": "string",
  "isSystemRecord": true,
  "isDeleted": true,
  "isReadOnly": true
}
```

<h3 id="getlistcategoryusingget-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully get list category|[CategoryResponse](#schemacategoryresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Entity does not exist|[ErrorMessage](#schemaerrormessage)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access Denied|[ErrorMessage](#schemaerrormessage)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|List category not found|[ErrorMessage](#schemaerrormessage)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|[ErrorMessage](#schemaerrormessage)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
JWT_Token
</aside>

## updateCategoryUsingPUT

<a id="opIdupdateCategoryUsingPUT"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Accept-Language: en' \
  -H 'company-uuid: string' \
  -H 'concur-correlationid: string' \
  -H 'concur-uid: string' \
  -H 'Authorization: API_KEY'

```

```http
PUT https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId} HTTP/1.1
Host: www.concursolutions.com
Content-Type: application/json
Accept: application/json
Accept-Language: en
company-uuid: string
concur-correlationid: string
concur-uid: string

```

```javascript
const inputBody = '{
  "value": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Accept-Language':'en',
  'company-uuid':'string',
  'concur-correlationid':'string',
  'concur-uid':'string',
  'Authorization':'API_KEY'
};

fetch('https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId}',
{
  method: 'PUT',
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
  'Accept' => 'application/json',
  'Accept-Language' => 'en',
  'company-uuid' => 'string',
  'concur-correlationid' => 'string',
  'concur-uid' => 'string',
  'Authorization' => 'API_KEY'
}

result = RestClient.put 'https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Accept-Language': 'en',
  'company-uuid': 'string',
  'concur-correlationid': 'string',
  'concur-uid': 'string',
  'Authorization': 'API_KEY'
}

r = requests.put('https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Accept-Language' => 'en',
    'company-uuid' => 'string',
    'concur-correlationid' => 'string',
    'concur-uid' => 'string',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId}', array(
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
URL obj = new URL("https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
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
        "Accept": []string{"application/json"},
        "Accept-Language": []string{"en"},
        "company-uuid": []string{"string"},
        "concur-correlationid": []string{"string"},
        "concur-uid": []string{"string"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /list/v4/categories/{categoryId}`

*Updates the specified category with provided request body*

Returns an updated category

> Body parameter

```json
{
  "value": "string"
}
```

<h3 id="updatecategoryusingput-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Accept-Language|header|string|false|Language code|
|categoryId|path|string(uuid)|true|The unique identifier of the category|
|company-uuid|header|string|false|Company UUID of the user (Used for x509 authorization)|
|concur-correlationid|header|string|false|The unique identifier of the consumer making the API calls. Minimum length: 6 characters|
|concur-uid|header|string|false|Concur Employee UUID of the caller (Used for x509 authorization)|
|body|body|[CategoryRequest](#schemacategoryrequest)|true|List Category that is updated for the company|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "value": "string",
  "type": "string",
  "isSystemRecord": true,
  "isDeleted": true,
  "isReadOnly": true
}
```

<h3 id="updatecategoryusingput-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully updated the list category|[CategoryResponse](#schemacategoryresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|This List Category name is already in use|[ErrorMessage](#schemaerrormessage)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access Denied|[ErrorMessage](#schemaerrormessage)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ErrorMessage](#schemaerrormessage)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|List category not found|[ErrorMessage](#schemaerrormessage)|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|The specified media type is not supported|[ErrorMessage](#schemaerrormessage)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|List category not updated|[ErrorMessage](#schemaerrormessage)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
JWT_Token
</aside>

## deleteListCategoryUsingDELETE

<a id="opIddeleteListCategoryUsingDELETE"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId} \
  -H 'Accept: application/json' \
  -H 'company-uuid: string' \
  -H 'concur-correlationid: string' \
  -H 'concur-uid: string' \
  -H 'Authorization: API_KEY'

```

```http
DELETE https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId} HTTP/1.1
Host: www.concursolutions.com
Accept: application/json
company-uuid: string
concur-correlationid: string
concur-uid: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'company-uuid':'string',
  'concur-correlationid':'string',
  'concur-uid':'string',
  'Authorization':'API_KEY'
};

fetch('https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId}',
{
  method: 'DELETE',

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
  'Accept' => 'application/json',
  'company-uuid' => 'string',
  'concur-correlationid' => 'string',
  'concur-uid' => 'string',
  'Authorization' => 'API_KEY'
}

result = RestClient.delete 'https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'company-uuid': 'string',
  'concur-correlationid': 'string',
  'concur-uid': 'string',
  'Authorization': 'API_KEY'
}

r = requests.delete('https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'company-uuid' => 'string',
    'concur-correlationid' => 'string',
    'concur-uid' => 'string',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId}', array(
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
URL obj = new URL("https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
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
        "Accept": []string{"application/json"},
        "company-uuid": []string{"string"},
        "concur-correlationid": []string{"string"},
        "concur-uid": []string{"string"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "https://www.concursolutions.com/api/v4.0/list/v4/categories/{categoryId}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /list/v4/categories/{categoryId}`

*Delete a list category*

Deletes list category

<h3 id="deletelistcategoryusingdelete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|categoryId|path|string(uuid)|true|The unique identifier of the category|
|company-uuid|header|string|false|Company UUID of the user (Used for x509 authorization)|
|concur-correlationid|header|string|false|The unique identifier of the consumer making the API calls. Minimum length: 6 characters|
|concur-uid|header|string|false|Concur Employee UUID of the caller (Used for x509 authorization)|

> Example responses

> 400 Response

```json
{
  "error": {
    "id": "string",
    "message": "string"
  },
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

<h3 id="deletelistcategoryusingdelete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|Successfully deleted list category|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|There are list associated with the list category|[ErrorMessage](#schemaerrormessage)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access Denied|[ErrorMessage](#schemaerrormessage)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ErrorMessage](#schemaerrormessage)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|[ErrorMessage](#schemaerrormessage)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
JWT_Token
</aside>

# Schemas

<h2 id="tocS_CategoryRequest">CategoryRequest</h2>

<a id="schemacategoryrequest"></a>
<a id="schema_CategoryRequest"></a>
<a id="tocScategoryrequest"></a>
<a id="tocscategoryrequest"></a>

```json
{
  "value": "string"
}

```

CategoryRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|value|string|false|none|List category value|

<h2 id="tocS_CategoryResponse">CategoryResponse</h2>

<a id="schemacategoryresponse"></a>
<a id="schema_CategoryResponse"></a>
<a id="tocScategoryresponse"></a>
<a id="tocscategoryresponse"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "value": "string",
  "type": "string",
  "isSystemRecord": true,
  "isDeleted": true,
  "isReadOnly": true
}

```

CategoryResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|The unique identifier of the list category|
|value|string|false|none|List category value|
|type|string|false|none|List category type|
|isSystemRecord|boolean|false|none|Whether the list category is a system record|
|isDeleted|boolean|false|none|Whether the list category has been deleted|
|isReadOnly|boolean|false|none|Whether the list category is read only|

<h2 id="tocS_ErrorMessage">ErrorMessage</h2>

<a id="schemaerrormessage"></a>
<a id="schema_ErrorMessage"></a>
<a id="tocSerrormessage"></a>
<a id="tocserrormessage"></a>

```json
{
  "error": {
    "id": "string",
    "message": "string"
  },
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
|error|[Message](#schemamessage)|true|none|none|
|httpStatus|string|true|none|The http response code and phrase for the response|
|path|string|true|none|The URI of the attempted request|
|timestamp|string(date-time)|true|none|The time when the error was captured|
|validationErrors|[[ValidationError](#schemavalidationerror)]|false|none|The validation error messages|

<h2 id="tocS_Link">Link</h2>

<a id="schemalink"></a>
<a id="schema_Link"></a>
<a id="tocSlink"></a>
<a id="tocslink"></a>

```json
{
  "deprecation": "string",
  "href": "string",
  "hreflang": "string",
  "media": "string",
  "rel": "string",
  "templated": true,
  "title": "string",
  "type": "string"
}

```

Link

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|deprecation|string|false|none|none|
|href|string|false|none|none|
|hreflang|string|false|none|none|
|media|string|false|none|none|
|rel|string|false|none|none|
|templated|boolean|false|none|none|
|title|string|false|none|none|
|type|string|false|none|none|

<h2 id="tocS_Message">Message</h2>

<a id="schemamessage"></a>
<a id="schema_Message"></a>
<a id="tocSmessage"></a>
<a id="tocsmessage"></a>

```json
{
  "id": "string",
  "message": "string"
}

```

Message

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|The unique identifier of the error associated with the response or is it error response itself|
|message|string|false|none|none|

<h2 id="tocS_PageMetadata">PageMetadata</h2>

<a id="schemapagemetadata"></a>
<a id="schema_PageMetadata"></a>
<a id="tocSpagemetadata"></a>
<a id="tocspagemetadata"></a>

```json
{
  "number": 0,
  "size": 0,
  "totalElements": 0,
  "totalPages": 0
}

```

PageMetadata

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|number|integer(int64)|false|none|none|
|size|integer(int64)|false|none|none|
|totalElements|integer(int64)|false|none|none|
|totalPages|integer(int64)|false|none|none|

<h2 id="tocS_PagedResourcesCategoryResponse">PagedResourcesCategoryResponse</h2>

<a id="schemapagedresourcescategoryresponse"></a>
<a id="schema_PagedResourcesCategoryResponse"></a>
<a id="tocSpagedresourcescategoryresponse"></a>
<a id="tocspagedresourcescategoryresponse"></a>

```json
{
  "content": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "value": "string",
      "type": "string",
      "isSystemRecord": true,
      "isDeleted": true,
      "isReadOnly": true
    }
  ],
  "links": [
    {
      "deprecation": "string",
      "href": "string",
      "hreflang": "string",
      "media": "string",
      "rel": "string",
      "templated": true,
      "title": "string",
      "type": "string"
    }
  ],
  "page": {
    "number": 0,
    "size": 0,
    "totalElements": 0,
    "totalPages": 0
  }
}

```

PagedResourcesCategoryResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|content|[[CategoryResponse](#schemacategoryresponse)]|false|none|none|
|links|[[Link](#schemalink)]|false|none|none|
|page|[PageMetadata](#schemapagemetadata)|false|none|none|

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


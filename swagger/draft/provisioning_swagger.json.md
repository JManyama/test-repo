---
title: Provisioning APIs v4
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

<h1 id="provisioning-apis">Provisioning APIs v4</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

Provisioning APIs

Base URLs:

* <a href="https://us.api.concursolutions.com/provisioning/v4">https://us.api.concursolutions.com/provisioning/v4</a>

<a href="http://us.api.concursolutions.com/terms">Terms of service</a>
Email: <a href="mailto:profile@concur.com">Support</a> 
License: <a href="https://developer.concur.com/Terms-of-Use.html">Concur</a>

# Authentication

* API Key (ApiKeyAuth)
    - Parameter Name: **Authorization**, in: header. 

<h1 id="provisioning-apis-provisions">Provisions</h1>

## provisions.id.status.get

<a id="opIdprovisions.id.status.get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://us.api.concursolutions.com/provisioning/v4/provisions/{id}/status \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
GET https://us.api.concursolutions.com/provisioning/v4/provisions/{id}/status HTTP/1.1
Host: us.api.concursolutions.com
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('https://us.api.concursolutions.com/provisioning/v4/provisions/{id}/status',
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
  'Authorization' => 'API_KEY'
}

result = RestClient.get 'https://us.api.concursolutions.com/provisioning/v4/provisions/{id}/status',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.get('https://us.api.concursolutions.com/provisioning/v4/provisions/{id}/status', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://us.api.concursolutions.com/provisioning/v4/provisions/{id}/status', array(
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
URL obj = new URL("https://us.api.concursolutions.com/provisioning/v4/provisions/{id}/status");
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
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://us.api.concursolutions.com/provisioning/v4/provisions/{id}/status", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /provisions/{id}/status`

*Get the status of a provisioning request.*

<h3 id="provisions.id.status.get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|Provision Id|
|attributes|query|string|false|Additional attributes to include in response|
|startIndex|query|integer|false|The 1-based index of the first operation in the set of operations|
|count|query|integer|false|The number of operations to be returned in response|

#### Enumerated Values

|Parameter|Value|
|---|---|
|attributes|operations|

> Example responses

> 200 Response

```json
{
  "id": "string",
  "itemsPerPage": 0,
  "operations": [
    {
      "bulkId": "string",
      "extensions": [
        {
          "messages": {
            "code": "string",
            "message": "string",
            "schemaPath": "string",
            "type": "error"
          },
          "name": "string",
          "status": {
            "code": "string",
            "completed": true,
            "result": "success",
            "success": true
          }
        }
      ],
      "id": "string",
      "resource": {
        "id": "string",
        "type": "User"
      },
      "status": {
        "completed": true,
        "success": true
      }
    }
  ],
  "startIndex": 0,
  "status": {
    "completed": true,
    "success": true
  },
  "totalResults": 0
}
```

<h3 id="provisions.id.status.get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|provision status|[ProvisionStatus](#schemaprovisionstatus)|
|default|Default|none|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth
</aside>

<h1 id="provisioning-apis-bulk">Bulk</h1>

## bulk.provision.create

<a id="opIdbulk.provision.create"></a>

> Code samples

```shell
# You can also use wget
curl -X POST https://us.api.concursolutions.com/provisioning/v4/Bulk \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
POST https://us.api.concursolutions.com/provisioning/v4/Bulk HTTP/1.1
Host: us.api.concursolutions.com
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:BulkRequest"
  ],
  "Operations": [
    {
      "data": {
        "active": true,
        "addresses": [
          {
            "country": "string",
            "locality": "string",
            "postalCode": "string",
            "region": "string",
            "streetAddress": "string",
            "type": "work"
          }
        ],
        "dateOfBirth": "string",
        "displayName": "string",
        "emails": [
          {
            "dateAdded": "string",
            "dateVerified": "string",
            "notifications": true,
            "type": "work",
            "value": "string",
            "verified": true
          }
        ],
        "emergencyContacts": [
          {
            "country": "string",
            "emails": [
              "string"
            ],
            "locality": "string",
            "name": "string",
            "phones": [
              "string"
            ],
            "postalCode": "string",
            "region": "string",
            "relationship": "Spouse",
            "streetAddress": "string"
          }
        ],
        "entitlements": [
          "Expense"
        ],
        "externalId": "string",
        "gender": "Male",
        "id": "string",
        "localeOverrides": {
          "preference24Hour": "h:mm AM/PM",
          "preferenceCurrencySymbolLocation": "BeforeAmount",
          "preferenceDateFormat": "mm/dd/yyyy",
          "preferenceDefaultCalView": "day",
          "preferenceDistance": "mile",
          "preferenceEndDayViewHour": 0,
          "preferenceFirstDayOfWeek": "Monday",
          "preferenceHourMinuteSeparator": ":",
          "preferenceNegativeCurrencyFormat": "-100",
          "preferenceNegativeNumberFormat": "-100",
          "preferenceNumberFormat": "1,000.00",
          "preferenceStartDayViewHour": 0
        },
        "meta": {},
        "name": {
          "familyName": "string",
          "formatted": "string",
          "givenName": "string",
          "hasNoMiddleName": true,
          "honorificPrefix": "Miss",
          "honorificSuffix": "Jr.",
          "legalName": "string",
          "middleInitial": "string",
          "middleName": "string"
        },
        "nickName": "string",
        "phoneNumbers": [
          {
            "countryCode": "string",
            "display": "string",
            "notifications": true,
            "operatingSystem": "Android Phone",
            "primary": true,
            "type": "work",
            "value": "string"
          }
        ],
        "preferredLanguage": "string",
        "timezone": "string",
        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:Payroll": {
          "adp": {
            "companyCode": "string",
            "deductionCode": "string",
            "employeeFileNumber": "string"
          }
        },
        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
          "companyId": "string",
          "costCenter": "string",
          "department": "string",
          "division": "string",
          "employeeNumber": "string",
          "jobTitle": "string",
          "manager": {
            "$ref": "string",
            "displayName": "string",
            "employeeNumber": "string",
            "value": "string"
          },
          "orgUnit": "string",
          "organization": "string",
          "self": {
            "$ref": "string",
            "displayName": "string",
            "employeeNumber": "string",
            "value": "string"
          },
          "startDate": "string",
          "terminationDate": "string"
        },
        "urn:ietf:params:scim:schemas:extension:spend:2.0:Approver": {
          "approverType": [
            "request"
          ]
        },
        "urn:ietf:params:scim:schemas:extension:spend:2.0:Delegate": {
          "delegateProdCode": [
            "payment"
          ]
        },
        "urn:ietf:params:scim:schemas:extension:spend:2.0:Role": {
          "roles": [
            {
              "roleGroups": [
                {}
              ],
              "roleName": {}
            }
          ]
        },
        "urn:ietf:params:scim:schemas:extension:spend:2.0:User": {
          "budgetCountryCode": "string",
          "cashAdvanceAccountCode": "string",
          "country": "string",
          "ledgerCode": "string",
          "locale": "string",
          "reimbursementCurrency": "string",
          "reimbursementType": "OTHER",
          "schemaCustomData": [
            {
              "id": "string",
              "value": "string"
            }
          ],
          "stateProvince": "string",
          "testEmployee": true
        },
        "urn:ietf:params:scim:schemas:extension:spend:2.0:UserPreference": {
          "allowCreditCardTransArrivalEmails": true,
          "allowReceiptImageAvailEmails": true,
          "autoAddTripCardTransOnReport": true,
          "defaultReportPrintFormat": "RECEIPTS",
          "expenseAuditRequired": "NEVER",
          "processorReportAccess": "All reports excluding returned",
          "promptForCardTransactionsOnReport": true,
          "promptForReportPrintFormat": true,
          "showExpenseOnReport": "ALL",
          "showImagingIntro": true,
          "showInstructHelpPanel": true,
          "showTotalOnReport": true,
          "useQuickItinAsDefault": true
        },
        "urn:ietf:params:scim:schemas:extension:spend:2.0:WorkflowPreference": {
          "emailAwaitApprovalOnCashAdvance": true,
          "emailAwaitApprovalOnPayment": true,
          "emailAwaitApprovalOnReport": true,
          "emailAwaitApprovalOnTravelRequest": true,
          "emailStatusChangeOnCashAdvance": true,
          "emailStatusChangeOnPayment": true,
          "emailStatusChangeOnReport": true,
          "emailStatusChangeOnTravelRequest": true,
          "promptForApproverOnPaymentSubmit": true,
          "promptForApproverOnReportSubmit": true,
          "promptForApproverOnTravelRequestSubmit": true
        },
        "urn:ietf:params:scim:schemas:extension:travel:2.0:User": {
          "customFields": [
            {
              "name": "string",
              "value": "string"
            }
          ],
          "groups": [
            0
          ],
          "manager": {
            "employeeNumber": "string",
            "value": "string"
          },
          "ruleClass": {
            "id": 0,
            "name": "string"
          },
          "travelCrsName": "string",
          "travelNameRemark": "string",
          "xmlProfileSyncId": "string"
        },
        "userName": "string"
      },
      "method": "POST",
      "bulkId": "string",
      "path": "/Users"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('https://us.api.concursolutions.com/provisioning/v4/Bulk',
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
  'Authorization' => 'API_KEY'
}

result = RestClient.post 'https://us.api.concursolutions.com/provisioning/v4/Bulk',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.post('https://us.api.concursolutions.com/provisioning/v4/Bulk', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','https://us.api.concursolutions.com/provisioning/v4/Bulk', array(
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
URL obj = new URL("https://us.api.concursolutions.com/provisioning/v4/Bulk");
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
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://us.api.concursolutions.com/provisioning/v4/Bulk", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /Bulk`

*Create a bulk provisioning request.*

> Body parameter

```json
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:BulkRequest"
  ],
  "Operations": [
    {
      "data": {
        "active": true,
        "addresses": [
          {
            "country": "string",
            "locality": "string",
            "postalCode": "string",
            "region": "string",
            "streetAddress": "string",
            "type": "work"
          }
        ],
        "dateOfBirth": "string",
        "displayName": "string",
        "emails": [
          {
            "dateAdded": "string",
            "dateVerified": "string",
            "notifications": true,
            "type": "work",
            "value": "string",
            "verified": true
          }
        ],
        "emergencyContacts": [
          {
            "country": "string",
            "emails": [
              "string"
            ],
            "locality": "string",
            "name": "string",
            "phones": [
              "string"
            ],
            "postalCode": "string",
            "region": "string",
            "relationship": "Spouse",
            "streetAddress": "string"
          }
        ],
        "entitlements": [
          "Expense"
        ],
        "externalId": "string",
        "gender": "Male",
        "id": "string",
        "localeOverrides": {
          "preference24Hour": "h:mm AM/PM",
          "preferenceCurrencySymbolLocation": "BeforeAmount",
          "preferenceDateFormat": "mm/dd/yyyy",
          "preferenceDefaultCalView": "day",
          "preferenceDistance": "mile",
          "preferenceEndDayViewHour": 0,
          "preferenceFirstDayOfWeek": "Monday",
          "preferenceHourMinuteSeparator": ":",
          "preferenceNegativeCurrencyFormat": "-100",
          "preferenceNegativeNumberFormat": "-100",
          "preferenceNumberFormat": "1,000.00",
          "preferenceStartDayViewHour": 0
        },
        "meta": {},
        "name": {
          "familyName": "string",
          "formatted": "string",
          "givenName": "string",
          "hasNoMiddleName": true,
          "honorificPrefix": "Miss",
          "honorificSuffix": "Jr.",
          "legalName": "string",
          "middleInitial": "string",
          "middleName": "string"
        },
        "nickName": "string",
        "phoneNumbers": [
          {
            "countryCode": "string",
            "display": "string",
            "notifications": true,
            "operatingSystem": "Android Phone",
            "primary": true,
            "type": "work",
            "value": "string"
          }
        ],
        "preferredLanguage": "string",
        "timezone": "string",
        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:Payroll": {
          "adp": {
            "companyCode": "string",
            "deductionCode": "string",
            "employeeFileNumber": "string"
          }
        },
        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
          "companyId": "string",
          "costCenter": "string",
          "department": "string",
          "division": "string",
          "employeeNumber": "string",
          "jobTitle": "string",
          "manager": {
            "$ref": "string",
            "displayName": "string",
            "employeeNumber": "string",
            "value": "string"
          },
          "orgUnit": "string",
          "organization": "string",
          "self": {
            "$ref": "string",
            "displayName": "string",
            "employeeNumber": "string",
            "value": "string"
          },
          "startDate": "string",
          "terminationDate": "string"
        },
        "urn:ietf:params:scim:schemas:extension:spend:2.0:Approver": {
          "approverType": [
            "request"
          ]
        },
        "urn:ietf:params:scim:schemas:extension:spend:2.0:Delegate": {
          "delegateProdCode": [
            "payment"
          ]
        },
        "urn:ietf:params:scim:schemas:extension:spend:2.0:Role": {
          "roles": [
            {
              "roleGroups": [
                {}
              ],
              "roleName": {}
            }
          ]
        },
        "urn:ietf:params:scim:schemas:extension:spend:2.0:User": {
          "budgetCountryCode": "string",
          "cashAdvanceAccountCode": "string",
          "country": "string",
          "ledgerCode": "string",
          "locale": "string",
          "reimbursementCurrency": "string",
          "reimbursementType": "OTHER",
          "schemaCustomData": [
            {
              "id": "string",
              "value": "string"
            }
          ],
          "stateProvince": "string",
          "testEmployee": true
        },
        "urn:ietf:params:scim:schemas:extension:spend:2.0:UserPreference": {
          "allowCreditCardTransArrivalEmails": true,
          "allowReceiptImageAvailEmails": true,
          "autoAddTripCardTransOnReport": true,
          "defaultReportPrintFormat": "RECEIPTS",
          "expenseAuditRequired": "NEVER",
          "processorReportAccess": "All reports excluding returned",
          "promptForCardTransactionsOnReport": true,
          "promptForReportPrintFormat": true,
          "showExpenseOnReport": "ALL",
          "showImagingIntro": true,
          "showInstructHelpPanel": true,
          "showTotalOnReport": true,
          "useQuickItinAsDefault": true
        },
        "urn:ietf:params:scim:schemas:extension:spend:2.0:WorkflowPreference": {
          "emailAwaitApprovalOnCashAdvance": true,
          "emailAwaitApprovalOnPayment": true,
          "emailAwaitApprovalOnReport": true,
          "emailAwaitApprovalOnTravelRequest": true,
          "emailStatusChangeOnCashAdvance": true,
          "emailStatusChangeOnPayment": true,
          "emailStatusChangeOnReport": true,
          "emailStatusChangeOnTravelRequest": true,
          "promptForApproverOnPaymentSubmit": true,
          "promptForApproverOnReportSubmit": true,
          "promptForApproverOnTravelRequestSubmit": true
        },
        "urn:ietf:params:scim:schemas:extension:travel:2.0:User": {
          "customFields": [
            {
              "name": "string",
              "value": "string"
            }
          ],
          "groups": [
            0
          ],
          "manager": {
            "employeeNumber": "string",
            "value": "string"
          },
          "ruleClass": {
            "id": 0,
            "name": "string"
          },
          "travelCrsName": "string",
          "travelNameRemark": "string",
          "xmlProfileSyncId": "string"
        },
        "userName": "string"
      },
      "method": "POST",
      "bulkId": "string",
      "path": "/Users"
    }
  ]
}
```

<h3 id="bulk.provision.create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[BulkRequest](#schemabulkrequest)|true|none|

> Example responses

> 202 Response

```json
{
  "id": "string",
  "itemsPerPage": 0,
  "operations": [
    {
      "bulkId": "string",
      "extensions": [
        {
          "messages": {
            "code": "string",
            "message": "string",
            "schemaPath": "string",
            "type": "error"
          },
          "name": "string",
          "status": {
            "code": "string",
            "completed": true,
            "result": "success",
            "success": true
          }
        }
      ],
      "id": "string",
      "resource": {
        "id": "string",
        "type": "User"
      },
      "status": {
        "completed": true,
        "success": true
      }
    }
  ],
  "startIndex": 0,
  "status": {
    "completed": true,
    "success": true
  },
  "totalResults": 0
}
```

<h3 id="bulk.provision.create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|accepted provision request|[ProvisionStatus](#schemaprovisionstatus)|
|default|Default|none|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth
</aside>

<h1 id="provisioning-apis-schemas">Schemas</h1>

## schema.get

<a id="opIdschema.get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://us.api.concursolutions.com/provisioning/v4/Schemas \
  -H 'Authorization: API_KEY'

```

```http
GET https://us.api.concursolutions.com/provisioning/v4/Schemas HTTP/1.1
Host: us.api.concursolutions.com

```

```javascript

const headers = {
  'Authorization':'API_KEY'
};

fetch('https://us.api.concursolutions.com/provisioning/v4/Schemas',
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
  'Authorization' => 'API_KEY'
}

result = RestClient.get 'https://us.api.concursolutions.com/provisioning/v4/Schemas',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Authorization': 'API_KEY'
}

r = requests.get('https://us.api.concursolutions.com/provisioning/v4/Schemas', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://us.api.concursolutions.com/provisioning/v4/Schemas', array(
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
URL obj = new URL("https://us.api.concursolutions.com/provisioning/v4/Schemas");
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
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://us.api.concursolutions.com/provisioning/v4/Schemas", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /Schemas`

*Get all supported schemas.*

<h3 id="schema.get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|default|Default|none|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth
</aside>

## schema.id.get

<a id="opIdschema.id.get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://us.api.concursolutions.com/provisioning/v4/Schemas/{id} \
  -H 'Authorization: API_KEY'

```

```http
GET https://us.api.concursolutions.com/provisioning/v4/Schemas/{id} HTTP/1.1
Host: us.api.concursolutions.com

```

```javascript

const headers = {
  'Authorization':'API_KEY'
};

fetch('https://us.api.concursolutions.com/provisioning/v4/Schemas/{id}',
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
  'Authorization' => 'API_KEY'
}

result = RestClient.get 'https://us.api.concursolutions.com/provisioning/v4/Schemas/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Authorization': 'API_KEY'
}

r = requests.get('https://us.api.concursolutions.com/provisioning/v4/Schemas/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://us.api.concursolutions.com/provisioning/v4/Schemas/{id}', array(
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
URL obj = new URL("https://us.api.concursolutions.com/provisioning/v4/Schemas/{id}");
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
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://us.api.concursolutions.com/provisioning/v4/Schemas/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /Schemas/{id}`

*Get a schema.*

<h3 id="schema.id.get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|none|

<h3 id="schema.id.get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|default|Default|none|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth
</aside>

<h1 id="provisioning-apis-serviceproviderconfig">ServiceProviderConfig</h1>

## serviceproviderconfig.get

<a id="opIdserviceproviderconfig.get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET https://us.api.concursolutions.com/provisioning/v4/ServiceProviderConfig \
  -H 'Authorization: API_KEY'

```

```http
GET https://us.api.concursolutions.com/provisioning/v4/ServiceProviderConfig HTTP/1.1
Host: us.api.concursolutions.com

```

```javascript

const headers = {
  'Authorization':'API_KEY'
};

fetch('https://us.api.concursolutions.com/provisioning/v4/ServiceProviderConfig',
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
  'Authorization' => 'API_KEY'
}

result = RestClient.get 'https://us.api.concursolutions.com/provisioning/v4/ServiceProviderConfig',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Authorization': 'API_KEY'
}

r = requests.get('https://us.api.concursolutions.com/provisioning/v4/ServiceProviderConfig', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','https://us.api.concursolutions.com/provisioning/v4/ServiceProviderConfig', array(
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
URL obj = new URL("https://us.api.concursolutions.com/provisioning/v4/ServiceProviderConfig");
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
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://us.api.concursolutions.com/provisioning/v4/ServiceProviderConfig", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /ServiceProviderConfig`

*SCIM service provider configuration representation/implementation details.*

<h3 id="serviceproviderconfig.get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|default|Default|none|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth
</aside>

# Schemas

<h2 id="tocS_WorkflowPreferenceExtension">WorkflowPreferenceExtension</h2>

<a id="schemaworkflowpreferenceextension"></a>
<a id="schema_WorkflowPreferenceExtension"></a>
<a id="tocSworkflowpreferenceextension"></a>
<a id="tocsworkflowpreferenceextension"></a>

```json
{
  "emailAwaitApprovalOnCashAdvance": true,
  "emailAwaitApprovalOnPayment": true,
  "emailAwaitApprovalOnReport": true,
  "emailAwaitApprovalOnTravelRequest": true,
  "emailStatusChangeOnCashAdvance": true,
  "emailStatusChangeOnPayment": true,
  "emailStatusChangeOnReport": true,
  "emailStatusChangeOnTravelRequest": true,
  "promptForApproverOnPaymentSubmit": true,
  "promptForApproverOnReportSubmit": true,
  "promptForApproverOnTravelRequestSubmit": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|emailAwaitApprovalOnCashAdvance|boolean|false|none|Send email when a cash advance is awaiting approval, defaulted to true.|
|emailAwaitApprovalOnPayment|boolean|false|none|Send email when a payment is awaiting approval, defaulted to true.|
|emailAwaitApprovalOnReport|boolean|false|none|Send email when a report is awaiting approval, defaulted to true.|
|emailAwaitApprovalOnTravelRequest|boolean|false|none|Send email when a travel request is awaiting approval, defaulted to true.|
|emailStatusChangeOnCashAdvance|boolean|false|none|Send email when the cash advance status changes, defaulted to true.|
|emailStatusChangeOnPayment|boolean|false|none|Send email when the payment status changes, defaulted to true.|
|emailStatusChangeOnReport|boolean|false|none|Send email when the report status changes, defaulted to true.|
|emailStatusChangeOnTravelRequest|boolean|false|none|Send email when the travel request status changes, defaulted to true.|
|promptForApproverOnPaymentSubmit|boolean|false|none|Prompt for approver when submitting a payment, defaulted to false.|
|promptForApproverOnReportSubmit|boolean|false|none|Prompt for approver when submitting a report, defaulted to false.|
|promptForApproverOnTravelRequestSubmit|boolean|false|none|Prompt for approver when submitting a travel request, defaulted to false.|

<h2 id="tocS_BulkRequest">BulkRequest</h2>

<a id="schemabulkrequest"></a>
<a id="schema_BulkRequest"></a>
<a id="tocSbulkrequest"></a>
<a id="tocsbulkrequest"></a>

```json
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:BulkRequest"
  ],
  "Operations": [
    {
      "data": {
        "active": true,
        "addresses": [
          {
            "country": "string",
            "locality": "string",
            "postalCode": "string",
            "region": "string",
            "streetAddress": "string",
            "type": "work"
          }
        ],
        "dateOfBirth": "string",
        "displayName": "string",
        "emails": [
          {
            "dateAdded": "string",
            "dateVerified": "string",
            "notifications": true,
            "type": "work",
            "value": "string",
            "verified": true
          }
        ],
        "emergencyContacts": [
          {
            "country": "string",
            "emails": [
              "string"
            ],
            "locality": "string",
            "name": "string",
            "phones": [
              "string"
            ],
            "postalCode": "string",
            "region": "string",
            "relationship": "Spouse",
            "streetAddress": "string"
          }
        ],
        "entitlements": [
          "Expense"
        ],
        "externalId": "string",
        "gender": "Male",
        "id": "string",
        "localeOverrides": {
          "preference24Hour": "h:mm AM/PM",
          "preferenceCurrencySymbolLocation": "BeforeAmount",
          "preferenceDateFormat": "mm/dd/yyyy",
          "preferenceDefaultCalView": "day",
          "preferenceDistance": "mile",
          "preferenceEndDayViewHour": 0,
          "preferenceFirstDayOfWeek": "Monday",
          "preferenceHourMinuteSeparator": ":",
          "preferenceNegativeCurrencyFormat": "-100",
          "preferenceNegativeNumberFormat": "-100",
          "preferenceNumberFormat": "1,000.00",
          "preferenceStartDayViewHour": 0
        },
        "meta": {},
        "name": {
          "familyName": "string",
          "formatted": "string",
          "givenName": "string",
          "hasNoMiddleName": true,
          "honorificPrefix": "Miss",
          "honorificSuffix": "Jr.",
          "legalName": "string",
          "middleInitial": "string",
          "middleName": "string"
        },
        "nickName": "string",
        "phoneNumbers": [
          {
            "countryCode": "string",
            "display": "string",
            "notifications": true,
            "operatingSystem": "Android Phone",
            "primary": true,
            "type": "work",
            "value": "string"
          }
        ],
        "preferredLanguage": "string",
        "timezone": "string",
        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:Payroll": {
          "adp": {
            "companyCode": "string",
            "deductionCode": "string",
            "employeeFileNumber": "string"
          }
        },
        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
          "companyId": "string",
          "costCenter": "string",
          "department": "string",
          "division": "string",
          "employeeNumber": "string",
          "jobTitle": "string",
          "manager": {
            "$ref": "string",
            "displayName": "string",
            "employeeNumber": "string",
            "value": "string"
          },
          "orgUnit": "string",
          "organization": "string",
          "self": {
            "$ref": "string",
            "displayName": "string",
            "employeeNumber": "string",
            "value": "string"
          },
          "startDate": "string",
          "terminationDate": "string"
        },
        "urn:ietf:params:scim:schemas:extension:spend:2.0:Approver": {
          "approverType": [
            "request"
          ]
        },
        "urn:ietf:params:scim:schemas:extension:spend:2.0:Delegate": {
          "delegateProdCode": [
            "payment"
          ]
        },
        "urn:ietf:params:scim:schemas:extension:spend:2.0:Role": {
          "roles": [
            {
              "roleGroups": [
                {}
              ],
              "roleName": {}
            }
          ]
        },
        "urn:ietf:params:scim:schemas:extension:spend:2.0:User": {
          "budgetCountryCode": "string",
          "cashAdvanceAccountCode": "string",
          "country": "string",
          "ledgerCode": "string",
          "locale": "string",
          "reimbursementCurrency": "string",
          "reimbursementType": "OTHER",
          "schemaCustomData": [
            {
              "id": "string",
              "value": "string"
            }
          ],
          "stateProvince": "string",
          "testEmployee": true
        },
        "urn:ietf:params:scim:schemas:extension:spend:2.0:UserPreference": {
          "allowCreditCardTransArrivalEmails": true,
          "allowReceiptImageAvailEmails": true,
          "autoAddTripCardTransOnReport": true,
          "defaultReportPrintFormat": "RECEIPTS",
          "expenseAuditRequired": "NEVER",
          "processorReportAccess": "All reports excluding returned",
          "promptForCardTransactionsOnReport": true,
          "promptForReportPrintFormat": true,
          "showExpenseOnReport": "ALL",
          "showImagingIntro": true,
          "showInstructHelpPanel": true,
          "showTotalOnReport": true,
          "useQuickItinAsDefault": true
        },
        "urn:ietf:params:scim:schemas:extension:spend:2.0:WorkflowPreference": {
          "emailAwaitApprovalOnCashAdvance": true,
          "emailAwaitApprovalOnPayment": true,
          "emailAwaitApprovalOnReport": true,
          "emailAwaitApprovalOnTravelRequest": true,
          "emailStatusChangeOnCashAdvance": true,
          "emailStatusChangeOnPayment": true,
          "emailStatusChangeOnReport": true,
          "emailStatusChangeOnTravelRequest": true,
          "promptForApproverOnPaymentSubmit": true,
          "promptForApproverOnReportSubmit": true,
          "promptForApproverOnTravelRequestSubmit": true
        },
        "urn:ietf:params:scim:schemas:extension:travel:2.0:User": {
          "customFields": [
            {
              "name": "string",
              "value": "string"
            }
          ],
          "groups": [
            0
          ],
          "manager": {
            "employeeNumber": "string",
            "value": "string"
          },
          "ruleClass": {
            "id": 0,
            "name": "string"
          },
          "travelCrsName": "string",
          "travelNameRemark": "string",
          "xmlProfileSyncId": "string"
        },
        "userName": "string"
      },
      "method": "POST",
      "bulkId": "string",
      "path": "/Users"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|schemas|[string]|false|none|none|
|Operations|[object]|false|none|none|
|» data|[User](#schemauser)|false|none|none|
|» method|string|false|none|HTTP Method|
|» bulkId|string|false|none|Transient identifier of newly created resource, unique within a bulk request. REQUIRED when "method" is "POST"|
|» path|string|false|none|Resource Path|

#### Enumerated Values

|Property|Value|
|---|---|
|method|POST|
|method|PUT|
|method|PATCH|
|path|/Users|

<h2 id="tocS_SpendDelegate">SpendDelegate</h2>

<a id="schemaspenddelegate"></a>
<a id="schema_SpendDelegate"></a>
<a id="tocSspenddelegate"></a>
<a id="tocsspenddelegate"></a>

```json
{
  "delegateProdCode": [
    "payment"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|delegateProdCode|[object]|false|none|A list of Delegate associated with the Delegate's product code.|
|» canApprove|boolean|false|none|Determines if delegate can approve|
|» canPrepare|boolean|false|none|Determines if delegate can prepare|
|» canPrepareForApproval|boolean|false|none|Determines if delegate can prepare for approval|
|» canReceiveApprovalEmail|boolean|false|none|Determines if delegate can receive approval emails|
|» canReceiveEmail|boolean|false|none|Determines if delegate can receive emails|
|» canSubmit|boolean|false|none|Determines if delegate can submit|
|» canSubmitTravelRequest|boolean|false|none|Determines if delegate can submit travel request|
|» canUseBi|boolean|false|none|Determines if delegate can use BI|
|» canViewReceipt|boolean|false|none|Determines if delegate can view receipts|
|» delegate|object|true|none|UserReference for the delegate|
|»» $ref|string|false|none|The URI reference for the user|
|»» displayName|string|false|none|The username for the user|
|»» employeeNumber|string|true|none|The employee number for the user|
|»» value|object|false|none|The internal UUID identifier for the user|
|» temporaryDelegation|object|false|none|Determines if delegate can temporarily approve|
|»» temporaryDelegationFromDate|string|false|none|Start date for delegates temporary approval permissions|
|»» temporaryDelegationToDate|string|false|none|End date for delegates temporary approval permissions|

<h2 id="tocS_TravelUser">TravelUser</h2>

<a id="schematraveluser"></a>
<a id="schema_TravelUser"></a>
<a id="tocStraveluser"></a>
<a id="tocstraveluser"></a>

```json
{
  "customFields": [
    {
      "name": "string",
      "value": "string"
    }
  ],
  "groups": [
    0
  ],
  "manager": {
    "employeeNumber": "string",
    "value": "string"
  },
  "ruleClass": {
    "id": 0,
    "name": "string"
  },
  "travelCrsName": "string",
  "travelNameRemark": "string",
  "xmlProfileSyncId": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|customFields|[object]|false|none|user can set values to custom data fields|
|» name|string|false|none|Name of the custom field|
|» value|string|false|none|Value for the given custom field|
|groups|[integer]|false|none|List of user groups that user belongs to for certain permissions|
|manager|object|false|none|Travel approver of this user|
|» employeeNumber|string|false|none|The referenced user's employee number|
|» value|string|false|none|The referenced user's UUID|
|ruleClass|object|true|none|Defines the rule class for the travel user either id or name should be provided|
|» id|integer|false|none|valid Rule class id to be assigned|
|» name|string|false|none|valid name of rule class|
|travelCrsName|string|true|none|The name of the profile in the GDS system|
|travelNameRemark|string|false|none|ravel name remark|
|xmlProfileSyncId|string|false|none|client-assigned Travel user identifier that allows the user profile to be synchronized with other vendors|

<h2 id="tocS_User">User</h2>

<a id="schemauser"></a>
<a id="schema_User"></a>
<a id="tocSuser"></a>
<a id="tocsuser"></a>

```json
{
  "active": true,
  "addresses": [
    {
      "country": "string",
      "locality": "string",
      "postalCode": "string",
      "region": "string",
      "streetAddress": "string",
      "type": "work"
    }
  ],
  "dateOfBirth": "string",
  "displayName": "string",
  "emails": [
    {
      "dateAdded": "string",
      "dateVerified": "string",
      "notifications": true,
      "type": "work",
      "value": "string",
      "verified": true
    }
  ],
  "emergencyContacts": [
    {
      "country": "string",
      "emails": [
        "string"
      ],
      "locality": "string",
      "name": "string",
      "phones": [
        "string"
      ],
      "postalCode": "string",
      "region": "string",
      "relationship": "Spouse",
      "streetAddress": "string"
    }
  ],
  "entitlements": [
    "Expense"
  ],
  "externalId": "string",
  "gender": "Male",
  "id": "string",
  "localeOverrides": {
    "preference24Hour": "h:mm AM/PM",
    "preferenceCurrencySymbolLocation": "BeforeAmount",
    "preferenceDateFormat": "mm/dd/yyyy",
    "preferenceDefaultCalView": "day",
    "preferenceDistance": "mile",
    "preferenceEndDayViewHour": 0,
    "preferenceFirstDayOfWeek": "Monday",
    "preferenceHourMinuteSeparator": ":",
    "preferenceNegativeCurrencyFormat": "-100",
    "preferenceNegativeNumberFormat": "-100",
    "preferenceNumberFormat": "1,000.00",
    "preferenceStartDayViewHour": 0
  },
  "meta": {},
  "name": {
    "familyName": "string",
    "formatted": "string",
    "givenName": "string",
    "hasNoMiddleName": true,
    "honorificPrefix": "Miss",
    "honorificSuffix": "Jr.",
    "legalName": "string",
    "middleInitial": "string",
    "middleName": "string"
  },
  "nickName": "string",
  "phoneNumbers": [
    {
      "countryCode": "string",
      "display": "string",
      "notifications": true,
      "operatingSystem": "Android Phone",
      "primary": true,
      "type": "work",
      "value": "string"
    }
  ],
  "preferredLanguage": "string",
  "timezone": "string",
  "urn:ietf:params:scim:schemas:extension:enterprise:2.0:Payroll": {
    "adp": {
      "companyCode": "string",
      "deductionCode": "string",
      "employeeFileNumber": "string"
    }
  },
  "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
    "companyId": "string",
    "costCenter": "string",
    "department": "string",
    "division": "string",
    "employeeNumber": "string",
    "jobTitle": "string",
    "manager": {
      "$ref": "string",
      "displayName": "string",
      "employeeNumber": "string",
      "value": "string"
    },
    "orgUnit": "string",
    "organization": "string",
    "self": {
      "$ref": "string",
      "displayName": "string",
      "employeeNumber": "string",
      "value": "string"
    },
    "startDate": "string",
    "terminationDate": "string"
  },
  "urn:ietf:params:scim:schemas:extension:spend:2.0:Approver": {
    "approverType": [
      "request"
    ]
  },
  "urn:ietf:params:scim:schemas:extension:spend:2.0:Delegate": {
    "delegateProdCode": [
      "payment"
    ]
  },
  "urn:ietf:params:scim:schemas:extension:spend:2.0:Role": {
    "roles": [
      {
        "roleGroups": [
          {}
        ],
        "roleName": {}
      }
    ]
  },
  "urn:ietf:params:scim:schemas:extension:spend:2.0:User": {
    "budgetCountryCode": "string",
    "cashAdvanceAccountCode": "string",
    "country": "string",
    "ledgerCode": "string",
    "locale": "string",
    "reimbursementCurrency": "string",
    "reimbursementType": "OTHER",
    "schemaCustomData": [
      {
        "id": "string",
        "value": "string"
      }
    ],
    "stateProvince": "string",
    "testEmployee": true
  },
  "urn:ietf:params:scim:schemas:extension:spend:2.0:UserPreference": {
    "allowCreditCardTransArrivalEmails": true,
    "allowReceiptImageAvailEmails": true,
    "autoAddTripCardTransOnReport": true,
    "defaultReportPrintFormat": "RECEIPTS",
    "expenseAuditRequired": "NEVER",
    "processorReportAccess": "All reports excluding returned",
    "promptForCardTransactionsOnReport": true,
    "promptForReportPrintFormat": true,
    "showExpenseOnReport": "ALL",
    "showImagingIntro": true,
    "showInstructHelpPanel": true,
    "showTotalOnReport": true,
    "useQuickItinAsDefault": true
  },
  "urn:ietf:params:scim:schemas:extension:spend:2.0:WorkflowPreference": {
    "emailAwaitApprovalOnCashAdvance": true,
    "emailAwaitApprovalOnPayment": true,
    "emailAwaitApprovalOnReport": true,
    "emailAwaitApprovalOnTravelRequest": true,
    "emailStatusChangeOnCashAdvance": true,
    "emailStatusChangeOnPayment": true,
    "emailStatusChangeOnReport": true,
    "emailStatusChangeOnTravelRequest": true,
    "promptForApproverOnPaymentSubmit": true,
    "promptForApproverOnReportSubmit": true,
    "promptForApproverOnTravelRequestSubmit": true
  },
  "urn:ietf:params:scim:schemas:extension:travel:2.0:User": {
    "customFields": [
      {
        "name": "string",
        "value": "string"
      }
    ],
    "groups": [
      0
    ],
    "manager": {
      "employeeNumber": "string",
      "value": "string"
    },
    "ruleClass": {
      "id": 0,
      "name": "string"
    },
    "travelCrsName": "string",
    "travelNameRemark": "string",
    "xmlProfileSyncId": "string"
  },
  "userName": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|active|boolean|true|none|A Boolean value indicating whether the User is active.|
|addresses|[object]|false|none|A physical mailing address for this User. Canonical type values of 'work', 'home', and 'other'. This attribute is a complex type with the following sub-attributes.|
|» country|string|false|none|A two-letter country code defined in ISO 3166-1 alpha-2|
|» locality|string|false|none|The city or locality.|
|» postalCode|string|false|none|The zip code or postal code.|
|» region|string|false|none|The state or region.|
|» streetAddress|string|false|none|The full street address component, which may include house number, street name, P.O. box, and multi-line extended street address information.  This attribute MAY contain newlines.|
|» type|string|false|none|A label indicating the function of the address, e.g., 'work' or 'home'.|
|dateOfBirth|string|false|none|The user's date of birth , in YYYY-MM-DD format|
|displayName|string|false|none|The name of the User, suitable for display to end-users.|
|emails|[object]|true|none|Email addresses for the user. The value SHOULD be canonicalized by the service provider, e.g., 'bjensen@example.com' instead of 'bjensen@EXAMPLE.COM'. Canonical type values of 'work', 'home', and 'other'.|
|» dateAdded|string|false|none|The date and time the email was added to the user's profile.|
|» dateVerified|string|false|none|The date and time the email was verified|
|» notifications|boolean|false|none|Notifications opt-in for emails|
|» type|string|false|none|A label indicating the attribute's function, e.g., 'Work' or 'Home'.|
|» value|string|true|none|Email address value|
|» verified|boolean|false|none|flag to note which email has been verified by the user.|
|emergencyContacts|[object]|false|none|Emergency Contact information for the User.|
|» country|string|false|none|A two-letter country code defined in ISO 3166-1 alpha-2|
|» emails|[string]|false|none|Emails of the contact|
|» locality|string|false|none|The city or locality.|
|» name|string|false|none|Contact name.|
|» phones|[string]|false|none|Phone numbers of the contact|
|» postalCode|string|false|none|The zip code or postal code.|
|» region|string|false|none|The state or region.|
|» relationship|string|true|none|Emergency contact relationship.|
|» streetAddress|string|false|none|The full street address component, which may include house number, street name, P.O. box, and multi-line extended street address information.  This attribute MAY contain newlines.|
|entitlements|[string]|false|none|The features enabled for the user|
|externalId|string|false|none|User identifier from the provisioning client|
|gender|string|false|none|The user's gender|
|id|string|true|none|Unique identifier for the user - a uuid|
|localeOverrides|object|false|none|Support for users who want to override locale settings|
|» preference24Hour|string|false|none|preferred 24 hour format for the user|
|» preferenceCurrencySymbolLocation|string|false|none|preferred currency symbol location for the user|
|» preferenceDateFormat|string|false|none|preferred date format for the user|
|» preferenceDefaultCalView|string|false|none|preferred default calendar view for the user|
|» preferenceDistance|string|false|none|preferred distance metric|
|» preferenceEndDayViewHour|integer|false|none|preferred hour setting for the end of day, 0-23|
|» preferenceFirstDayOfWeek|string|false|none|preferred first day of the week for the user|
|» preferenceHourMinuteSeparator|string|false|none|preferred separator between hour and minute|
|» preferenceNegativeCurrencyFormat|string|false|none|preferred negative currency format for the user|
|» preferenceNegativeNumberFormat|string|false|none|preferred negative number format for the user|
|» preferenceNumberFormat|string|false|none|preferred number format for the user|
|» preferenceStartDayViewHour|integer|false|none|preferred start of day for the user, from 1|
|meta|object|false|none|none|
|name|object|true|none|The user's name|
|» familyName|string|true|none|The family name of the User, or last name in most Western languages (e.g., 'Jensen' given the full name 'Ms. Barbara J Jensen, III').|
|» formatted|string|false|none|The full name, formatted for display (e.g., 'Jensen, Barbara Jane').|
|» givenName|string|true|none|The given name of the User, or first name in most Western languages (e.g., 'Barbara' given the full name 'Ms. Barbara J Jensen, III').|
|» hasNoMiddleName|boolean|false|none|A boolean indicating that the user does not have a middle name|
|» honorificPrefix|string|false|none|The honorific prefix(es) of the User, or title in most Western languages (e.g., 'Ms.' given the full name 'Ms. Barbara J Jensen, III').|
|» honorificSuffix|string|false|none|The honorific suffix(es) of the User, or  suffix in most Western languages (e.g., 'III' given the full name  'Ms. Barbara J Jensen, III').|
|» legalName|string|false|none|The legal name of the User (e.g., 'Jane' given the full name 'Ms. Barbara J Jensen, III').|
|» middleInitial|string|false|none|middle initial, if the user has a middle name|
|» middleName|string|false|none|The middle name(s) of the User (e.g., 'Jane' given the full name 'Ms. Barbara J Jensen, III').|
|nickName|string|false|none|The casual way to address the user in real  life, e.g., 'Bob' or 'Bobby' instead of 'Robert'.  This attribute  SHOULD NOT be used to represent a User's username (e.g., 'bjensen' or  'mpepperidge').|
|phoneNumbers|[object]|false|none|Phone numbers for the User.  The value SHOULD be canonicalized by the service provider according to the format specified in RFC 3966, e.g., 'tel:+1-201-555-0123'. Canonical type values of 'work', 'home', 'mobile', 'fax', 'pager', and 'other'.|
|» countryCode|string|false|none|A two-letter code defined in ISO 3166-1 alpha-2 denoting the country the phone number was issued in. e.g., US|
|» display|string|false|none|A human-readable phone number for display|
|» notifications|boolean|false|none|LNA Opt-in for mobile devices (type=Mobile)|
|» operatingSystem|string|false|none|The OS of the  device, when the phone is a cellphone type|
|» primary|boolean|false|none|Primary device for mobile devices (type=Mobile)|
|» type|string|false|none|A label indicating the attribute's function, e.g., 'Work', 'Home'.|
|» value|string|false|none|Phone number value|
|preferredLanguage|string|false|none|Indicates the User's preferred written or spoken language.  Generally used for selecting a localized user interface|
|timezone|string|false|none|The User's time zone in the 'Olson' time zone database format, e.g., 'America/Los_Angeles'.|
|urn:ietf:params:scim:schemas:extension:enterprise:2.0:Payroll|[PayrollExtension](#schemapayrollextension)|false|none|none|
|urn:ietf:params:scim:schemas:extension:enterprise:2.0:User|[EnterpriseUser](#schemaenterpriseuser)|false|none|none|
|urn:ietf:params:scim:schemas:extension:spend:2.0:Approver|[SpendApprover](#schemaspendapprover)|false|none|none|
|urn:ietf:params:scim:schemas:extension:spend:2.0:Delegate|[SpendDelegate](#schemaspenddelegate)|false|none|none|
|urn:ietf:params:scim:schemas:extension:spend:2.0:Role|[SpendRole](#schemaspendrole)|false|none|none|
|urn:ietf:params:scim:schemas:extension:spend:2.0:User|[SpendUser](#schemaspenduser)|false|none|none|
|urn:ietf:params:scim:schemas:extension:spend:2.0:UserPreference|[ExpenseUserPreferenceExtension](#schemaexpenseuserpreferenceextension)|false|none|none|
|urn:ietf:params:scim:schemas:extension:spend:2.0:WorkflowPreference|[WorkflowPreferenceExtension](#schemaworkflowpreferenceextension)|false|none|none|
|urn:ietf:params:scim:schemas:extension:travel:2.0:User|[TravelUser](#schematraveluser)|false|none|none|
|userName|string|true|none|The name that can be used to login to CTE|

#### Enumerated Values

|Property|Value|
|---|---|
|type|work|
|type|home|
|type|other|
|type|billing|
|type|bank|
|type|shipping|
|type|work|
|type|home|
|type|other|
|type|other2|
|type|work2|
|type|sms|
|relationship|Spouse|
|relationship|Brother|
|relationship|Parent|
|relationship|Sister|
|relationship|Life Partner|
|relationship|Other|
|gender|Male|
|gender|Female|
|gender|Others|
|preference24Hour|h:mm AM/PM|
|preference24Hour|H:mm|
|preferenceCurrencySymbolLocation|BeforeAmount|
|preferenceCurrencySymbolLocation|AfterAmount|
|preferenceDateFormat|mm/dd/yyyy|
|preferenceDateFormat|mm.dd.yyyy|
|preferenceDateFormat|mm-dd-yyyy|
|preferenceDateFormat|dd/mm/yyyy|
|preferenceDateFormat|dd.mm.yyyy|
|preferenceDateFormat|dd-mm-yyyy|
|preferenceDateFormat|yyyy/mm/dd|
|preferenceDateFormat|yyyy.mm.dd|
|preferenceDateFormat|yyyy-mm-dd|
|preferenceDefaultCalView|day|
|preferenceDefaultCalView|week|
|preferenceDefaultCalView|month|
|preferenceDistance|mile|
|preferenceDistance|km|
|preferenceFirstDayOfWeek|Monday|
|preferenceFirstDayOfWeek|Tuesday|
|preferenceFirstDayOfWeek|Wednesday|
|preferenceFirstDayOfWeek|Thursday|
|preferenceFirstDayOfWeek|Friday|
|preferenceFirstDayOfWeek|Saturday|
|preferenceFirstDayOfWeek|Sunday|
|preferenceHourMinuteSeparator|:|
|preferenceHourMinuteSeparator|.|
|preferenceNegativeCurrencyFormat|-100|
|preferenceNegativeCurrencyFormat|(100)|
|preferenceNegativeNumberFormat|-100|
|preferenceNegativeNumberFormat|(100)|
|preferenceNumberFormat|1,000.00|
|preferenceNumberFormat|1.000,00|
|preferenceNumberFormat|1 000,00|
|preferenceNumberFormat|1'000.00|
|preferenceNumberFormat|1'000,00|
|honorificPrefix|Miss|
|honorificPrefix|Mr|
|honorificPrefix|Mrs|
|honorificPrefix|Ms|
|honorificPrefix|Mx|
|honorificPrefix|B.A.|
|honorificPrefix|B.Sc.|
|honorificPrefix|CPA|
|honorificPrefix|D.D.|
|honorificPrefix|D.D.S.|
|honorificPrefix|D.P.S.|
|honorificPrefix|Dr|
|honorificPrefix|Dr Mr|
|honorificPrefix|Dr Mrs|
|honorificPrefix|Dr Ms|
|honorificPrefix|Eng.|
|honorificPrefix|Ing.|
|honorificPrefix|Lady|
|honorificPrefix|Lord|
|honorificPrefix|M.D.|
|honorificPrefix|MBA|
|honorificPrefix|P.Eng.|
|honorificPrefix|Ph.D|
|honorificPrefix|Ph.D.|
|honorificPrefix|Prof|
|honorificPrefix|Prof Dr|
|honorificPrefix|Prof Dr Mr|
|honorificPrefix|Prof Dr Mrs|
|honorificPrefix|Prof Dr Ms|
|honorificPrefix|Prof Mr|
|honorificPrefix|Prof Mrs|
|honorificPrefix|Prof Ms|
|honorificPrefix|Rev|
|honorificPrefix|Sir|
|honorificSuffix|Jr.|
|honorificSuffix|Sr.|
|honorificSuffix|I|
|honorificSuffix|II|
|honorificSuffix|III|
|honorificSuffix|IV|
|honorificSuffix|V|
|honorificSuffix|VI|
|operatingSystem|Android Phone|
|operatingSystem|Android Tablet|
|operatingSystem|Blackberry|
|operatingSystem|iOS Phone|
|operatingSystem|iOS Tablet|
|operatingSystem|Not a smartphone|
|operatingSystem|Other iOS device|
|operatingSystem|Other smartphone|
|operatingSystem|Unknown|
|operatingSystem|Window Mobile|
|type|work|
|type|home|
|type|mobile|
|type|fax|
|type|pager|
|type|other|
|type|work2|

<h2 id="tocS_ConcurError">ConcurError</h2>

<a id="schemaconcurerror"></a>
<a id="schema_ConcurError"></a>
<a id="tocSconcurerror"></a>
<a id="tocsconcurerror"></a>

```json
{
  "messages": {
    "code": "string",
    "message": "string",
    "schemaPath": "string",
    "type": "error"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|messages|object|false|none|Additional messages in case of errors / warnings|
|» code|string|true|none|Message Code|
|» message|string|false|none|Message description|
|» schemaPath|string|false|none|Relative schema path of attribute|
|» type|string|true|none|Message Type|

#### Enumerated Values

|Property|Value|
|---|---|
|type|error|
|type|warning|

<h2 id="tocS_SpendApprover">SpendApprover</h2>

<a id="schemaspendapprover"></a>
<a id="schema_SpendApprover"></a>
<a id="tocSspendapprover"></a>
<a id="tocsspendapprover"></a>

```json
{
  "approverType": [
    "request"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|approverType|[object]|false|none|A list of Approvers associated with the Approver's type.|
|» approver|object|false|none|The user reference for the approver|
|»» $ref|string|false|none|The URI reference for the user|
|»» displayName|string|false|none|The username for the user|
|»» employeeNumber|string|true|none|The employee number for the user|
|»» value|object|false|none|The internal UUID identifier for the user|
|» primary|boolean|true|none|The value for indicating whether the associated user is primary approver|

<h2 id="tocS_PayrollExtension">PayrollExtension</h2>

<a id="schemapayrollextension"></a>
<a id="schema_PayrollExtension"></a>
<a id="tocSpayrollextension"></a>
<a id="tocspayrollextension"></a>

```json
{
  "adp": {
    "companyCode": "string",
    "deductionCode": "string",
    "employeeFileNumber": "string"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|adp|object|false|none|Adp settings for Employee|
|» companyCode|string|true|none|The company code for the employee within ADP.|
|» deductionCode|string|true|none|The deduction code for the employee within ADP.|
|» employeeFileNumber|string|true|none|The identifier for the employee within ADP, also known as the "Employee File Number".|

<h2 id="tocS_EnterpriseUser">EnterpriseUser</h2>

<a id="schemaenterpriseuser"></a>
<a id="schema_EnterpriseUser"></a>
<a id="tocSenterpriseuser"></a>
<a id="tocsenterpriseuser"></a>

```json
{
  "companyId": "string",
  "costCenter": "string",
  "department": "string",
  "division": "string",
  "employeeNumber": "string",
  "jobTitle": "string",
  "manager": {
    "$ref": "string",
    "displayName": "string",
    "employeeNumber": "string",
    "value": "string"
  },
  "orgUnit": "string",
  "organization": "string",
  "self": {
    "$ref": "string",
    "displayName": "string",
    "employeeNumber": "string",
    "value": "string"
  },
  "startDate": "string",
  "terminationDate": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|companyId|string|true|none|Concur ID of the company|
|costCenter|string|false|none|employee cost center for product|
|department|string|false|none|Client supplied department name|
|division|string|false|none|Client supplied division name|
|employeeNumber|string|false|none|Client supplied employee's number within the company, unique for the company|
|jobTitle|string|false|none|user's job title in the company|
|manager|object|false|none|The manager of this user|
|» $ref|string|false|none|The URI of the SCIM resource representing the referenced user.|
|» displayName|string|false|none|The referenced user's display name|
|» employeeNumber|string|false|none|The referenced user's employee number, if it is an Enterprise user|
|» value|string|false|none|The referenced user's UUID|
|orgUnit|string|false|none|Client supplied org unit name|
|organization|string|false|none|Company name|
|self|object|false|none|A reference to this user|
|» $ref|string|false|none|The URI of the SCIM resource representing the referenced user.|
|» displayName|string|false|none|The referenced user's display name|
|» employeeNumber|string|false|none|The referenced user's employee number, if it is an Enterprise user|
|» value|string|false|none|The referenced user's UUID|
|startDate|string|false|none|Start Date, in YYYY-MM-DD format|
|terminationDate|string|false|none|Termination Date, in YYYY-MM-DD format, if the employee is terminated, this can also be used to calculate the data retention period|

<h2 id="tocS_ExpenseUserPreferenceExtension">ExpenseUserPreferenceExtension</h2>

<a id="schemaexpenseuserpreferenceextension"></a>
<a id="schema_ExpenseUserPreferenceExtension"></a>
<a id="tocSexpenseuserpreferenceextension"></a>
<a id="tocsexpenseuserpreferenceextension"></a>

```json
{
  "allowCreditCardTransArrivalEmails": true,
  "allowReceiptImageAvailEmails": true,
  "autoAddTripCardTransOnReport": true,
  "defaultReportPrintFormat": "RECEIPTS",
  "expenseAuditRequired": "NEVER",
  "processorReportAccess": "All reports excluding returned",
  "promptForCardTransactionsOnReport": true,
  "promptForReportPrintFormat": true,
  "showExpenseOnReport": "ALL",
  "showImagingIntro": true,
  "showInstructHelpPanel": true,
  "showTotalOnReport": true,
  "useQuickItinAsDefault": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|allowCreditCardTransArrivalEmails|boolean|false|none|Allow Credit Card Transaction Arrival Notification Emails, defaulted to true.|
|allowReceiptImageAvailEmails|boolean|false|none|Send email when faxed receipts are successfully received, defaulted to true.|
|autoAddTripCardTransOnReport|boolean|false|none|Add company card transactions within trip dates to 1 click expense report.|
|defaultReportPrintFormat|string|false|none|Default expense report print type.|
|expenseAuditRequired|string|false|none|Expense Audit is required.|
|processorReportAccess|string|false|none|Report access for processor roles (Expense Processor, Expense Processor Audit, Expense Processor Manager)|
|promptForCardTransactionsOnReport|boolean|false|none|Prompt for Company Card Transactions when creating a new report, defaulted to true.|
|promptForReportPrintFormat|boolean|false|none|Always prompt for the report format before printing.|
|showExpenseOnReport|string|false|none|Show expenses on detailed report.|
|showImagingIntro|boolean|false|none|Display imaging introduction, defaulted to true.|
|showInstructHelpPanel|boolean|false|none|Display instructional help, defaulted to true.|
|showTotalOnReport|boolean|false|none|Show Report Totals on Detailed Report.|
|useQuickItinAsDefault|boolean|false|none|Use quick itinerary as default.|

#### Enumerated Values

|Property|Value|
|---|---|
|defaultReportPrintFormat|RECEIPTS|
|defaultReportPrintFormat|DETAILED|
|defaultReportPrintFormat|FAX|
|expenseAuditRequired|NEVER|
|expenseAuditRequired|REQUIRED|
|expenseAuditRequired|ALWAYS|
|processorReportAccess|All reports excluding returned|
|processorReportAccess|All reports including returned|
|processorReportAccess|All reports Pending processor and above|
|showExpenseOnReport|ALL|
|showExpenseOnReport|PARENT|
|showExpenseOnReport|NOTHING|

<h2 id="tocS_SpendUser">SpendUser</h2>

<a id="schemaspenduser"></a>
<a id="schema_SpendUser"></a>
<a id="tocSspenduser"></a>
<a id="tocsspenduser"></a>

```json
{
  "budgetCountryCode": "string",
  "cashAdvanceAccountCode": "string",
  "country": "string",
  "ledgerCode": "string",
  "locale": "string",
  "reimbursementCurrency": "string",
  "reimbursementType": "OTHER",
  "schemaCustomData": [
    {
      "id": "string",
      "value": "string"
    }
  ],
  "stateProvince": "string",
  "testEmployee": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|budgetCountryCode|string|false|none|Valid ISO 3166 country code for Budget|
|cashAdvanceAccountCode|string|true|none|Valid cash advance account code|
|country|string|true|none|Valid ISO 3166 country code|
|ledgerCode|string|false|none|Ledger code to associate with the user|
|locale|string|true|none|Valid locale from the list of configured locales as defined in [RFC5646], i.e en-US|
|reimbursementCurrency|string|true|none|Valid three digit currency code in the list of system reimbursement currencies|
|reimbursementType|object|true|none|The reimbursement type for the user|
|schemaCustomData|[object]|false|none|The Custom Data associated with this user|
|» id|string|true|none|custom1 - custom22, orgUnit1 - orgUnit6|
|» value|string|true|none|Value of the custom field - For list = List Item Code|
|stateProvince|string|false|none|Valid ISO sub country code, i.e - WA|
|testEmployee|boolean|false|none|A Boolean value indicating whether the User is a test user. Can't be modified after the user is created.|

#### Enumerated Values

|Property|Value|
|---|---|
|reimbursementType|OTHER|
|reimbursementType|PAY_PAL|
|reimbursementType|CONCUR_PAY|
|reimbursementType|ADP_PAYROLL|
|reimbursementType|ACCOUNTS_PAYABLE|

<h2 id="tocS_ProvisionStatus">ProvisionStatus</h2>

<a id="schemaprovisionstatus"></a>
<a id="schema_ProvisionStatus"></a>
<a id="tocSprovisionstatus"></a>
<a id="tocsprovisionstatus"></a>

```json
{
  "id": "string",
  "itemsPerPage": 0,
  "operations": [
    {
      "bulkId": "string",
      "extensions": [
        {
          "messages": {
            "code": "string",
            "message": "string",
            "schemaPath": "string",
            "type": "error"
          },
          "name": "string",
          "status": {
            "code": "string",
            "completed": true,
            "result": "success",
            "success": true
          }
        }
      ],
      "id": "string",
      "resource": {
        "id": "string",
        "type": "User"
      },
      "status": {
        "completed": true,
        "success": true
      }
    }
  ],
  "startIndex": 0,
  "status": {
    "completed": true,
    "success": true
  },
  "totalResults": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|true|none|Unique identifier (uuid) for the provisioning request|
|itemsPerPage|integer|false|none|The number of operations returned in current response|
|operations|[object]|false|none|Status of each operation of the provisioning request|
|» bulkId|string|false|none|Transient identifier of newly created resource, unique within a bulk request|
|» extensions|[object]|false|none|extensions' status|
|»» messages|object|false|none|Additional messages in case of errors / warnings|
|»»» code|string|true|none|Message Code|
|»»» message|string|false|none|Message description|
|»»» schemaPath|string|false|none|Relative schema path of attribute|
|»»» type|string|true|none|Message Type|
|»» name|string|true|none|Extension Name|
|»» status|object|true|none|Status of the operation|
|»»» code|string|false|none|http status code|
|»»» completed|boolean|true|none|Is processing extension completed?|
|»»» result|string|false|none|result of action on resource|
|»»» success|boolean|false|none|Is processing extension success?|
|» id|string|true|none|Identifier of the operation (generated by provisioning service)|
|» resource|object|false|none|resource details|
|»» id|string|false|none|Unique Identifier (UUID) of the resource|
|»» type|string|false|none|resource type|
|» status|object|true|none|Status of the operation|
|»» completed|boolean|true|none|Is provisioning completed?|
|»» success|boolean|false|none|Is provisioning success?|
|startIndex|integer|false|none|The 1-based index of the first operation in the current set of operations|
|status|object|true|none|Status of the provision request|
|» completed|boolean|true|none|Is provisioning completed?|
|» success|boolean|false|none|Is provisioning successful?|
|totalResults|integer|false|none|The total number of operations in a bulk provisioning request|

#### Enumerated Values

|Property|Value|
|---|---|
|type|error|
|type|warning|
|result|success|
|result|error|
|result|no-op|
|result|not-processed|
|type|User|

<h2 id="tocS_SpendRole">SpendRole</h2>

<a id="schemaspendrole"></a>
<a id="schema_SpendRole"></a>
<a id="tocSspendrole"></a>
<a id="tocsspendrole"></a>

```json
{
  "roles": [
    {
      "roleGroups": [
        {}
      ],
      "roleName": {}
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|roles|[object]|false|none|Expense Roles for Employee|
|» roleGroups|[object]|false|none|Group(s) to be associated with the Expense Role|
|» roleName|object|true|none|Expense Role for Employee|


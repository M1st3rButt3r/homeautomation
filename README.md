# Homeautomation

## **Usage**

## List all devices <span style="color:red"> *Not implemented* <span>

### Definition
`GET /devices`

### Response
- `200 OK` on success
```json
[
    {
        "identifier": "355087d4-13ac-413f-a596-e2c33c62f1ea",
        "name": "Lamp",
        "type": "switch",
        "actions":
        [
            "on",
            "off"
        ]
    },
    {
        "identifier": "355087d4-13ac-413f-a596-e2c33c62f1ea",
        "...": "..."
    }
]
```

## Register new device <span style="color:red"> *Not implemented* <span>

### Definition
`POST /devices`

### Arguments
- `"name":string` a friendly name
- `"controller_gateway":string` the IP address of the device's controller

### Response
- `404 Not Found` if gateway is not found (but the device is created anyway, there is just no connection)
- `201 Created` on success

```json
{
    "identifier": "355087d4-13ac-413f-a596-e2c33c62f1ea",
    "name": "Lamp",
    "type": "switch",
    "actions":
    [
        "on",
        "off"
    ]
}
```

## Look up device details <span style="color:red"> *Not implemented* <span>

### Definition
`GET /device/<identifier>`

### Response
- `404 Not Found` if the device does not exist
- `200 OK` on success
```json
{
    "identifier": "355087d4-13ac-413f-a596-e2c33c62f1ea",
    "name": "Lamp",
    "type": "switch",
    "actions":
    [
        "on",
        "off"
    ]
}
```

## Delete device <span style="color:red"> *Not implemented* <span>

### Definition
`DELETE /device/<identifier>`

### Response
- `404 Not Found` if the device does not exist
- `204 No Content` on success

## Execute action <span style="color:red"> *Not implemented* <span>

### Definition
`POST /device/<indentfier>`

### Arguments
- `"action":string` the action which should be executed
# Документацией API я не занимался, поэтому, чтобы не тратить лишнее время, оставлю все здесь
**create_courier**
{
    "name": "name",
    "surname": "surname",
    "phone": "phone",
    "areas": [
        {
            "id": int
        },
        {
            "id": int
        }
    ]
}

**create_order**
{
    "delivery": "42.434914, 19.279949"
}

**create_delivery**
{
    "name": "Test",
    "of": {
        "x": 23,
        "y": 24
    },
    "to": {
        "x": 12,
        "y": 15
    }
}

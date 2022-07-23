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
    "name": "name",
    "of": {
        "x": 1,
        "y": 2
    },
    "to": {
        "x": 3,
        "y": 4
    }
}

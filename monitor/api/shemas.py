from drf_yasg import openapi

monitor_serializer_schema = {
    'properties': {
        'now': openapi.Schema(
            tilte='current datetime',
            type=openapi.TYPE_STRING,
        ),
        'unique': openapi.Schema(
            title='unique',
            type=openapi.TYPE_STRING,
        ),
        'totalSiteVisits': openapi.Schema(
            title='total visits site',
            type=openapi.TYPE_STRING,
        ),
        'cpu_usage': openapi.Schema(
            title='cpu usage',
            type=openapi.TYPE_STRING,
        ),
        'ram_usage': openapi.Schema(
            title='ram usage',
            type=openapi.TYPE_BOOLEAN,
        ),
        'dataSaved': openapi.Schema(
            title='data saved',
            type=openapi.TYPE_BOOLEAN,
        ),
    },
    'example': [
        {
            "now": "2022-01-31T15:53:54.440224",
            "unique": 6,
            "totalSiteVisits": 21,
            "cpu_usage": 25,
            "ram_usage": 62,
            "dataSaved": "<Page 1 of 1>"
        }
    ],
    'required': ['now', 'unique', 'totalSiteVisits', 'cpu_usage', 'ram_usage', 'dataSaved'],
}

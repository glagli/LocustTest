from locust import HttpUser, TaskSet, task, FastHttpUser


class UserBehavior(FastHttpUser):
    todayManual = ["2022-12-22"]

    @task(2)
    def sbol_android_mobile(self):
        body = {
            "meta": {
                "systemLanguage": "ru_BY",
                "timeStamp": "2022-12-22T15:59:12.668+03:00",
                "screenSize": "1507x720",
                "apiKey": "4faa2e69c853f26b144e0eaa06a6b5793df461bf439b68cfe856289510f850ef",
                "operationSystemVersion": "31",
                "deviceVendor": "Hisense",
                "deviceModel": "EBG-AN10",
                "operationSystem": "Android",
                "deviceMemorySize": "127948574720",
                "platform": "MOBILE"
            },
            "profile": {
                "appVersion": "14.4.0.7760",
                "applicationLanguage": "ru",
                "hashEpkId": "UNKNOWN",
                "clientBlock": "greenfield1.online.sberbank.ru:4477",
                "sessionId": "2022-12-22T15:59:12.144+03:00 fzCyWOPzYjA3WxxhFQUPYv3sRbU3XOd9",
                "hashUserLoginId": "HMsGcY8m3MHblGZLSdkdALjidpXeL7oX8oFTtOrUUh539vdqqnpt9bYlDo5U5tPZ",
                "deviceId": "fzCyWOPzYjA3WxxhFQUPYv3sRbU3XOd9",
                "hashEfsId": "UNKNOWN"
            },
            "data": [
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                }
            ]
        }

        self.client.post("/metrics/sbol", json=body,
                         headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'})

    @task(2)
    def sbol_ios_mobile(self):
        body = {
            "meta": {
                "systemLanguage": "ru_FI",
                "timeStamp": "2022-12-22T15:59:12.668+03:00",
                "screenSize": "2189x1080",
                "apiKey": "4faa2e69c853f26b144e0eaa06a6b5793df461bf439b68cfe856289510f850ef",
                "operationSystemVersion": "13.2",
                "deviceVendor": "Apple",
                "deviceModel": "iPhone9,1",
                "operationSystem": "iOS",
                "deviceMemorySize": "255993663488",
                "platform": "MOBILE"
            },
            "profile": {
                "appVersion": "12.11.0",
                "applicationLanguage": "de",
                "hashEpkId": "UNKNOWN",
                "clientBlock": "ift-guest",
                "sessionId": "2022-12-22T15:59:12.144+03:00 xyC8t7nToHZ3n955P2geo9u72YWf46s6",
                "hashUserLoginId": "caN5lIB1hwsfOofMOJrhufTpI2Ic41SPPyzP7HUzCin4ir4JjAcjNna0f5oHAVh0",
                "deviceId": "xyC8t7nToHZ3n955P2geo9u72YWf46s6",
                "hashEfsId": "UNKNOWN"
            },
            "data": [
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                }
            ]
        }

        self.client.post("/metrics/sbol", json=body,
                         headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'})

    @task(2)
    def sbol_web_mobile(self):
        body = {
            "meta": {
                "systemLanguage": "en_ES",
                "timeStamp": "2022-12-22T15:59:12.668+03:00",
                "screenSize": "2164x1080",
                "apiKey": "4faa2e69c853f26b144e0eaa06a6b5793df461bf439b68cfe856289510f850ef",
                "browser": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.141 YaBrowser/22.3.3.855 Yowser/2.5 Safari/537.36",
                "platform": "WEB"
            },
            "profile": {
                "applicationLanguage": "ru",
                "clientBlock": "https://pro-ift-node5.testonline.sberbank.ru",
                "sessionId": "SA1.4e19f129-1d66-4889-be85-72936fea5632.1662008545.1662016953",
                "hashUserLoginId": "38dd959ef1a4921a4afb8ea9b9f26b8e",
                "deviceId": "SA1.6f21456e-1761-4721-abdf-23b8da02ec72.1663039676"
            },
            "data": [
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                }
            ]
        }

        self.client.post("/metrics/sbol", json=body,
                         headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'})

    @task(2)
    def sbol_crash_mobile(self):
        body = {
            "meta": {
                "systemLanguage": "ru_FR",
                "timeStamp": "2022-12-22T15:59:12.668+03:00",
                "screenSize": "2267x1080",
                "apiKey": "c61d4c65a6bbd7cc2f012c30c683511170a6e8ca04648af612476e4b3fc21ab6",
                "operationSystemVersion": "29",
                "deviceVendor": "sprd",
                "browser": "Android",
                "deviceModel": "SM-M115F",
                "operationSystem": "Android",
                "deviceMemorySize": "27229675520",
                "platform": "MOBILE",
                "deviceAbi": "x86_64"
            },
            "profile": {
                "appVersion": "12.17.0.5704",
                "applicationLanguage": "en",
                "hashEpkId": "UNKNOWN",
                "appVersionNumber": "2022080918",
                "clientBlock": "ift-node9",
                "sessionId": "2022-12-22T15:59:12.144+03:00 EVpnfPX0YbMwqNc2ZYdo9P4VJhvta0IT",
                "hashUserLoginId": "oyYJ3E4d9m6RAvRrI1RRLdVsm8BXBeLoC36YIFcAOBv42Pg9lZ4iqtznSHuFxdkq",
                "deviceId": "EVpnfPX0YbMwqNc2ZYdo9P4VJhvta0IT",
                "hashEfsId": "UNKNOWN"
            },
            "data": [
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                }
            ]
        }

        self.client.post("/crash/sbol", json=body,
                         headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'})

    # _________________________________________________________________________________________________________________

    @task(2)
    def sberinvestor_android_mobile(self):
        body = {
            "meta": {
                "systemLanguage": "ru_BY",
                "timeStamp": "2022-12-22T15:59:12.668+03:00",
                "screenSize": "1507x720",
                "apiKey": "4faa2e69c853f26b144e0eaa06a6b5793df461bf439b68cfe856289510f850ef",
                "operationSystemVersion": "31",
                "deviceVendor": "Hisense",
                "deviceModel": "EBG-AN10",
                "operationSystem": "Android",
                "deviceMemorySize": "127948574720",
                "platform": "MOBILE"
            },
            "profile": {
                "appVersion": "14.4.0.7760",
                "applicationLanguage": "ru",
                "hashEpkId": "UNKNOWN",
                "clientBlock": "greenfield1.online.sberbank.ru:4477",
                "sessionId": "2022-12-22T15:59:12.144+03:00 fzCyWOPzYjA3WxxhFQUPYv3sRbU3XOd9",
                "hashUserLoginId": "HMsGcY8m3MHblGZLSdkdALjidpXeL7oX8oFTtOrUUh539vdqqnpt9bYlDo5U5tPZ",
                "deviceId": "fzCyWOPzYjA3WxxhFQUPYv3sRbU3XOd9",
                "hashEfsId": "UNKNOWN"
            },
            "data": [
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                }
            ]
        }

        self.client.post("/metrics/sberinvestor", json=body,
                         headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'})

    @task(2)
    def sberinvestor_ios_mobile(self):
        body = {
            "meta": {
                "systemLanguage": "ru_FI",
                "timeStamp": "2022-12-22T15:59:12.668+03:00",
                "screenSize": "2189x1080",
                "apiKey": "4faa2e69c853f26b144e0eaa06a6b5793df461bf439b68cfe856289510f850ef",
                "operationSystemVersion": "13.2",
                "deviceVendor": "Apple",
                "deviceModel": "iPhone9,1",
                "operationSystem": "iOS",
                "deviceMemorySize": "255993663488",
                "platform": "MOBILE"
            },
            "profile": {
                "appVersion": "12.11.0",
                "applicationLanguage": "de",
                "hashEpkId": "UNKNOWN",
                "clientBlock": "ift-guest",
                "sessionId": "2022-12-22T15:59:12.144+03:00 xyC8t7nToHZ3n955P2geo9u72YWf46s6",
                "hashUserLoginId": "caN5lIB1hwsfOofMOJrhufTpI2Ic41SPPyzP7HUzCin4ir4JjAcjNna0f5oHAVh0",
                "deviceId": "xyC8t7nToHZ3n955P2geo9u72YWf46s6",
                "hashEfsId": "UNKNOWN"
            },
            "data": [
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                }
            ]
        }

        self.client.post("/metrics/sberinvestor", json=body,
                         headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'})

    @task(2)
    def sberinvestor_web_mobile(self):
        body = {
            "meta": {
                "systemLanguage": "en_ES",
                "timeStamp": "2022-12-22T15:59:12.668+03:00",
                "screenSize": "2164x1080",
                "apiKey": "4faa2e69c853f26b144e0eaa06a6b5793df461bf439b68cfe856289510f850ef",
                "browser": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.141 YaBrowser/22.3.3.855 Yowser/2.5 Safari/537.36",
                "platform": "WEB"
            },
            "profile": {
                "applicationLanguage": "ru",
                "clientBlock": "https://pro-ift-node5.testonline.sberbank.ru",
                "sessionId": "SA1.4e19f129-1d66-4889-be85-72936fea5632.1662008545.1662016953",
                "hashUserLoginId": "38dd959ef1a4921a4afb8ea9b9f26b8e",
                "deviceId": "SA1.6f21456e-1761-4721-abdf-23b8da02ec72.1663039676"
            },
            "data": [
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                }
            ]
        }

        self.client.post("/metrics/sberinvestor", json=body,
                         headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'})

    @task(2)
    def sberinvestor_crash_mobile(self):
        body = {
            "meta": {
                "systemLanguage": "ru_FR",
                "timeStamp": "2022-12-22T15:59:12.668+03:00",
                "screenSize": "2267x1080",
                "apiKey": "c61d4c65a6bbd7cc2f012c30c683511170a6e8ca04648af612476e4b3fc21ab6",
                "operationSystemVersion": "29",
                "deviceVendor": "sprd",
                "browser": "Android",
                "deviceModel": "SM-M115F",
                "operationSystem": "Android",
                "deviceMemorySize": "27229675520",
                "platform": "MOBILE",
                "deviceAbi": "x86_64"
            },
            "profile": {
                "appVersion": "12.17.0.5704",
                "applicationLanguage": "en",
                "hashEpkId": "UNKNOWN",
                "appVersionNumber": "2022080918",
                "clientBlock": "ift-node9",
                "sessionId": "2022-12-22T15:59:12.144+03:00 EVpnfPX0YbMwqNc2ZYdo9P4VJhvta0IT",
                "hashUserLoginId": "oyYJ3E4d9m6RAvRrI1RRLdVsm8BXBeLoC36YIFcAOBv42Pg9lZ4iqtznSHuFxdkq",
                "deviceId": "EVpnfPX0YbMwqNc2ZYdo9P4VJhvta0IT",
                "hashEfsId": "UNKNOWN"
            },
            "data": [
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                }
            ]
        }

        self.client.post("/crash/sberinvestor", json=body,
                         headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'})

    # _________________________________________________________________________________________________________________

    @task(2)
    def sbermazing_android_mobile(self):
        body = {
            "meta": {
                "systemLanguage": "ru_BY",
                "timeStamp": "2022-12-22T15:59:12.668+03:00",
                "screenSize": "1507x720",
                "apiKey": "4faa2e69c853f26b144e0eaa06a6b5793df461bf439b68cfe856289510f850ef",
                "operationSystemVersion": "31",
                "deviceVendor": "Hisense",
                "deviceModel": "EBG-AN10",
                "operationSystem": "Android",
                "deviceMemorySize": "127948574720",
                "platform": "MOBILE"
            },
            "profile": {
                "appVersion": "14.4.0.7760",
                "applicationLanguage": "ru",
                "hashEpkId": "UNKNOWN",
                "clientBlock": "greenfield1.online.sberbank.ru:4477",
                "sessionId": "2022-12-22T15:59:12.144+03:00 fzCyWOPzYjA3WxxhFQUPYv3sRbU3XOd9",
                "hashUserLoginId": "HMsGcY8m3MHblGZLSdkdALjidpXeL7oX8oFTtOrUUh539vdqqnpt9bYlDo5U5tPZ",
                "deviceId": "fzCyWOPzYjA3WxxhFQUPYv3sRbU3XOd9",
                "hashEfsId": "UNKNOWN"
            },
            "data": [
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                }
            ]
        }

        self.client.post("/metrics/sbermazing", json=body,
                         headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'})

    @task(2)
    def sbermazing_ios_mobile(self):
        body = {
            "meta": {
                "systemLanguage": "ru_FI",
                "timeStamp": "2022-12-22T15:59:12.668+03:00",
                "screenSize": "2189x1080",
                "apiKey": "4faa2e69c853f26b144e0eaa06a6b5793df461bf439b68cfe856289510f850ef",
                "operationSystemVersion": "13.2",
                "deviceVendor": "Apple",
                "deviceModel": "iPhone9,1",
                "operationSystem": "iOS",
                "deviceMemorySize": "255993663488",
                "platform": "MOBILE"
            },
            "profile": {
                "appVersion": "12.11.0",
                "applicationLanguage": "de",
                "hashEpkId": "UNKNOWN",
                "clientBlock": "ift-guest",
                "sessionId": "2022-12-22T15:59:12.144+03:00 xyC8t7nToHZ3n955P2geo9u72YWf46s6",
                "hashUserLoginId": "caN5lIB1hwsfOofMOJrhufTpI2Ic41SPPyzP7HUzCin4ir4JjAcjNna0f5oHAVh0",
                "deviceId": "xyC8t7nToHZ3n955P2geo9u72YWf46s6",
                "hashEfsId": "UNKNOWN"
            },
            "data": [
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "54",
                    "connectionType": "WIFI",
                    "eventType": "technical",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ProductTypeMetric",
                            "value": "3.8"
                        },
                        {
                            "key": "session",
                            "value": "udp"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Auth By Login Init Show"
                }
            ]
        }

        self.client.post("/metrics/sbermazing", json=body,
                         headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'})

    @task(2)
    def sbermazing_web_mobile(self):
        body = {
            "meta": {
                "systemLanguage": "en_ES",
                "timeStamp": "2022-12-22T15:59:12.668+03:00",
                "screenSize": "2164x1080",
                "apiKey": "4faa2e69c853f26b144e0eaa06a6b5793df461bf439b68cfe856289510f850ef",
                "browser": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.141 YaBrowser/22.3.3.855 Yowser/2.5 Safari/537.36",
                "platform": "WEB"
            },
            "profile": {
                "applicationLanguage": "ru",
                "clientBlock": "https://pro-ift-node5.testonline.sberbank.ru",
                "sessionId": "SA1.4e19f129-1d66-4889-be85-72936fea5632.1662008545.1662016953",
                "hashUserLoginId": "38dd959ef1a4921a4afb8ea9b9f26b8e",
                "deviceId": "SA1.6f21456e-1761-4721-abdf-23b8da02ec72.1663039676"
            },
            "data": [
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                },
                {
                    "batteryLevel": "3",
                    "connectionType": "UNKNOWN",
                    "eventType": "business",
                    "eventCategory": "SBOL_WEB_PRO_profile",
                    "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "value": "Получить отчёт"
                }
            ]
        }

        self.client.post("/metrics/sbermazing", json=body,
                         headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'})

    @task(2)
    def sbermazing_crash_mobile(self):
        body = {
            "meta": {
                "systemLanguage": "ru_FR",
                "timeStamp": "2022-12-22T15:59:12.668+03:00",
                "screenSize": "2267x1080",
                "apiKey": "c61d4c65a6bbd7cc2f012c30c683511170a6e8ca04648af612476e4b3fc21ab6",
                "operationSystemVersion": "29",
                "deviceVendor": "sprd",
                "browser": "Android",
                "deviceModel": "SM-M115F",
                "operationSystem": "Android",
                "deviceMemorySize": "27229675520",
                "platform": "MOBILE",
                "deviceAbi": "x86_64"
            },
            "profile": {
                "appVersion": "12.17.0.5704",
                "applicationLanguage": "en",
                "hashEpkId": "UNKNOWN",
                "appVersionNumber": "2022080918",
                "clientBlock": "ift-node9",
                "sessionId": "2022-12-22T15:59:12.144+03:00 EVpnfPX0YbMwqNc2ZYdo9P4VJhvta0IT",
                "hashUserLoginId": "oyYJ3E4d9m6RAvRrI1RRLdVsm8BXBeLoC36YIFcAOBv42Pg9lZ4iqtznSHuFxdkq",
                "deviceId": "EVpnfPX0YbMwqNc2ZYdo9P4VJhvta0IT",
                "hashEfsId": "UNKNOWN"
            },
            "data": [
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                },
                {
                    "batteryLevel": "6",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.73088171194848",
                    "geoLongitude": "37.543203280432635",
                    "cellularProvider": "MTS",
                    "internalIP": "192.168.1.1",
                    "ramFree": "2324242356",
                    "diskFree": "1232424",
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "crashAction": "java.lang.Throwable",
                    "message": "My test exception Dev",
                    "stackTrace": [
                        "java.lang.Throwable: My test exception"
                    ],
                    "properties": [
                        {
                            "key": "From",
                            "value": "udp"
                        }
                    ]
                }
            ]
        }

        self.client.post("/crash/sbermazing", json=body,
                         headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'})

# _________________________________________________________________________________________________________________

    @task(2)
    def sberkids_android_mobile(self):
        body = {
            "meta": {
                "systemLanguage": "ru_BY",
                "timeStamp": "2022-12-22T15:59:12.668+03:00",
                "screenSize": "1507x720",
                "apiKey": "4faa2e69c853f26b144e0eaa06a6b5793df461bf439b68cfe856289510f850ef",
                "operationSystemVersion": "31",
                "deviceVendor": "Hisense",
                "deviceModel": "EBG-AN10",
                "operationSystem": "Android",
                "deviceMemorySize": "127948574720",
                "platform": "MOBILE"
            },
            "profile": {
                "appVersion": "14.4.0.7760",
                "applicationLanguage": "ru",
                "hashEpkId": "UNKNOWN",
                "clientBlock": "greenfield1.online.sberbank.ru:4477",
                "sessionId": "2022-12-22T15:59:12.144+03:00 fzCyWOPzYjA3WxxhFQUPYv3sRbU3XOd9",
                "hashUserLoginId": "HMsGcY8m3MHblGZLSdkdALjidpXeL7oX8oFTtOrUUh539vdqqnpt9bYlDo5U5tPZ",
                "deviceId": "fzCyWOPzYjA3WxxhFQUPYv3sRbU3XOd9",
                "hashEfsId": "UNKNOWN"
            },
            "data": [
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                },
                {
                    "cellularProvider": "MTS",
                    "batteryLevel": "4",
                    "connectionType": "CELLULAR",
                    "eventType": "NFE",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": "ABflag",
                            "value": "Load"
                        },
                        {
                            "key": "DetailsFrom",
                            "value": "true"
                        }
                    ],
                    "timeStamp": "2022-12-22T16:00:12.668+03:00",
                    "eventAction": "Card GeneralScreen Click"
                }
            ]
        }

        self.client.post("/metrics/sberkids", json=body,
                             headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'})

    @task(2)
    def sberkids_ios_mobile(self):
        body = {
                "meta": {
                    "systemLanguage": "ru_FI",
                    "timeStamp": "2022-12-22T15:59:12.668+03:00",
                    "screenSize": "2189x1080",
                    "apiKey": "4faa2e69c853f26b144e0eaa06a6b5793df461bf439b68cfe856289510f850ef",
                    "operationSystemVersion": "13.2",
                    "deviceVendor": "Apple",
                    "deviceModel": "iPhone9,1",
                    "operationSystem": "iOS",
                    "deviceMemorySize": "255993663488",
                    "platform": "MOBILE"
                },
                "profile": {
                    "appVersion": "12.11.0",
                    "applicationLanguage": "de",
                    "hashEpkId": "UNKNOWN",
                    "clientBlock": "ift-guest",
                    "sessionId": "2022-12-22T15:59:12.144+03:00 xyC8t7nToHZ3n955P2geo9u72YWf46s6",
                    "hashUserLoginId": "caN5lIB1hwsfOofMOJrhufTpI2Ic41SPPyzP7HUzCin4ir4JjAcjNna0f5oHAVh0",
                    "deviceId": "xyC8t7nToHZ3n955P2geo9u72YWf46s6",
                    "hashEfsId": "UNKNOWN"
                },
                "data": [
                    {
                        "cellularProvider": "MTS",
                        "batteryLevel": "54",
                        "connectionType": "WIFI",
                        "eventType": "technical",
                        "geoLatitude": "55.7408994",
                        "geoLongitude": "37.5318225",
                        "internalIP": "10.8.7.35",
                        "properties": [
                            {
                                "key": "ProductTypeMetric",
                                "value": "3.8"
                            },
                            {
                                "key": "session",
                                "value": "udp"
                            }
                        ],
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "eventAction": "Auth By Login Init Show"
                    },
                    {
                        "cellularProvider": "MTS",
                        "batteryLevel": "54",
                        "connectionType": "WIFI",
                        "eventType": "technical",
                        "geoLatitude": "55.7408994",
                        "geoLongitude": "37.5318225",
                        "internalIP": "10.8.7.35",
                        "properties": [
                            {
                                "key": "ProductTypeMetric",
                                "value": "3.8"
                            },
                            {
                                "key": "session",
                                "value": "udp"
                            }
                        ],
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "eventAction": "Auth By Login Init Show"
                    },
                    {
                        "cellularProvider": "MTS",
                        "batteryLevel": "54",
                        "connectionType": "WIFI",
                        "eventType": "technical",
                        "geoLatitude": "55.7408994",
                        "geoLongitude": "37.5318225",
                        "internalIP": "10.8.7.35",
                        "properties": [
                            {
                                "key": "ProductTypeMetric",
                                "value": "3.8"
                            },
                            {
                                "key": "session",
                                "value": "udp"
                            }
                        ],
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "eventAction": "Auth By Login Init Show"
                    },
                    {
                        "cellularProvider": "MTS",
                        "batteryLevel": "54",
                        "connectionType": "WIFI",
                        "eventType": "technical",
                        "geoLatitude": "55.7408994",
                        "geoLongitude": "37.5318225",
                        "internalIP": "10.8.7.35",
                        "properties": [
                            {
                                "key": "ProductTypeMetric",
                                "value": "3.8"
                            },
                            {
                                "key": "session",
                                "value": "udp"
                            }
                        ],
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "eventAction": "Auth By Login Init Show"
                    },
                    {
                        "cellularProvider": "MTS",
                        "batteryLevel": "54",
                        "connectionType": "WIFI",
                        "eventType": "technical",
                        "geoLatitude": "55.7408994",
                        "geoLongitude": "37.5318225",
                        "internalIP": "10.8.7.35",
                        "properties": [
                            {
                                "key": "ProductTypeMetric",
                                "value": "3.8"
                            },
                            {
                                "key": "session",
                                "value": "udp"
                            }
                        ],
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "eventAction": "Auth By Login Init Show"
                    },
                    {
                        "cellularProvider": "MTS",
                        "batteryLevel": "54",
                        "connectionType": "WIFI",
                        "eventType": "technical",
                        "geoLatitude": "55.7408994",
                        "geoLongitude": "37.5318225",
                        "internalIP": "10.8.7.35",
                        "properties": [
                            {
                                "key": "ProductTypeMetric",
                                "value": "3.8"
                            },
                            {
                                "key": "session",
                                "value": "udp"
                            }
                        ],
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "eventAction": "Auth By Login Init Show"
                    },
                    {
                        "cellularProvider": "MTS",
                        "batteryLevel": "54",
                        "connectionType": "WIFI",
                        "eventType": "technical",
                        "geoLatitude": "55.7408994",
                        "geoLongitude": "37.5318225",
                        "internalIP": "10.8.7.35",
                        "properties": [
                            {
                                "key": "ProductTypeMetric",
                                "value": "3.8"
                            },
                            {
                                "key": "session",
                                "value": "udp"
                            }
                        ],
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "eventAction": "Auth By Login Init Show"
                    },
                    {
                        "cellularProvider": "MTS",
                        "batteryLevel": "54",
                        "connectionType": "WIFI",
                        "eventType": "technical",
                        "geoLatitude": "55.7408994",
                        "geoLongitude": "37.5318225",
                        "internalIP": "10.8.7.35",
                        "properties": [
                            {
                                "key": "ProductTypeMetric",
                                "value": "3.8"
                            },
                            {
                                "key": "session",
                                "value": "udp"
                            }
                        ],
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "eventAction": "Auth By Login Init Show"
                    },
                    {
                        "cellularProvider": "MTS",
                        "batteryLevel": "54",
                        "connectionType": "WIFI",
                        "eventType": "technical",
                        "geoLatitude": "55.7408994",
                        "geoLongitude": "37.5318225",
                        "internalIP": "10.8.7.35",
                        "properties": [
                            {
                                "key": "ProductTypeMetric",
                                "value": "3.8"
                            },
                            {
                                "key": "session",
                                "value": "udp"
                            }
                        ],
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "eventAction": "Auth By Login Init Show"
                    },
                    {
                        "cellularProvider": "MTS",
                        "batteryLevel": "54",
                        "connectionType": "WIFI",
                        "eventType": "technical",
                        "geoLatitude": "55.7408994",
                        "geoLongitude": "37.5318225",
                        "internalIP": "10.8.7.35",
                        "properties": [
                            {
                                "key": "ProductTypeMetric",
                                "value": "3.8"
                            },
                            {
                                "key": "session",
                                "value": "udp"
                            }
                        ],
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "eventAction": "Auth By Login Init Show"
                    }
                ]
            }

        self.client.post("/metrics/sberkids", json=body,
                             headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'})

    @task(2)
    def sberkids_web_mobile(self):
        body = {
                "meta": {
                    "systemLanguage": "en_ES",
                    "timeStamp": "2022-12-22T15:59:12.668+03:00",
                    "screenSize": "2164x1080",
                    "apiKey": "4faa2e69c853f26b144e0eaa06a6b5793df461bf439b68cfe856289510f850ef",
                    "browser": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.141 YaBrowser/22.3.3.855 Yowser/2.5 Safari/537.36",
                    "platform": "WEB"
                },
                "profile": {
                    "applicationLanguage": "ru",
                    "clientBlock": "https://pro-ift-node5.testonline.sberbank.ru",
                    "sessionId": "SA1.4e19f129-1d66-4889-be85-72936fea5632.1662008545.1662016953",
                    "hashUserLoginId": "38dd959ef1a4921a4afb8ea9b9f26b8e",
                    "deviceId": "SA1.6f21456e-1761-4721-abdf-23b8da02ec72.1663039676"
                },
                "data": [
                    {
                        "batteryLevel": "3",
                        "connectionType": "UNKNOWN",
                        "eventType": "business",
                        "eventCategory": "SBOL_WEB_PRO_profile",
                        "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "value": "Получить отчёт"
                    },
                    {
                        "batteryLevel": "3",
                        "connectionType": "UNKNOWN",
                        "eventType": "business",
                        "eventCategory": "SBOL_WEB_PRO_profile",
                        "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "value": "Получить отчёт"
                    },
                    {
                        "batteryLevel": "3",
                        "connectionType": "UNKNOWN",
                        "eventType": "business",
                        "eventCategory": "SBOL_WEB_PRO_profile",
                        "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "value": "Получить отчёт"
                    },
                    {
                        "batteryLevel": "3",
                        "connectionType": "UNKNOWN",
                        "eventType": "business",
                        "eventCategory": "SBOL_WEB_PRO_profile",
                        "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "value": "Получить отчёт"
                    },
                    {
                        "batteryLevel": "3",
                        "connectionType": "UNKNOWN",
                        "eventType": "business",
                        "eventCategory": "SBOL_WEB_PRO_profile",
                        "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "value": "Получить отчёт"
                    },
                    {
                        "batteryLevel": "3",
                        "connectionType": "UNKNOWN",
                        "eventType": "business",
                        "eventCategory": "SBOL_WEB_PRO_profile",
                        "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "value": "Получить отчёт"
                    },
                    {
                        "batteryLevel": "3",
                        "connectionType": "UNKNOWN",
                        "eventType": "business",
                        "eventCategory": "SBOL_WEB_PRO_profile",
                        "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "value": "Получить отчёт"
                    },
                    {
                        "batteryLevel": "3",
                        "connectionType": "UNKNOWN",
                        "eventType": "business",
                        "eventCategory": "SBOL_WEB_PRO_profile",
                        "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "value": "Получить отчёт"
                    },
                    {
                        "batteryLevel": "3",
                        "connectionType": "UNKNOWN",
                        "eventType": "business",
                        "eventCategory": "SBOL_WEB_PRO_profile",
                        "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "value": "Получить отчёт"
                    },
                    {
                        "batteryLevel": "3",
                        "connectionType": "UNKNOWN",
                        "eventType": "business",
                        "eventCategory": "SBOL_WEB_PRO_profile",
                        "eventAction": "На карту за рубеж/Подтверждение перевода/Перевести 10 $__Клик",
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "value": "Получить отчёт"
                    }
                ]
            }

        self.client.post("/metrics/sberkids", json=body,
                             headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'})

    @task(2)
    def sberkids_crash_mobile(self):
        body = {
                "meta": {
                    "systemLanguage": "ru_FR",
                    "timeStamp": "2022-12-22T15:59:12.668+03:00",
                    "screenSize": "2267x1080",
                    "apiKey": "c61d4c65a6bbd7cc2f012c30c683511170a6e8ca04648af612476e4b3fc21ab6",
                    "operationSystemVersion": "29",
                    "deviceVendor": "sprd",
                    "browser": "Android",
                    "deviceModel": "SM-M115F",
                    "operationSystem": "Android",
                    "deviceMemorySize": "27229675520",
                    "platform": "MOBILE",
                    "deviceAbi": "x86_64"
                },
                "profile": {
                    "appVersion": "12.17.0.5704",
                    "applicationLanguage": "en",
                    "hashEpkId": "UNKNOWN",
                    "appVersionNumber": "2022080918",
                    "clientBlock": "ift-node9",
                    "sessionId": "2022-12-22T15:59:12.144+03:00 EVpnfPX0YbMwqNc2ZYdo9P4VJhvta0IT",
                    "hashUserLoginId": "oyYJ3E4d9m6RAvRrI1RRLdVsm8BXBeLoC36YIFcAOBv42Pg9lZ4iqtznSHuFxdkq",
                    "deviceId": "EVpnfPX0YbMwqNc2ZYdo9P4VJhvta0IT",
                    "hashEfsId": "UNKNOWN"
                },
                "data": [
                    {
                        "batteryLevel": "6",
                        "connectionType": "CELLULAR",
                        "eventType": "NFE",
                        "geoLatitude": "55.73088171194848",
                        "geoLongitude": "37.543203280432635",
                        "cellularProvider": "MTS",
                        "internalIP": "192.168.1.1",
                        "ramFree": "2324242356",
                        "diskFree": "1232424",
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "crashAction": "java.lang.Throwable",
                        "message": "My test exception Dev",
                        "stackTrace": [
                            "java.lang.Throwable: My test exception"
                        ],
                        "properties": [
                            {
                                "key": "From",
                                "value": "udp"
                            }
                        ]
                    },
                    {
                        "batteryLevel": "6",
                        "connectionType": "CELLULAR",
                        "eventType": "NFE",
                        "geoLatitude": "55.73088171194848",
                        "geoLongitude": "37.543203280432635",
                        "cellularProvider": "MTS",
                        "internalIP": "192.168.1.1",
                        "ramFree": "2324242356",
                        "diskFree": "1232424",
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "crashAction": "java.lang.Throwable",
                        "message": "My test exception Dev",
                        "stackTrace": [
                            "java.lang.Throwable: My test exception"
                        ],
                        "properties": [
                            {
                                "key": "From",
                                "value": "udp"
                            }
                        ]
                    },
                    {
                        "batteryLevel": "6",
                        "connectionType": "CELLULAR",
                        "eventType": "NFE",
                        "geoLatitude": "55.73088171194848",
                        "geoLongitude": "37.543203280432635",
                        "cellularProvider": "MTS",
                        "internalIP": "192.168.1.1",
                        "ramFree": "2324242356",
                        "diskFree": "1232424",
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "crashAction": "java.lang.Throwable",
                        "message": "My test exception Dev",
                        "stackTrace": [
                            "java.lang.Throwable: My test exception"
                        ],
                        "properties": [
                            {
                                "key": "From",
                                "value": "udp"
                            }
                        ]
                    },
                    {
                        "batteryLevel": "6",
                        "connectionType": "CELLULAR",
                        "eventType": "NFE",
                        "geoLatitude": "55.73088171194848",
                        "geoLongitude": "37.543203280432635",
                        "cellularProvider": "MTS",
                        "internalIP": "192.168.1.1",
                        "ramFree": "2324242356",
                        "diskFree": "1232424",
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "crashAction": "java.lang.Throwable",
                        "message": "My test exception Dev",
                        "stackTrace": [
                            "java.lang.Throwable: My test exception"
                        ],
                        "properties": [
                            {
                                "key": "From",
                                "value": "udp"
                            }
                        ]
                    },
                    {
                        "batteryLevel": "6",
                        "connectionType": "CELLULAR",
                        "eventType": "NFE",
                        "geoLatitude": "55.73088171194848",
                        "geoLongitude": "37.543203280432635",
                        "cellularProvider": "MTS",
                        "internalIP": "192.168.1.1",
                        "ramFree": "2324242356",
                        "diskFree": "1232424",
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "crashAction": "java.lang.Throwable",
                        "message": "My test exception Dev",
                        "stackTrace": [
                            "java.lang.Throwable: My test exception"
                        ],
                        "properties": [
                            {
                                "key": "From",
                                "value": "udp"
                            }
                        ]
                    },
                    {
                        "batteryLevel": "6",
                        "connectionType": "CELLULAR",
                        "eventType": "NFE",
                        "geoLatitude": "55.73088171194848",
                        "geoLongitude": "37.543203280432635",
                        "cellularProvider": "MTS",
                        "internalIP": "192.168.1.1",
                        "ramFree": "2324242356",
                        "diskFree": "1232424",
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "crashAction": "java.lang.Throwable",
                        "message": "My test exception Dev",
                        "stackTrace": [
                            "java.lang.Throwable: My test exception"
                        ],
                        "properties": [
                            {
                                "key": "From",
                                "value": "udp"
                            }
                        ]
                    },
                    {
                        "batteryLevel": "6",
                        "connectionType": "CELLULAR",
                        "eventType": "NFE",
                        "geoLatitude": "55.73088171194848",
                        "geoLongitude": "37.543203280432635",
                        "cellularProvider": "MTS",
                        "internalIP": "192.168.1.1",
                        "ramFree": "2324242356",
                        "diskFree": "1232424",
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "crashAction": "java.lang.Throwable",
                        "message": "My test exception Dev",
                        "stackTrace": [
                            "java.lang.Throwable: My test exception"
                        ],
                        "properties": [
                            {
                                "key": "From",
                                "value": "udp"
                            }
                        ]
                    },
                    {
                        "batteryLevel": "6",
                        "connectionType": "CELLULAR",
                        "eventType": "NFE",
                        "geoLatitude": "55.73088171194848",
                        "geoLongitude": "37.543203280432635",
                        "cellularProvider": "MTS",
                        "internalIP": "192.168.1.1",
                        "ramFree": "2324242356",
                        "diskFree": "1232424",
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "crashAction": "java.lang.Throwable",
                        "message": "My test exception Dev",
                        "stackTrace": [
                            "java.lang.Throwable: My test exception"
                        ],
                        "properties": [
                            {
                                "key": "From",
                                "value": "udp"
                            }
                        ]
                    },
                    {
                        "batteryLevel": "6",
                        "connectionType": "CELLULAR",
                        "eventType": "NFE",
                        "geoLatitude": "55.73088171194848",
                        "geoLongitude": "37.543203280432635",
                        "cellularProvider": "MTS",
                        "internalIP": "192.168.1.1",
                        "ramFree": "2324242356",
                        "diskFree": "1232424",
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "crashAction": "java.lang.Throwable",
                        "message": "My test exception Dev",
                        "stackTrace": [
                            "java.lang.Throwable: My test exception"
                        ],
                        "properties": [
                            {
                                "key": "From",
                                "value": "udp"
                            }
                        ]
                    },
                    {
                        "batteryLevel": "6",
                        "connectionType": "CELLULAR",
                        "eventType": "NFE",
                        "geoLatitude": "55.73088171194848",
                        "geoLongitude": "37.543203280432635",
                        "cellularProvider": "MTS",
                        "internalIP": "192.168.1.1",
                        "ramFree": "2324242356",
                        "diskFree": "1232424",
                        "timeStamp": "2022-12-22T16:00:12.668+03:00",
                        "crashAction": "java.lang.Throwable",
                        "message": "My test exception Dev",
                        "stackTrace": [
                            "java.lang.Throwable: My test exception"
                        ],
                        "properties": [
                            {
                                "key": "From",
                                "value": "udp"
                            }
                        ]
                    }
                ]
            }

        self.client.post("/crash/sberkids", json=body,
                             headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'})


class WebsiteUser(FastHttpUser):
    tasks = [UserBehavior]
    min_wait = 500
    max_wait = 2000

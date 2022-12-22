from locust import HttpUser, TaskSet, task, FastHttpUser
import datetime
import random
import hashlib
from locustFile import DataTestAndroid


class UserBehavior(FastHttpUser):

    @task(1)
    def android_mobile(self):
        time = datetime.datetime.today().strftime("%H:%M:%S")
        LoginId_deviceId = {
            hashlib.sha256(str(random.randrange(1000)).encode('ascii')).hexdigest(): [
                hashlib.md5(str(random.randrange(10000)).encode('ascii')).hexdigest(),
                hashlib.md5(str(random.randrange(10000)).encode('ascii')).hexdigest(),
                hashlib.md5(str(random.randrange(10000)).encode('ascii')).hexdigest()
            ]
        }

        login_hash = list(LoginId_deviceId.keys())[0]
        devices_hash = random.choice(list(LoginId_deviceId.values())[0])

        body = {
            "meta": {
                "systemLanguage": random.choice(DataTestAndroid.systemLanguage),
                "timeStamp": random.choice(DataTestAndroid.todayManual) + "T" + time + ".668+03:00",
                "screenSize": random.choice(DataTestAndroid.screenSize),
                "apiKey": random.choice(DataTestAndroid.apiKey),
                "operationSystemVersion": random.choice(DataTestAndroid.operationSystemVersion),
                "deviceVendor": random.choice(DataTestAndroid.deviceVendor),
                "browser": random.choice(DataTestAndroid.browser),
                "deviceModel": random.choice(DataTestAndroid.deviceModel),
                "operationSystem": random.choice(DataTestAndroid.operationSystem),
                "deviceMemorySize": random.choice(DataTestAndroid.deviceMemorySize),
                "platform": random.choice(DataTestAndroid.platforмm),
                "deviceAbi": random.choice(DataTestAndroid.deviceAbi)
            },
            "profile": {
                "appVersion": random.choice(DataTestAndroid.appVersion),
                "applicationLanguage": random.choice(DataTestAndroid.applicationLanguage),
                "hashEpkId": "UNKNOWN",
                "appVersionNumber": random.choice(DataTestAndroid.appVersionNumber),
                "clientBlock": random.choice(DataTestAndroid.clientBlock),
                "sessionId": random.choice(DataTestAndroid.todayManual) + "T" + time + ".144+03:00 "+devices_hash,
                "hashUserLoginId": login_hash,
                "deviceId": devices_hash,
                "hashEfsId": "UNKNOWN"
            },
            "data": [
                {
                    "batteryLevel": str(random.randrange(5, 100)),
                    "connectionType": random.choice(DataTestAndroid.connectionType),
                    "eventType": "business",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key":  random.choice(DataTestAndroid.key),
                            "value":  random.choice(DataTestAndroid.value),
                        },
                        {
                            "key": random.choice(DataTestAndroid.key),
                            "value": random.choice(DataTestAndroid.value),
                        }
                    ],
                    "timeStamp": random.choice(DataTestAndroid.todayManual) + "T" + time + ".417+03:00",
                    "eventAction": "Main Show"
                },
                {
                    "batteryLevel": str(random.randrange(5, 100)),
                    "connectionType": random.choice(DataTestAndroid.connectionType),
                    "eventType": "business",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": random.choice(DataTestAndroid.key),
                            "value": random.choice(DataTestAndroid.value),
                        },
                        {
                            "key": random.choice(DataTestAndroid.key),
                            "value": random.choice(DataTestAndroid.value),
                        }
                    ],
                    "timeStamp": random.choice(DataTestAndroid.todayManual) + "T" + time + ".417+03:00",
                    "eventAction": "Main Show"
                },
                {
                    "batteryLevel": str(random.randrange(5, 100)),
                    "connectionType": random.choice(DataTestAndroid.connectionType),
                    "eventType": "business",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": random.choice(DataTestAndroid.key),
                            "value": random.choice(DataTestAndroid.value),
                        },
                        {
                            "key": random.choice(DataTestAndroid.key),
                            "value": random.choice(DataTestAndroid.value),
                        }
                    ],
                    "timeStamp": random.choice(DataTestAndroid.todayManual) + "T" + time + ".417+03:00",
                    "eventAction": "Main Show"
                },
                {
                    "batteryLevel": str(random.randrange(5, 100)),
                    "connectionType": random.choice(DataTestAndroid.connectionType),
                    "eventType": "business",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": random.choice(DataTestAndroid.key),
                            "value": random.choice(DataTestAndroid.value),
                        },
                        {
                            "key": random.choice(DataTestAndroid.key),
                            "value": random.choice(DataTestAndroid.value),
                        }
                    ],
                    "timeStamp": random.choice(DataTestAndroid.todayManual) + "T" + time + ".417+03:00",
                    "eventAction": "Main Show"
                },
                {
                    "batteryLevel": str(random.randrange(5, 100)),
                    "connectionType": random.choice(DataTestAndroid.connectionType),
                    "eventType": "business",
                    "geoLatitude": "55.7408994",
                    "geoLongitude": "37.5318225",
                    "internalIP": "10.8.7.35",
                    "properties": [
                        {
                            "key": random.choice(DataTestAndroid.key),
                            "value": random.choice(DataTestAndroid.value),
                        },
                        {
                            "key": random.choice(DataTestAndroid.key),
                            "value": random.choice(DataTestAndroid.value),
                        }
                    ],
                    "timeStamp": random.choice(DataTestAndroid.todayManual) + "T" + time + ".417+03:00",
                    "eventAction": "Main Show"
                }
            ]
        }

        self.client.post("/metrics/sbol", json=body,
                         headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'})


class WebsiteUser(FastHttpUser):
    tasks = [UserBehavior]
    min_wait = 500
    max_wait = 2000

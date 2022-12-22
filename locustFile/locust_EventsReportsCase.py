from locust import HttpUser, TaskSet, task
import datetime
import random
import hashlib


class UserBehavior(TaskSet):

    @task(5)
    def reports_data_size(self):
        self.client.verify = False
        self.client.get("reports/data-size",
                        headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'},
                        cert=('/Users/19908726/PycharmProjects/LocustTest/Clicksbatech.crt',
                              '/Users/19908726/PycharmProjects/LocustTest/Clicksbatech.key')
                        )

    @task(5)
    def reports(self):
        self.client.verify = False
        self.client.get("/reports?limit=6&offset=0",
                        headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'},
                        cert=('/Users/19908726/PycharmProjects/LocustTest/Clicksbatech.crt',
                              '/Users/19908726/PycharmProjects/LocustTest/Clicksbatech.key')
                        )

    # @task(1)
    # def dates(self):
    #     self.client.verify = False
    #     self.client.get("/dates",
    #                     headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'},
    #                     cert=('/Users/19908726/PycharmProjects/LocustTest/Clicksbatech.crt',
    #                           '/Users/19908726/PycharmProjects/LocustTest/Clicksbatech.key')
    #                     )
    #
    # @task(1)
    # def platforms(self):
    #     self.client.verify = False
    #     self.client.get("/platforms",
    #                     headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'},
    #                     cert=('/Users/19908726/PycharmProjects/LocustTest/Clicksbatech.crt',
    #                           '/Users/19908726/PycharmProjects/LocustTest/Clicksbatech.key')
    #                     )
    #
    # @task(1)
    # def meta_api_keys(self):
    #     self.client.verify = False
    #     self.client.get("/meta-api-keys?platform=android&order_by=descending",
    #                     headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'},
    #                     cert=('/Users/19908726/PycharmProjects/LocustTest/Clicksbatech.crt',
    #                           '/Users/19908726/PycharmProjects/LocustTest/Clicksbatech.key')
    #                     )
    #
    # @task(1)
    # def unique_users(self):
    #     self.client.verify = False
    #     self.client.get(
    #         "/unique-users?platform=android&from_date=2022-10-31&to_date=2022-11-07&current_timestamp=1667844204016",
    #         headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'},
    #         cert=('/Users/19908726/PycharmProjects/LocustTest/Clicksbatech.crt',
    #               '/Users/19908726/PycharmProjects/LocustTest/Clicksbatech.key')
    #     )
    #
    # @task(1)
    # def nodes_data_size(self):
    #     self.client.verify = False
    #     self.client.get("/nodes/data-size?platform=android",
    #                     headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'},
    #                     cert=('/Users/19908726/PycharmProjects/LocustTest/Clicksbatech.crt',
    #                           '/Users/19908726/PycharmProjects/LocustTest/Clicksbatech.key')
    #                     )
    #
    # @task(1)
    # def nodes(self):
    #     self.client.verify = False
    #     self.client.get("/nodes?platform=android&order_by=descending&offset=0&limit=20",
    #                     headers={'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.29.2'},
    #                     cert=('/Users/19908726/PycharmProjects/LocustTest/Clicksbatech.crt',
    #                           '/Users/19908726/PycharmProjects/LocustTest/Clicksbatech.key')
    #                     )


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 1000
    max_wait = 2000

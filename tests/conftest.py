import pytest


@pytest.fixture
def operations_mocked_data():
    return [
        {
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041"
        },
        {
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689"
        },
        {
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961"
        },
        {
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582"
        },
        {
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890"
        },
        {
            "state": "EXECUTED",
            "date": "2019-11-19T09:22:25.899614"
        },
        {}
    ]


@pytest.fixture
def remove_mocked_data():
    return [
        {
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
        },
        {
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
        },
        {
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582"
        },
        {
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890"
        },
        {
            "state": "EXECUTED",
            "date": "2019-11-19T09:22:25.899614"
        }

    ]


@pytest.fixture
def dict_test():
    return {"date": "2019-08-26T10:50:58.294041", "other_key": "345"}


@pytest.fixture
def mocked_data_sort():
    return [
        {
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582"
        },
        {
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890"
        },
        {
            "state": "EXECUTED",
            "date": "2019-11-19T09:22:25.899614"
        },
        {
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
        },
        {
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
        },
        {
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        }
    ]


@pytest.fixture
def mocked_result_data():
    return [
        {
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582"
        },
        {
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890"
        },
        {
            "state": "EXECUTED",
            "date": "2019-11-19T09:22:25.899614"
        },
        {
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
        },
        {
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
        }
    ]

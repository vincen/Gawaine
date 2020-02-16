# -*- coding: utf8 -*-

__author__ = 'vincen'


class FundInfo(object):
    """
        "f006761":                                          "f005312":
            {                                                   {
                "code": "006761",                                   "code": "005312",
                "typename": "债券型",                                "typename": "混合型",
                "net": "2.3953",                                    "net": "1.8061",
                "name": "银河家盈债券",                               "name": "万家经济新动能混合C",
                "type": "zqx",                                      "type": "hhx",
                "totalnet": "2.4013",                               "totalnet": "1.8061",
                "newnet": "2.3953",                                 "newnet": "1.8061",
                "newtotalnet": "2.4013",                            "newtotalnet": "1.8061",
                "newdate": "2020-02-07",                            "newdate": "2020-02-07",
                "net1": "2.3938",                                   "net1": "1.7551",
                "totalnet1": "2.3998",                              "totalnet1": "1.7551",
                "ranges": "0.0015",                                 "ranges": "0.0510",
                "rate": "0.06",                                     "rate": "2.91",
                "syrate": "0.06",                                   "syrate": "2.91",
                "shstat": "开放",                                    "shstat": "开放",
                "sgstat": "开放",                                    "sgstat": "开放",
                "dt": "0",                                          "dt": "1",
                "buy": "0",                                         "buy": "1",
                "clrq": "2018-12-14",                               "clrq": "2018-02-07",
                "orgid": "jjjl0000049",                             "orgid": "T000009495",
                "orgname": "银河基金管理有限公司",                    "orgname": "万家基金管理有限公司",
                "SYENDDATE": "2020-02-07",                          "SYENDDATE": "2020-02-07",
                "prerate": "0.06",                                  "prerate": "2.91",
                "F003N_FUND33": "0.50",                             "F003N_FUND33": "10.17",
                "F005": "0.81",                                     "F005": "34.82",
                "F008": "0.75",                                     "F008": "29.15",
                "F009": "137.75",                                   "F009": "56.20",
                "F010": "136.46",                                   "F010": "65.62",
                "F011": "139.26",                                   "F011": "76.51",
                "F012": "140.94",                                   "F012": "80.61",
                "F014N_FUND33": "140.94",                           "F014N_FUND33": "80.61",
                "F015N_FUND33": "140.94"                            "F015N_FUND33": "80.61"
            },                                                  },
    """
    fcode = None
    fname = None
    type1 = None
    type2 = None
    created_at = None
    orgid = None


class FundRev(object):

    pkid = None
    code = None
    created_at = None
    updated_at = None
    FR01 = None
    FR02 = None
    FR03 = None
    FR04 = None
    FR05 = None
    FR06 = None
    FR07 = None
    FR08 = None
    FR09 = None
    FR10 = None
    totalNet = None
    income = None
    net = None


class FundManager(object):
    pkid = None
    name = None
    profile = None


class FundOrg(object):
    orgid = None
    orgname = None

#try:
#    import urllib.request as urllib2
#except ImportError:
#    import urrlib2
import urllib2
import base64
import HackerRank
from pprint import pprint

def tryCase(source, lang, testcases):
    try:
        api_client = HackerRank.swagger.ApiClient()
        checker_api = HackerRank.CheckerApi(api_client)
        response = checker_api.languages()    

        # To display structured information of a variable, please use var_dump: pip install var_dump
        # from var_dump import var_dump
        # var_dump(response)
        pprint(response)

    except urllib2.HTTPError as e:
        print('[HTTP Error {}]: {}'.format(e.code, e.reason))
        print('Request URL: {}'.format(e.geturl()))
        print('Response body: {}'.format(e.read()))
    except urllib2.URLError as e:
        print('[URL Error]: {}'.format(e.reason))
    except Exception as e:
        print(e)


    api_key = "hackerrank|232362-631|731ba0d30f24b7145437f295dc711c60a3ca78fa"
    #source = "puts 'Testing'"
    #lang = 5
    #testcases = "[\"Test 1\", \"Test 2\"]"
    format = "JSON"

    try:
        api_client = HackerRank.swagger.ApiClient()
        checker_api = HackerRank.CheckerApi(api_client)
        response = checker_api.submission(api_key, source, lang, testcases, format, callback_url="https://testing.com/response/handler", wait="true")    

        # To display structured information of a variable, please use var_dump: pip install var_dump
        # from var_dump import var_dump
        # var_dump(response)
        pprint(response)

    except urllib2.HTTPError as e:
        print('[HTTP Error {}]: {}'.format(e.code, e.reason))
        print('Request URL: {}'.format(e.geturl()))
        print('Response body: {}'.format(e.read()))
    except urllib2.URLError as e:
        print('[URL Error]: {}'.format(e.reason))
    except Exception as e:
        print(e)



    print("end");

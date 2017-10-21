import http.client, urllib.request, urllib.parse, urllib.error, base64, json


def transcribe(url):
    subscription_key = 'a48ce7ca33e746349ab4b33a2fe054c7'

    uri_base = 'westeurope.api.cognitive.microsoft.com'

    headers = {
        # Request headers.
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }

    params = urllib.parse.urlencode({
        # Request parameters. The language setting "unk" means automatically detect the language.
        'language': 'en',
        'detectOrientation ': 'true',
    })

    # The URL of a JPEG image containing text.
    body = "{'url':url}"

    try:
        # Execute the REST API call and get the response.
        conn = http.client.HTTPSConnection(uri_base)
        conn.request("POST", "/vision/v1.0/ocr?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()

        # 'data' contains the JSON data. The following formats the JSON data for display.
        parsed = json.loads(data)
        print ("Response:")
        # print (json.dumps(parsed, sort_keys=True, indent=2))
        lines = parsed['regions'][0]['lines']
        result = ""
        for line in lines:
            words = line['words']
            for word in words:
                result += " " + word['text']

        conn.close()
        return result

    except Exception as e:
    print('Error:')
        print(e)

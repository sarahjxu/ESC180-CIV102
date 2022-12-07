import urllib.request

def choose_variant(variants):
    max_variant = ""
    max_amount = 0
    for k in range(len(variants)):
        term = variants[k]
        print(term)
        to_perc = urllib.parse.quote(term)
        f = urllib.request.urlopen("https://ca.search.yahoo.com/search;_ylt=Av3YHOEya_QRKgRTD8kMWgst17V_?p="+to_perc+"&amp;toggle=1&amp;cop=mss&amp;ei=UTF-8&amp;fr=yfp-t-715&amp;fp=1")
        page = f.read().decode("utf-8")
        words = page.split()
        for i in range(len(words)):
            if words[i] == "lh-22\">About" and words[i+2] == "search" and words[i+3] == "results</span></h2>":
                results = float(words[i+1].replace(',',''))
                print(results)
                max_amount = max(results, max_amount)
                if max_amount == results:
                    max_variant = variants[k]
        f.close()
    return max_variant

choose_variant(['"five-year anniversary"', '"fifth anniversary"'])
#'fc-smoke"><h2', 'class="title', 'mb-0"><span', 'style="color:inherit;"', 'class="', 'fz-14', 'lh-22">About', '3,230,000,000', 'search', 'results</span></h2>'
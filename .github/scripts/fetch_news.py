import feedparser
import re
import datetime
import time

FEEDS = [
    {'url': 'https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms', 'r': 'ind', 'src': 'Economic Times'},
    {'url': 'https://www.moneycontrol.com/rss/MCtopnews.xml', 'r': 'ind', 'src': 'Moneycontrol'},
    {'url': 'https://feeds.bbci.co.uk/news/business/rss.xml', 'r': 'eu', 'src': 'BBC Business'},
    {'url': 'https://feeds.skynews.com/feeds/rss/business.xml', 'r': 'eu', 'src': 'Sky News'},
    {'url': 'https://www.cnbc.com/id/10000664/device/rss/rss.html', 'r': 'usa', 'src': 'CNBC Markets'},
    {'url': 'https://feeds.a.dj.com/rss/RSSMarketsMain.xml', 'r': 'usa', 'src': 'WSJ Markets'},
]

CAT_MAP = {
    'stock': 'Stocks', 'share': 'Stocks', 'nifty': 'Stocks', 'sensex': 'Stocks',
    'nasdaq': 'Stocks', 'dow': 'Stocks', 'dax': 'Stocks',
    'rupee': 'Currency', 'dollar': 'Currency', 'euro': 'Currency', 'forex': 'Currency',
    'oil': 'Energy', 'crude': 'Energy', 'brent': 'Energy', 'opec': 'Energy',
    'rbi': 'Central Bank', 'fed': 'Central Bank', 'ecb': 'Central Bank', 'rate': 'Central Bank',
    'gold': 'Commodities', 'silver': 'Commodities',
    'ipo': 'IPO', 'gdp': 'Economy', 'inflation': 'Economy', 'recession': 'Economy',
}

def get_cat(title):
    t = title.lower()
    for k, v in CAT_MAP.items():
        if k in t:
            return v
    return 'Markets'

def clean(text):
    text = re.sub(r'<[^>]+>', '', text or '')
    text = re.sub(r"[\x27\x22\\]", '', text)
    text = text.replace('\n', ' ').replace('\r', '').strip()
    return text[:180]

def ago(entry):
    try:
        pub = entry.get('published_parsed') or entry.get('updated_parsed')
        if not pub:
            return 'Today'
        diff = int((time.time() - time.mktime(pub)) / 60)
        if diff < 60:
            return str(diff) + 'm ago'
        elif diff < 1440:
            return str(diff // 60) + 'h ago'
        else:
            return str(diff // 1440) + 'd ago'
    except Exception:
        return 'Today'

articles = []
for feed in FEEDS:
    try:
        d = feedparser.parse(feed['url'])
        count = 0
        for entry in d.entries[:6]:
            title = clean(entry.get('title', ''))
            summary = clean(entry.get('summary', '') or entry.get('description', ''))
            if not title or len(title) < 10:
                continue
            articles.append({
                'r': feed['r'], 'h': title, 'b': summary,
                'cat': get_cat(title), 'src': feed['src'],
                'url': entry.get('link', '#'), 't': ago(entry), 'type': 'builtin'
            })
            count += 1
            if count >= 5:
                break
        print('OK ' + feed['src'] + ': ' + str(count) + ' articles')
    except Exception as e:
        print('FAIL ' + feed['src'] + ': ' + str(e))

ind = [a for a in articles if a['r'] == 'ind'][:6]
eu  = [a for a in articles if a['r'] == 'eu'][:5]
usa = [a for a in articles if a['r'] == 'usa'][:6]
final = ind + eu + usa
print('Total: ' + str(len(final)) + ' (' + str(len(ind)) + ' IND, ' + str(len(eu)) + ' EU, ' + str(len(usa)) + ' USA)')

if not final:
    print('No articles fetched - skipping update')
    exit(0)

def to_js(a):
    return '{r:' + repr(a['r']) + ',h:' + repr(a['h']) + ',b:' + repr(a['b']) + ',cat:' + repr(a['cat']) + ',src:' + repr(a['src']) + ',url:' + repr(a['url']) + ',t:' + repr(a['t']) + ',type:' + repr(a['type']) + '}'

js_array = '[\n  ' + ',\n  '.join(to_js(a) for a in final) + '\n]'

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = 'var BUILTIN=['
end_marker = '];'
start_idx = content.find(start_marker)
if start_idx == -1:
    print('ERROR: BUILTIN marker not found in index.html')
    exit(1)
end_idx = content.find(end_marker, start_idx) + len(end_marker)
new_content = content[:start_idx] + 'var BUILTIN=' + js_array + ';' + content[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

now = datetime.datetime.now(datetime.timezone.utc).strftime('%b %d, %Y %H:%M UTC')
print('index.html updated at ' + now)

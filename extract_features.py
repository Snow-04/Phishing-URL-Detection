import re
import tldextract
from urllib.parse import urlparse

def extract_features(url):
    parsed = urlparse(url)
    ext = tldextract.extract(url)

    hostname = parsed.hostname or ""
    path = parsed.path or ""
    full = url.lower()

    words_raw = re.split(r'\W+', full)
    words_raw = [w for w in words_raw if w]

    def shortest(lst): return min([len(w) for w in lst]) if lst else 0
    def longest(lst): return max([len(w) for w in lst]) if lst else 0
    def avg(lst): return sum([len(w) for w in lst]) / len(lst) if lst else 0

    features = {}

    features["length_url"] = len(url)
    features["length_hostname"] = len(hostname)
    features["ip"] = 1 if re.match(r"^\d+\.\d+\.\d+\.\d+$", hostname) else 0

    chars = {
        "nb_dots":".","nb_hyphens":"-","nb_at":"@","nb_qm":"?",
        "nb_and":"&","nb_or":"|","nb_eq":"=","nb_underscore":"_",
        "nb_tilde":"~","nb_percent":"%","nb_slash":"/","nb_star":"*",
        "nb_colon":":","nb_comma":",","nb_semicolumn":";","nb_dollar":"$",
        "nb_space":" "
    }
    for k,v in chars.items(): features[k] = url.count(v)

    features["nb_www"] = full.count("www")
    features["nb_com"] = full.count(".com")
    features["nb_dslash"] = url.count("//")

    features["http_in_path"] = 1 if "http" in path else 0
    features["https_token"] = 1 if "https" in hostname else 0

    features["ratio_digits_url"] = sum(c.isdigit() for c in url) / (len(url)+1)
    features["ratio_digits_host"] = sum(c.isdigit() for c in hostname) / (len(hostname)+1)

    features["punycode"] = 1 if "xn--" in hostname else 0
    features["port"] = parsed.port if parsed.port else 0

    features["tld_in_path"] = 1 if ext.suffix in path else 0
    features["tld_in_subdomain"] = 1 if ext.suffix in ext.subdomain else 0

    subs = ext.subdomain.split('.') if ext.subdomain else []
    features["abnormal_subdomain"] = 1 if len(subs)>=3 else 0
    features["nb_subdomains"] = len([s for s in subs if s])

    features["prefix_suffix"] = 1 if "-" in hostname else 0
    features["random_domain"] = 1 if re.search(r"[a-zA-Z]{6,}[0-9]{3,}",hostname) else 0

    shorteners=["bit.ly","goo.gl","tinyurl.com","t.co"]
    features["shortening_service"] = 1 if hostname in shorteners else 0

    match=re.search(r"\.([a-zA-Z0-9]+)$",path)
    features["path_extension"]=1 if match else 0

    features["nb_redirection"]=full.count("//")-1
    features["nb_external_redirection"]=1 if "://" in path else 0

    features["length_words_raw"]=len(words_raw)
    features["char_repeat"]=max([full.count(c) for c in set(full)]) if full else 0

    features["shortest_words_raw"]=shortest(words_raw)
    features["shortest_word_host"]=shortest(hostname.split('.'))
    features["shortest_word_path"]=shortest(path.split('/'))

    features["longest_words_raw"]=longest(words_raw)
    features["longest_word_host"]=longest(hostname.split('.'))
    features["longest_word_path"]=longest(path.split('/'))

    features["avg_words_raw"]=avg(words_raw)
    features["avg_word_host"]=avg(hostname.split('.'))
    features["avg_word_path"]=avg(path.split('/'))

    return features

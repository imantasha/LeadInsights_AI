import whois
from googlesearch import search
import time

def enrich_domain_data(domains):
    enriched = []
    for domain in domains:
        try:
            info = whois.whois(domain)
            email = info.emails[0] if info.emails else ""
            org = info.org or ""
            country = info.country or ""

            query = f"site:linkedin.com/in/ CEO OR CTO OR Founder {domain}"
            linkedin = ""
            try:
                results = list(search(query, num=1, stop=1, pause=2))
                linkedin = results[0] if results else ""
            except:
                pass

            enriched.append({
                "domain": domain,
                "email": email,
                "organization": org,
                "country": country,
                "linkedin": linkedin
            })
            time.sleep(1)
        except Exception as e:
            enriched.append({"domain": domain, "error": str(e)})
    return enriched
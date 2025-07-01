import whois
import time

def enrich_domain_data(domains):
    enriched = []
    for domain in domains:
        try:
            info = whois.whois(domain)

            # Handle emails safely
            if info.emails:
                if isinstance(info.emails, list):
                    email = info.emails[0]
                else:
                    email = info.emails
            else:
                email = ""

            org = info.org if info.org else ""
            country = info.country if info.country else ""

            # No LinkedIn search to avoid rate limits or external dependencies
            linkedin = "Not searched"

            enriched.append({
                "domain": domain,
                "email": email,
                "organization": org,
                "country": country,
                "linkedin": linkedin
            })

            time.sleep(1)

        except Exception as e:
            enriched.append({
                "domain": domain,
                "error": str(e),
                "email": "",
                "organization": "",
                "country": "",
                "linkedin": ""
            })

    return enriched

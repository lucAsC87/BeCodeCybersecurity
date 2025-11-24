# The Kamkar Challenge

Now that we have the list of all HackerOne domains in scope, let's try to break them!
Based on your [inputs](https://cryptpad.fr/sheet/#/2/sheet/edit/kyzkmVX0ZR0P7JBqtHHGpZ2v/), I made a simple list of scripts.
Each script will provide: a vulnerability, a potential vulnerability to check, or information about the infrastructure.

The goal is to build a giant scanner that will run each script on ALL the domains. By doing this, we will gather enough data to analyze and find real vulnerabilities.

## Git Repo

Before building the scanner, we need the scripts.
I will invite you all to a GitHub repository called: XXX
This repository contains three folders: ActiveScanners, PossibleScanners, and InfoScanners.
You all have access to the repository and can add, remove, or edit any files.
Be careful never to delete your teammates' scripts, working as a team on a single repository can be challenging.
If something gets deleted, please check the history.

## Script Format

Your script need to have a `scan_domain` function OR a `scan_url` function.
It should only take a domain or an URL as parameter.
It should return True if you found a (possible) vulnerability or an information.
Else it should return False.

Examples:
```
def scan_domain(domain: str) -> bool:
    print(f"I'm scanning th domain: {domain}")
    return False # i didn't found a vulnerability

def scan_url(url: str) -> bool:
    print(f"I'm scanning the URL: {url}")
    return True # i did found a vulnerability!
```

You will use these tools multiple times throughout your cybersecurity career.

The following is just a list of ideas.
You can update, increase or remove scripts as you want.


## Scripts Ideas

| Script Name                  | Severity       | Reason |
|------------------------------|----------------|--------|
| ssrf_param_finder            | ActiveVuln     | Can redirect victim to a target website     |
| exposed_file_finder          | ActiveVuln     | Exposed sensitives files contains database or creditentials
| takeover_indicator_scan      | ActiveVuln     | Can take control of a subdomain
| wordpress_version_check      | PossibleVuln   | Some wordpress version are vulnerable |
| mysql_banner_check           | PossibleVuln   | Some mysql version are vulnerable     |
| ssh_version_probe            | PossibleVuln   | Some SSH server version are vulnerable
| html_comment_crawler         | PossibleVuln   | Some comments contains creditentials or api routes
| smtp_banner_check            | PossibleVuln   | Some SMTP server are vulnerable
| cors_policy_checker          | PossibleVuln   | Find unsafe CORS policies
| nginx_version_check          | PossibleVuln   | Some nginx server version are vulnerable
| upload_endpoint_finder       | PossibleVuln   | Upload php file could lead to RCE
| robots_sitemap_fetcher       | Info           | X
| accessibility_structure_scan | Info           | X
| tls_info_collector           | Info           | X
| xmlrpc_detector              | Info           | X
| sourcemap_locator            | Info           | X
| dir_enum_light               | Info           | X
| graphql_discovery            | Info           | X

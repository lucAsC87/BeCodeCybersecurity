import requests
import json
import time
from typing import Dict, List
import concurrent.futures
from datetime import datetime, timezone

class HackerOneScraper:
    def __init__(self):
        self.directory_api = "https://hackerone.com/graphql"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/json",
            "Origin": "https://hackerone.com",
            "Referer": "https://hackerone.com/directory/programs"
        }
        self.session = requests.Session()

    def _get_csrf_token(self):
        try:
            print("Requesting main page to get initial cookies...")
            response = self.session.get(
                "https://hackerone.com/directory/programs",
                headers={
                    "User-Agent": self.headers["User-Agent"],
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                }
            )
            response.raise_for_status()
            print(f"Main page status code: {response.status_code}")
            
            print("Cookies received:")
            for cookie in self.session.cookies:
                print(f"- {cookie.name}: {cookie.value[:20]}...")

            return True

        except requests.RequestException as e:
            print(f"Error during initial request: {str(e)}")
            return False

    def get_programs_list(self) -> List[str]:
        """Get list of all program handles"""
        query = """
        query DirectoryQuery($cursor: String) {
          teams(
            first: 100,
            after: $cursor
          ) {
            pageInfo {
              hasNextPage
              endCursor
            }
            edges {
              node {
                handle
                name
                submission_state
                structured_scopes {
                  total_count
                }
              }
            }
          }
        }
        """

        programs = []
        cursor = None
        page = 1

        while True:
            try:
                print(f"Fetching page {page} of programs...")
                
                # Print full request details for debugging
                request_data = {
                    "operationName": "DirectoryQuery",
                    "variables": {"cursor": cursor},
                    "query": query
                }
                print(f"Request data: {json.dumps(request_data, indent=2)}")
                
                response = self.session.post(
                    self.directory_api,
                    headers=self.headers,
                    json=request_data
                )
                
                print(f"Response status: {response.status_code}")
                
                if response.status_code != 200:
                    print(f"Error response content: {response.text[:500]}")
                    break

                data = response.json()
                
                if "errors" in data:
                    print(f"GraphQL errors: {json.dumps(data['errors'], indent=2)}")
                    break

                teams_data = data.get("data", {}).get("teams", {})
                edges = teams_data.get("edges", [])
                
                if not edges:
                    print("No more programs found")
                    break

                for edge in edges:
                    node = edge.get("node", {})
                    if (node.get("handle") and 
                        node.get("submission_state") == "open" and 
                        node.get("structured_scopes", {}).get("total_count", 0) > 0):
                        programs.append(node["handle"])
                        print(f"Found program: {node['handle']}")

                page_info = teams_data.get("pageInfo", {})
                if not page_info.get("hasNextPage"):
                    print("No more pages available")
                    break

                cursor = page_info.get("endCursor")
                page += 1
                time.sleep(2)  # Increased rate limiting

            except Exception as e:
                print(f"Error fetching programs list: {str(e)}")
                break

        print(f"Total programs found: {len(programs)}")
        return programs

    def get_scope(self, program_handle: str) -> Dict[str, List[str]]:
        """Get the scope for a specific program"""
        query = """
        query TeamAssets($handle: String!) {
          team(handle: $handle) {
            structured_scopes(first: 100, archived: false, eligible_for_submission: true) {
              edges {
                node {
                  asset_identifier
                  asset_type
                  eligible_for_submission
                }
              }
            }
          }
        }
        """

        try:
            time.sleep(2)  # Increased rate limiting
            response = self.session.post(
                self.directory_api,
                headers=self.headers,
                json={
                    "operationName": "TeamAssets",
                    "variables": {"handle": program_handle},
                    "query": query
                }
            )
            
            if response.status_code != 200:
                print(f"Error fetching scope for {program_handle}: Status {response.status_code}")
                return {}

            data = response.json()
            
            if "errors" in data:
                print(f"GraphQL errors for {program_handle}: {data['errors']}")
                return {}

            scope_data = {
                "domains": [],
                "urls": [],
                "wildcards": []
            }

            scopes = data.get("data", {}).get("team", {}).get("structured_scopes", {}).get("edges", [])
            for edge in scopes:
                node = edge.get("node", {})
                if node.get("eligible_for_submission"):
                    identifier = node.get("asset_identifier", "").strip()
                    if not identifier:
                        continue

                    if identifier.startswith("*."):
                        scope_data["wildcards"].append(identifier)
                    elif identifier.startswith(("http://", "https://")):
                        scope_data["urls"].append(identifier)
                    else:
                        scope_data["domains"].append(identifier)

            return {k: v for k, v in scope_data.items() if v}

        except Exception as e:
            print(f"Error fetching scope for {program_handle}: {str(e)}")
            return {}

    def scrape_hackerone(self, max_workers: int = 2) -> None:
        """Scrape all program scopes and save to JSON"""
        print("Initializing session...")
        self._get_csrf_token()
        
        print("Getting programs list...")
        programs = self.get_programs_list()
        
        if not programs:
            print("No programs found. Check if the API is accessible.")
            return

        print(f"Found {len(programs)} programs. Starting scope collection...")
        results = {}

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_program = {
                executor.submit(self.get_scope, program): program 
                for program in programs
            }

            completed = 0
            total = len(programs)
            
            for future in concurrent.futures.as_completed(future_to_program):
                program = future_to_program[future]
                completed += 1
                try:
                    scope = future.result()
                    if scope:
                        results[program] = scope
                    print(f"Progress: {completed}/{total} - Processed {program}")
                except Exception as e:
                    print(f"Error processing {program}: {str(e)}")

        if not results:
            print("No results found. Check if the scopes are accessible.")
            return

        print(f"Saving {len(results)} programs to programs.json...")
        with open('programs.json', 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=4)

        print(f"Scraping completed. Saved data for {len(results)} programs.")

def main():
    try:
        print(f"Starting HackerOne scraper at {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC")
        scraper = HackerOneScraper()
        scraper.scrape_hackerone()
    except KeyboardInterrupt:
        print("\nScraping interrupted by user")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
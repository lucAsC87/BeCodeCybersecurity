#!/usr/bin/env python3
"""
OSINT Profile Generator CLI with Interactive Menu
Educational synthetic data generator for OSINT training
"""

import json
import random
import hashlib
import os
import sys
import webbrowser
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import uuid

class OSINTProfileGenerator:
    def __init__(self):
        # Sample data arrays for realistic generation
        self.sample_data = {
            'first_names': [
                'James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer', 'Michael', 'Linda',
                'David', 'Elizabeth', 'William', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica',
                'Thomas', 'Sarah', 'Christopher', 'Karen', 'Daniel', 'Nancy', 'Matthew', 'Lisa',
                'Anthony', 'Betty', 'Mark', 'Helen', 'Donald', 'Sandra', 'Paul', 'Donna',
                'Joshua', 'Carol', 'Kenneth', 'Ruth', 'Kevin', 'Sharon', 'Brian', 'Michelle'
            ],
            
            'last_names': [
                'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis',
                'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson',
                'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson',
                'White', 'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson'
            ],
            
            'companies': [
                'TechCorp Solutions', 'Global Dynamics Inc', 'InnovateNow LLC', 'DataFlow Systems',
                'CloudFirst Technologies', 'NextGen Industries', 'ProActive Services', 'SmartTech Innovations',
                'FutureWorks Ltd', 'DigitalEdge Corp', 'Synergy Partners', 'Quantum Ventures',
                'Alpha Systems', 'Beta Networks', 'Gamma Industries', 'Delta Solutions'
            ],
            
            'job_titles': [
                'Software Engineer', 'Marketing Manager', 'Sales Representative', 'Project Manager',
                'Data Analyst', 'HR Specialist', 'Financial Advisor', 'Operations Director',
                'Product Manager', 'Business Analyst', 'DevOps Engineer', 'UX Designer',
                'Quality Assurance', 'Account Executive', 'Technical Writer', 'System Administrator'
            ],
            
            'cities': [
                'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia',
                'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville',
                'Fort Worth', 'Columbus', 'Charlotte', 'Seattle', 'Denver', 'Boston'
            ],
            
            'universities': [
                'MIT', 'Stanford University', 'Harvard University', 'UC Berkeley', 'Carnegie Mellon',
                'University of Chicago', 'Northwestern', 'Yale University', 'Princeton', 'Columbia University',
                'Cornell University', 'University of Pennsylvania', 'Duke University', 'Caltech',
                'Johns Hopkins', 'University of Michigan', 'Georgia Tech', 'Rice University'
            ],
            
            'domains': [
                'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'icloud.com',
                'protonmail.com', 'aol.com', 'live.com', 'msn.com', 'comcast.net'
            ],
            
            'industries': [
                'Technology', 'Finance', 'Healthcare', 'Manufacturing', 'Consulting',
                'Education', 'Retail', 'Media', 'Transportation', 'Energy'
            ]
        }
        
        self.database = {
            'profiles': [],
            'companies': [],
            'social_profiles': [],
            'relationships': []
        }

    def get_random_element(self, arr: List[str]) -> str:
        """Get a random element from an array"""
        return random.choice(arr)

    def generate_random_number(self, min_val: int, max_val: int) -> int:
        """Generate a random number between min and max"""
        return random.randint(min_val, max_val)

    def generate_id(self) -> str:
        """Generate a unique ID"""
        return f"ID-{int(datetime.now().timestamp())}-{str(uuid.uuid4())[:8]}"

    def generate_phone_number(self) -> str:
        """Generate a realistic phone number"""
        return f"+1-{self.generate_random_number(200, 999)}-{self.generate_random_number(200, 999)}-{self.generate_random_number(1000, 9999)}"

    def generate_email(self, first_name: str, last_name: str, company: str = None) -> str:
        """Generate a realistic email address"""
        formats = [
            f"{first_name.lower()}.{last_name.lower()}",
            f"{first_name.lower()}{last_name.lower()}",
            f"{first_name[0].lower()}{last_name.lower()}",
            f"{first_name.lower()}{self.generate_random_number(10, 99)}"
        ]
        
        if company and random.random() > 0.3:
            # Company email
            domain = company.lower().replace(' ', '').replace(',', '').replace('.', '') + '.com'
        else:
            # Personal email
            domain = self.get_random_element(self.sample_data['domains'])
        
        return f"{random.choice(formats)}@{domain}"

    def generate_password(self, profile: Dict[str, Any]) -> str:
        """Generate a realistic password based on profile data"""
        components = [
            profile['first_name'],
            profile['last_name'], 
            str(profile['birth_year']),
            profile['city'],
            profile.get('company', 'work').split(' ')[0] if profile.get('company') else 'work'
        ]
        
        return random.choice(components) + random.choice(components) + str(self.generate_random_number(10, 99))

    def hash_password(self, password: str) -> str:
        """Generate SHA-512 hash of password"""
        return hashlib.sha512(password.encode()).hexdigest()

    def generate_salt(self) -> str:
        """Generate a random salt for password hashing"""
        import secrets
        return secrets.token_hex(16)  # 32 character hex salt

    def hash_password_with_salt(self, password: str, salt: str = None) -> tuple:
        """Generate salted SHA-512 hash of password"""
        if salt is None:
            salt = self.generate_salt()
        
        # Combine password and salt
        salted_password = password + salt
        hash_value = hashlib.sha512(salted_password.encode()).hexdigest()
        
        return hash_value, salt

    def generate_profile(self, use_salt: bool = False) -> Dict[str, Any]:
        """Generate a single profile with all data"""
        first_name = self.get_random_element(self.sample_data['first_names'])
        last_name = self.get_random_element(self.sample_data['last_names'])
        birth_year = self.generate_random_number(1970, 2000)
        company = self.get_random_element(self.sample_data['companies'])
        
        profile = {
            'id': self.generate_id(),
            'first_name': first_name,
            'last_name': last_name,
            'full_name': f"{first_name} {last_name}",
            'email': self.generate_email(first_name, last_name, company),
            'phone': self.generate_phone_number(),
            'birthdate': f"{self.generate_random_number(1, 12)}/{self.generate_random_number(1, 28)}/{birth_year}",
            'birth_year': birth_year,
            'age': 2025 - birth_year,
            'job_title': self.get_random_element(self.sample_data['job_titles']),
            'company': company,
            'city': self.get_random_element(self.sample_data['cities']),
            'university': self.get_random_element(self.sample_data['universities']),
            'graduation_year': self.generate_random_number(1990, 2020),
            'profile_pic': f"https://randomuser.me/api/portraits/{'men' if random.random() > 0.5 else 'women'}/{self.generate_random_number(1, 99)}.jpg",
            'linkedin_connections': self.generate_random_number(50, 500),
            'social_profiles': {
                'linkedin': f"https://linkedin.com/in/{first_name.lower()}-{last_name.lower()}",
                'twitter': f"https://twitter.com/{first_name.lower()}{last_name.lower()}",
                'github': f"https://github.com/{first_name.lower()}{last_name.lower()}" if random.random() > 0.4 else None
            },
            'generated_at': datetime.now().isoformat(),
            'url': f"/profiles/{self.generate_id()}"
        }

        # Generate password and hash (with optional salt)
        password = self.generate_password(profile)
        profile['password_hint'] = password
        
        if use_salt:
            hash_value, salt = self.hash_password_with_salt(password)
            profile['password_hash'] = hash_value
            profile['salt'] = salt
            profile['hash_type'] = 'SHA-512_SALTED'
        else:
            profile['password_hash'] = self.hash_password(password)
            profile['hash_type'] = 'SHA-512'

        return profile

    def generate_company_profile(self) -> Dict[str, Any]:
        """Generate a company profile"""
        company_name = self.get_random_element(self.sample_data['companies'])
        return {
            'id': self.generate_id(),
            'name': company_name,
            'industry': self.get_random_element(self.sample_data['industries']),
            'size': random.choice(['10-50', '51-200', '201-1000', '1000+']),
            'location': self.get_random_element(self.sample_data['cities']),
            'website': f"https://{company_name.lower().replace(' ', '').replace(',', '').replace('.', '')}.com",
            'employees': [],
            'departments': ['Engineering', 'Sales', 'Marketing', 'HR', 'Finance'],
            'generated_at': datetime.now().isoformat(),
            'url': f"/companies/{self.generate_id()}"
        }

    def generate_social_profile(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        """Generate social media data for a profile"""
        return {
            'id': profile['id'],
            'person_id': profile['id'],
            'posts': self.generate_random_number(10, 100),
            'followers': self.generate_random_number(50, 1000),
            'following': self.generate_random_number(30, 500),
            'last_active': (datetime.now() - timedelta(days=self.generate_random_number(1, 30))).isoformat()
        }

    def generate_dataset(self, num_profiles: int = 20, num_companies: int = 5, use_salt: bool = False) -> None:
        """Generate a complete dataset"""
        self.database = {'profiles': [], 'companies': [], 'social_profiles': [], 'relationships': []}
        
        print(f"\nGenerating {num_companies} companies...")
        
        # Generate companies first
        for i in range(num_companies):
            self.database['companies'].append(self.generate_company_profile())
        
        print(f"Generating {num_profiles} profiles{'with salted hashes' if use_salt else ''}...")
        
        # Generate profiles and assign to companies
        for i in range(num_profiles):
            profile = self.generate_profile(use_salt)
            # Assign to a random company
            if self.database['companies']:
                profile['company'] = random.choice(self.database['companies'])['name']
            
            self.database['profiles'].append(profile)
            
            # Generate social profile
            self.database['social_profiles'].append(self.generate_social_profile(profile))
            
            # Show progress
            if num_profiles >= 100:
                # More frequent updates for larger datasets
                if (i + 1) % 25 == 0 or i == num_profiles - 1:
                    print(f"  Generated {i + 1}/{num_profiles} profiles...")
            elif (i + 1) % 10 == 0 or i == num_profiles - 1:
                print(f"  Generated {i + 1}/{num_profiles} profiles...")

    def export_json(self, filename: str = None) -> str:
        """Export data to JSON format"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"osint_profiles_{timestamp}.json"
        
        export_data = {
            'metadata': {
                'exported_at': datetime.now().isoformat(),
                'total_profiles': len(self.database['profiles']),
                'total_companies': len(self.database['companies']),
                'format': 'OSINT_CLI_Export_v1.0',
                'generator': 'OSINT Profile Generator CLI'
            },
            'data': self.database
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
        
        return filename

    def export_txt(self, filename: str = None) -> str:
        """Export data to human-readable TXT format"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"osint_profiles_{timestamp}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            # Header
            f.write("="*80 + "\n")
            f.write("OSINT TRAINING PROFILES - SYNTHETIC DATA\n")
            f.write("="*80 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total Profiles: {len(self.database['profiles'])}\n")
            f.write(f"Total Companies: {len(self.database['companies'])}\n")
            f.write("="*80 + "\n\n")
            
            # Companies Section
            f.write("COMPANIES\n")
            f.write("-"*40 + "\n")
            for company in self.database['companies']:
                f.write(f"Company: {company['name']}\n")
                f.write(f"Industry: {company['industry']}\n")
                f.write(f"Size: {company['size']}\n")
                f.write(f"Location: {company['location']}\n")
                f.write(f"Website: {company['website']}\n")
                f.write(f"ID: {company['id']}\n")
                f.write("-"*40 + "\n")
            
            f.write("\n\nPROFILES\n")
            f.write("="*80 + "\n")
            
            # Profiles Section
            for i, profile in enumerate(self.database['profiles'], 1):
                f.write(f"\nPROFILE #{i:03d}\n")
                f.write("-"*40 + "\n")
                
                # Personal Information
                f.write(f"Name: {profile['full_name']}\n")
                f.write(f"Age: {profile['age']} years old\n")
                f.write(f"Birthday: {profile['birthdate']}\n")
                f.write(f"City: {profile['city']}\n")
                
                # Contact Information
                f.write(f"Email: {profile['email']}\n")
                f.write(f"Phone: {profile['phone']}\n")
                
                # Professional Information  
                f.write(f"Job Title: {profile['job_title']}\n")
                f.write(f"Company: {profile['company']}\n")
                
                # Education
                f.write(f"University: {profile['university']}\n")
                f.write(f"Graduation Year: {profile['graduation_year']}\n")
                
                # Social Media
                f.write(f"LinkedIn: {profile['social_profiles']['linkedin']}\n")
                f.write(f"LinkedIn Connections: {profile['linkedin_connections']}\n")
                f.write(f"Twitter: {profile['social_profiles']['twitter']}\n")
                if profile['social_profiles']['github']:
                    f.write(f"GitHub: {profile['social_profiles']['github']}\n")
                
                # Security Data (for educational purposes)
                f.write(f"Password Hint: {profile['password_hint']}\n")
                f.write(f"Password Hash (SHA-512): {profile['password_hash']}\n")
                
                # Metadata
                f.write(f"Profile ID: {profile['id']}\n")
                f.write(f"Generated: {profile['generated_at']}\n")
                f.write(f"Profile URL: {profile['url']}\n")
                
                # Social Media Stats
                social = next((s for s in self.database['social_profiles'] if s['person_id'] == profile['id']), None)
                if social:
                    f.write(f"Posts: {social['posts']}\n")
                    f.write(f"Followers: {social['followers']}\n")
                    f.write(f"Following: {social['following']}\n")
                    f.write(f"Last Active: {social['last_active']}\n")
                
                f.write("-"*40 + "\n")
        
        return filename

    def export_csv(self, filename: str = None) -> str:
        """Export profiles to CSV format"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"osint_profiles_{timestamp}.csv"
        
        headers = [
            'ID', 'FullName', 'FirstName', 'LastName', 'Email', 'Phone', 'Age', 'Birthdate',
            'Company', 'JobTitle', 'City', 'University', 'GraduationYear', 'LinkedInConnections',
            'LinkedIn', 'Twitter', 'GitHub', 'PasswordHint', 'PasswordHash', 'ProfileURL',
            'Posts', 'Followers', 'Following', 'LastActive', 'GeneratedAt'
        ]
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(','.join(headers) + '\n')
            
            for profile in self.database['profiles']:
                social = next((s for s in self.database['social_profiles'] if s['person_id'] == profile['id']), {})
                
                row = [
                    profile['id'],
                    f'"{profile["full_name"]}"',
                    f'"{profile["first_name"]}"', 
                    f'"{profile["last_name"]}"',
                    f'"{profile["email"]}"',
                    f'"{profile["phone"]}"',
                    str(profile['age']),
                    f'"{profile["birthdate"]}"',
                    f'"{profile["company"]}"',
                    f'"{profile["job_title"]}"',
                    f'"{profile["city"]}"',
                    f'"{profile["university"]}"',
                    str(profile['graduation_year']),
                    str(profile['linkedin_connections']),
                    f'"{profile["social_profiles"]["linkedin"]}"',
                    f'"{profile["social_profiles"]["twitter"]}"',
                    f'"{profile["social_profiles"]["github"] or ""}"',
                    f'"{profile["password_hint"]}"',
                    f'"{profile["password_hash"]}"',
                    f'"{profile["url"]}"',
                    str(social.get('posts', 0)),
                    str(social.get('followers', 0)),
                    str(social.get('following', 0)),
                    f'"{social.get("last_active", "")}"',
                    f'"{profile["generated_at"]}"'
                ]
                
                f.write(','.join(row) + '\n')
        
        return filename

    def generate_html_visualizer(self, filename: str = None) -> str:
        """Generate an HTML file to visualize the profiles"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"osint_profiles_{timestamp}.html"
        
        # Build HTML content using string concatenation to avoid f-string issues
        html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OSINT Profiles Visualizer</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        .header {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }
        .stat-card {
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
        .stat-number {
            font-size: 2em;
            font-weight: bold;
        }
        .stat-label {
            font-size: 0.9em;
            margin-top: 5px;
        }
        .content {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }
        .nav-tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 30px;
            border-bottom: 2px solid #eee;
        }
        .tab {
            padding: 12px 24px;
            background: #f8f9fa;
            border: none;
            border-radius: 8px 8px 0 0;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 500;
        }
        .tab.active {
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
        }
        .tab-content {
            display: none;
        }
        .tab-content.active {
            display: block;
        }
        .profile-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 20px;
        }
        .profile-card {
            background: white;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
            border-left: 5px solid #667eea;
            transition: transform 0.3s ease;
        }
        .profile-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        }
        .profile-header {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 15px;
        }
        .profile-pic {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid #667eea;
        }
        .profile-name {
            font-size: 18px;
            font-weight: bold;
            color: #333;
        }
        .profile-title {
            color: #667eea;
            font-size: 14px;
        }
        .profile-meta {
            color: #666;
            font-size: 12px;
            margin-top: 5px;
        }
        .profile-details {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-top: 15px;
            font-size: 13px;
        }
        .detail-item {
            padding: 8px;
            background: #f8f9ff;
            border-radius: 6px;
        }
        .detail-label {
            font-weight: bold;
            color: #764ba2;
        }
        .company-card {
            background: linear-gradient(45deg, #28a745, #20c997);
            color: white;
            border-left: 5px solid #155724;
        }
        .search-box {
            width: 100%;
            padding: 12px;
            border: 2px solid #667eea;
            border-radius: 25px;
            font-size: 16px;
            margin-bottom: 20px;
        }
        @media (max-width: 768px) {
            .profile-grid {
                grid-template-columns: 1fr;
            }
            .nav-tabs {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>OSINT Profiles Visualizer</h1>
            <p>Generated on ''' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '''</p>
            <div class="stats">
                <div class="stat-card">
                    <div class="stat-number">''' + str(len(self.database['profiles'])) + '''</div>
                    <div class="stat-label">Total Profiles</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">''' + str(len(self.database['companies'])) + '''</div>
                    <div class="stat-label">Companies</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">''' + str(len(self.database['social_profiles'])) + '''</div>
                    <div class="stat-label">Social Profiles</div>
                </div>
            </div>
        </div>
        <div class="content">
            <div class="nav-tabs">
                <button class="tab active" onclick="showTab('profiles')">Individual Profiles</button>
                <button class="tab" onclick="showTab('companies')">Companies</button>
                <button class="tab" onclick="showTab('social')">Social Media</button>
            </div>
            <input type="text" class="search-box" placeholder="Search profiles..." onkeyup="searchProfiles(this.value)">
            <div id="profiles" class="tab-content active">
                <div class="profile-grid">''' + self._generate_profile_cards() + '''</div>
            </div>
            <div id="companies" class="tab-content">
                <div class="profile-grid">''' + self._generate_company_cards() + '''</div>
            </div>
            <div id="social" class="tab-content">
                <div class="profile-grid">''' + self._generate_social_cards() + '''</div>
            </div>
        </div>
    </div>
    <script>
        function showTab(tabName) {
            document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
            document.getElementById(tabName).classList.add('active');
            event.target.classList.add('active');
        }
        function searchProfiles(query) {
            const cards = document.querySelectorAll('.profile-card');
            cards.forEach(card => {
                const text = card.textContent.toLowerCase();
                if (text.includes(query.toLowerCase())) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        }
    </script>
</body>
</html>'''

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return filename

    def export_hashes_only(self, filename: str = None) -> str:
        """Export only password hashes for hash cracking practice"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"osint_hashes_{timestamp}.txt"
        
        if not self.database['profiles']:
            raise ValueError("No profiles available. Generate profiles first.")
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("# OSINT Training Password Hashes (SHA-512)\n")
            f.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"# Total hashes: {len(self.database['profiles'])}\n")
            f.write("# Educational use only - for password cracking training\n")
            f.write("#" + "="*60 + "\n")
            f.write("# Format: username:hash\n")
            f.write("#" + "="*60 + "\n\n")
            
            for profile in self.database['profiles']:
                username = profile['email'].split('@')[0]  # Use email prefix as username
                password_hash = profile['password_hash']
                f.write(f"{username}:{password_hash}\n")
        
        return filename

    def export_salted_hashcat_format(self, filename: str = None) -> str:
        """Export salted hashes in hashcat format (hash:salt)"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"hashcat_salted_{timestamp}.txt"
        
        if not self.database['profiles']:
            raise ValueError("No profiles available. Generate profiles first.")
        
        salted_profiles = [p for p in self.database['profiles'] if p.get('hash_type') == 'SHA-512_SALTED']
        if not salted_profiles:
            raise ValueError("No salted hashes found. Generate profiles with salt option enabled.")
        
        with open(filename, 'w', encoding='utf-8') as f:
            for profile in salted_profiles:
                f.write(f"{profile['password_hash']}:{profile['salt']}\n")
        
        return filename

    def export_salt_reference(self, filename: str = None) -> str:
        """Export salt reference file with hash:salt:password mapping"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"salt_reference_{timestamp}.txt"
        
        if not self.database['profiles']:
            raise ValueError("No profiles available. Generate profiles first.")
        
        salted_profiles = [p for p in self.database['profiles'] if p.get('hash_type') == 'SHA-512_SALTED']
        if not salted_profiles:
            raise ValueError("No salted hashes found. Generate profiles with salt option enabled.")
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("# OSINT Training Salted Hash Reference\n")
            f.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"# Total entries: {len(salted_profiles)}\n")
            f.write("# Format: username | hash | salt | password_hint | full_name\n")
            f.write("#" + "="*80 + "\n\n")
            
            for profile in salted_profiles:
                username = profile['email'].split('@')[0]
                f.write(f"{username} | {profile['password_hash']} | {profile['salt']} | {profile['password_hint']} | {profile['full_name']}\n")
        
        return filename

    def export_hashcat_format(self, filename: str = None) -> str:
        """Export hashes in clean hashcat format (hash only, no usernames or metadata)"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"hashcat_hashes_{timestamp}.txt"
        
        if not self.database['profiles']:
            raise ValueError("No profiles available. Generate profiles first.")
        
        with open(filename, 'w', encoding='utf-8') as f:
            for profile in self.database['profiles']:
                f.write(f"{profile['password_hash']}\n")
        
        return filename

    def export_hash_reference(self, filename: str = None) -> str:
        """Export hash reference file with hints for educational purposes"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"osint_hash_reference_{timestamp}.txt"
        
        if not self.database['profiles']:
            raise ValueError("No profiles available. Generate profiles first.")
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("# OSINT Training Hash Reference File\n")
            f.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"# Total entries: {len(self.database['profiles'])}\n")
            f.write("# Educational use only - shows hash:password mapping for training\n")
            f.write("#" + "="*70 + "\n")
            f.write("# Format: username | hash | password_hint | full_name\n")
            f.write("#" + "="*70 + "\n\n")
            
            for profile in self.database['profiles']:
                username = profile['email'].split('@')[0]
                password_hash = profile['password_hash']
                password_hint = profile['password_hint']
                full_name = profile['full_name']
                f.write(f"{username} | {password_hash} | {password_hint} | {full_name}\n")
        
        return filename

    def generate_wordlist_from_json(self, json_filename: str, wordlist_filename: str = None) -> str:
        """Generate a wordlist from existing JSON file for password cracking training"""
        if not wordlist_filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            wordlist_filename = f"osint_wordlist_{timestamp}.txt"
        
        try:
            # Load JSON data
            with open(json_filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            profiles = data.get('data', {}).get('profiles', [])
            if not profiles:
                raise ValueError("No profiles found in JSON file")
            
            wordlist_entries = set()  # Use set to avoid duplicates
            
            # Generate wordlist entries from profile data
            for profile in profiles:
                # Add the actual password hint
                if 'password_hint' in profile:
                    wordlist_entries.add(profile['password_hint'])
                
                # Generate common password variations from profile data
                first_name = profile.get('first_name', '')
                last_name = profile.get('last_name', '')
                birth_year = str(profile.get('birth_year', ''))
                city = profile.get('city', '')
                company = profile.get('company', '').split(' ')[0] if profile.get('company') else ''
                university = profile.get('university', '').replace(' University', '').replace(' ', '') if profile.get('university') else ''
                
                # Common password patterns
                base_elements = [first_name, last_name, city, company, university]
                numbers = [birth_year, birth_year[-2:] if len(birth_year) >= 2 else '', '123', '1234', '12345']
                common_suffixes = ['!', '@', '#', '01', '02', '03', '99', '00']
                
                # Generate combinations
                for base in base_elements:
                    if base:
                        base_lower = base.lower()
                        base_cap = base.capitalize()
                        
                        # Just the base word
                        wordlist_entries.add(base_lower)
                        wordlist_entries.add(base_cap)
                        
                        # Base + numbers
                        for num in numbers:
                            if num:
                                wordlist_entries.add(base_lower + num)
                                wordlist_entries.add(base_cap + num)
                        
                        # Base + common suffixes
                        for suffix in common_suffixes:
                            wordlist_entries.add(base_lower + suffix)
                            wordlist_entries.add(base_cap + suffix)
                        
                        # Base + year + suffix combinations
                        if birth_year:
                            for suffix in ['!', '@', '#']:
                                wordlist_entries.add(base_lower + birth_year + suffix)
                                wordlist_entries.add(base_cap + birth_year + suffix)
                
                # Two-word combinations (most common actual pattern)
                for base1 in [first_name, last_name]:
                    for base2 in [last_name, city, company]:
                        if base1 and base2 and base1 != base2:
                            for num in ['', birth_year[-2:] if len(birth_year) >= 2 else '', '123']:
                                combo = base1.lower() + base2.lower() + num
                                wordlist_entries.add(combo)
                                combo_cap = base1.capitalize() + base2.capitalize() + num
                                wordlist_entries.add(combo_cap)
            
            # Sort wordlist by length then alphabetically for better organization
            sorted_wordlist = sorted(list(wordlist_entries), key=lambda x: (len(x), x.lower()))
            
            # Write wordlist file
            with open(wordlist_filename, 'w', encoding='utf-8') as f:
                f.write(f"# OSINT Training Wordlist\n")
                f.write(f"# Generated from: {json_filename}\n")
                f.write(f"# Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"# Total entries: {len(sorted_wordlist)}\n")
                f.write(f"# Educational use only - for password security training\n")
                f.write("#" + "="*60 + "\n\n")
                
                for entry in sorted_wordlist:
                    f.write(entry + '\n')
            
            return wordlist_filename
            
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file '{json_filename}' not found")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON file: '{json_filename}'")

    def generate_wordlist_from_current_data(self, wordlist_filename: str = None) -> str:
        """Generate wordlist from currently loaded profile data"""
        if not self.database['profiles']:
            raise ValueError("No profiles loaded. Generate profiles first.")
        
        if not wordlist_filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            wordlist_filename = f"osint_wordlist_{timestamp}.txt"
        
        # Create temporary JSON structure and use existing method
        temp_data = {
            'data': {
                'profiles': self.database['profiles']
            }
        }
        
        # Write temporary JSON
        temp_json = f"temp_wordlist_{timestamp}.json"
        with open(temp_json, 'w', encoding='utf-8') as f:
            json.dump(temp_data, f)
        
        try:
            # Generate wordlist from temp JSON
            result = self.generate_wordlist_from_json(temp_json, wordlist_filename)
            return result
        finally:
            # Clean up temp file
            if os.path.exists(temp_json):
                os.remove(temp_json)

    def _generate_profile_cards(self) -> str:
        """Generate HTML for profile cards"""
        cards = []
        for profile in self.database['profiles']:
            social = next((s for s in self.database['social_profiles'] if s['person_id'] == profile['id']), {})
            
            card = '<div class="profile-card" data-person-id="' + profile['id'] + '">'
            card += '<div class="profile-header">'
            card += '<img src="' + profile['profile_pic'] + '" alt="' + profile['full_name'] + '" class="profile-pic">'
            card += '<div>'
            card += '<div class="profile-name">' + profile['full_name'] + '</div>'
            card += '<div class="profile-title">' + profile['job_title'] + '</div>'
            card += '<div class="profile-meta">' + profile['company'] + ' • ' + profile['city'] + '</div>'
            card += '</div></div>'
            card += '<div class="profile-details">'
            card += '<div class="detail-item"><div class="detail-label">Email:</div>' + profile['email'] + '</div>'
            card += '<div class="detail-item"><div class="detail-label">Age:</div>' + str(profile['age']) + ' years old</div>'
            card += '<div class="detail-item"><div class="detail-label">University:</div>' + profile['university'] + '</div>'
            card += '<div class="detail-item"><div class="detail-label">LinkedIn:</div>' + str(profile['linkedin_connections']) + ' connections</div>'
            card += '<div class="detail-item"><div class="detail-label">Posts:</div>' + str(social.get('posts', 0)) + '</div>'
            card += '<div class="detail-item"><div class="detail-label">Followers:</div>' + str(social.get('followers', 0)) + '</div>'
            card += '</div></div>'
            
            cards.append(card)
        
        return ''.join(cards)

    def _generate_company_cards(self) -> str:
        """Generate HTML for company cards"""
        cards = []
        for company in self.database['companies']:
            employees = [p for p in self.database['profiles'] if p['company'] == company['name']]
            
            card = '<div class="profile-card company-card" data-company-id="' + company['id'] + '">'
            card += '<div class="profile-header">'
            card += '<div style="width: 60px; height: 60px; background: rgba(255,255,255,0.2); border-radius: 10px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 18px;">'
            card += company['name'][0] + '</div>'
            card += '<div>'
            card += '<div class="profile-name">' + company['name'] + '</div>'
            card += '<div class="profile-title">' + company['industry'] + '</div>'
            card += '<div class="profile-meta">' + company['location'] + ' • ' + str(len(employees)) + ' employees</div>'
            card += '</div></div>'
            card += '<div class="profile-details">'
            card += '<div class="detail-item"><div class="detail-label">Size:</div>' + company['size'] + '</div>'
            card += '<div class="detail-item"><div class="detail-label">Website:</div>' + company['website'] + '</div>'
            card += '<div class="detail-item"><div class="detail-label">Departments:</div>' + str(len(company['departments'])) + '</div>'
            card += '<div class="detail-item" style="grid-column: span 2;"><div class="detail-label">Recent Employees:</div>'
            card += ', '.join([emp['full_name'] for emp in employees[:3]])
            if len(employees) > 3:
                card += ' and ' + str(len(employees) - 3) + ' more'
            card += '</div></div></div>'
            
            cards.append(card)
        
        return ''.join(cards)

    def _generate_social_cards(self) -> str:
        """Generate HTML for social media cards"""
        cards = []
        for profile in self.database['profiles']:
            social = next((s for s in self.database['social_profiles'] if s['person_id'] == profile['id']), None)
            if not social:
                continue
                
            card = '<div class="profile-card" data-person-id="' + profile['id'] + '">'
            card += '<div class="profile-header">'
            card += '<img src="' + profile['profile_pic'] + '" alt="' + profile['full_name'] + '" class="profile-pic">'
            card += '<div>'
            card += '<div class="profile-name">@' + profile['first_name'].lower() + profile['last_name'].lower() + '</div>'
            card += '<div class="profile-title">' + profile['full_name'] + '</div>'
            card += '<div class="profile-meta">' + str(social['followers']) + ' followers • ' + str(social['posts']) + ' posts</div>'
            card += '</div></div>'
            card += '<div class="profile-details">'
            card += '<div class="detail-item"><div class="detail-label">Posts:</div>' + str(social['posts']) + '</div>'
            card += '<div class="detail-item"><div class="detail-label">Followers:</div>' + str(social['followers']) + '</div>'
            card += '<div class="detail-item"><div class="detail-label">Following:</div>' + str(social['following']) + '</div>'
            card += '<div class="detail-item"><div class="detail-label">Last Active:</div>' + datetime.fromisoformat(social['last_active']).strftime('%m/%d') + '</div>'
            card += '<div class="detail-item" style="grid-column: span 2;"><div class="detail-label">Social Links:</div>LinkedIn, Twitter'
            if profile['social_profiles']['github']:
                card += ', GitHub'
            card += '</div></div></div>'
            
            cards.append(card)
        
        return ''.join(cards)


class MenuInterface:
    def __init__(self):
        self.generator = OSINTProfileGenerator()
        self.clear_screen()

    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_banner(self):
        """Print the application banner"""
        print("="*60)
        print("🔍 OSINT PROFILE GENERATOR CLI")
        print("Educational Synthetic Data Generator for OSINT Training")
        print("="*60)
        print()

    def print_menu(self):
        """Print the main menu"""
        print("📋 MAIN MENU")
        print("-"*30)
        print("1. Generate Profiles")
        print("2. Export Data")
        print("3. Generate HTML Visualizer")
        print("4. Generate Wordlist")
        print("5. View Statistics")
        print("6. Clear All Data")
        print("7. Exit")
        print()

    def get_user_input(self, prompt: str, input_type: type = str, min_val: int = None, max_val: int = None):
        """Get and validate user input"""
        while True:
            try:
                value = input_type(input(prompt))
                if min_val is not None and value < min_val:
                    print(f"❌ Value must be at least {min_val}")
                    continue
                if max_val is not None and value > max_val:
                    print(f"❌ Value must be no more than {max_val}")
                    continue
                return value
            except ValueError:
                print(f"❌ Please enter a valid {input_type.__name__}")

    def generate_profiles_menu(self):
        """Handle profile generation"""
        self.clear_screen()
        self.print_banner()
        print("🎲 GENERATE PROFILES")
        print("-"*30)
        
        print("📊 Profile Amount Options:")
        print("1. Quick Test (10 profiles)")
        print("2. Small Dataset (25 profiles)")
        print("3. Medium Dataset (50 profiles)")
        print("4. Large Dataset (100 profiles)")
        print("5. Custom Amount (up to 1000)")
        print()
        
        amount_choice = self.get_user_input("Select profile amount (1-5): ", int, 1, 5)
        
        if amount_choice == 1:
            num_profiles = 10
        elif amount_choice == 2:
            num_profiles = 25
        elif amount_choice == 3:
            num_profiles = 50
        elif amount_choice == 4:
            num_profiles = 100
        elif amount_choice == 5:
            num_profiles = self.get_user_input("Enter custom amount (1-1000): ", int, 1, 1000)
        
        print(f"\n🏢 Company Amount Options:")
        print("1. Few Companies (3 companies)")
        print("2. Several Companies (5 companies)")
        print("3. Many Companies (10 companies)")
        print("4. Custom Amount")
        print()
        
        company_choice = self.get_user_input("Select company amount (1-4): ", int, 1, 4)
        
        if company_choice == 1:
            num_companies = 3
        elif company_choice == 2:
            num_companies = 5
        elif company_choice == 3:
            num_companies = 10
        elif company_choice == 4:
            num_companies = self.get_user_input("Enter custom amount (1-20): ", int, 1, 20)
        
        # Salt option
        print(f"\n🧂 Password Hash Options:")
        print("1. Standard SHA-512 (No Salt)")
        print("2. Salted SHA-512 (More Realistic)")
        print()
        
        salt_choice = self.get_user_input("Select hash type (1-2): ", int, 1, 2)
        use_salt = salt_choice == 2
        
        print(f"\n🔄 Generating {num_profiles} profiles and {num_companies} companies...")
        
        if num_profiles >= 500:
            print("⏳ Large dataset selected - this may take a few moments...")
        
        if use_salt:
            print("🧂 Using salted hashes for enhanced security training...")
        
        try:
            self.generator.generate_dataset(num_profiles, num_companies, use_salt)
            hash_type = "salted SHA-512" if use_salt else "SHA-512"
            print(f"✅ Successfully generated {num_profiles} profiles and {num_companies} companies with {hash_type} hashes!")
            
            # Ask if user wants to generate HTML visualizer
            generate_html = input("\n🌐 Generate HTML visualizer? (y/n): ").lower() == 'y'
            if generate_html:
                filename = self.generator.generate_html_visualizer()
                print(f"📄 HTML visualizer saved as: {filename}")
                
                open_browser = input("🌍 Open in browser? (y/n): ").lower() == 'y'
                if open_browser:
                    webbrowser.open(f'file://{os.path.abspath(filename)}')
                    print("🚀 Opening in browser...")
            
        except Exception as e:
            print(f"❌ Error generating profiles: {e}")
        
        input("\nPress Enter to continue...")

    def export_data_menu(self):
        """Handle data export"""
        if not self.generator.database['profiles']:
            print("❌ No profiles to export! Generate profiles first.")
            input("Press Enter to continue...")
            return
        
        self.clear_screen()
        self.print_banner()
        print("💾 EXPORT DATA")
        print("-"*30)
        print("1. JSON Format (Complete Data)")
        print("2. TXT Format (Human Readable)")  
        print("3. CSV Format (Spreadsheet)")
        print("4. Hashes Only (With Usernames)")
        print("5. Hashcat Format (Clean Hashes Only)")
        print("6. Salted Hashcat Format (Hash:Salt)")
        print("7. Hash Reference (Hashes with Hints)")
        print("8. Salt Reference (Salted Hashes with Hints)")
        print("9. All Standard Formats")
        print("10. Back to Main Menu")
        print()
        
        choice = self.get_user_input("Select export format (1-10): ", int, 1, 10)
        
        if choice == 10:
            return
        
        # Get custom filename
        custom_name = input("📝 Custom filename prefix (optional): ").strip()
        
        exported_files = []
        
        try:
            if choice in [1, 9]:  # JSON
                filename = f"{custom_name}.json" if custom_name else None
                file = self.generator.export_json(filename)
                exported_files.append(file)
                print(f"✅ JSON exported: {file}")
            
            if choice in [2, 9]:  # TXT
                filename = f"{custom_name}.txt" if custom_name else None
                file = self.generator.export_txt(filename)
                exported_files.append(file)
                print(f"✅ TXT exported: {file}")
            
            if choice in [3, 9]:  # CSV
                filename = f"{custom_name}.csv" if custom_name else None
                file = self.generator.export_csv(filename)
                exported_files.append(file)
                print(f"✅ CSV exported: {file}")
            
            if choice == 4:  # Hashes with usernames
                filename = f"{custom_name}_hashes.txt" if custom_name else None
                file = self.generator.export_hashes_only(filename)
                exported_files.append(file)
                print(f"✅ Hashes with usernames exported: {file}")
                
                # Show preview of hash file
                with open(file, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    hash_lines = [line.strip() for line in lines if not line.startswith('#') and line.strip()]
                
                print(f"\n🔒 Generated {len(hash_lines)} password hashes (with usernames)")
                print("🔍 Preview (first 3 entries):")
                for i, line in enumerate(hash_lines[:3]):
                    username, hash_val = line.split(':', 1)
                    print(f"  {i+1}. {username}:{hash_val[:20]}...{hash_val[-10:]}")
            
            if choice == 5:  # Hashcat format (clean hashes only)
                filename = f"{custom_name}_hashcat.txt" if custom_name else None
                file = self.generator.export_hashcat_format(filename)
                exported_files.append(file)
                print(f"✅ Hashcat format exported: {file}")
                
                # Show preview and hashcat usage info
                with open(file, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    hash_lines = [line.strip() for line in lines if line.strip()]
                
                print(f"\n🔒 Generated {len(hash_lines)} clean SHA-512 hashes")
                print("🔍 Preview (first 3 entries):")
                for i, hash_val in enumerate(hash_lines[:3]):
                    print(f"  {i+1}. {hash_val[:30]}...{hash_val[-20:]}")
                
                print(f"\n💡 Hashcat Usage:")
                print(f"   hashcat -m 1700 {file} wordlist.txt")
                print(f"   (Mode 1700 = SHA-512)")
            
            if choice == 6:  # Salted Hashcat format
                try:
                    filename = f"{custom_name}_salted_hashcat.txt" if custom_name else None
                    file = self.generator.export_salted_hashcat_format(filename)
                    exported_files.append(file)
                    print(f"✅ Salted Hashcat format exported: {file}")
                    
                    # Show preview and usage info
                    with open(file, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        hash_lines = [line.strip() for line in lines if line.strip()]
                    
                    print(f"\n🧂 Generated {len(hash_lines)} salted SHA-512 hashes")
                    print("🔍 Preview (first 3 entries):")
                    for i, line in enumerate(hash_lines[:3]):
                        hash_part, salt_part = line.split(':', 1)
                        print(f"  {i+1}. {hash_part[:20]}...:{salt_part}")
                    
                    print(f"\n💡 Hashcat Usage:")
                    print(f"   hashcat -m 1710 {file} wordlist.txt")
                    print(f"   (Mode 1710 = SHA-512 with salt)")
                    
                except ValueError as e:
                    print(f"❌ {e}")
                    print("💡 Generate profiles with salt option enabled first!")
            
            if choice == 7:  # Hash reference
                filename = f"{custom_name}_hash_reference.txt" if custom_name else None
                file = self.generator.export_hash_reference(filename)
                exported_files.append(file)
                print(f"✅ Hash reference exported: {file}")
                
                # Show preview
                with open(file, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    ref_lines = [line.strip() for line in lines if not line.startswith('#') and line.strip()]
                
                print(f"\n🔑 Generated {len(ref_lines)} hash references")
                print("🔍 Preview (first 3 entries):")
                for i, line in enumerate(ref_lines[:3]):
                    parts = line.split(' | ')
                    if len(parts) >= 3:
                        username, hash_val, hint = parts[0], parts[1], parts[2]
                        print(f"  {i+1}. {username} | {hash_val[:15]}... | {hint}")
            
            if choice == 8:  # Salt reference
                try:
                    filename = f"{custom_name}_salt_reference.txt" if custom_name else None
                    file = self.generator.export_salt_reference(filename)
                    exported_files.append(file)
                    print(f"✅ Salt reference exported: {file}")
                    
                    # Show preview
                    with open(file, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        ref_lines = [line.strip() for line in lines if not line.startswith('#') and line.strip()]
                    
                    print(f"\n🧂 Generated {len(ref_lines)} salted hash references")
                    print("🔍 Preview (first 3 entries):")
                    for i, line in enumerate(ref_lines[:3]):
                        parts = line.split(' | ')
                        if len(parts) >= 4:
                            username, hash_val, salt, hint = parts[0], parts[1], parts[2], parts[3]
                            print(f"  {i+1}. {username} | {hash_val[:15]}... | {salt[:8]}... | {hint}")
                            
                except ValueError as e:
                    print(f"❌ {e}")
                    print("💡 Generate profiles with salt option enabled first!")
            
            print(f"\n🎉 Successfully exported {len(exported_files)} file(s)!")
            
            if choice in [4, 5, 6, 7, 8]:
                print(f"\n⚠️  EDUCATIONAL USE ONLY")
                print("These hash files are for password security training and ethical testing only.")
                print("Use responsibly on systems you own or have explicit permission to test.")
            
        except Exception as e:
            print(f"❌ Export error: {e}")
        
        input("\nPress Enter to continue...")

    def generate_html_menu(self):
        """Handle HTML visualizer generation"""
        if not self.generator.database['profiles']:
            print("❌ No profiles to visualize! Generate profiles first.")
            input("Press Enter to continue...")
            return
        
        self.clear_screen()
        self.print_banner()
        print("🌐 GENERATE HTML VISUALIZER")
        print("-"*30)
        
        custom_name = input("📝 Custom filename (optional): ").strip()
        filename = f"{custom_name}.html" if custom_name else None
        
        try:
            file = self.generator.generate_html_visualizer(filename)
            print(f"✅ HTML visualizer generated: {file}")
            
            open_browser = input("🌍 Open in browser? (y/n): ").lower() == 'y'
            if open_browser:
                webbrowser.open(f'file://{os.path.abspath(file)}')
                print("🚀 Opening in browser...")
            
        except Exception as e:
            print(f"❌ Error generating HTML: {e}")
        
        input("\nPress Enter to continue...")

    def generate_wordlist_menu(self):
        """Handle wordlist generation"""
        self.clear_screen()
        self.print_banner()
        print("📝 GENERATE WORDLIST")
        print("-"*30)
        print("1. Generate from current profiles")
        print("2. Generate from existing JSON file")
        print("3. Back to Main Menu")
        print()
        
        choice = self.get_user_input("Select option (1-3): ", int, 1, 3)
        
        if choice == 3:
            return
        
        custom_name = input("📝 Custom wordlist filename (optional): ").strip()
        wordlist_filename = f"{custom_name}.txt" if custom_name else None
        
        try:
            if choice == 1:
                # Generate from current data
                if not self.generator.database['profiles']:
                    print("❌ No profiles loaded! Generate profiles first.")
                    input("Press Enter to continue...")
                    return
                
                filename = self.generator.generate_wordlist_from_current_data(wordlist_filename)
                print(f"✅ Wordlist generated: {filename}")
                
                # Show preview of first few entries
                with open(filename, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    data_lines = [line.strip() for line in lines if not line.startswith('#') and line.strip()]
                    
                print(f"\n📊 Generated {len(data_lines)} unique password candidates")
                print(f"🔍 Preview (first 10 entries):")
                for i, entry in enumerate(data_lines[:10]):
                    print(f"  {i+1}. {entry}")
                if len(data_lines) > 10:
                    print(f"  ... and {len(data_lines) - 10} more entries")
            
            elif choice == 2:
                # Generate from JSON file
                json_filename = input("📁 Enter JSON filename: ").strip()
                if not json_filename:
                    print("❌ No filename provided!")
                    input("Press Enter to continue...")
                    return
                
                filename = self.generator.generate_wordlist_from_json(json_filename, wordlist_filename)
                print(f"✅ Wordlist generated: {filename}")
                
                # Show preview
                with open(filename, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    data_lines = [line.strip() for line in lines if not line.startswith('#') and line.strip()]
                    
                print(f"\n📊 Generated {len(data_lines)} unique password candidates")
                print(f"🔍 Preview (first 10 entries):")
                for i, entry in enumerate(data_lines[:10]):
                    print(f"  {i+1}. {entry}")
        
        except FileNotFoundError as e:
            print(f"❌ File error: {e}")
        except ValueError as e:
            print(f"❌ Data error: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
        
        print(f"\n⚠️  EDUCATIONAL USE ONLY")
        print("This wordlist is for password security training and ethical penetration testing.")
        print("Use responsibly and only on systems you own or have explicit permission to test.")
        
        input("\nPress Enter to continue...")

    def view_statistics(self):
        """Display statistics about generated data"""
        self.clear_screen()
        self.print_banner()
        print("📊 DATA STATISTICS")
        print("-"*30)
        
        profiles = len(self.generator.database['profiles'])
        companies = len(self.generator.database['companies'])
        social_profiles = len(self.generator.database['social_profiles'])
        
        print(f"👥 Total Profiles: {profiles}")
        print(f"🏢 Total Companies: {companies}")
        print(f"📱 Social Profiles: {social_profiles}")
        
        if profiles > 0:
            print(f"\n🔍 PROFILE BREAKDOWN")
            print("-"*20)
            
            # Age distribution
            ages = [p['age'] for p in self.generator.database['profiles']]
            avg_age = sum(ages) / len(ages) if ages else 0
            print(f"📈 Average Age: {avg_age:.1f} years")
            
            # Company distribution
            company_counts = {}
            for profile in self.generator.database['profiles']:
                company = profile['company']
                company_counts[company] = company_counts.get(company, 0) + 1
            
            print(f"🏆 Most Popular Company: {max(company_counts, key=company_counts.get)} ({max(company_counts.values())} employees)")
            
            # Show sample profile
            sample = self.generator.database['profiles'][0]
            print(f"\n👤 SAMPLE PROFILE")
            print("-"*20)
            print(f"Name: {sample['full_name']}")
            print(f"Email: {sample['email']}")
            print(f"Company: {sample['company']}")
            print(f"City: {sample['city']}")
        
        else:
            print("\n❌ No data available. Generate profiles first!")
        
        input("\nPress Enter to continue...")

    def clear_data(self):
        """Clear all generated data"""
        if not self.generator.database['profiles']:
            print("❌ No data to clear!")
            input("Press Enter to continue...")
            return
        
        confirm = input("⚠️  Are you sure you want to clear all data? (y/n): ").lower()
        if confirm == 'y':
            self.generator.database = {'profiles': [], 'companies': [], 'social_profiles': [], 'relationships': []}
            print("✅ All data cleared!")
        else:
            print("❌ Clear cancelled.")
        
        input("Press Enter to continue...")

    def run(self):
        """Main application loop"""
        while True:
            self.clear_screen()
            self.print_banner()
            
            # Show current data status
            profiles_count = len(self.generator.database['profiles'])
            companies_count = len(self.generator.database['companies'])
            
            if profiles_count > 0:
                print(f"📊 Current Data: {profiles_count} profiles, {companies_count} companies")
                print()
            
            self.print_menu()
            
            choice = self.get_user_input("Select option (1-7): ", int, 1, 7)
            
            if choice == 1:
                self.generate_profiles_menu()
            elif choice == 2:
                self.export_data_menu()
            elif choice == 3:
                self.generate_html_menu()
            elif choice == 4:
                self.generate_wordlist_menu()
            elif choice == 5:
                self.view_statistics()
            elif choice == 6:
                self.clear_data()
            elif choice == 7:
                print("👋 Goodbye!")
                break


def main():
    """Main entry point"""
    try:
        menu = MenuInterface()
        menu.run()
    except KeyboardInterrupt:
        print("\n\n❌ Application interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
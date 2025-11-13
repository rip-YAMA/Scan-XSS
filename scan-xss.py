#!/usr/bin/env python3
"""
XSS GUARDIAN - PREMIUM EDITION
Developer: YAMA
Partner: Takanashi Hoshino
"""

import requests
import urllib.parse
import time
import sys
import threading
from colorama import Fore, Style, init

init(autoreset=True)

class Colors:
    PRIMARY = Fore.CYAN + Style.BRIGHT
    SECONDARY = Fore.BLUE + Style.BRIGHT
    SUCCESS = Fore.GREEN + Style.BRIGHT
    WARNING = Fore.YELLOW + Style.BRIGHT
    DANGER = Fore.RED + Style.BRIGHT
    INFO = Fore.WHITE + Style.BRIGHT
    RESET = Style.RESET_ALL

class PremiumAnimations:
    @staticmethod
    def sleek_loading(text="Loading", duration=2):
        """Loading animation yang sleek dan professional"""
        frames = ["▱", "▰"]
        start_time = time.time()
        
        while time.time() - start_time < duration:
            for frame in frames:
                print(f"\r{Colors.PRIMARY}{frame} {text}{Colors.RESET}", end="", flush=True)
                time.sleep(0.2)
        print(f"\r{Colors.SUCCESS}✓ {text} Complete{' ' * 20}{Colors.RESET}")
    
    @staticmethod
    def progress_bar(description, duration=3):
        """Progress bar yang elegant"""
        print(f"\n{Colors.SECONDARY}{description}{Colors.RESET}")
        width = 30
        
        for i in range(width + 1):
            percentage = (i * 100) // width
            bar = "█" * i + "░" * (width - i)
            print(f"\r{Colors.PRIMARY}[{bar}] {percentage}%{Colors.RESET}", end="", flush=True)
            time.sleep(duration / width)
        print()
    
    @staticmethod
    def scanning_animation(stop_event):
        """Animasi scanning yang subtle"""
        states = ["Analyzing", "Processing", "Scanning", "Testing"]
        dots = ["", ".", "..", "..."]
        
        while not stop_event.is_set():
            for state in states:
                for dot in dots:
                    if stop_event.is_set():
                        return
                    print(f"\r{Colors.INFO}{state}{dot}{' ' * 10}{Colors.RESET}", end="", flush=True)
                    time.sleep(0.3)

class PremiumXSSScanner:
    def __init__(self):
        self.developer = "YAMA"
        self.partner = "Takanashi Hoshino"
        self.version = "Premium v1.0"
        
        self.payloads = [
            '<script>alert("XSS")</script>',
            '<img src=x onerror=alert("XSS")>',
            '<svg onload=alert("XSS")>',
            '"><script>alert("XSS")</script>',
            'javascript:alert("XSS")'
        ]
    
    def show_premium_header(self):
        """Header yang clean dan professional"""
        print(f"\n{Colors.PRIMARY}{'=' * 50}")
        print(f"🛡️  XSS SECURITY SCANNER")
        print(f"{'=' * 50}")
        print(f"👨‍💻 Developer: {self.developer}")
        print(f"🤝 Partner: {self.partner}") 
        print(f"📦 Version: {self.version}")
        print(f"{'=' * 50}{Colors.RESET}")
        time.sleep(1)
    
    def scan_target(self, url):
        """Fungsi scanning yang powerful dan elegant"""
        print(f"\n{Colors.INFO}🎯 Target: {url}{Colors.RESET}")
        
        # Step 1: Initialization
        PremiumAnimations.sleek_loading("Initializing Scanner", 1.5)
        
        # Step 2: Parameter Discovery
        PremiumAnimations.progress_bar("Discovering URL Parameters", 2)
        
        try:
            parsed = urllib.parse.urlparse(url)
            params = urllib.parse.parse_qs(parsed.query)
            
            if not params:
                print(f"{Colors.WARNING}⚠️ No parameters found in URL{Colors.RESET}")
                return []
            
            print(f"{Colors.SUCCESS}✅ Found {len(params)} parameters{Colors.RESET}")
            
            # Step 3: Payload Preparation
            PremiumAnimations.progress_bar("Preparing XSS Payloads", 1.5)
            
            vulnerabilities = []
            
            # Step 4: Main Scanning
            print(f"\n{Colors.INFO}🚀 Starting Security Scan...{Colors.RESET}")
            
            stop_animation = threading.Event()
            animation_thread = threading.Thread(
                target=PremiumAnimations.scanning_animation,
                args=(stop_animation,)
            )
            animation_thread.start()
            
            # Real scanning logic
            for param_name in params:
                print(f"\n{Colors.SECONDARY}🔍 Testing parameter: {param_name}{Colors.RESET}")
                
                for payload in self.payloads:
                    try:
                        test_params = params.copy()
                        test_params[param_name] = [payload]
                        
                        new_query = urllib.parse.urlencode(test_params, doseq=True)
                        test_url = urllib.parse.urlunparse((
                            parsed.scheme, parsed.netloc, parsed.path,
                            parsed.params, new_query, parsed.fragment
                        ))
                        
                        response = requests.get(test_url, timeout=10, verify=False)
                        
                        if payload in response.text:
                            vulnerability = {
                                'parameter': param_name,
                                'payload': payload,
                                'type': 'Reflected XSS',
                                'risk': 'HIGH',
                                'url': test_url
                            }
                            vulnerabilities.append(vulnerability)
                            print(f"\r{Colors.DANGER}❌ VULNERABILITY FOUND: {param_name}{' ' * 30}{Colors.RESET}")
                            break
                            
                    except requests.RequestException:
                        continue
                    except Exception as e:
                        print(f"{Colors.WARNING}⚠️ Error testing {param_name}: {e}{Colors.RESET}")
                        continue
            
            stop_animation.set()
            animation_thread.join()
            
            return vulnerabilities
            
        except Exception as e:
            print(f"{Colors.DANGER}💥 Scan Error: {e}{Colors.RESET}")
            return []
    
    def generate_premium_report(self, url, vulnerabilities):
        """Generate laporan yang professional"""
        report = f"""
XSS SECURITY ASSESSMENT REPORT
{'=' * 50}

Assessment Details:
├─ Target URL: {url}
├─ Scan Date: {time.strftime('%Y-%m-%d %H:%M:%S')}
├─ Scanner: XSS Guardian Premium
├─ Developer: {self.developer}
└─ Partner: {self.partner}

Executive Summary:
├─ Total Vulnerabilities: {len(vulnerabilities)}
├─ Risk Level: {'HIGH' if vulnerabilities else 'LOW'}
└─ Status: {'REQUIRES IMMEDIATE ATTENTION' if vulnerabilities else 'SECURE'}

Vulnerability Details:
"""
        
        if vulnerabilities:
            for i, vuln in enumerate(vulnerabilities, 1):
                report += f"""
{i}. Reflected XSS Vulnerability
   ├─ Parameter: {vuln['parameter']}
   ├─ Payload: {vuln['payload']}
   ├─ Risk: {vuln['risk']}
   └─ Type: {vuln['type']}
"""
        else:
            report += "\nNo vulnerabilities detected.\n"
        
        report += f"""
Security Recommendations:
├─ 1. Implement proper input validation
├─ 2. Use output encoding for all user data
├─ 3. Deploy Content Security Policy (CSP)
├─ 4. Conduct regular security assessments
└─ 5. Keep software dependencies updated

Report Generated by:
XSS Guardian Premium - Professional Security Tool
Developer: {self.developer} | Partner: {self.partner}
"""
        return report
    
    def save_report(self, report, filename=None):
        """Save report dengan format yang rapi"""
        if not filename:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"xss_report_{timestamp}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"{Colors.SUCCESS}📄 Report saved: {filename}{Colors.RESET}")
            return True
        except Exception as e:
            print(f"{Colors.DANGER}❌ Error saving report: {e}{Colors.RESET}")
            return False

def main():
    scanner = PremiumXSSScanner()
    
    # Clear screen
    print("\033c", end="")
    
    # Show premium header
    scanner.show_premium_header()
    
    while True:
        print(f"\n{Colors.PRIMARY}🛡️  MAIN MENU")
        print(f"{Colors.SECONDARY}1. Security Scan")
        print(f"2. Quick Demo")
        print(f"3. Exit{Colors.RESET}")
        
        choice = input(f"\n{Colors.INFO}Select option: {Colors.RESET}").strip()
        
        if choice == '1':
            url = input(f"\n{Colors.INFO}Enter target URL: {Colors.RESET}").strip()
            
            if not url.startswith(('http://', 'https://')):
                print(f"{Colors.WARNING}⚠️ Please include protocol (http:// or https://){Colors.RESET}")
                continue
            
            print(f"{Colors.WARNING}🔒 Ethical Notice: Only scan authorized targets{Colors.RESET}")
            confirm = input(f"{Colors.INFO}Confirm scan? (y/n): {Colors.RESET}").strip().lower()
            
            if confirm != 'y':
                print(f"{Colors.INFO}Scan cancelled.{Colors.RESET}")
                continue
            
            # Execute scan
            vulnerabilities = scanner.scan_target(url)
            
            # Display results
            print(f"\n{Colors.PRIMARY}{'=' * 50}")
            print(f"📊 SCAN RESULTS")
            print(f"{'=' * 50}{Colors.RESET}")
            
            if vulnerabilities:
                print(f"{Colors.DANGER}❌ SECURITY ALERT: {len(vulnerabilities)} vulnerabilities found{Colors.RESET}")
                
                for vuln in vulnerabilities:
                    print(f"\n{Colors.DANGER}● Parameter: {vuln['parameter']}")
                    print(f"● Type: {vuln['type']}")
                    print(f"● Risk: {vuln['risk']}{Colors.RESET}")
                
                # Generate and offer to save report
                report = scanner.generate_premium_report(url, vulnerabilities)
                print(f"\n{report}")
                
                save = input(f"\n{Colors.INFO}Save detailed report? (y/n): {Colors.RESET}").lower()
                if save == 'y':
                    scanner.save_report(report)
            else:
                print(f"{Colors.SUCCESS}✅ No security vulnerabilities detected{Colors.RESET}")
                print(f"{Colors.INFO}The target appears to be secure against basic XSS attacks.{Colors.RESET}")
        
        elif choice == '2':
            print(f"\n{Colors.INFO}Running quick security demo...{Colors.RESET}")
            demo_url = "https://httpbin.org/get?test=security"
            scanner.scan_target(demo_url)
        
        elif choice == '3':
            print(f"\n{Colors.SUCCESS}✅ Thank you for using XSS Guardian Premium{Colors.RESET}")
            print(f"{Colors.INFO}Developer: {scanner.developer}{Colors.RESET}")
            break
        
        else:
            print(f"{Colors.WARNING}⚠️ Invalid selection{Colors.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.INFO}👋 Scan interrupted by user{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.DANGER}💥 Application Error: {e}{Colors.RESET}")
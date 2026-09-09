import csv
import random
import uuid

CWE_CLASSES = [
    {
        "cwe_id": "CWE-693",
        "description": "Protection Mechanism Failure (Missing CSP)",
        "vulnerable_syntax": "HTTP/1.1 200 OK\nServer: nginx\nContent-Type: text/html",
        "patch_diff": "+ Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-random123'; object-src 'none'",
        "remediation_explanation": "Added Content-Security-Policy header to mitigate XSS vulnerabilities by restricting the sources of executable scripts."
    },
    {
        "cwe_id": "CWE-942",
        "description": "Overly Permissive CORS Policy",
        "vulnerable_syntax": "Access-Control-Allow-Origin: *",
        "patch_diff": "- Access-Control-Allow-Origin: *\n+ Access-Control-Allow-Origin: https://trusted-domain.com",
        "remediation_explanation": "Restricted CORS origin to a specific trusted domain instead of a wildcard to prevent unauthorized cross-origin resource access."
    },
    {
        "cwe_id": "CWE-548",
        "description": "Information Exposure Through Directory Listing (Exposed .git)",
        "vulnerable_syntax": "location /.git {\n    autoindex on;\n}",
        "patch_diff": "- autoindex on;\n+ deny all;",
        "remediation_explanation": "Disabled directory listing and denied access to the .git directory to prevent source code and configuration exposure."
    },
    {
        "cwe_id": "CWE-319",
        "description": "Cleartext Transmission of Sensitive Information (Missing HSTS)",
        "vulnerable_syntax": "Strict-Transport-Security: max-age=0",
        "patch_diff": "- Strict-Transport-Security: max-age=0\n+ Strict-Transport-Security: max-age=31536000; includeSubDomains; preload",
        "remediation_explanation": "Enforced HTTP Strict Transport Security (HSTS) to ensure all communications are encrypted over HTTPS."
    },
    {
        "cwe_id": "CWE-200",
        "description": "Exposure of Sensitive Information to an Unauthorized Actor (Server Banner)",
        "vulnerable_syntax": "Server: Apache/2.4.41 (Ubuntu)",
        "patch_diff": "- Server: Apache/2.4.41 (Ubuntu)\n+ Server: Apache",
        "remediation_explanation": "Removed verbose server version information from the Server header to thwart targeted automated attacks."
    }
]

def generate_patch_pair(pair_id):
    cwe_template = random.choice(CWE_CLASSES)
    
    nuclei_id = f"nuclei-{cwe_template['cwe_id'].lower()}-template"
    cve_id = f"CVE-2023-{random.randint(1000, 9999)}" if random.random() > 0.5 else "N/A"
    
    return {
        "patch_id": f"PATCH-{pair_id:04d}",
        "nuclei_template_id": nuclei_id,
        "cwe_cve_mapping": f"{cwe_template['cwe_id']} / {cve_id}",
        "vulnerable_syntax_token_sequence": cwe_template["vulnerable_syntax"],
        "recommended_replacement_patch_diff": cwe_template["patch_diff"],
        "operational_remediation_explanation": cwe_template["remediation_explanation"]
    }

def main():
    num_samples = 1200
    output_file = "cwe_patch_corpus.csv"
    
    print(f"Generating {num_samples} synthetic CWE patch pairs...")
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            "patch_id", 
            "nuclei_template_id", 
            "cwe_cve_mapping", 
            "vulnerable_syntax_token_sequence", 
            "recommended_replacement_patch_diff", 
            "operational_remediation_explanation"
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for i in range(1, num_samples + 1):
            pair = generate_patch_pair(i)
            writer.writerow(pair)
            
    print(f"Dataset successfully saved to {output_file}")

if __name__ == "__main__":
    main()

import csv
import random
import datetime
import uuid

# Categories and Vectors
CATEGORIES = [
    "Financial UPI/Banking Fraud",
    "Job Offer Scams",
    "Cyberbullying/Harassment",
    "Matrimonial/Impersonation Scams",
    "Identity Theft"
]

VECTORS = ["WhatsApp", "SMS", "Telegram", "Phone"]

# Sample synthetic data building blocks
NAMES = ["Amit", "Priya", "Rahul", "Sneha", "Vikram", "Anjali", "Rohan", "Pooja"]
BANKS = ["HDFC", "SBI", "ICICI", "Axis", "Kotak"]
UPI_HANDLES = ["@okicici", "@oksbi", "@paytm", "@ybl", "@apl"]

COMPLAINT_TEMPLATES = {
    "Financial UPI/Banking Fraud": [
        "I received a call from someone claiming to be from {bank} asking for my UPI pin to block a fraudulent transaction. I lost {amount} INR.",
        "A person on {vector} sent me a QR code to receive payment for my OLX listing, but money was deducted from my account instead."
    ],
    "Job Offer Scams": [
        "I was offered a part-time job via {vector} to like YouTube videos. After initial small payments, they asked me to invest {amount} INR for premium tasks and then disappeared.",
        "Fake recruiter from a reputed company contacted me on {vector} asking for a registration fee of {amount} INR."
    ],
    "Cyberbullying/Harassment": [
        "Someone is sending abusive messages and morphing my photos on {vector}. I am feeling severely harassed.",
        "An anonymous user on {vector} is continuously threatening me and demanding money."
    ],
    "Matrimonial/Impersonation Scams": [
        "I met someone on a matrimonial site who shifted the conversation to {vector}. They claimed a medical emergency and I sent {amount} INR.",
        "A person impersonated an NRI doctor and asked for {amount} INR customs clearance fee for a gift they supposedly sent me."
    ],
    "Identity Theft": [
        "My PAN card details were used to take a loan of {amount} INR without my knowledge. I found out when recovery agents called me.",
        "Someone created a fake profile using my name and photos and is asking my contacts for money on {vector}."
    ]
}

OCR_TEMPLATES = {
    "Financial UPI/Banking Fraud": "Paid to {suspect_upi}\nAmount: Rs. {amount}\nStatus: SUCCESS\nTxn ID: {txn_id}",
    "Job Offer Scams": "VIP Task: Recharge {amount} to unlock 30% commission.\nSend screenshot after payment to {suspect_upi}.",
    "Cyberbullying/Harassment": "Pay {amount} now or I will leak these photos.\nUPI: {suspect_upi}",
    "Matrimonial/Impersonation Scams": "Customs clearance fee required: {amount} INR. Pay to {suspect_upi} immediately to release the parcel.",
    "Identity Theft": "Dear Customer, your loan of Rs. {amount} is approved. Verification fee of Rs. 1000 required."
}

def generate_incident(incident_id):
    category = random.choice(CATEGORIES)
    vector = random.choice(VECTORS)
    amount = random.randint(1000, 500000) if category != "Cyberbullying/Harassment" else random.choice([0, random.randint(1000, 10000)])
    bank = random.choice(BANKS)
    suspect_upi = f"{random.choice(NAMES).lower()}{random.randint(100, 999)}{random.choice(UPI_HANDLES)}"
    
    # Generate temporal logs
    days_ago = random.randint(1, 365)
    incident_date = datetime.datetime.now() - datetime.timedelta(days=days_ago)
    temporal_logs = incident_date.strftime("%Y-%m-%dT%H:%M:%SZ")
    
    txn_id = f"TXN{uuid.uuid4().hex[:10].upper()}"
    
    complaint_template = random.choice(COMPLAINT_TEMPLATES[category])
    complaint_narrative = complaint_template.format(bank=bank, vector=vector, amount=amount)
    
    ocr_template = OCR_TEMPLATES[category]
    ocr_evidence = ocr_template.format(suspect_upi=suspect_upi, amount=amount, txn_id=txn_id)
    
    return {
        "incident_id": f"INC-{incident_id:06d}",
        "category": category,
        "temporal_logs": temporal_logs,
        "monetary_loss_inr": amount,
        "scam_vector": vector,
        "suspect_bank_upi": suspect_upi,
        "complaint_narrative": complaint_narrative,
        "synthetic_ocr_evidence": ocr_evidence
    }

def main():
    num_samples = 15000
    output_file = "synthetic_cybercrime_corpus.csv"
    
    print(f"Generating {num_samples} synthetic incidents...")
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["incident_id", "category", "temporal_logs", "monetary_loss_inr", "scam_vector", "suspect_bank_upi", "complaint_narrative", "synthetic_ocr_evidence"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for i in range(1, num_samples + 1):
            incident = generate_incident(i)
            writer.writerow(incident)
            
    print(f"Dataset successfully saved to {output_file}")

if __name__ == "__main__":
    main()

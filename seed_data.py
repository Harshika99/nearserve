import asyncio
import logging
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import GEOSPHERE
from app.config import get_settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("settlerpulse.seed")

DEMO_PROVIDERS_HYDERABAD = [
    {
        "name": "Ravi Teja",
        "business_name": "Ravi Electricals & Plumbing",
        "category": "Plumbing",
        "skills": ["Tap leakage repair", "Flush tank fitting", "Pipe soldering"],
        "rating": 4.8,
        "total_reviews": 127,
        "completed_jobs": 135,
        "verified_jobs": 121,
        "repeat_customers_pct": 42,
        "avg_response_mins": 6,
        "distance_km": 0.8,
        "eta_mins": 7,
        "estimated_price_range": "₹150 – ₹300",
        "languages": ["Telugu", "Hindi", "English"],
        "availability_status": "AVAILABLE",
        "locality": "Kukatpally",
        "location": {"type": "Point", "coordinates": [78.4138, 17.4849]},
        "is_verified_identity": True
    },
    {
        "name": "Kumar Swamy",
        "business_name": "Swamy Home Services",
        "category": "Plumbing",
        "skills": ["Bathroom fittings", "Water heater leak", "Basin repair"],
        "rating": 4.6,
        "total_reviews": 84,
        "completed_jobs": 90,
        "verified_jobs": 82,
        "repeat_customers_pct": 35,
        "avg_response_mins": 11,
        "distance_km": 1.4,
        "eta_mins": 12,
        "estimated_price_range": "₹150 – ₹250",
        "languages": ["Telugu", "Hindi"],
        "availability_status": "AVAILABLE",
        "locality": "Kukatpally",
        "location": {"type": "Point", "coordinates": [78.4145, 17.4855]},
        "is_verified_identity": True
    },
    {
        "name": "Srinivas Rao",
        "business_name": "Apex Electrical Solutions",
        "category": "Electrical",
        "skills": ["MCB repair", "Wiring setup", "Ceiling fan fitting"],
        "rating": 4.9,
        "total_reviews": 156,
        "completed_jobs": 165,
        "verified_jobs": 150,
        "repeat_customers_pct": 48,
        "avg_response_mins": 5,
        "distance_km": 1.1,
        "eta_mins": 9,
        "estimated_price_range": "₹200 – ₹400",
        "languages": ["Telugu", "English"],
        "availability_status": "AVAILABLE",
        "locality": "KPHB Colony",
        "location": {"type": "Point", "coordinates": [78.3992, 17.4933]},
        "is_verified_identity": True
    }
]

async def seed_database():
    settings = get_settings()
    logger.info(f"Seeding database at {settings.MONGODB_URI}...")
    client = AsyncIOMotorClient(settings.MONGODB_URI)
    db = client[settings.DB_NAME]

    # Re-create 2DSphere spatial index
    await db["provider_locations"].create_index([("location", GEOSPHERE)])
    
    # Clear old seeded providers
    await db["provider_locations"].delete_many({})
    
    # Insert demo providers
    result = await db["provider_locations"].insert_many(DEMO_PROVIDERS_HYDERABAD)
    logger.info(f"Successfully seeded {len(result.inserted_ids)} Hyderabad providers into database!")
    client.close()

if __name__ == "__main__":
    asyncio.run(seed_database())

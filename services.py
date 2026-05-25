from ingestion.models import RawRecord
from .models import NormalizedEmissionRecord


EMISSION_FACTORS = {
    'diesel_liters': 2.68,
    'electricity_kwh': 0.82,
    'flight_km': 0.115,
}


def normalize_sap_record(raw_record):
    payload = raw_record.raw_payload

    liters = float(payload.get('fuel_quantity', 0))

    emissions = liters * EMISSION_FACTORS['diesel_liters']

    suspicious = liters > 10000

    return NormalizedEmissionRecord.objects.create(
        company=raw_record.datasource.company,
        scope='1',
        category='Fuel',
        activity_type='Diesel',
        activity_value=liters,
        normalized_unit='liters',
        emissions_kg_co2e=emissions,
        suspicious_flag=suspicious,
        raw_record=raw_record
    )
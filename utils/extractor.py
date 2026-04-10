import json

def extract_shipment(llm, docs):
    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
    Extract the following fields from the document:

    shipment_id, shipper, consignee, pickup_datetime,
    delivery_datetime, equipment_type, mode, rate,
    currency, weight, carrier_name

    Return JSON. Use null if missing.

    Document:
    {context}
    """

    response = llm(prompt)

    try:
        return json.loads(response)
    except:
        return {"error": "Invalid JSON"}
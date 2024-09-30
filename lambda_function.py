import os
from PIL import Image
import json
import io
import base64

def lambda_handler(event, context):
    try:
        # Decode the base64 image data from the event
        image_data = base64.b64decode(event['image_data'])
        image = Image.open(io.BytesIO(image_data))
        
        # Use environment variable for default mode if not specified
        mode = os.getenv('DEFAULT_MODE', image.mode)
        
        # Extract image metadata
        metadata = {
            "format": image.format,
            "size": image.size,
            "mode": mode,
            "info": image.info
        }
        
        return {
            'statusCode': 200,
            'body': json.dumps(metadata)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }

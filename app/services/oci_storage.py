import oci
import requests
from datetime import datetime, timedelta, timezone
from app.config import Config
from oci.config import from_file

config = {
    "user": Config.OCI_USER,
    "key_content": Config.OCI_KEY_CONTENT,
    "fingerprint": Config.OCI_FINGERPRINT,
    "tenancy": Config.OCI_TENANCY,
    "region": Config.OCI_REGION
}

object_storage_client = oci.object_storage.ObjectStorageClient(config)


def upload_img_with_par(file_buffer, content_type, object_name):
    par_url = Config.OCI_WRITE_PAR_URL

    request_url = f'{par_url}/{object_name}'

    response = requests.put(
        request_url,
        data=file_buffer,
        headers={'ContentType': content_type}
    )

    response.raise_for_status()

    return object_name

def get_img_with_par(object_name):
    par_url = Config.OCI_READ_PAR_URL

    request_url = f'{par_url}/{object_name}'

    response = requests.get(
        request_url
    )

    response.raise_for_status()

    return response.content

def delete_img_from_oci(object_name):
    namespace = object_storage_client.get_namespace().data
    bucket = Config.OCI_BUCKET_NAME
    object_storage_client.delete_object(
        namespace_name=namespace,
        bucket_name=bucket, 
        object_name=object_name
    )

    return 'image deleted from object storage'
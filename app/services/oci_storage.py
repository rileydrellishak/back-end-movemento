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
    # bucket = object_storage_client.get_bucket(
    #     namespace_name=Config.OCI_NAMESPACE,
    #     bucket_name=Config.OCI_BUCKET_NAME
    # )

    par_details = oci.object_storage.models.CreatePreauthenticatedRequestDetails(
        name=f'upload-entry-{object_name}',
        access_type='ObjectWrite',
        object_name=object_name,
        time_expires=datetime.now(timezone.utc) + timedelta(minutes=Config.OCI_PAR_EXPIRATION_MINUTES)
    )

    par = object_storage_client.create_preauthenticated_request(
        namespace_name=object_storage_client.get_namespace().data,
        bucket_name=Config.OCI_BUCKET_NAME,
        create_preauthenticated_request_details=par_details
    )

    par_url = f'https://objectstorage.{Config.OCI_REGION}.oraclecloud.com{par.data.access_uri}'

    response = requests.put(
        par_url,
        data=file_buffer,
        headers={'ContentType': content_type}
    )

    response.raise_for_status()

    return (
        f'https://objectstorage.{Config.OCI_REGION}.oraclecloud.com/n/{Config.OCI_NAMESPACE}/b/{Config.OCI_BUCKET_NAME}/o/{object_name}'
    )
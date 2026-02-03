import oci
import requests
from datetime import datetime, timedelta
from app.config import (
    OCI_REGION,
    OCI_NAMESPACE,
    OCI_BUCKET_NAME,
    OCI_PAR_EXPIRATION_MINUTES,
)

config = oci.config.from_file()

object_storage_client = oci.object_storage.ObjectStorageClient(config)


def upload_img_with_par(file_buffer, content_type, object_name):
    par_details = oci.object_storage.models.CreatePreauthenticatedRequestDetails(
        name=f'upload-entry-{object_name}',
        access_type='ObjectWrite',
        object_name=object_name,
        time_expires=datetime.now() + timedelta(minutes=OCI_PAR_EXPIRATION_MINUTES)
    )

    par = object_storage_client.create_preauthenticated_request(
        namespace_name=OCI_NAMESPACE,
        bucket_name=OCI_BUCKET_NAME,
        create_preauthenticated_request_details=par_details
    )

    par_url = f'https://objectstorage.{OCI_REGION}.oraclecloud.com{par.data.access_uri}'

    response = requests.put(
        par_url,
        data=file_buffer,
        headers={'ContentType': content_type}
    )

    response.raise_for_status()

    return (
        f'https://objectstorage.{OCI_REGION}.oraclecloud.com/n/{OCI_NAMESPACE}/b/{OCI_BUCKET_NAME}/o/{object_name}'
    )
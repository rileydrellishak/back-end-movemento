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
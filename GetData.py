import nasdaqdatalink
import boto3


class NasdaqToS3:
    def __init__(self, country_code):
        self.country_code = country_code
        self.file_path = ""
        self.bucket_name = "jrosiak-upload-test-bucket"

    def download_data(self):
        # For security purposes, API key is stored in a file which is added to .gitignore
        nasdaqdatalink.read_key(filename="../data/.corporatenasdaqdatalinkapikey")
        data = nasdaqdatalink.get(f"ECONOMIST/BIGMAC_{self.country_code}")

        filepath = f"data/BIGMAC_{self.country_code}.csv"
        data.to_csv(filepath)
        self.file_path = filepath

    def upload_data_to_s3(self):
        # AWS credentials are configured via AWC cli to avoid storing any credentials in repository
        s3 = boto3.client("s3")

        s3.upload_file(
            Filename=self.file_path,
            Bucket=self.bucket_name,
            Key=f"BIGMAC_{self.country_code}.csv",
        )


sample_upload = NasdaqToS3("USA")
sample_upload.download_data()
sample_upload.upload_data_to_s3()

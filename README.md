# ProjectOnwelo

Project for downloading data from Nasdaq Data Link and uploading it to AWS S3 bucket.

### Usage

Define instance of the class using 3 letter code for country of interest

```Python
data_class = NasdaqToS3("USA")
```

Download selected data

```Python
data_class.download_data()
```

Upload saved data to S3 bucket

```Python
data_class.upload_data_to_s3()
```

### Notes

1) Nasdaq API key is stored in a file which is ignored by git to avoid storing sensitive data in repository.
2) AWS credentials are configured using AWS cli for the same reason as above (could also be stored in a file).
3) Class could be developed to take into account user input (for example dictionary with country codes) or data download parameters (date range, columns etc), however they were not needed for the purpose of this project and thus not implemented.
import dropbox
import os
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        #1.Usage of os.walk
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path=os.path.join(root,filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = '9PqncgcsI1QAAAAAAAAAAcd44H_wyfFJJj5rRXRx_95niNUDclP-rQuBe9kRej-V'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer:")
    file_to = input("Enter the full path to upload to dropbox:")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been moved.")

#if __name__ == '__main__':
main()
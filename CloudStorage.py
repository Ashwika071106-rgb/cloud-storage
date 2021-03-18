import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_files(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
        
def main():
    access_token = '85wzTjuDVBwAAAAAAAAAAQmWmhyGrn6ovC77rlJXVOVfwU4Kuij-vP132Pnzmmz-'
    transferData = TransferData(access_token)
    file_from = input("Enter the file path to transfer : ")
    #this is the full path to upload the file to including the name that you wish the file to becalled once uploaded
    file_to = input("Enter the full path to upload to dropbox : ")

    transferData.upload_files(file_from,file_to)
    print("File has been moved")

main()
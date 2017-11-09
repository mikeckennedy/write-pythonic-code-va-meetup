class SocketError(object):
    pass

class DownloadService:
    def check_download_url(self):
        pass

    def check_access_allowed(self):
        pass

    def check_network(self):
        pass

    def download_file(self):
        pass


def save_file(_):
    pass


# LBYL
# 1. create DownloadService
# 2. test conditions
# 3. download
# 4. save
def some_method():
    svr = DownloadService()
    if not svr.check_access_allowed():
        print("Oh no access!")
        return
    if not svr.check_download_url():
        print("Oh no url!")
        return
    if not svr.check_network():
        print("Oh no network!")
        return

    file = svr.download_file()
    save_file(file)

# EAFF
# try to leap, differentiate via exceptions
try:
    svr = DownloadService()
    file = svr.download_file()
    save_file(file)
except SocketError as se:
    print(f"No network, check the wifi: {se}")
except Exception as x:
    print(f"Sorry, that wasn't good: {x}")

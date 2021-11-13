# Storage

# 套件
from google.cloud import storage

# 建立客戶端
storage_client = storage.Client()


def upload(storage, targetitem, rename):
    # 指定桶子
    bucket = storage_client.bucket(storage)

    # 指定桶內物件
    blob = bucket.blob(targetitem)

    # 本地檔案上傳
    blob.upload_from_filename(rename)

def download(storage, targetitem, rename):
    bucket = storage_client.bucket(storage)
    blob = bucket.blob(targetitem)
    blob.download_to_filename(rename)

def remove(storage, filename):
    
    bucket = storage_client.bucket(storage)
    # 指定物件名子
    blob = bucket.blob(filename)
    blob.delete()
    
    

# Firestore

from google.cloud import firestore
import json
# 啟用客戶端
db = firestore.Client()

# 獲 得 資 料

# 指定要操作的 表格 及 資料 
doc_ref = db.collection(u'cxcx-user').document(u'Ada')
doc = doc_ref.get()
if doc.exists:
    print(f'Document data: {doc.to_dict()}')
    with open('doc.txt','w') as f:
        # 文字 -> dict -> json
        f.write(json.dumps(doc.to_dict()))
else:
    print(u'No such document!')
    
    
    
    
# 增 加 資 料

doc_ref = db.collection(u'cxcx-user').document(u'Ada')

# 對那個key，增加資料
doc_ref.set({
     u'first': u'Ada',
     u'last': u'Lovelace',
     u'born': 1815
})
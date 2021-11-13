
# 建立連接資料庫
# storag 儲存圖片
# firestore 儲存文字

from google.cloud import storage
from google.cloud import firestore


# 取個資
line_user_profile= line_bot_api.get_profile(event.source.user_id)

# 跟line 取回照片，並放置在本地端
file_name = line_user_profile.user_id+'.jpg'
# 載到本地
urllib.request.urlretrieve(line_user_profile.picture_url, file_name)

# 設定內容
# 設定要存取的bucket
storage_client = storage.Client()
# 桶子˙
bucket_name="ai-class-python"
# 放哪
destination_blob_name=f"{line_user_profile.user_id}/user.png"
# 本地
source_file_name=file_name

# 進行上傳
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(source_file_name)










# 設定用戶資料json
user_dict={
        "user_id":line_user_profile.user_id,
        "picture_url": f"https://storage.googleapis.com/{bucket_name}/{destination_blob_name}",
        "display_name": line_user_profile.display_name,
        "status_message": line_user_profile.status_message
}



# 插入firestore
db = firestore.Client()
doc_ref = db.collection(u'line-user').document(user_dict.get("user_id"))
doc_ref.set(user_dict)
line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text="取個茲拉"))
    
  
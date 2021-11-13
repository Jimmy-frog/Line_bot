
@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):

    # 取出照片
    # event.message.id 照片編號
    image_blob = line_bot_api.get_message_content(event.message.id)
    temp_file_path=f"""{event.message.id}.png"""

    with open(temp_file_path, 'wb') as fd:
        for chunk in image_blob.iter_content():
            fd.write(chunk)

    # 上傳至cloud storage
    storage_client = storage.Client()
    bucket_name = "ai-class-python"
    destination_blob_name = f'{event.source.user_id}/image/{event.message.id}.png'
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(temp_file_path)
import pika, json

def upload(f, fs, channel, access):
    """
    Steps
    1. Upload the file to mongodb using gridfs
    2. After uploading, Put the message in the rabbitmq(channel) saying that file can be processed to convert to mp3 
    """
    try:
        fileid = fs.put(f)
    except Exception as err:
        return "internal server error", 500

    message = {
        "video_fid": str(fileid),
        "mp3_fid": None,
        "Username": access["username"]
    }

    try:
        channel.basic_publish(
            exchange = "",
            routing_key = "video",
            body = json.dumps(message),
            properties = pika.BasicProperties(
                delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
    except:
        #delete file from mongodb if message is not sent to rabbitmq
        fs.delete(fileid)
        return "internal server error", 500
    return None
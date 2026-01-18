def filter_messages(messages):
    msg_filtered = []
    dang_count = []

    for message in messages:
        words = message.split()
        good_words = []
        dangs_bucket = []

        for word in words:
            if word == "dang":
                dangs_bucket.append(word)
            else:
                good_words.append(word)

        new_message = " ".join(good_words)
        msg_filtered.append(new_message)
        dang_count.append(len(dangs_bucket))

    return msg_filtered, dang_count